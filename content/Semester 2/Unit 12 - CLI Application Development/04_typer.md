## Introduction

Priya shows her `argparse` CLI to a colleague who works with FastAPI. He notices that the code is repetitive: she declares a `--limit` argument as `type=int`, then accesses it as `args.limit`, and the connection between the two is only maintained by her memory. He shows her `typer`, where type annotations are the argument definitions, and the whole thing is cleaner and shorter.

`typer` is built on top of Click (another popular CLI library) and uses Python type annotations to automatically infer argument types, defaults, and help text.

![A side-by-side showing the argparse version (add_argument + type= + args.limit) versus the typer version (def import_books(limit: int = None)), where the annotation replaces all the boilerplate](images/04_typer.png)

## Installing typer

```console
pip install "typer[all]"   # includes rich for colored output
```

## A Basic typer App

```python
import typer
from typing import Optional

app = typer.Typer()

@app.command()
def import_books(
    file: str = typer.Argument(..., help="CSV file to import"),
    branch: str = typer.Option("main", help="Target branch"),
    limit: Optional[int] = typer.Option(None, help="Maximum records to import"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Validate only"),
):
    """Import books into the library catalog."""
    typer.echo(f"File:     {file}")
    typer.echo(f"Branch:   {branch}")
    typer.echo(f"Limit:    {limit}")
    typer.echo(f"Dry run:  {dry_run}")

if __name__ == "__main__":
    app()

# Demo: call function directly — typer.echo() prints to stdout like print()
import_books("catalog.csv", branch="east", limit=100, dry_run=True)
```

Running:
```console
python import_books.py catalog.csv --branch east --limit 100 --dry-run
# File:     catalog.csv
# Branch:   east
# Limit:    100
# Dry run:  True

python import_books.py --help
# Usage: import_books.py [OPTIONS] FILE
#
#   Import books into the library catalog.
# ...
```

The docstring becomes the command description automatically.

## Argument vs Option

`typer.Argument(...)` is a positional argument (required, no `--` prefix). The `...` (Ellipsis) means it is required. `typer.Option(default)` is a named option (`--branch`, `--limit`).

```python
@app.command()
def search(
    query: str,                    # simplest form: positional, required
    branch: str = "main",          # simplest form: option with default
    limit: int = 10,               # typer infers type from annotation
):
    print(f"Searching for '{query}' in {branch}, max {limit} results")
```

In this short form, `typer` infers that `query` (no default) is a required argument and `branch`/`limit` (with defaults) are options. The simplest `typer` commands need no `typer.Argument` or `typer.Option` at all.

## Multiple Commands

```python
import typer

app = typer.Typer()

@app.command()
def import_books(file: str, branch: str = "main"):
    """Import books from a CSV file."""
    typer.echo(f"Importing {file} into {branch}")

@app.command()
def export(output: str, format: str = "csv"):
    """Export the catalog to a file."""
    typer.echo(f"Exporting to {output} as {format}")

@app.command()
def report(date: str):
    """Generate a daily report."""
    typer.echo(f"Report for {date}")

if __name__ == "__main__":
    app()

# Demo: call each subcommand directly
import_books("catalog.csv", "east")
export("output.csv", "json")
report("2026-07-01")
```

Running:
```console
python library_cli.py --help
# Usage: library_cli.py [OPTIONS] COMMAND [ARGS]...
# Commands: import-books, export, report

python library_cli.py import-books catalog.csv --branch east
python library_cli.py report 2026-07-01
```

Note: typer converts `import_books` (underscore) to `import-books` (hyphen) in the CLI name automatically.

## Colors and Progress Bars

`typer` with `rich` provides colored output and progress bars:

```python
import typer
import time

app = typer.Typer()

@app.command()
def process(records: int = 1000):
    typer.echo(typer.style("Starting import...", fg=typer.colors.YELLOW))
    with typer.progressbar(range(records), label="Processing") as progress:
        for _ in progress:
            time.sleep(0.001)   # simulate work
    typer.echo(typer.style("Done!", fg=typer.colors.GREEN, bold=True))

if __name__ == "__main__":
    app()

# Demo: call directly — progressbar runs over 5 items
process(5)
```

## typer vs argparse

| Feature | argparse | typer |
|---|---|---|
| Setup | `parser.add_argument(...)` | Function signature + type annotations |
| Help text | `help="..."` in add_argument | Docstring + param description |
| Type conversion | `type=int` | Python annotation `: int` |
| Subcommands | `add_subparsers()` | Multiple `@app.command()` functions |
| Standard library | Yes | No (requires `pip install typer`) |
| Learning curve | Moderate | Low for Python 3.5+ users |

## typer at a Glance

| Feature | What it does |
|---|---|
| `@app.command()` | Register a function as a CLI command |
| `typer.Argument(...)` | Required positional argument |
| `typer.Option(default)` | Optional named argument |
| `typer.echo(msg)` | Print to stdout (like print) |
| `typer.style(msg, fg=...)` | Colored output |
| `typer.progressbar(iterable)` | Progress bar |

## Your Turn

Rewrite the `report.py` argparse CLI from the previous lesson using `typer`:

```python
import typer
from typing import Optional

app = typer.Typer()

@app.command()
def daily(date: str = typer.Argument(..., help="Date in YYYY-MM-DD format")):
    """Generate a daily report."""
    typer.echo(f"Daily report for: {date}")

@app.command()
def monthly(
    month: int = typer.Argument(..., help="Month number (1-12)"),
    year: int = typer.Argument(..., help="4-digit year"),
):
    """Generate a monthly report."""
    typer.echo(f"Monthly report for: {year}-{month:02d}")

if __name__ == "__main__":
    app()

# Demo: call each command with proper-typed arguments
daily("2026-07-01")
monthly(7, 2026)
```

Compare the two implementations and note which is shorter, which is more explicit, and which you would choose for a team project.

## Conclusion

`typer` builds CLIs from function signatures and type annotations, producing help text, type conversion, and subcommands automatically. It is cleaner than `argparse` for most use cases, at the cost of a third-party dependency. The next lesson covers input validation: how to check that the values the user provides are valid before the program tries to use them.
