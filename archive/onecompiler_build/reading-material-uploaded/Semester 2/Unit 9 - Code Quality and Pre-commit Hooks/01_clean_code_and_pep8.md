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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-01-clean-code-and-pep8-001-9e27bbd6fb.html"
 width="100%"
></iframe>

## Whitespace

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-01-clean-code-and-pep8-002-87a3a23333.html"
 width="100%"
></iframe>

## Line Length

PEP 8 recommends a maximum of 79 characters per line (72 for docstrings). Many teams use 88 or 100 characters, which is the `black` formatter's default. The principle is: keep lines short enough that two files can be opened side by side.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-01-clean-code-and-pep8-003-518eeb294e.html"
 width="100%"
></iframe>

## Import Order

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-01-clean-code-and-pep8-004-f9480a7ef3.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-01-clean-code-and-pep8-005-cae8daeb42.html"
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
