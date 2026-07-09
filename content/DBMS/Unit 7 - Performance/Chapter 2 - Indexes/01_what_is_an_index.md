## Introduction

The previous chapter left Priya with a precise problem: a `full table scan` checks every row, and its cost grows with table size, even when a query only needs a tiny handful of matching rows. An old-fashioned phone book solves a strikingly similar problem. Finding "Rathi, Sanjay" in a phone book does not mean reading every entry from the first page onward; the book is alphabetically sorted, so a reader can jump straight to the R section and narrow in from there. A database **index** does exactly this for a table: a separate structure, built on one or more columns, that lets the database jump directly to matching rows instead of checking every one.

## Searching Without an Index

The `orders` table from the storage chapter, large enough for the cost difference to be visible, sets up the comparison.

```postgresql file=index_demo.sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_name, amount)
SELECT i, 'Customer ' || i, (i * 12.5)::NUMERIC(10,2)
FROM generate_series(1, 10000) AS i;
```

```postgresql with=index_demo.sql
EXPLAIN SELECT * FROM orders WHERE customer_name = 'Customer 7500';
```

There is no structure supporting a search on `customer_name`, so the plan reports a `sequential scan`, checking all 10000 rows to find the one whose name matches, exactly the phone-book equivalent of reading every page from the beginning because nothing is organized to help.

## Creating an Index and Watching the Plan Change

`CREATE INDEX` builds a separate structure that keeps track of where rows with each value of a column can be found, without physically reordering the table itself.

```postgresql with=index_demo.sql
CREATE INDEX idx_orders_customer_name ON orders (customer_name);

EXPLAIN SELECT * FROM orders WHERE customer_name = 'Customer 7500';
```

The plan changes to an "`Index Scan`," using `idx_orders_customer_name` to jump almost directly to the matching row, rather than checking all 10000. The `index` itself is sorted by `customer_name`, the same way a phone book is sorted by last name, so the database can narrow down to the matching entries the same way a reader flips to the right section of a phone book instead of starting from page one.

## What an Index Actually Is

An `index` is not a copy of the table. It is:

- A separate, smaller structure holding just the `indexed` column's values, sorted.
- Paired with a pointer, the `ctid` from the storage chapter, back to where the full row actually lives on disk.

Looking up a value in the `index` gives the database the exact physical location to fetch, instead of checking every row's actual data to find a match.

```postgresql with=index_demo.sql
SELECT pg_size_pretty(pg_relation_size('orders')) AS table_size,
       pg_size_pretty(pg_relation_size('idx_orders_customer_name')) AS index_size;
```

The `index` takes up its own disk space, separate from the table, since it is a genuinely separate structure that has to be built and stored. This is the fundamental trade-off every `index` represents: extra storage and extra maintenance work, in exchange for dramatically faster lookups on the `indexed` column.

## An Index Speeds Up Reads, But Costs Something on Writes

Because an `index` is a separate structure that must stay in sync with the table, every `INSERT`, `UPDATE`, or `DELETE` that touches an `indexed` column has to update the `index` too, not just the table.

```postgresql with=index_demo.sql
EXPLAIN ANALYZE INSERT INTO orders (order_id, customer_name, amount) VALUES (10001, 'Customer 10001', 500.00);
```

This single `INSERT` now does more work than it would on a table with no `indexes` at all:

1. Add the new row to the table's heap.
2. Add a corresponding entry to `idx_orders_customer_name`, keeping the two in sync.

This cost is usually small for one `index` on one row, but it is the reason `indexes` are not simply added to every column without consideration, a trade-off the final lesson of this chapter examines directly.

## Indexes at a Glance

| Without an `index` | With an `index` |
|---|---|
| Every search is a sequential scan | A matching search becomes an `index` scan |
| Cost grows with table size | Cost grows much more slowly, closer to the size of the result |
| No extra storage, no extra write cost | Extra storage, extra write cost to keep the `index` in sync |
| Nothing to maintain | Every insert, update, and delete on the `indexed` column updates the `index` too |

## Your Turn

Create an `index` on the `amount` column of the `orders` table above, then run `EXPLAIN` on a query filtering for `amount = 5000.00`, confirming the plan now uses an `index scan` instead of a sequential scan.

```postgresql with=index_demo.sql
-- Write your queries below
```

If you run `CREATE INDEX idx_orders_amount ON orders (amount);` followed by `EXPLAIN SELECT * FROM orders WHERE amount = 5000.00;`, the plan reports an `index scan` using `idx_orders_amount`, since the database can now look up matching rows through the sorted `index` instead of checking all 10000 rows directly.

## Conclusion

An `index` is a separate, sorted structure built on one or more columns that lets the database jump directly to matching rows instead of scanning the whole table, trading extra storage and slightly slower writes for dramatically faster reads on the `indexed` column, the same trade a phone book's alphabetical sorting makes over a randomly ordered list of names. Priya's slow customer-name lookups are now `index scans` instead of full scans. The next lesson looks closely at the specific structure most `indexes` actually use internally: the B-tree.
