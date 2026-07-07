## Introduction

Priya built a web interface for the library catalog, but the librarians at the consortium's seven branches use it only for patron-facing tasks. For their own daily work -- bulk importing books, running end-of-day reports, exporting overdue lists -- they prefer the terminal. They run commands in scripts, pipe output to files, and chain tools together. A web form requires a browser, a mouse, and a slow page load for every operation.

Priya's team lead asks her to build CLI tools: command-line programs that librarians can run directly, script in cron jobs, and compose with shell utilities like `grep` and `sort`. This unit covers the tools Python provides.

![A terminal showing three commands piped together: a library CLI generating a list of overdue books, piped through grep to filter by branch, piped through sort to order by days overdue](images/01_why_clis.png)

## What a CLI Is

A command-line interface (CLI) is a program that:

- Accepts arguments and options from the command line
- Reads from stdin and writes to stdout / stderr
- Exits with a status code (0 for success, non-zero for failure)
- Composes with other tools via pipes

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3doeV9jbGlzIGNvZGUgMSIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDEuc2giLCJjb2RlIjoiIyBBIHR5cGljYWwgbGlicmFyeSBDTEkgd29ya2Zsb3c6XG5saWJyYXJ5LWNsaSBleHBvcnQtb3ZlcmR1ZSAtLWJyYW5jaCBtYWluIC0tZm9ybWF0IGNzdiA-IG92ZXJkdWUuY3N2XG5saWJyYXJ5LWNsaSBub3RpZnktcGF0cm9ucyAtLWlucHV0IG92ZXJkdWUuY3N2IC0tdGVtcGxhdGUgZW1haWxcbmxpYnJhcnktY2xpIHJlcG9ydCBkYWlseSAtLWRhdGUgMjAyNi0wNy0wMSB8IGdyZXAgXCJsYXRlIHJldHVyblwiIn0"
 width="100%"
></iframe>

Each command is focused, accepts clear arguments, and its output can be piped or redirected.

## Why CLIs Over Web UIs for Operations Tasks

| Task | Web UI | CLI |
|---|---|---|
| Bulk import 2,000 books | Slow: form per batch | Fast: `library-cli import books.csv` |
| Filter overdue by criteria | Requires navigation | `library-cli overdue | grep "branch=main"` |
| Automation / cron scheduling | Not composable | `0 8 * * * library-cli report daily` |
| SSH into a remote server | Requires browser | Works natively |
| Pipe output to another tool | Not possible | `library-cli export | sort | head -20` |

## Three Layers of Python CLI Tools

Python provides three layers of increasing abstraction for building CLIs:

| Tool | When to use |
|---|---|
| `sys.argv` | Read raw arguments manually; trivial scripts only |
| `argparse` | Standard library; robust argument parsing for most tools |
| `typer` | Third-party; clean, type-annotated, minimal boilerplate |

The rest of this unit covers all three, from simplest to most powerful, so you understand what each layer is doing.

## The Unix Philosophy

Well-designed CLIs follow the Unix philosophy:
- **Do one thing well**: each command has a clear, narrow purpose
- **Write to stdout**: output can be redirected or piped
- **Write errors to stderr**: errors go to a separate stream, not mixed with output
- **Exit codes**: 0 means success; non-zero means failure

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3doeV9jbGlzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgc3lzXG5cbiMgR29vZDogb3V0cHV0IGdvZXMgdG8gc3Rkb3V0LCBlcnJvciBnb2VzIHRvIHN0ZGVyclxuaWYgbm90IGZvdW5kOlxuICAgIHByaW50KFwiRXJyb3I6IGJvb2sgbm90IGZvdW5kXCIsIGZpbGU9c3lzLnN0ZGVycilcbiAgICBzeXMuZXhpdCgxKSAgICMgbm9uLXplcm86IGZhaWx1cmVcblxucHJpbnQoYm9vay50aXRsZSkgICAjIHN0ZG91dDogZ29lcyB0byBuZXh0IHBpcGUgc3RhZ2VcbnN5cy5leGl0KDApICAgICAgICAgIyAwOiBzdWNjZXNzIn0"
 width="100%"
></iframe>

## CLIs at a Glance

| Concept | What it means |
|---|---|
| Arguments | Positional values (`library-cli import books.csv`) |
| Options / flags | Named values (`--branch main`, `-v`) |
| stdin / stdout | Input/output streams for piping |
| stderr | Error stream (separate from output) |
| Exit code | 0 = success, 1+ = failure |

## Your Turn

Think of three operations in your library system that would work better as CLI commands than as web forms. For each:
1. Name the command (`library-cli <command>`)
2. List the arguments and options it would accept
3. Describe what it writes to stdout and what success/failure looks like

Example:
<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3doeV9jbGlzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJDb21tYW5kOiBsaWJyYXJ5LWNsaSBvdmVyZHVlXG5Bcmd1bWVudHM6IG5vbmVcbk9wdGlvbnM6IC0tYnJhbmNoIFRFWFQsIC0tZm9ybWF0IFtjc3Z8anNvbnx0ZXh0XVxuU3Rkb3V0OiBsaXN0IG9mIG92ZXJkdWUgcmVjb3JkcyBpbiB0aGUgcmVxdWVzdGVkIGZvcm1hdFxuU3VjY2VzczogZXhpdCAwLCBvdXRwdXQgd3JpdHRlblxuRmFpbHVyZTogZXhpdCAxLCBlcnJvciBtZXNzYWdlIG9uIHN0ZGVyciJ9"
 width="100%"
></iframe>

## Conclusion

CLIs are the right tool for operational tasks: batch imports, automated reports, system administration. They compose with shell tools, work in scripts and cron jobs, and do not require a browser. Python provides `sys.argv` for raw argument access, `argparse` from the standard library for structured parsing, and `typer` for the cleanest, most modern API. The next lesson shows how `sys.argv` works before abstracting to higher layers.
