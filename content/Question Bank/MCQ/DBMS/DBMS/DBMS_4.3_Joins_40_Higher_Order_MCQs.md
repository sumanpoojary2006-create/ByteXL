# DBMS 4.3: Joins — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** SQL for Data Retrieval and Analytics
- **Chapter:** Joins
- **Scope:** All seven Topic 4.3 subtopics in the attached course blueprint (Why Joins Exist; INNER JOIN; LEFT JOIN; RIGHT JOIN and FULL OUTER JOIN; Self Joins; Multi-Table Joins; Semi Joins and Anti Joins)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every item begins with a recognisable relationship or reporting task. Whenever an answer depends on matches, the participating tables, key meanings, and relevant rows are visible.
- **Evidence rule:** Students must trace pairings, complete or repair an ON condition, compare equivalent join forms, expose unmatched rows, or choose an existence pattern—not recall an isolated join definition.
- **Scope guard:** Only the seven join patterns explicitly taught in Topic 4.3 are assessed; aggregation appears only where the chapter itself combines it with joins.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all seven Topic 4.3 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. The rental slip that stores only a number

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Why Joins Exist  
**Is Curriculum Based:** No  
**Assessment type:** Design-rationale reasoning

A bike-share system's `rentals` table stores only `member_id = 7` on each rental row, never the member's name or phone. The monthly report, however, must show names.

`members`

| member_id | member_name | phone |
|---:|---|---|
| 7 | Leena | 9800-1122 |
| 9 | Omar | 9800-3344 |

`rentals`

| rental_id | member_id | bicycle_id |
|---:|---:|---:|
| 301 | 7 | 18 |
| 302 | 7 | 22 |

Choose the explanation that accounts for both the storage design and the report's ability to display `Leena` beside rentals 301 and 302.

A. Names were omitted accidentally and must be collected again for each report.  
B. Member facts live once in `members`; one update, recombined via join.  
C. Reports are forbidden from showing names stored in another table.  
D. Each report writer retypes the names by hand.

### 2. Only the matched callouts

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INNER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Match-only tracing

A city fire department tracks callouts received by each of its stations.

`fire_stations`

| station_id | station_name |
|---|---|
| 1 | Riverside |
| 2 | Old Town |
| 3 | Docklands |
| 4 | Hilltop |

`callouts`

| callout_id | station_id | severity |
|---|---|---|
| 11 | 1 | high |
| 12 | 1 | low |
| 13 | 3 | high |
| 14 | 2 | medium |

```sql
SELECT s.station_name, c.severity
FROM callouts c
INNER JOIN fire_stations s ON c.station_id = s.station_id;
```

Determine the result count and identify the station excluded by match-only behaviour.

A. 8 rows — every station against every callout.  
B. 5 rows — four matched callouts plus Hilltop padded with a NULL severity value.  
C. 3 rows — one per station with callouts.  
D. 4 rows — one per callout; Hilltop appears nowhere, no match found.

### 3. The member who never borrowed

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** LEFT JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Left-preservation tracing

A community toolshed tracks which members have borrowed tools.

`toolshed_members`

| member_id | name |
|---|---|
| 1 | Salim |
| 2 | Priya |
| 3 | Joel |

`tool_loans`

| loan_id | member_id | tool |
|---|---|---|
| 1 | 1 | Drill |
| 2 | 1 | Sander |
| 3 | 3 | Jigsaw |

```sql
SELECT m.name, l.tool
FROM toolshed_members m
LEFT JOIN tool_loans l ON m.member_id = l.member_id;
```

Trace the pairings and select the exact result shape.

A. 4 rows: Salim×2, Joel×1, Priya×1 with NULL tool.  
B. 3 rows — Priya is dropped.  
C. 2 rows — one for each member who has a recorded tool loan, with repeats merged.  
D. 6 rows — every member paired with every loan.

### 4. Neither side left behind

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** RIGHT JOIN and FULL OUTER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Join-type identification

An office audit compares `employees` with `parking_permits`. Some employees have no permit; some permits belong to contractors not in the employees table. The audit must show *both* kinds of mismatch, with NULLs marking the gaps.

Select the join that preserves both mismatch directions in one result.

A. INNER JOIN — unmatched employees and permits appear as padded rows.  
B. LEFT JOIN — it protects both tables.  
C. FULL OUTER JOIN, keeping every row from both sides, padded.  
D. No join can show both directions at once.

### 5. One table, wearing two name tags

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Self Joins  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism identification

A courier firm's `staff` table has `staff_id`, `name`, and `supervisor_id` — where `supervisor_id` holds the `staff_id` of another row in the *same table*. A report must show each person beside their supervisor's name.

`staff`

| staff_id | name | supervisor_id |
|---:|---|---:|
| 1 | Nila | NULL |
| 2 | Harsh | 1 |
| 3 | Iqbal | 1 |

Select the construction that lets the report treat one `staff` row as the employee and another row as the supervisor.

A. Two databases are needed, one per role.  
B. `SELECT supervisor_id FROM staff` — the referenced name is inferred from that number without a second table role.  
C. A join to a copied backup of the table.  
D. The table joins to itself under two aliases, playing two roles at once.

### 6. Three tables, one chain

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Multi-Table Joins  
**Is Curriculum Based:** No  
**Assessment type:** Join-chain construction

A campsite system has `guests(guest_id, name)`, `bookings(booking_id, guest_id, cabin_id)`, and `cabins(cabin_id, cabin_name)`. A report needs guest name beside cabin name for every booking.

Complete the report with the `FROM` clause that follows both foreign-key relationships.

A. `FROM guests g JOIN cabins c ON g.guest_id = c.cabin_id`, directly matching the two independent primary keys  
B. `FROM bookings b JOIN guests g ON b.guest_id = g.guest_id JOIN cabins c ON b.cabin_id = c.cabin_id`  
C. `FROM guests, bookings, cabins` with no conditions.  
D. `FROM cabins JOIN cabins ON guest_id = cabin_id`

### 7. Present in the audience, invisible in the columns

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Semi Joins and Anti Joins  
**Is Curriculum Based:** No  
**Assessment type:** Semi-join selection

A theatre wants each patron who has attended **at least one** show — each listed once, with no show columns in the output.

Choose the query shape that uses attendance only as an existence test.

A. INNER JOIN to attendances, returning one patron row per attendance and then projecting only the patron name.  
B. FULL OUTER JOIN with all columns.  
C. `SELECT name FROM patrons p WHERE EXISTS (SELECT 1 FROM attendances a WHERE a.patron_id = p.patron_id);`
D. A DELETE of patrons without shows.

### 8. Join first, then judge the bill

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INNER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Join-plus-filter tracing

A salon booking platform tracks appointments and their bill amount across salons.

`salons`

| salon_id | salon_name |
|---|---|
| 1 | Glow Studio |
| 2 | Shine Bar |

`appointments`

| appt_id | salon_id | bill |
|---|---|---|
| 1 | 1 | 500 |
| 2 | 1 | 700 |
| 3 | 2 | 300 |

```sql
SELECT s.salon_name, a.bill
FROM appointments a
JOIN salons s ON a.salon_id = s.salon_id
WHERE a.bill > 400;
```

Determine which report rows survive after the join and the bill filter are both applied.

A. Two rows: Glow Studio 500 and 700; Shine Bar's bill dropped.  
B. Three rows because WHERE cannot follow a joined FROM clause.  
C. One row — only the largest bill.  
D. Shine Bar 300 alone.

### 9. Every vendor, even the quiet ones

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** LEFT JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Count-including-zero construction

A crafts fair must report each vendor's sale count — **including vendors with zero sales**, shown as 0.

`vendors`

| vendor_id | vendor_name |
|---:|---|
| 1 | Loom House |
| 2 | Clay Corner |
| 3 | Paper Petal |

`sales`

| sale_id | vendor_id |
|---:|---:|
| 11 | 1 |
| 12 | 1 |
| 13 | 3 |

Select the executable query that reports `2, 0, 1` for the three vendors.

A. `SELECT v.vendor_name, COUNT(*) AS sale_count FROM vendors v JOIN sales s ON s.vendor_id = v.vendor_id GROUP BY v.vendor_id, v.vendor_name;`  
B. `SELECT v.vendor_name, COUNT(s.sale_id) FROM vendors v LEFT JOIN sales s ON s.vendor_id = v.vendor_id GROUP BY v.vendor_id, v.vendor_name;`  
C. `SELECT vendor_name FROM vendors WHERE sale_id > 0;`  
D. `SELECT COUNT(*) FROM sales;`

### 10. The one-line answer

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Why Joins Exist  
**Is Curriculum Based:** No  
**Assessment type:** Purpose identification

A trainee proposes four one-line descriptions before writing a report that combines customer names with their orders. Select the description that would lead to the correct design.

A. Joins compress tables to save disk.  
B. Joins permanently copy the matched columns into both source tables.  
C. Joins delete unmatched data.  
D. A join combines rows from related tables by matching values.

### 11. What the ON clause is for

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INNER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Clause-role identification

In `FROM deliveries d JOIN hubs h ON d.hub_id = h.hub_id`, identify the decision made by the `ON` clause before `SELECT` chooses the displayed columns.

A. Which columns appear in the output.  
B. The sort order of the result.  
C. Which row pairings belong together, matched by shared ID.  
D. The maximum number of rows the result is allowed to contain.

### 12. Surface the silent ones

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** LEFT JOIN  
**Is Curriculum Based:** No  
**Assessment type:** No-match-finding construction

A book club wants members who have **never** RSVP'd to any meetup, using `members(member_id, name)` and `rsvps(rsvp_id, member_id)`.

`members`

| member_id | name |
|---:|---|
| 1 | Uma |
| 2 | Tariq |
| 3 | Mei |

`rsvps`

| rsvp_id | member_id |
|---:|---:|
| 41 | 1 |
| 42 | 3 |

Choose the pattern that returns Tariq and no one else.

A. `SELECT m.name FROM members m LEFT JOIN rsvps r ON r.member_id = m.member_id WHERE r.member_id IS NULL;`  
B. `SELECT m.name FROM members m INNER JOIN rsvps r ON r.member_id = m.member_id WHERE r.member_id IS NOT NULL;`  
C. `SELECT name FROM members WHERE member_id = NULL;`  
D. `SELECT member_id FROM rsvps;`

### 13. The mirror image

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** RIGHT JOIN and FULL OUTER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Preservation-side identification

A fisheries report runs `boats b RIGHT JOIN licences l ON b.boat_id = l.boat_id`.

Identify the table whose rows are protected even when a matching row is absent.

A. `boats` — the left table.  
B. Both tables fully.  
C. Neither table; RIGHT JOIN retains matched pairs and discards every row lacking a partner.  
D. `licences` — RIGHT JOIN preserves every right-table row, padded.

### 14. Who mentors whom

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Self Joins  
**Is Curriculum Based:** No  
**Assessment type:** Self-join tracing

A ride-share collective tracks which experienced rider mentors each new rider.

`riders`

| rider_id | name | mentor_id |
|---|---|---|
| 1 | Asha | NULL |
| 2 | Binod | 1 |
| 3 | Chitra | 1 |
| 4 | Dev | 3 |

```sql
SELECT r.name AS rider, m.name AS mentor
FROM riders r
JOIN riders m ON r.mentor_id = m.rider_id;
```

Trace the alias-to-alias matches and select the complete report.

A. Four rows, including Asha paired with herself because her NULL is treated as rider 1.  
B. Three rows: Binod–Asha, Chitra–Asha, Dev–Chitra, matched.  
C. Two rows — one per mentor.  
D. An error: a table cannot join itself.

### 15. Letters that keep four tables straight

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Multi-Table Joins  
**Is Curriculum Based:** No  
**Assessment type:** Alias-practice rationale

A four-table booking query prefixes every column: `b.booking_id`, `g.name`, `c.cabin_name`, `p.amount`.

Account for the prefixes by selecting their role when several tables contain similarly named columns.

A. Each column is unambiguously tied to its table this way.  
B. They make the query run faster.  
C. They encrypt the table names.  
D. They are optional decorations with no role in resolving column names.

### 16. What lands in the combined row

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Why Joins Exist  
**Is Curriculum Based:** No  
**Assessment type:** Output-shape identification

A query uses `SELECT o.*, c.*` after matching an `orders` row to its `customers` row.

The reporting tool presents a single row for each matched order–customer pair. Select the description of that row's shape.

A. Only the shared key column.  
B. The order's columns only.  
C. A wider row holding both rows' columns.  
D. Two independent result sets, one for each source table.

### 17. Why EXISTS wears no JOIN badge

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Semi Joins and Anti Joins  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism discrimination

Semi and anti joins are join *concepts*, yet the chapter writes them with EXISTS and NOT EXISTS rather than the JOIN keyword.

Choose the explanation that distinguishes existence filtering from row combination.

A. JOIN syntax is reserved for tables above a minimum row count, while EXISTS handles smaller tables.  
B. Their job is filtering, not combining: just "does a match exist?"  
C. EXISTS is faster in every case, mandatorily.  
D. JOIN cannot reference two tables.

### 18. Reconciling the two rosters

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** RIGHT JOIN and FULL OUTER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Full-outer tracing

A training academy tracks which trainer is assigned to each batch.

`trainers`

| trainer_id | name |
|---|---|
| 1 | Kavi |
| 2 | Meenal |
| 3 | Arif |

`assigned_batches`

| batch_id | trainer_id | batch_name |
|---|---|---|
| 10 | 1 | Alpha |
| 11 | 2 | Bravo |
| 12 | 9 | Ghost |

```sql
SELECT t.name, b.batch_name
FROM trainers t
FULL OUTER JOIN assigned_batches b ON t.trainer_id = b.trainer_id;
```

Reconcile both rosters and select the result count together with the two unmatched entries.

A. 2 rows — matches only.  
B. 3 rows — the batches list wins.  
C. 6 rows — every trainer paired with every batch, followed by removal of duplicate names.  
D. 4 rows — two matched pairs, Arif and Ghost each padded with NULL.

### 19. Never ordered, by name

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Semi Joins and Anti Joins  
**Is Curriculum Based:** No  
**Assessment type:** Anti-join construction

A cheese shop wants products that appear in **no** order line, from `products p` and `order_lines ol`.

Select the query that keeps a product only after failing to find any matching order line.

A. `SELECT p.name FROM products p WHERE NOT EXISTS (SELECT 1 FROM order_lines ol WHERE ol.product_id = p.product_id);`  
B. `SELECT p.name FROM products p WHERE EXISTS (SELECT 1 FROM order_lines ol WHERE ol.product_id = p.product_id AND ol.product_id IS NOT NULL);`  
C. `SELECT p.name FROM products p JOIN order_lines ol ON ol.product_id = p.product_id;`  
D. `SELECT product_id FROM order_lines WHERE product_id IS NULL;`

### 20. One pier, many boats

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INNER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Match-multiplication tracing

A marina tracks which boats are moored at each pier.

`piers`

| pier_id | pier_name |
|---|---|
| 1 | North Pier |
| 2 | South Pier |

`moored_boats`

| boat_id | pier_id | boat_name |
|---|---|---|
| 1 | 1 | Kingfisher |
| 2 | 1 | Osprey |
| 3 | 1 | Tern |
| 4 | 2 | Heron |

```sql
SELECT p.pier_name, b.boat_name
FROM piers p
JOIN moored_boats b ON b.pier_id = p.pier_id;
```

Account for the four result rows without treating the repeated pier name as corrupt data.

A. The join malfunctioned and duplicated data.  
B. Each pier appears once, with all matching boat names combined into one cell automatically.  
C. The join produces one row per pairing: North Pier appears three times.  
D. Two rows are phantom padding.

### 21. What the NULLs are saying

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** LEFT JOIN  
**Is Curriculum Based:** No  
**Assessment type:** NULL-interpretation

In a `venues LEFT JOIN concerts` result, the row for Starlight Amphitheatre shows NULL in every concert column.

Interpret those result-only NULLs in terms of the attempted venue–concert match.

A. The venue's concert data was corrupted during the join, so existing values were replaced by NULL.  
B. Someone stored NULL concerts deliberately.  
C. The venue must be deleted.  
D. No concert row matched this venue; NULLs padded the missing columns.

### 22. The same report, written the other way round

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** RIGHT JOIN and FULL OUTER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Rewrite equivalence

A colleague's query reads `FROM shipments s RIGHT JOIN warehouses w ON s.wh_id = w.wh_id`, and the team style guide prefers LEFT JOIN. The report names its output columns explicitly, so source-column order is not part of the comparison.

Select the rewrite that preserves exactly the same warehouse rows while following the LEFT JOIN style rule.

A. `FROM shipments s LEFT JOIN warehouses w ON s.wh_id = w.wh_id`  
B. `FROM warehouses w LEFT JOIN shipments s ON s.wh_id = w.wh_id`, table order swapped.  
C. `FROM shipments s FULL OUTER JOIN warehouses w ON s.wh_id = w.wh_id`, followed by retaining all unmatched rows from both sides  
D. No LEFT JOIN can reproduce a RIGHT JOIN.

### 23. Why the aliases are not optional here

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Self Joins  
**Is Curriculum Based:** No  
**Assessment type:** Requirement rationale

A self join on `employees(employee_id, name, manager_id)` fails when written without aliases: `FROM employees JOIN employees ON employees.manager_id = employees.employee_id`.

Identify why two aliases are required before the employee and manager roles can be referenced separately.

A. The same table twice needs aliases for distinct names.  
B. Aliases make a self join execute one table reference at a time.  
C. The database bills per table name used.  
D. They are not required; the error is elsewhere.

### 24. Keep the guests, tolerate the missing vehicles

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Multi-Table Joins  
**Is Curriculum Based:** No  
**Assessment type:** Mixed-join-type construction

A resort stores `bookings(booking_id, guest_id)`, `guests(guest_id, guest_name)`, and `vehicles(vehicle_id, guest_id, plate_no)`. Every booking refers to a guest, but registering a vehicle is optional. The report needs every booking with its guest's name and the vehicle plate when one exists.

Choose the join sequence whose preservation rules match both parts of the requirement.

A. `FROM bookings b JOIN guests g ON g.guest_id = b.guest_id JOIN vehicles v ON v.guest_id = g.guest_id`  
B. `FROM bookings b LEFT JOIN guests g ON g.guest_id = b.guest_id LEFT JOIN vehicles v ON v.vehicle_id = b.booking_id`  
C. `FROM bookings b JOIN guests g ON g.guest_id = b.guest_id LEFT JOIN vehicles v ON v.guest_id = g.guest_id`  
D. `FROM bookings b FULL OUTER JOIN guests g ON g.guest_id = b.guest_id FULL OUTER JOIN vehicles v ON v.guest_id = g.guest_id`

### 25. The one-column shortcut

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Semi Joins and Anti Joins  
**Is Curriculum Based:** No  
**Assessment type:** IN-alternative identification

For "cities that have at least one branch," a developer writes:

```sql
SELECT city_name FROM cities
WHERE city_id IN (SELECT city_id FROM branches);
```

Classify this query by the membership question it answers and the number of city rows it produces.

A. It is unrelated because IN only compares literal text values.  
B. It is the semi-join idea in simpler clothing, like EXISTS.  
C. It is an anti-join.  
D. It duplicates each city per branch.

### 26. The unsponsored podcaster

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Semi Joins and Anti Joins  
**Is Curriculum Based:** No  
**Assessment type:** Anti-join tracing

A podcast network tracks which shows have secured brand sponsorships.

`podcasters`

| pod_id | show_name |
|---|---|
| 1 | Night Static |
| 2 | Fieldnotes |
| 3 | The Long Route |

`sponsorships`

| sponsor_id | pod_id | brand |
|---|---|---|
| 1 | 1 | KopiKo |
| 2 | 3 | TrailMix Co |

```sql
SELECT show_name FROM podcasters p
WHERE NOT EXISTS (SELECT 1 FROM sponsorships s WHERE s.pod_id = p.pod_id);
```

Trace the correlated test for each podcast and select the resulting show list.

A. Night Static and The Long Route — the two shows whose correlated test finds matching sponsors.  
B. All three shows.  
C. Nothing; NOT EXISTS needs a JOIN.  
D. Fieldnotes only, the one show with no sponsorship row.

### 27. Why the city was split out at all

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Why Joins Exist  
**Is Curriculum Based:** No  
**Assessment type:** Split-rationale identification

A junior developer asks why the customer's city isn't just stored on every order row, "so we'd never need joins."

Choose the response that connects normalized storage with the later need for a join.

A. Copying the city onto every order stores one fact many times over.  
B. Cities are too long to store on orders.  
C. Joins are retained mainly to preserve an older SQL-writing convention.  
D. The junior is right; all tables should be merged.

### 28. Count the survivors and the padding

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** LEFT JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Row-count computation

A flying club's `pilots` table has 4 rows. Their logged flights: Dara 2 flights, Eshan 0, Farida 1, Gul 3.

`pilots`

| pilot_id | name |
|---:|---|
| 1 | Dara |
| 2 | Eshan |
| 3 | Farida |
| 4 | Gul |

`flights`

| flight_no | pilot_id |
|---|---:|
| F11 | 1 |
| F12 | 1 |
| F13 | 3 |
| F14 | 4 |
| F15 | 4 |
| F16 | 4 |

```sql
SELECT p.name, f.flight_no
FROM pilots p
LEFT JOIN flights f ON f.pilot_id = p.pilot_id;
```

Calculate the number of matched and padded rows in the report.

A. 4 — exactly one output row is guaranteed per pilot, regardless of how many flights match.  
B. 6 — flights only.  
C. 7 — Dara 2, Farida 1, Gul 3, Eshan 1 padded with NULL.  
D. 12 — pilots × flights.

### 29. Missing from either ledger

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** RIGHT JOIN and FULL OUTER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Reconciliation construction

A payments team reconciles `gateway_txns` against `bank_txns` on transaction reference. They need every reference present in one system but absent from the other — both directions in one result.

Choose the join-and-filter pattern that reveals both discrepancy directions.

A. INNER JOIN, then delete the matches.  
B. FULL OUTER JOIN, keeping rows where either side is NULL.  
C. Two INNER JOINs run twice.  
D. LEFT JOIN alone, because only gateway-side omissions matter.

### 30. Jobs that need the mirror

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Self Joins  
**Is Curriculum Based:** No  
**Assessment type:** Use-case recognition

Select the report whose two roles are represented by different rows of the same table.

A. Counting orders per customer.  
B. Combining orders with products across two separate tables here.  
C. Removing duplicate emails.  
D. Showing each employee beside their manager, same table twice.

### 31. When match-only is exactly right

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INNER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Fit judgment

An invoicing run pairs `invoices` with `payments` to list settled invoices — pairs only; unpaid invoices and orphan payments belong to other reports.

Match the report's inclusion rule to the behaviour of `INNER JOIN`.

A. The report's subject is the matched pairs by definition.  
B. INNER JOIN is the only join type permitted for payment tables.  
C. It pads unpaid invoices with NULLs as needed.  
D. It runs the fastest, which settles everything.

### 32. Revenue by city, three tables deep

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Multi-Table Joins  
**Is Curriculum Based:** No  
**Assessment type:** Filter-and-group construction

Tables: `hubs(hub_id, city)`, `couriers(courier_id, hub_id)`, `deliveries(delivery_id, courier_id, fee, delivered_on TIMESTAMP)`. Requirement: total delivery fees per city, June 2025 only.

Select the query that follows the complete relationship path before filtering and grouping.

A. `SELECT h.city, SUM(d.fee) FROM deliveries d GROUP BY h.city;`  
B. `SELECT city, SUM(fee) FROM hubs, deliveries WHERE delivered_on >= DATE '2025-06-01' AND delivered_on < DATE '2025-07-01' GROUP BY city;`  
C. `SELECT h.city, SUM(d.fee) FROM deliveries d JOIN couriers c ON d.courier_id = c.courier_id JOIN hubs h ON c.hub_id = h.hub_id WHERE d.delivered_on >= DATE '2025-06-01' AND d.delivered_on < DATE '2025-07-01' GROUP BY h.city;`  
D. `SELECT h.city, SUM(d.fee) FROM deliveries d JOIN couriers c ON d.courier_id = c.hub_id JOIN hubs h ON c.courier_id = h.hub_id WHERE d.delivered_on >= DATE '2025-06-01' AND d.delivered_on < DATE '2025-07-01' GROUP BY h.city;`

### 33. Has one, or hasn't one

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Semi Joins and Anti Joins  
**Is Curriculum Based:** No  
**Assessment type:** Concept-pair discrimination

Two reports at a subscription service: (1) customers who **have** an active plan; (2) customers who have **none**.

Assign the appropriate existence pattern to each report.

A. Anti join for both, with `ORDER BY` deciding whether customers with plans or without plans are retained.  
B. Report 1 is the semi join (EXISTS); report 2 is the anti join (NOT EXISTS).  
C. Semi join for both.  
D. Neither concept applies to subscriptions.

### 34. Swap the order, change the survivors

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Multi-Table Joins  
**Is Curriculum Based:** No  
**Assessment type:** Order-sensitivity reasoning

Two drafts of a stables report differ only in table order:

- Draft 1: `horses h LEFT JOIN vet_visits v ON v.horse_id = h.horse_id`  
- Draft 2: `vet_visits v LEFT JOIN horses h ON v.horse_id = h.horse_id`

Choose the observation that explains why the two drafts can retain different unmatched rows.

A. LEFT JOIN alphabetizes the first table.  
B. They are equivalent because table order never affects LEFT JOIN or the unmatched rows it preserves.  
C. Draft 2 is a syntax error.  
D. LEFT JOIN preserves the left table; the two drafts differ in who survives.

### 35. Read the padded row

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** LEFT JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Result-content tracing

An arts council tracks which exhibitions are currently running at each gallery.

`galleries`

| gallery_id | gallery_name |
|---|---|
| 1 | Saltwater Arts |
| 2 | Ochre Room |

`exhibitions`

| exh_id | gallery_id | title |
|---|---|---|
| 1 | 1 | Tidal Forms |

```sql
SELECT g.gallery_name, e.title
FROM galleries g
LEFT JOIN exhibitions e ON e.gallery_id = g.gallery_id;
```

Trace the matched and unmatched gallery rows and select the complete result.

A. One row: Saltwater Arts – Tidal Forms.  
B. Two rows, both galleries showing `Tidal Forms` because the one title is copied to every preserved gallery.  
C. Two rows: Saltwater with a title, Ochre Room padded with NULL.  
D. Four rows — both galleries × both columns.

### 36. Choose the join for the depot rule

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** RIGHT JOIN and FULL OUTER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Requirement-to-join mapping

A depot report's rule: show **every warehouse**, even those with no shipments this week; shipments referencing unknown warehouses should not appear.

Select the join whose preserved side exactly matches the depot rule.

A. `warehouses LEFT JOIN shipments` — all warehouses preserved, unmatched dropped.  
B. `warehouses INNER JOIN shipments` — retaining every warehouse with NULL shipment data.  
C. `FULL OUTER JOIN` — unknown-warehouse shipments sneak in.  
D. No join; two separate queries are required.

### 37. The rider at the top of the tree

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Self Joins  
**Is Curriculum Based:** No  
**Assessment type:** Inner-self-join edge tracing

The hierarchy report reuses this source data:

| rider_id | name | mentor_id |
|---:|---|---:|
| 1 | Asha | NULL |
| 2 | Binod | 1 |
| 3 | Chitra | 1 |
| 4 | Dev | 3 |

A manager notices that the inner self join has no row where Asha is the *rider*.

Select the explanation together with the smallest join-type repair.

A. Asha was deleted by the join.  
B. Self joins discard whichever row was inserted first.  
C. A NULL mentor causes the self join to stop before producing later rows.  
D. Asha's `mentor_id` is NULL; a LEFT self join would keep her instead.

### 38. INNER JOIN, at a glance

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INNER JOIN  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

A reviewer must decide whether a draft will exclude every unmatched row. Select the statement that accurately describes `INNER JOIN`.

A. Every row from both tables, with NULL padding wherever either table lacks a matching partner.  
B. Only the left table's rows.  
C. Exactly the row combinations where the ON condition matches both tables.  
D. The rows of whichever table is larger.

### 39. The hub of the star

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Multi-Table Joins  
**Is Curriculum Based:** No  
**Assessment type:** Schema-shape reading

A city-tours schema: `tours(tour_id, guide_id, route_id, van_id, price)` plus `guides`, `routes`, and `vans`, each with its own primary key.

Identify the table that supplies the relationship path needed to reach all three descriptive tables.

A. The three lookup tables must join directly to one another before `tours` can contribute its price.  
B. `tours` is the connecting table, holding a foreign key to each other table.  
C. Four tables cannot be joined in one query.  
D. Only `vans` can join to `tours`.

### 40. Once each, and only the hosts

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Semi Joins and Anti Joins  
**Is Curriculum Based:** No  
**Assessment type:** Integrated pattern selection

An events platform wants venues that have hosted **at least one** concert in 2025 — each venue named once, no concert data in the output. A venue may have hosted dozens.

Select the query that enforces the full 2025 boundary and still returns each qualifying venue once.

A. `SELECT v.venue_name FROM venues v WHERE EXISTS (SELECT 1 FROM concerts c WHERE c.venue_id = v.venue_id AND c.held_on >= DATE '2025-01-01' AND c.held_on < DATE '2026-01-01');`  
B. `SELECT v.venue_name FROM venues v JOIN concerts c ON c.venue_id = v.venue_id WHERE c.held_on >= DATE '2025-01-01' AND c.held_on < DATE '2026-01-01';`  
C. `SELECT v.venue_name FROM venues v WHERE NOT EXISTS (SELECT 1 FROM concerts c WHERE c.venue_id = v.venue_id AND c.held_on >= DATE '2025-01-01' AND c.held_on < DATE '2026-01-01');`  
D. `SELECT venue_id FROM concerts;`

---

## Instructor Key

### 1. B

The split stores each member fact once; the join re-attaches it wherever needed. The design is deliberate — the alternative is the mass-update-and-miss-one problem that normalized storage exists to prevent.

### 2. D

An inner join emits one row per successful pairing: four callouts, four matches. Hilltop has no callout to pair with, and inner joins do not manufacture padding for the unmatched — that is the outer joins' business.

### 3. A

The left table's rows are all guaranteed a presence: Salim rides his two matches, Joel his one, and Priya — matchless — appears once with NULL in the borrowed columns. Four rows: 2 + 1 + 1.

### 4. C

Both directions of mismatch must survive, which is the full outer join's definition: every row from both tables, with NULLs filling whichever side of an unmatched row is absent.

### 5. D

A self join is one table under two aliases, each alias playing a role — the person and the supervisor. The ON clause connects a row's reference column to the *other alias's* key.

### 6. B

`bookings` holds both foreign keys, so it anchors the chain: join to `guests` on the guest key, join to `cabins` on the cabin key. Each JOIN clause walks one relationship.

### 7. C

The requirements — at least one, listed once, no attendance columns — are the semi-join's signature. An inner join (A) would list a frequent patron once per show attended.

### 8. A

The join attaches salon names to all three appointments; WHERE then tests each joined row's bill. Only Glow Studio's 500 and 700 survive — filters compose with joins exactly as they do with single tables.

### 9. B

Two load-bearing choices: LEFT JOIN keeps the zero-sale vendors in the result, and `COUNT(s.sale_id)` counts only non-NULL sale values — so the padded vendors count 0, not 1. Option A's inner join deletes exactly the vendors the report is about.

### 10. D

Joins are the read-side reunion of split data: match related rows on key values and present them together. Nothing is copied, deleted, or compressed.

### 11. C

ON is the matching rule — it defines which cross-table pairings are meaningful. Output columns belong to SELECT; ordering to ORDER BY.

### 12. A

The left join hands every member a row; members with no RSVP carry NULL in the right-side columns, and the IS NULL filter selects precisely those. This is the join-based anti-join pattern from the chapter.

### 13. D

The keyword names the preserved side: RIGHT JOIN guarantees the right table (`licences`) full attendance, padding boat columns with NULL where no boat matches.

### 14. B

Each rider row seeks the row its `mentor_id` names: three riders point at real mentors and pair up. Asha's NULL points at nothing — inner join, no row. (Her *appearing as a mentor* in others' rows is a different column.)

### 15. A

With four tables in one query — and column names like `name` liable to repeat — the prefixes are both disambiguation and documentation. Readability is the difference between a maintainable multi-join and a puzzle.

### 16. C

A join widens: the result row is the concatenation of the two matched rows' columns. That width is the point — the recombined view of the split data.

### 17. B

Semi and anti joins answer membership questions. EXISTS expresses "a match exists" without importing the matched row — no widening, no duplication per match, no unwanted columns. The concept is join-family; the syntax is a filter.

### 18. D

Two matches, plus one orphan per side: Arif (trainer, no batch) and Ghost (batch, no trainer — its ID 9 matches nobody). Full outer's four rows are the complete reconciliation picture in one result.

### 19. A

NOT EXISTS keeps a product exactly when the subquery finds no matching line — the anti-join. Option B is its mirror (the semi-join); option C lists only products that *were* ordered.

### 20. C

Join results count pairings, not tables: North Pier's three boats produce three pairings. The repetition is the one-to-many relationship faithfully rendered — not duplication (A).

### 21. D

Outer-join NULLs are the join's own annotation meaning "no partner found." They were never stored anywhere — they exist only in the result, marking the gap the left join preserved.

### 22. B

RIGHT JOIN preserving `warehouses` equals LEFT JOIN with `warehouses` moved to the left seat. Same preserved side, same result — which is why the chapter treats RIGHT as LEFT's mirror and teams standardize on one.

### 23. A

Using the same table name twice leaves no distinct qualifier for the employee and manager instances. Aliases give those two instances separate names, making the relationship and selected role explicit.

### 24. C

Each relationship gets the join its semantics demand: guests are mandatory (inner), vehicles optional (left). Uniform join types (A, B, D) either delete car-less bookings or invite rows the report never asked for.

### 25. B

For a single-column membership test, `IN (subquery)` is the semi-join in its most readable form. Same verdict as EXISTS: the city appears once if any branch matches, without join duplication.

### 26. D

NOT EXISTS keeps rows with no match in the subquery: only Fieldnotes lacks a sponsorship row. Options A inverts the verdict; the query is anti, not semi.

### 27. A

Copying the fact everywhere trades one join for a permanent update liability: hundreds of copies to keep in agreement, forever. Store once, join on demand is the chapter's one-line answer to "why not just copy it."

### 28. C

Matched pilots appear once per match: 2 + 1 + 3. Unmatched Eshan appears exactly once, padded. Total 7 — the left join's row arithmetic in one example.

### 29. B

Reconciliation needs orphans from both ledgers at once — full outer's exact deliverable. Filtering the joined result for a NULL on either side isolates the discrepancies; a LEFT JOIN (D) sees only one direction of the problem.

### 30. D

The self join exists for row-versus-row questions within one table — hierarchies being the canonical case. The other options are ordinary aggregations, two-table joins, or dedup work.

### 31. A

Fit, not habit: this report defines its subject as the matched pairs, so the join type whose behaviour *is* "matched pairs only" is a perfect match of tool to requirement. NULL padding here would be noise.

### 32. C

Three requirements, three mechanisms: the two-step join chain reaches the city, the half-open date interval includes every June timestamp, and `GROUP BY` totals per city. Option A references `h.city` without joining `hubs`; option B creates an unrelated cross product.

### 33. B

One membership question, two verdicts: EXISTS keeps the members (semi), NOT EXISTS the non-members (anti). Together they partition the customer list.

### 34. D

Outer joins are asymmetric: the left table is the protected one. Swapping the order swaps the protection — different unmatched rows survive, so the drafts genuinely differ. (For *inner* joins alone, order does not change the result.)

### 35. C

Every gallery attends (left join), so Ochre Room appears despite hosting nothing — its title cell is NULL, the join's marker for "no match," never a borrowed value from another row (B).

### 36. A

"Every left-side row, drop unmatched right-side rows" is the left join's exact contract, with warehouses in the left seat. The parenthetical mirror is the same report as a RIGHT JOIN — one behaviour, two spellings.

### 37. D

Inner joins require the match to exist, and NULL matches nothing — the hierarchy's root always falls out of an inner self join. Switching the self join to LEFT keeps the root with NULL mentor columns, the standard fix.

### 38. C

Inner join: the intersection of successful pairings, nothing else. Padding (A) belongs to outer joins; preserving one side (B) to LEFT/RIGHT.

### 39. B

`tours` is the hub carrying all three foreign keys, so every report joins outward from it, one JOIN per spoke. The spokes never need joining to each other — their only relationships run through the hub.

### 40. A

EXISTS delivers the required shape: at least one match, one outer row per venue, and no concert columns. The half-open interval includes every date in 2025 while excluding 2026; option B uses the same boundary but repeats a venue once per matching concert.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Join tracing over shown data | 2, 3, 8, 14, 18, 20, 26, 28, 35 |
| Query and pattern construction | 6, 9, 12, 19, 24, 29, 32, 40 |
| Join-type selection and fit judgment | 4, 7, 22, 31, 36 |
| Mechanism and rationale | 1, 5, 10, 11, 15, 16, 17, 21, 23, 25, 27, 30, 38, 39 |
| Edge cases, order sensitivity, and discrimination | 13, 33, 34, 37 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| Why Joins Exist | 1, 10, 16, 27 | 4 |
| INNER JOIN | 2, 8, 11, 20, 31, 38 | 6 |
| LEFT JOIN | 3, 9, 12, 21, 28, 35 | 6 |
| RIGHT JOIN and FULL OUTER JOIN | 4, 13, 18, 22, 29, 36 | 6 |
| Self Joins | 5, 14, 23, 30, 37 | 5 |
| Multi-Table Joins | 6, 15, 24, 32, 34, 39 | 6 |
| Semi Joins and Anti Joins | 7, 17, 19, 25, 26, 33, 40 | 7 |

Questions 1–10 collectively cover all seven Topic 4.3 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (10, 13, 15, 16, 21, 25, 27, 30, 31, 38)
- Intermediate: 26 questions
- Advanced: 4 questions (18, 29, 32, 40)
- Correct option A: 10 questions (3, 8, 12, 15, 19, 23, 27, 31, 36, 40)
- Correct option B: 10 questions (1, 6, 9, 14, 17, 22, 25, 29, 33, 39)
- Correct option C: 10 questions (4, 7, 11, 16, 20, 24, 28, 32, 35, 38)
- Correct option D: 10 questions (2, 5, 10, 13, 18, 21, 26, 30, 34, 37)
- Longest consecutive run of one correct letter: below 3 throughout
