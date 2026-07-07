## Introduction

Every one of Sam's catalog tests starts with the same three lines: create a `Catalog`, create a `Book`, add the book to the catalog. When the `Book` constructor signature changes -- which it does when the team adds a `publisher` field -- he has to update every test file. There are twenty-three tests. He spends forty minutes updating setup code instead of testing new behavior.

`pytest` fixtures are the solution. A fixture is a function that provides a pre-built, reusable piece of setup to any test that requests it. Change the fixture once, and every test that uses it is updated automatically.

![A diagram showing three test functions each previously containing identical setup code, transformed into three slim tests each receiving the same fixture via a parameter named catalog](images/05_fixtures.png)

## Defining and Using a Fixture

A fixture is a function decorated with `@pytest.fixture`. Any test function that declares a parameter with the same name as the fixture receives the fixture's return value automatically.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-05-fixtures-001-8a6a693b78.html"
 width="100%"
></iframe>

`pytest` sees that `test_catalog_length` has a parameter named `catalog_with_book`, finds the matching fixture, calls it, and passes its return value as the argument. This happens automatically.

## Fixture Composition

Fixtures can depend on other fixtures, as shown above with `catalog_with_book` depending on `sample_book`. `pytest` resolves the dependency graph and calls fixtures in the right order.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-05-fixtures-002-003860ad3a.html"
 width="100%"
></iframe>

## Fixture Scope

By default, a fixture runs once per test function. For expensive setups (like database connections), `scope` controls how often the fixture is created:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-05-fixtures-003-68132feaa7.html"
 width="100%"
></iframe>

| Scope | Created once per |
|---|---|
| `"function"` | Test function (default) |
| `"class"` | Test class |
| `"module"` | Test file |
| `"session"` | Entire test run |

## Fixtures with yield: Setup and Teardown

When a fixture uses `yield` instead of `return`, the code before `yield` runs before the test and the code after `yield` runs after the test (teardown). This is the clean way to manage resources in fixtures.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-05-fixtures-004-40e02ecf46.html"
 width="100%"
></iframe>

## conftest.py: Shared Fixtures

Fixtures in a `conftest.py` file are available to all test files in the same directory and its subdirectories, without any import:

```
tests/
    conftest.py       # fixtures here are shared across all tests/
    test_fines.py
    test_catalog.py
```

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-05-fixtures-005-588c8b9794.html"
 width="100%"
></iframe>

`test_fines.py` and `test_catalog.py` can both use `empty_catalog` and `sample_book` without importing them.

## Fixtures at a Glance

| Concept | What it means |
|---|---|
| `@pytest.fixture` | Marks a function as a fixture |
| Parameter name = fixture name | `pytest` injects it automatically |
| `yield` in fixture | Code after `yield` runs as teardown |
| `scope="module"` | Fixture created once per test file |
| `conftest.py` | Fixtures shared across the directory |

## Your Turn

Create a `tests/conftest.py` with three fixtures: `empty_catalog` (a fresh `Catalog`), `sample_book` (a `Book` with known values), and `loaded_catalog` (a `Catalog` with five pre-loaded books using a `yield` fixture that also prints "setup" and "teardown").

Then write three tests in `tests/test_catalog.py` that each use one of these fixtures. Run `pytest -v` and observe which test is passed each fixture.

## Conclusion

Fixtures centralize setup code so tests stay focused on behavior rather than boilerplate. `yield` fixtures add teardown. `conftest.py` shares fixtures across multiple test files. Fixture scope controls how often expensive setups run. The next lesson adds parameterization: running the same test against many inputs without duplicating the test function.
