## Introduction

`EXPLAIN` has appeared throughout this unit as a way to check whether a query uses a sequential scan or an `index scan`, but its output carries more detail than just a scan type, and reading that detail precisely is what turns `EXPLAIN` from a yes-or-no check into a genuine diagnostic tool. Priya wants to understand not just what plan the optimizer chose, but how expensive it expects that plan to be, and how it expects the different parts of a query to fit together.

## The Basic Shape of an EXPLAIN Plan

A plan for a simple, single-table query is the easiest starting point.

```postgresql file=explain_demo.sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_id, amount)
SELECT i, (i % 200) + 1, (i * 10.5)::NUMERIC(10,2)
FROM generate_series(1, 20000) AS i;

CREATE INDEX idx_orders_customer_id ON orders (customer_id);
```

```postgresql with=explain_demo.sql
EXPLAIN SELECT * FROM orders WHERE customer_id = 50;
```

A typical line of output looks like `Index Scan using idx_orders_customer_id on orders (cost=0.29..8.51 rows=100 width=15)`:

- **`Index Scan using idx_orders_customer_id`**: names the operation and which `index` it uses.
- **`cost=0.29..8.51`**: gives two numbers, the estimated cost to produce the very first row (0.29) and the estimated total cost to produce every row this step will return (8.51), in the optimizer's own internal cost units, not seconds.
- **`rows=100`**: the optimizer's estimate of how many rows this step will return.
- **`width=15`**: estimates the average size, in bytes, of each returned row.

## Cost Numbers Are Estimates, Not Measured Time

It is worth being precise about what the cost numbers mean: they are the optimizer's own relative units, used to compare candidate plans against each other, not a measurement of actual seconds or milliseconds. A cost of 8.51 for one query and 8.51 for a completely different query does not mean those two queries take the same real time to run; it only means the optimizer estimated a similar relative amount of work for each, under its own internal cost model.

```postgresql with=explain_demo.sql
EXPLAIN SELECT * FROM orders;
```

This plan reports a much higher total cost than the single-customer lookup above, since it has to account for producing all 20000 rows instead of roughly 100, and that relative difference in cost is exactly the kind of comparison `EXPLAIN`'s numbers are meant for: judging one plan as cheaper or more expensive than another, not reading off a literal duration.

## Reading a Plan with Multiple Steps

A query involving a `join` or a filter on top of a scan produces a plan with more than one line, nested to show which step feeds into which.

```postgresql with=explain_demo.sql
EXPLAIN SELECT customer_id, SUM(amount) AS total
FROM orders
WHERE customer_id < 100
GROUP BY customer_id;
```

The plan here shows an outer step, likely `HashAggregate`, wrapping an inner step, likely a `Bitmap Heap Scan` or `Index Scan` on `orders`, indented beneath it. Reading a nested plan means starting from the innermost, most indented step, which runs first and feeds its output upward, and working outward toward the final, least indented step, which represents the last operation applied before the result is returned. The aggregation cannot begin until the filtered rows beneath it have been gathered, which is exactly why it is nested underneath that scan in the output.

## Distinguishing Plan Nodes from Actual Table and Index Names

`EXPLAIN` output mixes generic operation names, `Seq Scan`, `Index Scan`, `HashAggregate`, `Nested Loop`, with the specific table and `index` names involved in this particular query. Learning to separate the two is part of reading a plan fluently: the operation name describes a strategy the database has, applicable across any query, while the table and `index` names describe what that strategy is being applied to in this one specific case.

```postgresql with=explain_demo.sql
EXPLAIN SELECT * FROM orders WHERE customer_id = 50 OR customer_id = 75;
```

This plan may report a `Bitmap Index Scan` feeding into a `Bitmap Heap Scan`, a two-step strategy the optimizer sometimes chooses when a condition matches a moderate number of rows scattered across the table, gathering matching row locations first through the `index`, then fetching them from the table in a more efficient, sorted order, a distinct strategy from either a plain sequential scan or a plain `index scan` covered earlier in this unit.

## Reading EXPLAIN at a Glance

| Part of the output | Meaning |
|---|---|
| Operation name (`Seq Scan`, `Index Scan`, etc.) | The strategy chosen for this step |
| `cost=startup..total` | Estimated relative cost to first row, and to all rows, in internal units |
| `rows=N` | The optimizer's estimated row count for this step |
| `width=N` | Estimated average row size in bytes |
| Indentation | Inner, more indented steps run first and feed outer steps |

## Your Turn

Run `EXPLAIN` on a query that filters `orders` for `amount > 205000.00`, a condition matching very few rows given the data generated above (`amount` tops out at 210000.00 for `order_id = 20000`), and identify the estimated row count and total cost reported for the plan.

```postgresql with=explain_demo.sql
-- Write your query below
```

`EXPLAIN SELECT * FROM orders WHERE amount > 205000.00;` reports a low estimated row count, reflecting how few of the generated rows actually exceed that amount, and a correspondingly low total cost, since the optimizer expects this condition to be highly selective.

## Conclusion

`EXPLAIN` output names the chosen operation for each step of a query, an estimated relative cost, an estimated row count, and an estimated row width, nested to show which steps feed into which, and none of those cost numbers represent actual measured time, only the optimizer's own relative comparison between candidate plans. Priya can now read a plan's structure and estimates with real understanding rather than just checking for the word "Index." Estimates are useful, but they are still just estimates; the next lesson introduces the version of `EXPLAIN` that actually runs the query and reports what really happened.
