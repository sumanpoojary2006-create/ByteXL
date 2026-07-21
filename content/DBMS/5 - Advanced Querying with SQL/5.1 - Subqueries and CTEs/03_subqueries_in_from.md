## Introduction

Kabir's next report needs a two-step calculation: first, find the average salary within each department, then find which departments pay above the overall company average. The first step is a grouped `query`. The second step needs to treat the result of that grouped `query` as if it were itself a `table`, filtering and comparing `rows` that do not exist anywhere in the original `employees` `table`, only in the summarized output.

A subquery does not have to sit inside `WHERE` producing a single value or a list; it can also sit inside `FROM`, standing in for an entire `table`. This kind of subquery is often called a **derived `table`**.

**Definition:** A subquery in `FROM`, or derived `table`, lets a `query` treat an intermediate result, especially a grouped or aggregated one, as if it were a real `table`, complete with the ability to filter, `join`, or select from it further.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_subqueries_in_from.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Kabir's next report needs a two-step calculation: first, find the average salary within each department, then find which departments pay above the overall company average. The first step is a grouped query. The second step needs to treat the result of that.

ON-IMAGE TEXT: show a short bold title "Subqueries In From" plus only these few labels, large and legible: Table, Query, Where. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for subqueries in from](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_intro_subqueries_in_from_clean_126d3ca3.png)

## Treating a Query's Result as a Table

The `employees` `table` is the same one used throughout this chapter.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `employees`

| employee_id | employee_name | department | salary | manager_id |
| --- | --- | --- | --- | --- |
| 1 | Ananya Sharma | Engineering | 95000.00 | NULL |
| 2 | Rajat Bhatia | Engineering | 78000.00 | 1 |
| 3 | Meghna Iyer | Engineering | 82000.00 | 1 |
| 4 | Sameer Khan | Sales | 65000.00 | NULL |
| 5 | Pooja Reddy | Sales | 58000.00 | 4 |
| 6 | Vikas Malhotra | Marketing | 60000.00 | NULL |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    department TEXT,
    salary NUMERIC(10, 2),
    manager_id INTEGER
);

INSERT INTO employees (employee_id, employee_name, department, salary, manager_id) VALUES
(1, 'Ananya Sharma', 'Engineering', 95000.00, NULL),
(2, 'Rajat Bhatia', 'Engineering', 78000.00, 1),
(3, 'Meghna Iyer', 'Engineering', 82000.00, 1),
(4, 'Sameer Khan', 'Sales', 65000.00, NULL),
(5, 'Pooja Reddy', 'Sales', 58000.00, 4),
(6, 'Vikas Malhotra', 'Marketing', 60000.00, NULL);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
SELECT department, AVG(salary) AS department_avg
FROM employees
GROUP BY department;
```

Expected output:

| department | department_avg |
| --- | --- |
| Engineering | 85000.00 |
| Marketing | 60000.00 |
| Sales | 61500.00 |

This is the first step on its own: three `rows`, one average per department. Now that same `query` becomes the `FROM` clause of an outer `query`, wrapped in parentheses and given an alias.

```postgresql with=init.sql
SELECT department, department_avg
FROM (
    SELECT department, AVG(salary) AS department_avg
    FROM employees
    GROUP BY department
) AS dept_averages
WHERE department_avg > (SELECT AVG(salary) FROM employees);
```

The subquery in `FROM`, aliased here as `dept_averages`, runs first and produces a small three-`row` result:

Expected output:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">department</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">department_avg</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Engineering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">85000.00</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sales</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">61500.00</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Marketing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">60000.00</td>
    </tr>
  </tbody>
</table>

The outer `query` then treats `dept_averages` exactly like a real `table`, filtering its `rows` with a `WHERE` clause that compares `department_avg`, a `column` that only exists because the inner `query` computed it, against the company-wide average of 73000.00 from a second subquery. Engineering is the only department whose average clears the company-wide bar.

![A FROM subquery producing a derived table that the outer query can filter](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_from_subquery_derived_table.png)

## Why a FROM Subquery Needs an Alias

Every subquery used in `FROM` must be given a name, since the outer `query` needs some way to refer to it, the same way any real `table` needs a name to be selected from.

```postgresql with=init.sql
SELECT department, department_avg
FROM (
    SELECT department, AVG(salary) AS department_avg
    FROM employees
    GROUP BY department
) AS dept_averages;
```

Expected output:

| department | department_avg |
| --- | --- |
| Engineering | 85000.00 |
| Marketing | 60000.00 |
| Sales | 61500.00 |

Leaving off `AS dept_averages` here would cause an error in most `databases`; a derived `table` without a name is not something the outer `query` can reference, even implicitly. This is one clear difference from a `WHERE` subquery, which never needs a name since it is only ever compared against, never selected from.

![A derived table needing an alias name before the outer query can use it](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_from_subquery_requires_alias.png)

## Joining a Derived Table to a Real Table

A `FROM` subquery can be `joined` to a normal `table` exactly like any other `table`, which is useful when a report needs both raw, `row`-level detail and a pre-computed summary side by side.

```postgresql with=init.sql
SELECT e.employee_name, e.salary, dept_averages.department_avg,
       e.salary - dept_averages.department_avg AS diff_from_dept_avg
FROM employees e
JOIN (
    SELECT department, AVG(salary) AS department_avg
    FROM employees
    GROUP BY department
) AS dept_averages ON e.department = dept_averages.department;
```

Expected output:

| employee_name | salary | department_avg | diff_from_dept_avg |
| --- | --- | --- | --- |
| Ananya Sharma | 95000.00 | 85000.00 | 10000.00 |
| Rajat Bhatia | 78000.00 | 85000.00 | -7000.00 |
| Meghna Iyer | 82000.00 | 85000.00 | -3000.00 |
| Sameer Khan | 65000.00 | 61500.00 | 3500.00 |
| Pooja Reddy | 58000.00 | 61500.00 | -3500.00 |
| Vikas Malhotra | 60000.00 | 60000.00 | 0.00 |

Here, `dept_averages` is `joined` to `employees` on the shared `department` `column`, letting every individual employee `row` see their own department's average sitting right next to their own salary, and a computed `column` shows exactly how far above or below that average each person falls:

- Ananya Sharma earns above her department's average.
- Rajat Bhatia and Meghna Iyer both earn below it.

## Subqueries in FROM at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rule</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Must be aliased</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The outer query needs a name to reference the derived table</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be <code>joined</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behaves like any other table once named</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Runs before the outer query</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The database computes it first, then treats the result as fixed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Common use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pre-aggregating data before filtering or <code>joining</code> on the aggregate</td>
    </tr>
  </tbody>
</table>

## Your Turn

Kabir wants to find the single department with the highest average salary, showing just its name and that average. Write a `query` using a `FROM` subquery against `employees` above, ordering the derived `table`'s results and keeping only the top `row`.

```postgresql with=init.sql
-- Write your query below
```

If your `query` wraps `SELECT department, AVG(salary) AS department_avg FROM employees GROUP BY department` as a derived `table`, then applies `ORDER BY department_avg DESC LIMIT 1` on the outer `query`, it returns Engineering as the top-paying department.


Expected output:

| department | department_avg |
| --- | --- |
| Engineering | 85000.00 |

## Conclusion

A subquery in `FROM`, or derived `table`, lets a `query` treat an intermediate result, especially a grouped or aggregated one, as if it were a real `table`, complete with the ability to filter, `join`, or select from it further.

Kabir can now compare department averages against a company average and see exactly how each employee sits relative to their department's norm, So far, every subquery has run independently of the outer `query`'s current `row`; the next lesson introduces a subquery that depends on it directly.
