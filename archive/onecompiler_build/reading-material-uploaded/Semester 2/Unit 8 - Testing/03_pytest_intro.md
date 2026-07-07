## Introduction

Sam's manual test file works but has a problem: when test 2 fails, tests 3 through 6 never run. He must fix test 2, re-run, find test 4 also fails, fix that, re-run again. He is getting the failures one at a time when he needs them all at once.

`pytest` solves this. It discovers all test functions in a project, runs them all regardless of which ones fail, and prints a clear report of every failure with the line, the expected value, and the actual value. Installing it is one command; using it is just naming your functions `test_`.

![A terminal showing pytest output: green dots for passing tests, red Fs for failing tests, and a final summary showing 5 passed, 2 failed with detailed diffs for each failure](images/03_pytest_intro.png)

## Installing pytest

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-03-pytest-intro-001-2ebaafdf5a.html"
 width="100%"
></iframe>

That is the only setup required. `pytest` is not part of the standard library, but it is the de facto standard Python testing tool.

## Writing Tests for pytest

`pytest` discovers test functions automatically: it looks for files named `test_*.py` or `*_test.py`, and within those files it finds functions named `test_*`. No imports, no registration, no boilerplate required.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-03-pytest-intro-002-47aaa9397d.html"
 width="100%"
></iframe>

## Running pytest

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-03-pytest-intro-003-7c1d2106d2.html"
 width="100%"
></iframe>

Sample output:

```
======= test session starts =======
collected 3 items

test_fines.py::test_fine_normal      PASSED
test_fines.py::test_fine_zero_days   PASSED
test_fines.py::test_fine_custom_rate PASSED

======= 3 passed in 0.12s =======
```

## pytest's Error Messages

When a test fails, `pytest` shows a rich diff. For `assert actual == expected`, it shows both values:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-03-pytest-intro-004-09b84368e9.html"
 width="100%"
></iframe>

This is far more useful than `AssertionError` with no context.

## Testing Exceptions with pytest.raises

`pytest.raises` is the clean way to test that a function raises a specific exception:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-03-pytest-intro-005-ccf61b83c8.html"
 width="100%"
></iframe>

If the exception is not raised, the test fails. If a different exception is raised, it propagates and the test also fails.

## Organizing Tests in a Project

A common layout puts tests in a `tests/` directory at the project root:

```
library_system/
    library/
        __init__.py
        fines.py
        catalog.py
    tests/
        __init__.py
        test_fines.py
        test_catalog.py
    pyproject.toml
```

Running `pytest` from the project root finds all `test_*.py` files automatically.

## pytest at a Glance

| Command | What it does |
|---|---|
| `pytest` | Discover and run all tests |
| `pytest -v` | Verbose output with test names |
| `pytest test_file.py::test_name` | Run one specific test |
| `pytest.raises(ExcType)` | Assert that an exception is raised |
| `pytest.raises(ExcType, match=pattern)` | Assert exception and check message |

## Your Turn

Move the `calculate_fine` function to its own file `library/fines.py`, then create `tests/test_fines.py`. Import `calculate_fine` and rewrite the manual tests as `pytest` tests, including one that uses `pytest.raises`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-03-pytest-intro-006-e05077f705.html"
 width="100%"
></iframe>

Run `pytest -v` and confirm all four tests pass.

## Conclusion

`pytest` discovers tests by naming convention (`test_*.py`, `test_*`), runs all of them in one pass, and reports every failure with a clear diff. `pytest.raises` replaces the manual try/except pattern for exception testing. The next lesson covers how to organize a growing test suite and write tests that are easy to read, maintain, and run in isolation.
