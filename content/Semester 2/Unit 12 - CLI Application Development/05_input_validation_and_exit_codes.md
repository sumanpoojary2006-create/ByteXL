## Introduction

Priya's import command accepts a `--date` option. A librarian passes `2026-13-45` as the date. The import script starts processing, reaches the date comparison, and crashes with a `ValueError: time data '2026-13-45' does not match format '%Y-%m-%d'`. The crash is confusing because the error appears in the middle of output, not at the start.

The principle: validate early, exit cleanly. Check all user-provided values at the start of the command, before doing any real work. If anything is invalid, print a clear error message and exit with a non-zero code.

![Two timelines: top shows late validation where processing starts and fails mid-way; bottom shows early validation where all checks happen before any work starts, with a clean error message at the top](images/05_input_validation_exit_codes.png)

## Validate Early

```python
import argparse
import sys
from datetime import date

def validate_date(value):
    try:
        return date.fromisoformat(value)
    except ValueError:
        print(f"Error: invalid date '{value}'. Expected YYYY-MM-DD")
        return None   # in real CLI: sys.exit(1)

# Demo: validate good and bad dates before doing any work
for test_date in ["2026-07-01", "2026-13-45", "not-a-date"]:
    result = validate_date(test_date)
    if result:
        print(f"  '{test_date}' -> valid: {result}")
    else:
        print(f"  '{test_date}' -> INVALID -- would exit(1) in real CLI")
```

## Validation Patterns

```python
def validate_positive_int(value, name):
    try:
        n = int(value)
    except ValueError:
        return None, f"Error: {name} must be an integer, got '{value}'"
    if n <= 0:
        return None, f"Error: {name} must be positive, got {n}"
    return n, None

def validate_choices(value, choices, name):
    if value not in choices:
        return None, f"Error: {name} must be one of {choices}, got '{value}'"
    return value, None

# Demo all validators
tests = [
    ("positive_int", validate_positive_int("50", "limit")),
    ("positive_int bad", validate_positive_int("abc", "limit")),
    ("positive_int neg", validate_positive_int("-5", "limit")),
    ("choices ok", validate_choices("csv", ["csv", "json", "text"], "format")),
    ("choices bad", validate_choices("xml", ["csv", "json", "text"], "format")),
]
for label, (result, error) in tests:
    if error:
        print(f"  {label}: {error}")
    else:
        print(f"  {label}: valid -> {result}")
```

## typer Validation with Callbacks

In `typer`, validation can be done with the `callback` parameter of `typer.Option`:

```python
# Simulate typer-style validation using stdlib (typer uses type annotations + callbacks)
from datetime import date

class BadParameter(Exception):
    pass

def validate_date(value):
    """Callback-style validator -- typer calls this automatically on the --date option."""
    try:
        date.fromisoformat(value)
        return value
    except ValueError:
        raise BadParameter(f"Invalid date '{value}'. Expected YYYY-MM-DD")

def report(date_str):
    """Simulate typer command -- generates a report for the validated date."""
    print(f"Generating report for {date_str}")

# Demo: valid date
try:
    validated = validate_date("2026-07-01")
    report(validated)
except BadParameter as e:
    print(f"BadParameter: {e}")

# Demo: invalid date (typer would print a formatted error and exit code 2)
try:
    validated = validate_date("2026-13-45")
    report(validated)
except BadParameter as e:
    print(f"BadParameter: {e}")
```

`typer.BadParameter` produces a well-formatted error and exits with code 2.

## Exit Codes

Exit codes are the CLI's way of communicating success or failure to the calling process (shell, script, CI):

```python
import sys

# Standard exit codes (demonstrated without actually exiting the process)
EXIT_CODES = {
    0: "success",
    1: "runtime error (general failure)",
    2: "invalid arguments (argparse default for bad args)",
    3: "file not found",
    4: "permission denied",
}

print("Standard CLI exit codes:")
for code, meaning in EXIT_CODES.items():
    print(f"  sys.exit({code})  ->  {meaning}")

# In a real CLI function:
def run_import(csv_file, dry_run=False):
    if not csv_file.endswith(".csv"):
        print(f"Error: expected a .csv file, got '{csv_file}'")
        return 2   # would call sys.exit(2) in real CLI
    print(f"Import {'(dry run) ' if dry_run else ''}from {csv_file}: done")
    return 0   # would call sys.exit(0) in real CLI

code = run_import("books.csv")
print(f"Exit code: {code} ({EXIT_CODES[code]})")

code = run_import("books.txt")
print(f"Exit code: {code} ({EXIT_CODES[code]})")
```

Shell scripts can check exit codes:

```console
python import_books.py catalog.csv || echo "Import failed"
```

`||` runs the second command only if the first fails (non-zero exit).

## typer's raise typer.Exit

In `typer`, use `raise typer.Exit(code=N)` instead of `sys.exit(N)`:

```python
# Simulate typer.Exit pattern using stdlib (typer uses raise typer.Exit(code=N))
class ExitError(SystemExit):
    pass

def check_file(file_path):
    """Simulate a typer command that checks if a file exists."""
    import io
    # Use StringIO to simulate a file that exists (no real filesystem access)
    fake_files = {"catalog.csv": "isbn,title\n978-001,Dune"}
    if file_path not in fake_files:
        print(f"Error: {file_path} not found")
        return 1   # typer: raise typer.Exit(code=1)
    print(f"File found: {file_path} ({len(fake_files[file_path])} bytes)")
    return 0

# Demo: existing file
code = check_file("catalog.csv")
print(f"Exit code: {code}")

# Demo: missing file
code = check_file("missing.csv")
print(f"Exit code: {code}")
```

`typer.echo(..., err=True)` writes to stderr instead of stdout.

## Input Validation and Exit Codes at a Glance

| Pattern | What it does |
|---|---|
| Validate early, before work starts | All errors appear at the top, cleanly |
| Print errors to `sys.stderr` | Does not mix with stdout output |
| `sys.exit(0)` | Signal success to the calling shell |
| `sys.exit(1)` | Signal failure |
| `raise typer.BadParameter(msg)` | Show a formatted validation error in typer |
| `raise typer.Exit(code=N)` | Exit with a specific code in typer |

## Your Turn

Add full input validation to the `import_books` command: validate that the file exists, that `--branch` is one of `["main", "east", "west", "north", "south"]`, and that `--limit` is a positive integer if provided. Print all validation errors before exiting.

## Conclusion

Good CLIs validate all inputs at the start, before doing any work. Errors go to stderr so they do not pollute stdout output. Exit codes communicate success and failure to calling scripts. The next lessons cover entry points (making a CLI installable and runnable by name), and UX best practices that make CLIs a pleasure to use.
