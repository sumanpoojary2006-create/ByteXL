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

```python
# Simulate library/cli.py without importing typer (same structure, stdlib only)

def import_books(file, branch="main"):
    """Import books from a CSV file."""
    print(f"Importing {file} into {branch}")

def export(output, format="csv"):
    """Export the catalog."""
    print(f"Exporting to {output} as {format}")

# When installed via pip, the entry point calls: app()
# Here we call the functions directly to demonstrate:
import_books("catalog.csv", branch="east")
export("catalog.json", format="json")

print("\nIn a real package, pyproject.toml maps:")
print("  library-cli = 'library.cli:app'")
print("  -> pip install creates an executable 'library-cli' in bin/")
```

## Installing in Development Mode

```console
# Install the package in editable mode with dev dependencies:
pip install -e .

# Now the entry point is available:
library-cli --help
library-cli import-books catalog.csv --branch east
library-cli export --output catalog.json --format json
```

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

```python
# Simulate library/__main__.py behavior (enables: python -m library)
# In a real package, this file imports and calls the CLI app.

def app():
    """The main CLI entry point (would be typer.Typer() in real code)."""
    print("Library CLI started via: python -m library")
    print("Commands: import-books, export, report")

# __main__.py runs when the package is invoked as: python -m library
# The __name__ == '__main__' check is True in that context.
if __name__ == "__main__":
    app()

# In onecompiler, __name__ is already '__main__', so let's call app() directly:
app()
```

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
