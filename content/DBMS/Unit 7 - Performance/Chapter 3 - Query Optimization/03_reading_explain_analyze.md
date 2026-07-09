## Introduction

Plain `EXPLAIN`, covered in the previous lesson, only ever reports what the optimizer expects to happen, an estimate produced without actually running the query. Those estimates can be wrong, sometimes significantly, when the database's statistics are stale or when a condition's true selectivity is harder to predict than usual. `EXPLAIN ANALYZE` closes that gap: it actually executes the query, for real, and reports the plan alongside the actual measured time and actual row counts observed, letting Priya compare what the optimizer expected against what genuinely happened.

## Estimated vs. Actual, Side by Side

The same `orders` table, with a deliberately skewed distribution, sets up a case where an estimate and reality can diverge.

```postgresql file=analyze_demo.sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_id, amount)
SELECT i, CASE WHEN i <= 15000 THEN 1 ELSE (i % 200) + 2 END, (i * 10.5)::NUMERIC(10,2)
FROM generate_series(1, 20000) AS i;

CREATE INDEX idx_orders_customer_id ON orders (customer_id);
ANALYZE orders;
```

```postgresql with=analyze_demo.sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 1;
```

The output now includes both the familiar `cost=` and `rows=` estimates from plain `EXPLAIN`, and a second set of numbers: `actual time=startup..total rows=N loops=N`.

- **`actual time`**: reports genuinely measured milliseconds, not internal cost units.
- **`rows=N`** (in the actual section): reports how many rows this step genuinely returned when actually run, which can be compared directly against the earlier estimate on the same line.

## When Estimates and Reality Disagree

In this deliberately skewed dataset, three quarters of all rows belong to `customer_id = 1`, a distribution the optimizer's general statistics may not always model with perfect precision, especially before `ANALYZE` has run recently.

```postgresql with=analyze_demo.sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 1;
```

If the estimated `rows=` figure and the actual `rows=` figure from this same run differ substantially, that gap is a direct, measurable sign that the optimizer's assumptions about this data did not match reality, which can lead it to choose a plan that looked cheap on paper but performs worse in practice, such as an `index scan` for a condition that actually matches a huge fraction of the table, closer to the situation where a sequential scan would have been the better call, as covered in the optimizer lesson.

## Why loops=N Matters

For a step that gets executed more than once, such as the inner side of certain `join` strategies run once per outer row, `EXPLAIN ANALYZE` reports `loops=N`, and the `actual time` shown is the average per loop, not the total across all loops combined.

```postgresql with=analyze_demo.sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT
);

INSERT INTO customers (customer_id, customer_name)
SELECT i, 'Customer ' || i FROM generate_series(1, 210) AS i;

EXPLAIN ANALYZE
SELECT c.customer_name, o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.customer_id BETWEEN 1 AND 5;
```

If this plan runs its inner scan of `orders` once per matching customer, `loops=5` would appear on that inner step, and the true total time contributed by that step is its reported `actual time` multiplied by 5, not the number shown alone. Missing this detail is a common way to misread `EXPLAIN ANALYZE` output, understating how expensive a repeatedly executed inner step actually was in total.

## Why EXPLAIN ANALYZE Should Be Used with Care

Because `EXPLAIN ANALYZE` genuinely executes the query, it is not risk-free to run against a statement that modifies data; an `UPDATE` or `DELETE` wrapped in `EXPLAIN ANALYZE` really performs that update or delete. PostgreSQL provides an option specifically to avoid this danger for write statements that still need analyzing.

```postgresql with=analyze_demo.sql
BEGIN;
EXPLAIN ANALYZE UPDATE orders SET amount = amount * 1.05 WHERE customer_id = 1;
ROLLBACK;
```

Wrapping the `EXPLAIN ANALYZE UPDATE` in a transaction that ends with `ROLLBACK` instead of `COMMIT` is the standard, safe way to measure a write statement's real `execution plan` and timing without letting its actual changes persist, exactly the transactional safety net covered in the previous unit.

## EXPLAIN vs. EXPLAIN ANALYZE at a Glance

| | `EXPLAIN` | `EXPLAIN ANALYZE` |
|---|---|---|
| Executes the query | No | Yes, for real |
| Reports | Estimated cost, estimated rows | Estimated and actual time, estimated and actual rows |
| Safe for any statement | Yes | Only if wrapped in a transaction with `ROLLBACK` for write statements |
| Best for | A quick check of the chosen plan | Diagnosing where estimates and reality diverge |

## Your Turn

Run `EXPLAIN ANALYZE` on a query filtering `orders` for `customer_id = 50`, a value from the less-skewed portion of the data, and compare its estimated versus actual row counts to the earlier `customer_id = 1` example, noting in a comment which one shows a larger gap between estimate and reality.

```postgresql with=analyze_demo.sql
-- Write your query and comment below
```

`EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 50;` should show estimated and actual row counts much closer together than the `customer_id = 1` case, since customer 50's share of the data follows the more evenly distributed pattern the optimizer's statistics model more accurately.

## Conclusion

`EXPLAIN ANALYZE` actually runs a query and reports real measured time and real row counts alongside the optimizer's original estimates, making it possible to see exactly where a plan's assumptions matched reality and where they did not, with `loops=N` and a `ROLLBACK`-wrapped transaction as two details worth remembering when reading or running it. Priya can now diagnose not just what plan ran, but whether it was actually a good plan once real execution is accounted for. Behind many of these plans sits a specific choice this unit has not yet examined directly: which algorithm the database uses to actually perform a `join`.
