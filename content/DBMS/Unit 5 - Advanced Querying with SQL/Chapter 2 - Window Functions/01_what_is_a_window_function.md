## Introduction

Leela tracks performance for a small sales team, and the `sales` table holds one row per sale, with the salesperson's name and the amount. `GROUP BY` and `SUM` can easily tell her each salesperson's total, but the moment she groups, she loses the individual sale rows, since grouping collapses many rows into one summary row per group. What Leela actually wants is both at once: every individual sale, shown next to that salesperson's running total, without collapsing anything away. This is precisely the gap a **`window function`** fills: it calculates something across a group of related rows, the way an aggregate does, but returns a value for every original row instead of collapsing them.

## The Problem GROUP BY Cannot Solve Alone

The `sales` table records individual sales made by three team members.

```postgresql file=sales.sql
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    salesperson TEXT,
    region TEXT,
    amount NUMERIC(10, 2),
    sale_date DATE
);

INSERT INTO sales (sale_id, salesperson, region, amount, sale_date) VALUES
(1, 'Nikhil Rao', 'North', 12000.00, '2025-06-01'),
(2, 'Nikhil Rao', 'North', 8500.00, '2025-06-05'),
(3, 'Sana Fatima', 'South', 15000.00, '2025-06-02'),
(4, 'Nikhil Rao', 'North', 9200.00, '2025-06-10'),
(5, 'Sana Fatima', 'South', 6000.00, '2025-06-11'),
(6, 'Tarun Bakshi', 'East', 11000.00, '2025-06-03');
```

```postgresql with=sales.sql
SELECT salesperson, SUM(amount) AS total_sales
FROM sales
GROUP BY salesperson;
```

This gives Leela three rows, one total per salesperson, but the individual sales that made up each total are gone from the result. There is no way to see, in this same output, that Nikhil's 8500.00 sale on June 5 contributed to a running total of 20500.00 at that point.

## Getting Both the Row and an Aggregate Together

A `window function` is written using an aggregate function followed by `OVER (...)`, and it does not collapse rows the way `GROUP BY` does.

```postgresql with=sales.sql
SELECT salesperson, sale_id, amount,
       SUM(amount) OVER (PARTITION BY salesperson) AS salesperson_total
FROM sales;
```

Every one of the 6 original sale rows is still present in the output, but each one now carries an extra column, `salesperson_total`, showing that salesperson's overall total, repeated on every one of their rows:

| salesperson | sale_id | amount | salesperson_total |
|---|---|---|---|
| Nikhil Rao | 1 | 12000.00 | 29700.00 |
| Nikhil Rao | 2 | 8500.00 | 29700.00 |
| Nikhil Rao | 4 | 9200.00 | 29700.00 |
| Sana Fatima | 3 | 15000.00 | 21000.00 |
| Sana Fatima | 5 | 6000.00 | 21000.00 |

Nikhil's three rows all show 29700.00, his total across all three sales, sitting right next to each individual sale amount. The `SUM` here works exactly like the `aggregate function` it already is; the difference is entirely in `OVER (...)`, which tells the database to compute the aggregate across a related group of rows without collapsing the result down to one row per group.

## What OVER Actually Does

`OVER (...)` defines the "window," the set of rows the calculation should look across, for each individual row's computation. `PARTITION BY salesperson` inside it says "group the window by salesperson," which is conceptually similar to `GROUP BY`, with one key difference:

- `GROUP BY` controls how many rows appear in the final result, collapsing each group into one row.
- `PARTITION BY` only controls which rows are included in each calculation, leaving every original row in place.

```postgresql with=sales.sql
SELECT salesperson, sale_id, amount,
       SUM(amount) OVER () AS company_total
FROM sales;
```

Leaving the parentheses after `OVER` completely empty means the window is the entire result set, with no partitioning at all, so every row shows the same company-wide total, 61700.00, alongside its own individual sale amount. This is the simplest possible window: one big window covering everything.

## Window Functions Run After Grouping and Filtering

A `window function` can be combined with `WHERE`, and it always operates on whatever rows survive filtering, computed after `WHERE` has already run but conceptually alongside the final `SELECT`.

```postgresql with=sales.sql
SELECT salesperson, sale_id, amount,
       SUM(amount) OVER (PARTITION BY salesperson) AS salesperson_total
FROM sales
WHERE region != 'East';
```

Tarun Bakshi's East-region row is filtered out by `WHERE` before the `window function` ever runs, so it never factors into anyone's partitioned total, and it does not appear in the output at all. The window calculation only ever sees the rows that make it past filtering, same as any other part of the `SELECT` list.

## Window Functions vs. GROUP BY at a Glance

| | `GROUP BY` with aggregate | Window function with `OVER` |
|---|---|---|
| Rows in the result | One per group | One per original row |
| Individual row detail | Lost | Preserved |
| Aggregate value | One per group | Repeated across every row in that group |

## Your Turn

Leela wants to see every sale alongside the total sales for that sale's region, without losing any individual sale rows. Write a query against the `sales` table above using a `window function` partitioned by `region`.

```postgresql with=sales.sql
-- Write your query below
```

If your query is `SELECT salesperson, region, amount, SUM(amount) OVER (PARTITION BY region) AS region_total FROM sales;`, all 6 rows remain, and every South-region row shows 21000.00 as its region total, Sana's two sales combined.

## Conclusion

A `window function` computes an aggregate-style value across a related set of rows, defined by `OVER (...)`, without collapsing those rows into a single summary row the way `GROUP BY` does, giving Leela both individual detail and group-level context in the same result. The examples so far have only partitioned a window; the next lesson looks at ordering rows within a window too, which unlocks running totals, rankings, and row-to-row comparisons.
