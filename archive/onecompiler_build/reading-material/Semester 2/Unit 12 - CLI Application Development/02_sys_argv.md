## Introduction

Priya's simplest CLI tool needs to accept one argument: a file path. Before using `argparse`, she wants to understand how Python receives command-line arguments at the lowest level: `sys.argv`. This foundation makes everything in the higher-level tools more intuitive.

![sys.argv shown as a list with index 0 being the script name and indices 1+ being the command-line arguments in order](images/02_sys_argv.png)

## What sys.argv Contains

When Python runs a script, `sys.argv` is a list of strings. The first element (`sys.argv[0]`) is the script name. Every subsequent element is a command-line argument.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N5c19hcmd2IGNvZGUgMSIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDEuc2giLCJjb2RlIjoicHl0aG9uIGltcG9ydF9ib29rcy5weSBjYXRhbG9nLmNzdiAtLWJyYW5jaCBtYWluIC0tZHJ5LXJ1biJ9"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N5c19hcmd2IGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgc3lzXG5wcmludChzeXMuYXJndilcbiMgWydpbXBvcnRfYm9va3MucHknLCAnY2F0YWxvZy5jc3YnLCAnLS1icmFuY2gnLCAnbWFpbicsICctLWRyeS1ydW4nXSJ9"
 width="100%"
></iframe>

Every argument is a string, even numbers. Converting types is the developer's responsibility.

## Reading Arguments Directly

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N5c19hcmd2IGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiIjIGltcG9ydF9ib29rcy5weVxuaW1wb3J0IHN5c1xuXG5pZiBsZW4oc3lzLmFyZ3YpIDwgMjpcbiAgICBwcmludChcIlVzYWdlOiBpbXBvcnRfYm9va3MucHkgPGNhdGFsb2dfZmlsZT5cIiwgZmlsZT1zeXMuc3RkZXJyKVxuICAgIHN5cy5leGl0KDEpXG5cbmNhdGFsb2dfZmlsZSA9IHN5cy5hcmd2WzFdXG5wcmludChmXCJJbXBvcnRpbmcgZnJvbToge2NhdGFsb2dfZmlsZX1cIikifQ"
 width="100%"
></iframe>

Running:
<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N5c19hcmd2IGNvZGUgNCIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDQuc2giLCJjb2RlIjoicHl0aG9uIGltcG9ydF9ib29rcy5weSBjYXRhbG9nLmNzdlxuIyBJbXBvcnRpbmcgZnJvbTogY2F0YWxvZy5jc3ZcblxucHl0aG9uIGltcG9ydF9ib29rcy5weVxuIyBVc2FnZTogaW1wb3J0X2Jvb2tzLnB5IDxjYXRhbG9nX2ZpbGU-XG4jIChleGl0cyB3aXRoIGNvZGUgMSkifQ"
 width="100%"
></iframe>

## Parsing Multiple Arguments Manually

For more arguments, manual parsing becomes fragile but illustrates what argparse does under the hood:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N5c19hcmd2IGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgc3lzXG5cbmRlZiBwYXJzZV9hcmdzKGFyZ3YpOlxuICAgIGFyZ3MgPSB7XCJmaWxlXCI6IE5vbmUsIFwiYnJhbmNoXCI6IFwiYWxsXCIsIFwiZHJ5X3J1blwiOiBGYWxzZX1cblxuICAgIGkgPSAxXG4gICAgd2hpbGUgaSA8IGxlbihhcmd2KTpcbiAgICAgICAgaWYgYXJndltpXSA9PSBcIi0tYnJhbmNoXCI6XG4gICAgICAgICAgICBpICs9IDFcbiAgICAgICAgICAgIGFyZ3NbXCJicmFuY2hcIl0gPSBhcmd2W2ldXG4gICAgICAgIGVsaWYgYXJndltpXSA9PSBcIi0tZHJ5LXJ1blwiOlxuICAgICAgICAgICAgYXJnc1tcImRyeV9ydW5cIl0gPSBUcnVlXG4gICAgICAgIGVsaWYgbm90IGFyZ3ZbaV0uc3RhcnRzd2l0aChcIi0tXCIpOlxuICAgICAgICAgICAgYXJnc1tcImZpbGVcIl0gPSBhcmd2W2ldXG4gICAgICAgIGkgKz0gMVxuICAgIHJldHVybiBhcmdzXG5cbnBhcnNlZCA9IHBhcnNlX2FyZ3Moc3lzLmFyZ3YpXG5wcmludChwYXJzZWQpXG4jIHsnZmlsZSc6ICdjYXRhbG9nLmNzdicsICdicmFuY2gnOiAnbWFpbicsICdkcnlfcnVuJzogVHJ1ZX0ifQ"
 width="100%"
></iframe>

This is essentially what `argparse` does, but with all the edge cases handled automatically.

## When sys.argv Is Enough

`sys.argv` is appropriate for:
- One-off scripts with at most one or two arguments
- Scripts where the arguments are always positional and never optional
- Simple utility functions used only internally

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N5c19hcmd2IGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiIjIGNsZWFudXBfdGVtcC5weSAtLSB0YWtlcyBleGFjdGx5IG9uZSBkaXJlY3RvcnlcbmltcG9ydCBzeXMsIHNodXRpbFxuXG5pZiBsZW4oc3lzLmFyZ3YpICE9IDI6XG4gICAgcHJpbnQoZlwiVXNhZ2U6IHtzeXMuYXJndlswXX0gPGRpcmVjdG9yeT5cIiwgZmlsZT1zeXMuc3RkZXJyKVxuICAgIHN5cy5leGl0KDEpXG5cbnNodXRpbC5ybXRyZWUoc3lzLmFyZ3ZbMV0pXG5wcmludChmXCJSZW1vdmVkOiB7c3lzLmFyZ3ZbMV19XCIpIn0"
 width="100%"
></iframe>

For anything more complex -- optional flags, types other than strings, help text, default values -- use `argparse` or `typer`.

## sys.argv at a Glance

| Item | Value |
|---|---|
| `sys.argv[0]` | The script name |
| `sys.argv[1]` | First argument |
| `sys.argv[1:]` | All arguments (excludes script name) |
| `len(sys.argv)` | Total items including script name |
| All values | Strings (even if they look like numbers) |

## Your Turn

Write a `word_count.py` script that accepts a filename as `sys.argv[1]` and prints the number of lines, words, and characters in the file, matching the behavior of the Unix `wc` command:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3N5c19hcmd2IGNvZGUgNyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNy5weSIsImNvZGUiOiJpbXBvcnQgc3lzXG5cbmRlZiB3b3JkX2NvdW50KHBhdGgpOlxuICAgIHdpdGggb3BlbihwYXRoKSBhcyBmOlxuICAgICAgICB0ZXh0ID0gZi5yZWFkKClcbiAgICBsaW5lcyA9IHRleHQuY291bnQoXCJcXG5cIilcbiAgICB3b3JkcyA9IGxlbih0ZXh0LnNwbGl0KCkpXG4gICAgY2hhcnMgPSBsZW4odGV4dClcbiAgICBwcmludChmXCJ7bGluZXM6OH0ge3dvcmRzOjh9IHtjaGFyczo4fSB7cGF0aH1cIilcblxuaWYgbGVuKHN5cy5hcmd2KSAhPSAyOlxuICAgIHByaW50KGZcIlVzYWdlOiB7c3lzLmFyZ3ZbMF19IDxmaWxlPlwiLCBmaWxlPXN5cy5zdGRlcnIpXG4gICAgc3lzLmV4aXQoMSlcblxud29yZF9jb3VudChzeXMuYXJndlsxXSkifQ"
 width="100%"
></iframe>

Run it on a text file, then run the real `wc` command on the same file and compare the output.

## Conclusion

`sys.argv` is a list of strings containing the script name and all command-line arguments. It provides direct, unmediated access to what the user typed. For anything beyond one or two positional arguments, the manual parsing it requires becomes error-prone. The next lesson introduces `argparse`, the standard library's structured argument parser.
