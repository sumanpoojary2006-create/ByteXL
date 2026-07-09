## Introduction

Most real-world performance problems trace back to a small handful of recurring patterns, not exotic, one-off causes. With scans, `indexes`, plans, and `join` algorithms all covered individually across this unit, this lesson names the three bottlenecks Priya is most likely to actually encounter in practice:

- A missing `index` on a genuinely selective column
- An application pattern called the `N+1 query` problem
- Large, unnecessary scans hiding inside an otherwise reasonable-looking query

## Bottleneck One: A Missing Index on a Selective Column

The clearest, most mechanical bottleneck is a filter condition on a column with no supporting `index`, forcing a `sequential scan` even when very few rows actually match.

```postgresql file=bottleneck_demo.sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    status TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_id, status, amount)
SELECT i, (i % 5000) + 1,
       CASE WHEN i % 1000 = 0 THEN 'flagged' ELSE 'normal' END,
       (i * 10.5)::NUMERIC(10,2)
FROM generate_series(1, 50000) AS i;
```

```postgresql with=bottleneck_demo.sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'flagged';
```

Only about 1 in 1000 rows are flagged, a highly selective condition, but with no `index` on `status`, the plan is forced into a `sequential scan` of all 50000 rows to find the roughly 50 that match. This is the most straightforward bottleneck to diagnose, `EXPLAIN` clearly shows a `sequential scan`, and the fix, an `index`, is exactly what the previous chapter covered.

```postgresql with=bottleneck_demo.sql
CREATE INDEX idx_orders_status ON orders (status);

EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'flagged';
```

The plan switches to an `index scan`, and the actual measured time drops accordingly, precisely the diagnostic workflow, run `EXPLAIN ANALYZE`, spot a `sequential scan` on a selective filter, add an `index`, confirm the plan changes.

## Bottleneck Two: The N+1 Query Problem

This bottleneck lives in application code, not in any single SQL statement. It happens when code first fetches a list of parent rows with one query, then loops over that list, running one additional query per item to fetch related data, N extra queries for N parent rows, instead of one query that fetches everything together.

```postgresql with=bottleneck_demo.sql
-- The N+1 pattern, shown as pseudocode alongside the SQL it represents:
-- 1 query to fetch customers:
SELECT customer_id FROM orders GROUP BY customer_id LIMIT 5;

-- then, in application code, looping over each of those 5 customer_ids:
-- for each customer_id in the list above:
--     SELECT * FROM orders WHERE customer_id = customer_id;
-- This runs 1 + 5 = 6 total queries for just 5 customers.
-- With 5000 customers instead of 5, this becomes 5001 separate round trips
-- to the database, each with its own network latency, even though the
-- total amount of data needed is the same either way.
```

The fix is almost always the same one covered throughout the `joins` chapter: replace the loop of individual queries with a single query that `joins` or filters for everything needed at once.

```postgresql with=bottleneck_demo.sql
SELECT customer_id, order_id, amount
FROM orders
WHERE customer_id IN (
    SELECT customer_id FROM orders GROUP BY customer_id LIMIT 5
);
```

This single query retrieves the exact same data the 6-query loop above would have gathered, but as one round trip instead of six, and the gap between those two approaches only widens as the number of parent rows grows, which is exactly why N+1 is such a common, costly bottleneck in real applications built on top of an object-relational mapper or any code that fetches a list and then loops.

## Bottleneck Three: Large Scans Hiding Inside a Reasonable-Looking Query

Sometimes a query looks selective at a glance but is not, because a function or a type mismatch on the filtered column silently defeats an otherwise-present `index`, forcing a full scan the same way a missing `index` would.

```postgresql with=bottleneck_demo.sql
CREATE INDEX idx_orders_amount ON orders (amount);

EXPLAIN SELECT * FROM orders WHERE amount::TEXT = '525.00';
```

Casting `amount` to text before comparing defeats `idx_orders_amount`, since the `index` is built on the numeric column's own sorted values, not on a text-converted version of them, forcing a `sequential scan` despite an `index` technically existing on the underlying column. This is a subtle bottleneck precisely because the query author may not realize the cast is even happening, especially if it was introduced indirectly through application code building the condition dynamically.

```postgresql with=bottleneck_demo.sql
EXPLAIN SELECT * FROM orders WHERE amount = 525.00;
```

Removing the cast and comparing directly against the numeric value restores the `index scan`, confirming the cast, not the `index` itself, was the actual bottleneck.

## Common Bottlenecks at a Glance

| Bottleneck | How it shows up | Fix |
|---|---|---|
| Missing `index` on a selective filter | `EXPLAIN` shows a sequential scan on a highly selective condition | Add an appropriate `index` |
| N+1 queries | One query, then N more in a loop, visible in application logs or query counts | Replace the loop with a single query using a `join` or `IN` |
| A function or cast defeating an `index` | `EXPLAIN` shows a sequential scan despite a relevant `index` existing | Remove the cast/function, or build an expression `index` matching it |

## Your Turn

Check whether filtering `orders` on `customer_id = 42` uses an `index`, given there is currently no `index` on `customer_id`, then create one and confirm the plan changes.

```postgresql with=bottleneck_demo.sql
-- Write your queries below
```

`EXPLAIN SELECT * FROM orders WHERE customer_id = 42;` shows a `sequential scan` before an `index` exists; after running `CREATE INDEX idx_orders_customer_id ON orders (customer_id);`, the same `EXPLAIN` shows an `index scan` instead, the same missing-index bottleneck pattern from earlier in this lesson.

## Conclusion

A missing `index` on a selective column, the `N+1 query` pattern hiding in application code, and a function or cast silently defeating an otherwise-useful `index` are three of the most common ways a real system slows down, and all three are diagnosable with the same tools covered across this unit: `EXPLAIN`, `EXPLAIN ANALYZE`, and a clear understanding of what each plan node actually means. Priya now has a checklist of the first places to look whenever a report starts running slower than expected. The final lesson in this unit turns these individual diagnoses into a repeatable process for tuning a query end to end.
