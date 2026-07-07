## Introduction

Sam now has eleven test functions spread across two files. Some of them share a common setup: they all create a sample catalog and a few borrow records before running. He is copying the setup code into each test function, which means when the data model changes, he has to update every copy. His team lead shows him how to organize tests so that setup lives in one place and each test focuses only on what it is actually testing.

![A test file diagram showing three test functions that each previously duplicated their setup, transformed into three slim test functions sharing one fixture at the top of the file](images/04_writing_organizing_tests.png)

## The Four-Phase Test Pattern

Well-written tests follow four phases: Arrange (set up the data), Act (call the code), Assert (check the result), Cleanup (optional teardown). Keeping these distinct makes tests readable and maintainable.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-04-writing-and-organizing-tests-001-408343d6ff.html"
 width="100%"
></iframe>

Notice that both tests independently set up their own `catalog` and `book`. This is intentional: tests should not depend on each other's state.

## One Assertion per Test (Roughly)

Tests that check many things at once are harder to diagnose. When a multi-assertion test fails, you know *something* went wrong, but not what. Prefer focused tests:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-04-writing-and-organizing-tests-002-def4463fcd.html"
 width="100%"
></iframe>

That said, if two values are invariably tested together (like a pair of coordinates), a single test checking both is fine. The goal is diagnostic clarity, not strict rule-following.

## Test Names as Documentation

Test function names are the first thing you read when a test fails. Name them to describe the scenario and expected behavior:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-04-writing-and-organizing-tests-003-d005679117.html"
 width="100%"
></iframe>

The convention `test_<thing>_<scenario>_<expected>` works well for describing edge cases.

## Organizing Tests by Feature

Group tests into files that correspond to the module they test. Use subdirectories for large codebases:

```
tests/
    test_fines.py          # tests for library/fines.py
    test_catalog.py        # tests for library/catalog.py
    test_patron.py         # tests for library/patron.py
    integration/
        test_borrow_flow.py  # tests that span multiple modules
```

Within a file, test functions in the same "group" can be collected into a class. This is not required, but it provides a namespace and allows shared fixtures at the class level:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-04-writing-and-organizing-tests-004-973ba538df.html"
 width="100%"
></iframe>

## Avoiding Inter-Test Dependencies

Tests must be independent. A test that only works if a previous test ran first is fragile and hard to debug.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-04-writing-and-organizing-tests-005-8238568a70.html"
 width="100%"
></iframe>

## Writing and Organizing Tests at a Glance

| Principle | What it means |
|---|---|
| Four-phase pattern | Arrange, Act, Assert, (Cleanup) |
| One focus per test | Each test checks one thing |
| Descriptive names | `test_<thing>_<scenario>_<expected>` |
| No shared mutable state | Each test creates its own data |
| Files mirror modules | `test_catalog.py` tests `catalog.py` |

## Your Turn

Write three tests for a `Catalog.remove(isbn)` method:

1. `test_remove_decreases_count` -- adding then removing a book reduces the count by one
2. `test_remove_book_not_in_find` -- after removing, finding that ISBN returns `None`
3. `test_remove_nonexistent_raises` -- removing an ISBN that was never added raises `KeyError`

Write each with the four-phase pattern, using a fresh `Catalog` instance in each test.

## Conclusion

Good test organization means: one focus per test, descriptive names, no shared mutable state between tests, and files that mirror the structure of the code they test. The four-phase pattern (Arrange/Act/Assert/Cleanup) makes the structure of each test immediately readable. The next lesson introduces `pytest` fixtures, which eliminate the duplicated Arrange code by providing shared setup in one place.
