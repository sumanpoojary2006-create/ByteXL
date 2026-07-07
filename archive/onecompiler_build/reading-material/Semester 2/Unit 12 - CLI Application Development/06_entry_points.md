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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2VudHJ5X3BvaW50cyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiIyBsaWJyYXJ5L2NsaS5weVxuaW1wb3J0IHR5cGVyXG5cbmFwcCA9IHR5cGVyLlR5cGVyKG5hbWU9XCJsaWJyYXJ5LWNsaVwiLCBoZWxwPVwiTGlicmFyeSBtYW5hZ2VtZW50IHRvb2xzXCIpXG5cbkBhcHAuY29tbWFuZCgpXG5kZWYgaW1wb3J0X2Jvb2tzKGZpbGU6IHN0ciwgYnJhbmNoOiBzdHIgPSBcIm1haW5cIik6XG4gICAgXCJcIlwiSW1wb3J0IGJvb2tzIGZyb20gYSBDU1YgZmlsZS5cIlwiXCJcbiAgICB0eXBlci5lY2hvKGZcIkltcG9ydGluZyB7ZmlsZX0gaW50byB7YnJhbmNofVwiKVxuXG5AYXBwLmNvbW1hbmQoKVxuZGVmIGV4cG9ydChvdXRwdXQ6IHN0ciwgZm9ybWF0OiBzdHIgPSBcImNzdlwiKTpcbiAgICBcIlwiXCJFeHBvcnQgdGhlIGNhdGFsb2cuXCJcIlwiXG4gICAgdHlwZXIuZWNobyhmXCJFeHBvcnRpbmcgdG8ge291dHB1dH1cIilcblxuIyBObyBpZiBfX25hbWVfXyA9PSBcIl9fbWFpbl9fXCI6IG5lZWRlZCBmb3IgZW50cnkgcG9pbnRzXG4jIHBpcCB3aWxsIGNhbGwgYXBwKCkgZGlyZWN0bHkifQ"
 width="100%"
></iframe>

## Installing in Development Mode

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2VudHJ5X3BvaW50cyBjb2RlIDIiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDAyLnNoIiwiY29kZSI6IiMgSW5zdGFsbCB0aGUgcGFja2FnZSBpbiBlZGl0YWJsZSBtb2RlIHdpdGggZGV2IGRlcGVuZGVuY2llczpcbnBpcCBpbnN0YWxsIC1lIC5cblxuIyBOb3cgdGhlIGVudHJ5IHBvaW50IGlzIGF2YWlsYWJsZTpcbmxpYnJhcnktY2xpIC0taGVscFxubGlicmFyeS1jbGkgaW1wb3J0LWJvb2tzIGNhdGFsb2cuY3N2IC0tYnJhbmNoIGVhc3RcbmxpYnJhcnktY2xpIGV4cG9ydCAtLW91dHB1dCBjYXRhbG9nLmpzb24gLS1mb3JtYXQganNvbiJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2VudHJ5X3BvaW50cyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiIyBsaWJyYXJ5L19fbWFpbl9fLnB5XG5mcm9tIGxpYnJhcnkuY2xpIGltcG9ydCBhcHBcblxuaWYgX19uYW1lX18gPT0gXCJfX21haW5fX1wiOlxuICAgIGFwcCgpIn0"
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
