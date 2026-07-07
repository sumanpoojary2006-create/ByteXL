## Introduction

Every one of Sam's catalog tests starts with the same three lines: create a `Catalog`, create a `Book`, add the book to the catalog. When the `Book` constructor signature changes -- which it does when the team adds a `publisher` field -- he has to update every test file. There are twenty-three tests. He spends forty minutes updating setup code instead of testing new behavior.

`pytest` fixtures are the solution. A fixture is a function that provides a pre-built, reusable piece of setup to any test that requests it. Change the fixture once, and every test that uses it is updated automatically.

![A diagram showing three test functions each previously containing identical setup code, transformed into three slim tests each receiving the same fixture via a parameter named catalog](images/05_fixtures.png)

## Defining and Using a Fixture

A fixture is a function decorated with `@pytest.fixture`. Any test function that declares a parameter with the same name as the fixture receives the fixture's return value automatically.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2ZpeHR1cmVzIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiIjIHRlc3RzL3Rlc3RfY2F0YWxvZy5weVxuaW1wb3J0IHB5dGVzdFxuZnJvbSBsaWJyYXJ5LmNhdGFsb2cgaW1wb3J0IENhdGFsb2csIEJvb2tcblxuQHB5dGVzdC5maXh0dXJlXG5kZWYgc2FtcGxlX2Jvb2soKTpcbiAgICByZXR1cm4gQm9vayhpc2JuPVwiOTc4LTAwMVwiLCB0aXRsZT1cIkR1bmVcIiwgZ2VucmU9XCJTY2ktRmlcIiwgY29waWVzPTMpXG5cbkBweXRlc3QuZml4dHVyZVxuZGVmIGNhdGFsb2dfd2l0aF9ib29rKHNhbXBsZV9ib29rKTpcbiAgICBjID0gQ2F0YWxvZygpXG4gICAgYy5hZGQoc2FtcGxlX2Jvb2spXG4gICAgcmV0dXJuIGNcblxuZGVmIHRlc3RfY2F0YWxvZ19sZW5ndGgoY2F0YWxvZ193aXRoX2Jvb2spOlxuICAgIGFzc2VydCBsZW4oY2F0YWxvZ193aXRoX2Jvb2spID09IDFcblxuZGVmIHRlc3RfZmluZF9ib29rKGNhdGFsb2dfd2l0aF9ib29rKTpcbiAgICByZXN1bHQgPSBjYXRhbG9nX3dpdGhfYm9vay5maW5kKFwiOTc4LTAwMVwiKVxuICAgIGFzc2VydCByZXN1bHQgaXMgbm90IE5vbmVcbiAgICBhc3NlcnQgcmVzdWx0LnRpdGxlID09IFwiRHVuZVwiXG5cbmRlZiB0ZXN0X2VtcHR5X2NhdGFsb2coKTpcbiAgICBjID0gQ2F0YWxvZygpICAgIyBubyBmaXh0dXJlIG5lZWRlZCBoZXJlXG4gICAgYXNzZXJ0IGxlbihjKSA9PSAwIn0"
 width="100%"
></iframe>

`pytest` sees that `test_catalog_length` has a parameter named `catalog_with_book`, finds the matching fixture, calls it, and passes its return value as the argument. This happens automatically.

## Fixture Composition

Fixtures can depend on other fixtures, as shown above with `catalog_with_book` depending on `sample_book`. `pytest` resolves the dependency graph and calls fixtures in the right order.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2ZpeHR1cmVzIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJAcHl0ZXN0LmZpeHR1cmVcbmRlZiBwYXRyb24oKTpcbiAgICByZXR1cm4ge1wiaWRcIjogXCJQMDAxXCIsIFwibmFtZVwiOiBcIkFsaWNlXCIsIFwiYWN0aXZlXCI6IFRydWV9XG5cbkBweXRlc3QuZml4dHVyZVxuZGVmIGJvcnJvd19yZWNvcmQoc2FtcGxlX2Jvb2ssIHBhdHJvbik6XG4gICAgcmV0dXJuIHtcbiAgICAgICAgXCJpc2JuXCI6IHNhbXBsZV9ib29rLmlzYm4sXG4gICAgICAgIFwicGF0cm9uX2lkXCI6IHBhdHJvbltcImlkXCJdLFxuICAgICAgICBcImJvcnJvd19kYXRlXCI6IFwiMjAyNi0wNi0wMVwiLFxuICAgICAgICBcImxvYW5fZGF5c1wiOiAyMSxcbiAgICB9XG5cbmRlZiB0ZXN0X292ZXJkdWVfcmVwb3J0KGJvcnJvd19yZWNvcmQpOlxuICAgIGZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGVcbiAgICBmcm9tIGxpYnJhcnkucmVwb3J0cyBpbXBvcnQgb3ZlcmR1ZV9yZXBvcnRcbiAgICByZXN1bHQgPSBvdmVyZHVlX3JlcG9ydChbYm9ycm93X3JlY29yZF0sIHRvZGF5PWRhdGUoMjAyNiwgNywgMTUpKVxuICAgIGFzc2VydCBsZW4ocmVzdWx0KSA9PSAxXG4gICAgYXNzZXJ0IHJlc3VsdFswXVtcImRheXNfb3ZlcmR1ZVwiXSA9PSAyMyJ9"
 width="100%"
></iframe>

## Fixture Scope

By default, a fixture runs once per test function. For expensive setups (like database connections), `scope` controls how often the fixture is created:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2ZpeHR1cmVzIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJAcHl0ZXN0LmZpeHR1cmUoc2NvcGU9XCJtb2R1bGVcIikgICAjIGNyZWF0ZWQgb25jZSBwZXIgdGVzdCBmaWxlXG5kZWYgZGJfY29ubmVjdGlvbigpOlxuICAgIGNvbm4gPSBjb25uZWN0X3RvX3Rlc3RfZGIoKVxuICAgIHlpZWxkIGNvbm5cbiAgICBjb25uLmNsb3NlKClcblxuQHB5dGVzdC5maXh0dXJlKHNjb3BlPVwic2Vzc2lvblwiKSAgIyBjcmVhdGVkIG9uY2UgZm9yIHRoZSBlbnRpcmUgdGVzdCBydW5cbmRlZiBhcHBfY29uZmlnKCk6XG4gICAgcmV0dXJuIGxvYWRfY29uZmlnKFwidGVzdF9jb25maWcuanNvblwiKSJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2ZpeHR1cmVzIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJpbXBvcnQgc3FsaXRlM1xuaW1wb3J0IHB5dGVzdFxuXG5AcHl0ZXN0LmZpeHR1cmVcbmRlZiBpbl9tZW1vcnlfZGIoKTpcbiAgICBjb25uID0gc3FsaXRlMy5jb25uZWN0KFwiOm1lbW9yeTpcIilcbiAgICBjb25uLmV4ZWN1dGUoXCJDUkVBVEUgVEFCTEUgYm9va3MgKGlzYm4gVEVYVCwgdGl0bGUgVEVYVClcIilcbiAgICB5aWVsZCBjb25uICAgIyB0ZXN0IHJlY2VpdmVzIHRoZSBjb25uZWN0aW9uIGhlcmVcbiAgICBjb25uLmNsb3NlKCkgIyBjbGVhbnVwOiBhbHdheXMgcnVucyBhZnRlciB0aGUgdGVzdFxuXG5kZWYgdGVzdF9pbnNlcnRfYm9vayhpbl9tZW1vcnlfZGIpOlxuICAgIGluX21lbW9yeV9kYi5leGVjdXRlKFwiSU5TRVJUIElOVE8gYm9va3MgVkFMVUVTICgnOTc4LTAwMScsICdEdW5lJylcIilcbiAgICByZXN1bHQgPSBpbl9tZW1vcnlfZGIuZXhlY3V0ZShcIlNFTEVDVCBDT1VOVCgqKSBGUk9NIGJvb2tzXCIpLmZldGNob25lKClcbiAgICBhc3NlcnQgcmVzdWx0WzBdID09IDEifQ"
 width="100%"
></iframe>

## conftest.py: Shared Fixtures

Fixtures in a `conftest.py` file are available to all test files in the same directory and its subdirectories, without any import:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2ZpeHR1cmVzIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJ0ZXN0cy9cbiAgICBjb25mdGVzdC5weSAgICAgICAjIGZpeHR1cmVzIGhlcmUgYXJlIHNoYXJlZCBhY3Jvc3MgYWxsIHRlc3RzL1xuICAgIHRlc3RfZmluZXMucHlcbiAgICB0ZXN0X2NhdGFsb2cucHkifQ"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2ZpeHR1cmVzIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiIjIHRlc3RzL2NvbmZ0ZXN0LnB5XG5pbXBvcnQgcHl0ZXN0XG5mcm9tIGxpYnJhcnkuY2F0YWxvZyBpbXBvcnQgQ2F0YWxvZywgQm9va1xuXG5AcHl0ZXN0LmZpeHR1cmVcbmRlZiBlbXB0eV9jYXRhbG9nKCk6XG4gICAgcmV0dXJuIENhdGFsb2coKVxuXG5AcHl0ZXN0LmZpeHR1cmVcbmRlZiBzYW1wbGVfYm9vaygpOlxuICAgIHJldHVybiBCb29rKGlzYm49XCI5NzgtMDAxXCIsIHRpdGxlPVwiRHVuZVwiLCBnZW5yZT1cIlNjaS1GaVwiLCBjb3BpZXM9MykifQ"
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
