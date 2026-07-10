## Introduction

An `index scan`, covered throughout this chapter, is already far cheaper than a sequential scan, but it is not free: after finding a matching entry in the `index`, the database still has to jump over to the actual table to fetch the rest of that row's columns, since a typical `index` only stores the `indexed` column plus a pointer, not the whole row. That extra jump, from `index` entry to table page, is called a heap fetch, and for a query that touches many rows, all those extra jumps add up. A **covering index** is an `index` built specifically to eliminate that extra step entirely, letting the database answer a query using only the `index`, never touching the table at all.

## Watching a Heap Fetch Happen

The `orders` table sets up a query that needs more than just the `indexed` column. Only 20 of its 10000 orders are still active, the selective situation an `index` is best at, and the closing `VACUUM ANALYZE` both refreshes the planner's statistics and marks the table's pages as stable, something index-only scans, this lesson's subject, specifically depend on.

```postgresql file=covering_demo.sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    status TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_name, status, amount)
SELECT i, 'Customer ' || i, CASE WHEN i % 500 = 0 THEN 'active' ELSE 'completed' END, (i * 12.5)::NUMERIC(10,2)
FROM generate_series(1, 10000) AS i;

CREATE INDEX idx_orders_status ON orders (status);

VACUUM ANALYZE orders;
```

```postgresql with=covering_demo.sql
EXPLAIN SELECT order_id, amount FROM orders WHERE status = 'active';
```

The plan shows `idx_orders_status` finding the 20 matching rows, but that is not the whole story: `idx_orders_status` only stores `status` values and pointers back to matching rows, so for every match, the database still has to fetch that row from the actual table's heap to retrieve `order_id` and `amount`, columns the `index` itself does not contain. This heap fetch step is exactly the extra cost a `covering index` is built to remove.

## Building a Covering Index with INCLUDE

PostgreSQL's `INCLUDE` clause adds extra columns to an `index` purely for storage alongside the `indexed` column, without making them part of the searchable, sorted key itself.

```postgresql with=covering_demo.sql
CREATE INDEX idx_orders_status_covering ON orders (status) INCLUDE (order_id, amount);

EXPLAIN SELECT order_id, amount FROM orders WHERE status = 'active';
```

The plan now reports an "Index Only Scan" instead of a scan that visits the heap, confirming that `order_id` and `amount`, both included in the `covering index`, are read directly from the `index` itself, with no need to visit the table's heap at all. Every column the query asks for, both in `WHERE` and in `SELECT`, is now available directly from `idx_orders_status_covering`, which is exactly what "covering" the query means: the `index` alone is enough to answer it completely.

## Why This Is Not Automatic for Every Index

An ordinary `index`, without `INCLUDE`, only ever gets an index-only scan if the query happens to need nothing beyond the `indexed` column itself and the table's visibility information; the moment a query asks for even one column the `index` does not store, the database has no choice but to fall back to a regular `index scan` with a heap fetch for every matching row.

```postgresql with=covering_demo.sql
CREATE INDEX idx_orders_status_covering ON orders (status) INCLUDE (order_id, amount);

EXPLAIN SELECT order_id, amount, customer_name FROM orders WHERE status = 'active';
```

Adding `customer_name` to the `SELECT` list, a column not included in `idx_orders_status_covering`, means the plan is no longer an Index Only Scan: the database is back to fetching every matching row from the heap, since the `covering index` cannot answer this broader request on its own. This is a direct, practical illustration of why a `covering index` has to be designed around the specific columns a specific query actually needs.

## The Trade-off a Covering Index Represents

`INCLUDE` columns come with two costs:

- The `index` grows larger, since it now physically stores copies of extra data beyond just the `indexed` key.
- Every write to those included columns also has to update the `index`, the same maintenance cost every `index` carries, just spread across more columns.

```postgresql with=covering_demo.sql
CREATE INDEX idx_orders_status_covering ON orders (status) INCLUDE (order_id, amount);

SELECT pg_size_pretty(pg_relation_size('idx_orders_status')) AS plain_index_size,
       pg_size_pretty(pg_relation_size('idx_orders_status_covering')) AS covering_index_size;
```

The `covering index` is noticeably larger than the plain one, since it duplicates `order_id` and `amount` alongside every entry, storage that exists purely to avoid heap fetches for a specific, known query pattern. `Covering indexes` are worth building for genuinely hot, frequently run queries where the read-speed benefit clearly outweighs the extra storage and write cost, not applied indiscriminately to every `index` in a `schema`.

## Covering Indexes at a Glance

| Concept | Detail |
|---|---|
| Heap fetch | The extra step of visiting the table after finding a match in a regular `index` |
| `INCLUDE (columns)` | Stores extra columns in the `index` purely for retrieval, not for searching |
| Index Only Scan | The plan shown when every needed column is available directly from the `index` |
| Trade-off | Larger `index`, more write overhead, in exchange for eliminating heap fetches |

## Your Turn

Create a `covering index` on `customer_name` that includes `status`, then confirm with `EXPLAIN` that a query selecting both columns, filtered by `customer_name`, produces an `index-only scan`.

```postgresql with=covering_demo.sql
-- Write your queries below
```

If you run `CREATE INDEX idx_orders_name_covering ON orders (customer_name) INCLUDE (status);` followed by `EXPLAIN SELECT customer_name, status FROM orders WHERE customer_name = 'Customer 5000';`, the plan reports an Index Only Scan, since both the filtered column and the selected column are fully available from the `covering index` alone.

## Conclusion

A `covering index`, built with `INCLUDE`, stores extra columns alongside the `indexed` key so that a matching query can be answered entirely from the `index`, skipping the heap fetch a regular `index scan` still requires, at the cost of a larger `index` and more write overhead. Priya's most frequently run reports can now be tuned to avoid that extra table visit entirely. Every `index` covered in this chapter has assumed adding one is worthwhile; the final lesson looks at when that assumption breaks down.
