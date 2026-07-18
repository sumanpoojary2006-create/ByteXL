# Mini Project 6: Speeding Up a Slow Query

## Background

An index is invisible until the table gets big, and then it is the only thing standing between a query that returns instantly and one that scans every single row. This project builds a table large enough to actually feel slow, measures it honestly with `EXPLAIN ANALYZE`, adds the right index, and measures again, so the improvement is something you observe rather than something you are told about.

## What You Will Build

A synthetic `orders` table with hundreds of thousands of rows, a baseline measurement of two realistic query patterns, targeted indexes, and a re-measurement showing the difference.

## Dataset

Before writing project queries, inspect the starting data so every task has a visible source to reason from.

This project generates a larger dataset in `init.sql`. Inspect the schema and generation rule below before evaluating its execution plans.

Use two files in OneCompiler. Keep all `CREATE TABLE` and `INSERT` statements in `init.sql`; keep only the current task query in the active SQL file. The `with=init.sql` attribute connects the two files.

```postgresql file=init.sql
CREATE TABLE orders (
    order_id        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_email  TEXT NOT NULL,
    order_date      DATE NOT NULL,
    status          TEXT NOT NULL,
    total_amount    NUMERIC(10, 2) NOT NULL
);

INSERT INTO orders (customer_email, order_date, status, total_amount)
SELECT
    'customer' || (random() * 20000)::int || '@example.com',
    CURRENT_DATE - (random() * 730)::int,
    (ARRAY['pending', 'shipped', 'delivered', 'cancelled'])[(floor(random() * 4 + 1))::int],
    round((random() * 5000 + 100)::numeric, 2)
FROM generate_series(1, 300000);
```

### Confirm the Setup

Run this in the active SQL file before starting the tasks. It confirms that `init.sql` loaded the expected number of rows.

```postgresql with=init.sql
SELECT COUNT(*) AS loaded_rows FROM orders;
```

Expected output:

| loaded_rows |
| --- |
| 300000 |

## Tasks

### Task 1: Establish a Baseline

1. Run this query and record the execution time and plan using `EXPLAIN ANALYZE`:

   ```postgresql with=init.sql
   EXPLAIN ANALYZE
   SELECT * FROM orders WHERE customer_email = 'customer4213@example.com';
   ```

Expected output (before any index on `customer_email`):

```
                                                       QUERY PLAN
--------------------------------------------------------------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..6215.00 rows=15 width=53) (actual time=0.031..28.442 rows=15 loops=1)
   Filter: (customer_email = 'customer4213@example.com'::text)
   Rows Removed by Filter: 299985
 Planning Time: 0.112 ms
 Execution Time: 28.471 ms
```

The `Seq Scan` reads all 300000 `rows` to find the roughly 15 that match this one email (since `customer_email` values were generated with `random() * 20000`, each email appears on average about 300000 / 20000 = 15 times), and the `Execution Time` of roughly 28 ms is the baseline to beat once an `index` is added in Task 2.

2. Run a second query for a common reporting pattern, and capture its plan too:

   ```postgresql with=init.sql
   EXPLAIN ANALYZE
   SELECT * FROM orders
   WHERE status = 'pending'
   ORDER BY order_date DESC
   LIMIT 20;
   ```

Expected output (before any index on `status` or `order_date`):

```
                                                            QUERY PLAN
-----------------------------------------------------------------------------------------------------------------------------
 Limit  (cost=6688.05..6688.10 rows=20 width=53) (actual time=48.203..48.211 rows=20 loops=1)
   ->  Sort  (cost=6688.05..6875.55 rows=75000 width=53) (actual time=48.201..48.206 rows=20 loops=1)
         Sort Key: order_date DESC
         Sort Method: top-N heapsort  Memory: 30kB
         ->  Seq Scan on orders  (cost=0.00..6215.00 rows=75000 width=53) (actual time=0.018..33.712 rows=74981 loops=1)
               Filter: (status = 'pending'::text)
               Rows Removed by Filter: 225019
 Planning Time: 0.098 ms
 Execution Time: 48.244 ms
```

Since `status` is chosen from 4 roughly equal values, about a quarter of the 300000 `rows`, 75000, are `pending`, and with no `index` on either `status` or `order_date`, the `database` has to scan and filter all 300000 `rows` before sorting the survivors to find the most recent 20. The `Execution Time` of roughly 48 ms is the second baseline to compare against after adding indexes.

3. In both plans, find the line that says `Seq Scan on orders`. Note the reported number of rows scanned and the execution time.

### Task 2: Add the Right Indexes

1. Create a standard B-Tree index on `customer_email`, then re-run the Task 1.1 query with `EXPLAIN ANALYZE`. Confirm the plan now shows an `Index Scan` instead of a `Seq Scan`, and compare the execution time.
2. Create a composite index on `(status, order_date)` to match the filter-then-sort pattern in Task 1.2, then re-run that query and compare its plan.
3. Since `pending` orders are a small fraction of the 300000 rows, create a partial index instead, indexing only rows where `status = 'pending'`, and compare its size against the full composite index from step 2.

   ```postgresql with=init.sql
   CREATE INDEX idx_orders_customer_email ON orders (customer_email);

   CREATE INDEX idx_orders_status_date ON orders (status, order_date);

   CREATE INDEX idx_orders_pending ON orders (order_date) WHERE status = 'pending';
   ```

Expected result: PostgreSQL creates both indexes successfully. Re-run the earlier `EXPLAIN ANALYZE` statements to verify whether the access path and execution time improve.

### Task 3: Iterate

1. Every index you add speeds up reads but slows down every `INSERT` and `UPDATE` on that table, and takes up disk space. Run `\di+` (or query `pg_indexes`) to see the size of each index you created, and decide whether all three are worth keeping on a table this size.
2. Describe, in a comment, what an "N+1 query" bottleneck looks like in application code that loops over a list of customers and issues one `SELECT * FROM orders WHERE customer_email = ...` per customer, instead of a single query with `WHERE customer_email IN (...)` or a join. Rewrite the loop as one query.
3. Pick one more slow pattern from your own reporting needs (for example, total revenue per month across all 300000 rows), measure it with `EXPLAIN ANALYZE`, add one index or rewrite the query, and measure again. Write down the before and after execution times.

**Answer these questions after completing all tasks:**
- Task 2.1 turned a `Seq Scan` into an `Index Scan`. If you ran the same indexed query but searched for an email with `LIKE '%4213%'` instead of an exact match, would the index still help? Test it and check the plan.
- You created three separate indexes in Task 2. If disk space and write speed were both tight constraints, which one would you drop first, and why, based on how selective each index actually is on this dataset?
- `EXPLAIN` shows you the planned cost before running a query; `EXPLAIN ANALYZE` actually runs it and shows real timings. Why might you prefer plain `EXPLAIN` over `EXPLAIN ANALYZE` when checking a query that includes a `DELETE` or `UPDATE`?
