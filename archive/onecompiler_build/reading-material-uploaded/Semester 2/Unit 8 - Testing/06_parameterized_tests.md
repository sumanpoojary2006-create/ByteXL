## Introduction

Sam needs to test `calculate_fine` for many different inputs: 0 days, 1 day, 7 days, 14 days, 30 days, 365 days, and two custom daily rates. Writing a separate test function for each combination means eleven almost-identical functions. If the function signature changes, he updates eleven places instead of one.

`pytest.mark.parametrize` solves this: write the test logic once, and provide a table of inputs and expected outputs. `pytest` generates a separate test case for each row in the table.

![A test function shown once on the left, with an arrow pointing right to a grid of five separate test cases, each showing a different (input, expected) pair from the parametrize table](images/06_parameterized_tests.png)

## Basic Parametrize

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-06-parameterized-tests-001-8be57bd83b.html"
 width="100%"
></iframe>

The decorator receives:
1. A string naming the parameters (comma-separated if multiple)
2. A list of tuples, one per test case

`pytest` runs the function once per tuple, substituting the tuple values for the parameters. The test names in the output are:

```
test_fine_calculation[0-0.0]
test_fine_calculation[1-0.5]
test_fine_calculation[7-3.5]
...
```

## Named Test Cases

For clearer output, use `pytest.param` with an `id`:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-06-parameterized-tests-002-32ef17194c.html"
 width="100%"
></iframe>

Output names become: `test_fine_calculation[zero-days]`, `test_fine_calculation[one-day]`, etc. Much easier to identify in a failure report.

## Multiple Parameters

When testing a function that takes multiple arguments:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-06-parameterized-tests-003-686d87dbd7.html"
 width="100%"
></iframe>

## Parametrizing Expected Exceptions

Combine `parametrize` with `pytest.raises` to test multiple error cases:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-06-parameterized-tests-004-9c7c28cbd7.html"
 width="100%"
></iframe>

## Combining Parametrize with Fixtures

Parametrized tests can also use fixtures:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-06-parameterized-tests-005-23c4413a88.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-8-testing-06-parameterized-tests-006-edcb95bb61.html"
 width="100%"
></iframe>

## Conclusion

`pytest.mark.parametrize` turns a single test function into a battery of test cases with one table. Named test cases with `pytest.param(id=...)` make failure output readable. Parametrize composes with fixtures, making it the standard tool for concise, comprehensive test coverage. The next lesson covers mocking and patching: testing code that depends on external systems without actually calling those systems.
