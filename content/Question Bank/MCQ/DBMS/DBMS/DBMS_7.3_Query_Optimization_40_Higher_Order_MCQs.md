# DBMS 7.3: Query Optimization — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Performance
- **Chapter:** Query Optimization
- **Scope:** Inside the Query Optimizer; Reading EXPLAIN; Reading EXPLAIN ANALYZE; Join Algorithms; Common Bottlenecks; Iterative Performance Tuning
- **SQL dialect:** PostgreSQL
- **Format:** Four plausible options with exactly one best answer
- **Is Curriculum Based:** No
- **Coverage rule:** Questions 1–10 collectively cover all six chapter subtopics.
- **Design standard:** Every diagnosis depends on supplied SQL, plan evidence, data distribution, or application behaviour.
- **Answer-quality controls:** A/B/C/D are each correct exactly 10 times; no answer letter occurs more than twice consecutively.

---

## Questions

### 1. The index that lost the cost contest

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Inside the Query Optimizer  
**Is Curriculum Based:** No  
**Assessment type:** Comparing candidate plans

A support dashboard queries a 20,000-row `orders` table. Every row has `customer_id > 0`, and an index exists on `customer_id`.

```sql
SELECT * FROM orders WHERE customer_id > 0;
```

The optimizer estimates these valid plans:

| Candidate | Estimated total cost |
|---|---:|
| Sequential scan | 389 |
| Index scan plus table-row fetches | 1,146 |

Which review note correctly explains the selected sequential scan?

A. PostgreSQL ignores an index whenever a predicate uses `>`.  
B. An index can be used only when the query returns one row.  
C. The optimizer estimates that one table sweep costs less than fetching nearly every row through the index.  
D. The optimizer executes both candidates and retains the first to finish.

### 2. A preview before the overnight report

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN  
**Is Curriculum Based:** No  
**Assessment type:** Completing diagnostic SQL

A DBA wants to inspect the intended plan for an expensive year-end report without running the report. Complete the missing prefix.

```sql
_____ 
SELECT customer_id, SUM(amount)
FROM orders
GROUP BY customer_id;
```

A. `EXPLAIN`  
B. `ANALYZE orders;`  
C. `EXPLAIN ANALYZE`  
D. `BEGIN;`

### 3. The estimate needs a reality check

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN ANALYZE  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the appropriate diagnostic

An `EXPLAIN` plan estimates 200 matching rows, but the operations team suspects a newly imported customer now owns most orders. They need both the original estimate and the real row count for this read-only query.

Which statement supplies that evidence?

A. `ANALYZE SELECT * FROM orders WHERE customer_id = 1;`  
B. `EXPLAIN SELECT * FROM orders WHERE customer_id = 1;`  
C. `SELECT EXPLAIN(*) FROM orders WHERE customer_id = 1;`  
D. `EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 1;`

### 4. Three customers drive the join

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Join Algorithms  
**Is Curriculum Based:** No  
**Assessment type:** Predicting a join strategy

`customers` has 5,000 rows and `orders` has 20,000. Both join columns are indexed. A report narrows the customer side to IDs 1–3 before joining.

Which physical strategy best fits this evidence?

A. Hash all 20,000 orders before reading the three customers.  
B. Use a nested loop and make indexed order lookups for three outer rows.  
C. Sequentially rescan all orders once for every customer in the table.  
D. Sort both complete tables even though targeted lookups are available.

### 5. Fifty alerts hidden among fifty thousand orders

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Common Bottlenecks  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest repair

The fraud page searches a 50,000-row table for the 50 orders whose `status` is `'flagged'`.

```text
Seq Scan on orders (actual rows=50)
  Filter: status = 'flagged'
  Rows Removed by Filter: 49950
```

No index exists on `status`. Which targeted change addresses the demonstrated bottleneck?

A. Remove the filter and let the application discard normal orders.  
B. Add `ORDER BY status` so flagged rows are displayed first.  
C. Replace the equality comparison with `LIKE '%flagged%'`.  
D. Create an index on `orders(status)`, then measure the query again.

### 6. A tuning experiment that can be defended

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Iterative Performance Tuning  
**Is Curriculum Based:** No  
**Assessment type:** Sequencing a tuning workflow

A refund report is slow. Four engineers propose workflows. Which one produces evidence that a particular change caused an improvement?

A. Add three indexes, restart PostgreSQL, and compare user impressions.  
B. Rewrite the report and accept the plan with the lowest estimated row count.  
C. Record `EXPLAIN ANALYZE`, make one targeted change, rerun it, and compare actual execution times.  
D. Create every plausible index and retain them unless an error occurs.

### 7. Statistics from before the bulk import

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Inside the Query Optimizer  
**Is Curriculum Based:** No  
**Assessment type:** Completing a corrective action

After ten million rows are bulk-loaded, this query receives a poor plan. The plan estimates 80 matches, while `EXPLAIN ANALYZE` observes 1,900,000. No statistics refresh followed the import.

Which smallest first action directly repairs the optimizer's information?

A. Run `ANALYZE` on the affected table and inspect the plan again.  
B. Disable sequential scans for the whole database.  
C. Replace the query with several smaller queries.  
D. Force one join algorithm for every session.

### 8. Reading a plan from its leaves

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN  
**Is Curriculum Based:** No  
**Assessment type:** Tracing plan flow

A booking report has this plan:

```text
Hash Join
  Hash Cond: (b.hotel_id = h.hotel_id)
  -> Seq Scan on bookings b
  -> Hash
       -> Seq Scan on hotels h
```

Which description follows the plan tree correctly?

A. The hash join produces rows first, which are then scanned by both children.  
B. `hotels` is scanned and hashed; `bookings` is scanned and probes that hash.  
C. The indentation means `bookings` runs only if the hotel scan returns no rows.  
D. Both scans are alternative plans, so only one of them will execute.

### 9. One inner lookup, repeated 400 times

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN ANALYZE  
**Is Curriculum Based:** No  
**Assessment type:** Calculating repeated work

An inner node reports:

```text
Index Scan on orders
  (actual time=0.010..0.250 rows=6 loops=400)
```

PostgreSQL reports actual time and rows as averages per loop. Which approximation best describes this node's accumulated work?

A. About 0.25 ms and 6 rows in total.  
B. About 400 ms and 2,400 rows in total.  
C. About 1.5 ms and 406 rows in total.  
D. About 100 ms and 2,400 rows in total.

### 10. The latency is outside each individual plan

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Common Bottlenecks  
**Is Curriculum Based:** No  
**Assessment type:** Identifying a distributed-query defect

An application first retrieves 80 customers. It then executes one indexed order query per customer. Every child query takes only 1 ms in PostgreSQL, but each database round trip adds network latency.

Which change attacks the pattern rather than merely speeding up each child query?

A. Fetch the required customer–order data with one join or set-based query.  
B. Replace each child query's index scan with a sequential scan.  
C. Run plain `EXPLAIN` on all 81 statements during every request.  
D. Increase the number of parent rows returned by the first query.

### 11. Distinguishing estimates from measurements

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN ANALYZE  
**Is Curriculum Based:** No  
**Assessment type:** Interpreting plan annotations

Consider one plan line:

```text
Seq Scan on orders
  (cost=0.00..389.00 rows=15288 width=15)
  (actual time=0.014..3.912 rows=15000 loops=1)
```

Which pair compares like with like?

A. Estimated milliseconds `389.00` versus actual rows `15000`.  
B. Estimated rows `15288` versus actual rows `15000`.  
C. Estimated bytes `15` versus actual milliseconds `3.912`.  
D. Estimated loops `1` versus actual startup cost `0.00`.

### 12. Testing a write plan without retaining the test update

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN ANALYZE  
**Is Curriculum Based:** No  
**Assessment type:** Completing a safe diagnostic

A DBA must measure an `UPDATE` plan but preserve all current values. Which script both executes the measured plan and discards its data changes?

A. `EXPLAIN UPDATE orders SET amount=amount*1.05; COMMIT;`  
B. `ANALYZE orders; UPDATE orders SET amount=amount*1.05;`  
C. `BEGIN; EXPLAIN UPDATE orders SET amount=amount*1.05; ROLLBACK;`  
D. `BEGIN; EXPLAIN ANALYZE UPDATE orders SET amount=amount*1.05; ROLLBACK;`

### 13. An index exists, but the expression bypasses it

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Common Bottlenecks  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest query repair

`orders.amount` is numeric and indexed. The current predicate produces a sequential scan:

```sql
WHERE amount::TEXT = '525.00'
```

The application needs the numeric amount 525.00. Which replacement lets the existing numeric index become useful without changing the requested rows?

A. `WHERE amount = 525.00`  
B. `WHERE amount::TEXT LIKE '%525.00%'`  
C. `WHERE CAST(amount AS TEXT) = CAST(525.00 AS TEXT)`  
D. `WHERE amount::TEXT >= '525.00'`

### 14. Two large unsorted inputs

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Join Algorithms  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the appropriate structure

A join must match all 20,000 orders with all 5,000 customers by `customer_id`. Neither input is filtered, and no useful sort order is required in the result.

Which strategy is the most natural candidate from the chapter?

A. Nested loop with a full inner scan for every outer row.  
B. Hash join: hash one side, then scan and probe with the other.  
C. Merge join after discarding the join key from both inputs.  
D. Run one child query for every customer from application code.

### 15. The cost numbers are not a stopwatch

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN  
**Is Curriculum Based:** No  
**Assessment type:** Correcting a plan-reading claim

A trainee says `cost=0.29..8.51` proves the node will finish in 8.51 milliseconds.

Which correction should the reviewer make?

A. Both values are estimated row counts, not durations.  
B. The first value is bytes and the second is disk blocks.  
C. They are optimizer cost units—startup then total—not measured milliseconds.  
D. They are minimum and maximum execution times from earlier runs.

### 16. The second experiment changes two variables

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Iterative Performance Tuning  
**Is Curriculum Based:** No  
**Assessment type:** Spotting an invalid comparison

Baseline execution time is 39 ms. Before the next measurement, an engineer adds a composite index and also adds `LIMIT 10`. The new time is 1.2 ms.

What conclusion is justified?

A. The index alone produced the entire 37.8 ms improvement.  
B. `LIMIT 10` alone produced the entire 37.8 ms improvement.  
C. Neither change helped because the SQL text changed.  
D. The combination helped, but this experiment cannot attribute the gain to either change alone.

### 17. A plan width that affects data volume

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN  
**Is Curriculum Based:** No  
**Assessment type:** Interpreting plan metadata

Two candidate scans each estimate 10,000 rows. Plan X has `width=12`; Plan Y has `width=240`.

What does this evidence mean?

A. Plan Y estimates wider output rows, so downstream nodes may handle more bytes.  
B. Plan Y estimates 240 times as many rows as Plan X.  
C. Plan X has an actual execution time of 12 milliseconds.  
D. Plan Y must use 240 indexes to produce its result.

### 18. A merge join loses its main advantage

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Join Algorithms  
**Is Curriculum Based:** No  
**Assessment type:** Comparing implementation suitability

Version A can read both join inputs in `customer_id` order from indexes. Version B has the same rows but must sort both complete inputs before merging.

Which assessment is best?

A. Version B is always faster because sorting removes duplicates.  
B. The merge strategy is more naturally attractive in A because both streams already arrive ordered.  
C. The versions must have identical cost because they return identical rows.  
D. Version A cannot use merge join because indexes prevent sorted output.

### 19. An estimate that is close enough to trust provisionally

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN ANALYZE  
**Is Curriculum Based:** No  
**Assessment type:** Evaluating estimate quality

Three nodes show estimated and actual rows:

| Node | Estimated | Actual |
|---|---:|---:|
| X | 12,000 | 11,850 |
| Y | 50 | 8,000 |
| Z | 900 | 9 |

Which node has the closest row-count estimate?

A. Y, because 50 is the smallest estimate.  
B. Z, because 9 is the smallest actual count.  
C. X, because 12,000 and 11,850 are proportionally close.  
D. All three estimates are equally accurate.

### 20. The optimizer and the SQL result

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Inside the Query Optimizer  
**Is Curriculum Based:** No  
**Assessment type:** Deciding semantic equivalence

The optimizer considers a hash join and a nested-loop join for the same inner join. Both are valid candidate plans.

Which statement must be true for either candidate to be chosen?

A. It must use the same indexes as the other candidate.  
B. It must have the same internal cost number as the other candidate.  
C. It must visit the physical rows in the same order.  
D. It must preserve the SQL query's required result even though its execution method differs.

### 21. Counting the queries behind a page

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Common Bottlenecks  
**Is Curriculum Based:** No  
**Assessment type:** Tracing application behaviour

A page runs one query to fetch 25 departments. Inside a loop, it runs one employee query for each department.

How many database queries does one page request issue?

A. 26  
B. 25  
C. 50  
D. 625

### 22. Choosing where to look first

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Common Bottlenecks  
**Is Curriculum Based:** No  
**Assessment type:** Prioritizing evidence

A selective lookup is slow. The plan shows an index scan returning 2 rows in 0.04 ms, while application logs show the statement repeated 2,000 times per web request.

Which diagnosis best matches both sources?

A. The index scan should be replaced with a sequential scan.  
B. The dominant defect is the repeated-query pattern, not one slow execution.  
C. The estimated `width` must be causing all network latency.  
D. The two returned rows prove that PostgreSQL statistics are stale.

### 23. Filling the missing plan-reading calculation

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN ANALYZE  
**Is Curriculum Based:** No  
**Assessment type:** Completing a calculation

An inner nested-loop node reports `actual time=0.02..1.40 rows=3 loops=50`. Complete the review note:

> The displayed 1.40 ms is an average per loop, so the approximate accumulated total time is _____.

A. 1.40 ms  
B. 3.00 ms  
C. 70 ms  
D. 150 ms

### 24. A sequential scan that should not be “repaired”

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Inside the Query Optimizer  
**Is Curriculum Based:** No  
**Assessment type:** Rejecting a false defect

`status='completed'` matches 59,880 of 60,000 orders. An index exists on `status`, but the plan uses a sequential scan.

Which response is most appropriate?

A. Force the index because any index scan is cheaper than a table scan.  
B. Drop the `status` column because its values are not unique.  
C. Treat the plan as corrupt because an existing index was skipped.  
D. Accept that scanning almost the whole table may be cheaper than many indexed row fetches.

### 25. Finding the changed node

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Iterative Performance Tuning  
**Is Curriculum Based:** No  
**Assessment type:** Comparing before-and-after plans

A report is measured before and after adding `idx_orders_status_date`.

| Evidence | Before | After |
|---|---|---|
| Access node | Seq Scan | Index Scan |
| Rows returned by access node | 70 | 70 |
| Rows removed by filter | 59,930 | 0 shown |
| Execution time | 39.021 ms | 1.298 ms |

What is the strongest conclusion?

A. The index changed which business rows satisfy the query.  
B. The index reduced unnecessary scanning and the measured runtime fell substantially.  
C. The query became faster because it now returns no rows.  
D. The `GROUP BY` was removed during the second measurement.

### 26. The update node reports zero rows

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN ANALYZE  
**Is Curriculum Based:** No  
**Assessment type:** Interpreting nested plan evidence

A measured update shows:

```text
Update on orders (actual rows=0)
  -> Seq Scan on orders (actual rows=15000)
       Filter: customer_id = 1
```

What should the reviewer record?

A. The update changed zero rows because the top node says `rows=0`.  
B. The plan is contradictory and cannot be interpreted.  
C. The scan found 15,000 rows to modify; an `Update` node need not return result rows to the client.  
D. The scan examined exactly 15,000 rows and filtered none out.

### 27. Repairing a cast-induced scan

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Common Bottlenecks  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two implementations

An indexed numeric column is queried in two versions:

```sql
-- Version P
WHERE amount::TEXT = '525.00'

-- Version Q
WHERE amount = 525.00
```

Both are intended to find numeric amount 525.00. Which prediction follows the chapter?

A. Q can use the numeric index directly, while P may force a sequential scan.  
B. P must be faster because text comparisons use fewer bytes.  
C. Both must use identical plans because their intended result is the same.  
D. Q cannot use an index unless `amount` is converted to text first.

### 28. Forcing a join only for diagnosis

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Join Algorithms  
**Is Curriculum Based:** No  
**Assessment type:** Evaluating a diagnostic experiment

For an unfiltered join, PostgreSQL chooses a hash join. A DBA temporarily runs:

```sql
SET enable_hashjoin = off;
EXPLAIN SELECT ...;
SET enable_hashjoin = on;
```

What is the sound interpretation of this experiment?

A. It proves hash joins should be disabled permanently in production.  
B. It changes the SQL result so the two plans cannot be compared.  
C. It refreshes table statistics before producing the second plan.  
D. It exposes the optimizer's next alternative for comparison without retaining the setting.

### 29. Selecting a composite-index experiment

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Iterative Performance Tuning  
**Is Curriculum Based:** No  
**Assessment type:** Choosing one targeted change

A report filters both columns together:

```sql
WHERE status = 'refunded'
  AND order_date > DATE '2025-06-01'
```

The baseline scans 60,000 rows and returns 70. Which single first experiment most directly matches the filter?

A. Add separate indexes, rewrite the query, and add `LIMIT` in one deployment.  
B. Create an index on `(status, order_date)`, then rerun the same measured query.  
C. Remove `order_date` from the result table and repeat the report.  
D. Disable hash joins before testing the filter again.

### 30. The top-ten change must match the requirement

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Iterative Performance Tuning  
**Is Curriculum Based:** No  
**Assessment type:** Validating a semantic repair

An engineer adds `LIMIT 10` to reduce a sort from all refund totals to a top-N sort.

When is this a valid tuning change?

A. Only when the business requirement asks for the ten highest totals.  
B. Whenever the original query returns more than ten rows.  
C. Whenever an index exists on the filtered columns.  
D. Only when plain `EXPLAIN` reports a sequential scan.

### 31. The plan line with the damaged estimate

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN ANALYZE  
**Is Curriculum Based:** No  
**Assessment type:** Locating a cardinality defect

Which node provides the clearest evidence of an estimate problem likely to distort later plan choices?

A. `Sort (rows=500) (actual rows=505 loops=1)`  
B. `Index Scan (rows=20) (actual rows=21 loops=1)`  
C. `Seq Scan (rows=80) (actual rows=1900000 loops=1)`  
D. `Hash (rows=5000) (actual rows=4988 loops=1)`

### 32. Choosing the inner side of a small nested loop

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Join Algorithms  
**Is Curriculum Based:** No  
**Assessment type:** Completing a plan

A filtered customer scan returns three rows. `idx_orders_customer_id` supports targeted lookups. Complete the useful inner node:

```text
Nested Loop
  -> Index Scan on customers (actual rows=3)
  -> _________________________________
```

A. Seq Scan on all orders, repeated for every order row  
B. Hash all customers again for each of the three rows  
C. Sort the full orders table independently three times  
D. Index Scan on orders using `customer_id = c.customer_id`

### 33. A plan whose children are not optional

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a plan-reading logic bug

A student reads this plan and says, “PostgreSQL chooses either the bitmap index scan or the bitmap heap scan.”

```text
Bitmap Heap Scan on orders
  -> Bitmap Index Scan on idx_orders_customer_id
```

Which correction is accurate?

A. The index scan builds matching locations that the heap scan uses to fetch table rows.  
B. The heap scan creates an index after the query finishes.  
C. Both lines name competing plans with equal estimated cost.  
D. The bitmap index scan returns complete table rows directly to the client.

### 34. The N+1 repair must preserve the requested data

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Common Bottlenecks  
**Is Curriculum Based:** No  
**Assessment type:** Selecting missing SQL

The UI needs every selected customer and that customer's orders. Application code currently issues one customer query and N order queries. Which query shape replaces the loop while retaining related data?

A. `SELECT customer_id FROM customers LIMIT 1;`  
B. `SELECT c.customer_id, o.order_id, o.amount FROM customers c LEFT JOIN orders o ON o.customer_id=c.customer_id WHERE ...;`  
C. `SELECT COUNT(*) FROM orders;`  
D. `EXPLAIN SELECT * FROM customers;`

### 35. Startup cost versus total cost

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN  
**Is Curriculum Based:** No  
**Assessment type:** Evaluating operator notation

Two candidate nodes show:

```text
P: cost=0.29..90.00
Q: cost=40.00..70.00
```

If the optimizer compares work to produce all rows, which value is the relevant total-cost comparison?

A. P's 0.29 versus Q's 40.00.  
B. Add the two values within each pair before comparing.  
C. P's 90.00 versus Q's 70.00.  
D. Divide startup by total cost for each candidate.

### 36. The evidence does not support more indexes yet

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Iterative Performance Tuning  
**Is Curriculum Based:** No  
**Assessment type:** Choosing the next tuning step

After one index change, a report falls from 39 ms to 1.3 ms and meets its 5 ms target. The new plan shows the intended index scan.

What is the most defensible next action?

A. Add two more indexes because every read query benefits from more indexes.  
B. Replace the successful index scan with a forced sequential scan.  
C. Change the join algorithm even though this query has no join.  
D. Record the verified result and stop this tuning cycle unless a remaining requirement exists.

### 37. Exposing stale estimates with the right tool

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN ANALYZE  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an observation that exposes a defect

Which observation most directly exposes that optimizer assumptions no longer match the data?

A. Plain `EXPLAIN` shows `rows=200`, with no actual count available.  
B. `EXPLAIN ANALYZE` shows `rows=200` estimated and `rows=15000` actual.  
C. A query returns columns in a different display order than expected.  
D. An index has a longer name than its table.

### 38. Same SQL, different join plans

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Inside the Query Optimizer  
**Is Curriculum Based:** No  
**Assessment type:** Explaining unexpected plan change

Yesterday a join used a nested loop after filtering to two customers. Today the filter matches 4,000 customers and the optimizer selects a hash join. The SQL template is unchanged.

Which explanation fits cost-based optimization?

A. The optimizer must use each algorithm in rotation.  
B. A hash join indicates the SQL query has become semantically different.  
C. Larger estimated inputs changed relative costs, so another valid plan became cheaper.  
D. Nested loops are automatically prohibited after one day.

### 39. An index name is not an operation

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Reading EXPLAIN  
**Is Curriculum Based:** No  
**Assessment type:** Parsing a plan node

Read the node:

```text
Index Scan using idx_orders_customer_id on orders
```

Which mapping is correct?

A. Operation: `Index Scan`; index: `idx_orders_customer_id`; table: `orders`.  
B. Operation: `orders`; table: `idx_orders_customer_id`; index: `Index Scan`.  
C. Operation and table: `Index Scan`; index: `orders`.  
D. Operation: `idx_orders_customer_id`; table: `Index Scan`; index: `orders`.

### 40. A complete performance investigation

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Iterative Performance Tuning  
**Is Curriculum Based:** No  
**Assessment type:** Applying the complete concept

A report is slow. Logs show only one SQL statement per request. Its measured plan scans 600,000 rows, returns 30 through a selective unindexed predicate, and spends nearly all runtime in that scan.

Which plan of action is the strongest?

A. Diagnose N+1, although the logs show one statement, and add more connections.  
B. Add several unrelated indexes and rewrite the aggregation before measuring again.  
C. Keep the baseline, add one index matching the selective predicate, rerun the same `EXPLAIN ANALYZE`, and compare.  
D. Use plain `EXPLAIN` after the change and compare estimated cost with the old actual milliseconds.

---

## Instructor Key

### 1. C

The optimizer compares valid candidate plans using estimated costs. Because every row matches, one sequential pass is estimated to beat many index-directed table fetches.

### 2. A

Plain `EXPLAIN` shows the plan and its estimates without executing the report. `EXPLAIN ANALYZE` would run it.

### 3. D

`EXPLAIN ANALYZE` executes this read-only query and reports actual rows and times alongside the optimizer's estimates.

### 4. B

Three outer customer rows plus an index on the inner join key is the characteristic strong case for a nested loop with targeted lookups.

### 5. D

The filter is highly selective but must inspect 50,000 rows. An index on `status`, followed by remeasurement, directly tests the smallest relevant repair.

### 6. C

A baseline, one controlled change, and the same measurement afterward allow the improvement to be demonstrated and attributed.

### 7. A

`ANALYZE` refreshes the statistics used for cardinality and cost estimates, directly addressing information made stale by the bulk load.

### 8. B

Indented child nodes feed their parent. The hotel rows are scanned into a hash, and the bookings scan probes it during the hash join.

### 9. D

The node averages about 0.250 ms and 6 rows per loop. Across 400 loops, that is about 100 ms and 2,400 rows.

### 10. A

One set-based query removes the 80 per-customer round trips. Making each repeated child query marginally faster would leave the N+1 structure intact.

### 11. B

The estimated `rows=15288` and actual `rows=15000` are the comparable cardinalities on the same node.

### 12. D

`EXPLAIN ANALYZE` must really execute the update to measure it; the surrounding transaction and `ROLLBACK` prevent those changes from persisting.

### 13. A

Comparing the numeric column directly with a numeric literal matches the existing index. Casting the indexed column to text can prevent that index from being used.

### 14. B

For two substantial, unsorted, unfiltered inputs, building a hash from one side and probing it with the other is a natural candidate.

### 15. C

The two values are estimated startup and total cost in PostgreSQL's internal relative units, not measured time.

### 16. D

The combined result is encouraging, but two simultaneous changes destroy causal attribution. Each should be evaluated in its own iteration.

### 17. A

`width` estimates average bytes per output row. With equal row counts, the wider plan may send substantially more data into later operations.

### 18. B

Merge join benefits when both inputs already arrive ordered by the join key. Sorting both complete inputs adds work that can change the preferred plan.

### 19. C

Node X misses by only 150 out of roughly 12,000. The other nodes are wrong by large multiples.

### 20. D

Physical strategies may differ in order, access paths, and costs, but every valid candidate must preserve the result required by the SQL.

### 21. A

The request issues one parent query plus 25 child queries: `1 + 25 = 26`.

### 22. B

One execution is already fast. Repeating it 2,000 times makes query count and round-trip overhead the dominant demonstrated problem.

### 23. C

The reported 1.40 ms is an average for one loop, so `1.40 × 50` is approximately 70 ms.

### 24. D

The predicate returns almost every row. A sequential sweep may legitimately cost less than using the index to fetch nearly the whole table.

### 25. B

Both versions return 70 rows, but the after plan avoids discarding 59,930 rows and its measured execution time is much lower.

### 26. C

The child scan identifies the 15,000 rows to modify. The top update operation does not have to emit those rows as a client result set.

### 27. A

Version Q compares values in the indexed numeric domain. Version P applies a text conversion to the indexed column and may require scanning.

### 28. D

Temporarily disabling hash joins can reveal the next costed alternative for diagnosis. Restoring the setting avoids turning the experiment into a permanent rule.

### 29. B

The composite index matches the two filter columns, and changing only that one factor permits a clean before-and-after measurement.

### 30. A

`LIMIT 10` changes the result set. It is correct only when returning the top ten, rather than every total, matches the business requirement.

### 31. C

Estimating 80 rows but observing 1.9 million is an extreme cardinality error and can make downstream algorithms appear far cheaper than they are.

### 32. D

For each of three outer customers, the inner index scan can retrieve orders matching that customer's ID without scanning all orders.

### 33. A

These are cooperating parent and child nodes: the bitmap index scan finds row locations, then the bitmap heap scan fetches the table rows.

### 34. B

The join retrieves customers and their related order data in one set-based statement, replacing repeated child queries without discarding the relationship.

### 35. C

In `startup..total`, the second number is the estimated cost to produce all rows. Q's total cost of 70 is lower than P's 90.

### 36. D

The measured result meets the requirement and the expected plan change is visible. More speculative changes would add cost without a demonstrated need.

### 37. B

Only `EXPLAIN ANALYZE` supplies estimate and reality together here; 200 estimated versus 15,000 actual directly reveals the mismatch.

### 38. C

Join algorithms are costed for the estimated input sizes. Expanding the filtered side from two to 4,000 rows can make hashing cheaper than repeated lookups.

### 39. A

`Index Scan` is the operation, `idx_orders_customer_id` is the index used, and `orders` is the table being accessed.

### 40. C

The evidence points to a selective scan with no supporting index. One matching index followed by the same actual measurement is the controlled, evidence-based repair.

---

## Coverage summary

| Subtopic | Questions |
|---|---|
| Inside the Query Optimizer | 1, 7, 20, 24, 38 |
| Reading EXPLAIN | 2, 8, 15, 17, 33, 35, 39 |
| Reading EXPLAIN ANALYZE | 3, 9, 11, 12, 19, 23, 26, 31, 37 |
| Join Algorithms | 4, 14, 18, 28, 32 |
| Common Bottlenecks | 5, 10, 13, 21, 22, 27, 34 |
| Iterative Performance Tuning | 6, 16, 25, 29, 30, 36, 40 |
