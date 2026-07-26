# DBMS 5.2: Window Functions — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Advanced Querying with SQL
- **Chapter:** Window Functions
- **Scope:** All six Topic 5.2 subtopics in the attached course blueprint (What is a Window Function; OVER, PARTITION BY, and ORDER BY; Ranking Functions; Offset Functions: LAG and LEAD; Running Totals, Moving Averages, and Window Frames; Top-N Per Group)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every item begins with a recognisable analytical or reporting task. Whenever the answer depends on values, the source rows, ordering columns, and partition keys are visible.
- **Evidence rule:** Students must trace a window row by row, complete or repair an `OVER` clause, compare ranking policies, expose an ordering defect, calculate an offset or frame boundary, or assemble a filterable top-N pattern.
- **Scope guard:** Only the six Topic 5.2 concepts are assessed. Peer-sensitive default-frame claims are made only when the ordering values shown make the outcome unambiguous.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all six Topic 5.2 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. The report GROUP BY couldn't write

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Window Function  
**Is Curriculum Based:** No  
**Assessment type:** Problem-to-tool mapping

A payroll analyst needs one line **per employee** showing the employee's own salary *and* the company average beside it. A GROUP BY attempt collapses everything into a single average row and loses the employees.

Select the expression that preserves every employee row while adding the shared benchmark.

A. Two databases side by side.  
B. `HAVING AVG(salary)`, which filters grouped rows but restores the original employee detail.  
C. A second spreadsheet for the average.  
D. A window function: `AVG(salary) OVER ()`, without collapsing rows.

### 2. What OVER actually does

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** OVER, PARTITION BY, and ORDER BY  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism identification

Every window function call carries an OVER clause, even an empty `OVER ()`.

Identify the calculation boundary established by `OVER`, including the meaning of empty parentheses.

A. The output column's name.  
B. The window — the rows the function looks at per row.  
C. The table the query reads from.  
D. The number of physical scans PostgreSQL must perform.

### 3. The rank after the tie

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Ranking Functions  
**Is Curriculum Based:** No  
**Assessment type:** RANK-gap tracing

A baking competition ranks contestants by their final score.

`pastry_contest`

| baker | score |
|---|---|
| Noor | 90 |
| Petra | 88 |
| Qasim | 88 |
| Ravi | 75 |

```sql
SELECT baker, RANK() OVER (ORDER BY score DESC) AS rnk FROM pastry_contest;
```

Trace the tied positions and assign Ravi's rank.

A. 4 — Petra and Qasim tie at 2, so RANK skips to 4.  
B. 3 — ranks never skip.  
C. 2 — ties push others up.  
D. 1 — descending ranking assigns first place to the lowest score.

### 4. What February remembers about January

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Offset Functions: LAG and LEAD  
**Is Curriculum Based:** No  
**Assessment type:** LAG tracing

A mall kiosk tracks its monthly revenue.

`kiosk_revenue`

| month_no | month | revenue |
|---:|---|---:|
| 1 | Jan | 100 |
| 2 | Feb | 130 |

```sql
SELECT month, revenue,
       LAG(revenue) OVER (ORDER BY month_no) AS prev_rev
FROM kiosk_revenue;
```

Follow the declared month sequence and select February's fetched value.

A. 130 — its own value.  
B. 230 — the two summed.  
C. 100 — LAG reaches back one row, fetching January's revenue.  
D. NULL, because `LAG` returns NULL for every row in a two-row window.

### 5. The total that grows row by row

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Running Totals, Moving Averages, and Window Frames  
**Is Curriculum Based:** No  
**Assessment type:** Running-total tracing

A charity tracks daily donation totals during its fundraiser.

`donations`

| day | amount |
|---|---|
| 1 | 10 |
| 2 | 20 |
| 3 | 30 |

```sql
SELECT day, SUM(amount) OVER (ORDER BY day) AS running FROM donations;
```

Accumulate the ordered frame through day 3.

A. 60 — SUM accumulates with ORDER BY: 10, 30, 60.  
B. 30 — the day's own amount.  
C. 20 — the average.  
D. 90 — each preceding amount is counted again on every later row.

### 6. Two best sellers from every store

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Top-N Per Group  
**Is Curriculum Based:** No  
**Assessment type:** Pattern construction

A grocery chain guarantees at least two products per store and wants exactly two products from each store, ordered by revenue. Equal revenues may be broken by product ID.

Choose the pattern that applies the quota independently within every store.

A. `ORDER BY revenue DESC, product_id LIMIT 2`, which applies one global quota after combining every store into a single ranking  
B. `GROUP BY store`, selecting two ungrouped product rows from each aggregate group  
C. A MAX() per store — one row, not two.  
D. Number rows with `ROW_NUMBER() OVER (PARTITION BY store ORDER BY revenue DESC, product_id)`, then filter `rn <= 2` outside.

### 7. Collapse or annotate

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Window Function  
**Is Curriculum Based:** No  
**Assessment type:** Contrast identification

Choose the report-shape comparison that accounts for the number of output rows.

A. Both collapse rows identically.  
B. GROUP BY collapses rows into one per group; a window function keeps every row.  
C. Window functions collapse rows, while `GROUP BY` preserves every original detail row unchanged.  
D. Neither can compute aggregates.

### 8. Numbering that starts over

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Ranking Functions  
**Is Curriculum Based:** No  
**Assessment type:** Partitioned-numbering tracing

A trail-running event tracks checkpoints along each route by distance.

`checkpoints`

| route | checkpoint | dist_km |
|---|---|---|
| Coastal | CP-A | 5 |
| Coastal | CP-B | 12 |
| Ridge | CP-C | 4 |
| Ridge | CP-D | 9 |
| Ridge | CP-E | 15 |

```sql
SELECT route, checkpoint,
       ROW_NUMBER() OVER (PARTITION BY route ORDER BY dist_km) AS seq
FROM checkpoints;
```

Trace the restart at each route boundary.

A. 1 through 5 continuously because `PARTITION BY` affects labels but not numbering.  
B. All rows get 1.  
C. Coastal: 1, 2; Ridge: 1, 2, 3, restarting per partition.  
D. Random numbers per run.

### 9. What this departure knows about the next

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Offset Functions: LAG and LEAD  
**Is Curriculum Based:** No  
**Assessment type:** LEAD tracing

A ferry operator publishes its departure timetable.

`ferry_departures`

| dep_time |
|---|
| 08:00 |
| 09:30 |
| 11:00 |

```sql
SELECT dep_time, LEAD(dep_time) OVER (ORDER BY dep_time) AS next_dep
FROM ferry_departures;
```

Move one ordered row forward from 09:30.

A. 08:00 — `LEAD` moves to the previous departure when the ordering is ascending.  
B. 09:30 — itself.  
C. NULL — LEAD looks backward.  
D. 11:00 — LEAD reaches forward, fetching the next departure.

### 10. Slicing without collapsing

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** OVER, PARTITION BY, and ORDER BY  
**Is Curriculum Based:** No  
**Assessment type:** Clause-role identification

Inside an OVER clause, a query writes `PARTITION BY warehouse`.

Select the effect `PARTITION BY warehouse` has on calculation membership and result-row count.

A. Deletes the smaller warehouses.  
B. Splits rows into per-warehouse groups; all rows remain in the result.  
C. Collapses the output to one aggregate row per warehouse while retaining no individual warehouse rows.  
D. Sorts the final output by warehouse.

### 11. Every clerk beside the same number

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Window Function  
**Is Curriculum Based:** No  
**Assessment type:** Row-plus-aggregate tracing

A retail office tracks each clerk's salary.

`clerks`

| clerk | salary |
|---|---|
| Devi | 400 |
| Emil | 600 |
| Faiz | 800 |

```sql
SELECT clerk, salary, AVG(salary) OVER () AS company_avg FROM clerks;
```

Determine both the output-row count and the repeated benchmark value.

A. Three rows, each with own salary plus 600 in `company_avg`.  
B. One row: 600.  
C. Three rows, each averaging only the current clerk's salary.  
D. An error; AVG demands GROUP BY.

### 12. The two clauses inside the window

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** OVER, PARTITION BY, and ORDER BY  
**Is Curriculum Based:** No  
**Assessment type:** Combined-clause reasoning

A logistics ranking uses `RANK() OVER (PARTITION BY region ORDER BY tonnage DESC)`.

Assign the grouping and sequencing responsibilities to the two clauses.

A. `PARTITION BY` sorts the displayed rows, while `ORDER BY` creates region groups.  
B. Both clauses sort the final output.  
C. PARTITION BY scopes ranking per region; ORDER BY defines "first" there.  
D. The clauses cancel each other.

### 13. Why 3 went missing

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Ranking Functions  
**Is Curriculum Based:** No  
**Assessment type:** Gap-behaviour identification

A sailing regatta's RANK column reads 1, 2, 2, 4 — no 3 anywhere.

Explain the missing position from the tie policy rather than from the displayed order.

A. One of the tied boats consumes rank 3 but is displayed with rank 2.  
B. The database miscounted.  
C. RANK always skips odd numbers.  
D. Two boats tied at rank 2; RANK skips ahead to 4.

### 14. The row with no yesterday

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Offset Functions: LAG and LEAD  
**Is Curriculum Based:** No  
**Assessment type:** Boundary-behaviour identification

A temperature log's `LAG(reading) OVER (ORDER BY read_at)` column shows a value on every row except the first, which shows NULL.

Interpret the boundary NULL using the ordered window.

A. The first reading failed.  
B. The first row has no previous row for LAG, so it reports NULL.  
C. `LAG` assigns NULL to whichever row PostgreSQL happens to read first.  
D. The ORDER BY is broken.

### 15. The average that travels in pairs

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Running Totals, Moving Averages, and Window Frames  
**Is Curriculum Based:** No  
**Assessment type:** Custom-frame tracing

An environmental monitor logs the daily air quality index (AQI).

`aqi_readings`

| day | aqi |
|---|---|
| 1 | 10 |
| 2 | 20 |
| 3 | 30 |

```sql
SELECT day, AVG(aqi) OVER (ORDER BY day
       ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS smooth
FROM aqi_readings;
```

Apply the explicit two-row frame to day 3.

A. 25 — the frame spans days 2 and 3, average (20 + 30) / 2.  
B. 20 — the frame expands to all rows because an average ignores frame limits.  
C. 30 — its own value only.  
D. 60 — the running sum.

### 16. Why the filter had to move upstairs

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Top-N Per Group  
**Is Curriculum Based:** No  
**Assessment type:** Placement-constraint reasoning

A developer writes:

```sql
SELECT product_id
FROM products
WHERE ROW_NUMBER() OVER (ORDER BY revenue DESC) <= 3;
```

The statement fails.

Identify the evaluation-order defect and the role of the outer query.

A. A CTE changes `ROW_NUMBER` into an aggregate that runs before `WHERE` in the same query block.  
B. WHERE clauses reject all numbers.  
C. Window functions run after WHERE, so WHERE can't see the row number.  
D. It is a stylistic preference only.

### 17. No gaps, please

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Ranking Functions  
**Is Curriculum Based:** No  
**Assessment type:** Function selection

A medals committee wants tied athletes to share a rank, and the *next* rank to follow immediately — after two athletes share 2nd, the next is 3rd, never 4th.

Choose the function whose tie policy matches both requirements.

A. `ROW_NUMBER`, because unique numbers preserve a shared rank after a tie.  
B. RANK — it skips after ties.  
C. SUM — ranks are additive.  
D. DENSE_RANK — ties share a rank, and numbering continues without gaps.

### 18. A window that is ordered but whole

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** OVER, PARTITION BY, and ORDER BY  
**Is Curriculum Based:** No  
**Assessment type:** Clause-combination reasoning

A query uses `SUM(amount) OVER (ORDER BY sale_date)` — ORDER BY present, no PARTITION BY.

Describe the membership and cumulative frame created by this clause combination.

A. One single-row partition per result row, because omitting `PARTITION BY` isolates rows.  
B. One big window over all rows, ordered by date, sum accumulating.  
C. An empty window; PARTITION BY is mandatory.  
D. A random sample of rows.

### 19. The pane that looks both ways

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Running Totals, Moving Averages, and Window Frames  
**Is Curriculum Based:** No  
**Assessment type:** Centered-frame tracing

A mall tracks hourly visitor footfall.

`footfall`

| hour | visitors |
|---|---|
| 1 | 10 |
| 2 | 20 |
| 3 | 60 |

```sql
SELECT hour, AVG(visitors) OVER (ORDER BY hour
       ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS centered
FROM footfall;
```

Evaluate the centered frame on the middle row.

A. 30 — the frame reaches back one, forward one, averaging all three.  
B. 15 — only the backward pair.  
C. 40 — the frame includes only the current and following rows, averaging 20 and 60.  
D. 20 — its own value.

### 20. One dish per city survives

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Top-N Per Group  
**Is Curriculum Based:** No  
**Assessment type:** Top-1 tracing

A food-delivery app tracks monthly orders for each dish by city.

`street_food`

| city | dish | monthly_orders |
|---|---|---|
| Pune | Misal | 900 |
| Pune | Vada Pav | 700 |
| Surat | Locho | 800 |

A CTE numbers dishes with `ROW_NUMBER() OVER (PARTITION BY city ORDER BY monthly_orders DESC)`, and the outer query keeps `rn = 1`.

Apply the independently restarted row numbers and select the retained dishes.

A. Misal only, because `rn = 1` is applied once after all cities are combined.  
B. Vada Pav and Locho.  
C. Misal (Pune's #1) and Locho (Surat's #1), each city's first row kept.  
D. All three dishes.

### 21. After the dust settles

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Window Function  
**Is Curriculum Based:** No  
**Assessment type:** Evaluation-order identification

A query has a WHERE clause and a window function.

Place the window calculation in the logical pipeline and identify its input rows.

A. Every base-table row, including those rejected by the earlier `WHERE` predicate.  
B. Only rows the window itself filters.  
C. Rows from other tables too.  
D. Only the rows that survived WHERE, computed after filtering.

### 22. Two months back

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Offset Functions: LAG and LEAD  
**Is Curriculum Based:** No  
**Assessment type:** Multi-step offset tracing

A fuel retailer tracks the monthly diesel price.

`diesel_prices`

| month_no | price |
|---|---|
| 1 | 5 |
| 2 | 7 |
| 3 | 9 |
| 4 | 12 |

```sql
SELECT month_no, LAG(price, 2) OVER (ORDER BY month_no) AS two_back
FROM diesel_prices;
```

Move exactly two ordered positions backward from month 4.

A. 9 — one row back.  
B. 7 — the second argument reaches back two rows to month 2.  
C. 5, because an offset of 2 always refers to the partition's first row.  
D. NULL — multi-step LAG is invalid.

### 23. The family, defined

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Window Function  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

Choose the definition that accounts for both calculation scope and preserved row detail.

A. A function computing a value per row from its window, without collapsing.  
B. A function that evaluates its related rows through a separate database connection.  
C. A function limited to text columns.  
D. A synonym for a subquery.

### 24. The three dials on the window

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** OVER, PARTITION BY, and ORDER BY  
**Is Curriculum Based:** No  
**Assessment type:** Ingredient matching

Match all three `OVER` ingredients to their distinct responsibilities.

A. `PARTITION BY`: sorts output; `ORDER BY`: groups rows; frame: renames columns.  
B. All three delete rows.  
C. PARTITION BY groups the window's rows; ORDER BY sequences; frame slices.  
D. Only one may appear at a time.

### 25. Ties, numbered anyway

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Ranking Functions  
**Is Curriculum Based:** No  
**Assessment type:** Function-behaviour discrimination

Two vineyards tie on rating, yet the `ROW_NUMBER()` column shows them as 2 and 3, not 2 and 2.

Explain why a tie can still receive two different sequence numbers.

A. The ratings secretly differ.  
B. ROW_NUMBER is broken for ties.  
C. Equal ordering values automatically create separate hidden partitions.  
D. ROW_NUMBER assigns unique sequential integers regardless of ties.

### 26. How much did it change?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Offset Functions: LAG and LEAD  
**Is Curriculum Based:** No  
**Assessment type:** Delta-calculation tracing

A gym tracks its monthly new member signups.

`gym_signups`

| month_no | month | signups |
|---:|---|---:|
| 3 | Mar | 220 |
| 4 | Apr | 260 |

```sql
SELECT month, signups,
       signups - LAG(signups) OVER (ORDER BY month_no) AS change
FROM gym_signups;
```

Calculate April's signed difference from its fetched predecessor.

A. 260 — its own value.  
B. 40 — the row's value minus LAG's fetched March value (260 − 220).  
C. −40 — LAG subtracts forward.  
D. NULL, because a value returned by `LAG` cannot participate in arithmetic.

### 27. Same SUM, two meanings

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Running Totals, Moving Averages, and Window Frames  
**Is Curriculum Based:** No  
**Assessment type:** Default-frame reasoning

Two windowed sums over the same rows: `SUM(amt) OVER ()` shows 600 on every row, while `SUM(amt) OVER (ORDER BY day)` shows 100, 300, 600.

Identify the frame change introduced by adding the internal ordering.

A. Adding ORDER BY changes the default frame, narrowing it per row.  
B. The ordered version implicitly switches to a different source table.  
C. ORDER BY multiplies values.  
D. The first query is cached.

### 28. When the tie refuses to fit the quota

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Top-N Per Group  
**Is Curriculum Based:** No  
**Assessment type:** Tie-policy discrimination

A "top 3 agents per branch" report hits a branch where two agents tie for third place.

Select the tie policy that either enforces or deliberately exceeds the three-row quota.

A. Delete one of the tied agents.  
B. Ties always crash top-N queries.  
C. ROW_NUMBER picks 3 arbitrarily; RANK would keep both tied agents.  
D. The report must switch to `GROUP BY`, because window rankings cannot retain tied rows.

### 29. South division, third place

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Ranking Functions  
**Is Curriculum Based:** No  
**Assessment type:** Partitioned-rank tracing

A company tracks sales figures for its agents across regions.

`sales_agents`

| region | agent | sales |
|---|---|---|
| North | Ira | 90 |
| North | Tan | 70 |
| South | Ade | 85 |
| South | Bel | 85 |
| South | Cy | 60 |

```sql
SELECT agent, RANK() OVER (PARTITION BY region ORDER BY sales DESC) AS rnk
FROM sales_agents;
```

Restart the ranking within South and assign Cy's position after the tie.

A. 2 — next after the tie.  
B. 5 — both regions contribute to one company-wide rank sequence before the South rows are labelled.  
C. 1 — lowest first.  
D. 3 — within South, Ade and Bel tie at 1, RANK skips 2, Cy takes 3.

### 30. The countdown to the next service

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Offset Functions: LAG and LEAD  
**Is Curriculum Based:** No  
**Assessment type:** Construction selection

A machine-maintenance log must show, on each service row, the number of days until that machine's **next** service.

Complete the forward-looking, per-machine interval calculation.

A. `service_date - LAG(service_date) OVER (PARTITION BY machine_id ORDER BY service_date) AS days_since_previous`  
B. `LEAD(service_date) OVER (PARTITION BY machine_id ORDER BY service_date) - service_date`.  
C. `MAX(service_date) OVER ()` — the last service overall.  
D. `ROW_NUMBER() OVER (PARTITION BY machine_id ORDER BY service_date)`  

### 31. Totals that reset at the border

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Running Totals, Moving Averages, and Window Frames  
**Is Curriculum Based:** No  
**Assessment type:** Partitioned running-total tracing

A digital wallet app tracks each user's top-up amounts by day.

`wallet_topups`

| user_id | day | amount |
|---|---|---|
| U1 | 1 | 200 |
| U1 | 2 | 150 |
| U2 | 1 | 50 |

```sql
SELECT user_id, day,
       SUM(amount) OVER (PARTITION BY user_id ORDER BY day) AS balance
FROM wallet_topups;
```

Trace the accumulation and its reset at the user boundary.

A. U1: 200 then 350; U2: 50, fresh per user partition.  
B. 200, 350, 400 — `ORDER BY day` overrides the user partitions.  
C. 400 on every row.  
D. 200, 150, 50 — no accumulation.

### 32. One pattern, any N

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Top-N Per Group  
**Is Curriculum Based:** No  
**Assessment type:** Generalization identification

Yesterday the team shipped "top 2 products per store." Today's requests: top 5 routes per port, top 1 course per instructor, top 3 posts per author.

Generalize the structure by identifying which parts change and which remain fixed.

A. Each requires a distinct SQL technique because the requested value of N differs.  
B. Only top-1 queries are possible.  
C. They are all the same pattern: partition, order, number, filter outside.  
D. Databases cap N at 2.

### 33. Say the frame out loud

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Running Totals, Moving Averages, and Window Frames  
**Is Curriculum Based:** No  
**Assessment type:** Frame-specification selection

A pollution dashboard needs, per row, the average of the previous reading, the current one, and the next one.

Translate “previous, current, next” into explicit frame boundaries.

A. `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` — a three-row trailing frame ending at the current reading  
B. `ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING` — three forward rows.  
C. No frame; the default already does this.  
D. `ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING` — one back, itself, one ahead.

### 34. Numbered inside, shuffled outside

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Top-N Per Group  
**Is Curriculum Based:** No  
**Assessment type:** Ordering-scope reasoning

A top-3-per-region query computes correct row numbers, yet the final rows print in no useful order, regions interleaved.

Select the explanation and the smallest presentation-order repair.

A. The internal ordering is broken, so replace it with an outer ordering and leave `OVER ()` unordered.  
B. The `ORDER BY` inside `OVER` governs numbering; add an outer `ORDER BY region, rn` for display.  
C. Windows randomize output as a security feature.  
D. Row numbers cannot coexist with sorted output.

### 35. Eight in, how many out?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Window Function  
**Is Curriculum Based:** No  
**Assessment type:** Row-count contrast

A `harvests` table has 8 rows across 3 orchards. Query A: `SELECT orchard, SUM(kg) FROM harvests GROUP BY orchard;` Query B: `SELECT orchard, kg, SUM(kg) OVER (PARTITION BY orchard) FROM harvests;`

Compare the two output shapes and calculate both row counts.

A. A: 3, collapsed per orchard; B: 8, every row annotated.  
B. Both return 8.  
C. Both return 3.  
D. Query A returns 8 detail rows, while Query B returns 3 grouped orchard rows.

### 36. Each stylist beside the branch number

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** OVER, PARTITION BY, and ORDER BY  
**Is Curriculum Based:** No  
**Assessment type:** Partitioned-aggregate tracing

A salon chain tracks the number of haircuts each stylist completes.

`stylists`

| branch | stylist | cuts |
|---|---|---|
| Andheri | Mo | 30 |
| Andheri | Nia | 50 |
| Bandra | Om | 20 |

```sql
SELECT stylist, cuts,
       AVG(cuts) OVER (PARTITION BY branch) AS branch_avg
FROM stylists;
```

Restrict the average to Mo's branch and calculate the value.

A. 33.3 — every branch is included because `AVG` ignores `PARTITION BY`.  
B. 30 — his own cuts.  
C. 40 — the Andheri partition's average, 30 and 50 combined.  
D. 50 — the branch maximum.

### 37. Three functions, one scoreboard

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Ranking Functions  
**Is Curriculum Based:** No  
**Assessment type:** Side-by-side tracing

A trivia competition ranks finalists by their score.

`quiz_finals`

| player | score |
|---|---|
| Kito | 100 |
| Lena | 90 |
| Mira | 90 |
| Nils | 80 |

All three ranking functions run over `ORDER BY score DESC`. Determine Nils's `(ROW_NUMBER, RANK, DENSE_RANK)` triple.

A. (4, 3, 4), reordered wrong.  
B. (3, 3, 3), because the tie reduces Nils's physical row position to third.  
C. (4, 4, 4), because every ranking function counts occupied row positions identically.  
D. (4, 4, 3): ROW_NUMBER 4th, RANK 4, DENSE_RANK 3.

### 38. Which way does each one look?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Offset Functions: LAG and LEAD  
**Is Curriculum Based:** No  
**Assessment type:** Direction pairing

Match each function to its direction in the declared window order.

A. `LAG` fetches a following row, while `LEAD` fetches a preceding row in the same declared order.  
B. LAG fetches from a previous row; LEAD from a following row.  
C. Both look only at the current row.  
D. Both require GROUP BY.

### 39. Write the three-day sum

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Running Totals, Moving Averages, and Window Frames  
**Is Curriculum Based:** No  
**Assessment type:** Explicit-frame construction

A reservoir dashboard needs, on each day's row, the total inflow of that day and the two days before it — a three-day trailing sum.

Complete the trailing three-row frame without turning it into an all-history running total.

A. `SUM(inflow) OVER (ORDER BY day ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)`.  
B. `SUM(inflow) OVER ()` — the grand total.  
C. `SUM(inflow) OVER (ORDER BY day)` — the running total since day one, forever accumulating.  
D. `LAG(inflow, 3) OVER (ORDER BY day)` — one value from three days ago.

### 40. The whole pattern, assembled

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Top-N Per Group  
**Is Curriculum Based:** No  
**Assessment type:** Integrated construction

A streaming service wants each genre's 2 most-played tracks from `plays(track, genre, play_count)`.

Select the executable CTE pattern that returns at most two tracks per genre.

A. `WITH ranked AS (SELECT track, genre, play_count, ROW_NUMBER() OVER (ORDER BY play_count DESC NULLS LAST, track ASC) AS rn FROM plays) SELECT genre, track, play_count FROM ranked WHERE rn <= 2 ORDER BY genre, rn, track;`  
B. `SELECT track, RANK() FROM plays LIMIT 2;`  
C. `WITH ranked AS (SELECT track, genre, play_count, ROW_NUMBER() OVER (PARTITION BY genre ORDER BY play_count DESC, track) AS rn FROM plays) SELECT genre, track, play_count FROM ranked WHERE rn <= 2 ORDER BY genre, rn;`  
D. `SELECT TOP 2 track PER genre FROM plays;`

---

## Instructor Key

### 1. D

The requirement is per-row detail *plus* an aggregate — exactly what GROUP BY cannot produce, since it trades the rows for the summary. The window function computes the aggregate while leaving every row in place.

### 2. B

OVER defines the window: which rows the function consults when computing this row's value. Empty parentheses widen the window to the whole result — the function still writes an answer onto every row.

### 3. A

Petra and Qasim share rank 2; RANK then jumps to 4 because three bakers stand ahead of Ravi. The skipped 3 is not an error — it is positional truth.

### 4. C

LAG reaches one row back in the declared order and fetches January's revenue: 100. February's row therefore shows its own 130 in `revenue` and the fetched 100 in `prev_rev` — the current row borrowing the previous row's value.

### 5. A

ORDER BY inside the window gives SUM a cumulative frame: each row's total covers the first row through itself. Day 3 sees 10 + 20 + 30 = 60.

### 6. D

The chapter's top-N template: partition by the group, order by the metric, number the rows, and filter the numbering in an outer query. LIMIT (A) knows nothing of stores; it takes a global slice.

### 7. B

The contrast in one line: GROUP BY summarizes (fewer rows out), window functions annotate (same rows out, plus computed columns). Option C states it exactly backwards.

### 8. C

PARTITION BY route makes each route its own numbering universe; ORDER BY dist_km fixes the sequence inside each. Coastal counts to 2, Ridge to 3, and neither counts the other's rows.

### 9. D

LEAD is LAG's mirror: one row forward in the window's order. The 09:30 sailing's `next_dep` is 11:00; the final row's LEAD, with nothing ahead, would be NULL.

### 10. B

PARTITION BY groups rows *for the computation only* — each row's window is its own partition, but the result keeps all rows. Collapsing (C) is GROUP BY's behaviour, precisely what the window avoids.

### 11. A

The empty OVER makes one window of all three rows; AVG computes 600 once, and every row carries it beside its own salary. Row and aggregate, side by side — the family's founding trick.

### 12. C

Two dials, two jobs: PARTITION BY scopes (rank *within what*), ORDER BY defines the metric's direction (rank *by what*). An independent, heaviest-first ranking inside each region.

### 13. D

RANK's positions count rows ahead, so a two-way tie at 2 pushes the next boat to 4. The missing 3 records the fact that three boats finished ahead of the fourth.

### 14. B

Offsets can point past the window's edge: the first row's "previous row" does not exist, and LAG reports that absence as NULL rather than inventing a value.

### 15. A

The explicit frame is a two-row sliding pane: previous plus current. On day 3 that is (20 + 30) / 2 = 25 — a moving average, born entirely from the frame clause.

### 16. C

Evaluation order is the obstacle: WHERE runs before window functions exist, so the row number is not yet a thing WHERE can test. The CTE turns it into an ordinary column, and ordinary columns are filterable.

### 17. D

"Ties share, no gaps" is DENSE_RANK's exact contract. RANK shares but skips; ROW_NUMBER refuses to share at all.

### 18. B

Without PARTITION BY the window is all rows; with ORDER BY present, the default frame becomes start-through-current-row. The combination is the classic all-rows running total.

### 19. A

The frame reads one back, itself, one forward: 10, 20, 60 → average 30. Centered frames are how smoothing uses both neighbours; the backward-only pane (B) is a different frame spec.

### 20. C

The partition resets the numbering per city, so each city owns a row 1: Misal in Pune, Locho in Surat. The filter keeps exactly those — per-group winners, not a global one (A).

### 21. D

Window functions run late in the pipeline: after WHERE and GROUP BY have settled which rows exist. The window sees the survivors — which is also why a filtered-out row can never influence a running total.

### 22. B

`LAG(price, 2)` stretches the reach: from month 4, two rows back is month 2, price 7. The second argument is the step count, defaulting to 1.

### 23. A

The definition has both halves: computes per row over a defined set of related rows, and never collapses. Each half rules out one of the wrong options.

### 24. C

The three dials: PARTITION BY picks the window's membership, ORDER BY its internal sequence, and the frame the slice of that sequence the function actually reads. Together they fully describe what the function sees.

### 25. D

ROW_NUMBER's promise is uniqueness, not fairness: sequential integers even across ties. Sharing is what RANK and DENSE_RANK are for — choosing among the three is choosing a tie policy.

### 26. B

The pattern subtracts LAG's fetched value from the row's own: 260 − 220 = 40. LAG supplies the past; ordinary arithmetic does the rest.

### 27. A

One function, two frames: no ORDER BY → whole-window total on every row; ORDER BY → default frame of start-through-current, which *is* the running total. The difference lives entirely in the frame the ORDER BY switches on.

### 28. C

The tie forces a policy decision, and the function encodes it: ROW_NUMBER enforces the quota by arbitrary tie-breaking; RANK honours the tie by exceeding the quota. Neither is wrong — unexamined is the only wrong choice.

### 29. D

South's ranking is a private affair: Ade and Bel tie at 1, RANK skips 2, Cy lands at 3. Ira's 90 in the North partition is invisible to South's numbering.

### 30. B

"Next" points forward, so LEAD: the machine's following service date minus the current one is the gap ahead. The partition keeps each machine's timeline separate. Option A computes the backward gap.

### 31. A

PARTITION BY makes the accumulation per-user: U1 builds 200 then 350; U2 starts over at 50. The partition boundary is a reset line for the running frame.

### 32. C

The template generalizes on three axes — group, metric, N — with no structural change. Recognizing yesterday's query in today's three requests is the pattern-literacy the chapter is building.

### 33. D

"Previous, current, next" translates directly: 1 PRECEDING through 1 FOLLOWING. Options A and B are trailing and leading panes — real frames, wrong requirement.

### 34. B

Two different ORDER BYs govern two different things: the window's orders the computation; only an outer ORDER BY orders the printout. Correct numbers in a shuffled display means exactly one of them is missing.

### 35. A

The row counts tell the whole story: 3 versus 8. GROUP BY spent the rows to buy the totals; the window kept both.

### 36. C

Mo's window is the Andheri partition: (30 + 50) / 2 = 40. Om's window is Bandra alone: 20. Same expression, different slice per row — partitioned aggregation in one glance.

### 37. D

Nils by each ruler: fourth row (ROW_NUMBER), rank 4 (three players ahead — RANK's gap after the 90-90 tie), third distinct score (DENSE_RANK). One row, three philosophies of counting.

### 38. B

LAG reaches back, LEAD reaches ahead — both along the window's declared order, both leaving the current row where it is. Option A swaps the directions.

### 39. A

"Today and the two before" is a trailing three-row frame: 2 PRECEDING through CURRENT ROW. The running total (C) never forgets old days; LAG (D) fetches one value rather than summing three.

### 40. C

Every piece is present: CTE, per-genre partition, play-count ordering with a deterministic track-name tie-breaker, `ROW_NUMBER`, outer filter `rn <= 2`, and display sorting. Option A numbers the entire service globally because it omits `PARTITION BY genre`.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Window-result tracing over shown data | 3, 4, 5, 8, 9, 11, 15, 19, 20, 22, 26, 29, 31, 36, 37 |
| Construction and pattern selection | 6, 30, 33, 39, 40 |
| Mechanism and clause-role reasoning | 2, 10, 12, 16, 18, 21, 24, 27, 34 |
| Function discrimination and policy judgment | 1, 7, 13, 14, 17, 23, 25, 28, 32, 35, 38 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| What is a Window Function | 1, 7, 11, 21, 23, 35 | 6 |
| OVER, PARTITION BY, and ORDER BY | 2, 10, 12, 18, 24, 36 | 6 |
| Ranking Functions | 3, 8, 13, 17, 25, 29, 37 | 7 |
| Offset Functions: LAG and LEAD | 4, 9, 14, 22, 26, 30, 38 | 7 |
| Running Totals, Moving Averages, and Window Frames | 5, 15, 19, 27, 31, 33, 39 | 7 |
| Top-N Per Group | 6, 16, 20, 28, 32, 34, 40 | 7 |

Questions 1–10 collectively cover all six Topic 5.2 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (7, 10, 13, 14, 21, 23, 24, 25, 35, 38)
- Intermediate: 27 questions
- Advanced: 3 questions (28, 37, 40)
- Correct option A: 10 questions (3, 5, 11, 15, 19, 23, 27, 31, 35, 39)
- Correct option B: 10 questions (2, 7, 10, 14, 18, 22, 26, 30, 34, 38)
- Correct option C: 10 questions (4, 8, 12, 16, 20, 24, 28, 32, 36, 40)
- Correct option D: 10 questions (1, 6, 9, 13, 17, 21, 25, 29, 33, 37)
- Longest consecutive run of one correct letter: below 3 throughout
