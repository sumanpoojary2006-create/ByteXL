## Introduction

Raj's library system had a bug last month: a function that expected an integer number of days was passed the string `"14"` from a form input. The multiplication `"14" * 0.50` returned `"1414141414141414141414141414"` -- a 28-character string -- because Python's `*` operator repeats strings. No error was raised. The bug silently produced wrong output for days before anyone noticed.

Type hints would have caught this at analysis time. `mypy` would have flagged the function call as incorrect before the code ever ran.

![A function signature with and without type hints: without hints, a wrong type is passed silently; with hints and mypy, a red underline appears at the call site before the code runs](images/02_type_hints_mypy.png)

## What Type Hints Are

Type hints are optional annotations that describe what type a variable, parameter, or return value should be. Python itself ignores them at runtime -- they are metadata. Tools like `mypy` read the annotations and flag type mismatches.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3R5cGVfaGludHNfYW5kX215cHkgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6IiMgV2l0aG91dCB0eXBlIGhpbnRzOiBQeXRob24gYWNjZXB0cyBhbnkgdHlwZSBzaWxlbnRseVxuZGVmIGNhbGN1bGF0ZV9maW5lKGRheXNfb3ZlcmR1ZSwgZGFpbHlfcmF0ZT0wLjUwKTpcbiAgICByZXR1cm4gZGF5c19vdmVyZHVlICogZGFpbHlfcmF0ZVxuXG4jIFdpdGggdHlwZSBoaW50czogaW50ZW50IGlzIGV4cGxpY2l0LCBteXB5IGNhbiB2ZXJpZnkgY2FsbGVyc1xuZGVmIGNhbGN1bGF0ZV9maW5lKGRheXNfb3ZlcmR1ZTogaW50LCBkYWlseV9yYXRlOiBmbG9hdCA9IDAuNTApIC0-IGZsb2F0OlxuICAgIHJldHVybiBkYXlzX292ZXJkdWUgKiBkYWlseV9yYXRlXG5cbiMgVHlwZSBoaW50cyBvbiB2YXJpYWJsZXNcbmJvb2tfY291bnQ6IGludCA9IDBcbmlzYm46IHN0ciA9IFwiOTc4LTAwMVwiXG5jYXRhbG9nOiBsaXN0W3N0cl0gPSBbXSJ9"
 width="100%"
></iframe>

## Built-in Types in Annotations

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3R5cGVfaGludHNfYW5kX215cHkgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImRlZiBmaW5kX2Jvb2soaXNibjogc3RyLCBjYXRhbG9nOiBsaXN0KSAtPiBkaWN0IHwgTm9uZTpcbiAgICBmb3IgYm9vayBpbiBjYXRhbG9nOlxuICAgICAgICBpZiBib29rW1wiaXNiblwiXSA9PSBpc2JuOlxuICAgICAgICAgICAgcmV0dXJuIGJvb2tcbiAgICByZXR1cm4gTm9uZSJ9"
 width="100%"
></iframe>

From Python 3.10+, `X | Y` means "either X or Y". In Python 3.9, use `Optional[X]` from the `typing` module for nullable types. In Python 3.8, use `Union[X, Y]`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3R5cGVfaGludHNfYW5kX215cHkgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6IiMgUHl0aG9uIDMuMTArXG5kZWYgZmluZChpc2JuOiBzdHIpIC0-IGRpY3QgfCBOb25lOiAuLi5cblxuIyBQeXRob24gMy45IGFuZCBlYXJsaWVyXG5mcm9tIHR5cGluZyBpbXBvcnQgT3B0aW9uYWwsIFVuaW9uXG5kZWYgZmluZChpc2JuOiBzdHIpIC0-IE9wdGlvbmFsW2RpY3RdOiAuLi4ifQ"
 width="100%"
></iframe>

## Complex Types

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3R5cGVfaGludHNfYW5kX215cHkgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImZyb20gdHlwaW5nIGltcG9ydCBDYWxsYWJsZVxuXG4jIExpc3Qgb2Ygc3RyaW5nc1xuZGVmIHByb2Nlc3ModGl0bGVzOiBsaXN0W3N0cl0pIC0-IE5vbmU6IC4uLlxuXG4jIERpY3Rpb25hcnkgbWFwcGluZyBzdHJpbmcgdG8gaW50XG5kZWYgZ2V0X2NvdW50cygpIC0-IGRpY3Rbc3RyLCBpbnRdOiAuLi5cblxuIyBUdXBsZSBvZiBmaXhlZCB0eXBlc1xuZGVmIGdldF9sb2NhdGlvbigpIC0-IHR1cGxlW2Zsb2F0LCBmbG9hdF06IC4uLlxuXG4jIEEgY2FsbGFibGUgdGhhdCB0YWtlcyBhbiBpbnQgYW5kIHJldHVybnMgYSBmbG9hdFxuZGVmIGFwcGx5KGZuOiBDYWxsYWJsZVtbaW50XSwgZmxvYXRdLCB2YWx1ZTogaW50KSAtPiBmbG9hdDpcbiAgICByZXR1cm4gZm4odmFsdWUpIn0"
 width="100%"
></iframe>

## Installing and Running mypy

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3R5cGVfaGludHNfYW5kX215cHkgY29kZSA1IiwibGFuZ3VhZ2UiOiJiYXNoIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5zaCIsImNvZGUiOiJwaXAgaW5zdGFsbCBteXB5XG5teXB5IGxpYnJhcnkvZmluZXMucHkifQ"
 width="100%"
></iframe>

Sample output when a type error exists:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3R5cGVfaGludHNfYW5kX215cHkgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6ImxpYnJhcnkvZmluZXMucHk6MTI6IGVycm9yOiBBcmd1bWVudCAxIHRvIFwiY2FsY3VsYXRlX2ZpbmVcIiBoYXMgaW5jb21wYXRpYmxlIHR5cGUgXCJzdHJcIjsgZXhwZWN0ZWQgXCJpbnRcIlxuRm91bmQgMSBlcnJvciBpbiAxIGZpbGUgKGNoZWNrZWQgMSBzb3VyY2UgZmlsZSkifQ"
 width="100%"
></iframe>

`mypy` reads the type annotations and checks every call site. If a function annotated `-> float` is passed `"14"` where an `int` is expected, it flags the call.

## Gradual Typing

You do not need to annotate everything at once. `mypy` checks only the files and functions it can analyze. Start with the most critical modules:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3R5cGVfaGludHNfYW5kX215cHkgY29kZSA3IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA3LnB5IiwiY29kZSI6IiMgRnVsbHkgYW5ub3RhdGVkIC0tIG15cHkgY2hlY2tzIGV2ZXJ5dGhpbmdcbmRlZiByZXNlcnZlKGlzYm46IHN0ciwgcGF0cm9uX2lkOiBzdHIsIGRheXM6IGludCkgLT4gYm9vbDpcbiAgICAuLi5cblxuIyBQYXJ0aWFsbHkgYW5ub3RhdGVkIC0tIG15cHkgY2hlY2tzIG9ubHkgdGhlIGFubm90YXRlZCBwYXJ0c1xuZGVmIHJlc2VydmUoaXNibiwgcGF0cm9uX2lkLCBkYXlzOiBpbnQpOlxuICAgIC4uLlxuXG4jIFVuYW5ub3RhdGVkIC0tIG15cHkgc2tpcHMgdGhpcyBmdW5jdGlvblxuZGVmIHJlc2VydmUoaXNibiwgcGF0cm9uX2lkLCBkYXlzKTpcbiAgICAuLi4ifQ"
 width="100%"
></iframe>

A `py.typed` marker file in the package root tells `mypy` that the package has complete type annotations and should be fully checked.

## dataclasses and TypedDict

For structured data, type hints combine cleanly with `@dataclass`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3R5cGVfaGludHNfYW5kX215cHkgY29kZSA4IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA4LnB5IiwiY29kZSI6ImZyb20gZGF0YWNsYXNzZXMgaW1wb3J0IGRhdGFjbGFzc1xuXG5AZGF0YWNsYXNzXG5jbGFzcyBCb29rOlxuICAgIGlzYm46IHN0clxuICAgIHRpdGxlOiBzdHJcbiAgICBnZW5yZTogc3RyXG4gICAgY29waWVzOiBpbnRcblxuICAgIGRlZiBpc19hdmFpbGFibGUoc2VsZikgLT4gYm9vbDpcbiAgICAgICAgcmV0dXJuIHNlbGYuY29waWVzID4gMCJ9"
 width="100%"
></iframe>

Every field has an explicit type. `mypy` catches `book.copies = "three"` as a type error.

`TypedDict` is useful for dictionaries with known keys:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3R5cGVfaGludHNfYW5kX215cHkgY29kZSA5IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA5LnB5IiwiY29kZSI6ImZyb20gdHlwaW5nIGltcG9ydCBUeXBlZERpY3RcblxuY2xhc3MgQm9ycm93UmVjb3JkKFR5cGVkRGljdCk6XG4gICAgaXNibjogc3RyXG4gICAgcGF0cm9uX2lkOiBzdHJcbiAgICBib3Jyb3dfZGF0ZTogc3RyXG4gICAgbG9hbl9kYXlzOiBpbnQifQ"
 width="100%"
></iframe>

## Type Hints and mypy at a Glance

| Syntax | Meaning |
|---|---|
| `x: int` | x should be an int |
| `x: str \| None` | x is a string or None |
| `-> float` | function returns a float |
| `list[str]` | list whose elements are strings |
| `dict[str, int]` | dict mapping string keys to int values |
| `Callable[[int], float]` | callable taking int, returning float |

## Your Turn

Add type hints to these three functions from earlier units:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX3R5cGVfaGludHNfYW5kX215cHkgY29kZSAxMCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAxMC5weSIsImNvZGUiOiJmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRlLCB0aW1lZGVsdGFcblxuZGVmIG92ZXJkdWVfcmVwb3J0KHJlY29yZHMsIHRvZGF5PU5vbmUpOlxuICAgIHRvZGF5ID0gdG9kYXkgb3IgZGF0ZS50b2RheSgpXG4gICAgb3ZlcmR1ZSA9IFtdXG4gICAgZm9yIHJlY29yZCBpbiByZWNvcmRzOlxuICAgICAgICBib3Jyb3cgPSBkYXRlLmZyb21pc29mb3JtYXQocmVjb3JkW1wiYm9ycm93X2RhdGVcIl0pXG4gICAgICAgIGR1ZSA9IGJvcnJvdyArIHRpbWVkZWx0YShkYXlzPXJlY29yZFtcImxvYW5fZGF5c1wiXSlcbiAgICAgICAgaWYgdG9kYXkgPiBkdWU6XG4gICAgICAgICAgICBvdmVyZHVlLmFwcGVuZCh7KipyZWNvcmQsIFwiZGF5c19vdmVyZHVlXCI6ICh0b2RheSAtIGR1ZSkuZGF5c30pXG4gICAgcmV0dXJuIG92ZXJkdWVcblxuZGVmIGNhbGN1bGF0ZV9maW5lKGRheXNfb3ZlcmR1ZSwgZGFpbHlfcmF0ZT0wLjUwKTpcbiAgICBpZiBkYXlzX292ZXJkdWUgPCAwOlxuICAgICAgICByYWlzZSBWYWx1ZUVycm9yKFwiY2Fubm90IGJlIG5lZ2F0aXZlXCIpXG4gICAgcmV0dXJuIGRheXNfb3ZlcmR1ZSAqIGRhaWx5X3JhdGVcblxuZGVmIGZpbmRfYm9vayhpc2JuLCBjYXRhbG9nKTpcbiAgICByZXR1cm4gbmV4dCgoYiBmb3IgYiBpbiBjYXRhbG9nIGlmIGIuaXNibiA9PSBpc2JuKSwgTm9uZSkifQ"
 width="100%"
></iframe>

After annotating, run `mypy` and fix any errors it finds.

## Conclusion

Type hints describe expected types; `mypy` checks that callers respect them. Python does not enforce type hints at runtime, but `mypy` catches mismatches statically, before the code runs. The next lesson adds the next layer of automated checking: `ruff`, a linter that enforces PEP 8 style rules and catches common logic errors, faster than any human code reviewer.
