## Introduction

Sam needs to test `calculate_fine` for many different inputs: 0 days, 1 day, 7 days, 14 days, 30 days, 365 days, and two custom daily rates. Writing a separate test function for each combination means eleven almost-identical functions. If the function signature changes, he updates eleven places instead of one.

`pytest.mark.parametrize` solves this: write the test logic once, and provide a table of inputs and expected outputs. `pytest` generates a separate test case for each row in the table.

![A test function shown once on the left, with an arrow pointing right to a grid of five separate test cases, each showing a different (input, expected) pair from the parametrize table](images/06_parameterized_tests.png)

## Basic Parametrize

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3BhcmFtZXRlcml6ZWRfdGVzdHMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImltcG9ydCBtYXRoXG5pbXBvcnQgcHl0ZXN0XG5mcm9tIGxpYnJhcnkuZmluZXMgaW1wb3J0IGNhbGN1bGF0ZV9maW5lXG5cbkBweXRlc3QubWFyay5wYXJhbWV0cml6ZShcImRheXNfb3ZlcmR1ZSxleHBlY3RlZF9maW5lXCIsIFtcbiAgICAoMCwgICAwLjAwKSxcbiAgICAoMSwgICAwLjUwKSxcbiAgICAoNywgICAzLjUwKSxcbiAgICAoMTQsICA3LjAwKSxcbiAgICAoMzAsIDE1LjAwKSxcbiAgICAoMzY1LCAxODIuNTApLFxuXSlcbmRlZiB0ZXN0X2ZpbmVfY2FsY3VsYXRpb24oZGF5c19vdmVyZHVlLCBleHBlY3RlZF9maW5lKTpcbiAgICByZXN1bHQgPSBjYWxjdWxhdGVfZmluZShkYXlzX292ZXJkdWUpXG4gICAgYXNzZXJ0IG1hdGguaXNjbG9zZShyZXN1bHQsIGV4cGVjdGVkX2ZpbmUpIn0"
 width="100%"
></iframe>

The decorator receives:
1. A string naming the parameters (comma-separated if multiple)
2. A list of tuples, one per test case

`pytest` runs the function once per tuple, substituting the tuple values for the parameters. The test names in the output are:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3BhcmFtZXRlcml6ZWRfdGVzdHMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6InRlc3RfZmluZV9jYWxjdWxhdGlvblswLTAuMF1cbnRlc3RfZmluZV9jYWxjdWxhdGlvblsxLTAuNV1cbnRlc3RfZmluZV9jYWxjdWxhdGlvbls3LTMuNV1cbi4uLiJ9"
 width="100%"
></iframe>

## Named Test Cases

For clearer output, use `pytest.param` with an `id`:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3BhcmFtZXRlcml6ZWRfdGVzdHMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6IkBweXRlc3QubWFyay5wYXJhbWV0cml6ZShcImRheXNfb3ZlcmR1ZSxleHBlY3RlZF9maW5lXCIsIFtcbiAgICBweXRlc3QucGFyYW0oMCwgICAwLjAwLCAgIGlkPVwiemVyby1kYXlzXCIpLFxuICAgIHB5dGVzdC5wYXJhbSgxLCAgIDAuNTAsICAgaWQ9XCJvbmUtZGF5XCIpLFxuICAgIHB5dGVzdC5wYXJhbSgxNCwgIDcuMDAsICAgaWQ9XCJ0d28td2Vla3NcIiksXG4gICAgcHl0ZXN0LnBhcmFtKDM2NSwgMTgyLjUwLCBpZD1cIm9uZS15ZWFyXCIpLFxuXSlcbmRlZiB0ZXN0X2ZpbmVfY2FsY3VsYXRpb24oZGF5c19vdmVyZHVlLCBleHBlY3RlZF9maW5lKTpcbiAgICBhc3NlcnQgbWF0aC5pc2Nsb3NlKGNhbGN1bGF0ZV9maW5lKGRheXNfb3ZlcmR1ZSksIGV4cGVjdGVkX2ZpbmUpIn0"
 width="100%"
></iframe>

Output names become: `test_fine_calculation[zero-days]`, `test_fine_calculation[one-day]`, etc. Much easier to identify in a failure report.

## Multiple Parameters

When testing a function that takes multiple arguments:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3BhcmFtZXRlcml6ZWRfdGVzdHMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6IkBweXRlc3QubWFyay5wYXJhbWV0cml6ZShcImRheXMscmF0ZSxleHBlY3RlZFwiLCBbXG4gICAgKDEwLCAwLjUwLCA1LjAwKSxcbiAgICAoMTAsIDEuMDAsIDEwLjAwKSxcbiAgICAoMTQsIDAuNzUsIDEwLjUwKSxcbiAgICAoIDAsIDIuMDAsICAwLjAwKSxcbl0pXG5kZWYgdGVzdF9maW5lX2N1c3RvbV9yYXRlKGRheXMsIHJhdGUsIGV4cGVjdGVkKTpcbiAgICBhc3NlcnQgbWF0aC5pc2Nsb3NlKGNhbGN1bGF0ZV9maW5lKGRheXMsIGRhaWx5X3JhdGU9cmF0ZSksIGV4cGVjdGVkKSJ9"
 width="100%"
></iframe>

## Parametrizing Expected Exceptions

Combine `parametrize` with `pytest.raises` to test multiple error cases:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3BhcmFtZXRlcml6ZWRfdGVzdHMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6IkBweXRlc3QubWFyay5wYXJhbWV0cml6ZShcImJhZF9pbnB1dFwiLCBbXG4gICAgcHl0ZXN0LnBhcmFtKC0xLCAgIGlkPVwibWludXMtb25lXCIpLFxuICAgIHB5dGVzdC5wYXJhbSgtMTAwLCBpZD1cImxhcmdlLW5lZ2F0aXZlXCIpLFxuXSlcbmRlZiB0ZXN0X2ZpbmVfbmVnYXRpdmVfcmFpc2VzKGJhZF9pbnB1dCk6XG4gICAgd2l0aCBweXRlc3QucmFpc2VzKFZhbHVlRXJyb3IsIG1hdGNoPVwiY2Fubm90IGJlIG5lZ2F0aXZlXCIpOlxuICAgICAgICBjYWxjdWxhdGVfZmluZShiYWRfaW5wdXQpIn0"
 width="100%"
></iframe>

## Combining Parametrize with Fixtures

Parametrized tests can also use fixtures:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3BhcmFtZXRlcml6ZWRfdGVzdHMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6IkBweXRlc3QuZml4dHVyZVxuZGVmIGNhdGFsb2coc2FtcGxlX2Jvb2spOlxuICAgIGMgPSBDYXRhbG9nKClcbiAgICBjLmFkZChzYW1wbGVfYm9vaylcbiAgICByZXR1cm4gY1xuXG5AcHl0ZXN0Lm1hcmsucGFyYW1ldHJpemUoXCJpc2JuLHNob3VsZF9maW5kXCIsIFtcbiAgICAoXCI5NzgtMDAxXCIsIFRydWUpLFxuICAgIChcIjk3OC05OTlcIiwgRmFsc2UpLFxuXSlcbmRlZiB0ZXN0X2NhdGFsb2dfZmluZChjYXRhbG9nLCBpc2JuLCBzaG91bGRfZmluZCk6XG4gICAgcmVzdWx0ID0gY2F0YWxvZy5maW5kKGlzYm4pXG4gICAgaWYgc2hvdWxkX2ZpbmQ6XG4gICAgICAgIGFzc2VydCByZXN1bHQgaXMgbm90IE5vbmVcbiAgICBlbHNlOlxuICAgICAgICBhc3NlcnQgcmVzdWx0IGlzIE5vbmUifQ"
 width="100%"
></iframe>

`pytest` passes both the fixture and the parametrize values to the test function.

## Parametrize at a Glance

| Feature | Syntax |
|---|---|
| Basic parametrize | `@pytest.mark.parametrize("name", [val1, val2])` |
| Multiple parameters | `@pytest.mark.parametrize("a,b", [(1, 2), (3, 4)])` |
| Named test cases | `pytest.param(val, id="name")` |
| Exception cases | Combine with `pytest.raises` inside the function body |
| With fixtures | Declare fixture parameter alongside parametrize parameters |

## Your Turn

Write a parametrized test for `overdue_report` that covers these cases:

| Test ID | borrow_date | loan_days | today | expected overdue count |
|---|---|---|---|---|
| not-overdue | 2026-06-20 | 21 | 2026-07-10 | 0 |
| one-day-over | 2026-06-20 | 21 | 2026-07-12 | 1 |
| exact-due-date | 2026-06-20 | 21 | 2026-07-11 | 0 |
| multiple-overdue | 2026-06-01 | 7  | 2026-07-01 | 1 |

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X3BhcmFtZXRlcml6ZWRfdGVzdHMgY29kZSA3IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA3LnB5IiwiY29kZSI6ImZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGVcbmltcG9ydCBweXRlc3RcbmZyb20gbGlicmFyeS5yZXBvcnRzIGltcG9ydCBvdmVyZHVlX3JlcG9ydFxuXG5AcHl0ZXN0Lm1hcmsucGFyYW1ldHJpemUoXCJib3Jyb3dfZGF0ZSxsb2FuX2RheXMsdG9kYXlfc3RyLGV4cGVjdGVkX2NvdW50XCIsIFtcbiAgICBweXRlc3QucGFyYW0oXCIyMDI2LTA2LTIwXCIsIDIxLCBcIjIwMjYtMDctMTBcIiwgMCwgaWQ9XCJub3Qtb3ZlcmR1ZVwiKSxcbiAgICBweXRlc3QucGFyYW0oXCIyMDI2LTA2LTIwXCIsIDIxLCBcIjIwMjYtMDctMTJcIiwgMSwgaWQ9XCJvbmUtZGF5LW92ZXJcIiksXG4gICAgcHl0ZXN0LnBhcmFtKFwiMjAyNi0wNi0yMFwiLCAyMSwgXCIyMDI2LTA3LTExXCIsIDAsIGlkPVwiZXhhY3QtZHVlLWRhdGVcIiksXG4gICAgcHl0ZXN0LnBhcmFtKFwiMjAyNi0wNi0wMVwiLCAgNywgXCIyMDI2LTA3LTAxXCIsIDEsIGlkPVwibXVsdGlwbGUtb3ZlcmR1ZVwiKSxcbl0pXG5kZWYgdGVzdF9vdmVyZHVlX3JlcG9ydChib3Jyb3dfZGF0ZSwgbG9hbl9kYXlzLCB0b2RheV9zdHIsIGV4cGVjdGVkX2NvdW50KTpcbiAgICByZWNvcmRzID0gW3tcImlzYm5cIjogXCI5NzgtMDAxXCIsIFwicGF0cm9uX2lkXCI6IFwiUDAwMVwiLFxuICAgICAgICAgICAgICAgIFwiYm9ycm93X2RhdGVcIjogYm9ycm93X2RhdGUsIFwibG9hbl9kYXlzXCI6IGxvYW5fZGF5c31dXG4gICAgcmVzdWx0ID0gb3ZlcmR1ZV9yZXBvcnQocmVjb3JkcywgdG9kYXk9ZGF0ZS5mcm9taXNvZm9ybWF0KHRvZGF5X3N0cikpXG4gICAgYXNzZXJ0IGxlbihyZXN1bHQpID09IGV4cGVjdGVkX2NvdW50In0"
 width="100%"
></iframe>

## Conclusion

`pytest.mark.parametrize` turns a single test function into a battery of test cases with one table. Named test cases with `pytest.param(id=...)` make failure output readable. Parametrize composes with fixtures, making it the standard tool for concise, comprehensive test coverage. The next lesson covers mocking and patching: testing code that depends on external systems without actually calling those systems.
