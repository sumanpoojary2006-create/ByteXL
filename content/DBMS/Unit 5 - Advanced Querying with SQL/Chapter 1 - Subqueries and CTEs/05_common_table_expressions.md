## Introduction

Kabir's department-average report from the `FROM` subquery lesson worked correctly, but re-reading it a week later, he found himself squinting at nested parentheses to figure out which `SELECT` belonged to which part of the query. As soon as a query needs two or three layered steps, subqueries buried inside `FROM` or `WHERE` start to read inside-out, with the first thing the eye lands on being the deepest, least important detail. SQL offers a cleaner way to write exactly the same logic: a **`Common Table Expression`**, written with a `WITH` clause, which names an intermediate result up front and lets the rest of the query read top to bottom in the order the logic actually happens.

## Rewriting a Subquery as a CTE

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

Here is the derived-table version from an earlier lesson, for comparison.

```postgresql with=employees.sql
SELECT department, department_avg
FROM (
    SELECT department, AVG(salary) AS department_avg
    FROM employees
    GROUP BY department
) AS dept_averages
WHERE department_avg > (SELECT AVG(salary) FROM employees);
```

And here is the same logic rewritten with a CTE.

```postgresql with=employees.sql
WITH dept_averages AS (
    SELECT department, AVG(salary) AS department_avg
    FROM employees
    GROUP BY department
)
SELECT department, department_avg
FROM dept_averages
WHERE department_avg > (SELECT AVG(salary) FROM employees);
```

`WITH dept_averages AS (...)` names the inner query before the main query even begins, and the main query afterward simply reads `FROM dept_averages`, exactly as if it were a real table. The two versions produce an identical result, Engineering as the only department above the company average, but the CTE version reads in the order a person would naturally explain it out loud: "first compute department averages, then find the ones above the company average."

## Chaining Several CTEs Together

A single `WITH` clause can define more than one CTE, separated by commas, and later CTEs are allowed to reference earlier ones, building up a multi-step calculation one readable piece at a time.

```postgresql with=employees.sql
WITH dept_averages AS (
    SELECT department, AVG(salary) AS department_avg
    FROM employees
    GROUP BY department
),
company_average AS (
    SELECT AVG(salary) AS company_avg FROM employees
)
SELECT dept_averages.department, dept_averages.department_avg, company_average.company_avg
FROM dept_averages, company_average
WHERE dept_averages.department_avg > company_average.company_avg;
```

`dept_averages` and `company_average` are each defined once, given clear names, and then both referenced in the final `SELECT`, which lists them side by side and compares their columns directly. Naming each step this way pays off in two ways:

- It makes it far easier to check each piece in isolation, since the whole first CTE can be run on its own, just by selecting from it directly, before it is ever plugged into the larger query.
- It documents what each intermediate result actually represents, for anyone reading the query later.

## Why CTEs Are Often Preferred Over Nested Subqueries

Both derived tables and CTEs are ultimately handled by the database in comparable ways, and neither is inherently faster than the other in most modern databases. The real difference is readability and maintainability: a CTE gives an intermediate result a name that documents what it represents, and it keeps deeply nested queries from turning into a wall of parentheses that has to be read from the inside out. For any query with more than one layer of subquery, reaching for a CTE instead is usually the better habit to build.

## A CTE Can Also Simplify a WHERE Subquery

CTEs are not limited to replacing `FROM` subqueries; any subquery, including the correlated and list-based ones from earlier lessons, can be pulled out into a named CTE if doing so makes the query easier to follow.

```postgresql with=employees.sql
WITH high_earners AS (
    SELECT employee_id, employee_name, salary
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
)
SELECT employee_name, salary
FROM high_earners
ORDER BY salary DESC;
```

This is a small example, but the pattern scales: as soon as a `WHERE` subquery's own logic becomes complex enough to deserve a name, wrapping it in a CTE keeps the final query focused on what happens with the result, not how that result was derived.

## CTEs at a Glance

| Feature | Detail |
|---|---|
| Syntax | `WITH name AS (subquery) SELECT ... FROM name` |
| Multiple CTEs | Comma-separated, later ones can reference earlier ones |
| Scope | Only visible within the single statement that defines them |
| Main benefit | Readability: names each step, avoids deeply nested parentheses |

## Your Turn

Rewrite the `correlated subquery` from the previous lesson, finding employees whose salary exceeds their own department's average, as a CTE-based query instead of a `WHERE`-embedded subquery.

```postgresql with=employees.sql
-- Write your query below
```

One valid answer defines `WITH dept_averages AS (SELECT department, AVG(salary) AS department_avg FROM employees GROUP BY department)` and then `joins` `employees` to `dept_averages` on `department`, filtering with `WHERE employees.salary > dept_averages.department_avg`, returning Ananya Sharma and Meghna Iyer.

## Conclusion

A CTE, written with `WITH`, names an intermediate query result up front so the rest of a statement can read top to bottom instead of inside out, and several CTEs can be chained together, each one building on the last, without losing clarity as the logic grows more layered. Kabir's department-average report is now something a colleague can read and understand in one pass. Every CTE so far has referenced only tables or earlier CTEs; the next lesson introduces a CTE that is allowed to reference itself.
