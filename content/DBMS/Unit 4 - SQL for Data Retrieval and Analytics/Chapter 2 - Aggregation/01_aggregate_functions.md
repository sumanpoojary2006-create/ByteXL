## Introduction

Priya handles finance reporting for a small online bookstore, and every question she gets from the founders is about the whole business, not any single row:

- "How many orders did we get this month?"
- "What is our total revenue?"
- "What is the average order value?"
- "What was our biggest single sale?"

None of those questions can be answered by looking at one row of the `orders` table; each one requires looking at every row and boiling it down to a single number. SQL calls this **aggregation**, and it provides a small set of built-in `aggregate functions`, `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`, that do exactly this kind of summarizing.

## Counting Rows

The `orders` table holds one row per order placed on the bookstore's site.

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

```postgresql with=orders.sql
SELECT COUNT(*) AS total_orders
FROM orders;
```

`COUNT(*)` counts every row in the result set, regardless of what any column contains, and here it answers Priya's first question directly: the bookstore received 8 orders. `COUNT(column_name)` behaves slightly differently, counting only the rows where that specific column is not `NULL`, which matters once a table has optional fields.

## Totaling and Averaging a Column

Revenue and average order value both come from the same `amount` column, just combined differently.

```postgresql with=orders.sql
SELECT SUM(amount) AS total_revenue, AVG(amount) AS average_order_value
FROM orders;
```

`SUM` adds up every value in the specified column across all matching rows, giving Priya total revenue in one number. `AVG` divides that same sum by the count of rows automatically, giving the average order value without Priya having to calculate it by hand from the other two numbers. Both functions ignore `NULL` values in the column they are summarizing, rather than treating a `NULL` as zero.

## Finding the Smallest and Largest Values

Priya's last question, the biggest single sale, needs a function that looks at every value and keeps only the extreme.

```postgresql with=orders.sql
SELECT MIN(amount) AS smallest_order, MAX(amount) AS largest_order
FROM orders;
```

`MIN` returns the smallest value found in the column across all matching rows, and `MAX` returns the largest. Here, the smallest order is Aman Gupta's 175.00 children's book purchase, and the largest is Sonal Deshpande's 1450.00 non-fiction order. `MIN` and `MAX` work on dates and text too, not just numbers, so `MIN(order_date)` would return the earliest date in the table.

## Combining Several Aggregates in One Query

All five `aggregate functions` can appear together in a single `SELECT`, each one summarizing the same set of rows in its own way.

```postgresql with=orders.sql
SELECT COUNT(*) AS total_orders,
       SUM(amount) AS total_revenue,
       ROUND(AVG(amount), 2) AS average_order_value,
       MIN(amount) AS smallest_order,
       MAX(amount) AS largest_order
FROM orders;
```

This single query answers every question the founders originally asked, in one pass over the table, with `ROUND` from the previous chapter cleaning up the average to two decimal places. This is the shape a founder-facing summary dashboard query usually takes: a handful of `aggregate functions`, no `GROUP BY` yet, producing exactly one summary row for the whole table.

## Aggregate Functions at a Glance

| Function | Purpose | Ignores NULLs? |
|---|---|---|
| `COUNT(*)` | Number of rows | No, counts every row |
| `COUNT(column)` | Number of non-NULL values in a column | Yes |
| `SUM(column)` | Total of a numeric column | Yes |
| `AVG(column)` | Average of a numeric column | Yes |
| `MIN(column)` / `MAX(column)` | Smallest / largest value | Yes |

## Your Turn

The founders now want to know the total number of orders placed and the total revenue earned specifically from the "Fiction" category. Write a query against the `orders` table above that returns both numbers, aliased as `fiction_orders` and `fiction_revenue`.

```postgresql with=orders.sql
-- Write your query below
```

If your query filters with `WHERE category = 'Fiction'` before aggregating, it returns 3 orders and 1380.00 in revenue, since `WHERE` narrows the rows down first and the `aggregate functions` only ever see what survives that filter.

## Conclusion

`COUNT`, `SUM`, `AVG`, `MIN`, and `MAX` collapse an entire result set into single summary numbers, answering exactly the kind of whole-business questions raw rows cannot answer on their own. Priya now has order counts, revenue, average order value, and the smallest and largest sales, all from one small table. So far every aggregate has summarized the whole table at once; the next step is producing one summary per category instead of a single overall number.
