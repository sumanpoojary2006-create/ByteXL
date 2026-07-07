## Introduction

The library system now has eleven Python files scattered across a single folder. Dev imports functions by path, the test runner can't find the modules, and a volunteer who cloned the repository got a different error on every machine. What was a small script has become a project without a structure.

This unit is about turning that collection of files into a proper Python package: one that installs cleanly, exposes a CLI command, and can be shared with anyone using `pip install`.

![A messy folder of Python files on the left transforming into a structured src-layout package on the right, with pyproject.toml at the root](images/01_project_structure.png)

## The src Layout

The most reliable project structure for installable packages is the `src` layout:

```python
# Visualize the recommended project layout

layout = {
    "library-system/": {
        "src/": {
            "library/": {
                "__init__.py":    "makes 'library' a package",
                "database.py":    "LibraryDatabase class",
                "catalog.py":     "book/member management",
                "cli.py":         "typer CLI commands",
            }
        },
        "tests/": {
            "__init__.py":        "makes tests a package",
            "test_database.py":   "database tests",
            "test_catalog.py":    "catalog tests",
        },
        "pyproject.toml":         "project metadata and dependencies",
        "README.md":              "user-facing documentation",
        ".pre-commit-config.yaml":"code quality hooks",
    }
}

def print_tree(tree, indent=0):
    for key, value in tree.items():
        print("  " * indent + key)
        if isinstance(value, dict):
            print_tree(value, indent + 1)
        else:
            print("  " * (indent + 1) + f"# {value}")

print_tree(layout)
```

## Why Not Put Everything at the Root?

```python
# Two structures -- only one installs reliably

flat_structure = [
    "library.py",       # at the root
    "tests/",
    "setup.py",
]

src_structure = [
    "src/library/",     # inside src/
    "tests/",
    "pyproject.toml",
]

print("Flat structure problems:")
problems = [
    "pytest can import library.py directly from current directory",
    "  -> tests pass locally but fail in CI (different working dir)",
    "Installed package might shadow the source file",
    "  -> you edit source but import still uses the installed version",
]
for p in problems:
    print(" ", p)

print()
print("src layout benefits:")
benefits = [
    "Tests must import the installed package, not the source folder",
    "  -> catches import errors before they reach users",
    "No accidental source-vs-installed confusion",
    "Cleaner: source code is in one place, project files at root",
]
for b in benefits:
    print(" ", b)
```

## The `__init__.py` File

```python
# What __init__.py does

# Without __init__.py: folder is just a folder
# With __init__.py: folder is a package Python can import

# src/library/__init__.py might look like:
init_content = '''
from .database import LibraryDatabase
from .catalog import BookCatalog

__version__ = "1.0.0"
__all__ = ["LibraryDatabase", "BookCatalog"]
'''

print("Contents of src/library/__init__.py:")
print(init_content)

# Relative imports (.database, .catalog) work inside a package
# They say "import from the same package, not from sys.path"
print("Relative imports (.module) work only inside packages")
print("Absolute imports work from anywhere")

# Demonstrate what __version__ provides
version = "1.0.0"
parts = version.split(".")
print(f"\nVersion {version}: major={parts[0]}, minor={parts[1]}, patch={parts[2]}")
```

## Namespacing: Why Packages Beat Scripts

```python
# A package controls its public API

# From outside: users import only what __all__ exposes
public_api = ["LibraryDatabase", "BookCatalog"]
internal = ["_connection_pool", "_migrate_schema", "_Row"]

print("Public API (importable by users):")
for name in public_api:
    print(f"  from library import {name}")

print("\nInternal (underscore prefix = not for external use):")
for name in internal:
    print(f"  library.{name}  # exists but not in __all__")

print("\nResult: users get a stable interface")
print("Internal changes don't break their code")
```

## Checking the Structure Is Correct

```python
import os

# Simulate checking that a project structure is valid
def check_structure(root_files, required):
    missing = [f for f in required if f not in root_files]
    present = [f for f in required if f in root_files]
    return present, missing

# Files that should be at the project root
required_files = ["pyproject.toml", "README.md", ".pre-commit-config.yaml"]

# Simulate what we have
actual_files = ["pyproject.toml", "README.md", "library.py"]   # missing pre-commit

present, missing = check_structure(actual_files, required_files)
print("Present:", present)
print("Missing:", missing)

if missing:
    print(f"\nFix: create {', '.join(missing)}")
else:
    print("\nStructure looks correct")
```

## Project Structure at a Glance

| Item | Location | Purpose |
|---|---|---|
| `src/library/` | Inside `src/` | The installable package source |
| `__init__.py` | Every package directory | Marks it as a Python package |
| `tests/` | At the project root | Test files, separate from source |
| `pyproject.toml` | At the project root | Metadata, dependencies, tool config |
| `README.md` | At the project root | User-facing documentation |

## Your Turn

Draw (or write out) the directory tree for a project called `bookworm` that has two sub-packages: `bookworm.search` and `bookworm.export`. Where does each `__init__.py` go? Where does `pyproject.toml` go? Where do the tests go?

## Conclusion

The `src` layout prevents the most common packaging bugs by forcing tests to import the installed package rather than the source folder. Every package directory needs an `__init__.py`. Project metadata and configuration live in `pyproject.toml` at the root. The next lesson writes that `pyproject.toml` from scratch.
