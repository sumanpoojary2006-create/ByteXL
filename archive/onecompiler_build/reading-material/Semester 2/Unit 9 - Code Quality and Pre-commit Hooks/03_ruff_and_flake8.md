## Introduction

Raj's team has agreed on PEP 8, but enforcing it manually in code reviews is tedious and inconsistent. Different reviewers catch different issues. The same reviewer catches different things on Monday and Friday. What the team needs is a tool that checks style rules the same way every time, in milliseconds.

That tool is a linter. `ruff` is the modern choice: it is written in Rust and is 10-100x faster than its predecessor `flake8`, while covering a superset of `flake8`'s rules. This lesson covers how to use `ruff` to find and fix style issues automatically.

![A terminal showing ruff output: a list of files with line numbers, rule codes (E501, W291, F401), and one-line descriptions of each violation, followed by a fix command](images/03_ruff_flake8.png)

## Installing and Running ruff

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3J1ZmZfYW5kX2ZsYWtlOCBjb2RlIDEiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDAxLnNoIiwiY29kZSI6InBpcCBpbnN0YWxsIHJ1ZmZcblxuIyBDaGVjayBhbGwgUHl0aG9uIGZpbGVzIGluIHRoZSBwcm9qZWN0OlxucnVmZiBjaGVjayAuXG5cbiMgQ2hlY2sgYSBzcGVjaWZpYyBmaWxlOlxucnVmZiBjaGVjayBsaWJyYXJ5L2ZpbmVzLnB5XG5cbiMgQXV0by1maXggZml4YWJsZSBpc3N1ZXM6XG5ydWZmIGNoZWNrIC0tZml4IC4ifQ"
 width="100%"
></iframe>

Sample output:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3J1ZmZfYW5kX2ZsYWtlOCBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoibGlicmFyeS9maW5lcy5weTozOjE6IEY0MDEgYG9zYCBpbXBvcnRlZCBidXQgdW51c2VkXG5saWJyYXJ5L2NhdGFsb2cucHk6MjI6ODk6IEU1MDEgTGluZSB0b28gbG9uZyAoOTIgPiA4OCBjaGFyYWN0ZXJzKVxubGlicmFyeS9ub3RpZmljYXRpb25zLnB5Ojc6MTogRjg0MSBMb2NhbCB2YXJpYWJsZSBgY29ubmAgaXMgYXNzaWduZWQgdG8gYnV0IG5ldmVyIHVzZWRcbkZvdW5kIDMgZXJyb3JzLlxuWypdIDEgZml4YWJsZSB3aXRoIHRoZSBgLS1maXhgIG9wdGlvbi4ifQ"
 width="100%"
></iframe>

## Rule Codes

`ruff` organizes rules into named groups. Each violation has a code like `E501` or `F401`:

| Prefix | Category | Examples |
|---|---|---|
| `E` | Style errors (PEP 8) | `E501` line too long, `E302` missing blank lines |
| `W` | Style warnings | `W291` trailing whitespace |
| `F` | Pyflakes (logic issues) | `F401` unused import, `F841` unused variable, `F821` undefined name |
| `I` | Import sorting (isort) | `I001` imports not sorted |
| `N` | Naming conventions | `N802` function name should be lowercase |
| `UP` | Pyupgrade (modern Python) | `UP007` use `X \| Y` instead of `Union[X, Y]` |

## Configuring ruff

Configuration lives in `pyproject.toml`:

```toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "N", "UP"]   # which rule groups to enable
ignore = ["E501"]                            # ignore line-too-long (let black handle it)
```

## Ignoring Specific Lines

When a violation is intentional, annotate the line:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3J1ZmZfYW5kX2ZsYWtlOCBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiaW1wb3J0IG9zICAjIG5vcWE6IEY0MDEgICAtLSBzdXBwcmVzcyB1bnVzZWQgaW1wb3J0IHdhcm5pbmcgb24gdGhpcyBsaW5lIG9ubHkifQ"
 width="100%"
></iframe>

`noqa` (no quality assurance) tells the linter to skip that line. Overuse of `noqa` defeats the purpose; use it only for genuine exceptions.

## ruff vs flake8

`ruff` is a drop-in replacement for `flake8` in almost all cases. It also replaces `isort` (import sorting), `pyupgrade` (modern syntax), and several other plugins. The main reasons to choose `ruff` over `flake8`:

- `ruff` is 10-100x faster (written in Rust; an entire repo checks in milliseconds)
- `ruff check --fix` auto-fixes many issues
- One tool replaces several plugins

`flake8` remains widely used in existing projects because it has a large plugin ecosystem. Both follow the same rule numbering scheme.

## Running as Part of a Git Workflow

Raj's goal is to run `ruff` automatically before every commit, so style violations are caught locally before they reach CI. The next lessons cover `pre-commit` hooks which make this happen.

For now, running manually confirms the tool is working:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3J1ZmZfYW5kX2ZsYWtlOCBjb2RlIDQiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDA0LnNoIiwiY29kZSI6IiMgQ2hlY2sgYW5kIGF1dG8tZml4XG5ydWZmIGNoZWNrIC0tZml4IC5cblxuIyBTaG93IHJlbWFpbmluZyB1bmZpeGFibGUgaXNzdWVzXG5ydWZmIGNoZWNrIC4ifQ"
 width="100%"
></iframe>

## ruff / Linting at a Glance

| Command | What it does |
|---|---|
| `ruff check .` | Check all Python files for violations |
| `ruff check --fix .` | Fix auto-fixable violations |
| `ruff check file.py` | Check one file |
| `# noqa: CODE` | Suppress a specific warning on one line |
| `pyproject.toml [tool.ruff.lint]` | Configure selected rules and ignores |

## Your Turn

Install `ruff` and run it on a Python project from this semester. Examine the first five violations it finds and categorize them by prefix (E, F, W, I, N). For each one:
1. Read the rule description (`ruff rule E501` prints it)
2. Decide whether to fix it, configure it away, or suppress it with `noqa`

Then add a `[tool.ruff.lint]` section to `pyproject.toml` with your team's agreed rule set.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3J1ZmZfYW5kX2ZsYWtlOCBjb2RlIDUiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDA1LnNoIiwiY29kZSI6IiMgSW5zdGFsbCBhbmQgY2hlY2tcbnBpcCBpbnN0YWxsIHJ1ZmZcbnJ1ZmYgY2hlY2sgLlxuXG4jIExvb2sgdXAgYSBzcGVjaWZpYyBydWxlOlxucnVmZiBydWxlIEY0MDFcbiMgT3V0cHV0czogRjQwMTogYHtuYW1lfWAgaW1wb3J0ZWQgYnV0IHVudXNlZCAuLi4ifQ"
 width="100%"
></iframe>

## Conclusion

`ruff` is a fast linter that catches PEP 8 style issues, unused imports, undefined variables, and sorting problems in milliseconds. It auto-fixes many violations. Configuration lives in `pyproject.toml`. The next lesson adds the final automated style tool: `black`, the opinionated code formatter that enforces consistent style by rewriting code, not just flagging it.
