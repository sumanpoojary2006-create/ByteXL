## Introduction

Every `EXPLAIN` output used so far in this unit was treated as a simple fact: "the plan uses a `sequential scan`" or "the plan uses an `index scan`." Behind that single line of output sits a piece of the database that has quietly done real work before ever touching a single row: the **`query optimizer`**, sometimes called the `query planner`.

Given a SQL query, there is often more than one valid way to actually execute it, scan the whole table or use an index, join two tables in this order or that order, and the optimizer's job is to choose, in advance, which of those valid strategies is likely to be cheapest, before running any of them.

**Definition:** The `query optimizer` evaluates multiple valid ways to execute the same SQL query, estimating the cost of each using statistics about the data rather than actually running every option, and chooses whichever it estimates will be cheapest, which is why the same index can be used in one query and skipped entirely in another depending on how selective the condition actually is.

![Intro visual for inside the query optimizer](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_inside_the_query_optimizer_actual3d_4816b928.png)

## The Same Query, More Than One Valid Plan

A join between two tables can be executed by starting with either table first, and the optimizer has to pick one.

## Source Data Used in This Lesson

Some lessons need a larger dataset to make execution plans or maintenance behavior visible. For those tables, `init.sql` generates the rows instead of listing every row manually.

### Generated `customers` dataset

| Column | Definition in the setup |
| --- | --- |
| `customer_id` | `INTEGER PRIMARY KEY` |
| `customer_name` | `TEXT` |

The setup generates 100 rows, numbered from 1 through 100. This scale is intentional because performance behavior is difficult to observe on a tiny table.

### Generated `orders` dataset

| Column | Definition in the setup |
| --- | --- |
| `order_id` | `INTEGER PRIMARY KEY` |
| `customer_id` | `INTEGER REFERENCES customers(customer_id)` |
| `amount` | `NUMERIC(10, 2)` |

The setup generates 100 rows, numbered from 1 through 100. This scale is intentional because performance behavior is difficult to observe on a tiny table.

## Hands-On Setup: Prepare the Database

```postgresql
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

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajxvt" 
 width="100%"
></iframe>

Expected output:

```
                                             QUERY PLAN
-----------------------------------------------------------------------------------------------------
 Nested Loop  (cost=0.29..344.79 rows=200 width=19)
   ->  Index Scan using customers_pkey on customers c  (cost=0.29..8.31 rows=1 width=15)
         Index Cond: (customer_id = 5)
   ->  Seq Scan on orders o  (cost=0.00..339.00 rows=200 width=11)
         Filter: (customer_id = 5)
```

The optimizer starts from `customers`, the smaller table, uses its `primary key` index to pull out the single matching row for `customer_id = 5`, then, for that one outer row, scans `orders` looking for matches, at this point with no index yet on `orders.customer_id`, so the inner step is a `Seq Scan`. Logically, `customers JOIN orders` and `orders JOIN customers` would produce an identical result, `joining` is not order-dependent for correctness, but they are not necessarily equally fast to execute. Filtering `customers` down to a single row first, then finding that one customer's orders, is a very different amount of work from scanning all 20000 orders first and matching each one against customers.

The optimizer decides this, not the order the tables happen to appear in the written SQL.

![The query optimizer compares multiple valid plans and chooses the cheapest estimate](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_optimizer_compares_candidate_plans.png)

## How the Optimizer Estimates Cost

The optimizer does not actually run each candidate plan to see which is fastest, that would defeat the purpose of planning ahead of time. Instead, it relies on statistics about the data:

- How many rows a table has.
- How many distinct values a column contains.

From these statistics it estimates roughly how many rows each step of a candidate plan would touch, and from that, an estimated cost.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajybg" 
 width="100%"
></iframe>

Expected output:

| relname | n_live_tup |
| --- | --- |
| customers | 100 |
| orders | 20000 |

- `n_live_tup` shows PostgreSQL's tracked estimate of how many rows each table currently holds, one of the statistics the optimizer consults when comparing candidate plans.
- These statistics are not always perfectly up to date; they are refreshed by a background process, and a table that has changed dramatically without a fresh statistics update can occasionally mislead the optimizer into a worse choice than it would otherwise make, a detail worth remembering when a plan looks surprising.

## Why the Optimizer Sometimes Chooses a Sequential Scan on Purpose

It is a common misconception that an index, once created, is always used. The optimizer weighs the estimated cost of every available option, including ignoring a perfectly good index.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajynd" 
 width="100%"
></iframe>

Expected output:

```
                        QUERY PLAN
------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..389.00 rows=20000 width=11)
   Filter: (customer_id > 0)
```

Since every row in `orders` satisfies `customer_id > 0`, using the index would mean reading almost every index entry and then fetching almost every row from the table anyway, extra work compared to just scanning the table directly in one pass. The optimizer correctly recognizes this and chooses a `sequential scan` instead, despite a usable index existing, because for this particular condition, the index would actually be slower, not faster.

![When most rows match, the optimizer may skip the index and choose a sequential scan](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_optimizer_skips_index_when_most_rows_match.png)

## The Optimizer's Job, Summarized

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Step</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parse the query</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understand what tables, columns, and conditions are involved</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generate candidate plans</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different scan methods, different <code>join</code> orders, different <code>join</code> algorithms</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate cost of each candidate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using table and column statistics, not by actually running them</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose the cheapest estimated plan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">This becomes the plan <code>EXPLAIN</code> reports</td>
    </tr>
  </tbody>
</table>

## Your Turn

Run `EXPLAIN` on a query filtering `orders` for `customer_id = 5`, a highly selective condition matching a small fraction of rows, and compare it to the plan for `customer_id > 0` from above, noting in a comment why the optimizer makes a different choice for each.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajyy4" 
 width="100%"
></iframe>

Expected result and verification:

`EXPLAIN SELECT * FROM orders WHERE customer_id = 5;` returns:

```
                                       QUERY PLAN
-----------------------------------------------------------------------------------------
 Index Scan using idx_orders_customer_id on orders  (cost=0.29..8.51 rows=200 width=11)
   Index Cond: (customer_id = 5)
```

- This uses the index, since only a small, precise fraction of rows match (200 out of 20000), while `customer_id > 0` matches nearly the whole table, making a `sequential scan` the genuinely cheaper estimated choice.
- the optimizer is reasoning about estimated rows touched, not simply "an index exists, so use it."

## Conclusion

The `query optimizer` evaluates multiple valid ways to execute the same SQL query, estimating the cost of each using statistics about the data rather than actually running every option, and chooses whichever it estimates will be cheapest, which is why the same index can be used in one query and skipped entirely in another depending on how selective the condition actually is.

Understanding that a plan is a considered estimate, not a fixed rule, is the foundation for reading `EXPLAIN` output with real understanding, the subject of the next lesson.
