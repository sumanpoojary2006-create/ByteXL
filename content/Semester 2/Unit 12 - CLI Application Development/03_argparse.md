## Introduction

Priya's `import_books.py` script needs three things `sys.argv` makes difficult: optional arguments with defaults, a `--help` flag that explains how to use the tool, and automatic type conversion (the `--limit` option should be an integer, not a string). `argparse` provides all of these in about ten lines.

![An argparse-powered command shown with --help output: usage line, positional arguments, optional arguments with types and defaults, all automatically generated from the parser definition](images/03_argparse.png)

## Basic argparse Structure

```python
import argparse

parser = argparse.ArgumentParser(
    description="Import books into the library catalog"
)
parser.add_argument("file", help="CSV file to import")
parser.add_argument("--branch", default="main", help="Target branch (default: main)")
parser.add_argument("--limit", type=int, default=None, help="Maximum records to import")
parser.add_argument("--dry-run", action="store_true", help="Validate only, do not import")

# Pass args explicitly so this runs without a real command line
args = parser.parse_args(["catalog.csv", "--branch", "east", "--limit", "100", "--dry-run"])
print(f"File:     {args.file}")
print(f"Branch:   {args.branch}")
print(f"Limit:    {args.limit}")
print(f"Dry run:  {args.dry_run}")
```

Running:
```console
python import_books.py catalog.csv --branch east --limit 100 --dry-run
# File:     catalog.csv
# Branch:   east
# Limit:    100
# Dry run:  True

python import_books.py --help
# usage: import_books.py [-h] [--branch BRANCH] [--limit LIMIT] [--dry-run] file
# Import books into the library catalog
# positional arguments:
#   file           CSV file to import
# options:
#   ...
```

## Argument Types

`argparse` converts arguments to the specified type, raising a clean error if conversion fails:

```python
import argparse

parser = argparse.ArgumentParser(description="Book import tool")
parser.add_argument("file", help="CSV file to import")
parser.add_argument("--limit", type=int, help="Max records")        # integer
parser.add_argument("--rate", type=float, default=1.0)             # float
parser.add_argument("--date", type=str, default="2026-01-01")      # string
parser.add_argument("--verbose", "-v", action="store_true")        # short -v flag
parser.add_argument("--format", choices=["csv", "json", "text"],   # restrict choices
                    default="text")

args = parser.parse_args(["books.csv", "--limit", "50", "-v", "--format", "json"])
print(f"limit={args.limit} (type: {type(args.limit).__name__})")
print(f"rate={args.rate}   (type: {type(args.rate).__name__})")
print(f"verbose={args.verbose}")
print(f"format={args.format}")
```

```console
python import_books.py catalog.csv --limit abc
# error: argument --limit: invalid int value: 'abc'
```

Argparse shows the error message and exits with code 2 automatically.

## Subcommands

Many CLIs have subcommands (`git commit`, `git push`). `argparse` supports this with subparsers:

```python
import argparse

def cmd_import(args):
    print(f"Importing {args.file} into branch '{args.branch}'")

def cmd_export(args):
    print(f"Exporting catalog to {args.output}")

parser = argparse.ArgumentParser(prog="library-cli")
subparsers = parser.add_subparsers(dest="command", required=True)

# Sub-command: import
p_import = subparsers.add_parser("import", help="Import books from CSV")
p_import.add_argument("file")
p_import.add_argument("--branch", default="main")
p_import.set_defaults(func=cmd_import)

# Sub-command: export
p_export = subparsers.add_parser("export", help="Export catalog to file")
p_export.add_argument("--output", required=True)
p_export.set_defaults(func=cmd_export)

# Demo: simulate running both sub-commands
for demo_args in [
    ["import", "catalog.csv", "--branch", "east"],
    ["export", "--output", "catalog.json"],
]:
    args = parser.parse_args(demo_args)
    args.func(args)   # call the function set by set_defaults
```

Running:
```console
python library_cli.py import catalog.csv --branch east
# Importing catalog.csv into east

python library_cli.py --help
# usage: library-cli [-h] {import,export} ...
```

## Mutually Exclusive Arguments

```python
import argparse

parser = argparse.ArgumentParser(description="Library report tool")
parser.add_argument("report", help="Report name")
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose", action="store_true", help="Show full detail")
group.add_argument("--quiet", action="store_true", help="Suppress output")

# Demo: --verbose is set, --quiet is not
args = parser.parse_args(["catalog", "--verbose"])
print(f"verbose={args.verbose}, quiet={args.quiet}")

# Demo: --quiet is set, --verbose is not
args = parser.parse_args(["catalog", "--quiet"])
print(f"verbose={args.verbose}, quiet={args.quiet}")

# Trying to pass both would raise SystemExit (argparse handles it automatically)
print("Passing --verbose and --quiet together would print an error and exit.")
```

## argparse at a Glance

| Feature | How to use |
|---|---|
| Positional arg | `add_argument("name")` |
| Optional arg | `add_argument("--name")` |
| Type conversion | `add_argument("--n", type=int)` |
| Default value | `add_argument("--n", default=10)` |
| Flag (boolean) | `add_argument("--flag", action="store_true")` |
| Restricted choices | `add_argument("--fmt", choices=["csv","json"])` |
| Subcommands | `subparsers = parser.add_subparsers(...)` |

## Your Turn

Build a `report.py` CLI with two subcommands: `daily` (requires `--date`) and `monthly` (requires `--month`, `--year`). Each prints a summary of what it would generate:

```python
import argparse

def daily_report(args):
    print(f"Daily report for: {args.date}")

def monthly_report(args):
    print(f"Monthly report for: {args.year}-{args.month:02d}")

parser = argparse.ArgumentParser(prog="report")
subs = parser.add_subparsers(dest="command", required=True)

p_daily = subs.add_parser("daily")
p_daily.add_argument("--date", required=True, help="Date (YYYY-MM-DD)")
p_daily.set_defaults(func=daily_report)

p_monthly = subs.add_parser("monthly")
p_monthly.add_argument("--month", type=int, required=True)
p_monthly.add_argument("--year", type=int, required=True)
p_monthly.set_defaults(func=monthly_report)

# Test both sub-commands
args = parser.parse_args(["daily", "--date", "2026-07-01"])
args.func(args)

args = parser.parse_args(["monthly", "--month", "7", "--year", "2026"])
args.func(args)
```

Test: `python report.py daily --date 2026-07-01` and `python report.py monthly --month 7 --year 2026`.

## Conclusion

`argparse` provides structured argument parsing: types, defaults, help text, choices, and subcommands, all with automatic `--help` and error messages. It is the standard library choice for most CLI tools. The next lesson introduces `typer`, a third-party library that achieves the same thing with even less code by using Python type annotations.
