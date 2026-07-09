## Introduction

Tanvi's next request from the marketing team is more specific than a merged mailing list:

- First, she needs to know exactly which customers shop both online and in-store, for a special cross-channel loyalty reward.
- Then, separately, she needs to know which online customers have never once shopped in a physical store, for a "visit us in person" campaign targeted only at them.

`UNION` cannot answer either question, since it only combines everything from both sides. What Tanvi needs now are two more set operations: **`INTERSECT`**, which returns only the rows common to both queries, and **`EXCEPT`**, which returns rows from the first query that do not appear in the second.

## Finding Rows Common to Both Queries

The same two customer tables from the `UNION` lesson apply here.

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
SELECT customer_name, email FROM online_customers
INTERSECT
SELECT customer_name, email FROM store_customers;
```

`INTERSECT` compares the two result sets and keeps only the rows that appear in both, matching on every selected column at once. Here, that means a row must have the exact same `customer_name` and `email` in both `online_customers` and `store_customers` to survive. Only Kavya Nair qualifies, since she is the one customer whose full row appears identically in both tables, which is exactly the cross-channel shopper list Tanvi needs for the loyalty reward.

## Finding Rows in One Query but Not the Other

`EXCEPT` (called `MINUS` in some databases, though PostgreSQL and MySQL both use `EXCEPT`) takes the first query's results and removes anything that also appears in the second query's results, keeping only what is left over.

```postgresql with=customers_channels.sql
SELECT customer_name, email FROM online_customers
EXCEPT
SELECT customer_name, email FROM store_customers;
```

This returns Aditi Kulkarni and Rohan Das, the two online customers who do not appear anywhere in `store_customers`, exactly the list the "visit us in person" campaign needs. Order matters with `EXCEPT`: this query starts from `online_customers` and subtracts `store_customers`, which is a different question from starting with `store_customers` and subtracting `online_customers`.

## Why EXCEPT Is Not Symmetric

Reversing the two queries in an `EXCEPT` statement produces a different, not merely reordered, result.

```postgresql with=customers_channels.sql
SELECT customer_name, email FROM store_customers
EXCEPT
SELECT customer_name, email FROM online_customers;
```

This returns Imran Sheikh and Neha Bhatt instead, the store customers who have never shopped online. Unlike `UNION` and `INTERSECT`, where the order of the two queries does not change the final set of rows returned, `EXCEPT` is directional, much like regular subtraction: 5 minus 2 is not the same as 2 minus 5.

## The Same Column Rules Apply

`INTERSECT` and `EXCEPT` follow the identical column requirements covered for `UNION`: both queries must return the same number of columns, in compatible types, in the same order, and the comparison happens across the whole row, not column by column independently.

```postgresql with=customers_channels.sql
SELECT customer_name FROM online_customers
INTERSECT
SELECT customer_name FROM store_customers;
```

Dropping down to just the `customer_name` column changes what counts as a match. If two different customers happened to share the exact same name across the two tables but had different emails, this narrower query would treat them as the same person, while the earlier two-column version would correctly keep them apart. Choosing which columns to include in a set operation is choosing exactly how strict the matching should be.

## INTERSECT and EXCEPT at a Glance

| Operator | Returns | Order-sensitive? |
|---|---|---|
| `INTERSECT` | Rows present in both queries | No |
| `EXCEPT` | Rows in the first query, absent from the second | Yes |

## Your Turn

Tanvi wants to confirm the loyalty reward list a different way: find every store customer who is also an online customer, using `INTERSECT`, but starting the query from `store_customers` this time instead of `online_customers`.

```postgresql with=customers_channels.sql
-- Write your query below
```

If your query is `SELECT customer_name, email FROM store_customers INTERSECT SELECT customer_name, email FROM online_customers;`, it still returns just Kavya Nair, confirming that unlike `EXCEPT`, swapping the order of the two queries in an `INTERSECT` does not change which rows come back.

## Conclusion

`INTERSECT` isolates exactly the rows two queries have in common, and `EXCEPT` isolates the rows one query has that the other does not, with `EXCEPT` alone being sensitive to which query is written first. Tanvi now has a precise cross-channel shopper list and two direction-specific single-channel lists, all built from the same two source tables. Set operations and `joins` can sometimes answer overlapping questions, and knowing which one fits a given situation is worth examining directly.
