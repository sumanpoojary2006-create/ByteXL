## Introduction

Priya shows her `argparse` CLI to a colleague who works with FastAPI. He notices that the code is repetitive: she declares a `--limit` argument as `type=int`, then accesses it as `args.limit`, and the connection between the two is only maintained by her memory. He shows her `typer`, where type annotations are the argument definitions, and the whole thing is cleaner and shorter.

`typer` is built on top of Click (another popular CLI library) and uses Python type annotations to automatically infer argument types, defaults, and help text.

![A side-by-side showing the argparse version (add_argument + type= + args.limit) versus the typer version (def import_books(limit: int = None)), where the annotation replaces all the boilerplate](images/04_typer.png)

## Installing typer

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-04-typer-001-b7926ecb5a.html"
 width="100%"
></iframe>

## A Basic typer App

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-04-typer-002-e904e6d6ad.html"
 width="100%"
></iframe>

Running:
<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-04-typer-003-41ab312f37.html"
 width="100%"
></iframe>

The docstring becomes the command description automatically.

## Argument vs Option

`typer.Argument(...)` is a positional argument (required, no `--` prefix). The `...` (Ellipsis) means it is required. `typer.Option(default)` is a named option (`--branch`, `--limit`).

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-04-typer-004-0f285b2a81.html"
 width="100%"
></iframe>

In this short form, `typer` infers that `query` (no default) is a required argument and `branch`/`limit` (with defaults) are options. The simplest `typer` commands need no `typer.Argument` or `typer.Option` at all.

## Multiple Commands

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-04-typer-005-2ca1424dbd.html"
 width="100%"
></iframe>

Running:
<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-04-typer-006-e3d4144f3a.html"
 width="100%"
></iframe>

Note: typer converts `import_books` (underscore) to `import-books` (hyphen) in the CLI name automatically.

## Colors and Progress Bars

`typer` with `rich` provides colored output and progress bars:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-04-typer-007-d97456779c.html"
 width="100%"
></iframe>

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

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-04-typer-008-8bef65ecc1.html"
 width="100%"
></iframe>

Compare the two implementations and note which is shorter, which is more explicit, and which you would choose for a team project.

## Conclusion

`typer` builds CLIs from function signatures and type annotations, producing help text, type conversion, and subcommands automatically. It is cleaner than `argparse` for most use cases, at the cost of a third-party dependency. The next lesson covers input validation: how to check that the values the user provides are valid before the program tries to use them.
