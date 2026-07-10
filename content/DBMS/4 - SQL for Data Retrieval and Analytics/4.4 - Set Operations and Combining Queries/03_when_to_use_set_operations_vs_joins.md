## Introduction

Tanvi noticed something while building her cross-channel shopper list: the `INTERSECT` query from the last lesson and a `NOT EXISTS`-based anti `join` from the `joins` chapter both seem to be answering similar "does this row also appear elsewhere" questions, just phrased differently. She now wants to know when to reach for a `join`, when to reach for `EXISTS`, and when to reach for a set operation like `INTERSECT` or `EXCEPT`, since more than one of them can sometimes produce the same answer. The short version is that `joins` combine columns from two tables side by side, while set operations combine entire rows from two queries stacked vertically, and that structural difference is what decides which tool actually fits a given question.

## The Core Difference: Sideways vs. Stacked

A `join` widens a row, pulling in extra columns from a second table for each match. A set operation never adds columns; it only ever stacks, filters, or intersects whole rows that already have the same shape.

```postgresql file=customers_channels.sql
CREATE TABLE online_customers (
    customer_name TEXT,
    email TEXT
);

CREATE TABLE store_customers (
    customer_name TEXT,
    email TEXT
);

INSERT INTO online_customers (customer_name, email) VALUES
('Aditi Kulkarni', 'aditi.k@example.com'),
('Rohan Das', 'rohan.das@example.com'),
('Kavya Nair', 'kavya.nair@example.com');

INSERT INTO store_customers (customer_name, email) VALUES
('Kavya Nair', 'kavya.nair@example.com'),
('Imran Sheikh', 'imran.s@example.com'),
('Neha Bhatt', 'neha.bhatt@example.com');
```

```postgresql with=customers_channels.sql
SELECT o.customer_name, o.email, s.customer_name AS store_side_name
FROM online_customers o
JOIN store_customers s ON o.email = s.email;
```

This `join` produces a row with columns from both tables side by side, `customer_name` and `email` from `online_customers`, plus `store_side_name` from `store_customers`, even though in this data they happen to hold the same value. Compare that to the `INTERSECT` version from the previous lesson, which returns exactly the same two matching people but as a single set of columns, not a widened row. Both queries can answer "who shops in both channels," but only the `join` naturally supports pulling in extra, non-matching columns from either side, such as a loyalty tier stored only on the store side.

## Rewriting an Anti Join as an EXCEPT

The `NOT EXISTS`-based anti `join` from the `joins` chapter and an `EXCEPT`-based query can produce identical results for a single-table, single-condition case like this one.

```postgresql with=customers_channels.sql
SELECT customer_name, email FROM online_customers o
WHERE NOT EXISTS (
    SELECT 1 FROM store_customers s WHERE s.email = o.email
);
```

```postgresql with=customers_channels.sql
SELECT customer_name, email FROM online_customers
EXCEPT
SELECT customer_name, email FROM store_customers;
```

Both return Aditi Kulkarni and Rohan Das. The two read differently, and that difference is a useful guide for which to reach for:

- The `NOT EXISTS` version reads naturally as "keep this row if no match exists," and generalizes easily to conditions involving other tables or columns beyond a simple whole-row comparison.
- The `EXCEPT` version reads naturally as "everything in the first list, minus everything in the second," and is often the more direct choice when the comparison genuinely is a whole-row match between two similarly shaped queries, exactly the situation Tanvi has here.

## When a Join Is the Right Choice

Reach for a `join` whenever the result needs columns from both tables sitting together in one row, especially when one side can legitimately match more than one row on the other side. An order joined to its customer and its restaurant, covered throughout the `joins` chapter, is a clear `join` situation: each order needs its customer's name and its restaurant's name attached, and a customer can have many orders.

## When a Set Operation Is the Right Choice

Reach for a set operation when both queries already return the same shape of row, same columns, same meaning, and the question is really about which rows belong to one group, another group, both, or neither. Tanvi's mailing list, cross-channel shopper list, and channel-exclusive lists are all this kind of question: `online_customers` and `store_customers` are shaped identically, and she cares about set membership across them, not about attaching extra columns from one to the other.

## When EXISTS Is the Right Choice

Reach for `EXISTS` or `NOT EXISTS` when the existence check involves a condition more complex than matching every column, or when a second table is being checked against without any interest in its columns at all, such as "does this customer have at least one order over 1000," a check that a plain set operation between differently shaped tables cannot express.

## Choosing the Right Tool at a Glance

| Situation | Best fit |
|---|---|
| Need columns from both tables in one row | `Join` |
| One side may match many rows on the other | `Join` |
| Two queries return the same shape, comparing whole rows | Set operation (`UNION`, `INTERSECT`, `EXCEPT`) |
| Checking existence with a condition beyond a simple column match | `EXISTS` / `NOT EXISTS` |
| Checking existence against `NULL`-containing columns | `EXISTS` / `NOT EXISTS` over `IN` / `NOT IN` |

## Your Turn

Using the `online_customers` and `store_customers` tables above, find every customer name that appears in exactly one of the two tables, not both, the customers who shop through only one channel. This needs `EXCEPT` run once in each direction, then stitched together with `UNION ALL`.

```postgresql with=customers_channels.sql
-- Write your query below
```

One valid answer is `(SELECT customer_name FROM online_customers EXCEPT SELECT customer_name FROM store_customers) UNION ALL (SELECT customer_name FROM store_customers EXCEPT SELECT customer_name FROM online_customers);`, which returns Aditi Kulkarni, Rohan Das, Imran Sheikh, and Neha Bhatt, everyone who shops through exactly one channel.

## Conclusion

`Joins` widen rows by attaching columns from a matching table, set operations stack or compare whole rows across similarly shaped queries, and `EXISTS` checks for a match without pulling in any columns at all, and recognizing which shape a question actually needs is what decides between them. Tanvi can now choose confidently between a `join`, a set operation, and an existence check depending on what her marketing questions actually require. With retrieval, transformation, aggregation, `joins`, and set operations all covered, more advanced ways of structuring a query, including subqueries and `window functions`, are next.
