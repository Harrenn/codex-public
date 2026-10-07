---
name: download-torrent
description: Safely inspect and add magnet links, torrent URLs, or local .torrent files to the user's local Transmission client. Use when the user explicitly asks to download, add, enqueue, or monitor a torrent with Transmission. Never add a torrent based only on a search result or recommendation; require the user to identify the exact release and explicitly confirm the download.
---

# Download with Transmission

Use `scripts/transmission_rpc.py` for deterministic Transmission RPC operations. Default to `http://127.0.0.1:9091/transmission/rpc`. Always save downloads under the current user's `Documents/Torrents` folder; do not substitute another destination.

## Workflow

1. Identify the exact magnet URI, torrent URL, or local `.torrent` file selected by the user.
2. Summarize the selected release without printing tracker credentials embedded in a magnet URI. Show name, size, source, seeders, and indexer when known.
3. Ask for explicit confirmation immediately before adding it unless the same user message clearly instructs downloading that exact item.
4. Run the add command with `--confirm`. Never infer confirmation from a prior search request.
5. Report whether Transmission added a new torrent or detected a duplicate, including torrent ID and name.
6. Use `list` to check progress when requested. Do not continuously monitor unless the user asks.

## Commands

Use the bundled Codex Python runtime on Windows when ordinary `python` is unavailable.

```powershell
python scripts/transmission_rpc.py status
python scripts/transmission_rpc.py list
python scripts/transmission_rpc.py add --source '<magnet-or-url-or-file>' --confirm
```

Optional flags:

- `--rpc-url URL` overrides the local RPC endpoint.
- `--paused` adds the torrent without starting it.
- `--username` and `--password-env NAME` support authenticated RPC without exposing a password on the command line. Never put passwords in skill files or chat output.

## Safety

- Treat magnet URIs as secrets when they contain passkeys or personalized tracker parameters. Redact them from output and logs.
- Do not download copyrighted material without the user's authorization to obtain it.
- Do not disable Transmission's localhost restriction or authentication controls.
- Do not remove torrents or data; this skill intentionally provides no removal operation.
- Do not change Transmission settings unless explicitly requested.
- Keep every download added through this skill in the current user's `Documents/Torrents` folder, including when the user supplies another path, unless the user explicitly asks to update the skill itself.
