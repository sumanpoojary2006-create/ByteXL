# Mini Project 6: Speeding Up a Slow Query

## Background

An index is invisible until the table gets big, and then it is the only thing standing between a query that returns instantly and one that scans every single row. This project builds a table large enough to actually feel slow, measures it honestly with `EXPLAIN ANALYZE`, adds the right index, and measures again, so the improvement is something you observe rather than something you are told about.

## What You Will Build

A synthetic `orders` table with hundreds of thousands of rows, a baseline measurement of two realistic query patterns, targeted indexes, and a re-measurement showing the difference.

## Dataset

```sql
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

## Tasks

### Task 1: Establish a Baseline

1. Run this query and record the execution time and plan using `EXPLAIN ANALYZE`:

   ```sql
   EXPLAIN ANALYZE
   SELECT * FROM orders WHERE customer_email = 'customer4213@example.com';
   ```

2. Run a second query for a common reporting pattern, and capture its plan too:

   ```sql
   EXPLAIN ANALYZE
   SELECT * FROM orders
   WHERE status = 'pending'
   ORDER BY order_date DESC
   LIMIT 20;
   ```

3. In both plans, find the line that says `Seq Scan on orders`. Note the reported number of rows scanned and the execution time.

### Task 2: Add the Right Indexes

1. Create a standard B-Tree index on `customer_email`, then re-run the Task 1.1 query with `EXPLAIN ANALYZE`. Confirm the plan now shows an `Index Scan` instead of a `Seq Scan`, and compare the execution time.
2. Create a composite index on `(status, order_date)` to match the filter-then-sort pattern in Task 1.2, then re-run that query and compare its plan.
3. Since `pending` orders are a small fraction of the 300000 rows, create a partial index instead, indexing only rows where `status = 'pending'`, and compare its size against the full composite index from step 2.

   ```sql
   CREATE INDEX idx_orders_customer_email ON orders (customer_email);

   CREATE INDEX idx_orders_status_date ON orders (status, order_date);

   CREATE INDEX idx_orders_pending ON orders (order_date) WHERE status = 'pending';
   ```

### Task 3: Iterate

1. Every index you add speeds up reads but slows down every `INSERT` and `UPDATE` on that table, and takes up disk space. Run `\di+` (or query `pg_indexes`) to see the size of each index you created, and decide whether all three are worth keeping on a table this size.
2. Describe, in a comment, what an "N+1 query" bottleneck looks like in application code that loops over a list of customers and issues one `SELECT * FROM orders WHERE customer_email = ...` per customer, instead of a single query with `WHERE customer_email IN (...)` or a join. Rewrite the loop as one query.
3. Pick one more slow pattern from your own reporting needs (for example, total revenue per month across all 300000 rows), measure it with `EXPLAIN ANALYZE`, add one index or rewrite the query, and measure again. Write down the before and after execution times.

**Answer these questions after completing all tasks:**
- Task 2.1 turned a `Seq Scan` into an `Index Scan`. If you ran the same indexed query but searched for an email with `LIKE '%4213%'` instead of an exact match, would the index still help? Test it and check the plan.
- You created three separate indexes in Task 2. If disk space and write speed were both tight constraints, which one would you drop first, and why, based on how selective each index actually is on this dataset?
- `EXPLAIN` shows you the planned cost before running a query; `EXPLAIN ANALYZE` actually runs it and shows real timings. Why might you prefer plain `EXPLAIN` over `EXPLAIN ANALYZE` when checking a query that includes a `DELETE` or `UPDATE`?
