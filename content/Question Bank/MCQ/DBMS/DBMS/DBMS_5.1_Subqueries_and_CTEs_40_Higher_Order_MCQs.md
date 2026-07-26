# DBMS 5.1: Subqueries and CTEs — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Advanced Querying with SQL
- **Chapter:** Subqueries and CTEs
- **Scope:** All six Topic 5.1 subtopics in the attached course blueprint (What is a Subquery; Subqueries in WHERE; Subqueries in FROM; Correlated Subqueries; Common Table Expressions; Recursive CTEs)
- **SQL dialect:** PostgreSQL 16+
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every item begins with a recognisable reporting, validation, or hierarchy task. Whenever an answer depends on values, the source rows and column meanings are visible.
- **Evidence rule:** Students must trace inner and outer results, repair a shape or NULL defect, complete missing SQL, compare equivalent formulations, follow a correlation per outer row, or walk recursive levels.
- **Scope guard:** Only the six concepts explicitly taught in Topic 5.1 are assessed; PostgreSQL behaviour is used where the reading's simplified wording would otherwise overstate a syntax rule.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all six Topic 5.1 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Above an average nobody typed in

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Subquery  
**Is Curriculum Based:** No  
**Assessment type:** Single-value subquery tracing

A solar-equipment retailer lists the inverters it sells along with their price.

`inverters`

| model | price |
|---|---|
| Volt-A | 200 |
| Volt-B | 400 |
| Volt-C | 600 |

```sql
SELECT model FROM inverters
WHERE price > (SELECT AVG(price) FROM inverters);
```

Compute the inner average first, then select the surviving inverter model.

A. All three models — averages match everything.  
B. Volt-A only — the cheapest stands out.  
C. Volt-C only.
D. An error; a query cannot appear inside another.

### 2. Flags on the watchlist

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in WHERE  
**Is Curriculum Based:** No  
**Assessment type:** IN-subquery tracing

A port authority screens incoming vessels against a watchlist of flagged countries.

`vessels`

| vessel | flag_code |
|---|---|
| Kestrel | PA |
| Mira | LR |
| Onyx | IN |

`flag_watchlist`

| flag_code |
|---|
| PA |
| LR |

```sql
SELECT vessel FROM vessels
WHERE flag_code IN (SELECT flag_code FROM flag_watchlist);
```

Use the inner result as a membership list and select the matching vessels.

A. Kestrel and Mira.
B. Onyx only — IN excludes the list.  
C. All three vessels.  
D. None; IN cannot take a subquery.

### 3. The table that exists only mid-query

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in FROM  
**Is Curriculum Based:** No  
**Assessment type:** Derived-table identification

A cinema analyst writes:

```sql
SELECT t.hall, t.day_total
FROM (SELECT hall, SUM(amount) AS day_total
      FROM ticket_sales GROUP BY hall) t;
```

Identify what `t` names during execution and whether anything permanent is created.

A. A permanent table created by the statement.  
B. A typo the database ignores.  
C. A column of ticket_sales.  
D. The alias of a derived table.

### 4. The subquery that peeks at the outer row

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Correlated Subqueries  
**Is Curriculum Based:** No  
**Assessment type:** Correlation identification

A wholesaler's query:

```sql
SELECT o.order_id
FROM orders o
WHERE o.amount > (SELECT AVG(amount) FROM orders x
                  WHERE x.customer_id = o.customer_id);
```

Locate the outer-row dependency and select its consequence for evaluating the inner average.

A. The inner aggregate scans `orders`, the same base table used by the outer query.  
B. It references the outer row's `o.customer_id`, so its value depends on the current order.
C. Both queries read the same table, so the inner average must be recomputed for each row regardless of its references.  
D. Nothing; the query is uncorrelated.

### 5. Naming a query before using it

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Common Table Expressions  
**Is Curriculum Based:** No  
**Assessment type:** Syntax-purpose identification

A reporting query begins:

```sql
WITH big_shipments AS (
    SELECT * FROM shipments WHERE weight_kg > 500
)
SELECT shipment_id, weight_kg FROM big_shipments;
```

Classify `big_shipments` by its lifetime and role in the remaining statement.

A. Creates a permanent table named big_shipments.  
B. Renames the shipments table.  
C. Deletes the light shipments.  
D. Defines a named query.

### 6. The two halves of a recursive CTE

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Recursive CTEs  
**Is Curriculum Based:** No  
**Assessment type:** Anatomy understanding

A recursive CTE for an org chart has a first SELECT (the anchor, picking the starting person), UNION ALL, and a second SELECT that joins back to the CTE itself.

Distinguish the second `SELECT` from the anchor by identifying its role in successive rounds.

A. It sorts the anchor's rows.  
B. It removes all anchor rows, sorts the remaining hierarchy, and returns a finished result without repeating.  
C. The repeating step: each round joins the current recursive rows to the table again.
D. A backup copy of the anchor row.

### 7. Beating every bid, or just one

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in WHERE  
**Is Curriculum Based:** No  
**Assessment type:** ALL-operator interpretation

A land auction accepts a new bid only if it beats **every** existing bid.

`existing_bids`

| bid |
|---:|
| 300 |
| 450 |

The admission predicate is `new_bid > ALL (SELECT bid FROM existing_bids)`.

Choose the boundary that a new bid must cross.

A. Any bid above 300 — one comparison suffices.  
B. Only bids above 450.
C. Only bids exactly equal to 450.  
D. Every bid, because `ALL` tests only whether the inner query returns rows.

### 8. Where the inner query may sit

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Subquery  
**Is Curriculum Based:** No  
**Assessment type:** Placement identification

A trainee asks whether subqueries require a separate query language from ordinary `SELECT`.

Choose the response that also accounts for where the nested result may be used.

A. It is an ordinary `SELECT` nested in parentheses; its result can act as a value, list, or derived table.  
B. It uses a separate query language mode enabled whenever parentheses contain SQL, and only scalar results may leave that mode.  
C. Subqueries may only appear in UPDATE statements.  
D. Subqueries are limited to one per database.

### 9. The same threshold, named instead of nested

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Common Table Expressions  
**Is Curriculum Based:** No  
**Assessment type:** Rewrite equivalence

A nested query filtering rentals above the average is rewritten:

```sql
WITH avg_rent AS (SELECT AVG(rent) AS a FROM listings)
SELECT flat_code FROM listings, avg_rent WHERE rent > a;
```

Compare the two formulations by result rather than by layout.

A. The CTE version returns more rows.  
B. The CTE version ignores the average.  
C. Same result.
D. The versions cannot both be valid.

### 10. Studios with at least one vacancy

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Correlated Subqueries  
**Is Curriculum Based:** No  
**Assessment type:** Correlated-EXISTS tracing

A film-industry job board tracks which studios currently have open crew roles.

`film_studios`

| studio_id | studio_name |
|---|---|
| 1 | Grey Lantern |
| 2 | Cutaway Films |
| 3 | Ninth Reel |

`open_roles`

| role_id | studio_id | role |
|---|---|---|
| 1 | 1 | Colourist |
| 2 | 3 | Gaffer |
| 3 | 3 | Editor |

```sql
SELECT studio_name FROM film_studios s
WHERE EXISTS (SELECT 1 FROM open_roles r WHERE r.studio_id = s.studio_id);
```

Trace the correlated existence check once per studio and select the deduplicated studio list.

A. Grey Lantern and Ninth Reel.  
B. Cutaway Films only, because `EXISTS` retains the studios for which the correlated search finds no row.  
C. All three studios.  
D. Ninth Reel twice.

### 11. The list with a hole in it

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in WHERE  
**Is Curriculum Based:** No  
**Assessment type:** NOT-IN-NULL prediction

A logistics company checks which depots are unaffected by flooding before rerouting deliveries.

`depots`

| depot |
|---|
| Central |
| Harbour |

`flooded_zones`

| depot |
|---|
| Harbour |
| NULL |

```sql
SELECT depot FROM depots
WHERE depot NOT IN (SELECT depot FROM flooded_zones);
```

Predict the report outcome caused by the `NULL` in the inner list.

A. Central, because its name differs from the only non-NULL flooded depot.  
B. Central and Harbour.  
C. An error over the NULL.  
D. No rows at all.

### 12. Totals meet their branches

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in FROM  
**Is Curriculum Based:** No  
**Assessment type:** Derived-table join construction

A courier firm wants each branch's name beside its total parcels, computed from `parcel_log(parcel_id, branch_id)` and `branches(branch_id, branch_name)`.

Select the query that first aggregates parcels by branch and then attaches the branch name.

A. `SELECT branch_name, total FROM branches JOIN parcel_log;`  
B. `SELECT b.branch_name, t.total FROM (SELECT branch_id, COUNT(*) AS total FROM parcel_log GROUP BY branch_id) t JOIN branches b ON b.branch_id = t.branch_id;`
C. `SELECT branch_name, COUNT(*) FROM branches;`  
D. `SELECT b.branch_name, t.total FROM (SELECT branch_id, COUNT(*) AS total FROM parcel_log GROUP BY branch_id) t JOIN branches b ON b.branch_id = t.total AND t.total >= 0;`

### 13. Inside first, outside second

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Subquery  
**Is Curriculum Based:** No  
**Assessment type:** Structure identification

A query reads: `SELECT name FROM sanctuaries WHERE area_ha > (SELECT AVG(area_ha) FROM sanctuaries);`

Identify the inner statement and the value it supplies to the outer filter.

A. The parenthesized inner SELECT is the subquery.
B. The outer query runs first and feeds rows inward.  
C. Both queries run independently and merge results.  
D. The parentheses mark a comment.

### 14. Spot the correlation

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Correlated Subqueries  
**Is Curriculum Based:** No  
**Assessment type:** Correlated-versus-uncorrelated discrimination

Two subqueries from a stable-management system:

1. `WHERE feed_kg > (SELECT AVG(feed_kg) FROM horses)`  
2. `WHERE feed_kg > (SELECT AVG(feed_kg) FROM horses h2 WHERE h2.stable_id = h.stable_id)`

Find the version whose inner average changes with the current outer horse.

A. Both, because both inner statements aggregate rows from `horses`.  
B. Query 1, because it comes first.  
C. Query 2.
D. Neither is correlated.

### 15. Steps that read like a recipe

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Common Table Expressions  
**Is Curriculum Based:** No  
**Assessment type:** Chained-CTE mechanics

A revenue report begins:

```sql
WITH paid AS (SELECT * FROM invoices WHERE status = 'paid'),
     monthly AS (SELECT month, SUM(amount) AS m_total FROM paid GROUP BY month)
SELECT * FROM monthly WHERE m_total > 100000;
```

Identify the dependency permitted between `paid` and `monthly`.

A. Each CTE is independent and cannot read a CTE declared earlier in the same `WITH` clause.  
B. The second CTE overwrites the first.  
C. Only one CTE is allowed per statement.  
D. CTE chaining.

### 16. Two pieces with different jobs

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Recursive CTEs  
**Is Curriculum Based:** No  
**Assessment type:** Syntax-requirement reasoning

A hierarchy query is written as `WITH RECURSIVE hierarchy AS (anchor_query UNION ALL recursive_query) SELECT * FROM hierarchy`. PostgreSQL also permits `UNION` in recursive CTEs, but this query intentionally uses `UNION ALL`.

Select the accurate role of `RECURSIVE` and of `UNION ALL` in the shown pattern.

A. They are optional decorations in modern PostgreSQL.  
B. `RECURSIVE` permits self-reference; `UNION ALL` retains the anchor and every recursive row in this pattern.  
C. `RECURSIVE` sorts the tree by depth, while `UNION ALL` removes repeated rows before every recursive round begins automatically.  
D. Both exist only for backwards compatibility.

### 17. The number that goes stale

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Subquery  
**Is Curriculum Based:** No  
**Assessment type:** Hardcoding-versus-subquery judgment

Two versions of a fleet report exist. Version 1: `WHERE mileage > 48200` — the fleet average someone computed last quarter and pasted in. Version 2: `WHERE mileage > (SELECT AVG(mileage) FROM fleet)`.

Choose the version whose threshold remains aligned with changing fleet data.

A. The subquery recomputes the current average every run.
B. Hardcoded numeric comparisons require a sort before the threshold can be applied.  
C. Version 1 automatically refreshes the literal whenever fleet rows change.  
D. Writing 48200 as a literal instructs PostgreSQL to recalculate the average.

### 18. The nameless table that wouldn't run

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in FROM  
**Is Curriculum Based:** No  
**Assessment type:** Error diagnosis and repair

A brewery analyst's query fails:

```sql
SELECT t.style, t.avg_rating
FROM (SELECT style, AVG(rating) AS avg_rating
      FROM tastings GROUP BY style);
```

The selected columns use qualifier `t`, but no `FROM` item has that name. Identify the smallest repair after the closing parenthesis.

A. `GROUP BY` is not permitted inside a derived table that is read by an outer query.  
B. The outer SELECT must use `*`.  
C. Add `AS t` so the qualifier names the derived table.
D. AVG cannot be aliased.

### 19. Same city as the flagship

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in WHERE  
**Is Curriculum Based:** No  
**Assessment type:** Scalar-comparison tracing

A retail chain compares each outlet's city to its flagship store's city.

`flagship_store`

| city |
|---|
| Pune |

`outlets`

| outlet | city |
|---|---|
| O-1 | Pune |
| O-2 | Surat |
| O-3 | Pune |

```sql
SELECT outlet FROM outlets
WHERE city = (SELECT city FROM flagship_store);
```

Evaluate the scalar city result and select the matching outlets.

A. O-2 only.  
B. All three outlets.  
C. Nothing; cities cannot be compared.  
D. O-1 and O-3.

### 20. Filter the summary, not the rows

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in FROM  
**Is Curriculum Based:** No  
**Assessment type:** Derived-table filtering trace

An orchard co-op computes per-variety averages, then filters them:

```sql
SELECT variety, avg_price
FROM (SELECT variety, AVG(price) AS avg_price
      FROM apple_lots GROUP BY variety) t
WHERE avg_price > 200;
```

The derived table exposes:

| variety | avg_price |
|---|---:|
| Fuji | 120 |
| Honeycrisp | 340 |

Apply the outer predicate to these summary rows.

A. Both fruit varieties listed.  
B. (Honeycrisp, 340).
C. (Fuji, 120).  
D. An empty result.

### 21. One row, one column, one value

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Subquery  
**Is Curriculum Based:** No  
**Assessment type:** Shape-requirement identification

A query compares `WHERE budget > (subquery)` using the `>` operator.

Determine the result shape required by a scalar `>` comparison.

A. Exactly one row with one column.
B. At least ten rows.  
C. The same columns as the outer table.  
D. Any shape; the database averages whatever comes back.

### 22. A thousand little queries

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Correlated Subqueries  
**Is Curriculum Based:** No  
**Assessment type:** Cost reasoning

Two report drafts over a 1,000-row `claims` table: one uses an uncorrelated average subquery, the other a correlated per-claimant average.

Choose the execution dependency that can make the correlated version more expensive.

A. Correlated subqueries use more keywords.  
B. Averages are slow in any position.  
C. The uncorrelated value is independent of the current outer row and can be reused.
D. Correlation guarantees identical work to an uncorrelated scalar subquery, because the optimizer always stores one shared average.

### 23. Why the nesting got retired

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Common Table Expressions  
**Is Curriculum Based:** No  
**Assessment type:** Preference rationale

A team rewrites a triple-nested report query as three chained CTEs.

Identify the benefit that remains valid without assuming either form is inherently faster.

A. CTEs always execute faster than subqueries.  
B. CTEs bypass permissions.  
C. Nested queries stop working past two levels.  
D. Readability: each step gets a name.

### 24. Walk the whole crew tree

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Recursive CTEs  
**Is Curriculum Based:** No  
**Assessment type:** Recursive-walk tracing

A mountaineering expedition tracks the reporting chain among its crew members.

`expedition_crew`

| id | name | leader_id |
|---|---|---|
| 1 | Vera | NULL |
| 2 | Sam | 1 |
| 3 | Lin | 1 |
| 4 | Ott | 3 |

A recursive CTE anchors on Vera and repeatedly joins to find everyone whose `leader_id` is in the current result.

Select the row count and level-by-level discovery sequence.

A. 1 — recursion stops at the anchor.  
B. 4 — Vera, then Sam and Lin at the next level, then Ott; order within a level is unspecified.
C. 3 — the anchor is excluded.  
D. 4 — Vera, Sam, Lin, and Ott are returned automatically in alphabetical order by the recursive CTE.

### 25. How long the name lives

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Common Table Expressions  
**Is Curriculum Based:** No  
**Assessment type:** Scope reasoning

On Monday an analyst runs `WITH vip_guests AS (SELECT guest_id FROM guests WHERE tier = 'VIP') SELECT * FROM vip_guests;`. On Tuesday, `SELECT * FROM vip_guests;` alone produces “relation does not exist.”

Explain why a CTE name cannot be queried by a later, separate statement.

A. A CTE exists only for the one statement defining it.
B. CTE names expire after 24 hours.  
C. The database automatically drops every CTE at midnight.  
D. CTEs are invisible on Tuesdays.

### 26. The climb instead of the descent

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Recursive CTEs  
**Is Curriculum Based:** No  
**Assessment type:** Direction-reversal reasoning

A working recursive CTE lists everyone *below* a regional head in a sales hierarchy. A new request: list the *chain of managers above* one named salesperson instead.

Choose the anchor and relationship-direction changes needed to reverse the walk.

A. Recursion can only follow child references downward, so an upward report requires copying the hierarchy into a second table.  
B. Only the ORDER BY changes.  
C. The anchor becomes the named salesperson; the recursive join follows each manager reference upward.
D. UNION ALL becomes UNION.

### 27. One value expected, three arrived

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in WHERE  
**Is Curriculum Based:** No  
**Assessment type:** Operator-choice reasoning

A query fails: `WHERE region = (SELECT region FROM storm_alerts)` — the subquery currently returns three regions.

Select the operator repair that accepts all three returned regions without deleting valid alerts.

A. Delete two of the storm alerts.  
B. Run the query three times.  
C. Wrap the subquery in parentheses twice.  
D. Change `=` to `IN`.

### 28. What the outer query may call the columns

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in FROM  
**Is Curriculum Based:** No  
**Assessment type:** Column-visibility reasoning

A derived table is written as `(SELECT zone, SUM(fee) AS zone_total FROM tolls GROUP BY zone) z`.

Treat the derived table's `SELECT` list as its interface and identify the visible columns.

A. `fee` and `tolls` directly.  
B. `z.zone` and `z.zone_total`.
C. Any column of the tolls table.  
D. Only `z.zone`; aggregates stay private.

### 29. Find the query inside the query

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** What is a Subquery  
**Is Curriculum Based:** No  
**Assessment type:** Statement reading

```sql
SELECT trail_name
FROM trails
WHERE length_km > (SELECT MAX(length_km) FROM trails WHERE district = 'Coastal');
```

Locate the nested statement and identify the scalar threshold it computes.

A. The parenthesized SELECT after `>`.
B. `SELECT trail_name` — the first words are always the subquery.  
C. `FROM trails` — table references are subqueries.  
D. The whole statement is one indivisible query.

### 30. Above its own category's bar

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Correlated Subqueries  
**Is Curriculum Based:** No  
**Assessment type:** Pattern-construction selection

A lighting store wants lamps priced above **their own category's** average — desk lamps against the desk average, floor lamps against the floor average.

Complete the moving threshold with the required outer-row correlation.

A. `WHERE price > (SELECT AVG(price) FROM lamps)` — one company-wide comparison value  
B. `WHERE price > ALL (SELECT price FROM lamps)` — beat everything.  
C. `WHERE price > (SELECT AVG(price) FROM lamps l2 WHERE l2.category = l.category)`
D. `WHERE category = price`.

### 31. Write once, use twice

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Common Table Expressions  
**Is Curriculum Based:** No  
**Assessment type:** Reuse benefit identification

A festival report needs the same filtered set — this year's ticketed events — in two places: once to total revenue, once to count venues.

Choose the design that centralizes the filter while keeping both consumers in one statement.

A. It emails the result to both teams.  
B. It runs the report twice automatically.  
C. Each consumer must contain a separate copy of the filter logic because a CTE name can be referenced only once per statement.  
D. Define the filtered event query once as a CTE named `ticketed` and reference that name twice.

### 32. What finally stops the loop

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Recursive CTEs  
**Is Curriculum Based:** No  
**Assessment type:** Termination reasoning

A recursive CTE walks an acyclic component hierarchy: assemblies contain sub-assemblies, which eventually end in parts.

Identify the data-driven termination condition for this acyclic walk.

A. The number of anchor rows establishes a fixed maximum number of recursive rounds.  
B. In this acyclic hierarchy, a recursive round eventually finds no child rows.
C. `UNION ALL` removes every previously visited row, so a cycle cannot continue the recursion.  
D. The anchor query runs again to cancel it.

### 33. The venues nobody booked

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Correlated Subqueries  
**Is Curriculum Based:** No  
**Assessment type:** NOT-EXISTS construction

`venues(venue_id, name)` and `bookings(booking_id, venue_id)` exist. Marketing wants venues with **no** bookings at all.

Select the correlated anti-membership pattern.

A. `SELECT v.name FROM venues v WHERE NOT EXISTS (SELECT 1 FROM bookings b WHERE b.venue_id = v.venue_id);`
B. `SELECT v.name FROM venues v WHERE EXISTS (SELECT 1 FROM bookings b WHERE b.venue_id = v.venue_id AND b.booking_id IS NOT NULL);`  
C. `SELECT venue_id FROM bookings WHERE venue_id IS NULL;`  
D. `SELECT name FROM venues JOIN bookings USING (venue_id);`

### 34. Fixed floors versus bottomless trees

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Recursive CTEs  
**Is Curriculum Based:** No  
**Assessment type:** Tool-necessity discrimination

Four data shapes are on a review board's desk. Choose the one whose number of relationship hops is unknown when the SQL is written.

A. Orders joined to customers — one hop.  
B. Orders to customers to cities, with exactly two known relationships that are both resolved using ordinary joins.  
C. A referral network where members recruit members to an unknown depth.
D. A two-level menu of categories and items.

### 35. At least one, or every single one

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in WHERE  
**Is Curriculum Based:** No  
**Assessment type:** ANY-versus-ALL tracing

Rival gyms expose these membership fees:

| monthly_fee |
|---:|
| 300 |
| 450 |

A pricing analyst tests proposed fees 250, 320, and 500 against `> ANY (subquery)`.

Evaluate each proposal against the existential comparison.

A. Only 500 — ANY means all.  
B. All three fees.  
C. None of them.  
D. 320 and 500.

### 36. Trace the join to the derived totals

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in FROM  
**Is Curriculum Based:** No  
**Assessment type:** Derived-join tracing

A beachfront ice-cream vendor tracks sales at each of its kiosks.

`kiosks`

| kiosk_id | kiosk_name |
|---|---|
| 1 | Pier Stand |
| 2 | Park Cart |

`scoop_sales`

| sale_id | kiosk_id | amount |
|---:|---:|---:|
| 1 | 1 | 1000 |
| 2 | 1 | 800 |
| 3 | 2 | 950 |

```sql
SELECT k.kiosk_name, t.total
FROM (SELECT kiosk_id, SUM(amount) AS total
      FROM scoop_sales GROUP BY kiosk_id) t
JOIN kiosks k ON k.kiosk_id = t.kiosk_id
WHERE t.total > 1000;
```

Compute the derived totals, attach the kiosk names, and apply the final threshold.

A. Both kiosks with their totals.  
B. One row: Pier Stand, 1800.
C. Park Cart, 950.  
D. An error; derived tables cannot be filtered after joining.

### 37. Above their own average, by the numbers

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Correlated Subqueries  
**Is Curriculum Based:** No  
**Assessment type:** Correlated tracing over data

A lighting store's catalog lists each lamp's category and price.

`lamps`

| name | category | price |
|---|---|---|
| Nova | desk | 900 |
| Pico | desk | 500 |
| Arc | floor | 1200 |
| Halo | floor | 800 |

```sql
SELECT name FROM lamps l
WHERE price > (SELECT AVG(price) FROM lamps l2
               WHERE l2.category = l.category);
```

Recompute the comparison bar per category and select the lamps above their local average.

A. Nova and Arc.
B. Nova, Arc, and Halo.  
C. Arc only — the single most expensive lamp.  
D. Pico and Halo — the below-average pair.

### 38. Two stages, one number

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Common Table Expressions  
**Is Curriculum Based:** No  
**Assessment type:** Chained-CTE tracing

A yacht charter company logs the amount billed for each trip.

`charter_trips`

| trip_id | amount |
|---:|---:|
| 1 | 100 |
| 2 | 300 |
| 3 | 500 |

```sql
WITH big AS (SELECT amount FROM charter_trips WHERE amount > 150),
     summary AS (SELECT AVG(amount) AS avg_big FROM big)
SELECT avg_big FROM summary;
```

Trace both named stages and select the final scalar value.

A. 300 — the average of all three trips.  
B. 500 — the maximum.  
C. 400.
D. 150 — the filter's own threshold.

### 39. Making "not in" safe

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Subqueries in WHERE  
**Is Curriculum Based:** No  
**Assessment type:** Defensive-pattern selection

After the flooded-zones incident (a NULL in the subquery emptied the whole NOT IN report), a data team standardizes a safer pattern for "rows not in that list."

Choose the guarded `NOT IN` repair that prevents an inner `NULL` from poisoning the comparison.

A. `WHERE key NOT IN (SELECT key FROM blocked_values WHERE key IS NULL OR key IS NOT NULL)`  
B. `WHERE key NOT IN (SELECT key FROM blocked_values WHERE key IS NOT NULL)`  
C. `WHERE key UNION ALL (SELECT key FROM blocked_values)`  
D. `WHERE NOT EXISTS (SELECT 1 FROM blocked_values)`

### 40. Build the reporting chain

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Advanced Querying with SQL  
**Subtopic:** Recursive CTEs  
**Is Curriculum Based:** No  
**Assessment type:** Integrated construction

A shipping line stores this acyclic reporting hierarchy:

`crew`

| id | name | reports_to |
|---:|---|---:|
| 1 | Captain Rao | NULL |
| 2 | Mira | 1 |
| 3 | Dev | 1 |
| 4 | Ishan | 2 |

The report needs Captain Rao and every crew member beneath her, regardless of depth.

Select the recursive statement that returns all four names.

A. `SELECT name FROM crew WHERE reports_to = 1;`  
B. `WITH chain AS (SELECT * FROM crew WHERE id = 1) SELECT name FROM chain;`  
C. `WITH RECURSIVE chain AS (SELECT id, name, reports_to FROM crew WHERE id = 1 UNION ALL SELECT c.id, c.name, c.reports_to FROM crew c JOIN chain ch ON c.id = ch.reports_to) SELECT name FROM chain ORDER BY name;`  
D. `WITH RECURSIVE chain AS (SELECT id, name, reports_to FROM crew WHERE id = 1 UNION ALL SELECT c.id, c.name, c.reports_to FROM crew c JOIN chain ch ON c.reports_to = ch.id) SELECT name FROM chain;`

---

## Instructor Key

### 1. C

The uncorrelated inner query runs first and yields one number: 400. The outer query then reads as `WHERE price > 400`, which only Volt-C satisfies. The subquery is a computed comparison value, nothing more exotic.

### 2. A

The subquery produces the list {PA, LR}; IN keeps outer rows whose flag appears in it. Kestrel and Mira match; Onyx's flag is not on the watchlist.

### 3. D

The parenthesized result is a derived table, and `t` is the alias used to qualify its columns. PostgreSQL 16+ can omit an alias when no such qualifier is used, but once the outer query writes `t.hall`, an alias named `t` must exist.

### 4. B

The correlation is the reference to `o.customer_id`: the subquery's meaning changes with each outer row, so no single precomputed value can serve. Sharing a table name (C) is incidental; reaching *outward* is the defining sign.

### 5. D

WITH introduces a common table expression: a query given a name, usable like a table for the rest of the statement. Nothing is stored, renamed, or deleted.

### 6. C

The anchor finds the starting rows; the recursive member is the engine. Each round joins the current working rows back to the table to fetch the next level, and the walk halts when a round contributes nothing.

### 7. B

`> ALL` is a universal condition: the bid must exceed every value the subquery returns, so the maximum (450) becomes the effective bar. Exceeding "at least one" is ANY's job, not ALL's.

### 8. A

Subqueries are ordinary SELECTs in specific positions — a comparison value or list in WHERE, a derived table in FROM. Same syntax, new placement; that is the chapter's demystifying point.

### 9. C

The rewrite relocates the identical logic: the average is computed once and named, and the main query reads in execution order. Equivalent result; the currency is clarity, not row counts.

### 10. A

Per studio, EXISTS asks whether any `open_roles` row points at it: Grey Lantern (one role) and Ninth Reel (two) pass; Cutaway fails. EXISTS is a yes/no test, so Ninth Reel's two roles still produce one row — no duplication.

### 11. D

NOT IN unrolls to `depot <> 'Harbour' AND depot <> NULL`, and the second comparison is unknown for every depot — so no row can ever pass. One NULL in the list silently empties the report, which is precisely the chapter's "extra care" warning.

### 12. B

The aggregation happens inside the derived table — one row per branch with its count — and that result then joins to `branches` on the shared key like any real table. Option A joins without keys or aggregation; option D shadows a real table's name with unrelated contents.

### 13. A

Uncorrelated means self-contained: the inner query executes first, once, producing the average; the outer query then treats it as a literal number. Inside-out is the reading order for nested subqueries.

### 14. C

The tell is an outer reference: `h.stable_id` belongs to the outer query's row, so query 2's average is per-stable, recomputed conceptually per row. Query 1 is closed over its own table and runs once.

### 15. D

CTEs chain: each may reference those defined before it, building a top-down pipeline of named stages. The main query at the bottom consumes the final stage.

### 16. B

`RECURSIVE` permits the CTE to reference itself. In this hierarchy pattern, `UNION ALL` combines the anchor with every row produced by later rounds without a duplicate-removal pass. PostgreSQL can also use `UNION` in a recursive CTE, so `UNION ALL` is a design choice here, not the keyword that authorizes recursion.

### 17. A

The pasted number is a snapshot; the fleet is not. The subquery keeps the threshold tied to the live data — the report's meaning ("above the current average") stays true as rows change.

### 18. C

The failure is the unresolved qualifier, not the mere presence of an unaliased subquery: PostgreSQL 16+ allows an omitted derived-table alias. Adding `AS t` after the closing parenthesis defines the exact qualifier already used by the outer `SELECT`.

### 19. D

The single-row subquery yields 'Pune', and the outer equality keeps both Pune outlets. A scalar subquery in a comparison behaves exactly like the literal it produces.

### 20. B

To the outer query, the derived table *is* the data: two computed rows. Its WHERE then filters those summary rows — filtering after aggregation, achieved by putting the aggregation a level down.

### 21. A

Comparison operators need a scalar: one row, one column. That shape requirement is why multi-row subqueries pair with IN, ANY, or ALL instead.

### 22. C

The costs differ in multiplicity: once versus once-per-row. A thousand outer rows can mean a thousand evaluations of the correlated inner query — the price paid for each row getting its own answer.

### 23. D

The cited gain is human: named steps in reading order. The deepest-parentheses-first decoding of nested queries is what the CTE form eliminates.

### 24. B

The anchor yields Vera. The next round finds Sam and Lin, and the following round finds Ott through Lin; a final round finds nothing. Four rows are discovered level by level, although SQL does not guarantee Sam-versus-Lin order without an explicit ordering rule.

### 25. A

A CTE is part of one statement's text, not an object in the database. When the statement ends, the name is gone; Tuesday's bare SELECT is asking for a table that never existed.

### 26. C

Same machinery, opposite direction: anchor at the bottom, and the recursive join now treats the current person's `manager_id` as the link to the *next* row's `id`. The walk climbs until the top manager's NULL ends it.

### 27. D

The subquery legitimately returns a list, so the operator must accept a list: IN. Equality's one-value expectation was the mismatch, not the data.

### 28. B

A derived table's interface is its SELECT list: `zone` and the alias `zone_total`, reachable through `z`. The inner table's other columns ended their journey inside the parentheses.

### 29. A

The subquery is the parenthesized SELECT in the comparison: it condenses the coastal district's trails to one number — the maximum length — which the outer query uses as an ordinary bar to clear.

### 30. C

"Its own category" is inherently per-row: the bar moves with the row being judged, which is exactly what the correlated reference `l2.category = l.category` encodes. The global average (A) judges every lamp against one bar.

### 31. D

One named definition, referenced wherever needed within the statement: totals and counts both read `ticketed`. The duplicate-logic risk — two copies drifting apart under maintenance — disappears with the second copy.

### 32. B

Recursion inherits its stopping point from the data: leaves have no children, so some round returns empty, and an empty round is the halt condition. No counter or limit is involved — structure ends the walk.

### 33. A

The anti-join in correlated form: for each venue, check that no booking points at it. Option B keeps exactly the wrong venues; option C searches bookings for NULLs, a different question entirely.

### 34. C

Recursion earns its keep where depth is unknown and unbounded: referral chains grow arbitrarily, so no fixed number of self-joins can be written in advance. Shapes A, B, and D have known depths — ordinary joins cover them.

### 35. D

`> ANY` is existential: beat at least one returned value. The 300 makes 320 and 500 passers; 250 beats nothing. The contrast with ALL — where only 500 survives — is the pair's entire teaching point.

### 36. B

Three stages compose: the derived table sums per kiosk, the join attaches names, and the final WHERE tests the computed totals. Park Cart's 950 falls at the last gate, leaving one row.

### 37. A

Two categories, two bars, computed per row: desk 700, floor 1000. Nova and Arc clear their own bars; Pico and Halo sit below theirs. One query, four evaluations, category-local judgment throughout.

### 38. C

Stage one keeps 300 and 500; stage two averages the survivors: 400. Each CTE consumes its predecessor — the trace is simply the pipeline run by hand.

### 39. B

Option B is the smallest repair to the existing `NOT IN` pattern: its inner filter guarantees that every compared value is non-NULL. A correlated `NOT EXISTS` can also be safe, but option D is uncorrelated and therefore does not express the required row-by-row exclusion.

### 40. D

The full pattern is present: `RECURSIVE`, an anchor selecting Captain Rao by `id = 1`, `UNION ALL`, and a recursive member joining children to the current level. Options A and C return only direct reports, while option B returns only the anchor.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Subquery and CTE tracing over shown data | 1, 2, 10, 11, 19, 20, 24, 35, 36, 37, 38 |
| Construction and pattern selection | 12, 30, 33, 39, 40 |
| Error diagnosis and repair | 18, 25, 27 |
| Mechanism, anatomy, and scope reasoning | 3, 4, 5, 6, 8, 13, 14, 15, 16, 21, 26, 28, 29, 31, 32 |
| Cost, preference, and necessity judgment | 7, 9, 17, 22, 23, 34 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| What is a Subquery | 1, 8, 13, 17, 21, 29 | 6 |
| Subqueries in WHERE | 2, 7, 11, 19, 27, 35, 39 | 7 |
| Subqueries in FROM | 3, 12, 18, 20, 28, 36 | 6 |
| Correlated Subqueries | 4, 10, 14, 22, 30, 33, 37 | 7 |
| Common Table Expressions | 5, 9, 15, 23, 25, 31, 38 | 7 |
| Recursive CTEs | 6, 16, 24, 26, 32, 34, 40 | 7 |

Questions 1–10 collectively cover all six Topic 5.1 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (5, 8, 13, 14, 19, 21, 23, 27, 29, 31)
- Intermediate: 26 questions
- Advanced: 4 questions (22, 32, 37, 40)
- Correct option A: 10 questions (2, 8, 10, 13, 17, 21, 25, 29, 33, 37)
- Correct option B: 10 questions (4, 7, 12, 16, 20, 24, 28, 32, 36, 39)
- Correct option C: 10 questions (1, 6, 9, 14, 18, 22, 26, 30, 34, 38)
- Correct option D: 10 questions (3, 5, 11, 15, 19, 23, 27, 31, 35, 40)
- Longest consecutive run of one correct letter: below 3 throughout
