## Introduction

A B-tree is an excellent default, but it is not the only shape an `index` can take, and a few specialized variants solve problems a plain B-tree either cannot solve at all or solves less efficiently than a purpose-built alternative. Priya's reporting queries have grown more specific:

- An exact-match lookup that never needs ranges
- A search that always filters on two columns together
- A report that only ever looks at "active" orders out of a much larger table
- A search that needs to match a lowercased version of a name regardless of how it was typed

Each of these has a dedicated `index` type suited to it.

## Hash Indexes: Optimized for Equality Alone

A `hash index`, briefly introduced when file organization strategies were first covered, stores entries by their computed hash value rather than in sorted order, which makes it well suited to exact-match lookups but useless for range queries, since hashing intentionally destroys any sense of order between values.

```postgresql file=index_variants.sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    status TEXT,
    region TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_name, status, region, amount) VALUES
(1, 'Aditi Kulkarni', 'active', 'North', 450.00),
(2, 'Rohan Das', 'completed', 'South', 620.00),
(3, 'Kavya Nair', 'active', 'North', 300.00),
(4, 'Imran Sheikh', 'cancelled', 'East', 900.00),
(5, 'Neha Bhatt', 'active', 'South', 150.00);

CREATE INDEX idx_orders_status_hash ON orders USING hash (status);
```

```postgresql with=index_variants.sql
EXPLAIN SELECT * FROM orders WHERE status = 'active';
```

A `hash index` can serve this equality check, but it would provide no help at all for `WHERE status > 'a'` or `ORDER BY status`, since a `hash index` carries no ordering information whatsoever. In practice, a B-tree `index` handles equality just as well as a `hash index` while also supporting ranges, which is why `hash indexes` see limited use; they matter mainly as a reminder that "sorted" and "searchable by equality" are not the same requirement.

## Composite Indexes: Covering More Than One Column

A `composite index` spans two or more columns together, useful when queries consistently filter on the same combination of columns.

```postgresql with=index_variants.sql
CREATE INDEX idx_orders_status_region ON orders (status, region);

EXPLAIN SELECT * FROM orders WHERE status = 'active' AND region = 'North';
```

`idx_orders_status_region` sorts first by `status`, then by `region` within each `status` value, so a query filtering on both columns together can use the `index` efficiently. Column order in a `composite index` matters: this same `index` can still help a query that filters on `status` alone, since `status` is the leading column, but it offers little help to a query that filters on `region` alone without mentioning `status`, since the `index` is not separately sorted by `region` on its own.

## Partial Indexes: Indexing Only the Rows That Matter

A `partial index` includes only the rows matching a specified condition, which keeps the `index` smaller and faster to maintain when most queries only ever care about a subset of the table.

```postgresql with=index_variants.sql
CREATE INDEX idx_orders_active ON orders (order_id) WHERE status = 'active';

EXPLAIN SELECT * FROM orders WHERE status = 'active' AND order_id = 3;
```

`idx_orders_active` only ever contains rows where `status = 'active'`, entirely excluding completed and cancelled orders. For a system where active orders are a small fraction of a much larger historical table, this keeps the `index` compact and cheap to maintain, since inserting a completed order never touches this `index` at all.

## Expression Indexes: Indexing a Computed Value, Not a Raw Column

An expression `index` `indexes` the result of a function or calculation applied to a column, rather than the column's raw stored value, which matters when queries consistently search using a transformed version of that column.

```postgresql with=index_variants.sql
CREATE INDEX idx_orders_lower_name ON orders (LOWER(customer_name));

EXPLAIN SELECT * FROM orders WHERE LOWER(customer_name) = 'aditi kulkarni';
```

A plain B-tree on `customer_name` would not help a query filtering on `LOWER(customer_name)`, since the `index` is sorted by the raw column value, not the lowercased result of a function applied to it. `idx_orders_lower_name` instead stores the already-lowercased value, letting this exact query use an `index scan`; the same query without an expression `index` would fall back to a sequential scan, computing `LOWER(customer_name)` fresh for every row.

## Index Types at a Glance

| Type | Best for | Limitation |
|---|---|---|
| B-tree (default) | Equality, ranges, sorting | None significant for general use |
| Hash | Equality only | No range or sort support |
| Composite | Queries filtering on the same multiple columns together | Column order matters; less useful for the trailing columns alone |
| Partial | Queries that only ever touch a known subset of rows | Only helps queries matching the partial condition |
| Expression | Queries filtering on a computed or transformed value | Only helps queries using that exact expression |

## Your Turn

Create a `partial index` on `orders` for rows where `status = 'cancelled'`, indexing `order_id`, then confirm with `EXPLAIN` that a query filtering for cancelled order 4 uses it.

```postgresql with=index_variants.sql
-- Write your queries below
```

If you run `CREATE INDEX idx_orders_cancelled ON orders (order_id) WHERE status = 'cancelled';` followed by `EXPLAIN SELECT * FROM orders WHERE status = 'cancelled' AND order_id = 4;`, the plan uses the new `partial index`, which only ever contains the table's cancelled orders.

## Conclusion

`Hash indexes` optimize equality at the cost of range support, `composite indexes` serve queries that filter on the same multiple columns together, `partial indexes` shrink an `index` down to only the rows a query actually cares about, and `expression indexes` make a computed or transformed value searchable, each one a deliberate specialization beyond what a plain B-tree offers. Priya can now match the right `index` shape to each of her report's specific filtering patterns. Having many kinds of `indexes` available raises a new question worth answering directly: how does a query actually make the most of an `index` without still touching the table at all.
