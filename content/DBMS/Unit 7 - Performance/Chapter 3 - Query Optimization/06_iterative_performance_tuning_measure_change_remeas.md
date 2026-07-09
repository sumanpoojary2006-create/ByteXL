## Introduction

Every technique covered in this unit, storage layout, `indexes`, `EXPLAIN`, `join` algorithms, and common bottlenecks, is a piece of a single repeatable process, not a checklist to apply once and forget. Real performance tuning is iterative: measure how a query actually performs, make one deliberate change, measure again to confirm that change actually helped, and repeat, rather than guessing at several changes at once and hoping the combination works. This final lesson walks through that full loop, start to finish, on one query.

## Step One: Measure the Starting Point

Before changing anything, the first step is always establishing an honest baseline with `EXPLAIN ANALYZE`, the actual-execution tool covered earlier in this chapter.

```postgresql file=tuning_demo.sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    status TEXT,
    amount NUMERIC(10, 2),
    order_date DATE
);

INSERT INTO orders (order_id, customer_id, status, amount, order_date)
SELECT i, (i % 8000) + 1,
       CASE WHEN i % 500 = 0 THEN 'refunded' ELSE 'completed' END,
       (i * 7.25)::NUMERIC(10,2),
       DATE '2025-01-01' + (i % 365)
FROM generate_series(1, 60000) AS i;
```

```postgresql with=tuning_demo.sql
EXPLAIN ANALYZE
SELECT customer_id, SUM(amount) AS total_refunded
FROM orders
WHERE status = 'refunded' AND order_date > '2025-06-01'
GROUP BY customer_id
ORDER BY total_refunded DESC;
```

This baseline plan, with no supporting `index` on either `status` or `order_date`, is expected to show a `sequential scan` across all 60000 rows before filtering down to the small refunded, recent subset the query actually cares about. Recording this baseline's actual time is essential, since without it, there is no way to later confirm whether a change genuinely helped or made no real difference.

## Step Two: Make One Deliberate Change

Rather than adding several `indexes` at once, the disciplined approach is one change at a time, so its individual effect can be measured cleanly. A `composite index` matching both filter columns together, the technique covered in the `indexes` chapter, is a reasonable first attempt here.

```postgresql with=tuning_demo.sql
CREATE INDEX idx_orders_status_date ON orders (status, order_date);
```

This single, targeted change is the entire first iteration, nothing else about the query or the `schema` is touched yet, keeping the next measurement a clean, isolated comparison against the baseline.

## Step Three: Re-measure and Compare

```postgresql with=tuning_demo.sql
EXPLAIN ANALYZE
SELECT customer_id, SUM(amount) AS total_refunded
FROM orders
WHERE status = 'refunded' AND order_date > '2025-06-01'
GROUP BY customer_id
ORDER BY total_refunded DESC;
```

Comparing this plan's actual time directly against the baseline's is the entire point of the exercise:

- If the plan now shows an `index scan` on `idx_orders_status_date` with a meaningfully lower actual time, the change is confirmed as a real improvement, not just a plausible-sounding guess.
- If the actual time barely moved, or if the optimizer still chose a `sequential scan` anyway, perhaps because the filtered rows are not selective enough for the `index` to be worth using, that is equally important information, and it means the next iteration should try a different change rather than assuming this one worked.

## Step Four: Repeat, One Change at a Time

If the first change helped but the query is still slower than needed, the loop continues: identify the next likely bottleneck from what `EXPLAIN ANALYZE` now shows, make one more targeted change, and measure again.

```postgresql with=tuning_demo.sql
EXPLAIN ANALYZE
SELECT customer_id, SUM(amount) AS total_refunded
FROM orders
WHERE status = 'refunded' AND order_date > '2025-06-01'
GROUP BY customer_id
ORDER BY total_refunded DESC
LIMIT 10;
```

If the actual business need only ever wants the top 10 customers by refund total, adding `LIMIT 10` is itself a legitimate next iteration, changing the query rather than the `schema`, and it is worth re-measuring separately from the `indexing` change to see how much it alone contributes, keeping each iteration's effect distinct and attributable.

## Why This Discipline Matters More Than Any Single Technique

The specific techniques covered across this unit, storage awareness, `indexing`, reading plans, understanding `join` algorithms, are all just tools available during this loop. A tuning session that skips measurement and jumps straight to "add `indexes` everywhere" risks the over-indexing cost covered earlier in this unit, paying for write overhead on `indexes` that never actually helped the query they were added for. Measuring first, changing one thing, and measuring again is what turns tuning from guesswork into an evidence-based process with a clear, demonstrable outcome at every step.

## The Iterative Tuning Loop at a Glance

| Step | Action |
|---|---|
| 1. Measure | Run `EXPLAIN ANALYZE` to get an honest actual-time baseline |
| 2. Change | Make exactly one deliberate, targeted change |
| 3. Re-measure | Run `EXPLAIN ANALYZE` again, compare actual time against the baseline |
| 4. Repeat | If still not fast enough, identify the next bottleneck and repeat from step 2 |

## Your Turn

Using the `orders` table above, measure the baseline for a query filtering `WHERE customer_id = 4000`, add an appropriate `index`, and re-measure to confirm the improvement, following the same measure-change-re-measure discipline covered in this lesson.

```postgresql with=tuning_demo.sql
-- Write your queries below
```

Running `EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 4000;` first establishes a sequential-scan baseline, then `CREATE INDEX idx_orders_customer_id ON orders (customer_id);` followed by the same `EXPLAIN ANALYZE` a second time confirms the switch to an `index scan` and a measurably lower actual time, the complete loop applied end to end.

## Conclusion

Iterative tuning, measure with `EXPLAIN ANALYZE`, make one deliberate change, re-measure to confirm it actually helped, and repeat, is the discipline that ties every technique in this unit together into a real, evidence-based process, rather than a collection of tricks applied on faith. Priya now has a complete, repeatable method for taking any slow query from a first honest measurement to a confirmed improvement. With storage, `indexing`, and query optimization all covered, the course moves next into the practical work of running a database in a real, production environment.
