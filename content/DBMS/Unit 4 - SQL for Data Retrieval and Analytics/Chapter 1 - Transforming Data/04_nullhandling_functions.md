## Introduction

Vikram maintains the employee directory for a mid-sized company, and the `employees` table has two honest gaps:

- Not every employee has a secondary phone number on file.
- Not every employee reports to a manager, since the CEO does not report to anyone.

Both gaps are stored as `NULL`, and both cause the same problem once Vikram tries to build a printable directory: `NULL` values show up as blank cells or, worse, silently break calculations that touch them. SQL provides two small but essential functions, **`COALESCE`** and **`NULLIF`**, built specifically to handle `NULL` gracefully instead of letting it derail a query.

## Filling In a Default When a Value Is Missing

The directory needs a phone number to display for every employee, even the ones with no secondary number recorded. Rather than leaving those rows blank, Vikram wants to fall back to the primary number, and if even that is missing, fall back to a placeholder.

```postgresql file=employees.sql
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    full_name TEXT,
    primary_phone TEXT,
    secondary_phone TEXT,
    manager_id INTEGER
);

INSERT INTO employees (employee_id, full_name, primary_phone, secondary_phone, manager_id) VALUES
(1, 'Neha Choudhary', '9811100001', '9811100002', NULL),
(2, 'Rahul Bose', '9811100003', NULL, 1),
(3, 'Ayesha Khan', NULL, NULL, 1),
(4, 'Manoj Tiwari', '9811100005', '9811100005', 2),
(5, 'Simran Kaur', '9811100006', NULL, 2);
```

```postgresql with=employees.sql
SELECT full_name, COALESCE(secondary_phone, primary_phone, 'Not on file') AS contact_number
FROM employees;
```

`COALESCE` scans its arguments left to right and returns the first one that is not `NULL`. For Rahul, `secondary_phone` is `NULL`, so it falls through to `primary_phone`. For Ayesha, both phone columns are `NULL`, so it falls all the way through to the literal text `'Not on file'`. This is the standard pattern for showing a sensible default instead of a blank space.

Tracing a few employees through the fallback chain makes the left-to-right scan concrete:

| Employee | `secondary_phone` | `primary_phone` | `contact_number` result |
|---|---|---|---|
| Rahul Bose | `NULL` | `9811100003` | `9811100003` (falls back one step) |
| Ayesha Khan | `NULL` | `NULL` | `'Not on file'` (falls back two steps) |
| Simran Kaur | `NULL` | `9811100006` | `9811100006` (falls back one step) |

## Treating Two Equal Values as Missing

Manoj's row has an odd duplication: his `primary_phone` and `secondary_phone` are identical, which happened because someone copied the primary number into the secondary field by mistake instead of leaving it blank. Vikram wants the directory to treat a secondary number that exactly matches the primary as if it were not really provided at all.

```postgresql with=employees.sql
SELECT full_name, primary_phone, secondary_phone,
       NULLIF(secondary_phone, primary_phone) AS real_secondary_phone
FROM employees;
```

`NULLIF(a, b)` compares its two arguments, and if they are equal, it returns `NULL`; otherwise it returns `a` unchanged. For Manoj, `secondary_phone` equals `primary_phone`, so the result is `NULL` instead of a duplicate number. For every other employee, the two phone values differ, so `real_secondary_phone` just passes through whatever `secondary_phone` already held.

## Combining Both to Handle Messy Real Data

The two functions are often used together: first clean up an accidental duplicate with `NULLIF`, then supply a fallback with `COALESCE` so the final column has no blanks left at all.

```postgresql with=employees.sql
SELECT full_name,
       COALESCE(NULLIF(secondary_phone, primary_phone), primary_phone, 'Not on file') AS best_contact_number
FROM employees;
```

Reading from the inside out: `NULLIF` first turns Manoj's duplicated secondary number into `NULL`, then `COALESCE` steps in and falls back to his `primary_phone` since the secondary is now effectively missing. Every other row resolves the same way it did before, since `NULLIF` only changes behavior when the two compared values are identical.

## COALESCE and NULLIF at a Glance

| Function | Purpose | Example |
|---|---|---|
| `COALESCE(a, b, c, ...)` | Return the first non-`NULL` argument | `COALESCE(secondary_phone, primary_phone, 'N/A')` |
| `NULLIF(a, b)` | Return `NULL` if `a` equals `b`, else return `a` | `NULLIF(secondary_phone, primary_phone)` |

## Your Turn

The company org chart needs a "reports to" column: for every employee, show their `employee_id` as the reporting line if `manager_id` is missing, otherwise show `manager_id` itself, aliased as `reports_to`. Write that query against the `employees` table above.

```postgresql with=employees.sql
-- Write your query below
```

If your query is `SELECT full_name, COALESCE(manager_id, employee_id) AS reports_to FROM employees;`, Neha's row will show her own `employee_id` in the `reports_to` column, correctly marking her as the top of the chart with nobody above her.

## Conclusion

`COALESCE` and `NULLIF` are small functions that solve a large, recurring problem: real data has gaps, and a query that ignores those gaps produces blank cells, broken math, or misleading duplicates. `COALESCE` fills a missing value with a fallback, and `NULLIF` turns an unwanted match into a `NULL` that `COALESCE` can then catch. Vikram's directory now shows a usable number for every employee and a clean reporting line for every row. Cleaning up individual values is one kind of transformation; choosing between entirely different outputs based on a condition is the next tool to add.
