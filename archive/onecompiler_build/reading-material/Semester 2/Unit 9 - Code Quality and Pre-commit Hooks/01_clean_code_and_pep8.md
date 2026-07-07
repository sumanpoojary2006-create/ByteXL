## Introduction

Raj joined the library consortium's engineering team six months ago. In every code review, the same comment threads appear: "this variable name is too short," "this line is 110 characters wide," "add a blank line before this function." His team wastes an hour each sprint debating style in reviews instead of discussing design.

His proposal: agree on a style standard, enforce it automatically, and stop discussing it in reviews. The starting point is PEP 8, Python's official style guide, and the first question is: what does it actually say and why?

![A code snippet shown before and after PEP 8: unclear variable names, crowded spacing, and long lines on the left; clean names, breathing room, and consistent indentation on the right](images/01_clean_code_pep8.png)

## What PEP 8 Is

PEP 8 is the Style Guide for Python Code, written by Guido van Rossum and published as a Python Enhancement Proposal. It covers naming, whitespace, imports, and line length. Most Python projects follow it, which means any Python developer can read any PEP 8-compliant codebase without adjusting to a personal style.

The most important rule in PEP 8: "A Foolish Consistency is the Hobgoblin of Little Minds." The guide is not the law. Deviation is acceptable when it makes the code clearer. But within a project, consistency matters more than any single rule.

## Naming Conventions

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2NsZWFuX2NvZGVfYW5kX3BlcDggY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6IiMgVmFyaWFibGVzIGFuZCBmdW5jdGlvbnM6IGxvd2VyY2FzZV93aXRoX3VuZGVyc2NvcmVzIChzbmFrZV9jYXNlKVxuYm9va19jb3VudCA9IDBcbm1heF9sb2FuX2RheXMgPSAyMVxuXG5kZWYgY2FsY3VsYXRlX2ZpbmUoZGF5c19vdmVyZHVlLCBkYWlseV9yYXRlPTAuNTApOlxuICAgIHJldHVybiBkYXlzX292ZXJkdWUgKiBkYWlseV9yYXRlXG5cbiMgQ2xhc3NlczogQ2FwV29yZHMgKFBhc2NhbENhc2UpXG5jbGFzcyBMaWJyYXJ5SXRlbTpcbiAgICBwYXNzXG5cbmNsYXNzIEVCb29rQ2F0YWxvZzpcbiAgICBwYXNzXG5cbiMgQ29uc3RhbnRzOiBBTExfQ0FQU19XSVRIX1VOREVSU0NPUkVTXG5NQVhfTE9BTl9QRVJJT0RfREFZUyA9IDIxXG5ERUZBVUxUX0ZJTkVfUkFURSA9IDAuNTBcblxuIyBQcml2YXRlIC8gaW50ZXJuYWw6IHNpbmdsZSBsZWFkaW5nIHVuZGVyc2NvcmVcbmNsYXNzIEJvb2s6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBzZWxmLl9jb3BpZXMgPSAwICAgICAgICAjIHByb3RlY3RlZDogY29udmVudGlvbiBvbmx5XG4gICAgICAgIHNlbGYuX19jaGVja3N1bSA9IFwiXCIgICAgIyBwcml2YXRlOiBuYW1lLW1hbmdsZWRcblxuIyBEdW5kZXIgbWV0aG9kczogZG91YmxlIGxlYWRpbmcgYW5kIHRyYWlsaW5nIHVuZGVyc2NvcmVzXG5kZWYgX19yZXByX18oc2VsZik6XG4gICAgcmV0dXJuIGZcIkJvb2soe3NlbGYuaXNibiFyfSlcIiJ9"
 width="100%"
></iframe>

## Whitespace

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2NsZWFuX2NvZGVfYW5kX3BlcDggY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6IiMgR29vZDogc3BhY2VzIGFyb3VuZCBvcGVyYXRvcnNcbnJlc3VsdCA9IGRheXNfb3ZlcmR1ZSAqIGRhaWx5X3JhdGVcbnRvdGFsID0gYSArIGJcblxuIyBCYWQ6IG5vIHNwYWNlc1xucmVzdWx0PWRheXNfb3ZlcmR1ZSpkYWlseV9yYXRlXG5cbiMgR29vZDogbm8gc3BhY2UgYmVmb3JlIHRoZSBjb2xvbiBpbiBzbGljZXMgYW5kIGZ1bmN0aW9uIGNhbGxzXG5ib29rc1sxOjVdXG5jYWxjdWxhdGVfZmluZShkYXlzLCByYXRlPTAuNTApXG5cbiMgQmFkOiBleHRyYSBzcGFjZXNcbmJvb2tzIFsxOjVdXG5jYWxjdWxhdGVfZmluZSggZGF5cyAsIHJhdGUgPSAwLjUwIClcblxuIyBHb29kOiBibGFuayBsaW5lcyB0byBzZXBhcmF0ZSBsb2dpY2FsIHNlY3Rpb25zXG5jbGFzcyBDYXRhbG9nOlxuXG4gICAgZGVmIF9faW5pdF9fKHNlbGYpOlxuICAgICAgICBzZWxmLl9ib29rcyA9IFtdXG5cbiAgICBkZWYgYWRkKHNlbGYsIGJvb2spOlxuICAgICAgICBzZWxmLl9ib29rcy5hcHBlbmQoYm9vaylcblxuICAgIGRlZiBmaW5kKHNlbGYsIGlzYm4pOlxuICAgICAgICByZXR1cm4gbmV4dCgoYiBmb3IgYiBpbiBzZWxmLl9ib29rcyBpZiBiLmlzYm4gPT0gaXNibiksIE5vbmUpIn0"
 width="100%"
></iframe>

## Line Length

PEP 8 recommends a maximum of 79 characters per line (72 for docstrings). Many teams use 88 or 100 characters, which is the `black` formatter's default. The principle is: keep lines short enough that two files can be opened side by side.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2NsZWFuX2NvZGVfYW5kX3BlcDggY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6IiMgVG9vIGxvbmc6XG5yZXN1bHQgPSBjYWxjdWxhdGVfb3ZlcmR1ZV9maW5lKGRheXNfb3ZlcmR1ZT1yZWNvcmRbXCJkYXlzX292ZXJkdWVcIl0sIGRhaWx5X3JhdGU9Y29uZmlnW1wiZmluZV9yYXRlX3Blcl9kYXlcIl0pXG5cbiMgQmV0dGVyOiBicmVhayBhdCBhIG5hdHVyYWwgcG9pbnRcbnJlc3VsdCA9IGNhbGN1bGF0ZV9vdmVyZHVlX2ZpbmUoXG4gICAgZGF5c19vdmVyZHVlPXJlY29yZFtcImRheXNfb3ZlcmR1ZVwiXSxcbiAgICBkYWlseV9yYXRlPWNvbmZpZ1tcImZpbmVfcmF0ZV9wZXJfZGF5XCJdXG4pIn0"
 width="100%"
></iframe>

## Import Order

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2NsZWFuX2NvZGVfYW5kX3BlcDggY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6IiMgUEVQIDggaW1wb3J0IG9yZGVyOiBzdGRsaWIsIHRoZW4gdGhpcmQtcGFydHksIHRoZW4gbG9jYWwgKGVhY2ggZ3JvdXAgc2VwYXJhdGVkIGJ5IGEgYmxhbmsgbGluZSlcbmltcG9ydCBvc1xuaW1wb3J0IHN5c1xuZnJvbSBwYXRobGliIGltcG9ydCBQYXRoXG5cbmltcG9ydCBweXRlc3RcbmltcG9ydCByZXF1ZXN0c1xuXG5mcm9tIGxpYnJhcnkuY2F0YWxvZyBpbXBvcnQgQ2F0YWxvZ1xuZnJvbSBsaWJyYXJ5LmZpbmVzIGltcG9ydCBjYWxjdWxhdGVfZmluZSJ9"
 width="100%"
></iframe>

The `ruff` and `isort` tools enforce this order automatically.

## What PEP 8 Does Not Cover

PEP 8 does not cover variable naming quality (only style), function length, complexity, or architecture. A variable named `x` with an underscore is PEP 8-compliant but incomprehensible. "Clean code" goes beyond style:

- Functions do one thing
- Names describe intent: `days_overdue` not `d`, `patron_id` not `pid`
- Functions are short enough to read without scrolling
- Logic is expressed directly, not obscured by complexity

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2NsZWFuX2NvZGVfYW5kX3BlcDggY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IiMgUEVQIDgtY29tcGxpYW50IGJ1dCBwb29yOlxuZGVmIGYoZCwgcik6XG4gICAgcmV0dXJuIGQgKiByXG5cbiMgUEVQIDgtY29tcGxpYW50IGFuZCBjbGVhcjpcbmRlZiBjYWxjdWxhdGVfZmluZShkYXlzX292ZXJkdWUsIGRhaWx5X3JhdGU9MC41MCk6XG4gICAgcmV0dXJuIGRheXNfb3ZlcmR1ZSAqIGRhaWx5X3JhdGUifQ"
 width="100%"
></iframe>

## PEP 8 / Clean Code at a Glance

| Rule | Convention |
|---|---|
| Variables, functions | `snake_case` |
| Classes | `PascalCase` |
| Constants | `ALL_CAPS` |
| Max line length | 79 (PEP 8) or 88 (black) |
| Import order | stdlib, third-party, local |
| Blank lines | 2 between top-level, 1 inside class |

## Your Turn

Open any Python file you have written and apply PEP 8 manually:
1. Rename any single-letter variables (except loop counters) to descriptive names
2. Confirm function names use `snake_case` and class names use `PascalCase`
3. Check that imports are grouped and ordered correctly
4. Find any line longer than 88 characters and break it at a natural point

Then run `python -m pep8 yourfile.py` or the next lesson's tool to confirm automatically.

## Conclusion

PEP 8 provides naming, whitespace, and import conventions that make Python code consistent and readable to any Python developer. Clean code goes beyond style to include naming quality, function focus, and simplicity. The next lesson introduces type hints and `mypy`, which catch entire classes of bugs that PEP 8 cannot: passing the wrong type to a function.
