## Introduction

Priya's simplest CLI tool needs to accept one argument: a file path. Before using `argparse`, she wants to understand how Python receives command-line arguments at the lowest level: `sys.argv`. This foundation makes everything in the higher-level tools more intuitive.

![sys.argv shown as a list with index 0 being the script name and indices 1+ being the command-line arguments in order](images/02_sys_argv.png)

## What sys.argv Contains

When Python runs a script, `sys.argv` is a list of strings. The first element (`sys.argv[0]`) is the script name. Every subsequent element is a command-line argument.

```console
python import_books.py catalog.csv --branch main --dry-run
```

```python
import sys
print(sys.argv)
# ['import_books.py', 'catalog.csv', '--branch', 'main', '--dry-run']
```

Every argument is a string, even numbers. Converting types is the developer's responsibility.

## Reading Arguments Directly

```python
# import_books.py
import sys

if len(sys.argv) < 2:
    print("Usage: import_books.py <catalog_file>", file=sys.stderr)
    sys.exit(1)

catalog_file = sys.argv[1]
print(f"Importing from: {catalog_file}")
```

Running:
```console
python import_books.py catalog.csv
# Importing from: catalog.csv

python import_books.py
# Usage: import_books.py <catalog_file>
# (exits with code 1)
```

## Parsing Multiple Arguments Manually

For more arguments, manual parsing becomes fragile but illustrates what argparse does under the hood:

```python
import sys

def parse_args(argv):
    args = {"file": None, "branch": "all", "dry_run": False}

    i = 1
    while i < len(argv):
        if argv[i] == "--branch":
            i += 1
            args["branch"] = argv[i]
        elif argv[i] == "--dry-run":
            args["dry_run"] = True
        elif not argv[i].startswith("--"):
            args["file"] = argv[i]
        i += 1
    return args

parsed = parse_args(sys.argv)
print(parsed)
# {'file': 'catalog.csv', 'branch': 'main', 'dry_run': True}
```

This is essentially what `argparse` does, but with all the edge cases handled automatically.

## When sys.argv Is Enough

`sys.argv` is appropriate for:
- One-off scripts with at most one or two arguments
- Scripts where the arguments are always positional and never optional
- Simple utility functions used only internally

```python
# cleanup_temp.py -- takes exactly one directory
import sys, shutil

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <directory>", file=sys.stderr)
    sys.exit(1)

shutil.rmtree(sys.argv[1])
print(f"Removed: {sys.argv[1]}")
```

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

```python
import sys

def word_count(path):
    with open(path) as f:
        text = f.read()
    lines = text.count("\n")
    words = len(text.split())
    chars = len(text)
    print(f"{lines:8} {words:8} {chars:8} {path}")

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file>", file=sys.stderr)
    sys.exit(1)

word_count(sys.argv[1])
```

Run it on a text file, then run the real `wc` command on the same file and compare the output.

## Conclusion

`sys.argv` is a list of strings containing the script name and all command-line arguments. It provides direct, unmediated access to what the user typed. For anything beyond one or two positional arguments, the manual parsing it requires becomes error-prone. The next lesson introduces `argparse`, the standard library's structured argument parser.
