## Introduction

Even with `ruff` checking style, Raj's team still argues about formatting in code reviews: single quotes or double quotes? Trailing commas or not? How to break a long function call across lines? These are not bugs -- they are preference, and debating preferences in reviews is a waste of time.

`black` is "The Uncompromising Code Formatter." It makes exactly one formatting choice for each situation and applies it consistently. You do not configure it (much). You just run it. Code review debates about formatting become impossible because `black` has already decided.

![A before-and-after showing inconsistently formatted code with mixed quotes and varied spacing on the left, and uniformly black-formatted code on the right](images/04_black.png)

## Installing and Running black

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-04-black-001-5aa7933845.html"
 width="100%"
></iframe>

`black .` reformats files in place. `black --check .` is used in CI pipelines to verify that committed code is already formatted.

## What black Does

`black` makes consistent, opinionated choices:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-04-black-002-04f0ea814a.html"
 width="100%"
></iframe>

Key choices `black` makes:
- Double quotes for all strings (configurable only to single)
- Spaces around binary operators
- No space before `=` in keyword arguments
- Trailing comma after the last element in a multi-line collection
- 88-character line length by default
- Long expressions broken consistently at a magic trailing comma

## The Magic Trailing Comma

If you add a trailing comma after the last element in a collection or function call, `black` treats it as a signal to keep the structure expanded across multiple lines, even if it fits on one line:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-04-black-003-1105d89e9e.html"
 width="100%"
></iframe>

## Configuring black

`black` has very few configuration options. The most common is line length:

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ["py311"]
```

Leave `line-length` at 88 unless there is a project-specific reason to change it. Using the default means `black` and `ruff`'s `E501` check agree on the maximum.

## black vs. Manual Formatting

The philosophy of `black` is: consistency over preference. You may not like every formatting choice it makes. That is expected. The trade-off is: you spend zero time debating formatting, and every developer's code looks the same after formatting. For most teams, this is a net gain.

The one thing `black` does not do: rename variables or restructure logic. It only changes whitespace and quotes. Style and logic are separate concerns.

## Integrating black with ruff

`ruff` includes formatting rules that overlap with `black`. The standard integration is to run `black` for formatting and `ruff` for linting, and disable `ruff`'s format-overlap rules:

```toml
[tool.ruff.lint]
# Disable rules that black handles (formatting)
extend-ignore = ["E501", "W503"]
```

Alternatively, `ruff format` (introduced in ruff 0.1.0+) is a `black`-compatible formatter. Check your team's tool version to decide which to use.

## black at a Glance

| Command | What it does |
|---|---|
| `black .` | Format all files in place |
| `black --check .` | Fail if any file would change (for CI) |
| `black --diff .` | Show diffs without modifying |
| `# fmt: off` / `# fmt: on` | Disable black for a section |

## Your Turn

Run `black --diff library/` on the library project. Read the diff output and identify three formatting changes `black` would make. Then run `black library/` to apply them. Confirm the code still runs correctly and all tests still pass.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-04-black-004-990473ae59.html"
 width="100%"
></iframe>

## Conclusion

`black` ends formatting debates by making consistent, non-negotiable choices. Run it before committing or in CI with `--check`. The next lesson introduces git hooks, the mechanism that runs tools like `ruff` and `black` automatically at commit time, before any code reaches the shared repository.
