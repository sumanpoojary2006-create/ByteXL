## Introduction

Priya's one-number summaries answered the founders' first round of questions, but the very next question was sharper: "which category earns us the most, Fiction, Non-Fiction, or Children's books?" A single `SUM(amount)` across the whole `orders` table cannot answer that, since it blends every category into one blurred total. What Priya actually needs is the table split into separate buckets, one per category, with the `aggregate functions` run separately inside each bucket. SQL's **`GROUP BY`** clause does exactly this: it partitions rows into groups before the `aggregate functions` ever run.

## Splitting Rows Into Groups

The `orders` table from `aggregate functions` is the starting point again.

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
SELECT category, SUM(amount) AS category_revenue
FROM orders
GROUP BY category;
```

`GROUP BY category` tells the database to gather all rows that share the same `category` value into one group before `SUM(amount)` runs, so instead of one grand total, Priya gets three totals, one per category:

| category | category_revenue |
|---|---|
| Fiction | 1380.00 |
| Non-Fiction | 3339.00 |
| Children | 385.00 |

Fiction, Non-Fiction, and Children's books each get their own row in the result, and the founders' question is answered directly: Non-Fiction earns the most.

## Why Every Selected Column Must Be Grouped or Aggregated

A common mistake when starting with `GROUP BY` is trying to select a column that is neither grouped on nor wrapped in an `aggregate function`.

```postgresql with=orders.sql
SELECT category, customer_name, SUM(amount) AS category_revenue
FROM orders
GROUP BY category;
```

This query fails, because once rows are collapsed into a `category` group, `customer_name` no longer refers to a single value within that group; the Fiction group alone contains orders from both Ishita Rao and Vivek Menon, so the database has no single `customer_name` to return for that row.

The rule that follows from this: every column in the `SELECT` list must do one of two things:

1. Appear in `GROUP BY`.
2. Be wrapped in an `aggregate function` like `SUM`, `COUNT`, `MIN`, or `MAX`.

Either way, the database always knows exactly one value to produce per group.

## Grouping by More Than One Column

Priya can group by more than one column at a time, which produces one group for every distinct combination of the grouped values.

```postgresql with=orders.sql
SELECT customer_name, category, COUNT(*) AS orders_placed, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_name, category;
```

Each row in the result now represents one customer and one category together, so Ishita Rao's Fiction orders are summarized separately from her Non-Fiction order, even though both belong to the same customer. This level of detail is useful for a report that needs to see spending patterns broken down two ways at once, rather than by category or by customer alone.

## Ordering Grouped Results

`GROUP BY` collapses rows into groups, but it does not control what order those groups appear in. Combining it with `ORDER BY` on the aggregated column gives a ranked summary.

```postgresql with=orders.sql
SELECT category, SUM(amount) AS category_revenue
FROM orders
GROUP BY category
ORDER BY category_revenue DESC;
```

`ORDER BY category_revenue DESC` sorts the three grouped rows by their computed total, largest first, turning a plain summary into a ranked list the founders can read top to bottom. This pattern, group first, then order by the aggregate, is one of the most common shapes a reporting query takes.

## GROUP BY at a Glance

| Clause | Purpose |
|---|---|
| `GROUP BY column` | Collapse rows sharing the same value into one group per value |
| `GROUP BY col1, col2` | Group by every distinct combination of two or more columns |
| Aggregate + `GROUP BY` | Run `SUM`, `COUNT`, `AVG`, `MIN`, `MAX` separately within each group |
| Non-grouped, non-aggregated column in `SELECT` | Not allowed; the database would not know which value to show |

## Your Turn

The founders want to know how many orders each individual customer has placed, and their total spend, ranked from the highest spender down. Write a query against the `orders` table above that returns `customer_name`, an `order_count`, and a `total_spent`, ordered by `total_spent` descending.

```postgresql with=orders.sql
-- Write your query below
```

If your query groups by `customer_name` with `COUNT(*) AS order_count` and `SUM(amount) AS total_spent`, ordered by `total_spent DESC`, Ishita Rao comes out on top with three orders totaling 1760.00.

## Conclusion

`GROUP BY` is what turns a single flat summary into a per-category, per-customer, or per-combination breakdown, by partitioning rows before the `aggregate functions` run over them. Priya now has revenue by category, spending by customer and category together, and a ranked leaderboard, all built on the same `aggregate functions` from before. Grouping answers "summarize each bucket," but sometimes a report needs to discard entire buckets based on their summarized value, which is a job `WHERE` cannot do.
