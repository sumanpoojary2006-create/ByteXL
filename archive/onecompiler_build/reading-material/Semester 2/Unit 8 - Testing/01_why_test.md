## Introduction

Sam pushed a small change to the library system on a Friday afternoon: a one-line fix to the overdue-fine calculator. On Monday, the system sent incorrect fine notices to three hundred patrons. The bug was not in the one line he changed -- it was in a helper function that his change started calling in a new code path. There were no tests. The bug was invisible until real patrons reported it.

His team lead's response was not a reprimand but a question: "What would have caught this before it reached production?" The answer is tests. This unit explains what tests are, why they matter, and how to write them with Python's `pytest` framework.

![A timeline showing code written, then a bug introduced, with two branches: one where tests catch it before production (highlighted in green) and one where it reaches users (highlighted in red)](images/01_why_test.png)

## What Testing Is

A test is code that calls your code and checks that the result is what you expect. That is the entire idea. The sophistication is in which scenarios you test and how you organize and run those checks.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3doeV90ZXN0IGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiIjIFRoZSBmdW5jdGlvbiBTYW0gY2hhbmdlZDpcbmRlZiBjYWxjdWxhdGVfZmluZShkYXlzX292ZXJkdWUsIGRhaWx5X3JhdGU9MC41MCk6XG4gICAgcmV0dXJuIGRheXNfb3ZlcmR1ZSAqIGRhaWx5X3JhdGVcblxuIyBBIHRlc3Q6IGNhbGwgdGhlIGZ1bmN0aW9uIGFuZCBjaGVjayB0aGUgcmVzdWx0XG5yZXN1bHQgPSBjYWxjdWxhdGVfZmluZSgxMClcbmFzc2VydCByZXN1bHQgPT0gNS4wLCBmXCJFeHBlY3RlZCA1LjAsIGdvdCB7cmVzdWx0fVwiIn0"
 width="100%"
></iframe>

Running this after every change catches regressions: situations where a previously working feature stops working because something unrelated changed.

## Why Automated Tests Beat Manual Verification

Sam verified his change manually: he borrowed one book, returned it ten days late, and confirmed the fine was correct. He did not check: borrowed on the last day of the month, borrowed on February 29, borrowed by a patron with an existing outstanding balance, or the edge case where `days_overdue` is zero.

Automated tests check all these cases every time, in seconds, without anyone having to remember them:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3doeV90ZXN0IGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJkZWYgdGVzdF9maW5lX3plcm9fZGF5cygpOlxuICAgIGFzc2VydCBjYWxjdWxhdGVfZmluZSgwKSA9PSAwLjBcblxuZGVmIHRlc3RfZmluZV90ZW5fZGF5cygpOlxuICAgIGFzc2VydCBjYWxjdWxhdGVfZmluZSgxMCkgPT0gNS4wXG5cbmRlZiB0ZXN0X2ZpbmVfY3VzdG9tX3JhdGUoKTpcbiAgICBhc3NlcnQgY2FsY3VsYXRlX2ZpbmUoMTAsIGRhaWx5X3JhdGU9MS4wMCkgPT0gMTAuMFxuXG5kZWYgdGVzdF9maW5lX29uZV9kYXkoKTpcbiAgICBhc3NlcnQgY2FsY3VsYXRlX2ZpbmUoMSkgPT0gMC41MCJ9"
 width="100%"
></iframe>

After Sam adds these four tests, any future change that breaks the fine calculation is caught immediately, not by three hundred confused patrons.

## The Three Values of Testing

**Safety to change**: tests let you refactor and add features with confidence. If all tests pass after a change, the previously verified behavior still works.

**Documentation**: tests describe what the code is supposed to do. A new developer reading `test_fine_zero_days` learns that the function accepts zero and returns zero, without reading the implementation.

**Design pressure**: writing tests often reveals when code is hard to test, which usually means it is also hard to use. Functions with too many responsibilities, hidden side effects, or hard-coded dependencies are all harder to test. Testing pressure is a signal to improve the design.

## What to Test

The most valuable tests cover:

- **Normal cases**: the expected, common inputs
- **Edge cases**: the boundaries (zero, empty, maximum value, first and last day of a period)
- **Error cases**: what happens when invalid input is passed

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3doeV90ZXN0IGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiIjIE5vcm1hbFxuYXNzZXJ0IGNhbGN1bGF0ZV9maW5lKDcpID09IDMuNTBcblxuIyBFZGdlOiB6ZXJvIGRheXNcbmFzc2VydCBjYWxjdWxhdGVfZmluZSgwKSA9PSAwLjBcblxuIyBFZGdlOiBsYXJnZSBudW1iZXJcbmFzc2VydCBjYWxjdWxhdGVfZmluZSgzNjUpID09IDE4Mi41MFxuXG4jIEVycm9yIGNhc2U6IG5lZ2F0aXZlIGlucHV0IHNob3VsZCBwcm9iYWJseSBiZSB0cmVhdGVkIGFzIHplcm8gKG9yIHJhaXNlKVxuIyBrbm93aW5nIHdoaWNoIGlzIGNvcnJlY3QgaXMgcGFydCBvZiBzcGVjaWZ5aW5nIHRoZSBiZWhhdmlvciJ9"
 width="100%"
></iframe>

## What Not to Test

Not every line of code needs a test. Testing Python itself (that `1 + 1 == 2`) or testing the framework you are using wastes time without adding safety. Focus tests on *your* logic.

## Why Test at a Glance

| Value | What it means |
|---|---|
| Safety to change | Regressions are caught before reaching users |
| Documentation | Tests show what the code is supposed to do |
| Design feedback | Hard-to-test code is often hard to use |
| Edge case coverage | Checks scenarios humans forget |

## Your Turn

Look at Nadia's `overdue_report` function from Unit 7:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX3doeV90ZXN0IGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRlLCB0aW1lZGVsdGFcblxuZGVmIG92ZXJkdWVfcmVwb3J0KHJlY29yZHMsIHRvZGF5PU5vbmUpOlxuICAgIHRvZGF5ID0gdG9kYXkgb3IgZGF0ZS50b2RheSgpXG4gICAgb3ZlcmR1ZSA9IFtdXG4gICAgZm9yIHJlY29yZCBpbiByZWNvcmRzOlxuICAgICAgICBib3Jyb3cgPSBkYXRlLmZyb21pc29mb3JtYXQocmVjb3JkW1wiYm9ycm93X2RhdGVcIl0pXG4gICAgICAgIGR1ZSA9IGJvcnJvdyArIHRpbWVkZWx0YShkYXlzPXJlY29yZFtcImxvYW5fZGF5c1wiXSlcbiAgICAgICAgaWYgdG9kYXkgPiBkdWU6XG4gICAgICAgICAgICBvdmVyZHVlLmFwcGVuZCh7KipyZWNvcmQsIFwiZGF5c19vdmVyZHVlXCI6ICh0b2RheSAtIGR1ZSkuZGF5c30pXG4gICAgcmV0dXJuIG92ZXJkdWUifQ"
 width="100%"
></iframe>

Without running the code, write down four test cases you would write for this function: one normal case, one edge case where no books are overdue, one edge case where a book is exactly on its due date, and one edge case where the records list is empty.

## Conclusion

Tests are code that calls your code and checks the result. They catch regressions before they reach users, document intended behavior, and create design pressure toward simpler, more focused functions. The next lesson introduces `assert` as the foundation of all testing, and shows how to write and run tests with `pytest`.
