## Introduction

Leela's next report tracks month-over-month growth: for each salesperson's monthly total, how much did it change compared to the previous month? Answering this means comparing a row to a different row, specifically, whichever row comes immediately before it once the data is ordered by month. A plain `SELECT` has no built-in way to reach into a neighboring row like that. SQL's **offset functions**, `LAG` and `LEAD`, are `window functions` purpose-built for exactly this: pulling a value from a row a fixed number of positions before or after the current one, within an ordered window.

## Looking Back at the Previous Row with LAG

The `monthly_sales` table holds one row per salesperson per month.

```postgresql file=monthly_sales.sql
CREATE TABLE monthly_sales (
    salesperson TEXT,
    sale_month DATE,
    total_amount NUMERIC(10, 2)
);

INSERT INTO monthly_sales (salesperson, sale_month, total_amount) VALUES
('Nikhil Rao', '2025-03-01', 22000.00),
('Nikhil Rao', '2025-04-01', 25500.00),
('Nikhil Rao', '2025-05-01', 21000.00),
('Nikhil Rao', '2025-06-01', 29700.00),
('Sana Fatima', '2025-05-01', 18000.00),
('Sana Fatima', '2025-06-01', 21000.00);
```

```postgresql with=monthly_sales.sql
SELECT salesperson, sale_month, total_amount,
       LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) AS previous_month
FROM monthly_sales
ORDER BY salesperson, sale_month;
```

`LAG(total_amount)` reaches back one row within each salesperson's partition, ordered by month, and returns that prior row's `total_amount`:

| salesperson | sale_month | total_amount | previous_month |
|---|---|---|---|
| Nikhil Rao | 2025-03-01 | 22000.00 | `NULL` |
| Nikhil Rao | 2025-04-01 | 25500.00 | 22000.00 |
| Nikhil Rao | 2025-05-01 | 21000.00 | 25500.00 |
| Nikhil Rao | 2025-06-01 | 29700.00 | 21000.00 |

- Nikhil's April row shows 22000.00 as its `previous_month`, exactly March's total.
- His March row, having nothing before it in the partition, shows `NULL`, since there is no earlier row for `LAG` to reach.

## Calculating Change Using LAG

With the previous month's value sitting in the same row, calculating growth is now a plain subtraction.

```postgresql with=monthly_sales.sql
SELECT salesperson, sale_month, total_amount,
       total_amount - LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) AS change_from_last_month
FROM monthly_sales
ORDER BY salesperson, sale_month;
```

Nikhil's April change is 3500.00, an increase, and his May change is -4500.00, a drop, computed directly from two values that now live on the same logical row thanks to `LAG`. Before `window functions`, this same calculation would have needed a self `join` matching each row to "the row for the same salesperson, one month earlier," a noticeably more complex query for the same result.

## Looking Ahead to the Next Row with LEAD

`LEAD` is the mirror of `LAG`, reaching forward to a later row instead of an earlier one.

```postgresql with=monthly_sales.sql
SELECT salesperson, sale_month, total_amount,
       LEAD(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) AS next_month
FROM monthly_sales
ORDER BY salesperson, sale_month;
```

Nikhil's March row now shows 25500.00 as `next_month`, April's total, and his last row, June, shows `NULL`, since there is no later row in his partition for `LEAD` to reach forward into. `LEAD` is useful for questions phrased the other way around, such as "what did this salesperson do right after this particular month."

## Reaching More Than One Row Away

Both `LAG` and `LEAD` accept two optional extra arguments:

- A second argument specifying how many rows to look back or forward, defaulting to 1 when left out.
- A third argument specifying what to return when there is no such row, instead of `NULL`.

```postgresql with=monthly_sales.sql
SELECT salesperson, sale_month, total_amount,
       LAG(total_amount, 2, 0) OVER (PARTITION BY salesperson ORDER BY sale_month) AS two_months_ago
FROM monthly_sales
ORDER BY salesperson, sale_month;
```

`LAG(total_amount, 2, 0)` reaches back two rows instead of one, and supplies 0 instead of `NULL` whenever there is no row that far back, which is useful when a downstream calculation needs a real number rather than a `NULL` to work with.

## LAG and LEAD at a Glance

| Function | Direction | Default offset | Default fallback |
|---|---|---|---|
| `LAG(col)` | Backward, to an earlier row | 1 row | `NULL` |
| `LEAD(col)` | Forward, to a later row | 1 row | `NULL` |
| `LAG(col, n)` / `LEAD(col, n)` | n rows in that direction | n | `NULL` |
| `LAG(col, n, default)` / `LEAD(col, n, default)` | n rows, with a fallback value | n | `default` |

## Your Turn

Leela wants to flag any month where a salesperson's total dropped compared to the previous month. Write a query against `monthly_sales` above that shows `salesperson`, `sale_month`, `total_amount`, and a `trend` column reading either "up" or "down" based on `LAG`.

```postgresql with=monthly_sales.sql
-- Write your query below
```

One valid answer wraps the `LAG` comparison in a `CASE` expression: `CASE WHEN total_amount < LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) THEN 'down' ELSE 'up' END AS trend`, which correctly labels Nikhil's May row as "down" and every other row as "up," including the first row of each salesperson, which has nothing to compare against and defaults to "up" through the `ELSE` branch.

## Conclusion

`LAG` and `LEAD` pull a value from a neighboring row, before or after the current one within an ordered window, turning row-to-row comparisons like month-over-month change into a straightforward calculation on a single row instead of a self `join` across two. Leela can now show growth, decline, and trend directly in her monthly report. Comparing to one neighboring row is useful, but some calculations need to look across a whole range of surrounding rows at once, which is where window frames come in.
