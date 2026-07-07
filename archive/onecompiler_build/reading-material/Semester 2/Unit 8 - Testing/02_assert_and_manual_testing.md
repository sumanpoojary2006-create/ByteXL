## Introduction

Before Sam learns about any testing framework, his team lead wants him to understand the single building block that all Python tests are built on: the `assert` statement. It is already in the language and requires no installation. Understanding it well makes everything in the testing framework more intuitive.

![The word assert followed by an expression and an optional message, shown as a gate: if the expression is True, execution passes through; if False, an AssertionError is raised with the message](images/02_assert_manual_testing.png)

## The assert Statement

`assert expression` does nothing if `expression` is truthy, and raises `AssertionError` if it is falsy. It is the programmatic version of "this must be true here."

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Fzc2VydF9hbmRfbWFudWFsX3Rlc3RpbmcgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6IiMgUGFzc2VzOiBubyBvdXRwdXQsIG5vIGVycm9yXG5hc3NlcnQgMSArIDEgPT0gMlxuYXNzZXJ0IGxlbihcImhlbGxvXCIpID09IDVcbmFzc2VydCBbMSwgMiwgM10gIT0gW11cblxuIyBGYWlsczogcmFpc2VzIEFzc2VydGlvbkVycm9yXG5hc3NlcnQgMSArIDEgPT0gMyAgICAgICAgIyBBc3NlcnRpb25FcnJvclxuXG4jIFdpdGggYSBtZXNzYWdlICh0aGUgbWVzc2FnZSBhcHBlYXJzIGluIHRoZSBBc3NlcnRpb25FcnJvcilcbnJlc3VsdCA9IDVcbmFzc2VydCByZXN1bHQgPT0gMTAsIGZcIkV4cGVjdGVkIDEwLCBnb3Qge3Jlc3VsdH1cIlxuIyBBc3NlcnRpb25FcnJvcjogRXhwZWN0ZWQgMTAsIGdvdCA1In0"
 width="100%"
></iframe>

Always include a message. Without one, the error says only `AssertionError` with no indication of what was wrong.

## Asserting with Context

The most useful assertions compare expected and actual values directly:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Fzc2VydF9hbmRfbWFudWFsX3Rlc3RpbmcgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImRlZiBjYWxjdWxhdGVfZmluZShkYXlzX292ZXJkdWUsIGRhaWx5X3JhdGU9MC41MCk6XG4gICAgcmV0dXJuIGRheXNfb3ZlcmR1ZSAqIGRhaWx5X3JhdGVcblxuIyBUZXN0IGJ5IGNhbGxpbmcgdGhlIGZ1bmN0aW9uIGFuZCBhc3NlcnRpbmcgdGhlIHJlc3VsdFxuYWN0dWFsID0gY2FsY3VsYXRlX2ZpbmUoMTApXG5leHBlY3RlZCA9IDUuMFxuYXNzZXJ0IGFjdHVhbCA9PSBleHBlY3RlZCwgZlwiRmluZSBmb3IgMTAgZGF5czogZXhwZWN0ZWQge2V4cGVjdGVkfSwgZ290IHthY3R1YWx9XCJcblxuYWN0dWFsID0gY2FsY3VsYXRlX2ZpbmUoMClcbmFzc2VydCBhY3R1YWwgPT0gMC4wLCBmXCJGaW5lIGZvciAwIGRheXM6IGV4cGVjdGVkIDAuMCwgZ290IHthY3R1YWx9XCIifQ"
 width="100%"
></iframe>

## Asserting Exceptions

To test that a function raises a specific exception, you need to catch it and confirm the type. Python's `pytest` framework provides a cleaner way (covered in the next lesson), but the raw approach shows what is happening underneath:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Fzc2VydF9hbmRfbWFudWFsX3Rlc3RpbmcgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImRlZiBnZXRfYm9vayhpc2JuLCBjYXRhbG9nKTpcbiAgICBpZiBpc2JuIG5vdCBpbiBjYXRhbG9nOlxuICAgICAgICByYWlzZSBLZXlFcnJvcihmXCJCb29rIG5vdCBmb3VuZDoge2lzYm59XCIpXG4gICAgcmV0dXJuIGNhdGFsb2dbaXNibl1cblxuIyBUZXN0IHRoYXQgdGhlIGV4Y2VwdGlvbiBpcyByYWlzZWQ6XG5yYWlzZWQgPSBGYWxzZVxudHJ5OlxuICAgIGdldF9ib29rKFwibWlzc2luZy1pc2JuXCIsIHt9KVxuZXhjZXB0IEtleUVycm9yOlxuICAgIHJhaXNlZCA9IFRydWVcblxuYXNzZXJ0IHJhaXNlZCwgXCJFeHBlY3RlZCBLZXlFcnJvciB3YXMgbm90IHJhaXNlZFwiIn0"
 width="100%"
></iframe>

## Floating-Point Comparisons

Floating-point arithmetic introduces rounding errors. Never compare floats with `==` in tests:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Fzc2VydF9hbmRfbWFudWFsX3Rlc3RpbmcgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6IiMgVGhpcyBtYXkgZmFpbCBkdWUgdG8gZmxvYXQgcm91bmRpbmc6XG5hc3NlcnQgMC4xICsgMC4yID09IDAuMyAgICAjIEZhbHNlISAwLjEgKyAwLjIgPSAwLjMwMDAwMDAwMDAwMDAwMDA0XG5cbiMgU2FmZTogY29tcGFyZSB3aXRoaW4gYSB0b2xlcmFuY2VcbmltcG9ydCBtYXRoXG5hc3NlcnQgbWF0aC5pc2Nsb3NlKDAuMSArIDAuMiwgMC4zLCByZWxfdG9sPTFlLTkpICAgIyBUcnVlIn0"
 width="100%"
></iframe>

`math.isclose` checks whether two floats are equal within a relative tolerance. Use it whenever testing float results.

## Running Tests Manually

A simple manual test file collects all assertions into functions. Running the file with Python executes them:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Fzc2VydF9hbmRfbWFudWFsX3Rlc3RpbmcgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IiMgdGVzdF9maW5lcy5weVxuZnJvbSBsaWJyYXJ5IGltcG9ydCBjYWxjdWxhdGVfZmluZVxuaW1wb3J0IG1hdGhcblxuZGVmIHRlc3RfZmluZV9ub3JtYWwoKTpcbiAgICBhc3NlcnQgbWF0aC5pc2Nsb3NlKGNhbGN1bGF0ZV9maW5lKDEwKSwgNS4wKVxuXG5kZWYgdGVzdF9maW5lX3plcm9fZGF5cygpOlxuICAgIGFzc2VydCBjYWxjdWxhdGVfZmluZSgwKSA9PSAwLjBcblxuZGVmIHRlc3RfZmluZV9jdXN0b21fcmF0ZSgpOlxuICAgIGFzc2VydCBtYXRoLmlzY2xvc2UoY2FsY3VsYXRlX2ZpbmUoMTAsIGRhaWx5X3JhdGU9MS4wMCksIDEwLjApXG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICB0ZXN0X2ZpbmVfbm9ybWFsKClcbiAgICB0ZXN0X2ZpbmVfemVyb19kYXlzKClcbiAgICB0ZXN0X2ZpbmVfY3VzdG9tX3JhdGUoKVxuICAgIHByaW50KFwiQWxsIHRlc3RzIHBhc3NlZC5cIikifQ"
 width="100%"
></iframe>

This works but has a limitation: if one test fails, the rest do not run. A testing framework like `pytest` runs all tests and reports all failures at once.

## assert in Production Code

`assert` in production code is risky: Python can be run with the `-O` (optimize) flag, which strips all `assert` statements. Use `raise` instead for runtime validation that must always run:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Fzc2VydF9hbmRfbWFudWFsX3Rlc3RpbmcgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6IiMgRG8gTk9UIHVzZSBhc3NlcnQgZm9yIGlucHV0IHZhbGlkYXRpb24gaW4gcHJvZHVjdGlvbiBjb2RlOlxuZGVmIGNhbGN1bGF0ZV9maW5lKGRheXNfb3ZlcmR1ZSwgZGFpbHlfcmF0ZT0wLjUwKTpcbiAgICBhc3NlcnQgZGF5c19vdmVyZHVlID49IDAsIFwiZGF5c19vdmVyZHVlIGNhbm5vdCBiZSBuZWdhdGl2ZVwiICAjIHN0cmlwcGVkIGJ5IC1PXG5cbiMgVXNlIHJhaXNlIGluc3RlYWQ6XG5kZWYgY2FsY3VsYXRlX2ZpbmUoZGF5c19vdmVyZHVlLCBkYWlseV9yYXRlPTAuNTApOlxuICAgIGlmIGRheXNfb3ZlcmR1ZSA8IDA6XG4gICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoZlwiZGF5c19vdmVyZHVlIGNhbm5vdCBiZSBuZWdhdGl2ZToge2RheXNfb3ZlcmR1ZX1cIilcbiAgICByZXR1cm4gZGF5c19vdmVyZHVlICogZGFpbHlfcmF0ZSJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAyX2Fzc2VydF9hbmRfbWFudWFsX3Rlc3RpbmcgY29kZSA3IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA3LnB5IiwiY29kZSI6ImltcG9ydCBtYXRoXG5cbmRlZiBjYWxjdWxhdGVfZmluZShkYXlzX292ZXJkdWUsIGRhaWx5X3JhdGU9MC41MCk6XG4gICAgaWYgZGF5c19vdmVyZHVlIDwgMDpcbiAgICAgICAgcmFpc2UgVmFsdWVFcnJvcihcImRheXNfb3ZlcmR1ZSBjYW5ub3QgYmUgbmVnYXRpdmVcIilcbiAgICByZXR1cm4gZGF5c19vdmVyZHVlICogZGFpbHlfcmF0ZVxuXG5kZWYgdGVzdF9ub3JtYWwoKTpcbiAgICBhc3NlcnQgbWF0aC5pc2Nsb3NlKGNhbGN1bGF0ZV9maW5lKDEwKSwgNS4wKVxuXG5kZWYgdGVzdF96ZXJvKCk6XG4gICAgYXNzZXJ0IGNhbGN1bGF0ZV9maW5lKDApID09IDAuMFxuXG5kZWYgdGVzdF9vbmVfZGF5KCk6XG4gICAgYXNzZXJ0IG1hdGguaXNjbG9zZShjYWxjdWxhdGVfZmluZSgxKSwgMC41MClcblxuZGVmIHRlc3RfbGFyZ2UoKTpcbiAgICBhc3NlcnQgbWF0aC5pc2Nsb3NlKGNhbGN1bGF0ZV9maW5lKDEwMCksIDUwLjApXG5cbmRlZiB0ZXN0X2N1c3RvbV9yYXRlKCk6XG4gICAgYXNzZXJ0IG1hdGguaXNjbG9zZShjYWxjdWxhdGVfZmluZSgxMCwgZGFpbHlfcmF0ZT0xLjAwKSwgMTAuMClcblxuZGVmIHRlc3RfbmVnYXRpdmVfcmFpc2VzKCk6XG4gICAgcmFpc2VkID0gRmFsc2VcbiAgICB0cnk6XG4gICAgICAgIGNhbGN1bGF0ZV9maW5lKC0xKVxuICAgIGV4Y2VwdCBWYWx1ZUVycm9yOlxuICAgICAgICByYWlzZWQgPSBUcnVlXG4gICAgYXNzZXJ0IHJhaXNlZCwgXCJFeHBlY3RlZCBWYWx1ZUVycm9yIGZvciBuZWdhdGl2ZSBpbnB1dFwiXG5cbmlmIF9fbmFtZV9fID09IFwiX19tYWluX19cIjpcbiAgICB0ZXN0X25vcm1hbCgpXG4gICAgdGVzdF96ZXJvKClcbiAgICB0ZXN0X29uZV9kYXkoKVxuICAgIHRlc3RfbGFyZ2UoKVxuICAgIHRlc3RfY3VzdG9tX3JhdGUoKVxuICAgIHRlc3RfbmVnYXRpdmVfcmFpc2VzKClcbiAgICBwcmludChcIkFsbCB0ZXN0cyBwYXNzZWQuXCIpIn0"
 width="100%"
></iframe>

## Conclusion

`assert` is the foundation of Python testing: it checks a condition and raises `AssertionError` with a message if it fails. Use `math.isclose` for floats. Reserve `raise` for production validation and `assert` for test code. The next lesson introduces `pytest`, which discovers and runs these functions automatically, collects all failures in one report, and provides much better error messages than raw assertions.
