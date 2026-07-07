## Introduction

Before Sam learns about any testing framework, his team lead wants him to understand the single building block that all Python tests are built on: the `assert` statement. It is already in the language and requires no installation. Understanding it well makes everything in the testing framework more intuitive.

![The word assert followed by an expression and an optional message, shown as a gate: if the expression is True, execution passes through; if False, an AssertionError is raised with the message](images/02_assert_manual_testing.png)

## The assert Statement

`assert expression` does nothing if `expression` is truthy, and raises `AssertionError` if it is falsy. It is the programmatic version of "this must be true here."

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-02-assert-and-manual-testing-001-0f756624a8.html"
 width="100%"
></iframe>

Always include a message. Without one, the error says only `AssertionError` with no indication of what was wrong.

## Asserting with Context

The most useful assertions compare expected and actual values directly:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-02-assert-and-manual-testing-002-a4a543b572.html"
 width="100%"
></iframe>

## Asserting Exceptions

To test that a function raises a specific exception, you need to catch it and confirm the type. Python's `pytest` framework provides a cleaner way (covered in the next lesson), but the raw approach shows what is happening underneath:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-02-assert-and-manual-testing-003-c9ddf3d369.html"
 width="100%"
></iframe>

## Floating-Point Comparisons

Floating-point arithmetic introduces rounding errors. Never compare floats with `==` in tests:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-02-assert-and-manual-testing-004-6da40f57e7.html"
 width="100%"
></iframe>

`math.isclose` checks whether two floats are equal within a relative tolerance. Use it whenever testing float results.

## Running Tests Manually

A simple manual test file collects all assertions into functions. Running the file with Python executes them:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-02-assert-and-manual-testing-005-0f5269fb40.html"
 width="100%"
></iframe>

This works but has a limitation: if one test fails, the rest do not run. A testing framework like `pytest` runs all tests and reports all failures at once.

## assert in Production Code

`assert` in production code is risky: Python can be run with the `-O` (optimize) flag, which strips all `assert` statements. Use `raise` instead for runtime validation that must always run:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-02-assert-and-manual-testing-006-dabc1c1059.html"
 width="100%"
></iframe>

`assert` belongs in test code; `raise` belongs in production code.

## assert at a Glance

| Form | What it does |
|---|---|
| `assert expr` | Raises `AssertionError` if expr is falsy |
| `assert expr, msg` | Same, with a descriptive message |
| `math.isclose(a, b)` | Safe float comparison within tolerance |
| `assert raised` after try/except | Verify exception was raised |

## Your Turn

Write a file `test_manual.py` with at least five test functions for `calculate_fine`. Include: normal case, zero days, one day, large number of days, and a case with a custom daily rate. Run the file with `python test_manual.py` and confirm all tests pass.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-02-assert-and-manual-testing-007-1b1033ae20.html"
 width="100%"
></iframe>

## Conclusion

`assert` is the foundation of Python testing: it checks a condition and raises `AssertionError` with a message if it fails. Use `math.isclose` for floats. Reserve `raise` for production validation and `assert` for test code. The next lesson introduces `pytest`, which discovers and runs these functions automatically, collects all failures in one report, and provides much better error messages than raw assertions.
