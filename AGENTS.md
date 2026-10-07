# Global working agreements

## Linux and WSL

- Use WSL whenever a task materially requires a Linux environment.
- Prefer WSL when the user identifies the work as a Linux task, asks to make a project runnable on Linux, or explicitly asks to run or work on the project in Linux.
- For such tasks, perform the relevant setup, build, test, and runtime verification inside WSL using the Linux filesystem conventions and toolchain where practical.
- Keep ordinary Windows-native work on Windows unless WSL is needed or provides a clear task-specific benefit.
