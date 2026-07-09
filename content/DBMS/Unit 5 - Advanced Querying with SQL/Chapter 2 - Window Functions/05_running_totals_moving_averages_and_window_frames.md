## Introduction

The running total from earlier in this chapter, built with `SUM(amount) OVER (PARTITION BY salesperson ORDER BY sale_date)`, quietly relied on a default behavior Leela never had to name explicitly: it summed every row from the start of the partition up through the current row. That default is not the only option. The sales director's newest request needs a genuinely different range, a 3-month moving average, where each month's value is the average of itself and the two months before it, not the average of everything since the beginning. Getting this right means controlling the **window frame** directly, the exact slice of rows a `window function` looks at for each calculation.

## The Default Frame Behind a Running Total

The `monthly_sales` table tracks one row per salesperson per month.

```postgresql file=monthly_sales.sql
CREATE TABLE monthly_sales (
    salesperson TEXT,
    sale_month DATE,
    total_amount NUMERIC(10, 2)
);

INSERT INTO monthly_sales (salesperson, sale_month, total_amount) VALUES
('Nikhil Rao', '2025-01-01', 18000.00),
('Nikhil Rao', '2025-02-01', 20000.00),
('Nikhil Rao', '2025-03-01', 22000.00),
('Nikhil Rao', '2025-04-01', 25500.00),
('Nikhil Rao', '2025-05-01', 21000.00),
('Nikhil Rao', '2025-06-01', 29700.00);
```

```postgresql with=monthly_sales.sql
SELECT sale_month, total_amount,
       SUM(total_amount) OVER (ORDER BY sale_month) AS running_total
FROM monthly_sales
ORDER BY sale_month;
```

This is the same running-total pattern from earlier in the chapter, and its exact frame, though never written out, is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, meaning "everything from the very first row in the window up to and including the current one." That default frame is what makes a plain `ORDER BY` inside `OVER` produce a cumulative total in the first place.

## Writing a Window Frame Explicitly

The same running total can be written out fully, naming the frame instead of relying on the default.

```postgresql with=monthly_sales.sql
SELECT sale_month, total_amount,
       SUM(total_amount) OVER (
           ORDER BY sale_month
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM monthly_sales
ORDER BY sale_month;
```

`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` names the frame directly: start from the first row available (`UNBOUNDED PRECEDING`) and end at the current row (`CURRENT ROW`). This produces an identical result to the shorthand version, but writing it explicitly is what makes it possible to change the frame to something other than the default.

## Building a Moving Average with a Custom Frame

A 3-month moving average needs a frame of exactly the current row plus the two rows before it, which `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` expresses directly.

```postgresql with=monthly_sales.sql
SELECT sale_month, total_amount,
       ROUND(AVG(total_amount) OVER (
           ORDER BY sale_month
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ), 2) AS moving_avg_3month
FROM monthly_sales
ORDER BY sale_month;
```

- January's moving average is just 18000.00, its own value, since only zero rows precede it.
- February's is the average of January and February, two rows.
- From March onward, every row's moving average is built from exactly three months: itself and the two immediately before it, sliding forward one month at a time as `sale_month` increases, which is exactly the smoothing effect a moving average is meant to produce.

## A Frame That Looks Both Backward and Forward

A frame does not have to be limited to rows before the current one; it can extend in both directions at once.

```postgresql with=monthly_sales.sql
SELECT sale_month, total_amount,
       ROUND(AVG(total_amount) OVER (
           ORDER BY sale_month
           ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
       ), 2) AS centered_avg
FROM monthly_sales
ORDER BY sale_month;
```

`ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING` centers the frame on the current row, including one row before and one row after, which is a common way to smooth out noisy data symmetrically rather than only looking backward.

## Window Frame Options at a Glance

| Frame clause | Meaning |
|---|---|
| `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` | From the start of the window to the current row (the default with `ORDER BY`) |
| `ROWS BETWEEN n PRECEDING AND CURRENT ROW` | Current row plus the n rows before it |
| `ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING` | Current row, one before, one after |
| `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` | The entire partition, same as no `ORDER BY` at all |

## Your Turn

Leela wants a 2-month moving total, the current month plus the one before it, for Nikhil's sales. Write a query against `monthly_sales` above using an explicit window frame to compute it.

```postgresql with=monthly_sales.sql
-- Write your query below
```

If your query uses `SUM(total_amount) OVER (ORDER BY sale_month ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS moving_total_2month`, February shows 38000.00, January plus February combined, and March shows 42000.00, February plus March.

## Conclusion

A window frame, written with `ROWS BETWEEN ... AND ...`, controls exactly which rows a `window function` considers for each calculation, and changing it turns the same `SUM` or `AVG` from a full running total into a fixed-size moving calculation or a centered average. Leela can now build the exact 3-month moving average the director asked for, with full control over how wide that window actually is. With individual rows ranked, compared, and smoothed, the last piece is combining ranking with filtering to find a top few rows within each group.
