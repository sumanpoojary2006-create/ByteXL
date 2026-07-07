## Introduction

Priya shows her `argparse` CLI to a colleague who works with FastAPI. He notices that the code is repetitive: she declares a `--limit` argument as `type=int`, then accesses it as `args.limit`, and the connection between the two is only maintained by her memory. He shows her `typer`, where type annotations are the argument definitions, and the whole thing is cleaner and shorter.

`typer` is built on top of Click (another popular CLI library) and uses Python type annotations to automatically infer argument types, defaults, and help text.

![A side-by-side showing the argparse version (add_argument + type= + args.limit) versus the typer version (def import_books(limit: int = None)), where the annotation replaces all the boilerplate](images/04_typer.png)

## Installing typer

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVyIGNvZGUgMSIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDEuc2giLCJjb2RlIjoicGlwIGluc3RhbGwgXCJ0eXBlclthbGxdXCIgICAjIGluY2x1ZGVzIHJpY2ggZm9yIGNvbG9yZWQgb3V0cHV0In0"
 width="100%"
></iframe>

## A Basic typer App

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVyIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJpbXBvcnQgdHlwZXJcbmZyb20gdHlwaW5nIGltcG9ydCBPcHRpb25hbFxuXG5hcHAgPSB0eXBlci5UeXBlcigpXG5cbkBhcHAuY29tbWFuZCgpXG5kZWYgaW1wb3J0X2Jvb2tzKFxuICAgIGZpbGU6IHN0ciA9IHR5cGVyLkFyZ3VtZW50KC4uLiwgaGVscD1cIkNTViBmaWxlIHRvIGltcG9ydFwiKSxcbiAgICBicmFuY2g6IHN0ciA9IHR5cGVyLk9wdGlvbihcIm1haW5cIiwgaGVscD1cIlRhcmdldCBicmFuY2hcIiksXG4gICAgbGltaXQ6IE9wdGlvbmFsW2ludF0gPSB0eXBlci5PcHRpb24oTm9uZSwgaGVscD1cIk1heGltdW0gcmVjb3JkcyB0byBpbXBvcnRcIiksXG4gICAgZHJ5X3J1bjogYm9vbCA9IHR5cGVyLk9wdGlvbihGYWxzZSwgXCItLWRyeS1ydW5cIiwgaGVscD1cIlZhbGlkYXRlIG9ubHlcIiksXG4pOlxuICAgIFwiXCJcIkltcG9ydCBib29rcyBpbnRvIHRoZSBsaWJyYXJ5IGNhdGFsb2cuXCJcIlwiXG4gICAgdHlwZXIuZWNobyhmXCJGaWxlOiAgICAge2ZpbGV9XCIpXG4gICAgdHlwZXIuZWNobyhmXCJCcmFuY2g6ICAge2JyYW5jaH1cIilcbiAgICB0eXBlci5lY2hvKGZcIkxpbWl0OiAgICB7bGltaXR9XCIpXG4gICAgdHlwZXIuZWNobyhmXCJEcnkgcnVuOiAge2RyeV9ydW59XCIpXG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICBhcHAoKSJ9"
 width="100%"
></iframe>

Running:
<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVyIGNvZGUgMyIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDMuc2giLCJjb2RlIjoicHl0aG9uIGltcG9ydF9ib29rcy5weSBjYXRhbG9nLmNzdiAtLWJyYW5jaCBlYXN0IC0tbGltaXQgMTAwIC0tZHJ5LXJ1blxuIyBGaWxlOiAgICAgY2F0YWxvZy5jc3ZcbiMgQnJhbmNoOiAgIGVhc3RcbiMgTGltaXQ6ICAgIDEwMFxuIyBEcnkgcnVuOiAgVHJ1ZVxuXG5weXRob24gaW1wb3J0X2Jvb2tzLnB5IC0taGVscFxuIyBVc2FnZTogaW1wb3J0X2Jvb2tzLnB5IFtPUFRJT05TXSBGSUxFXG4jXG4jICAgSW1wb3J0IGJvb2tzIGludG8gdGhlIGxpYnJhcnkgY2F0YWxvZy5cbiMgLi4uIn0"
 width="100%"
></iframe>

The docstring becomes the command description automatically.

## Argument vs Option

`typer.Argument(...)` is a positional argument (required, no `--` prefix). The `...` (Ellipsis) means it is required. `typer.Option(default)` is a named option (`--branch`, `--limit`).

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVyIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJAYXBwLmNvbW1hbmQoKVxuZGVmIHNlYXJjaChcbiAgICBxdWVyeTogc3RyLCAgICAgICAgICAgICAgICAgICAgIyBzaW1wbGVzdCBmb3JtOiBwb3NpdGlvbmFsLCByZXF1aXJlZFxuICAgIGJyYW5jaDogc3RyID0gXCJtYWluXCIsICAgICAgICAgICMgc2ltcGxlc3QgZm9ybTogb3B0aW9uIHdpdGggZGVmYXVsdFxuICAgIGxpbWl0OiBpbnQgPSAxMCwgICAgICAgICAgICAgICAjIHR5cGVyIGluZmVycyB0eXBlIGZyb20gYW5ub3RhdGlvblxuKTpcbiAgICBwcmludChmXCJTZWFyY2hpbmcgZm9yICd7cXVlcnl9JyBpbiB7YnJhbmNofSwgbWF4IHtsaW1pdH0gcmVzdWx0c1wiKSJ9"
 width="100%"
></iframe>

In this short form, `typer` infers that `query` (no default) is a required argument and `branch`/`limit` (with defaults) are options. The simplest `typer` commands need no `typer.Argument` or `typer.Option` at all.

## Multiple Commands

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVyIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJpbXBvcnQgdHlwZXJcblxuYXBwID0gdHlwZXIuVHlwZXIoKVxuXG5AYXBwLmNvbW1hbmQoKVxuZGVmIGltcG9ydF9ib29rcyhmaWxlOiBzdHIsIGJyYW5jaDogc3RyID0gXCJtYWluXCIpOlxuICAgIFwiXCJcIkltcG9ydCBib29rcyBmcm9tIGEgQ1NWIGZpbGUuXCJcIlwiXG4gICAgdHlwZXIuZWNobyhmXCJJbXBvcnRpbmcge2ZpbGV9IGludG8ge2JyYW5jaH1cIilcblxuQGFwcC5jb21tYW5kKClcbmRlZiBleHBvcnQob3V0cHV0OiBzdHIsIGZvcm1hdDogc3RyID0gXCJjc3ZcIik6XG4gICAgXCJcIlwiRXhwb3J0IHRoZSBjYXRhbG9nIHRvIGEgZmlsZS5cIlwiXCJcbiAgICB0eXBlci5lY2hvKGZcIkV4cG9ydGluZyB0byB7b3V0cHV0fSBhcyB7Zm9ybWF0fVwiKVxuXG5AYXBwLmNvbW1hbmQoKVxuZGVmIHJlcG9ydChkYXRlOiBzdHIpOlxuICAgIFwiXCJcIkdlbmVyYXRlIGEgZGFpbHkgcmVwb3J0LlwiXCJcIlxuICAgIHR5cGVyLmVjaG8oZlwiUmVwb3J0IGZvciB7ZGF0ZX1cIilcblxuaWYgX19uYW1lX18gPT0gXCJfX21haW5fX1wiOlxuICAgIGFwcCgpIn0"
 width="100%"
></iframe>

Running:
<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVyIGNvZGUgNiIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDYuc2giLCJjb2RlIjoicHl0aG9uIGxpYnJhcnlfY2xpLnB5IC0taGVscFxuIyBVc2FnZTogbGlicmFyeV9jbGkucHkgW09QVElPTlNdIENPTU1BTkQgW0FSR1NdLi4uXG4jIENvbW1hbmRzOiBpbXBvcnQtYm9va3MsIGV4cG9ydCwgcmVwb3J0XG5cbnB5dGhvbiBsaWJyYXJ5X2NsaS5weSBpbXBvcnQtYm9va3MgY2F0YWxvZy5jc3YgLS1icmFuY2ggZWFzdFxucHl0aG9uIGxpYnJhcnlfY2xpLnB5IHJlcG9ydCAyMDI2LTA3LTAxIn0"
 width="100%"
></iframe>

Note: typer converts `import_books` (underscore) to `import-books` (hyphen) in the CLI name automatically.

## Colors and Progress Bars

`typer` with `rich` provides colored output and progress bars:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVyIGNvZGUgNyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNy5weSIsImNvZGUiOiJpbXBvcnQgdHlwZXJcbmltcG9ydCB0aW1lXG5cbmFwcCA9IHR5cGVyLlR5cGVyKClcblxuQGFwcC5jb21tYW5kKClcbmRlZiBwcm9jZXNzKHJlY29yZHM6IGludCA9IDEwMDApOlxuICAgIHR5cGVyLmVjaG8odHlwZXIuc3R5bGUoXCJTdGFydGluZyBpbXBvcnQuLi5cIiwgZmc9dHlwZXIuY29sb3JzLllFTExPVykpXG4gICAgd2l0aCB0eXBlci5wcm9ncmVzc2JhcihyYW5nZShyZWNvcmRzKSwgbGFiZWw9XCJQcm9jZXNzaW5nXCIpIGFzIHByb2dyZXNzOlxuICAgICAgICBmb3IgXyBpbiBwcm9ncmVzczpcbiAgICAgICAgICAgIHRpbWUuc2xlZXAoMC4wMDEpICAgIyBzaW11bGF0ZSB3b3JrXG4gICAgdHlwZXIuZWNobyh0eXBlci5zdHlsZShcIkRvbmUhXCIsIGZnPXR5cGVyLmNvbG9ycy5HUkVFTiwgYm9sZD1UcnVlKSlcblxuaWYgX19uYW1lX18gPT0gXCJfX21haW5fX1wiOlxuICAgIGFwcCgpIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3R5cGVyIGNvZGUgOCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwOC5weSIsImNvZGUiOiJpbXBvcnQgdHlwZXJcbmZyb20gdHlwaW5nIGltcG9ydCBPcHRpb25hbFxuXG5hcHAgPSB0eXBlci5UeXBlcigpXG5cbkBhcHAuY29tbWFuZCgpXG5kZWYgZGFpbHkoZGF0ZTogc3RyID0gdHlwZXIuQXJndW1lbnQoLi4uLCBoZWxwPVwiRGF0ZSBpbiBZWVlZLU1NLUREIGZvcm1hdFwiKSk6XG4gICAgXCJcIlwiR2VuZXJhdGUgYSBkYWlseSByZXBvcnQuXCJcIlwiXG4gICAgdHlwZXIuZWNobyhmXCJEYWlseSByZXBvcnQgZm9yOiB7ZGF0ZX1cIilcblxuQGFwcC5jb21tYW5kKClcbmRlZiBtb250aGx5KFxuICAgIG1vbnRoOiBpbnQgPSB0eXBlci5Bcmd1bWVudCguLi4sIGhlbHA9XCJNb250aCBudW1iZXIgKDEtMTIpXCIpLFxuICAgIHllYXI6IGludCA9IHR5cGVyLkFyZ3VtZW50KC4uLiwgaGVscD1cIjQtZGlnaXQgeWVhclwiKSxcbik6XG4gICAgXCJcIlwiR2VuZXJhdGUgYSBtb250aGx5IHJlcG9ydC5cIlwiXCJcbiAgICB0eXBlci5lY2hvKGZcIk1vbnRobHkgcmVwb3J0IGZvcjoge3llYXJ9LXttb250aDowMmR9XCIpXG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICBhcHAoKSJ9"
 width="100%"
></iframe>

Compare the two implementations and note which is shorter, which is more explicit, and which you would choose for a team project.

## Conclusion

`typer` builds CLIs from function signatures and type annotations, producing help text, type conversion, and subcommands automatically. It is cleaner than `argparse` for most use cases, at the cost of a third-party dependency. The next lesson covers input validation: how to check that the values the user provides are valid before the program tries to use them.
