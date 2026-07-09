## Introduction

The previous two lessons established two physical facts: data is read in whole pages, not individual rows, and a heap, PostgreSQL's default organization, offers no guarantee about which rows end up on which pages. This lesson connects those two facts directly to something Priya can actually see happen: without any help, finding rows in a heap table means reading every single page, checking every single row, an approach called a `full table scan`, and it gets slower in direct proportion to how large the table grows.

## Watching a Full Table Scan Happen

A larger table makes the cost of a full scan easy to observe directly.

```postgresql file=scan_demo.sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_name, amount)
SELECT i, 'Customer ' || i, (i * 12.5)::NUMERIC(10,2)
FROM generate_series(1, 5000) AS i;
```

```postgresql with=scan_demo.sql
EXPLAIN SELECT * FROM orders WHERE order_id = 3000;
```

`EXPLAIN`, covered in full detail later in this unit, previews how the database plans to execute a query without actually running it. The plan here reports a "Seq Scan," short for `sequential scan`, meaning the database intends to read the table page by page, from the beginning, checking every row's `order_id` against 3000 until it either finds a match or reaches the end. Even though this query is only interested in exactly one row out of 5000, the heap organization from the previous lesson gives the database no shortcut, no way to know in advance which page holds `order_id = 3000` without checking.

## Why the Primary Key Alone Does Not Prevent This

It might seem surprising that searching by `order_id`, the table's own `primary key`, still results in a full scan. The physical reality is that a `primary key` `constraint` guarantees uniqueness and enforces `NOT NULL`, but it does not, by itself, change how rows are physically organized on disk into a heap. What actually prevents a full scan is a separate structure entirely, an `index`, which the very next chapter in this unit covers in depth. Without one, even a search on the `primary key` column has to fall back to checking every page.

```postgresql with=scan_demo.sql
SELECT COUNT(*) AS pages_touched_in_worst_case
FROM (SELECT DISTINCT ctid::text FROM orders) AS distinct_pages;
```

This is an approximation for illustration, counting distinct physical row locations, but the underlying point holds regardless of the exact number: a `sequential scan`'s cost scales with the size of the whole table, not with how many rows the query actually needs, whether that need is 1 row or 1000.

## How Table Size Directly Predicts Scan Cost

Doubling the number of rows in a heap table roughly doubles the number of pages it occupies, and a full scan reads every page, so a full scan's cost grows linearly with table size, a relationship worth being able to reason about directly.

```postgresql with=scan_demo.sql
SELECT pg_size_pretty(pg_relation_size('orders')) AS current_size;

INSERT INTO orders (order_id, customer_name, amount)
SELECT i, 'Customer ' || i, (i * 12.5)::NUMERIC(10,2)
FROM generate_series(5001, 10000) AS i;

SELECT pg_size_pretty(pg_relation_size('orders')) AS size_after_doubling_rows;
```

Doubling the row count roughly doubles the reported table size, and a full scan against this larger table now has roughly twice as many pages to check for the exact same single-row lookup, even though the answer being searched for has not changed in any way. This is precisely why "it worked fine on my small test table" is not evidence that a query will stay fast once real data volume arrives; a `full table scan`'s cost is a direct, predictable function of table size.

## What a Full Table Scan Is and Is Not

A full scan is not always the wrong choice:

- When a query genuinely needs most or all of a table's rows, such as computing an aggregate across the entire table, reading every page is unavoidable regardless of any structure available, and a full scan is often the most efficient plan the database could choose.
- Full scans become a problem specifically when a query only needs a small fraction of a large table's rows, since that is exactly the situation where reading every page is enormously wasteful compared to reading just the handful of pages that actually matter.

## Storage Layout and Query Speed at a Glance

| Situation | What happens without an `index` | Cost scales with |
|---|---|---|
| Query needs most/all rows | Full table scan, often the right plan anyway | Table size, but unavoidable regardless |
| Query needs a few rows out of many | Full table scan, checking every page for a rare match | Table size, wastefully, since only a few rows were needed |
| Heap has no ordering guarantee | Even a primary key search cannot skip pages without an `index` | Table size, until an `index` changes this |

## Your Turn

Run `EXPLAIN` on a query filtering the `orders` table above for `amount > 50000`, a condition that only a small fraction of rows will satisfy, and note in a comment whether the plan shows a `sequential scan` and why that is expected given everything covered in this lesson.

```postgresql with=scan_demo.sql
-- Write your query and comment below
```

`EXPLAIN SELECT * FROM orders WHERE amount > 50000;` reports a `sequential scan`, exactly as expected, since `amount` has no supporting structure to help the database skip pages, meaning it must check every row's `amount` value against the condition regardless of how few rows actually qualify.

## Conclusion

Without any supporting structure, a heap-organized table forces every query, even one filtering on the `primary key`, to fall back to a full table scan, reading every single page and checking every single row, with cost that scales directly with table size regardless of how few rows the query actually needs. Priya finally has a concrete, physical explanation for why her reports slow down as the company's order history grows. The next chapter introduces the structure specifically designed to fix exactly this problem: the `index`.
