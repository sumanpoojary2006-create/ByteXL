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
EXPLAIN SELECT * FROM orders WHERE customer_name = 'Customer 3000';
```

`EXPLAIN`, covered in full detail later in this unit, previews how the database plans to execute a query without actually running it. The plan here reports a "Seq Scan," short for `sequential scan`, meaning the database intends to read the table page by page, from the beginning, checking every row's `customer_name` against 'Customer 3000' until it reaches the end. Even though this query is only interested in exactly one row out of 5000, the heap organization from the previous lesson gives the database no shortcut, no way to know in advance which page holds that customer without checking.

```postgresql with=scan_demo.sql
SELECT COUNT(DISTINCT (ctid::text::point)[0]) AS pages_a_full_scan_must_read
FROM orders;
```

Using the same page-number extraction from the first lesson, this counts how many distinct pages the table occupies; a `sequential scan` has to read every single one of them, even for this single-row lookup, because a `sequential scan`'s cost scales with the size of the whole table, not with how many rows the query actually needs, whether that need is 1 row or 1000.

## Why the Primary Key Search Behaves Differently

Running the same shape of query, but filtering on `order_id`, the table's `primary key`, produces a completely different plan.

```postgresql with=scan_demo.sql
EXPLAIN SELECT * FROM orders WHERE order_id = 3000;
```

The plan now reports an "Index Scan using orders_pkey" instead of a `sequential scan`. The physical reality is that a `primary key` `constraint` does not change how rows are organized on disk, the table is still the same unordered heap, but PostgreSQL automatically builds a separate structure, an `index`, for every `primary key` in order to enforce uniqueness, and the planner uses that structure to jump straight to the right page instead of checking all of them. Nothing about the table's layout changed between these two queries; the only difference is that one column has a supporting structure and the other does not. That structure, the `index`, is exactly what the next chapter covers in depth.

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

| Situation | What happens | Cost scales with |
|---|---|---|
| Query needs most/all rows | Full table scan, often the right plan anyway | Table size, but unavoidable regardless |
| Query needs a few rows, column has no supporting structure | Full table scan, checking every page for a rare match | Table size, wastefully, since only a few rows were needed |
| Query filters on the `primary key` | `Index scan`, because PostgreSQL automatically builds an `index` for every `primary key` | Only the handful of pages actually holding the answer |

## Your Turn

Run `EXPLAIN` on a query filtering the `orders` table above for `amount > 120000`, a condition only a small fraction of rows will satisfy (`amount` tops out at 125000.00 for `order_id = 10000`), and note in a comment whether the plan shows a `sequential scan` and why that is expected given everything covered in this lesson.

```postgresql with=scan_demo.sql
-- Write your query and comment below
```

`EXPLAIN SELECT * FROM orders WHERE amount > 120000;` reports a `sequential scan`, exactly as expected, since `amount` has no supporting structure to help the database skip pages, meaning it must check every row's `amount` value against the condition regardless of how few rows actually qualify.

## Conclusion

Without a supporting structure on the column being filtered, a heap-organized table forces a query into a full table scan, reading every single page and checking every single row, with cost that scales directly with table size regardless of how few rows the query actually needs; the `primary key` search escaped this fate only because PostgreSQL quietly built an `index` for it. Priya finally has a concrete, physical explanation for why her reports slow down as the company's order history grows. The next chapter introduces that rescuing structure properly, and shows how to build one for any column a query filters on: the `index`.
