## Introduction

Kabir's next report needs a two-step calculation: first, find the average salary within each department, then find which departments pay above the overall company average. The first step is a grouped query. The second step needs to treat the result of that grouped query as if it were itself a table, filtering and comparing rows that do not exist anywhere in the original `employees` table, only in the summarized output. A subquery does not have to sit inside `WHERE` producing a single value or a list; it can also sit inside `FROM`, standing in for an entire table. This kind of subquery is often called a **derived table**.

## Treating a Query's Result as a Table

The `employees` table is the same one used throughout this chapter.

```postgresql file=employees.sql
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

```postgresql with=employees.sql
SELECT department, AVG(salary) AS department_avg
FROM employees
GROUP BY department;
```

This is the first step on its own: three rows, one average per department. Now that same query becomes the `FROM` clause of an outer query, wrapped in parentheses and given an alias.

```postgresql with=employees.sql
SELECT department, department_avg
FROM (
    SELECT department, AVG(salary) AS department_avg
    FROM employees
    GROUP BY department
) AS dept_averages
WHERE department_avg > (SELECT AVG(salary) FROM employees);
```

The subquery in `FROM`, aliased here as `dept_averages`, runs first and produces a small three-row result:

| department | department_avg |
|---|---|
| Engineering | 85000.00 |
| Sales | 61500.00 |
| Marketing | 60000.00 |

The outer query then treats `dept_averages` exactly like a real table, filtering its rows with a `WHERE` clause that compares `department_avg`, a column that only exists because the inner query computed it, against the company-wide average of 73000.00 from a second subquery. Engineering is the only department whose average clears the company-wide bar.

## Why a FROM Subquery Needs an Alias

Every subquery used in `FROM` must be given a name, since the outer query needs some way to refer to it, the same way any real table needs a name to be selected from.

```postgresql with=employees.sql
SELECT department, department_avg
FROM (
    SELECT department, AVG(salary) AS department_avg
    FROM employees
    GROUP BY department
) AS dept_averages;
```

Leaving off `AS dept_averages` here would cause an error in most databases; a derived table without a name is not something the outer query can reference, even implicitly. This is one clear difference from a `WHERE` subquery, which never needs a name since it is only ever compared against, never selected from.

## Joining a Derived Table to a Real Table

A `FROM` subquery can be `joined` to a normal table exactly like any other table, which is useful when a report needs both raw, row-level detail and a pre-computed summary side by side.

```postgresql with=employees.sql
SELECT e.employee_name, e.salary, dept_averages.department_avg,
       e.salary - dept_averages.department_avg AS diff_from_dept_avg
FROM employees e
JOIN (
    SELECT department, AVG(salary) AS department_avg
    FROM employees
    GROUP BY department
) AS dept_averages ON e.department = dept_averages.department;
```

Here, `dept_averages` is `joined` to `employees` on the shared `department` column, letting every individual employee row see their own department's average sitting right next to their own salary, and a computed column shows exactly how far above or below that average each person falls:

- Ananya Sharma earns above her department's average.
- Rajat Bhatia and Meghna Iyer both earn below it.

## Subqueries in FROM at a Glance

| Rule | Detail |
|---|---|
| Must be aliased | The outer query needs a name to reference the derived table |
| Can be `joined` | Behaves like any other table once named |
| Runs before the outer query | The database computes it first, then treats the result as fixed |
| Common use | Pre-aggregating data before filtering or `joining` on the aggregate |

## Your Turn

Kabir wants to find the single department with the highest average salary, showing just its name and that average. Write a query using a `FROM` subquery against `employees` above, ordering the derived table's results and keeping only the top row.

```postgresql with=employees.sql
-- Write your query below
```

If your query wraps `SELECT department, AVG(salary) AS department_avg FROM employees GROUP BY department` as a derived table, then applies `ORDER BY department_avg DESC LIMIT 1` on the outer query, it returns Engineering as the top-paying department.

## Conclusion

A subquery in `FROM`, or derived table, lets a query treat an intermediate result, especially a grouped or aggregated one, as if it were a real table, complete with the ability to filter, `join`, or select from it further. Kabir can now compare department averages against a company average and see exactly how each employee sits relative to their department's norm. So far, every subquery has run independently of the outer query's current row; the next lesson introduces a subquery that depends on it directly.
