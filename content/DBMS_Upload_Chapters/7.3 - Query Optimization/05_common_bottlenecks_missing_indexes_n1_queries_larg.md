## Introduction

Most real-world performance problems trace back to a small handful of recurring patterns, not exotic, one-off causes. With scans, indexes, plans, and join algorithms all covered individually across this unit, this lesson names the three bottlenecks Priya is most likely to actually encounter in practice:

- A missing index on a genuinely selective column
- An application pattern called the `N+1 query` problem
- Large, unnecessary scans hiding inside an otherwise reasonable-looking query

**Definition:** A missing index on a selective column, the `N+1 query` pattern hiding in application code, and a function or cast silently defeating an otherwise-useful index are three of the most common ways a real system slows down, and all three are diagnosable with the same tools covered across this unit: `EXPLAIN`, `EXPLAIN ANALYZE`, and a clear understanding of what each plan node actually means.

![Intro visual for common bottlenecks missing indexes n1 queries larg](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_intro_common_bottlenecks_missing_indexes_n1_queries_la.png)

## Bottleneck One: A Missing Index on a Selective Column

The clearest, most mechanical bottleneck is a filter condition on a column with no supporting index, forcing a `sequential scan` even when very few rows actually match.

## Source Data Used in This Lesson

Some lessons need a larger dataset to make execution plans or maintenance behavior visible. For those tables, `init.sql` generates the rows instead of listing every row manually.

### Generated `orders` dataset

| Column | Definition in the setup |
| --- | --- |
| `order_id` | `INTEGER PRIMARY KEY` |
| `customer_id` | `INTEGER` |
| `status` | `TEXT` |
| `amount` | `NUMERIC(10, 2)` |

The setup generates 50,000 rows, numbered from 1 through 50000. This scale is intentional because performance behavior is difficult to observe on a tiny table.

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    status TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_id, status, amount)
SELECT i, (i % 5000) + 1,
       CASE WHEN i % 1000 = 0 THEN 'flagged' ELSE 'normal' END,
       (i * 10.5)::NUMERIC(10,2)
FROM generate_series(1, 50000) AS i;
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkak4t4" 
 width="100%"
></iframe>

Expected output (before the index exists):

```
                                                    QUERY PLAN
-------------------------------------------------------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..1035.00 rows=50 width=23) (actual time=0.017..8.204 rows=50 loops=1)
   Filter: (status = 'flagged'::text)
   Rows Removed by Filter: 49950
 Planning Time: 0.078 ms
 Execution Time: 8.231 ms
```

Only about 1 in 1000 rows are flagged, a highly selective condition, but with no index on `status`, the plan is forced into a `sequential scan` of all 50000 rows to find the roughly 50 that match. This is the most straightforward bottleneck to diagnose, `EXPLAIN` clearly shows a `sequential scan`, and the fix, an index, is exactly what the previous chapter covered.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkak53u" 
 width="100%"
></iframe>

Expected output (after the index exists):

```
                                                         QUERY PLAN
---------------------------------------------------------------------------------------------------------------------------
 Index Scan using idx_orders_status on orders  (cost=0.29..12.80 rows=50 width=23) (actual time=0.020..0.041 rows=50 loops=1)
   Index Cond: (status = 'flagged'::text)
 Planning Time: 0.084 ms
 Execution Time: 0.062 ms
```

The plan switches to an `index scan`, and the actual measured time drops from 8.231 ms to 0.062 ms, well over 100x faster, precisely the diagnostic workflow, run `EXPLAIN ANALYZE`, spot a `sequential scan` on a selective filter, add an index, confirm the plan changes.

![A missing index on a selective filter forces a scan until an index shortcut is added](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_missing_index_selective_filter_bottleneck.png)

## Bottleneck Two: The N+1 Query Problem

This bottleneck lives in application code, not in any single SQL statement. It happens when code first fetches a list of parent rows with one query, then loops over that list, running one additional query per item to fetch related data, N extra queries for N parent rows, instead of one query that fetches everything together.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkak5cy" 
 width="100%"
></iframe>

Expected output for the first query (`GROUP BY` with no `ORDER BY` returns whichever 5 groups the plan happens to produce first, so the exact `customer_id` values can vary between runs; this is one representative result):

| customer_id |
| --- |
| 3427 |
| 891 |
| 4102 |
| 15 |
| 2650 |

Each of those 5 `customer_id`s then triggers one more round trip in the loop, `SELECT * FROM orders WHERE customer_id = 3427;`, then the same for 891, 4102, 15, and 2650, six queries total for five customers.

The fix is almost always the same one covered throughout the joins chapter: replace the loop of individual queries with a single query that joins or filters for everything needed at once.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkak5rq" 
 width="100%"
></iframe>

Expected output (using the same 5 `customer_id`s from above; each customer has 10 matching `orders` rows, since 50000 rows are spread across 5000 customers, so this returns 50 rows total, shown here truncated to the first few per customer):

| customer_id | order_id | amount |
| --- | --- | --- |
| 3427 | 3426 | 35973.00 |
| 3427 | 8426 | 88473.00 |
| 3427 | 13426 | 140973.00 |
| 891 | 890 | 9345.00 |
| 891 | 5890 | 61845.00 |
| ... | ... | ... |

This single query retrieves the exact same data the 6-query loop above would have gathered. It does that as one round trip instead of six. The gap between the two approaches only widens as the number of parent rows grows.

That is why N+1 is such a common, costly bottleneck in real applications built on top of an object-relational mapper or any code that fetches a list and then loops.

![The N+1 query problem makes one query plus many repeated child queries](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_n_plus_one_queries_many_round_trips.png)

## Bottleneck Three: Large Scans Hiding Inside a Reasonable-Looking Query

Sometimes a query looks selective at a glance but is not, because a function or a type mismatch on the filtered column silently defeats an otherwise-present index, forcing a full scan the same way a missing index would.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkak629" 
 width="100%"
></iframe>

Expected output:

```
                            QUERY PLAN
-------------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..1160.00 rows=250 width=23)
   Filter: ((amount)::text = '525.00'::text)
```

Casting `amount` to text before comparing defeats `idx_orders_amount`, since the index is built on the numeric column's own sorted values, not on a text-converted version of them, forcing a `sequential scan` despite an index technically existing on the underlying column. This is a subtle bottleneck precisely because the query author may not realize the cast is even happening, especially if it was introduced indirectly through application code building the condition dynamically.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkak6dx" 
 width="100%"
></iframe>

Expected output:

```
                                   QUERY PLAN
---------------------------------------------------------------------------------
 Index Scan using idx_orders_amount on orders  (cost=0.29..8.31 rows=1 width=23)
   Index Cond: (amount = 525.00)
```

Removing the cast and comparing directly against the numeric value restores the `index scan`, confirming the cast, not the index itself, was the actual bottleneck.

![A cast or function around an indexed column can block the existing index](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_cast_or_function_defeats_index.png)

## Common Bottlenecks at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Bottleneck</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it shows up</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Fix</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing <code>index</code> on a selective filter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>EXPLAIN</code> shows a sequential scan on a highly selective condition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add an appropriate <code>index</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">N+1 queries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One query, then N more in a loop, visible in application logs or query counts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace the loop with a single query using a <code>join</code> or <code>IN</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A function or cast defeating an <code>index</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>EXPLAIN</code> shows a sequential scan despite a relevant <code>index</code> existing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove the cast/function, or build an expression <code>index</code> matching it</td>
    </tr>
  </tbody>
</table>

## Your Turn

Check whether filtering `orders` on `customer_id = 42` uses an index, given there is currently no index on `customer_id`, then create one and confirm the plan changes.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkak6pq" 
 width="100%"
></iframe>

Expected result and verification:

`EXPLAIN SELECT * FROM orders WHERE customer_id = 42;` shows a `sequential scan` before an index exists:

```
                            QUERY PLAN
-------------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..1035.00 rows=10 width=23)
   Filter: (customer_id = 42)
```

After running `CREATE INDEX idx_orders_customer_id ON orders (customer_id);`, the same `EXPLAIN` shows an `index scan` instead:

```
                                     QUERY PLAN
-------------------------------------------------------------------------------------
 Index Scan using idx_orders_customer_id on orders  (cost=0.29..9.35 rows=10 width=23)
   Index Cond: (customer_id = 42)
```

the same missing-index bottleneck pattern from earlier in this lesson.

## Conclusion

A missing index on a selective column, the `N+1 query` pattern hiding in application code, and a function or cast silently defeating an otherwise-useful index are three of the most common ways a real system slows down, and all three are diagnosable with the same tools covered across this unit: `EXPLAIN`, `EXPLAIN ANALYZE`, and a clear understanding of what each plan node actually means.

Priya now has a checklist of the first places to look whenever a report starts running slower than expected. The final lesson in this unit turns these individual diagnoses into a repeatable process for tuning a query end to end.
