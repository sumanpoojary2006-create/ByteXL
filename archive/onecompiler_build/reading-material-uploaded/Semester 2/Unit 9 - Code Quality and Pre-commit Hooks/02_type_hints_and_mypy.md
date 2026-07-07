## Introduction

Raj's library system had a bug last month: a function that expected an integer number of days was passed the string `"14"` from a form input. The multiplication `"14" * 0.50` returned `"1414141414141414141414141414"` -- a 28-character string -- because Python's `*` operator repeats strings. No error was raised. The bug silently produced wrong output for days before anyone noticed.

Type hints would have caught this at analysis time. `mypy` would have flagged the function call as incorrect before the code ever ran.

![A function signature with and without type hints: without hints, a wrong type is passed silently; with hints and mypy, a red underline appears at the call site before the code runs](images/02_type_hints_mypy.png)

## What Type Hints Are

Type hints are optional annotations that describe what type a variable, parameter, or return value should be. Python itself ignores them at runtime -- they are metadata. Tools like `mypy` read the annotations and flag type mismatches.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-02-type-hints-and-mypy-001-889ca103f7.html"
 width="100%"
></iframe>

## Built-in Types in Annotations

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-02-type-hints-and-mypy-002-cf5d51fb03.html"
 width="100%"
></iframe>

From Python 3.10+, `X | Y` means "either X or Y". In Python 3.9, use `Optional[X]` from the `typing` module for nullable types. In Python 3.8, use `Union[X, Y]`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-02-type-hints-and-mypy-003-138c9ef314.html"
 width="100%"
></iframe>

## Complex Types

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-02-type-hints-and-mypy-004-3474a3310d.html"
 width="100%"
></iframe>

## Installing and Running mypy

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-02-type-hints-and-mypy-005-35f404e911.html"
 width="100%"
></iframe>

Sample output when a type error exists:

```
library/fines.py:12: error: Argument 1 to "calculate_fine" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

`mypy` reads the type annotations and checks every call site. If a function annotated `-> float` is passed `"14"` where an `int` is expected, it flags the call.

## Gradual Typing

You do not need to annotate everything at once. `mypy` checks only the files and functions it can analyze. Start with the most critical modules:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-02-type-hints-and-mypy-006-00d5914818.html"
 width="100%"
></iframe>

A `py.typed` marker file in the package root tells `mypy` that the package has complete type annotations and should be fully checked.

## dataclasses and TypedDict

For structured data, type hints combine cleanly with `@dataclass`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-02-type-hints-and-mypy-007-d82c25e987.html"
 width="100%"
></iframe>

Every field has an explicit type. `mypy` catches `book.copies = "three"` as a type error.

`TypedDict` is useful for dictionaries with known keys:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-02-type-hints-and-mypy-008-5e38fffda7.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-02-type-hints-and-mypy-009-c4bdef6ebe.html"
 width="100%"
></iframe>

After annotating, run `mypy` and fix any errors it finds.

## Conclusion

Type hints describe expected types; `mypy` checks that callers respect them. Python does not enforce type hints at runtime, but `mypy` catches mismatches statically, before the code runs. The next lesson adds the next layer of automated checking: `ruff`, a linter that enforces PEP 8 style rules and catches common logic errors, faster than any human code reviewer.
