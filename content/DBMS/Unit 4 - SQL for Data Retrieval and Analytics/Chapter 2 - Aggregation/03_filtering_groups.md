## Introduction

Priya's category breakdown worked well, but the founders' next request exposed a gap: "just show me customers who have spent over 1000 total, I don't need to see anyone below that." Priya's first instinct was to reach for `WHERE`, the filter she already knew, and add `WHERE SUM(amount) > 1000` to her grouped query. It failed immediately with an error about `aggregate functions` not being allowed there. The reason is about timing: `WHERE` filters individual rows before grouping happens, but Priya's condition depends on a sum that only exists after grouping happens. SQL has a separate clause for exactly this situation, **`HAVING`**, which filters groups after they have already been summarized.

## Why WHERE Cannot Filter on an Aggregate

The `orders` table is the same one used for grouping.

```postgresql file=orders.sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    category TEXT,
    amount NUMERIC(10, 2),
    order_date DATE
);

INSERT INTO orders (order_id, customer_name, category, amount, order_date) VALUES
(1, 'Ishita Rao', 'Fiction', 450.00, '2025-04-02'),
(2, 'Vivek Menon', 'Non-Fiction', 899.00, '2025-04-03'),
(3, 'Ishita Rao', 'Fiction', 320.00, '2025-04-05'),
(4, 'Aman Gupta', 'Children', 210.00, '2025-04-06'),
(5, 'Sonal Deshpande', 'Non-Fiction', 1450.00, '2025-04-08'),
(6, 'Vivek Menon', 'Fiction', 610.00, '2025-04-10'),
(7, 'Aman Gupta', 'Children', 175.00, '2025-04-12'),
(8, 'Ishita Rao', 'Non-Fiction', 990.00, '2025-04-14');
```

A query like `SELECT customer_name, SUM(amount) FROM orders WHERE SUM(amount) > 1000 GROUP BY customer_name;` raises an error, because `WHERE` runs before `GROUP BY` ever forms groups, back when the database is still looking at individual rows, and no single row has a `SUM(amount)` value to compare. `WHERE` can only see columns that already exist on a row, such as `amount` or `category`, not a total that has not been computed yet.

## Filtering After Grouping with HAVING

`HAVING` runs after `GROUP BY` has already collapsed rows into groups and the `aggregate functions` have already produced their results, so it can filter directly on those aggregate values.

```postgresql with=orders.sql
SELECT customer_name, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_name
HAVING SUM(amount) > 1000;
```

This groups every order by `customer_name`, computes each customer's total, and only then discards the groups whose total does not exceed 1000:

| customer_name | total_spent | Survives `HAVING SUM(amount) > 1000`? |
|---|---|---|
| Ishita Rao | 1760.00 | Yes |
| Vivek Menon | 1509.00 | Yes |
| Sonal Deshpande | 1450.00 | Yes |
| Aman Gupta | 385.00 | No |

Ishita Rao, Vivek Menon, and Sonal Deshpande survive the filter; Aman Gupta, whose total falls under 1000, is dropped from the result entirely, group and all.

## Combining WHERE and HAVING in the Same Query

`WHERE` and `HAVING` are not interchangeable, but they work well together, since each one filters at a different stage. `WHERE` can narrow down the rows before grouping even happens, which is often cheaper than grouping everything first and discarding groups afterward.

```postgresql with=orders.sql
SELECT customer_name, SUM(amount) AS total_spent
FROM orders
WHERE category != 'Children'
GROUP BY customer_name
HAVING SUM(amount) > 500;
```

This query runs in three clean stages:

1. `WHERE category != 'Children'` removes Aman Gupta's two children's-book orders before any grouping starts, so his rows never even reach the grouping stage.
2. `GROUP BY` then forms totals from what remains.
3. `HAVING SUM(amount) > 500` discards any customer whose remaining total does not clear 500.

The two clauses divide the work cleanly: `WHERE` picks which rows count, `HAVING` picks which resulting groups are worth keeping.

## Filtering on Count Instead of Sum

`HAVING` works with any `aggregate function`, not just `SUM`. A common use is filtering on how many rows landed in a group.

```postgresql with=orders.sql
SELECT customer_name, COUNT(*) AS orders_placed
FROM orders
GROUP BY customer_name
HAVING COUNT(*) >= 3;
```

This surfaces only the customers who placed 3 or more orders, which is a different, and for a loyalty program, often more useful, cut of the same data than filtering on total spend.

## WHERE vs. HAVING at a Glance

| Clause | Filters | Runs |
|---|---|---|
| `WHERE` | Individual rows | Before `GROUP BY` |
| `HAVING` | Groups, using aggregate results | After `GROUP BY` |

## Your Turn

The founders want to see only the product categories that generated less than 1000 in total revenue, so the team can decide whether to keep stocking them. Write a query against the `orders` table above that returns `category` and `total_revenue`, showing only categories under that threshold.

```postgresql with=orders.sql
-- Write your query below
```

If your query groups by `category` with `SUM(amount) AS total_revenue` and filters with `HAVING SUM(amount) < 1000`, only the Children's category appears, with a combined total of 385.00.

## Conclusion

`HAVING` fills the exact gap `WHERE` cannot: filtering on values that only exist after grouping and aggregation have already run. Used together, `WHERE` trims rows before grouping and `HAVING` trims groups after, giving Priya precise control over both stages of a report. With grouping, aggregating, and filtering groups all in hand, the next step is seeing how these pieces sit relative to sorting, row-level filtering, and `joins` in a single, more complete query.
