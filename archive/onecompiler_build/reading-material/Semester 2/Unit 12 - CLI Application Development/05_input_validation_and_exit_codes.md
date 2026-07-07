## Introduction

Priya's import command accepts a `--date` option. A librarian passes `2026-13-45` as the date. The import script starts processing, reaches the date comparison, and crashes with a `ValueError: time data '2026-13-45' does not match format '%Y-%m-%d'`. The crash is confusing because the error appears in the middle of output, not at the start.

The principle: validate early, exit cleanly. Check all user-provided values at the start of the command, before doing any real work. If anything is invalid, print a clear error message and exit with a non-zero code.

![Two timelines: top shows late validation where processing starts and fails mid-way; bottom shows early validation where all checks happen before any work starts, with a clean error message at the top](images/05_input_validation_exit_codes.png)

## Validate Early

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2lucHV0X3ZhbGlkYXRpb25fYW5kX2V4aXRfY29kZXMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImltcG9ydCBhcmdwYXJzZVxuaW1wb3J0IHN5c1xuZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZVxuXG5kZWYgdmFsaWRhdGVfZGF0ZSh2YWx1ZTogc3RyKSAtPiBkYXRlOlxuICAgIHRyeTpcbiAgICAgICAgcmV0dXJuIGRhdGUuZnJvbWlzb2Zvcm1hdCh2YWx1ZSlcbiAgICBleGNlcHQgVmFsdWVFcnJvcjpcbiAgICAgICAgcHJpbnQoZlwiRXJyb3I6IGludmFsaWQgZGF0ZSAne3ZhbHVlfScuIEV4cGVjdGVkIFlZWVktTU0tRERcIiwgZmlsZT1zeXMuc3RkZXJyKVxuICAgICAgICBzeXMuZXhpdCgxKVxuXG5kZWYgbWFpbigpOlxuICAgIHBhcnNlciA9IGFyZ3BhcnNlLkFyZ3VtZW50UGFyc2VyKClcbiAgICBwYXJzZXIuYWRkX2FyZ3VtZW50KFwiLS1kYXRlXCIsIHJlcXVpcmVkPVRydWUpXG4gICAgcGFyc2VyLmFkZF9hcmd1bWVudChcIi0tZmlsZVwiLCByZXF1aXJlZD1UcnVlKVxuICAgIGFyZ3MgPSBwYXJzZXIucGFyc2VfYXJncygpXG5cbiAgICAjIFZhbGlkYXRlIEFMTCBpbnB1dHMgYXQgdGhlIHRvcCBiZWZvcmUgYW55IHdvcmsgYmVnaW5zOlxuICAgIHJlcG9ydF9kYXRlID0gdmFsaWRhdGVfZGF0ZShhcmdzLmRhdGUpXG4gICAgZmlsZV9wYXRoID0gdmFsaWRhdGVfZmlsZShhcmdzLmZpbGUpXG5cbiAgICAjIE5vdyBkbyB0aGUgYWN0dWFsIHdvcms6XG4gICAgZ2VuZXJhdGVfcmVwb3J0KHJlcG9ydF9kYXRlLCBmaWxlX3BhdGgpIn0"
 width="100%"
></iframe>

## Validation Patterns

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2lucHV0X3ZhbGlkYXRpb25fYW5kX2V4aXRfY29kZXMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImltcG9ydCBzeXNcbmZyb20gcGF0aGxpYiBpbXBvcnQgUGF0aFxuXG5kZWYgdmFsaWRhdGVfZmlsZV9leGlzdHMocGF0aDogc3RyKSAtPiBQYXRoOlxuICAgIHAgPSBQYXRoKHBhdGgpXG4gICAgaWYgbm90IHAuZXhpc3RzKCk6XG4gICAgICAgIHByaW50KGZcIkVycm9yOiBmaWxlIG5vdCBmb3VuZDoge3BhdGh9XCIsIGZpbGU9c3lzLnN0ZGVycilcbiAgICAgICAgc3lzLmV4aXQoMSlcbiAgICBpZiBub3QgcC5pc19maWxlKCk6XG4gICAgICAgIHByaW50KGZcIkVycm9yOiBub3QgYSBmaWxlOiB7cGF0aH1cIiwgZmlsZT1zeXMuc3RkZXJyKVxuICAgICAgICBzeXMuZXhpdCgxKVxuICAgIHJldHVybiBwXG5cbmRlZiB2YWxpZGF0ZV9wb3NpdGl2ZV9pbnQodmFsdWU6IHN0ciwgbmFtZTogc3RyKSAtPiBpbnQ6XG4gICAgdHJ5OlxuICAgICAgICBuID0gaW50KHZhbHVlKVxuICAgIGV4Y2VwdCBWYWx1ZUVycm9yOlxuICAgICAgICBwcmludChmXCJFcnJvcjoge25hbWV9IG11c3QgYmUgYW4gaW50ZWdlciwgZ290ICd7dmFsdWV9J1wiLCBmaWxlPXN5cy5zdGRlcnIpXG4gICAgICAgIHN5cy5leGl0KDEpXG4gICAgaWYgbiA8PSAwOlxuICAgICAgICBwcmludChmXCJFcnJvcjoge25hbWV9IG11c3QgYmUgcG9zaXRpdmUsIGdvdCB7bn1cIiwgZmlsZT1zeXMuc3RkZXJyKVxuICAgICAgICBzeXMuZXhpdCgxKVxuICAgIHJldHVybiBuXG5cbmRlZiB2YWxpZGF0ZV9jaG9pY2VzKHZhbHVlOiBzdHIsIGNob2ljZXM6IGxpc3QsIG5hbWU6IHN0cikgLT4gc3RyOlxuICAgIGlmIHZhbHVlIG5vdCBpbiBjaG9pY2VzOlxuICAgICAgICBwcmludChmXCJFcnJvcjoge25hbWV9IG11c3QgYmUgb25lIG9mIHtjaG9pY2VzfSwgZ290ICd7dmFsdWV9J1wiLCBmaWxlPXN5cy5zdGRlcnIpXG4gICAgICAgIHN5cy5leGl0KDEpXG4gICAgcmV0dXJuIHZhbHVlIn0"
 width="100%"
></iframe>

## typer Validation with Callbacks

In `typer`, validation can be done with the `callback` parameter of `typer.Option`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2lucHV0X3ZhbGlkYXRpb25fYW5kX2V4aXRfY29kZXMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImltcG9ydCB0eXBlclxuZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZVxuXG5kZWYgdmFsaWRhdGVfZGF0ZSh2YWx1ZTogc3RyKSAtPiBzdHI6XG4gICAgdHJ5OlxuICAgICAgICBkYXRlLmZyb21pc29mb3JtYXQodmFsdWUpXG4gICAgICAgIHJldHVybiB2YWx1ZVxuICAgIGV4Y2VwdCBWYWx1ZUVycm9yOlxuICAgICAgICByYWlzZSB0eXBlci5CYWRQYXJhbWV0ZXIoZlwiSW52YWxpZCBkYXRlICd7dmFsdWV9Jy4gRXhwZWN0ZWQgWVlZWS1NTS1ERFwiKVxuXG5hcHAgPSB0eXBlci5UeXBlcigpXG5cbkBhcHAuY29tbWFuZCgpXG5kZWYgcmVwb3J0KFxuICAgIGRhdGVfc3RyOiBzdHIgPSB0eXBlci5PcHRpb24oLi4uLCBcIi0tZGF0ZVwiLCBjYWxsYmFjaz12YWxpZGF0ZV9kYXRlLCBoZWxwPVwiWVlZWS1NTS1ERFwiKVxuKTpcbiAgICBcIlwiXCJHZW5lcmF0ZSBhIHJlcG9ydC5cIlwiXCJcbiAgICB0eXBlci5lY2hvKGZcIkdlbmVyYXRpbmcgcmVwb3J0IGZvciB7ZGF0ZV9zdHJ9XCIpXG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICBhcHAoKSJ9"
 width="100%"
></iframe>

`typer.BadParameter` produces a well-formatted error and exits with code 2.

## Exit Codes

Exit codes are the CLI's way of communicating success or failure to the calling process (shell, script, CI):

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2lucHV0X3ZhbGlkYXRpb25fYW5kX2V4aXRfY29kZXMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImltcG9ydCBzeXNcblxuIyBTdWNjZXNzOlxuc3lzLmV4aXQoMCkgICAjIG9yIGp1c3QgcmV0dXJuIGZyb20gbWFpbigpXG5cbiMgRmFpbHVyZSAoZ2VuZXJhbCk6XG5zeXMuZXhpdCgxKVxuXG4jIE1pc3VzZSAoYmFkIGFyZ3VtZW50cykgLS0gYXJncGFyc2UgdXNlcyAyIGJ5IGRlZmF1bHQ6XG5zeXMuZXhpdCgyKVxuXG4jIEN1c3RvbSAoZG9jdW1lbnQgd2hhdCBlYWNoIGNvZGUgbWVhbnMpOlxuIyAwID0gc3VjY2Vzc1xuIyAxID0gcnVudGltZSBlcnJvclxuIyAyID0gaW52YWxpZCBhcmd1bWVudHNcbiMgMyA9IGZpbGUgbm90IGZvdW5kXG4jIDQgPSBwZXJtaXNzaW9uIGRlbmllZCJ9"
 width="100%"
></iframe>

Shell scripts can check exit codes:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2lucHV0X3ZhbGlkYXRpb25fYW5kX2V4aXRfY29kZXMgY29kZSA1IiwibGFuZ3VhZ2UiOiJiYXNoIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5zaCIsImNvZGUiOiJweXRob24gaW1wb3J0X2Jvb2tzLnB5IGNhdGFsb2cuY3N2IHx8IGVjaG8gXCJJbXBvcnQgZmFpbGVkXCIifQ"
 width="100%"
></iframe>

`||` runs the second command only if the first fails (non-zero exit).

## typer's raise typer.Exit

In `typer`, use `raise typer.Exit(code=N)` instead of `sys.exit(N)`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2lucHV0X3ZhbGlkYXRpb25fYW5kX2V4aXRfY29kZXMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6ImltcG9ydCB0eXBlclxuXG5hcHAgPSB0eXBlci5UeXBlcigpXG5cbkBhcHAuY29tbWFuZCgpXG5kZWYgY2hlY2soZmlsZTogc3RyKTpcbiAgICBmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGhcbiAgICBpZiBub3QgUGF0aChmaWxlKS5leGlzdHMoKTpcbiAgICAgICAgdHlwZXIuZWNobyhmXCJFcnJvcjoge2ZpbGV9IG5vdCBmb3VuZFwiLCBlcnI9VHJ1ZSlcbiAgICAgICAgcmFpc2UgdHlwZXIuRXhpdChjb2RlPTEpXG4gICAgdHlwZXIuZWNobyhcIkZpbGUgZm91bmRcIilcblxuaWYgX19uYW1lX18gPT0gXCJfX21haW5fX1wiOlxuICAgIGFwcCgpIn0"
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
