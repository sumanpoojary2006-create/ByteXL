## Introduction

Priya's import command accepts a `--date` option. A librarian passes `2026-13-45` as the date. The import script starts processing, reaches the date comparison, and crashes with a `ValueError: time data '2026-13-45' does not match format '%Y-%m-%d'`. The crash is confusing because the error appears in the middle of output, not at the start.

The principle: validate early, exit cleanly. Check all user-provided values at the start of the command, before doing any real work. If anything is invalid, print a clear error message and exit with a non-zero code.

![Two timelines: top shows late validation where processing starts and fails mid-way; bottom shows early validation where all checks happen before any work starts, with a clean error message at the top](images/05_input_validation_exit_codes.png)

## Validate Early

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-05-input-validation-and-exit-co-001-55af8949d3.html"
 width="100%"
></iframe>

## Validation Patterns

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-05-input-validation-and-exit-co-002-03029a50be.html"
 width="100%"
></iframe>

## typer Validation with Callbacks

In `typer`, validation can be done with the `callback` parameter of `typer.Option`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-05-input-validation-and-exit-co-003-9ea9e8710a.html"
 width="100%"
></iframe>

`typer.BadParameter` produces a well-formatted error and exits with code 2.

## Exit Codes

Exit codes are the CLI's way of communicating success or failure to the calling process (shell, script, CI):

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-05-input-validation-and-exit-co-004-fe18478100.html"
 width="100%"
></iframe>

Shell scripts can check exit codes:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-05-input-validation-and-exit-co-005-b7758f75ce.html"
 width="100%"
></iframe>

`||` runs the second command only if the first fails (non-zero exit).

## typer's raise typer.Exit

In `typer`, use `raise typer.Exit(code=N)` instead of `sys.exit(N)`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-12-cli-application-development-05-input-validation-and-exit-co-006-162669cf67.html"
 width="100%"
></iframe>

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
