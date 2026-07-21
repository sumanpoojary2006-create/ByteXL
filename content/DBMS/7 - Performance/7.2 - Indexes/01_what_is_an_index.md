## Introduction

The previous chapter left Priya with a precise problem: a `full table scan` checks every `row`, and its cost grows with `table` size, even when a `query` only needs a tiny handful of matching `rows`. An old-fashioned phone book solves a strikingly similar problem.

Finding "Rathi, Sanjay" in a phone book does not mean reading every entry from the first page onward; the book is alphabetically sorted, so a reader can jump straight to the R section and narrow in from there. A `database` **`index`** does exactly this for a `table`: a separate structure, built on one or more `columns`, that lets the `database` jump directly to matching `rows` instead of checking every one.

**Definition:** An `index` is a separate, sorted structure built on one or more `columns` that lets the `database` jump directly to matching `rows` instead of scanning the whole `table`, trading extra storage and slightly slower writes for dramatically faster reads on the `indexed` `column`, the same trade a phone book's alphabetical sorting makes over a randomly ordered list of names.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_what_is_an_index.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: The previous chapter left Priya with a precise problem: a full table scan checks every row, and its cost grows with table size, even when a query only needs a tiny handful of matching rows. An old-fashioned phone book solves a strikingly similar problem.

ON-IMAGE TEXT: show a short bold title "What Is An Index" plus only these few labels, large and legible: Table, Row, Query. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for what is an index](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_what_is_an_index_matched_12adb909.png)

## Searching Without an Index

The `orders` `table` from the storage chapter, large enough for the cost difference to be visible, sets up the comparison. The closing `ANALYZE` statement refreshes the statistics the `query planner` uses to estimate how many `rows` a condition will match; every setup in this chapter runs it after loading data, and it returns in full detail alongside `EXPLAIN` in the next chapter.

## Source Data Used in This Lesson

Some lessons need a larger dataset to make execution plans or maintenance behavior visible. For those tables, `init.sql` generates the rows instead of listing every row manually.

### Generated `orders` dataset

| Column | Definition in the setup |
| --- | --- |
| `order_id` | `INTEGER PRIMARY KEY` |
| `customer_name` | `TEXT` |
| `amount` | `NUMERIC(10, 2)` |

The setup generates 10,000 rows, numbered from 1 through 10000. This scale is intentional because performance behavior is difficult to observe on a tiny table.

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_name, amount)
SELECT i, 'Customer ' || i, (i * 12.5)::NUMERIC(10,2)
FROM generate_series(1, 10000) AS i;

ANALYZE orders;
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
EXPLAIN SELECT * FROM orders WHERE customer_name = 'Customer 7500';
```

Expected output:

```
                            QUERY PLAN
-------------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..195.00 rows=1 width=23)
   Filter: (customer_name = 'Customer 7500'::text)
```

There is no structure supporting a search on `customer_name`, so the plan reports a `sequential scan`, checking all 10000 `rows` to find the one whose name matches, exactly the phone-book equivalent of reading every page from the beginning because nothing is organized to help.

![Without an index the database scans all rows; with an index it jumps to the match](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_without_index_vs_with_index_shortcut.png)

## Creating an Index and Watching the Plan Change

`CREATE INDEX` builds a separate structure that keeps track of where `rows` with each value of a `column` can be found, without physically reordering the `table` itself.

```postgresql with=init.sql
CREATE INDEX idx_orders_customer_name ON orders (customer_name);

EXPLAIN SELECT * FROM orders WHERE customer_name = 'Customer 7500';
```

Expected output:

```
                                        QUERY PLAN
--------------------------------------------------------------------------------------------
 Index Scan using idx_orders_customer_name on orders  (cost=0.29..8.31 rows=1 width=23)
   Index Cond: (customer_name = 'Customer 7500'::text)
```

The plan changes to an "`Index Scan`," using `idx_orders_customer_name` to jump almost directly to the matching `row`, rather than checking all 10000. The `index` itself is sorted by `customer_name`, the same way a phone book is sorted by last name, so the `database` can narrow down to the matching entries the same way a reader flips to the right section of a phone book instead of starting from page one.

![An index stores key values with pointers back to the full table rows](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_index_key_plus_pointer.png)

## What an Index Actually Is

An `index` is not a copy of the `table`. It is:

- A separate, smaller structure holding just the `indexed` `column`'s values, sorted.
- Paired with a pointer, the `ctid` from the storage chapter, back to where the full `row` actually lives on disk.

Looking up a value in the `index` gives the `database` the exact physical location to fetch, instead of checking every `row`'s actual data to find a match.

```postgresql with=init.sql
CREATE INDEX idx_orders_customer_name ON orders (customer_name);

SELECT pg_size_pretty(pg_relation_size('orders')) AS table_size,
       pg_size_pretty(pg_relation_size('idx_orders_customer_name')) AS index_size;
```

Expected output:

| table_size | index_size |
| --- | --- |
| 728 kB | 320 kB |

The `index` takes up its own disk space, separate from the `table`, since it is a genuinely separate structure that has to be built and stored. This is the fundamental trade-off every `index` represents: extra storage and extra maintenance work, in exchange for dramatically faster lookups on the `indexed` `column`.

## An Index Speeds Up Reads, But Costs Something on Writes

Because an `index` is a separate structure that must stay in sync with the `table`, every `INSERT`, `UPDATE`, or `DELETE` that touches an `indexed` `column` has to update the `index` too, not just the `table`.

```postgresql with=init.sql
CREATE INDEX idx_orders_customer_name ON orders (customer_name);

SELECT pg_size_pretty(pg_relation_size('idx_orders_customer_name')) AS index_size_before;

INSERT INTO orders (order_id, customer_name, amount)
SELECT i, 'Customer ' || i, (i * 12.5)::NUMERIC(10,2)
FROM generate_series(10001, 20000) AS i;

SELECT pg_size_pretty(pg_relation_size('idx_orders_customer_name')) AS index_size_after;
```

Expected output:

| index_size_before |
| --- |
| 320 kB |

| index_size_after |
| --- |
| 640 kB |

The `index` visibly grows after the insert, which is the proof that every one of those 10000 new `rows` did double work:

1. Add the new `row` to the `table`'s heap.

2. Add a corresponding entry to `idx_orders_customer_name`, keeping the two in sync.

This cost is usually small for one `index` on one `row`, but it is the reason `indexes` are not simply added to every `column` without consideration, a trade-off the final lesson of this chapter examines directly.

## Indexes at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Without an <code>index</code></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">With an <code>index</code></th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every search is a sequential scan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A matching search becomes an <code>index</code> scan</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost grows with table size</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost grows much more slowly, closer to the size of the result</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No extra storage, no extra write cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extra storage, extra write cost to keep the <code>index</code> in sync</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nothing to maintain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every insert, update, and delete on the <code>indexed</code> column updates the <code>index</code> too</td>
    </tr>
  </tbody>
</table>

## Your Turn

Create an `index` on the `amount` `column` of the `orders` `table` above, then run `EXPLAIN` on a `query` filtering for `amount = 5000.00`, confirming the plan now uses an `index scan` instead of a `sequential scan`.

```postgresql with=init.sql
-- Write your queries below
```

Expected result and verification:

If you run `CREATE INDEX idx_orders_amount ON orders (amount);` followed by `EXPLAIN SELECT * FROM orders WHERE amount = 5000.00;`, the plan reports an `index scan` using `idx_orders_amount`, since the `database` can now look up matching `rows` through the sorted `index` instead of checking all 10000 `rows` directly.

## Conclusion

An `index` is a separate, sorted structure built on one or more `columns` that lets the `database` jump directly to matching `rows` instead of scanning the whole `table`, trading extra storage and slightly slower writes for dramatically faster reads on the `indexed` `column`, the same trade a phone book's alphabetical sorting makes over a randomly ordered list of names. Priya's slow customer-name lookups are now `index scans` instead of full scans.

The next lesson looks closely at the specific structure most `indexes` actually use internally: the B-tree.
