## Introduction

Sam now has eleven test functions spread across two files. Some of them share a common setup: they all create a sample catalog and a few borrow records before running. He is copying the setup code into each test function, which means when the data model changes, he has to update every copy. His team lead shows him how to organize tests so that setup lives in one place and each test focuses only on what it is actually testing.

![A test file diagram showing three test functions that each previously duplicated their setup, transformed into three slim test functions sharing one fixture at the top of the file](images/04_writing_organizing_tests.png)

## The Four-Phase Test Pattern

Well-written tests follow four phases: Arrange (set up the data), Act (call the code), Assert (check the result), Cleanup (optional teardown). Keeping these distinct makes tests readable and maintainable.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3dyaXRpbmdfYW5kX29yZ2FuaXppbmdfdGVzdHMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6IiMgdGVzdF9jYXRhbG9nLnB5XG5mcm9tIGxpYnJhcnkuY2F0YWxvZyBpbXBvcnQgQ2F0YWxvZywgQm9va1xuXG5kZWYgdGVzdF9hZGRfYm9va19pbmNyZWFzZXNfY291bnQoKTpcbiAgICAjIEFycmFuZ2VcbiAgICBjYXRhbG9nID0gQ2F0YWxvZygpXG4gICAgYm9vayA9IEJvb2soaXNibj1cIjk3OC0wMDFcIiwgdGl0bGU9XCJEdW5lXCIsIGdlbnJlPVwiU2NpLUZpXCIsIGNvcGllcz0zKVxuXG4gICAgIyBBY3RcbiAgICBjYXRhbG9nLmFkZChib29rKVxuXG4gICAgIyBBc3NlcnRcbiAgICBhc3NlcnQgbGVuKGNhdGFsb2cpID09IDFcblxuZGVmIHRlc3RfZmluZF9ib29rX2J5X2lzYm4oKTpcbiAgICAjIEFycmFuZ2VcbiAgICBjYXRhbG9nID0gQ2F0YWxvZygpXG4gICAgYm9vayA9IEJvb2soaXNibj1cIjk3OC0wMDFcIiwgdGl0bGU9XCJEdW5lXCIsIGdlbnJlPVwiU2NpLUZpXCIsIGNvcGllcz0zKVxuICAgIGNhdGFsb2cuYWRkKGJvb2spXG5cbiAgICAjIEFjdFxuICAgIHJlc3VsdCA9IGNhdGFsb2cuZmluZChcIjk3OC0wMDFcIilcblxuICAgICMgQXNzZXJ0XG4gICAgYXNzZXJ0IHJlc3VsdC50aXRsZSA9PSBcIkR1bmVcIiJ9"
 width="100%"
></iframe>

Notice that both tests independently set up their own `catalog` and `book`. This is intentional: tests should not depend on each other's state.

## One Assertion per Test (Roughly)

Tests that check many things at once are harder to diagnose. When a multi-assertion test fails, you know *something* went wrong, but not what. Prefer focused tests:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3dyaXRpbmdfYW5kX29yZ2FuaXppbmdfdGVzdHMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6IiMgSGFyZCB0byBkaWFnbm9zZSB3aGVuIGl0IGZhaWxzOlxuZGVmIHRlc3RfYm9va19wcm9wZXJ0aWVzKCk6XG4gICAgYm9vayA9IEJvb2soaXNibj1cIjk3OC0wMDFcIiwgdGl0bGU9XCJEdW5lXCIsIGdlbnJlPVwiU2NpLUZpXCIsIGNvcGllcz0zKVxuICAgIGFzc2VydCBib29rLmlzYm4gPT0gXCI5NzgtMDAxXCJcbiAgICBhc3NlcnQgYm9vay50aXRsZSA9PSBcIkR1bmVcIlxuICAgIGFzc2VydCBib29rLmNvcGllcyA9PSAzXG4gICAgYXNzZXJ0IGJvb2suZ2VucmUgPT0gXCJTY2ktRmlcIlxuXG4jIEJldHRlcjogb25lIGZvY3VzZWQgY2hlY2sgcGVyIHRlc3QgKG9yIGdyb3VwIHJlbGF0ZWQgYXNzZXJ0aW9ucylcbmRlZiB0ZXN0X2Jvb2tfc3RvcmVzX2lzYm4oKTpcbiAgICBib29rID0gQm9vayhpc2JuPVwiOTc4LTAwMVwiLCB0aXRsZT1cIkR1bmVcIiwgZ2VucmU9XCJTY2ktRmlcIiwgY29waWVzPTMpXG4gICAgYXNzZXJ0IGJvb2suaXNibiA9PSBcIjk3OC0wMDFcIlxuXG5kZWYgdGVzdF9ib29rX3N0b3Jlc19jb3BpZXMoKTpcbiAgICBib29rID0gQm9vayhpc2JuPVwiOTc4LTAwMVwiLCB0aXRsZT1cIkR1bmVcIiwgZ2VucmU9XCJTY2ktRmlcIiwgY29waWVzPTMpXG4gICAgYXNzZXJ0IGJvb2suY29waWVzID09IDMifQ"
 width="100%"
></iframe>

That said, if two values are invariably tested together (like a pair of coordinates), a single test checking both is fine. The goal is diagnostic clarity, not strict rule-following.

## Test Names as Documentation

Test function names are the first thing you read when a test fails. Name them to describe the scenario and expected behavior:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3dyaXRpbmdfYW5kX29yZ2FuaXppbmdfdGVzdHMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6IiMgSGFyZCB0byB1bmRlcnN0YW5kIHdoYXQgZmFpbGVkOlxuZGVmIHRlc3RfMSgpOlxuICAgIC4uLlxuXG5kZWYgdGVzdF9jYXRhbG9nKCk6XG4gICAgLi4uXG5cbiMgQ2xlYXIgYW5kIHNlYXJjaGFibGU6XG5kZWYgdGVzdF9hZGRfYm9va19pbmNyZWFzZXNfY2F0YWxvZ19sZW5ndGgoKTpcbiAgICAuLi5cblxuZGVmIHRlc3RfZmluZF9yZXR1cm5zX25vbmVfZm9yX3Vua25vd25faXNibigpOlxuICAgIC4uLlxuXG5kZWYgdGVzdF9maW5kX3JhaXNlc19mb3JfaW52YWxpZF9pc2JuX2Zvcm1hdCgpOlxuICAgIC4uLiJ9"
 width="100%"
></iframe>

The convention `test_<thing>_<scenario>_<expected>` works well for describing edge cases.

## Organizing Tests by Feature

Group tests into files that correspond to the module they test. Use subdirectories for large codebases:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3dyaXRpbmdfYW5kX29yZ2FuaXppbmdfdGVzdHMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6InRlc3RzL1xuICAgIHRlc3RfZmluZXMucHkgICAgICAgICAgIyB0ZXN0cyBmb3IgbGlicmFyeS9maW5lcy5weVxuICAgIHRlc3RfY2F0YWxvZy5weSAgICAgICAgIyB0ZXN0cyBmb3IgbGlicmFyeS9jYXRhbG9nLnB5XG4gICAgdGVzdF9wYXRyb24ucHkgICAgICAgICAjIHRlc3RzIGZvciBsaWJyYXJ5L3BhdHJvbi5weVxuICAgIGludGVncmF0aW9uL1xuICAgICAgICB0ZXN0X2JvcnJvd19mbG93LnB5ICAjIHRlc3RzIHRoYXQgc3BhbiBtdWx0aXBsZSBtb2R1bGVzIn0"
 width="100%"
></iframe>

Within a file, test functions in the same "group" can be collected into a class. This is not required, but it provides a namespace and allows shared fixtures at the class level:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3dyaXRpbmdfYW5kX29yZ2FuaXppbmdfdGVzdHMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImNsYXNzIFRlc3RDYXRhbG9nOlxuICAgIGRlZiB0ZXN0X2VtcHR5X2F0X3N0YXJ0KHNlbGYpOlxuICAgICAgICBjYXRhbG9nID0gQ2F0YWxvZygpXG4gICAgICAgIGFzc2VydCBsZW4oY2F0YWxvZykgPT0gMFxuXG4gICAgZGVmIHRlc3RfYWRkX2luY3JlYXNlc19jb3VudChzZWxmKTpcbiAgICAgICAgY2F0YWxvZyA9IENhdGFsb2coKVxuICAgICAgICBjYXRhbG9nLmFkZChCb29rKFwiOTc4LTAwMVwiLCBcIkR1bmVcIiwgXCJTY2ktRmlcIiwgMykpXG4gICAgICAgIGFzc2VydCBsZW4oY2F0YWxvZykgPT0gMSJ9"
 width="100%"
></iframe>

## Avoiding Inter-Test Dependencies

Tests must be independent. A test that only works if a previous test ran first is fragile and hard to debug.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3dyaXRpbmdfYW5kX29yZ2FuaXppbmdfdGVzdHMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6IiMgV1JPTkc6IHRlc3RfZmluZCBkZXBlbmRzIG9uIHRlc3RfYWRkIGhhdmluZyBydW4gZmlyc3RcbmNhdGFsb2cgPSBDYXRhbG9nKCkgICAjIHNoYXJlZCBzdGF0ZSBhdCBtb2R1bGUgbGV2ZWxcblxuZGVmIHRlc3RfYWRkKCk6XG4gICAgY2F0YWxvZy5hZGQoQm9vayhcIjk3OC0wMDFcIiwgXCJEdW5lXCIsIFwiU2NpLUZpXCIsIDMpKVxuXG5kZWYgdGVzdF9maW5kKCk6XG4gICAgcmVzdWx0ID0gY2F0YWxvZy5maW5kKFwiOTc4LTAwMVwiKSAgIyBvbmx5IHdvcmtzIGlmIHRlc3RfYWRkIHJhbiBmaXJzdFxuICAgIGFzc2VydCByZXN1bHQgaXMgbm90IE5vbmVcblxuIyBDT1JSRUNUOiBlYWNoIHRlc3QgY3JlYXRlcyBpdHMgb3duIGZyZXNoIGNhdGFsb2dcbmRlZiB0ZXN0X2FkZCgpOlxuICAgIGMgPSBDYXRhbG9nKClcbiAgICBjLmFkZChCb29rKFwiOTc4LTAwMVwiLCBcIkR1bmVcIiwgXCJTY2ktRmlcIiwgMykpXG4gICAgYXNzZXJ0IGxlbihjKSA9PSAxXG5cbmRlZiB0ZXN0X2ZpbmQoKTpcbiAgICBjID0gQ2F0YWxvZygpXG4gICAgYy5hZGQoQm9vayhcIjk3OC0wMDFcIiwgXCJEdW5lXCIsIFwiU2NpLUZpXCIsIDMpKVxuICAgIHJlc3VsdCA9IGMuZmluZChcIjk3OC0wMDFcIilcbiAgICBhc3NlcnQgcmVzdWx0IGlzIG5vdCBOb25lIn0"
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
