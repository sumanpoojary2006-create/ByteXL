## Introduction

Sam's team lead asks a question he cannot answer: "What percentage of the code is covered by tests?" Sam knows his tests pass, but he does not know if there are entire code paths his tests never reach. The fine-calculation bug that caused the incident was in a branch of code that no test exercised, even though the main path was tested.

Coverage analysis answers the question by running the test suite and tracking which lines of code were executed. Any line not executed by any test is a gap that could hide a bug.

![A file shown with lines color-coded: green lines were executed during tests, red lines were never reached, creating a visual map of what the test suite does and does not cover](images/08_coverage.png)

## Installing pytest-cov

Coverage for `pytest` is provided by the `pytest-cov` plugin, which wraps the `coverage.py` library:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvdmVyYWdlIGNvZGUgMSIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDEuc2giLCJjb2RlIjoicGlwIGluc3RhbGwgcHl0ZXN0LWNvdiJ9"
 width="100%"
></iframe>

## Running Coverage

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvdmVyYWdlIGNvZGUgMiIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDIuc2giLCJjb2RlIjoiIyBSdW4gdGVzdHMgYW5kIG1lYXN1cmUgY292ZXJhZ2UgZm9yIHRoZSBsaWJyYXJ5LyBwYWNrYWdlOlxucHl0ZXN0IC0tY292PWxpYnJhcnkgdGVzdHMvXG5cbiMgU2FtcGxlIG91dHB1dDpcbiMgTmFtZSAgICAgICAgICAgICAgICAgICAgIFN0bXRzICAgTWlzcyAgQ292ZXJcbiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuIyBsaWJyYXJ5L2ZpbmVzLnB5ICAgICAgICAgICAgMTIgICAgICAyICAgIDgzJVxuIyBsaWJyYXJ5L2NhdGFsb2cucHkgICAgICAgICAgMzEgICAgICA1ICAgIDg0JVxuIyBsaWJyYXJ5L25vdGlmaWNhdGlvbnMucHkgICAgMTggICAgICA4ICAgIDU2JVxuIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4jIFRPVEFMICAgICAgICAgICAgICAgICAgICAgICA2MSAgICAgMTUgICAgNzUlIn0"
 width="100%"
></iframe>

The output shows: total statements in each file, how many were never executed, and the percentage covered.

## HTML Coverage Report

The terminal summary shows percentages but not which lines are missed. The HTML report shows the exact lines:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvdmVyYWdlIGNvZGUgMyIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDMuc2giLCJjb2RlIjoicHl0ZXN0IC0tY292PWxpYnJhcnkgLS1jb3YtcmVwb3J0PWh0bWwgdGVzdHMvXG4jIENyZWF0ZXMgaHRtbGNvdi9pbmRleC5odG1sIn0"
 width="100%"
></iframe>

Open `htmlcov/index.html` in a browser. Each file shows lines in green (covered) and red (not covered). This is the most useful view for finding gaps.

## Reading Coverage: What It Tells You and What It Does Not

Coverage tells you which lines were executed. It does not tell you whether the behavior on those lines was correct. A test that calls a function but does not assert anything achieves 100% coverage without testing anything.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvdmVyYWdlIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJkZWYgY2FsY3VsYXRlX2ZpbmUoZGF5c19vdmVyZHVlLCBkYWlseV9yYXRlPTAuNTApOlxuICAgIGlmIGRheXNfb3ZlcmR1ZSA8IDA6XG4gICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoXCJjYW5ub3QgYmUgbmVnYXRpdmVcIilcbiAgICByZXR1cm4gZGF5c19vdmVyZHVlICogZGFpbHlfcmF0ZVxuXG4jIFRoaXMgdGVzdCBjb3ZlcnMgYWxsIGxpbmVzIGJ1dCB0ZXN0cyBub3RoaW5nIG1lYW5pbmdmdWw6XG5kZWYgdGVzdF9jYWxjdWxhdGVfZmluZSgpOlxuICAgIGNhbGN1bGF0ZV9maW5lKDEwKSAgICMgbGluZSBleGVjdXRlZCAtLSBubyBhc3NlcnRcbiAgICAjIDEwMCUgY292ZXJhZ2UsIDAlIGNvbmZpZGVuY2UifQ"
 width="100%"
></iframe>

Coverage is a lower bound on test quality, not an upper bound. 100% coverage with no assertions proves only that the code does not crash.

## Branch Coverage

Line coverage misses the case where a line is reached but a branch within it is not taken. `--cov-branch` enables branch coverage:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvdmVyYWdlIGNvZGUgNSIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDUuc2giLCJjb2RlIjoicHl0ZXN0IC0tY292PWxpYnJhcnkgLS1jb3YtYnJhbmNoIHRlc3RzLyJ9"
 width="100%"
></iframe>

For `if days_overdue < 0: raise ValueError(...)`, branch coverage requires both the `True` path (exception raised) and the `False` path (normal return) to be exercised.

## Setting a Coverage Target

Configure a minimum acceptable coverage in `pyproject.toml` so the CI build fails if coverage drops below the target:

```toml
# pyproject.toml
[tool.pytest.ini_options]
addopts = "--cov=library --cov-report=term-missing --cov-fail-under=80"
```

`--cov-fail-under=80` makes `pytest` exit with a failure code if total coverage drops below 80%. `--cov-report=term-missing` adds a "missing lines" column to the terminal output.

## What Lines Not to Worry About

Not every uncovered line is a problem. Lines in `if __name__ == "__main__":` blocks, defensive error handlers for truly impossible conditions, and abstract methods that are never instantiated directly are commonly excluded from coverage targets.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvdmVyYWdlIGNvZGUgNiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNi5weSIsImNvZGUiOiIjIC5jb3ZlcmFnZXJjIG9yIHB5cHJvamVjdC50b21sIFt0b29sLmNvdmVyYWdlLnJlcG9ydF1cblt0b29sLmNvdmVyYWdlLnJlcG9ydF1cbmV4Y2x1ZGVfbGluZXMgPVxuICAgIHByYWdtYTogbm8gY292ZXJcbiAgICBpZiBfX25hbWVfXyA9PSBcIl9fbWFpbl9fXCI6XG4gICAgcmFpc2UgTm90SW1wbGVtZW50ZWRFcnJvciJ9"
 width="100%"
></iframe>

Any line with `# pragma: no cover` is excluded from the report.

## Coverage at a Glance

| Command | What it does |
|---|---|
| `pytest --cov=pkg` | Measure coverage for a package |
| `pytest --cov-report=html` | Generate HTML report |
| `pytest --cov-branch` | Also measure branch coverage |
| `pytest --cov-fail-under=80` | Fail build below coverage threshold |
| `# pragma: no cover` | Exclude a line from the report |

## Your Turn

Run the coverage report on your test suite from this unit:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvdmVyYWdlIGNvZGUgNyIsImxhbmd1YWdlIjoiYmFzaCIsImZpbGVuYW1lIjoibWFpbl8wMDcuc2giLCJjb2RlIjoicHl0ZXN0IC0tY292PWxpYnJhcnkgLS1jb3YtYnJhbmNoIC0tY292LXJlcG9ydD10ZXJtLW1pc3NpbmcgdGVzdHMvIn0"
 width="100%"
></iframe>

Find two lines that are not covered and write tests that cover them. Then add a coverage target to `pyproject.toml` that requires 80% line coverage.

## Conclusion

Coverage shows which code lines and branches your tests reach. It is a lower bound on quality, not an upper bound: 100% coverage with no assertions proves nothing about correctness. Branch coverage is more thorough than line coverage. A CI-enforced minimum target prevents the test suite from degrading over time. The final lesson in this unit shows how test-driven development uses tests not as a verification step but as a design tool, written before the code they test.
