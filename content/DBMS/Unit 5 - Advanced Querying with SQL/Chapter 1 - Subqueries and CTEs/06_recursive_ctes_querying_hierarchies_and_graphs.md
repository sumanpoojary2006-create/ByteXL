## Introduction

Kabir's `employees` table has a `manager_id` column, and a self `join` can pair each employee with their direct manager, one level up. But the company's actual org chart runs deeper than one level: an intern reports to a team lead, who reports to a director, who reports to the CEO. A self `join` can only ever reach exactly one level up per `join` written, so answering "list every person above this employee, all the way to the top, however many levels that takes" would need a different self `join` for every possible depth, and depth is not something Kabir can know in advance. A **`recursive CTE`** solves this by repeating its own logic against its own growing result, one level at a time, until nothing new is left to add.

## The Shape of the Hierarchy

The `employees` table now includes a few more reporting levels to make the hierarchy worth walking.

```postgresql file=employees_hierarchy.sql
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    manager_id INTEGER
);

INSERT INTO employees (employee_id, employee_name, manager_id) VALUES
(1, 'Ananya Sharma', NULL),
(2, 'Rajat Bhatia', 1),
(3, 'Meghna Iyer', 1),
(4, 'Karan Oberoi', 2),
(5, 'Divya Nambiar', 2),
(6, 'Farhan Sheikh', 4);
```

Ananya sits at the top with no manager, Rajat and Meghna report to her, Karan and Divya report to Rajat, and Farhan reports to Karan, four levels deep in one branch. A single self `join` could find Farhan's direct manager, Karan, but not Karan's manager, Rajat, in the same query without another `join` added on top, and not Ananya above that without yet another.

## Writing a Recursive CTE

A `recursive CTE` has two parts `joined` by `UNION ALL`: a base case that starts the recursion, and a recursive case that repeats, each time building on the previous round's result.

```postgresql with=employees_hierarchy.sql
WITH RECURSIVE reporting_chain AS (
    SELECT employee_id, employee_name, manager_id, 1 AS level
    FROM employees
    WHERE employee_id = 6

    UNION ALL

    SELECT e.employee_id, e.employee_name, e.manager_id, reporting_chain.level + 1
    FROM employees e
    JOIN reporting_chain ON e.employee_id = reporting_chain.manager_id
)
SELECT employee_name, level
FROM reporting_chain
ORDER BY level;
```

The base case, `WHERE employee_id = 6`, starts with just Farhan Sheikh, at level 1. The recursive case then `joins` `employees` back to `reporting_chain` itself, `e.employee_id = reporting_chain.manager_id`, finding whoever manages the person just added, and that newly found manager becomes part of `reporting_chain` for the next round:

| employee_name | level |
|---|---|
| Farhan Sheikh | 1 |
| Karan Oberoi | 2 |
| Rajat Bhatia | 3 |
| Ananya Sharma | 4 |

The database repeats the recursive case automatically, each round adding one more level up the chain, and stops on its own the moment a round produces no new rows, which happens once it tries to find a manager for Ananya and finds none.

## Why RECURSIVE and UNION ALL Are Both Required

Two pieces of syntax are both required, for different reasons:

- `WITH RECURSIVE` is the keyword that tells the database this CTE is allowed to reference itself; a plain `WITH` would reject a query that tries to select from its own name inside its own definition.
- `UNION ALL` is required rather than a plain `JOIN`, because the recursive case needs to combine the base case's starting row with every additional row the recursive step produces, round after round, exactly the stacking behavior `UNION ALL` was built for.

## Reversing the Direction: Finding Everyone Below a Person

The same recursive structure works in the opposite direction, finding every employee under a given manager instead of every manager above a given employee, just by flipping which side of the `join` condition matches which column.

```postgresql with=employees_hierarchy.sql
WITH RECURSIVE team_below AS (
    SELECT employee_id, employee_name, manager_id, 1 AS level
    FROM employees
    WHERE employee_id = 1

    UNION ALL

    SELECT e.employee_id, e.employee_name, e.manager_id, team_below.level + 1
    FROM employees e
    JOIN team_below ON e.manager_id = team_below.employee_id
)
SELECT employee_name, level
FROM team_below
ORDER BY level;
```

Starting from Ananya at level 1, the recursive case now matches `e.manager_id = team_below.employee_id`, finding everyone who reports to whoever was just added, which walks down the org chart instead of up it. This returns all six employees, since every person in the table eventually traces back to Ananya, with `level` showing how many steps down from her each one sits.

## Recursive CTEs at a Glance

| Part | Purpose |
|---|---|
| `WITH RECURSIVE name AS (...)` | Declares a CTE allowed to reference itself |
| Base case | The starting row or rows, before `UNION ALL` |
| Recursive case | `Joins` the table back to the CTE's own name, run repeatedly |
| Stops when | A round produces zero new rows |
| Typical use | Org charts, category trees, bill-of-materials, any graph of parent-child relationships |

## Your Turn

Find every employee who reports, directly or indirectly, to Rajat Bhatia, including how many levels below him each one sits. Write a `recursive CTE` against the `employees` table above, starting from Rajat.

```postgresql with=employees_hierarchy.sql
-- Write your query below
```

If your query bases the recursion on `WHERE employee_id = 2` and recurses with `e.manager_id = team_below.employee_id`, it returns Rajat himself at level 1, Karan and Divya at level 2, and Farhan at level 3, correctly walking down every branch under Rajat regardless of depth.

## Conclusion

A `recursive CTE` repeats its own logic against a growing result set until no new rows appear, which is exactly the tool needed for hierarchies and graphs whose depth is not known in advance, whether that means walking up an org chart to find every manager above a person or walking down to find every report beneath one. Kabir can now answer any reporting-chain question regardless of how many levels deep the company's structure goes. With subqueries and CTEs covered from every angle, the next chapter turns to a different kind of advanced query: calculations that look across a set of rows without collapsing them into a single group.
