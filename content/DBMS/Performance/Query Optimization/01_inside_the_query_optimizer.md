## Introduction

Every `EXPLAIN` output used so far in this unit was treated as a simple fact: "the plan uses a sequential scan" or "the plan uses an `index scan`." Behind that single line of output sits a piece of the database that has quietly done real work before ever touching a single row: the **query optimizer**, sometimes called the query planner. Given a SQL query, there is often more than one valid way to actually execute it, scan the whole table or use an `index`, `join` two tables in this order or that order, and the optimizer's job is to choose, in advance, which of those valid strategies is likely to be cheapest, before running any of them.

## The Same Query, More Than One Valid Plan

A `join` between two tables can be executed by starting with either table first, and the optimizer has to pick one.

```postgresql file=optimizer_demo.sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    amount NUMERIC(10, 2)
);

INSERT INTO customers (customer_id, customer_name)
SELECT i, 'Customer ' || i FROM generate_series(1, 100) AS i;

INSERT INTO orders (order_id, customer_id, amount)
SELECT i, (i % 100) + 1, (i * 10.5)::NUMERIC(10,2)
FROM generate_series(1, 20000) AS i;
```

```postgresql with=optimizer_demo.sql
EXPLAIN SELECT c.customer_name, o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.customer_id = 5;
```

Logically, `customers JOIN orders` and `orders JOIN customers` would produce an identical result, `joining` is not order-dependent for correctness, but they are not necessarily equally fast to execute. Filtering `customers` down to a single row first, then finding that one customer's orders, is a very different amount of work from scanning all 20000 orders first and matching each one against customers. The optimizer decides this, not the order the tables happen to appear in the written SQL.

## How the Optimizer Estimates Cost

The optimizer does not actually run each candidate plan to see which is fastest, that would defeat the purpose of planning ahead of time. Instead, it relies on statistics about the data:

- How many rows a table has.
- How many distinct values a column contains.

From these statistics it estimates roughly how many rows each step of a candidate plan would touch, and from that, an estimated cost.

```postgresql with=optimizer_demo.sql
SELECT relname, n_live_tup FROM pg_stat_user_tables WHERE relname IN ('customers', 'orders');
```

`n_live_tup` shows PostgreSQL's tracked estimate of how many rows each table currently holds, one of the statistics the optimizer consults when comparing candidate plans. These statistics are not always perfectly up to date; they are refreshed by a background process, and a table that has changed dramatically without a fresh statistics update can occasionally mislead the optimizer into a worse choice than it would otherwise make, a detail worth remembering when a plan looks surprising.

## Why the Optimizer Sometimes Chooses a Sequential Scan on Purpose

It is a common misconception that an `index`, once created, is always used. The optimizer weighs the estimated cost of every available option, including ignoring a perfectly good `index`.

```postgresql with=optimizer_demo.sql
CREATE INDEX idx_orders_customer_id ON orders (customer_id);

EXPLAIN SELECT * FROM orders WHERE customer_id > 0;
```

Since every row in `orders` satisfies `customer_id > 0`, using the `index` would mean reading almost every `index` entry and then fetching almost every row from the table anyway, extra work compared to just scanning the table directly in one pass. The optimizer correctly recognizes this and chooses a `sequential scan` instead, despite a usable `index` existing, because for this particular condition, the `index` would actually be slower, not faster.

## The Optimizer's Job, Summarized

| Step | What happens |
|---|---|
| Parse the query | Understand what tables, columns, and conditions are involved |
| Generate candidate plans | Different scan methods, different `join` orders, different `join` algorithms |
| Estimate cost of each candidate | Using table and column statistics, not by actually running them |
| Choose the cheapest estimated plan | This becomes the plan `EXPLAIN` reports |

## Your Turn

Run `EXPLAIN` on a query filtering `orders` for `customer_id = 5`, a highly selective condition matching a small fraction of rows, and compare it to the plan for `customer_id > 0` from above, noting in a comment why the optimizer makes a different choice for each.

```postgresql with=optimizer_demo.sql
-- Write your query and comment below
```

`EXPLAIN SELECT * FROM orders WHERE customer_id = 5;` uses the `index`, since only a small, precise fraction of rows match, while `customer_id > 0` matches nearly the whole table, making a `sequential scan` the genuinely cheaper estimated choice; the optimizer is reasoning about estimated rows touched, not simply "an `index` exists, so use it."

## Conclusion

The query optimizer evaluates multiple valid ways to execute the same SQL query, estimating the cost of each using statistics about the data rather than actually running every option, and chooses whichever it estimates will be cheapest, which is why the same `index` can be used in one query and skipped entirely in another depending on how selective the condition actually is. Understanding that a plan is a considered estimate, not a fixed rule, is the foundation for reading `EXPLAIN` output with real understanding, the subject of the next lesson.
