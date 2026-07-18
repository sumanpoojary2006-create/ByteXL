# Mini Project 4: Employee Hierarchy and Leaderboard

## Background

Two questions come up constantly in a company's database: "who reports to whom, all the way up the chain?" and "who is our top performer, and how does this month compare to last month?" The first needs a query that can walk a self-referencing hierarchy of unknown depth. The second needs window functions that can rank and compare rows without collapsing them the way `GROUP BY` does. This project builds both, using subqueries, CTEs, recursive CTEs, and window functions on a small sales team dataset.

## What You Will Build

A set of SQL queries over an `employees` and `sales` schema that surfaces above-average performers, a full management hierarchy, and a ranked sales leaderboard with month-over-month comparisons.

## Dataset

Before writing project queries, inspect the starting data so every task has a visible source to reason from.

### Starting `employees` rows

| full_name | manager_id | department |
| --- | --- | --- |
| Meera Iyer | NULL | Leadership |
| Naveen Kumar | 1 | Sales |
| Asha Gupta | 1 | Sales |
| Rohit Verma | 2 | Sales |
| Kiran Das | 2 | Sales |
| Fatima Sheikh | 3 | Sales |

### Starting `sales` rows

| employee_id | sale_month | amount |
| --- | --- | --- |
| 4 | 2026-01-01 | 40000 |
| 4 | 2026-02-01 | 55000 |
| 5 | 2026-01-01 | 30000 |
| 5 | 2026-02-01 | 30000 |
| 6 | 2026-01-01 | 60000 |
| 6 | 2026-02-01 | 20000 |

Use two files in OneCompiler. Keep all `CREATE TABLE` and `INSERT` statements in `init.sql`; keep only the current task query in the active SQL file. The `with=init.sql` attribute connects the two files.

```postgresql file=init.sql
CREATE TABLE employees (
    employee_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name    TEXT NOT NULL,
    manager_id   INTEGER REFERENCES employees(employee_id),
    department   TEXT NOT NULL
);

CREATE TABLE sales (
    sale_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    employee_id  INTEGER NOT NULL REFERENCES employees(employee_id),
    sale_month   DATE NOT NULL,
    amount       NUMERIC(10, 2) NOT NULL
);

INSERT INTO employees (full_name, manager_id, department) VALUES
('Meera Iyer', NULL, 'Leadership'),
('Naveen Kumar', 1, 'Sales'),
('Asha Gupta', 1, 'Sales'),
('Rohit Verma', 2, 'Sales'),
('Kiran Das', 2, 'Sales'),
('Fatima Sheikh', 3, 'Sales');

INSERT INTO sales (employee_id, sale_month, amount) VALUES
(4, '2026-01-01', 40000), (4, '2026-02-01', 55000),
(5, '2026-01-01', 30000), (5, '2026-02-01', 30000),
(6, '2026-01-01', 60000), (6, '2026-02-01', 20000);
```

### Confirm the Setup

Run this in the active SQL file before starting the tasks. It confirms that `init.sql` loaded the expected number of rows.

```postgresql with=init.sql
SELECT COUNT(*) AS loaded_rows FROM employees;
```

Expected output:

| loaded_rows |
| --- |
| 6 |

Meera is the CEO. Naveen and Asha report to her. Rohit and Kiran report to Naveen. Fatima reports to Asha.

## Tasks

### Task 1: Above-Average Performers

1. Write a query using a subquery in `FROM` that computes each salesperson's total sales across both months.
2. Using that same logic as a correlated subquery in `WHERE`, find every salesperson whose total sales exceed the company-wide average total per person.
3. State, in a comment, which two employees this returns and why the third does not qualify.

### Task 2: The Full Reporting Chain

1. Write a plain CTE that first computes each employee's total sales, then joins it back to `employees` to show name, department, and total side by side, purely to keep the main query readable.
2. Write a recursive CTE that starts from Meera (the row with `manager_id IS NULL`) and walks down the `manager_id` chain, producing every employee along with their depth level (Meera at level 1, Naveen and Asha at level 2, and so on).

   ```postgresql with=init.sql
   WITH RECURSIVE org_chart AS (
       SELECT employee_id, full_name, manager_id, 1 AS level
       FROM employees
       WHERE manager_id IS NULL

       UNION ALL

       SELECT e.employee_id, e.full_name, e.manager_id, oc.level + 1
       FROM employees e
       JOIN org_chart oc ON e.manager_id = oc.employee_id
   )
   SELECT * FROM org_chart ORDER BY level, full_name;
   ```

Expected result: the query returns the complete six-person hierarchy, with Meera at level 1, Naveen and Asha at level 2, and Rohit, Kiran, and Fatima at level 3.

### Task 3: The Leaderboard

1. Rank Sales-department employees by total sales (highest first) using `RANK() OVER (PARTITION BY department ORDER BY ...)`.
2. For each employee, use `LAG` to show their previous month's sales next to the current month, and compute the change between the two.
3. Compute each employee's running total of sales, ordered by month.
4. Using the ranking from step 1, return only the top 2 earners in the Sales department.

**Answer these questions after completing all tasks:**
- Rohit Verma's two months were 40000 and 55000; Fatima Sheikh's were 60000 and 20000. Their totals are 95000 and 80000. Does your `RANK()` in Task 3.1 put Rohit ahead of Fatima, and does this match what a simple `SUM` per employee would tell you on its own?
- Your recursive CTE in Task 2.2 starts from `manager_id IS NULL`. What would happen if two employees both had `manager_id IS NULL` (two independent CEOs)? Would the query still work, and what would change about the result?
- Task 3.2 uses `LAG` to compare a month to the one before it. For Kiran Das, both months were 30000. What does the computed "change" show for Kiran, and how is that different from Fatima Sheikh, whose sales dropped from 60000 to 20000?
