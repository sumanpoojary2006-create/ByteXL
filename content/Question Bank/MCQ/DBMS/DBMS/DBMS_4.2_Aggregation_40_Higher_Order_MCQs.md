# DBMS 4.2: Aggregation — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** SQL for Data Retrieval and Analytics
- **Chapter:** Aggregation
- **Scope:** All four Topic 4.2 subtopics in the attached course blueprint (Aggregate Functions; Grouping Data; Filtering Groups; Combining Aggregation with Sorting, Filtering, and Joins)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every item begins with a recognisable reporting task. Questions that depend on values show the relevant tables and rows, while query-selection items define their schema and business rule.
- **Evidence rule:** Students must trace aggregates, complete or repair grouped SQL, compare pipeline stages, expose a boundary defect, or diagnose grouping granularity—not recall isolated definitions.
- **Scope guard:** Only aggregation concepts taught in Topic 4.2 are assessed; joins appear only in the limited join-then-group role introduced by this chapter.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all four Topic 4.2 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Two counts that disagree on the same table

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** Output tracing with NULL awareness

An EV charging network logs every charging session. Sessions interrupted by a power cut have no recorded energy figure.

`charge_sessions`

| session_id | station | kwh_delivered |
|---|---|---|
| 1 | Riverside | 12.5 |
| 2 | Riverside | NULL |
| 3 | Airport | 30.0 |
| 4 | Airport | NULL |
| 5 | Depot | 22.0 |

```sql
SELECT COUNT(*) AS sessions, COUNT(kwh_delivered) AS metered
FROM charge_sessions;
```

Calculate both counts from the visible sessions.

A. `sessions = 5`, `metered = 5`  
B. `sessions = 5`, `metered = 3`  
C. `sessions = 3`, `metered = 3`  
D. `sessions = 3`, `metered = 5`

### 2. The SELECT list a grouped query cannot accept

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Grouping Data  
**Is Curriculum Based:** No  
**Assessment type:** Invalid-query identification

A freight operator summarizes cargo by route from `shipments(shipment_id, route, weight_kg)`. Four report drafts are proposed.

Identify the draft whose SELECT list has no single value per route.

A. `SELECT route, SUM(weight_kg) AS total_weight FROM shipments GROUP BY route;`  
B. `SELECT route, COUNT(*) FROM shipments GROUP BY route;`  
C. `SELECT route, MAX(weight_kg) FROM shipments GROUP BY route;`  
D. `SELECT route, shipment_id, SUM(weight_kg) FROM shipments GROUP BY route;`

### 3. Trace a query that filters twice

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Filtering Groups  
**Is Curriculum Based:** No  
**Assessment type:** Two-stage filter tracing

A podcast platform measures episode performance.

`episodes`

| episode_id | show | downloads |
|---|---|---|
| 1 | Night Signal | 900 |
| 2 | Night Signal | 400 |
| 3 | Deep Field | 1500 |
| 4 | Deep Field | 200 |
| 5 | Waypoint | 300 |

```sql
SELECT show, SUM(downloads) AS total
FROM episodes
WHERE downloads >= 400
GROUP BY show
HAVING SUM(downloads) > 1000;
```

Trace the row filter, grouping, and group filter in sequence.

A. Night Signal 1300 and Deep Field 1500  
B. Night Signal 1300 and Deep Field 1700  
C. Deep Field 1500 only  
D. Night Signal 1300, Deep Field 1700, and Waypoint 300

### 4. One alias, two different verdicts

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Combining Aggregation with Sorting, Filtering, and Joins  
**Is Curriculum Based:** No  
**Assessment type:** Execution-order explanation

An analyst at a ride-hailing company defines `SUM(fare) AS fare_total` in a grouped query. Writing `ORDER BY fare_total` works, yet `WHERE fare_total > 500` raises an error.

Choose the execution-order explanation that accounts for both outcomes.

A. `WHERE` recognizes aliases only when they are written in uppercase.  
B. `ORDER BY` executes before `WHERE`, so only `ORDER BY` sees the alias.  
C. `WHERE` runs before SELECT; `ORDER BY` runs afterward.  
D. Aggregate results may be sorted but cannot be filtered at any query stage.

### 5. Extremes on a date column

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** Non-numeric aggregate tracing

A solar farm records panel inspections.

`inspections`

| inspection_id | panel | inspected_on |
|---|---|---|
| 1 | P-01 | 2025-03-14 |
| 2 | P-07 | 2025-01-30 |
| 3 | P-03 | 2025-06-02 |
| 4 | P-07 | 2025-04-19 |

```sql
SELECT MIN(inspected_on) AS first_check, MAX(inspected_on) AS last_check
FROM inspections;
```

Record the earliest and latest inspection dates.

A. An error, because `MIN` and `MAX` accept only numeric columns  
B. `2025-03-14` and `2025-04-19`, the first and last rows inserted  
C. `2025-01-30` and `2025-06-02`  
D. `2025-06-02` and `2025-01-30`

### 6. Complete the loyalty threshold

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Filtering Groups  
**Is Curriculum Based:** No  
**Assessment type:** Missing-clause completion with boundary

A museum wants the member IDs of everyone who has visited three or more times, from `visits(visit_id, member_id, visited_on)`.

Complete `SELECT member_id FROM visits ...` so the boundary member qualifies.

A. `GROUP BY member_id HAVING COUNT(*) >= 3`  
B. `WHERE COUNT(*) >= 3 GROUP BY member_id ORDER BY member_id`  
C. `GROUP BY member_id HAVING COUNT(*) > 3`  
D. `HAVING member_id >= 3`  

### 7. How many rows survive a two-column grouping

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Grouping Data  
**Is Curriculum Based:** No  
**Assessment type:** Group-count prediction

An airline's punctuality team studies delays.

`delays`

| flight_id | carrier | origin | delay_min |
|---|---|---|---|
| 1 | Aria | BLR | 10 |
| 2 | Aria | BLR | 25 |
| 3 | Aria | DEL | 0 |
| 4 | Nimbus | BLR | 40 |
| 5 | Nimbus | DEL | 15 |
| 6 | Nimbus | DEL | 5 |

```sql
SELECT carrier, origin, AVG(delay_min)
FROM delays
GROUP BY carrier, origin;
```

Count the carrier–origin groups actually formed.

A. 2, one per carrier  
B. 6, one per flight  
C. 12, one per carrier–origin pairing whether or not it occurs  
D. 4, one per carrier–origin combination present in the data

### 8. Roll a join up into city totals

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Combining Aggregation with Sorting, Filtering, and Joins  
**Is Curriculum Based:** No  
**Assessment type:** Join-plus-aggregate tracing

A plant nursery delivers crates to garden stores.

`stores`

| store_id | city |
|---|---|
| 1 | Pune |
| 2 | Pune |
| 3 | Nagpur |

`deliveries`

| delivery_id | store_id | crates |
|---|---|---|
| 10 | 1 | 40 |
| 11 | 2 | 25 |
| 12 | 3 | 60 |
| 13 | 1 | 35 |

```sql
SELECT s.city, SUM(d.crates) AS total_crates
FROM deliveries d
JOIN stores s ON d.store_id = s.store_id
GROUP BY s.city;
```

Roll the joined delivery rows into city totals.

A. Pune 65 and Nagpur 60  
B. Pune 100 and Nagpur 60  
C. A single row with 160  
D. Four rows, one per delivery

### 9. An average that skips a blank

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** NULL-handling computation

A fitness studio collects session ratings; one member skipped the rating step.

`trainer_ratings`

| rating_id | trainer | stars |
|---|---|---|
| 1 | Kabir | 4 |
| 2 | Kabir | NULL |
| 3 | Kabir | 5 |

```sql
SELECT AVG(stars) FROM trainer_ratings;
```

Compute the average from the submitted ratings only.

A. 4.5  
B. 3.0  
C. NULL  
D. An error, because AVG cannot process a NULL

### 10. Assign each rule to the right clause

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Filtering Groups  
**Is Curriculum Based:** No  
**Assessment type:** Clause-role mapping

A telecom report on tower outages has two requirements: consider only outages from 2025, and show only towers whose summed downtime exceeds 60 minutes.

Assign each business rule to the stage where its value exists.

A. `HAVING` for the year, `WHERE` for the summed downtime  
B. Both conditions in `WHERE`  
C. Both conditions in `HAVING`  
D. `WHERE` for the year, `HAVING` for the summed downtime

### 11. Vehicles versus visits

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** DISTINCT-aggregate tracing

A car service centre logs every job against the vehicle's registration.

`jobs`

| job_id | vehicle_no | cost |
|---|---|---|
| 1 | KA-01-F 2211 | 1200 |
| 2 | KA-05-M 8890 | 800 |
| 3 | KA-01-F 2211 | 500 |
| 4 | KA-09-B 4433 | 2000 |
| 5 | KA-05-M 8890 | 900 |

```sql
SELECT COUNT(vehicle_no) AS a, COUNT(DISTINCT vehicle_no) AS b
FROM jobs;
```

Calculate the ordinary and distinct vehicle counts.

A. `a = 5`, `b = 5`  
B. `a = 3`, `b = 3`  
C. `a = 5`, `b = 3`  
D. `a = 3`, `b = 5`

### 12. Predict the size of a grouped result

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Grouping Data  
**Is Curriculum Based:** No  
**Assessment type:** Group-formation reasoning

A music-streaming service tags each play with a genre.

`plays`

| play_id | genre |
|---|---|
| 1 | Jazz |
| 2 | Rock |
| 3 | Jazz |
| 4 | Folk |
| 5 | Rock |
| 6 | Jazz |

```sql
SELECT genre, COUNT(*) FROM plays GROUP BY genre;
```

Predict the grouped result's row count.

A. 6, one per play  
B. 3, one per distinct genre  
C. 1, a single overall count  
D. 2, because only genres appearing more than once form groups

### 13. Surface the double-bookers

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Filtering Groups  
**Is Curriculum Based:** No  
**Assessment type:** Query selection for a duplicate report

A boutique hotel suspects some guests hold multiple simultaneous reservations in `bookings(booking_id, guest_email, room)`. The front desk wants each email address that appears on more than one booking.

Select the query that isolates only repeated email groups.

A. `SELECT guest_email FROM bookings GROUP BY guest_email HAVING COUNT(*) > 1;`  
B. `SELECT guest_email FROM bookings WHERE COUNT(*) > 1 GROUP BY guest_email;`  
C. `SELECT guest_email FROM bookings GROUP BY guest_email HAVING COUNT(*) >= 1;`  
D. `SELECT DISTINCT guest_email FROM bookings;`

### 14. Follow the whole pipeline to its one surviving row

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Combining Aggregation with Sorting, Filtering, and Joins  
**Is Curriculum Based:** No  
**Assessment type:** Full-pipeline final-state prediction

A courier firm assigns riders to zones.

`couriers`

| courier_id | zone |
|---|---|
| 1 | East |
| 2 | East |
| 3 | West |

`parcels`

| parcel_id | courier_id | weight_kg |
|---|---|---|
| 11 | 1 | 3 |
| 12 | 1 | 9 |
| 13 | 2 | 12 |
| 14 | 3 | 20 |
| 15 | 3 | 4 |

```sql
SELECT c.zone, SUM(p.weight_kg) AS zone_load
FROM parcels p
JOIN couriers c ON p.courier_id = c.courier_id
WHERE p.weight_kg >= 5
GROUP BY c.zone
HAVING COUNT(*) >= 2
ORDER BY zone_load DESC;
```

Follow the entire pipeline to its surviving output.

A. Two rows: East 24 and West 24  
B. One row: West 20  
C. Two rows: East 21 and West 20  
D. One row: East 21

### 15. Zero is not nothing

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** Zero-versus-NULL computation

Four weather stations report daily rainfall; one recorded a genuine zero.

`rainfall`

| station | rain_mm |
|---|---|
| Ridge | 12 |
| Valley | 8 |
| Coast | 0 |
| Plains | 4 |

```sql
SELECT SUM(rain_mm) AS total, AVG(rain_mm) AS average FROM rainfall;
```

Calculate the total and average without treating zero as missing.

A. `total = 24`, `average = 8`  
B. `total = 24`, `average = 24`  
C. `total = 24`, `average = 6`  
D. `total = 6`, `average = 24`

### 16. Smallest repair for a rejected leaderboard

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Grouping Data  
**Is Curriculum Based:** No  
**Assessment type:** Smallest-correct-repair selection

An e-sports league runs this against `results(match_id, team, player, score)` and gets an error about `player`:

```sql
SELECT team, player, SUM(score)
FROM results
GROUP BY team;
```

The report only needs one total per team. What is the smallest repair?

A. Remove `GROUP BY team` entirely so all columns become ordinary again here  
B. Remove `player` from the SELECT list, since teams hold many players  
C. Move `player` into `ORDER BY` instead of `SELECT`  
D. Wrap `team` in `SUM` so every column is aggregated

### 17. Put the pipeline in running order

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Combining Aggregation with Sorting, Filtering, and Joins  
**Is Curriculum Based:** No  
**Assessment type:** Execution-sequence selection

A query on a joined pair of tables uses `WHERE`, `GROUP BY`, `HAVING`, and `ORDER BY` together.

Arrange the stages in logical execution order.

A. `SELECT` → `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `ORDER BY`  
B. `FROM` → `GROUP BY` → `WHERE` → `HAVING` → `SELECT` → `ORDER BY`  
C. `FROM` → `WHERE` → `HAVING` → `GROUP BY` → `SELECT` → `ORDER BY`  
D. `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`

### 18. Design the dataset that exposes the difference

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** Defect-exposing data selection

A job portal team believes `COUNT(*)` and `COUNT(resume_url)` on their `applications` table are interchangeable and wants a test dataset that proves whether they are.

Choose the smallest kind of dataset that exposes the team's assumption.

A. One where some rows have `resume_url` set to NULL  
B. One where several rows share the same `resume_url` value  
C. One where some `resume_url` values are empty strings  
D. One with many more rows than the production table

### 19. Keep the level that lands exactly on the line

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Filtering Groups  
**Is Curriculum Based:** No  
**Assessment type:** Boundary-condition selection

A parking operator flags garage levels handling 50 or more sessions a day, grouped from `sessions(session_id, level_no)`. Level 3 recorded exactly 50 sessions and must be flagged.

Complete the boundary condition without excluding level 3.

A. `HAVING COUNT(*) > 50`  
B. `HAVING COUNT(*) = 51`  
C. `HAVING COUNT(*) >= 50`  
D. `HAVING COUNT(*) BETWEEN 51 AND 100`

### 20. Only the paid invoices count

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Combining Aggregation with Sorting, Filtering, and Joins  
**Is Curriculum Based:** No  
**Assessment type:** WHERE-plus-HAVING tracing

A wholesale bakery reviews its client accounts.

`invoices`

| invoice_id | client | amount | paid |
|---|---|---|---|
| 1 | Crumb Cafe | 900 | true |
| 2 | Crumb Cafe | 400 | false |
| 3 | Oven Door | 700 | true |
| 4 | Oven Door | 800 | true |
| 5 | Slice Bar | 300 | true |

```sql
SELECT client, SUM(amount) AS paid_total
FROM invoices
WHERE paid
GROUP BY client
HAVING SUM(amount) > 1000;
```

Trace paid rows into their client groups and apply the total threshold.

A. Oven Door 1500 and Crumb Cafe 1300  
B. Oven Door 1500 only  
C. No rows at all  
D. Oven Door 1500 and Slice Bar 300

### 21. MIN meets a text column

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** Type-behaviour prediction

A radio network stores its advertisers in `sponsors(sponsor_id, sponsor_name)` where `sponsor_name` is TEXT. A producer runs `SELECT MIN(sponsor_name) FROM sponsors;`.

Choose the result description that does not assume a particular locale.

A. An error, because text has no minimum  
B. The shortest sponsor name  
C. The first sponsor inserted, regardless of how its text value sorts  
D. The text value first under the database's ordering

### 22. Pick the report that answers a two-way question

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Grouping Data  
**Is Curriculum Based:** No  
**Assessment type:** Grouping-granularity selection

A property manager bills electricity from `meter_readings(reading_id, building, billing_month, units)` and must see consumption for every building in every month separately.

Select the grouping granularity matching one building-month result row.

A. `GROUP BY building`, one total per building across all months  
B. `GROUP BY billing_month`, one total per month across all buildings here  
C. `GROUP BY building, billing_month`, one total per building-month pair  
D. No grouping, a single grand total for the whole portfolio

### 23. One of these two queries cannot run

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Filtering Groups  
**Is Curriculum Based:** No  
**Assessment type:** Equivalence-and-validity judgment

A cinema chain wants adult-ticket counts per screen from `sales(sale_id, screen, ticket_type)`. Two drafts exist:

```sql
-- Draft 1
SELECT screen, COUNT(*) FROM sales
WHERE ticket_type = 'Adult'
GROUP BY screen;

-- Draft 2
SELECT screen, COUNT(*) FROM sales
GROUP BY screen
HAVING ticket_type = 'Adult';
```

Decide whether the drafts are equivalent and executable.

A. Draft 2 fails since `ticket_type` is neither grouped nor aggregated.  
B. The drafts are interchangeable because both mention the same condition  
C. Draft 2 is preferable because group filters run before row filters  
D. Draft 1 fails because `WHERE` is not allowed before `GROUP BY`

### 24. Recover the average without rerunning anything

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** Aggregate-relationship reasoning

A fishing cooperative's daily report shows `SUM(catch_kg) = 60` and `COUNT(*) = 4` over the day's landings, with no NULL weights.

Recover `AVG(catch_kg)` from the two supplied aggregates.

A. 60  
B. 15  
C. 4  
D. It cannot be determined from the sum and count

### 25. The group that vanished

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Grouping Data  
**Is Curriculum Based:** No  
**Assessment type:** Filtered-grouping prediction

A news site tracks article status.

`articles`

| article_id | section | published |
|---|---|---|
| 1 | Politics | true |
| 2 | Politics | false |
| 3 | Culture | false |
| 4 | Sports | true |
| 5 | Sports | true |

```sql
SELECT section, COUNT(*) AS live_articles
FROM articles
WHERE published
GROUP BY section;
```

Determine whether Culture forms a result group after the row filter.

A. Three rows, with Culture showing 0  
B. Three rows, with Culture showing NULL  
C. Five rows, one per article  
D. Two rows; Culture doesn't appear

### 26. Two drivers, or one busy one?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Filtering Groups  
**Is Curriculum Based:** No  
**Assessment type:** DISTINCT-in-HAVING selection

A ride-hailing operator wants zones covered by at least two different drivers.

`trips`

| trip_id | zone | driver_id |
|---|---|---|
| 1 | Downtown | D1 |
| 2 | Downtown | D1 |
| 3 | Downtown | D1 |
| 4 | Uptown | D2 |
| 5 | Uptown | D3 |

Downtown must be excluded — its three trips all belong to one driver. Which query is correct?

A. `SELECT zone FROM trips GROUP BY zone HAVING COUNT(*) >= 2;`  
B. `SELECT zone FROM trips WHERE COUNT(DISTINCT driver_id) >= 2 GROUP BY zone ORDER BY zone;`  
C. `SELECT zone FROM trips GROUP BY zone HAVING COUNT(DISTINCT driver_id) >= 2;`  
D. `SELECT zone FROM trips GROUP BY zone HAVING driver_id >= 2;`

### 27. Build the revenue leaderboard

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Combining Aggregation with Sorting, Filtering, and Joins  
**Is Curriculum Based:** No  
**Assessment type:** Query completion for ranked output

A craft-supplies store wants product lines ranked by revenue, highest first, from `sales(sale_id, product_line, amount)`.

Complete the revenue leaderboard.

A. `SELECT product_line, SUM(amount) AS revenue FROM sales GROUP BY product_line ORDER BY amount DESC;`  
B. `SELECT product_line, SUM(amount) AS revenue FROM sales GROUP BY product_line ORDER BY revenue DESC;`  
C. `SELECT product_line, SUM(amount) AS revenue FROM sales GROUP BY product_line ORDER BY product_line DESC;`  
D. `SELECT product_line, SUM(amount) AS revenue FROM sales GROUP BY revenue;`

### 28. Where did the other 55 rows go?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Grouping Data  
**Is Curriculum Based:** No  
**Assessment type:** Misconception correction

A laundry pickup service has 60 rows in `pickups`, but grouping by neighbourhood returns only 5 rows. A trainee worries that 55 pickups have been lost.

Explain the smaller result without implying any stored data changed.

A. One row summarizes each neighbourhood; stored pickups remain unchanged  
B. The 55 rows were moved to a temporary table and will return after `COMMIT`  
C. Grouping removes the 55 repeated neighbourhood rows from the stored table  
D. The result is wrong, and the query must be rerun with `SELECT *`

### 29. Four customers who are really two

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Combining Aggregation with Sorting, Filtering, and Joins  
**Is Curriculum Based:** No  
**Assessment type:** Root-cause diagnosis in a joined aggregate

A pet-grooming franchise counts customers per city by joining appointments to branches.

`appointments` (already joined to its branch's city)

| appt_id | city | customer_name |
|---|---|---|
| 1 | Pune | Meera Joshi |
| 2 | Pune | Meera Joshi |
| 3 | Pune | Meera Joshi |
| 4 | Pune | Dev Patil |

The report used `COUNT(customer_name)` and claims Pune has 4 customers, but only Meera and Dev exist.

Diagnose the inflated customer count.

A. The join dropped two customers, so the count is coincidentally high  
B. `COUNT` always counts distinct values, so the data itself must contain 4 names  
C. NULL customer names inflated the count by two  
D. `COUNT(customer_name)` counted every appointment row; DISTINCT was needed

### 30. Averages against a cutoff

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Filtering Groups  
**Is Curriculum Based:** No  
**Assessment type:** HAVING-with-AVG tracing

A co-working operator studies room usage.

`room_bookings`

| booking_id | room | hours |
|---|---|---|
| 1 | Hive | 2 |
| 2 | Hive | 4 |
| 3 | Loft | 6 |
| 4 | Loft | 10 |
| 5 | Dock | 5 |

```sql
SELECT room, AVG(hours) AS avg_hours
FROM room_bookings
GROUP BY room
HAVING AVG(hours) >= 5;
```

Compute each room's average and apply the inclusive cutoff.

A. Loft only  
B. Dock only  
C. Loft and Dock  
D. Hive, Loft, and Dock

### 31. A sum with a hole in the data

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** NULL-in-SUM prediction

A smart-home hub logs appliance energy use; one reading failed to upload.

`energy_log`

| log_id | appliance | kwh |
|---|---|---|
| 1 | Heater | 5 |
| 2 | Oven | NULL |
| 3 | Dryer | 7 |
| 4 | Fridge | 3 |

```sql
SELECT SUM(kwh) FROM energy_log;
```

Calculate the aggregate despite the failed reading.

A. NULL, because any NULL in the column poisons the total  
B. 15  
C. An error, because SUM cannot run over a column containing NULL  
D. 0, because SUM refuses columns with missing readings

### 32. Six rows where three were expected

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Grouping Data  
**Is Curriculum Based:** No  
**Assessment type:** Over-grouping diagnosis

A florist wholesaler wanted revenue for each of its 3 flower types, but this query returned 6 rows:

```sql
SELECT flower_type, SUM(amount)
FROM orders
GROUP BY flower_type, buyer_name;
```

Identify the extra grouping dimension that changed the granularity.

A. Grouping by `buyer_name` too divided each flower type per buyer  
B. `SUM` produces two rows per group, one gross and one net  
C. The table stores each order twice for audit reasons  
D. Sorting the grouped columns duplicates each group in the result

### 33. Same answer, different amount of work

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Combining Aggregation with Sorting, Filtering, and Joins  
**Is Curriculum Based:** No  
**Assessment type:** Equivalence-with-efficiency judgment

A warehouse audits damaged stock. Version 1 filters `WHERE status = 'damaged'` before grouping by aisle. Version 2 groups all rows by aisle and status, then keeps only damaged groups afterward. Both end up reporting the same damaged-stock totals per aisle.

Compare the two implementations for result equivalence and avoidable work.

A. Version 2 is better because `HAVING` conditions are checked earlier than `WHERE`  
B. The versions must return different totals, so one of them is wrong  
C. Version 1 is incorrect because `WHERE` cannot run in a query that groups  
D. The results match, but Version 1 avoids grouping rows only to be thrown away

### 34. The alias HAVING refuses to see

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Filtering Groups  
**Is Curriculum Based:** No  
**Assessment type:** Error repair via execution order

A subscription-box service writes:

```sql
SELECT subscriber_id, SUM(amount) AS total_spent
FROM renewals
GROUP BY subscriber_id
HAVING total_spent > 1000;
```

PostgreSQL rejects `total_spent` in the HAVING clause. Which repair works, and why?

A. Rename the alias to lowercase so HAVING can resolve it  
B. Replace the alias with `SUM(amount)` in HAVING directly  
C. Move the condition into `WHERE total_spent > 1000`, which runs after SELECT  
D. Add `ORDER BY total_spent` so the alias is registered before HAVING runs

### 35. One number: the single biggest bid

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** Function-to-requirement mapping

An auction house needs exactly one number from `bids(bid_id, lot_no, bid_amount)`: the largest single bid placed all evening, across all lots.

Map the one-number requirement to its aggregate.

A. `SELECT SUM(bid_amount) FROM bids;`  
B. `SELECT COUNT(bid_amount) FROM bids;`  
C. `SELECT MAX(bid_amount) FROM bids;`  
D. `SELECT AVG(bid_amount) FROM bids;`

### 36. Read one cell of a two-way summary

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Grouping Data  
**Is Curriculum Based:** No  
**Assessment type:** Multi-column group computation

A ferry operator counts passengers per route and time of day.

`crossings`

| crossing_id | route | day_part | passengers |
|---|---|---|---|
| 1 | Harbor | AM | 120 |
| 2 | Harbor | PM | 80 |
| 3 | Harbor | AM | 60 |
| 4 | Island | PM | 90 |

```sql
SELECT route, day_part, SUM(passengers) AS total
FROM crossings
GROUP BY route, day_part;
```

Calculate the Harbor–AM cell of the two-way summary.

A. 180  
B. 260.  
C. 120.  
D. 90

### 37. The cheapest item sets the bar

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Filtering Groups  
**Is Curriculum Based:** No  
**Assessment type:** Aggregate-choice completion

An electronics assembler vets suppliers using `catalog(item_id, supplier, unit_price)`. Procurement wants suppliers whose **cheapest** listed item still costs more than 100.

Complete `SELECT supplier FROM catalog GROUP BY supplier ...` using the relevant group extreme.

A. `HAVING MAX(unit_price) > 100`  
B. `HAVING MIN(unit_price) > 100`  
C. `WHERE unit_price > 100`, placed before GROUP BY  
D. `HAVING AVG(unit_price) > 100`

### 38. Translate the whole request into one query

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Combining Aggregation with Sorting, Filtering, and Joins  
**Is Curriculum Based:** No  
**Assessment type:** Specification-to-query selection

An artisan marketplace asks: "revenue per city for March orders only, restricted to cities with at least two distinct buyers, highest revenue first." Tables: `orders(order_id, buyer_id, city, amount, order_date)`.

Translate every stage of the request into one query.

A. `SELECT city, SUM(amount) AS revenue FROM orders GROUP BY city HAVING order_date >= '2025-03-01' AND COUNT(buyer_id) >= 2 ORDER BY revenue DESC;`  
B. `SELECT city, SUM(amount) AS revenue FROM orders WHERE order_date BETWEEN '2025-03-01' AND '2025-03-31' GROUP BY city HAVING COUNT(buyer_id) >= 2 ORDER BY revenue DESC;`  
C. `SELECT city, SUM(amount) AS revenue FROM orders WHERE order_date BETWEEN '2025-03-01' AND '2025-03-31' AND COUNT(DISTINCT buyer_id) >= 2 GROUP BY city HAVING SUM(amount) > 0 ORDER BY revenue DESC;`  
D. `SELECT city, SUM(amount) AS revenue FROM orders WHERE order_date BETWEEN '2025-03-01' AND '2025-03-31' GROUP BY city HAVING COUNT(DISTINCT buyer_id) >= 2 ORDER BY revenue DESC;`

### 39. Count only what the filter and the column allow

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Aggregate Functions  
**Is Curriculum Based:** No  
**Assessment type:** Combined WHERE-and-NULL counting

A bike-share scheme logs rides; ride 3's tracker died mid-trip, so its duration is missing.

`rides`

| ride_id | distance_km | duration_min |
|---|---|---|
| 1 | 4 | 20 |
| 2 | 12 | 35 |
| 3 | 18 | NULL |
| 4 | 9 | 15 |
| 5 | 11 | 40 |

```sql
SELECT COUNT(duration_min)
FROM rides
WHERE distance_km > 10;
```

Apply the distance filter first, then count available durations.

A. 3  
B. 5  
C. 2  
D. 4

### 40. Rank the roster from the raw plays

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Combining Aggregation with Sorting, Filtering, and Joins  
**Is Curriculum Based:** No  
**Assessment type:** Group-then-sort output ordering

A music label sums streaming plays per artist.

`streams`

| stream_id | artist | plays |
|---|---|---|
| 1 | Vela | 300 |
| 2 | Vela | 200 |
| 3 | Moss | 450 |
| 4 | Kite | 100 |
| 5 | Kite | 120 |

```sql
SELECT artist, SUM(plays) AS total_plays
FROM streams
GROUP BY artist
ORDER BY total_plays DESC;
```

Rank the three aggregate totals in the order returned.

A. Vela 500, Moss 450, Kite 220  
B. Moss (450), Vela (500), Kite (220)  
C. Kite (220), Moss (450), Vela (500)  
D. Vela (300), Moss (450), Kite (120)

---

## Instructor Key

### 1. B

`COUNT(*)` counts all 5 rows regardless of content. `COUNT(kwh_delivered)` skips the two NULL readings from the interrupted sessions, counting only rows 1, 3, and 5. The temptation in option A is assuming the two forms are synonyms; they diverge exactly when a column is optional.

### 2. D

`shipment_id` appears in the SELECT list but is neither listed in `GROUP BY` nor wrapped in an aggregate. Once rows collapse into route groups, a group contains many shipment IDs, so the database has no single value to display and rejects the query. The other three drafts pair the grouped column with a legal aggregate.

### 3. A

`WHERE downloads >= 400` keeps rows 1, 2, and 3 before grouping. Night Signal then sums to 1300 and Deep Field to 1500; both clear the `HAVING` bar of 1000, and Waypoint's only episode never survived the row filter. Option B is the trap of forgetting that `WHERE` removed Deep Field's 200-download episode before the sum ran.

### 4. C

The pipeline runs `WHERE` at step 2, before `GROUP BY` forms groups and before `SELECT` computes `SUM(fare)` and names it — so the alias and the aggregate simply do not exist yet. `ORDER BY` runs last, after `SELECT`, so the alias is available. One execution order explains both symptoms.

### 5. C

`MIN` and `MAX` work on dates, returning the earliest and latest values in the column: 2025-01-30 and 2025-06-02. Insertion order (option B) is irrelevant to aggregates; they scan values, not row positions.

### 6. A

"Three or more" is a group-level condition on a count that exists only after grouping, so it belongs in `HAVING COUNT(*) >= 3`. Option C's strict `>` silently drops members with exactly three visits, and option B places an aggregate in `WHERE`, which runs before any count exists.

### 7. D

Grouping by two columns creates one group per distinct combination that actually occurs: Aria–BLR, Aria–DEL, Nimbus–BLR, Nimbus–DEL. Option C describes a cross product of all possible pairings; `GROUP BY` only ever forms groups from combinations present in the data.

### 8. B

The join tags each delivery with its store's city, then grouping sums by city: Pune receives deliveries 10, 11, and 13 (40 + 25 + 35 = 100) because two different stores share the city, and Nagpur receives delivery 12 (60). Option A misses that store 1 delivered twice.

### 9. A

`AVG` ignores NULLs entirely: (4 + 5) ÷ 2 = 4.5. Option B is the classic error of treating the missing rating as a zero, which would wrongly drag the average down to 3.0.

### 10. D

The year restriction tests individual outage rows, so it belongs in `WHERE`, which runs before grouping. The downtime total exists only after grouping sums it, so its filter belongs in `HAVING`. Splitting the work this way is exactly the division of labour the two clauses are designed for.

### 11. C

`COUNT(vehicle_no)` counts every non-NULL value — all 5 rows here. `COUNT(DISTINCT vehicle_no)` collapses repeats, and only 3 different registrations appear. The gap between the two numbers is precisely the repeat-customer effect.

### 12. B

`GROUP BY genre` forms one group per distinct value: Jazz, Rock, and Folk. Option D reflects a misreading that only duplicated values are "grouped"; a value appearing once still forms its own group of one row.

### 13. A

Appearing "on more than one booking" is a per-group count, so the pattern is group by the email, then `HAVING COUNT(*) > 1`. Option B puts the aggregate where no groups exist yet, option C's `>= 1` keeps every guest, and option D lists each guest once without testing frequency at all.

### 14. D

`WHERE weight_kg >= 5` keeps parcels 12, 13, and 14. The join maps 12 and 13 to East (9 + 12 = 21, two parcels) and 14 to West (20, one parcel). `HAVING COUNT(*) >= 2` eliminates West, leaving only East 21. Option C forgets the group-count filter; option A ignores the row filter.

### 15. C

Coast's 0 is a real recorded value, so it participates: SUM = 12 + 8 + 0 + 4 = 24 and AVG = 24 ÷ 4 = 6. Option A comes from mentally discarding the zero as if it were NULL — but aggregates skip NULLs, not zeros.

### 16. B

The report needs one row per team, so the fix is removing the column that does not belong at that granularity: `player`. Removing `GROUP BY` (option A) destroys the per-team totals, and aggregating `team` (option D) destroys the breakdown the report exists to show.

### 17. D

The database combines tables (`FROM`/`JOIN`), filters rows (`WHERE`), forms groups (`GROUP BY`), filters groups (`HAVING`), computes the output columns (`SELECT`), and sorts last (`ORDER BY`). This single sequence is why `WHERE` cannot use aggregates and why `ORDER BY` can use aliases.

### 18. A

The two counts differ only in their treatment of NULL: `COUNT(*)` counts rows, `COUNT(resume_url)` counts non-NULL values. Duplicates (B) and empty strings (C) are non-NULL and count normally in both; extra volume (D) scales both numbers equally.

### 19. C

"50 or more" includes the boundary, so `>= 50` is required; Level 3's exactly-50 day proves the point. Option A's strict inequality excludes precisely the case the requirement names.

### 20. B

`WHERE paid` first removes invoice 2, so Crumb Cafe's group totals only 900 and fails the 1000 bar. Oven Door totals 1500 and passes; Slice Bar's 300 does not. Option A is the result of running `HAVING` against unfiltered totals — forgetting that `WHERE` already trimmed Crumb Cafe's sum.

### 21. D

`MIN` and `MAX` accept text and use the database's configured text ordering, so `MIN` returns the value that sorts first under that ordering. String length and insertion history do not determine it.

### 22. C

Consumption "for every building in every month separately" is a two-dimensional breakdown, which needs one group per building–month combination. Grouping by either column alone blends the other dimension into one number.

### 23. A

In Draft 2, `ticket_type` is neither in `GROUP BY` nor aggregated, so after grouping a screen's group holds many ticket types and `HAVING` has no single value to test — the query fails. Row-level conditions belong in `WHERE`, which is exactly what Draft 1 does.

### 24. B

With no NULLs, `AVG` is defined as the sum divided by the count: 60 ÷ 4 = 15. The relationship between the three aggregates is fixed, which is why the average is fully determined here.

### 25. D

`WHERE published` removes rows 2 and 3 before grouping, and Culture has no published articles left to form a group from. A group that loses all its rows to `WHERE` doesn't appear as zero — it never comes into existence. Option A is the intuitive but wrong expectation of a 0-count row.

### 26. C

The requirement counts *different drivers*, not trips, so the group filter must be `COUNT(DISTINCT driver_id) >= 2`. Option A's plain `COUNT(*)` wrongly admits Downtown on the strength of one driver's three trips — the exact confusion the data is built to expose.

### 27. B

The leaderboard needs grouping by product line, an alias for the summed revenue, and `ORDER BY revenue DESC` — legal because sorting runs after `SELECT` defines the alias. Option A orders by the raw ungrouped column `amount`, which no longer exists per-group; option D tries to group by a result that grouping itself produces.

### 28. A

A grouped result has one row per group by design; all 60 pickups are still in the table and every one of them contributed to some neighbourhood's summary row. Aggregation reads and condenses — it never modifies or discards stored rows.

### 29. D

`COUNT(customer_name)` counts one per row, and Meera's three appointments each contributed. Counting *people* rather than *visits* requires `COUNT(DISTINCT customer_name)`, which returns 2. This distinction is easy to miss precisely because the query runs without error and returns a plausible-looking number.

### 30. C

Averages per room: Hive (2+4)/2 = 3, Loft (6+10)/2 = 8, Dock 5/1 = 5. The `>= 5` bar keeps Loft and Dock — Dock sits exactly on the boundary and the inclusive comparison admits it. Option A comes from misreading `>=` as `>`.

### 31. B

`SUM` skips NULLs rather than propagating them, so the total is 5 + 7 + 3 = 15. Option A confuses aggregate behaviour with expression arithmetic, where `5 + NULL` would indeed be NULL — aggregates are the exception to that intuition.

### 32. A

Every extra column in `GROUP BY` refines the grouping: `flower_type, buyer_name` makes one group per flower-per-buyer, splitting each flower type across its buyers. The repair is to group by `flower_type` alone, matching the granularity the report actually wants.

### 33. D

Both queries isolate damaged stock, but Version 1 discards non-damaged rows at step 2, before any grouping effort is spent on them, while Version 2 builds groups it immediately throws away. Filtering rows early with `WHERE` is the cheaper shape when the condition is row-level.

### 34. B

`HAVING` executes at step 4, before `SELECT` computes expressions and binds aliases at step 5, so `total_spent` does not exist when `HAVING` needs it — repeating `SUM(amount)` is the standard fix. `ORDER BY` alone can use the alias, because sorting happens after `SELECT`.

### 35. C

"The largest single value in a column" is the definition of `MAX`. `SUM` blends all bids together, `COUNT` measures how many there were, and `AVG` describes a typical bid — none can recover the top one.

### 36. A

The Harbor–AM group contains crossings 1 and 3, so its total is 120 + 60 = 180. Option B (260) merges Harbor's AM and PM figures, which is what a one-column `GROUP BY route` would have produced instead.

### 37. B

"The cheapest item still costs more than 100" is a condition on each supplier's minimum, so `HAVING MIN(unit_price) > 100`. Option C is subtly wrong: filtering rows with `WHERE unit_price > 100` deletes the cheap items from view, letting a supplier with a 40-rupee part still qualify on its surviving expensive parts.

### 38. D

The date restriction is row-level (`WHERE`), the buyer threshold needs a per-city count of distinct buyers after grouping (`HAVING COUNT(DISTINCT buyer_id) >= 2`), and the ranking is `ORDER BY revenue DESC`. Option B counts buyer rows rather than distinct buyers, so one repeat customer could satisfy it; options A and C put conditions in stages that cannot evaluate them.

### 39. C

`WHERE distance_km > 10` keeps rides 2, 3, and 5. `COUNT(duration_min)` then counts non-NULL durations among those survivors — ride 3's missing duration drops out, leaving 2. Option A is the answer to `COUNT(*)`, not `COUNT(duration_min)`.

### 40. A

Totals are Vela 500, Moss 450, Kite 220; `ORDER BY total_plays DESC` lists them from highest to lowest. Option D ranks by each artist's single largest row instead of the group total.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Output and pipeline tracing over shown data | 1, 3, 5, 8, 9, 11, 14, 15, 20, 25, 30, 31, 36, 39, 40 |
| Invalid-query identification and error repair | 2, 16, 23, 34 |
| Missing-clause and query completion | 6, 19, 27, 37, 38 |
| Group-count and granularity prediction | 7, 12, 22, 36 |
| Root-cause diagnosis and misconception correction | 28, 29, 32 |
| Equivalence and efficiency judgment | 23, 33 |
| Defect-exposing data design | 18, 26 |
| Concept-to-clause and function mapping | 4, 10, 17, 21, 24, 35 |

## Blueprint Taxonomy Coverage

| Subtopic | Question numbers | Count |
|---|---|---:|
| Aggregate Functions | 1, 5, 9, 11, 15, 18, 21, 24, 31, 35, 39 | 11 |
| Grouping Data | 2, 7, 12, 16, 22, 25, 28, 32, 36 | 9 |
| Filtering Groups | 3, 6, 10, 13, 19, 23, 26, 30, 34, 37 | 10 |
| Combining Aggregation with Sorting, Filtering, and Joins | 4, 8, 14, 17, 20, 27, 29, 33, 38, 40 | 10 |

Questions 1–10 collectively cover all four Topic 4.2 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (1, 5, 10, 12, 15, 17, 21, 24, 28, 35)
- Intermediate: 27 questions
- Advanced: 3 questions (14, 33, 38)
- Correct option A: 10 questions (3, 6, 9, 13, 18, 23, 28, 32, 36, 40)
- Correct option B: 10 questions (1, 8, 12, 16, 20, 24, 27, 31, 34, 37)
- Correct option C: 10 questions (4, 5, 11, 15, 19, 22, 26, 30, 35, 39)
- Correct option D: 10 questions (2, 7, 10, 14, 17, 21, 25, 29, 33, 38)
- Longest consecutive run of one correct letter: 2 (questions 4–5)
