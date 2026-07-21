## Introduction

Vikram maintains the employee directory for a mid-sized company, and the `employees` `table` has two honest gaps:

- Not every employee has a secondary phone number on file.
- Not every employee reports to a manager, since the CEO does not report to anyone.

Both gaps are stored as `NULL`, and both cause the same problem once Vikram tries to build a printable directory: `NULL` values show up as blank cells or, worse, silently break calculations that touch them. SQL provides two small but essential `functions`, **`COALESCE`** and **`NULLIF`**, built specifically to handle `NULL` gracefully instead of letting it derail a `query`.

**Definition:** `COALESCE` and `NULLIF` are small `functions` that solve a large, recurring problem: real data has gaps, and a `query` that ignores those gaps produces blank cells, broken math, or misleading duplicates.

![Intro visual for nullhandling functions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_intro_nullhandling_functions.png)

## Filling In a Default When a Value Is Missing

The directory needs a phone number to display for every employee, even the ones with no secondary number recorded, Rather than leaving those `rows` blank, Vikram wants to fall back to the primary number, and if even that is missing, fall back to a placeholder.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the data they will use. The tables below show the rows loaded by the setup file.

### `employees`

| employee_id | full_name | primary_phone | secondary_phone | manager_id |
| --- | --- | --- | --- | --- |
| 1 | Neha Choudhary | 9811100001 | 9811100002 | *NULL* |
| 2 | Rahul Bose | 9811100003 | *NULL* | 1 |
| 3 | Ayesha Khan | *NULL* | *NULL* | 1 |
| 4 | Manoj Tiwari | 9811100005 | 9811100005 | 2 |
| 5 | Simran Kaur | 9811100006 | *NULL* | 2 |

The OneCompiler activity keeps setup and practice separate. `init.sql` creates and populates the displayed data, while the active SQL file contains only the query being studied.

## Hands-On Setup: Prepare the Data

```postgresql
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

Before running the active query, read its `SELECT` list and clauses against the displayed source rows. Then compare the returned values with the expected output to see exactly what the function or operation changed.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakvhc" 
 width="100%"
></iframe>

Expected output:

| full_name | contact_number |
| --- | --- |
| Neha Choudhary | 9811100002 |
| Rahul Bose | 9811100003 |
| Ayesha Khan | Not on file |
| Manoj Tiwari | 9811100005 |
| Simran Kaur | 9811100006 |

- `COALESCE` scans its arguments left to right and returns the first one that is not `NULL`.
- For Rahul, `secondary_phone` is `NULL`, so it falls through to `primary_phone`.
- For Ayesha, both phone `columns` are `NULL`, so it falls all the way through to the literal text `'Not on file'`.
- This is the standard pattern for showing a sensible default instead of a blank space.

![COALESCE choosing the first available phone value as a contact number](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_coalesce_first_available_fallback.png)

Tracing a few employees through the fallback chain makes the left-to-right scan concrete:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Employee</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"><code>secondary_phone</code></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"><code>primary_phone</code></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"><code>contact_number</code> result</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rahul Bose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NULL</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>9811100003</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>9811100003</code> (falls back one step)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ayesha Khan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NULL</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NULL</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>&#x27;Not on file&#x27;</code> (falls back two steps)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simran Kaur</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NULL</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>9811100006</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>9811100006</code> (falls back one step)</td>
    </tr>
  </tbody>
</table>

## Treating Two Equal Values as Missing

Manoj's `row` has an odd duplication: his `primary_phone` and `secondary_phone` are identical, which happened because someone copied the primary number into the secondary field by mistake instead of leaving it blank. Vikram wants the directory to treat a secondary number that exactly matches the primary as if it were not really provided at all.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakvvt" 
 width="100%"
></iframe>

Expected output:

| full_name | primary_phone | secondary_phone | real_secondary_phone |
| --- | --- | --- | --- |
| Neha Choudhary | 9811100001 | 9811100002 | 9811100002 |
| Rahul Bose | 9811100003 | *NULL* | *NULL* |
| Ayesha Khan | *NULL* | *NULL* | *NULL* |
| Manoj Tiwari | 9811100005 | 9811100005 | *NULL* |
| Simran Kaur | 9811100006 | *NULL* | *NULL* |

- `NULLIF(a, b)` compares its two arguments, and if they are equal, it returns `NULL`; otherwise it returns `a` unchanged.
- For Manoj, `secondary_phone` equals `primary_phone`, so the result is `NULL` instead of a duplicate number.
- For every other employee, the two phone values differ, so `real_secondary_phone` just passes through whatever `secondary_phone` already held.

![NULLIF turning a duplicated secondary phone into NULL](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_nullif_duplicate_to_null.png)

## Combining Both to Handle Messy Real Data

The two `functions` are often used together: first clean up an accidental duplicate with `NULLIF`, then supply a fallback with `COALESCE` so the final `column` has no blanks left at all.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakw86" 
 width="100%"
></iframe>

Expected output:

| full_name | best_contact_number |
| --- | --- |
| Neha Choudhary | 9811100002 |
| Rahul Bose | 9811100003 |
| Ayesha Khan | Not on file |
| Manoj Tiwari | 9811100005 |
| Simran Kaur | 9811100006 |

- Reading from the inside out: `NULLIF` first turns Manoj's duplicated secondary number into `NULL`, then `COALESCE` steps in and falls back to his `primary_phone` since the secondary is now effectively missing.
- Every other `row` resolves the same way it did before, since `NULLIF` only changes behavior when the two compared values are identical.

## COALESCE and NULLIF at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Function</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>COALESCE(a, b, c, ...)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Return the first non-<code>NULL</code> argument</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>COALESCE(secondary_phone, primary_phone, &#x27;N/A&#x27;)</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NULLIF(a, b)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Return <code>NULL</code> if <code>a</code> equals <code>b</code>, else return <code>a</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NULLIF(secondary_phone, primary_phone)</code></td>
    </tr>
  </tbody>
</table>

## Your Turn

The company org chart needs a "reports to" `column`: for every employee, show their `employee_id` as the reporting line if `manager_id` is missing, otherwise show `manager_id` itself, aliased as `reports_to`. Write that `query` against the `employees` `table` above.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakwjc" 
 width="100%"
></iframe>

If your `query` is `SELECT full_name, COALESCE(manager_id, employee_id) AS reports_to FROM employees;`, Neha's `row` will show her own `employee_id` in the `reports_to` `column`, correctly marking her as the top of the chart with nobody above her.


Expected output for the practice query:

| full_name | reports_to |
| --- | --- |
| Neha Choudhary | 1 |
| Rahul Bose | 1 |
| Ayesha Khan | 1 |
| Manoj Tiwari | 2 |
| Simran Kaur | 2 |

## Conclusion

`COALESCE` and `NULLIF` are small `functions` that solve a large, recurring problem: real data has gaps, and a `query` that ignores those gaps produces blank cells, broken math, or misleading duplicates.

`COALESCE` fills a missing value with a fallback, and `NULLIF` turns an unwanted match into a `NULL` that `COALESCE` can then catch.

Vikram's directory now shows a usable number for every employee and a clean reporting line for every `row`.

Cleaning up individual values is one kind of transformation; choosing between entirely different outputs based on a condition is the next tool to add.
