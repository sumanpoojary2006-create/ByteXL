## Introduction

An `index scan`, covered throughout this chapter, is already far cheaper than a `sequential scan`, but it is not free: after finding a matching entry in the index, the database still has to jump over to the actual table to fetch the rest of that row's columns, since a typical index only stores the `indexed` column plus a pointer, not the whole row.

That extra jump, from index entry to table page, is called a heap fetch, and for a query that touches many rows, all those extra jumps add up. A **covering index** is an index built specifically to eliminate that extra step entirely, letting the database answer a query using only the index, never touching the table at all.

**Definition:** A `covering index`, built with `INCLUDE`, stores extra columns alongside the `indexed` key so that a matching query can be answered entirely from the index, skipping the heap fetch a regular `index scan` still requires, at the cost of a larger index and more write overhead.

![Intro visual for covering indexes and indexonly scans](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_intro_covering_indexes_and_indexonly_scans_matched_5a0933ed.png)

## Watching a Heap Fetch Happen

The `orders` table sets up a query that needs more than just the `indexed` column. Only 20 of its 10000 orders are still active, the selective situation an index is best at, and the closing `VACUUM ANALYZE` both refreshes the planner's statistics and marks the table's pages as stable, something index-only scans, this lesson's subject, specifically depend on.

## Source Data Used in This Lesson

Some lessons need a larger dataset to make execution plans or maintenance behavior visible. For those tables, `init.sql` generates the rows instead of listing every row manually.

### Generated `orders` dataset

| Column | Definition in the setup |
| --- | --- |
| `order_id` | `INTEGER PRIMARY KEY` |
| `customer_name` | `TEXT` |
| `status` | `TEXT` |
| `amount` | `NUMERIC(10, 2)` |

The setup generates 10,000 rows, numbered from 1 through 10000. This scale is intentional because performance behavior is difficult to observe on a tiny table.

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
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

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkag6yr" 
 width="100%"
></iframe>

Expected output:

```
                                       QUERY PLAN
-----------------------------------------------------------------------------------------
 Index Scan using idx_orders_status on orders  (cost=4.32..44.15 rows=20 width=11)
   Index Cond: (status = 'active'::text)
```

The plan shows `idx_orders_status` finding the 20 matching rows, but that is not the whole story: `idx_orders_status` only stores `status` values and pointers back to matching rows, so for every match, the database still has to fetch that row from the actual table's heap to retrieve `order_id` and `amount`, columns the index itself does not contain. This heap fetch step is exactly the extra cost a `covering index` is built to remove.

![A regular index scan still performs heap fetches for missing columns](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_regular_index_scan_heap_fetch.png)

## Building a Covering Index with INCLUDE

PostgreSQL's `INCLUDE` clause adds extra columns to an index purely for storage alongside the `indexed` column, without making them part of the searchable, sorted key itself.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkag79y" 
 width="100%"
></iframe>

Expected output:

```
                                            QUERY PLAN
----------------------------------------------------------------------------------------------------
 Index Only Scan using idx_orders_status_covering on orders  (cost=0.29..12.63 rows=20 width=11)
   Index Cond: (status = 'active'::text)
   Heap Fetches: 0
```

The plan now reports an "Index Only Scan" instead of a scan that visits the heap, confirming that `order_id` and `amount`, both included in the `covering index`, are read directly from the index itself, with no need to visit the table's heap at all.

Every column the query asks for, both in `WHERE` and in `SELECT`, is now available directly from `idx_orders_status_covering`, which is exactly what "covering" the query means: the index alone is enough to answer it completely.

![A covering index can answer the query from the index alone](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_covering_index_index_only_scan.png)

## Why This Is Not Automatic for Every Index

An ordinary index, without `INCLUDE`, only ever gets an `index-only scan` if the query happens to need nothing beyond the `indexed` column itself and the table's visibility information the moment a query asks for even one column the index does not store, the database has no choice but to fall back to a regular `index scan` with a heap fetch for every matching row.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkag7kn" 
 width="100%"
></iframe>

Expected output:

```
                                       QUERY PLAN
-----------------------------------------------------------------------------------------
 Index Scan using idx_orders_status_covering on orders  (cost=0.29..44.15 rows=20 width=27)
   Index Cond: (status = 'active'::text)
```

Adding `customer_name` to the `SELECT` list, a column not included in `idx_orders_status_covering`, means the plan is no longer an Index Only Scan: the database is back to fetching every matching row from the heap, since the `covering index` cannot answer this broader request on its own. This is a direct, practical illustration of why a `covering index` has to be designed around the specific columns a specific query actually needs.

## The Trade-off a Covering Index Represents

`INCLUDE` columns come with two costs:

- The index grows larger, since it now physically stores copies of extra data beyond just the `indexed` key.
- Every write to those included columns also has to update the index, the same maintenance cost every index carries, just spread across more columns.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkag7vc" 
 width="100%"
></iframe>

Expected output:

| plain_index_size | covering_index_size |
| --- | --- |
| 88 kB | 296 kB |

- The `covering index` is noticeably larger than the plain one, since it duplicates `order_id` and `amount` alongside every entry, storage that exists purely to avoid heap fetches for a specific, known query pattern.
- `Covering indexes` are worth building for genuinely hot, frequently run queries where the read-speed benefit clearly outweighs the extra storage and write cost, not applied indiscriminately to every index in a schema.

![INCLUDE columns are stored in the index for reading, but are not the main search key](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_include_columns_stored_for_reading.png)

## Covering Indexes at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Heap fetch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The extra step of visiting the table after finding a match in a regular <code>index</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>INCLUDE (columns)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stores extra columns in the <code>index</code> purely for retrieval, not for searching</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Index Only Scan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The plan shown when every needed column is available directly from the <code>index</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trade-off</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Larger <code>index</code>, more write overhead, in exchange for eliminating heap fetches</td>
    </tr>
  </tbody>
</table>

## Your Turn

Create a `covering index` on `customer_name` that includes `status`, then confirm with `EXPLAIN` that a query selecting both columns, filtered by `customer_name`, produces an `index-only scan`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkag86d" 
 width="100%"
></iframe>

Expected result and verification:

If you run `CREATE INDEX idx_orders_name_covering ON orders (customer_name) INCLUDE (status);` followed by `EXPLAIN SELECT customer_name, status FROM orders WHERE customer_name = 'Customer 5000';`, the plan returns:

```
                                              QUERY PLAN
------------------------------------------------------------------------------------------------------
 Index Only Scan using idx_orders_name_covering on orders  (cost=0.29..8.31 rows=1 width=19)
   Index Cond: (customer_name = 'Customer 5000'::text)
   Heap Fetches: 0
```

This reports an Index Only Scan, since both the filtered column and the selected column are fully available from the `covering index` alone.

## Conclusion

A `covering index`, built with `INCLUDE`, stores extra columns alongside the `indexed` key so that a matching query can be answered entirely from the index, skipping the heap fetch a regular `index scan` still requires, at the cost of a larger index and more write overhead. Priya's most frequently run reports can now be tuned to avoid that extra table visit entirely.

Every index covered in this chapter has assumed adding one is worthwhile; the final lesson looks at when that assumption breaks down.
