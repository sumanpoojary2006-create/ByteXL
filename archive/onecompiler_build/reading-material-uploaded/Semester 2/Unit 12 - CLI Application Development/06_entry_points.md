## Introduction

Priya's colleagues run her tools as `python import_books.py`. She wants them to run `library-cli import-books` -- no Python prefix, no file path, just the command name. This requires packaging the tool so that pip creates an executable entry point when it is installed.

Entry points are defined in `pyproject.toml`. When a package is installed with `pip install`, pip reads the entry points and creates a script in the environment's `bin/` directory that calls the CLI function directly.

![A diagram showing pyproject.toml defining a [project.scripts] entry point, pip install creating a script in bin/, and the user running the command directly by name](images/06_entry_points.png)

## The [project.scripts] Section

In `pyproject.toml`, define a console script entry point:

```toml
# pyproject.toml
[project]
name = "library-tools"
version = "1.0.0"
dependencies = ["typer[all]"]

[project.scripts]
library-cli = "library.cli:app"
```

The format is `command-name = "package.module:callable"`. Here:
- `library-cli` is the command users type
- `library.cli` is the Python module (`library/cli.py`)
- `app` is the callable in that module (the `typer.Typer()` app object)

## The cli.py Module

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-06-entry-points-001-75216aee25.html"
 width="100%"
></iframe>

## Installing in Development Mode

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-06-entry-points-002-63e778894f.html"
 width="100%"
></iframe>

The `-e` (editable) flag makes changes to `library/cli.py` immediately available without reinstalling.

## Multiple Entry Points

A package can expose multiple commands:

```toml
[project.scripts]
library-cli = "library.cli:app"
library-admin = "library.admin_cli:admin_app"
library-report = "library.reports.cli:report_app"
```

Each becomes its own executable. `pip install library-tools` creates all three in the user's `bin/`.

## The __main__.py Pattern

For `python -m library.cli` to also work (useful for debugging and scripts), add a `__main__.py`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-06-entry-points-003-3d2c8552aa.html"
 width="100%"
></iframe>

This allows `python -m library` to launch the CLI, alongside the installed `library-cli` command.

## Entry Points at a Glance

| Concept | What it means |
|---|---|
| `[project.scripts]` | Maps command names to Python callables |
| `cmd = "pkg.module:callable"` | Format for script entry points |
| `pip install -e .` | Editable install; updates immediately |
| `__main__.py` | Enables `python -m package` form |

## Your Turn

Create a `pyproject.toml` for the library tools project with one entry point: `library-cli` mapping to `library.cli:app`. Install it with `pip install -e .` and run `library-cli --help` to confirm the command is available. Then add a second entry point `library-report` for a separate report CLI.

```toml
[project]
name = "library-tools"
version = "1.0.0"
requires-python = ">=3.11"
dependencies = ["typer[all]"]

[project.scripts]
library-cli = "library.cli:app"
library-report = "library.reports.cli:report_app"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## Conclusion

Entry points in `pyproject.toml` register CLI commands so that `pip install` creates runnable executables. The format is `command = "module:callable"`. Editable installs (`pip install -e .`) make development fast. The final lesson covers CLI UX best practices: how to design CLIs that are intuitive and hard to misuse.
