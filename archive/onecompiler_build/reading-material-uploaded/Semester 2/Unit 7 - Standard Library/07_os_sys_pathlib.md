## Introduction

Nadia's catalog export script runs fine on her MacBook but fails on the Windows server in the consortium's office. The path separator is wrong: `"data/catalogs/branch_1.csv"` uses a forward slash that Windows does not accept in certain contexts. Her script also hard-codes `"/home/nadia/data"` as the working directory, which does not exist on the server.

The fix is to stop constructing file paths as strings and start using Python's path objects, which handle separators, relative vs absolute paths, and home-directory expansion automatically.

![Two paths shown side by side: a fragile string path built with + and "/" operators, and a safe pathlib.Path built with / operator, annotated with methods: .exists(), .mkdir(), .glob()](images/07_os_sys_pathlib.png)

## pathlib.Path: The Modern Way

`pathlib.Path` represents a file system path as an object. The `/` operator joins path segments, automatically using the correct separator for the platform.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-07-os-sys-pathlib-001-c2e7dc52ba.html"
 width="100%"
></iframe>

## Creating and Walking Directories

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-07-os-sys-pathlib-002-ede989e9fe.html"
 width="100%"
></iframe>

`mkdir(parents=True, exist_ok=True)` is the safe combination: `parents=True` creates all missing parent directories, `exist_ok=True` avoids an error if the directory already exists.

## Globbing: Find Files by Pattern

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-07-os-sys-pathlib-003-8014b8d658.html"
 width="100%"
></iframe>

`rglob` is "recursive glob" -- it searches the directory and all subdirectories.

## os and os.path

`os` provides lower-level system operations. `pathlib` replaces most of `os.path`, but some `os` operations have no pathlib equivalent:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-07-os-sys-pathlib-004-ef6d03ca65.html"
 width="100%"
></iframe>

## sys: Process-Level Information

`sys` provides access to the Python interpreter itself:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-07-os-sys-pathlib-005-310fb3b56d.html"
 width="100%"
></iframe>

`sys.stderr` is the standard error stream. Writing error messages there, rather than to `sys.stdout`, allows shell pipelines to separate output from errors.

## Combining os, sys, and pathlib

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-07-os-sys-pathlib-006-0d4fe50fbb.html"
 width="100%"
></iframe>

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

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-7-standard-library-07-os-sys-pathlib-007-36743bc580.html"
 width="100%"
></iframe>

## Conclusion

`pathlib.Path` is the modern way to handle file paths in Python: cross-platform, readable, and rich with methods for existence checks, globbing, and I/O. `os` fills the gaps where pathlib has no equivalent (environment variables, `os.walk`). `sys` gives access to the interpreter and process-level operations. The next lesson wraps up the standard library unit with `json` and `csv`, the two formats Nadia uses to exchange data with every other system in the consortium.
