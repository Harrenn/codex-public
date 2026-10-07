#!/usr/bin/env python3
"""Minimal, dependency-free client for safe Transmission RPC operations."""

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


DEFAULT_RPC = "http://127.0.0.1:9091/transmission/rpc"
DOWNLOAD_DIR = str(Path.home() / "Documents" / "Torrents")
FIELDS = ["id", "name", "status", "percentDone", "rateDownload", "eta", "totalSize"]


class Transmission:
    def __init__(self, url, username=None, password=None):
        self.url = url
        self.session_id = None
        self.auth = None
        if username is not None:
            token = base64.b64encode(f"{username}:{password or ''}".encode()).decode()
            self.auth = f"Basic {token}"

    def call(self, method, arguments=None):
        payload = json.dumps({"method": method, "arguments": arguments or {}}).encode()
        for _ in range(2):
            headers = {"Content-Type": "application/json"}
            if self.session_id:
                headers["X-Transmission-Session-Id"] = self.session_id
            if self.auth:
                headers["Authorization"] = self.auth
            request = urllib.request.Request(self.url, data=payload, headers=headers)
            try:
                with urllib.request.urlopen(request, timeout=10) as response:
                    result = json.load(response)
                if result.get("result") != "success":
                    raise RuntimeError(result.get("result", "Unknown Transmission error"))
                return result.get("arguments", {})
            except urllib.error.HTTPError as exc:
                if exc.code == 409:
                    self.session_id = exc.headers.get("X-Transmission-Session-Id")
                    continue
                raise
        raise RuntimeError("Could not negotiate a Transmission RPC session")


def source_arguments(source):
    path = Path(source).expanduser()
    if path.is_file():
        if path.suffix.lower() != ".torrent":
            raise ValueError("Local source must be a .torrent file")
        return {"metainfo": base64.b64encode(path.read_bytes()).decode()}
    if source.startswith("magnet:?") or source.startswith("http://") or source.startswith("https://"):
        return {"filename": source}
    raise ValueError("Source must be a magnet URI, torrent URL, or local .torrent file")


def parser():
    result = argparse.ArgumentParser(description="Safe Transmission RPC client")
    result.add_argument("--rpc-url", default=DEFAULT_RPC)
    result.add_argument("--username")
    result.add_argument("--password-env", help="Environment variable containing the RPC password")
    commands = result.add_subparsers(dest="command", required=True)
    commands.add_parser("status")
    commands.add_parser("list")
    add = commands.add_parser("add")
    add.add_argument("--source", required=True)
    add.add_argument("--paused", action="store_true")
    add.add_argument("--confirm", action="store_true")
    return result


def main():
    args = parser().parse_args()
    password = os.environ.get(args.password_env, "") if args.password_env else None
    client = Transmission(args.rpc_url, args.username, password)
    if args.command == "status":
        data = client.call("session-get", {"fields": ["version", "download-dir", "rpc-version"]})
    elif args.command == "list":
        data = client.call("torrent-get", {"fields": FIELDS})
    else:
        if not args.confirm:
            raise RuntimeError("Refusing to add torrent without --confirm")
        arguments = source_arguments(args.source)
        arguments["paused"] = args.paused
        Path(DOWNLOAD_DIR).mkdir(parents=True, exist_ok=True)
        arguments["download-dir"] = DOWNLOAD_DIR
        data = client.call("torrent-add", arguments)
    print(json.dumps(data, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=True), file=sys.stderr)
        sys.exit(1)
