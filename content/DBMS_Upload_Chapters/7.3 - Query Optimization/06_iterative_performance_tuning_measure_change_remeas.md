## Introduction

Every technique covered in this unit, storage layout, indexes, `EXPLAIN`, join algorithms, and common bottlenecks, is a piece of a single repeatable process, not a checklist to apply once and forget. Real performance tuning is iterative: measure how a query actually performs, make one deliberate change, measure again to confirm that change actually helped, and repeat, rather than guessing at several changes at once and hoping the combination works.

This final lesson walks through that full loop, start to finish, on one query.

**Definition:** Iterative tuning, measure with `EXPLAIN ANALYZE`, make one deliberate change, re-measure to confirm it actually helped, and repeat, is the discipline that ties every technique in this unit together into a real, evidence-based process, rather than a collection of tricks applied on faith.

![Intro visual for iterative performance tuning measure change remeas](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_intro_iterative_performance_tuning_measure_change_reme_clean_b3787e9d.png)

## Step One: Measure the Starting Point

Before changing anything, the first step is always establishing an honest baseline with `EXPLAIN ANALYZE`, the actual-execution tool covered earlier in this chapter.

## Source Data Used in This Lesson

Some lessons need a larger dataset to make execution plans or maintenance behavior visible. For those tables, `init.sql` generates the rows instead of listing every row manually.

### Generated `orders` dataset

| Column | Definition in the setup |
| --- | --- |
| `order_id` | `INTEGER PRIMARY KEY` |
| `customer_id` | `INTEGER` |
| `status` | `TEXT` |
| `amount` | `NUMERIC(10, 2)` |
| `order_date` | `DATE` |

The setup generates 60,000 rows, numbered from 1 through 60000. This scale is intentional because performance behavior is difficult to observe on a tiny table.

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    status TEXT,
    amount NUMERIC(10, 2),
    order_date DATE
);

INSERT INTO orders (order_id, customer_id, status, amount, order_date)
SELECT i, (i % 8000) + 1,
       CASE WHEN i % 500 = 0 THEN 'refunded' ELSE 'completed' END,
       (i * 7.25)::NUMERIC(10,2),
       DATE '2025-01-01' + (i % 365)
FROM generate_series(1, 60000) AS i;
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajz9q" 
 width="100%"
></iframe>

Expected output (baseline, before any new index):

```
                                                            QUERY PLAN
-----------------------------------------------------------------------------------------------------------------------------
 Sort  (cost=1245.32..1245.48 rows=64 width=36) (actual time=38.912..38.921 rows=70 loops=1)
   Sort Key: (sum(amount)) DESC
   Sort Method: quicksort  Memory: 27kB
   ->  HashAggregate  (cost=1241.50..1242.30 rows=64 width=36) (actual time=38.782..38.812 rows=70 loops=1)
         Group Key: customer_id
         ->  Seq Scan on orders  (cost=0.00..1235.00 rows=75 width=11) (actual time=0.021..37.664 rows=70 loops=1)
               Filter: ((status = 'refunded'::text) AND (order_date > '2025-06-01'::date))
               Rows Removed by Filter: 59930
 Planning Time: 0.184 ms
 Execution Time: 39.021 ms
```

This baseline plan, with no supporting index on either `status` or `order_date`, shows a `Seq Scan` across all 60000 rows, discarding 59930 of them, before filtering down to the small refunded, recent subset (70 rows) the query actually cares about. Recording this baseline's actual time, 39.021 ms, is essential, since without it, there is no way to later confirm whether a change genuinely helped or made no real difference.

![Iterative tuning starts by measuring a baseline before making changes](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/13_iterative_tuning_measure_change_remeasure.png)

## Step Two: Make One Deliberate Change

Rather than adding several indexes at once, the disciplined approach is one change at a time, so its individual effect can be measured cleanly. A `composite index` matching both filter columns together, the technique covered in the indexes chapter, is a reasonable first attempt here.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajzjm" 
 width="100%"
></iframe>

Expected observation: PostgreSQL confirms that the index was created. The command does not return business rows; its effect is verified by rerunning the related query or `EXPLAIN` statement.

This single, targeted change is the entire first iteration, nothing else about the query or the schema is touched yet, keeping the next measurement a clean, isolated comparison against the baseline.

## Step Three: Re-measure and Compare

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkak24x" 
 width="100%"
></iframe>

Expected output (after adding `idx_orders_status_date`):

```
                                                                 QUERY PLAN
------------------------------------------------------------------------------------------------------------------------------------------
 Sort  (cost=98.47..98.63 rows=64 width=36) (actual time=1.203..1.211 rows=70 loops=1)
   Sort Key: (sum(amount)) DESC
   Sort Method: quicksort  Memory: 27kB
   ->  HashAggregate  (cost=94.60..95.40 rows=64 width=36) (actual time=1.132..1.162 rows=70 loops=1)
         Group Key: customer_id
         ->  Index Scan using idx_orders_status_date on orders  (cost=0.29..94.20 rows=70 width=11) (actual time=0.019..1.041 rows=70 loops=1)
               Index Cond: ((status = 'refunded'::text) AND (order_date > '2025-06-01'::date))
 Planning Time: 0.121 ms
 Execution Time: 1.298 ms
```

Comparing this plan's actual time directly against the baseline's is the entire point of the exercise:

- The plan now shows an `Index Scan` on `idx_orders_status_date` instead of a `Seq Scan`, and the total `Execution Time` dropped from 39.021 ms to 1.298 ms, roughly a 30x improvement, confirming the change as a real improvement, not just a plausible-sounding guess.
- Had the actual time barely moved, or had the optimizer still chosen a `sequential scan` anyway, perhaps because the filtered rows are not selective enough for the index to be worth using, that would be equally important information, and it would mean the next iteration should try a different change rather than assuming this one worked.

![Compare baseline time with after-change time to prove whether tuning helped](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/14_baseline_vs_after_change_actual_time.png)

## Step Four: Repeat, One Change at a Time

If the first change helped but the query is still slower than needed, the loop continues: identify the next likely bottleneck from what `EXPLAIN ANALYZE` now shows, make one more targeted change, and measure again.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkak2fg" 
 width="100%"
></iframe>

Expected output:

```
                                                                  QUERY PLAN
-------------------------------------------------------------------------------------------------------------------------------------------
 Limit  (cost=98.47..98.49 rows=10 width=36) (actual time=1.198..1.202 rows=10 loops=1)
   ->  Sort  (cost=98.47..98.63 rows=64 width=36) (actual time=1.196..1.199 rows=10 loops=1)
         Sort Key: (sum(amount)) DESC
         Sort Method: top-N heapsort  Memory: 25kB
         ->  HashAggregate  (cost=94.60..95.40 rows=64 width=36) (actual time=1.129..1.158 rows=70 loops=1)
               Group Key: customer_id
               ->  Index Scan using idx_orders_status_date on orders  (cost=0.29..94.20 rows=70 width=11) (actual time=0.018..1.038 rows=70 loops=1)
                     Index Cond: ((status = 'refunded'::text) AND (order_date > '2025-06-01'::date))
 Planning Time: 0.118 ms
 Execution Time: 1.241 ms
```

Adding `LIMIT 10` shaves the `Sort` step down to a cheaper `top-N heapsort` and trims total `Execution Time` from 1.298 ms to 1.241 ms, a small but real and separately attributable gain on top of the index change. If the actual business need only ever wants the top 10 customers by refund total, adding `LIMIT 10` is itself a legitimate next iteration, changing the query rather than the schema, and it is worth re-measuring separately from the `indexing` change to see how much it alone contributes, keeping each iteration's effect distinct and attributable.

## Why This Discipline Matters More Than Any Single Technique

The specific techniques covered across this unit, storage awareness, `indexing`, reading plans, understanding join algorithms, are all just tools available during this loop. A tuning session that skips measurement and jumps straight to "add indexes everywhere" risks the over-indexing cost covered earlier in this unit, paying for write overhead on indexes that never actually helped the query they were added for.

Measuring first, changing one thing, and measuring again is what turns tuning from guesswork into an evidence-based process with a clear, demonstrable outcome at every step.

## The Iterative Tuning Loop at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Step</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1. Measure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run <code>EXPLAIN ANALYZE</code> to get an honest actual-time baseline</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2. Change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make exactly one deliberate, targeted change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3. Re-measure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run <code>EXPLAIN ANALYZE</code> again, compare actual time against the baseline</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4. Repeat</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">If still not fast enough, identify the next bottleneck and repeat from step 2</td>
    </tr>
  </tbody>
</table>

## Your Turn

Using the `orders` table above, measure the baseline for a query filtering `WHERE customer_id = 4000`, add an appropriate index, and re-measure to confirm the improvement, following the same measure-change-re-measure discipline covered in this lesson.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkak2sc" 
 width="100%"
></iframe>

Expected result and verification:

Running `EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 4000;` first establishes a baseline:

```
                                              QUERY PLAN
--------------------------------------------------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..1235.00 rows=8 width=27) (actual time=0.028..9.812 rows=8 loops=1)
   Filter: (customer_id = 4000)
   Rows Removed by Filter: 59992
 Planning Time: 0.084 ms
 Execution Time: 9.841 ms
```

Then `CREATE INDEX idx_orders_customer_id ON orders (customer_id);` followed by the same `EXPLAIN ANALYZE` a second time confirms the switch to an `index scan` and a measurably lower actual time:

```
                                                       QUERY PLAN
--------------------------------------------------------------------------------------------------------------------
 Index Scan using idx_orders_customer_id on orders  (cost=0.29..8.51 rows=8 width=27) (actual time=0.021..0.034 rows=8 loops=1)
   Index Cond: (customer_id = 4000)
 Planning Time: 0.076 ms
 Execution Time: 0.061 ms
```

Execution Time drops from 9.841 ms to 0.061 ms, well over 100x faster, the complete measure-change-re-measure loop applied end to end.

## Conclusion

Iterative tuning, measure with `EXPLAIN ANALYZE`, make one deliberate change, re-measure to confirm it actually helped, and repeat, is the discipline that ties every technique in this unit together into a real, evidence-based process, rather than a collection of tricks applied on faith. Priya now has a complete, repeatable method for taking any slow query from a first honest measurement to a confirmed improvement.

With storage, `indexing`, and query optimization all covered, the course moves next into the practical work of running a database in a real, production environment.
