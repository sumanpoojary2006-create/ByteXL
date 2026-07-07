## Introduction

Nadia's catalog export script runs fine on her MacBook but fails on the Windows server in the consortium's office. The path separator is wrong: `"data/catalogs/branch_1.csv"` uses a forward slash that Windows does not accept in certain contexts. Her script also hard-codes `"/home/nadia/data"` as the working directory, which does not exist on the server.

The fix is to stop constructing file paths as strings and start using Python's path objects, which handle separators, relative vs absolute paths, and home-directory expansion automatically.

![Two paths shown side by side: a fragile string path built with + and "/" operators, and a safe pathlib.Path built with / operator, annotated with methods: .exists(), .mkdir(), .glob()](images/07_os_sys_pathlib.png)

## pathlib.Path: The Modern Way

`pathlib.Path` represents a file system path as an object. The `/` operator joins path segments, automatically using the correct separator for the platform.

```python
from pathlib import Path

# Build a path without caring about OS separators
data_dir = Path("data") / "catalogs" / "2026"
print(data_dir)         # data/catalogs/2026  (Linux/Mac)
                        # data\catalogs\2026   (Windows)

# Inspect a path
path = Path("/Users/nadia/data/catalog.csv")
print(path.name)        # 'catalog.csv'
print(path.stem)        # 'catalog'
print(path.suffix)      # '.csv'
print(path.parent)      # /Users/nadia/data

# Check existence
print(path.exists())    # True or False
print(path.is_file())   # True if it is a file
print(path.is_dir())    # True if it is a directory
```

## Creating and Walking Directories

```python
from pathlib import Path

output_dir = Path("exports") / "2026" / "july"
output_dir.mkdir(parents=True, exist_ok=True)
# creates all intermediate directories; no error if already exists

# Write a file into the directory:
catalog_file = output_dir / "branch_1.csv"
catalog_file.write_text("isbn,title\n978-001,Dune\n")

# Read it back:
print(catalog_file.read_text())
```

`mkdir(parents=True, exist_ok=True)` is the safe combination: `parents=True` creates all missing parent directories, `exist_ok=True` avoids an error if the directory already exists.

## Globbing: Find Files by Pattern

```python
from pathlib import Path

data_dir = Path("exports")

# Find all CSV files recursively:
csv_files = list(data_dir.rglob("*.csv"))
for f in csv_files:
    print(f)

# Find all files in the immediate directory only:
json_files = list(data_dir.glob("*.json"))
```

`rglob` is "recursive glob" -- it searches the directory and all subdirectories.

## os and os.path

`os` provides lower-level system operations. `pathlib` replaces most of `os.path`, but some `os` operations have no pathlib equivalent:

```python
import os

# Environment variables
home = os.environ.get("HOME", "/tmp")   # safe: returns default if missing
api_key = os.environ["LIBRARY_API_KEY"]  # raises KeyError if missing

# Current working directory
print(os.getcwd())

# List directory contents (returns strings)
files = os.listdir(".")
print(files)

# Remove a file
os.remove("old_catalog.txt")

# Remove an empty directory
os.rmdir("empty_dir")

# Walk a directory tree (yields dirpath, dirnames, filenames)
for dirpath, dirnames, filenames in os.walk("exports"):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
```

## sys: Process-Level Information

`sys` provides access to the Python interpreter itself:

```python
import sys

print(sys.version)         # Python version string
print(sys.platform)        # 'darwin', 'linux', 'win32'
print(sys.executable)      # path to the Python binary
print(sys.argv)            # command-line arguments
print(sys.path)            # module search path

# Exit the program:
if not config_file.exists():
    print("Config file missing", file=sys.stderr)
    sys.exit(1)   # exit with error code 1
```

`sys.stderr` is the standard error stream. Writing error messages there, rather than to `sys.stdout`, allows shell pipelines to separate output from errors.

## Combining os, sys, and pathlib

```python
import os
import sys
from pathlib import Path

def get_data_dir() -> Path:
    """Return the data directory, creating it if needed."""
    base = Path(os.environ.get("LIBRARY_DATA_DIR", "."))
    data_dir = base / "data" / "catalogs"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir

def process_all_catalogs():
    data_dir = get_data_dir()
    csv_files = list(data_dir.rglob("*.csv"))
    if not csv_files:
        print(f"No catalogs found in {data_dir}", file=sys.stderr)
        sys.exit(1)
    for f in csv_files:
        print(f"Processing: {f}")
        content = f.read_text()
        # ... process content
```

## os / sys / pathlib at a Glance

| Tool | When to use |
|---|---|
| `Path("/a") / "b"` | Build cross-platform paths |
| `path.exists()`, `.is_file()`, `.is_dir()` | Check path state |
| `path.mkdir(parents=True, exist_ok=True)` | Create directories safely |
| `path.rglob("*.csv")` | Find files by pattern recursively |
| `path.read_text()`, `.write_text()` | Simple file I/O |
| `os.environ.get("KEY", default)` | Read environment variables |
| `os.walk(dir)` | Recursively iterate directory tree |
| `sys.argv` | Command-line arguments |
| `sys.exit(code)` | Exit with a status code |
| `sys.stderr` | Write error messages |

## Your Turn

Write a function `find_catalogs(base_dir, since_date)` that walks a directory tree looking for CSV files whose names start with a date stamp (`YYYY-MM-DD_catalog.csv`) and returns only those whose date is on or after `since_date`:

```python
import tempfile, os
from pathlib import Path
from datetime import date

def find_catalogs(base_dir, since_date):
    base = Path(base_dir)
    result = []
    for f in base.rglob("*_catalog.csv"):
        try:
            date_part = f.stem.split("_")[0]   # e.g. '2026-07-01'
            file_date = date.fromisoformat(date_part)
            if file_date >= since_date:
                result.append(f)
        except ValueError:
            continue   # skip files that don't match the pattern
    return sorted(result)

# Demo: create a temp directory with dated catalog files
tmp = tempfile.mkdtemp()
for fname in ["2026-01-15_catalog.csv", "2026-06-01_catalog.csv", "2025-12-31_catalog.csv"]:
    Path(tmp, fname).write_text("isbn,title\n")

cutoff = date(2026, 3, 1)
result = find_catalogs(tmp, cutoff)
print(f"find_catalogs(tmp, date(2026,3,1)) -> {[f.name for f in result]}")

import shutil
shutil.rmtree(tmp)
```

## Conclusion

`pathlib.Path` is the modern way to handle file paths in Python: cross-platform, readable, and rich with methods for existence checks, globbing, and I/O. `os` fills the gaps where pathlib has no equivalent (environment variables, `os.walk`). `sys` gives access to the interpreter and process-level operations. The next lesson wraps up the standard library unit with `json` and `csv`, the two formats Nadia uses to exchange data with every other system in the consortium.
