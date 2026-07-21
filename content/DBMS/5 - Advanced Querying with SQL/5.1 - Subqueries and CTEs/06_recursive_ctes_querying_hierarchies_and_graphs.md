## Introduction

Kabir's `employees` `table` has a `manager_id` `column`, and a self `join` can pair each employee with their direct manager, one level up. But the company's actual org chart runs deeper than one level: an intern reports to a team lead, who reports to a director, who reports to the CEO.

A self `join` can only ever reach exactly one level up per `join` written, so answering "list every person above this employee, all the way to the top, however many levels that takes" would need a different self `join` for every possible depth, and depth is not something Kabir can know in advance.

A **`recursive CTE`** solves this by repeating its own logic against its own growing result, one level at a time, until nothing new is left to add.

**Definition:** A `recursive CTE` repeats its own logic against a growing result set until no new `rows` appear, which is exactly the tool needed for hierarchies and graphs whose depth is not known in advance, whether that means walking up an org chart to find every manager above a person or walking down to find every report beneath one.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_recursive_ctes_querying_hierarchies_and_graphs.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Kabir's employees table has a managerid column, and a self join can pair each employee with their direct manager, one level up. But the company's actual org chart runs deeper than one level: an intern reports to a team lead, who reports to a director, who.

ON-IMAGE TEXT: show a short bold title "Recursive Ctes Querying Hierarchies And Graphs" plus only these few labels, large and legible: Table, Column, Join. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for recursive ctes querying hierarchies and graphs](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_intro_recursive_ctes_querying_hierarchies_and_graphs_clean_e3c87a9b.png)

## The Shape of the Hierarchy

The `employees` `table` now includes a few more reporting levels to make the hierarchy worth walking.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `employees`

| employee_id | employee_name | manager_id |
| --- | --- | --- |
| 1 | Ananya Sharma | NULL |
| 2 | Rajat Bhatia | 1 |
| 3 | Meghna Iyer | 1 |
| 4 | Karan Oberoi | 2 |
| 5 | Divya Nambiar | 2 |
| 6 | Farhan Sheikh | 4 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
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

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

Ananya sits at the top with no manager, Rajat and Meghna report to her, Karan and Divya report to Rajat, and Farhan reports to Karan, four levels deep in one branch. A single self `join` could find Farhan's direct manager, Karan, but not Karan's manager, Rajat, in the same `query` without another `join` added on top, and not Ananya above that without yet another.

## Writing a Recursive CTE

A `recursive CTE` has two parts `joined` by `UNION ALL`: a base case that starts the recursion, and a recursive case that repeats, each time building on the previous round's result.

```postgresql with=init.sql
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

Expected output:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">employee_name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">level</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Farhan Sheikh</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Karan Oberoi</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rajat Bhatia</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ananya Sharma</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
    </tr>
  </tbody>
</table>

The `database` repeats the recursive case automatically, each round adding one more level up the chain, and stops on its own the moment a round produces no new `rows`, which happens once it tries to find a manager for Ananya and finds none.

![A recursive CTE walking upward through a manager chain one level at a time](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_recursive_cte_walks_up_manager_chain.png)

## Why RECURSIVE and UNION ALL Are Both Required

Two pieces of syntax are both required, for different reasons:

- `WITH RECURSIVE` is the keyword that tells the `database` this CTE is allowed to reference itself; a plain `WITH` would reject a `query` that tries to select from its own name inside its own definition.
- `UNION ALL` is required rather than a plain `JOIN`, because the recursive case needs to combine the base case's starting `row` with every additional `row` the recursive step produces, round after round, exactly the stacking behavior `UNION ALL` was built for.

## Reversing the Direction: Finding Everyone Below a Person

The same recursive structure works in the opposite direction, finding every employee under a given manager instead of every manager above a given employee, just by flipping which side of the `join` condition matches which `column`.

```postgresql with=init.sql
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

Expected output:

| employee_name | level |
| --- | --- |
| Ananya Sharma | 1 |
| Meghna Iyer | 2 |
| Rajat Bhatia | 2 |
| Divya Nambiar | 3 |
| Karan Oberoi | 3 |
| Farhan Sheikh | 4 |

Starting from Ananya at level 1, the recursive case now matches `e.manager_id = team_below.employee_id`, finding everyone who reports to whoever was just added, which walks down the org chart instead of up it. This returns all six employees, since every person in the `table` eventually traces back to Ananya, with `level` showing how many steps down from her each one sits.

![A recursive CTE walking downward through the team tree from a manager](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_recursive_cte_walks_down_team_tree.png)

## Recursive CTEs at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Part</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>WITH RECURSIVE name AS (...)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Declares a CTE allowed to reference itself</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Base case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The starting row or rows, before <code>UNION ALL</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recursive case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>Joins</code> the table back to the CTE&#x27;s own name, run repeatedly</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stops when</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A round produces zero new rows</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Typical use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Org charts, category trees, bill-of-materials, any graph of parent-child relationships</td>
    </tr>
  </tbody>
</table>

## Your Turn

Find every employee who reports, directly or indirectly, to Rajat Bhatia, including how many levels below him each one sits. Write a `recursive CTE` against the `employees` `table` above, starting from Rajat.

```postgresql with=init.sql
-- Write your query below
```

If your `query` bases the recursion on `WHERE employee_id = 2` and recurses with `e.manager_id = team_below.employee_id`, it returns Rajat himself at level 1, Karan and Divya at level 2, and Farhan at level 3, correctly walking down every branch under Rajat regardless of depth.


Expected output:

| employee_name | level |
| --- | --- |
| Rajat Bhatia | 1 |
| Karan Oberoi | 2 |
| Divya Nambiar | 2 |
| Farhan Sheikh | 3 |

## Conclusion

A `recursive CTE` repeats its own logic against a growing result set until no new `rows` appear, which is exactly the tool needed for hierarchies and graphs whose depth is not known in advance, whether that means walking up an org chart to find every manager above a person or walking down to find every report beneath one.

Kabir can now answer any reporting-chain question regardless of how many levels deep the company's structure goes. With subqueries and CTEs covered from every angle, the next chapter turns to a different kind of advanced `query`: calculations that look across a set of `rows` without collapsing them into a single group.
