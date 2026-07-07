## Introduction

Sam's manual test file works but has a problem: when test 2 fails, tests 3 through 6 never run. He must fix test 2, re-run, find test 4 also fails, fix that, re-run again. He is getting the failures one at a time when he needs them all at once.

`pytest` solves this. It discovers all test functions in a project, runs them all regardless of which ones fail, and prints a clear report of every failure with the line, the expected value, and the actual value. Installing it is one command; using it is just naming your functions `test_`.

![A terminal showing pytest output: green dots for passing tests, red Fs for failing tests, and a final summary showing 5 passed, 2 failed with detailed diffs for each failure](images/03_pytest_intro.png)

## Installing pytest

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3B5dGVzdF9pbnRybyBjb2RlIDEiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDAxLnNoIiwiY29kZSI6InBpcCBpbnN0YWxsIHB5dGVzdCJ9"
 width="100%"
></iframe>

That is the only setup required. `pytest` is not part of the standard library, but it is the de facto standard Python testing tool.

## Writing Tests for pytest

`pytest` discovers test functions automatically: it looks for files named `test_*.py` or `*_test.py`, and within those files it finds functions named `test_*`. No imports, no registration, no boilerplate required.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3B5dGVzdF9pbnRybyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiIyB0ZXN0X2ZpbmVzLnB5XG5pbXBvcnQgbWF0aFxuXG5kZWYgY2FsY3VsYXRlX2ZpbmUoZGF5c19vdmVyZHVlLCBkYWlseV9yYXRlPTAuNTApOlxuICAgIGlmIGRheXNfb3ZlcmR1ZSA8IDA6XG4gICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoXCJkYXlzX292ZXJkdWUgY2Fubm90IGJlIG5lZ2F0aXZlXCIpXG4gICAgcmV0dXJuIGRheXNfb3ZlcmR1ZSAqIGRhaWx5X3JhdGVcblxuZGVmIHRlc3RfZmluZV9ub3JtYWwoKTpcbiAgICBhc3NlcnQgbWF0aC5pc2Nsb3NlKGNhbGN1bGF0ZV9maW5lKDEwKSwgNS4wKVxuXG5kZWYgdGVzdF9maW5lX3plcm9fZGF5cygpOlxuICAgIGFzc2VydCBjYWxjdWxhdGVfZmluZSgwKSA9PSAwLjBcblxuZGVmIHRlc3RfZmluZV9jdXN0b21fcmF0ZSgpOlxuICAgIGFzc2VydCBtYXRoLmlzY2xvc2UoY2FsY3VsYXRlX2ZpbmUoMTAsIGRhaWx5X3JhdGU9MS4wMCksIDEwLjApXG5cbmRlZiB0ZXN0X2ZpbmVfbmVnYXRpdmVfcmFpc2VzKCk6XG4gICAgIyBUaGlzIGlzIHRoZSBweXRlc3Qgd2F5IHRvIHRlc3QgZXhjZXB0aW9ucyAobmV4dCBsZXNzb24pXG4gICAgcGFzcyJ9"
 width="100%"
></iframe>

## Running pytest

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3B5dGVzdF9pbnRybyBjb2RlIDMiLCJsYW5ndWFnZSI6ImJhc2giLCJmaWxlbmFtZSI6Im1haW5fMDAzLnNoIiwiY29kZSI6IiMgUnVuIGFsbCBkaXNjb3ZlcmVkIHRlc3RzOlxucHl0ZXN0XG5cbiMgUnVuIGEgc3BlY2lmaWMgZmlsZTpcbnB5dGVzdCB0ZXN0X2ZpbmVzLnB5XG5cbiMgUnVuIGEgc3BlY2lmaWMgdGVzdCBmdW5jdGlvbjpcbnB5dGVzdCB0ZXN0X2ZpbmVzLnB5Ojp0ZXN0X2ZpbmVfbm9ybWFsXG5cbiMgVmVyYm9zZSBvdXRwdXQgKHNob3dzIGVhY2ggdGVzdCBuYW1lKTpcbnB5dGVzdCAtdiJ9"
 width="100%"
></iframe>

Sample output:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3B5dGVzdF9pbnRybyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiPT09PT09PSB0ZXN0IHNlc3Npb24gc3RhcnRzID09PT09PT1cbmNvbGxlY3RlZCAzIGl0ZW1zXG5cbnRlc3RfZmluZXMucHk6OnRlc3RfZmluZV9ub3JtYWwgICAgICBQQVNTRURcbnRlc3RfZmluZXMucHk6OnRlc3RfZmluZV96ZXJvX2RheXMgICBQQVNTRURcbnRlc3RfZmluZXMucHk6OnRlc3RfZmluZV9jdXN0b21fcmF0ZSBQQVNTRURcblxuPT09PT09PSAzIHBhc3NlZCBpbiAwLjEycyA9PT09PT09In0"
 width="100%"
></iframe>

## pytest's Error Messages

When a test fails, `pytest` shows a rich diff. For `assert actual == expected`, it shows both values:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3B5dGVzdF9pbnRybyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiZGVmIHRlc3RfZmluZV9ub3JtYWwoKTpcbiAgICBhc3NlcnQgY2FsY3VsYXRlX2ZpbmUoMTApID09IDYuMCAgICMgd3JvbmcgZXhwZWN0ZWQgdmFsdWVcblxuIyBweXRlc3Qgb3V0cHV0OlxuIyBGQUlMRUQgdGVzdF9maW5lcy5weTo6dGVzdF9maW5lX25vcm1hbFxuIyBhc3NlcnQgNS4wID09IDYuMFxuIyAgKyAgd2hlcmUgNS4wID0gY2FsY3VsYXRlX2ZpbmUoMTApIn0"
 width="100%"
></iframe>

This is far more useful than `AssertionError` with no context.

## Testing Exceptions with pytest.raises

`pytest.raises` is the clean way to test that a function raises a specific exception:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3B5dGVzdF9pbnRybyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoiaW1wb3J0IHB5dGVzdFxuXG5kZWYgdGVzdF9maW5lX25lZ2F0aXZlX3JhaXNlcygpOlxuICAgIHdpdGggcHl0ZXN0LnJhaXNlcyhWYWx1ZUVycm9yKTpcbiAgICAgICAgY2FsY3VsYXRlX2ZpbmUoLTEpXG5cbiMgQ2hlY2sgdGhlIGV4Y2VwdGlvbiBtZXNzYWdlIHRvbzpcbmRlZiB0ZXN0X2ZpbmVfbmVnYXRpdmVfbWVzc2FnZSgpOlxuICAgIHdpdGggcHl0ZXN0LnJhaXNlcyhWYWx1ZUVycm9yLCBtYXRjaD1cImNhbm5vdCBiZSBuZWdhdGl2ZVwiKTpcbiAgICAgICAgY2FsY3VsYXRlX2ZpbmUoLTEpIn0"
 width="100%"
></iframe>

If the exception is not raised, the test fails. If a different exception is raised, it propagates and the test also fails.

## Organizing Tests in a Project

A common layout puts tests in a `tests/` directory at the project root:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3B5dGVzdF9pbnRybyBjb2RlIDciLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDcucHkiLCJjb2RlIjoibGlicmFyeV9zeXN0ZW0vXG4gICAgbGlicmFyeS9cbiAgICAgICAgX19pbml0X18ucHlcbiAgICAgICAgZmluZXMucHlcbiAgICAgICAgY2F0YWxvZy5weVxuICAgIHRlc3RzL1xuICAgICAgICBfX2luaXRfXy5weVxuICAgICAgICB0ZXN0X2ZpbmVzLnB5XG4gICAgICAgIHRlc3RfY2F0YWxvZy5weVxuICAgIHB5cHJvamVjdC50b21sIn0"
 width="100%"
></iframe>

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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3B5dGVzdF9pbnRybyBjb2RlIDgiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDgucHkiLCJjb2RlIjoiIyB0ZXN0cy90ZXN0X2ZpbmVzLnB5XG5pbXBvcnQgbWF0aFxuaW1wb3J0IHB5dGVzdFxuZnJvbSBsaWJyYXJ5LmZpbmVzIGltcG9ydCBjYWxjdWxhdGVfZmluZVxuXG5kZWYgdGVzdF9ub3JtYWwoKTpcbiAgICBhc3NlcnQgbWF0aC5pc2Nsb3NlKGNhbGN1bGF0ZV9maW5lKDEwKSwgNS4wKVxuXG5kZWYgdGVzdF96ZXJvKCk6XG4gICAgYXNzZXJ0IGNhbGN1bGF0ZV9maW5lKDApID09IDAuMFxuXG5kZWYgdGVzdF9jdXN0b21fcmF0ZSgpOlxuICAgIGFzc2VydCBtYXRoLmlzY2xvc2UoY2FsY3VsYXRlX2ZpbmUoMTAsIGRhaWx5X3JhdGU9MS4wMCksIDEwLjApXG5cbmRlZiB0ZXN0X25lZ2F0aXZlX3JhaXNlcygpOlxuICAgIHdpdGggcHl0ZXN0LnJhaXNlcyhWYWx1ZUVycm9yLCBtYXRjaD1cImNhbm5vdCBiZSBuZWdhdGl2ZVwiKTpcbiAgICAgICAgY2FsY3VsYXRlX2ZpbmUoLTEpIn0"
 width="100%"
></iframe>

Run `pytest -v` and confirm all four tests pass.

## Conclusion

`pytest` discovers tests by naming convention (`test_*.py`, `test_*`), runs all of them in one pass, and reports every failure with a clear diff. `pytest.raises` replaces the manual try/except pattern for exception testing. The next lesson covers how to organize a growing test suite and write tests that are easy to read, maintain, and run in isolation.
