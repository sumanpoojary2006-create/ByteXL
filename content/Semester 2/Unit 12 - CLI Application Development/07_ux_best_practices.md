## Introduction

Priya's CLI works correctly, but librarians complain that they cannot remember the options, the error messages do not explain what is wrong, and the import command gives no feedback during a 20-minute run. A CLI that works is not the same as a CLI that is enjoyable to use. This lesson covers the UX principles that separate professional tools from fragile scripts.

![A terminal window showing four UX improvements: a progress bar during a long operation, colored output distinguishing success (green) and error (red), a --dry-run option, and a friendly --help message with examples](images/07_ux_best_practices.png)

## Principle 1: Give Feedback for Long Operations

A command that runs for 20 seconds with no output looks frozen. Provide progress:

```python
import time

def import_books_with_progress(records, branch="main"):
    """Simulate typer.progressbar feedback during a long operation."""
    total = len(records)
    print(f"Found {total} records. Importing into '{branch}'...")

    for i, record in enumerate(records, 1):
        time.sleep(0.01)   # simulate work per record
        # Simple progress bar: [====    ] 40%
        filled = int(20 * i / total)
        bar = "=" * filled + " " * (20 - filled)
        print(f"\r  Importing [{bar}] {i}/{total}", end="", flush=True)

    print()   # newline after progress bar
    print(f"Done. {total} records imported into '{branch}'.")

sample_records = [{"isbn": f"978-{i:03d}", "title": f"Book {i}"} for i in range(1, 6)]
import_books_with_progress(sample_records, "east")
```

## Principle 2: Use Color Meaningfully

- Green for success
- Yellow for warnings or dry-run messages
- Red for errors

```python
# ANSI color codes (typer uses these internally; terminals render them as colors)
GREEN  = "\033[32m"
YELLOW = "\033[33m"
RED    = "\033[31m"
RESET  = "\033[0m"

def echo(msg, color=RESET):
    print(f"{color}{msg}{RESET}")

# Success (green), Warning (yellow), Error (red)
echo("Import complete: 2,000 records", GREEN)
echo("Warning: 5 records skipped (duplicate ISBN)", YELLOW)
echo("Error: file catalog.csv not found", RED)
```

Check `typer.get_terminal_size()` or use `NO_COLOR` environment variable respecting (typer does this automatically) for scripts that pipe output.

## Principle 3: Provide a --dry-run Mode

Any command that modifies data should have a `--dry-run` flag that shows what would happen without actually doing it:

```python
YELLOW = "\033[33m"
RESET  = "\033[0m"

def import_books(records, branch="main", dry_run=False):
    if dry_run:
        print(f"{YELLOW}[DRY RUN] Would import:{RESET}")
        for r in records[:5]:
            print(f"  {r['isbn']}: {r['title']}")
        if len(records) > 5:
            print(f"  ... and {len(records) - 5} more")
        return

    # Actual import
    for record in records:
        pass   # simulate import_record(record, branch)
    print(f"Imported {len(records)} records into '{branch}'")

sample = [{"isbn": f"978-{i:03d}", "title": f"Book {i}"} for i in range(1, 9)]

print("-- dry run mode --")
import_books(sample, branch="east", dry_run=True)

print("\n-- real run --")
import_books(sample, branch="east", dry_run=False)
```

## Principle 4: Clear, Actionable Error Messages

The best error message says what was wrong, why it is wrong, and what the user can do:

```python
# Contrast: bad vs good error messages
bad_message  = "Error: invalid argument"
good_message = (
    "Error: --branch 'northwest' is not a valid branch.\n"
    "Valid branches: main, east, west, north, south\n"
    "Run 'library-cli branches' to list all available branches."
)

print("BAD error message:")
print(" ", bad_message)
print()
print("GOOD error message:")
print(good_message)
```

```python
VALID_BRANCHES = ["main", "east", "west", "north", "south"]

def validate_branch(branch):
    if branch not in VALID_BRANCHES:
        print(
            f"Error: '{branch}' is not a valid branch.\n"
            f"Valid branches: {', '.join(VALID_BRANCHES)}\n"
            f"Run 'library-cli branches' to list all available branches."
        )
        return None
    return branch

# Demo
for test_branch in ["east", "northwest", "main", "central"]:
    result = validate_branch(test_branch)
    if result:
        print(f"  '{test_branch}' -> valid branch")
    else:
        print(f"  (would exit with code 1)")
    print()
```

## Principle 5: Add --verbose and --quiet Flags

```python
from enum import Enum

class LogLevel(str, Enum):
    quiet   = "quiet"
    normal  = "normal"
    verbose = "verbose"

def import_books(records, file="catalog.csv", log_level=LogLevel.normal):
    if log_level == LogLevel.verbose:
        print(f"Loading file: {file}")
    if log_level != LogLevel.quiet:
        print(f"Importing {len(records)} records...")
    for record in records:
        if log_level == LogLevel.verbose:
            print(f"  Imported: {record['isbn']}")
    if log_level != LogLevel.quiet:
        print(f"Done.")

records = [{"isbn": "978-001", "title": "Dune"}, {"isbn": "978-002", "title": "Foundation"}]

print("=== verbose ===")
import_books(records, log_level=LogLevel.verbose)

print("\n=== normal ===")
import_books(records, log_level=LogLevel.normal)

print("\n=== quiet ===")
import_books(records, log_level=LogLevel.quiet)
print("(no output in quiet mode)")
```

## Principle 6: Confirm Dangerous Operations

For operations that cannot be undone, ask for confirmation before proceeding:

```python
@app.command()
def delete_branch(branch: str, force: bool = typer.Option(False, "--force")):
    """Delete all records for a branch. IRREVERSIBLE."""
    if not force:
        confirmed = typer.confirm(
            f"Delete ALL records for branch '{branch}'? This cannot be undone."
        )
        if not confirmed:
            typer.echo("Aborted.")
            raise typer.Exit()

    # Proceed with deletion
    typer.echo(f"Deleted branch: {branch}")

# Demo:
result = delete_branch(5, True, True)
print(f"delete_branch(5, True, True) ->", result)
```

## CLI UX at a Glance

| Practice | Why it matters |
|---|---|
| Progress bar for long ops | Tells users the program is working |
| Meaningful color | Visual hierarchy; errors stand out |
| `--dry-run` mode | Safe to explore before committing |
| Actionable error messages | User knows what to fix |
| `--verbose` / `--quiet` | Adaptable to scripting and interactive use |
| Confirm before destructive ops | Prevents accidental data loss |

## Your Turn

Add two improvements to any command you have built:
1. A progress bar using `typer.progressbar` for an operation with many items
2. A confirmation prompt for any destructive operation using `typer.confirm`

Test that `--force` bypasses the confirmation for scripted use.

## Conclusion

A CLI that works is not enough. The best CLIs give feedback during long operations, use color meaningfully, offer dry-run modes, write clear error messages, and confirm before deleting data. These practices make the difference between a tool that users trust and one they avoid. Unit 13 moves to the persistence layer that most CLI tools depend on: database interaction with Python.
