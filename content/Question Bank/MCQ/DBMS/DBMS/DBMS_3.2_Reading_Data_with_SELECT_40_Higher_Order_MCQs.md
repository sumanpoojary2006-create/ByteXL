# DBMS 3.2: Reading Data with SELECT — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** SQL Essentials
- **Chapter:** Reading Data with SELECT
- **Scope:** All six Topic 3.2 subtopics in the attached course blueprint (The SELECT Statement; Column and Table Aliases; DISTINCT; Expressions and Calculated Columns; Sorting Results; Limiting Results)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every scenario defines the database table, field meanings, and requested result before asking for a judgment. Source tables, expected-result requirements, and executable PostgreSQL fragments are used so outputs can be traced rather than guessed.
- **Scope guard:** Questions use only the six SELECT features taught in Topic 3.2; no filtering, aggregation, joins, or later SQL concepts are required.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all six Topic 3.2 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Two columns of the nursery

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The SELECT Statement  
**Is Curriculum Based:** No  
**Assessment type:** Result-shape tracing

An online nursery lists its plants for sale, tracking each one's price and light requirements.

`plants`

| plant_id | name | price | light_needs |
|---|---|---|---|
| 1 | Monstera | 850 | Indirect |
| 2 | Snake Plant | 400 | Low |
| 3 | Fiddle Fig | 1200 | Bright |
| 4 | Pothos | 300 | Low |

```sql
SELECT name, price FROM plants;
```

Record the exact row-and-column shape produced by the projection.

A. Four rows with exactly two columns each: name and price.  
B. Two rows with four columns.  
C. Only the Monstera row, fully.  
D. All four columns, but only for plants under 500 rupees exactly.

### 2. The headers on the yearly bill

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Column and Table Aliases  
**Is Curriculum Based:** No  
**Assessment type:** Alias-output tracing

A subscription service lists its plans along with their monthly price.

`plans`

| plan_name | monthly_price |
|---|---|
| Basic | 99 |
| Plus | 199 |

```sql
SELECT plan_name, monthly_price * 12 AS yearly_price FROM plans;
```

Complete the result header after PostgreSQL applies the alias.

A. `plan_name` and `monthly_price * 12`, unaliased and raw.  
B. `plan_name` and `monthly_price`  
C. `yearly_price` only  
D. `plan_name` and `yearly_price`, renamed via alias.

### 3. How many cities, really?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DISTINCT  
**Is Curriculum Based:** No  
**Assessment type:** DISTINCT tracing

An EV network tracks which city each of its charging stations is located in.

`charging_stations`

| station_id | city |
|---|---|
| 1 | Pune |
| 2 | Pune |
| 3 | Surat |
| 4 | Jaipur |
| 5 | Surat |

```sql
SELECT DISTINCT city FROM charging_stations;
```

Count the rows remaining after duplicate city values collapse.

A. 5 — one per station.  
B. 3 — Pune, Surat, Jaipur.  
C. 2 — only the cities that repeat here.  
D. 1 — the first city found.

### 4. Arithmetic on line two

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Expressions and Calculated Columns  
**Is Curriculum Based:** No  
**Assessment type:** Expression tracing

A stationery shop's order system logs each line item ordered, along with its quantity and unit price.

`order_lines`

| line_id | item | qty | unit_price |
|---|---|---|---|
| 1 | Notebook | 2 | 120 |
| 2 | Marker set | 4 | 75 |
| 3 | Easel | 1 | 999 |

```sql
SELECT item, qty * unit_price AS line_total FROM order_lines;
```

Trace the expression for the Marker set row.

A. 79 — the two values added.  
B. 75 — calculated columns always repeat the stored unit price.  
C. 300 — 4 × 75, computed by the expression.  
D. 475 — the price plus a fixed fee.

### 5. Highest price first

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Sorting Results  
**Is Curriculum Based:** No  
**Assessment type:** Sort tracing

A power-bank rental service lists its kiosks along with their hourly rental rate.

`powerbank_rentals`

| kiosk | hourly_rate |
|---|---|
| Metro Gate | 40 |
| Airport T2 | 90 |
| City Mall | 60 |

```sql
SELECT kiosk, hourly_rate FROM powerbank_rentals ORDER BY hourly_rate DESC;
```

Identify the first row after applying the descending sort.

A. Metro Gate (40) — `DESC` places the smallest value first and preserves it at the top.  
B. Airport T2 (90) — descending puts the largest rate on top.  
C. City Mall (60) — the middle value leads.  
D. Whichever row was inserted first.

### 6. The top two, and only the top two

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Limiting Results  
**Is Curriculum Based:** No  
**Assessment type:** LIMIT-with-sort tracing

A street-festival organizer tracks the crowd rating earned by each performing band.

`street_bands`

| band | crowd_rating |
|---|---|
| Brass Monkeys | 4.8 |
| Tin Lids | 4.2 |
| Velvet Horns | 4.9 |
| Echo Pips | 3.9 |

```sql
SELECT band FROM street_bands ORDER BY crowd_rating DESC LIMIT 2;
```

Trace the sort first, then retain only the rows surviving `LIMIT 2`.

A. Velvet Horns and Brass Monkeys — the two highest ratings.  
B. Brass Monkeys and Tin Lids — the first two rows of the table itself.  
C. Echo Pips and Tin Lids — LIMIT takes from the bottom.  
D. All four bands; LIMIT is advisory.

### 7. The report that dragged forty columns

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The SELECT Statement  
**Is Curriculum Based:** No  
**Assessment type:** Practice-rationale judgment

A fleet dashboard has this dependency:

| Dashboard need | Current query behavior |
|---|---|
| `vehicle_no`, `battery_pct` | Retrieves all 40 telemetry columns |
| Stable output contract | Changes whenever the table gains or renames a column |
| Network transfer | Carries 38 unused columns per row |

Choose the review finding supported by all three pieces of evidence.

A. The asterisk is deprecated syntax.  
B. Star projection guarantees a different row order on every execution and prevents stable application output.  
C. `SELECT *` cannot be combined with WHERE.  
D. It hauls every column, coupling the app to the table's current shape.

### 8. Assembling the badge line

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Expressions and Calculated Columns  
**Is Curriculum Based:** No  
**Assessment type:** Concatenation tracing

A conference tracks its speakers' first and last names to print badges.

`speakers`

| first_name | last_name |
|---|---|
| Anita | Rao |
| Farid | Khan |

```sql
SELECT first_name || ' ' || last_name AS badge_name FROM speakers;
```

Build the first output value exactly as the concatenation specifies.

A. `first_name last_name` — literals only.  
B. `AnitaRao`, because a literal space is ignored during concatenation.  
C. `Anita Rao` — joined with the literal space between them.  
D. An error; text cannot be combined.

### 9. Salty before sweet, pricey before cheap

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Sorting Results  
**Is Curriculum Based:** No  
**Assessment type:** Multi-column sort tracing

A cinema snack counter tracks each item's category and price.

`snacks`

| item | category | price |
|---|---|---|
| Chips | Salty | 30 |
| Cookies | Sweet | 50 |
| Peanuts | Salty | 45 |
| Fudge | Sweet | 40 |

```sql
SELECT item FROM snacks ORDER BY category ASC, price DESC;
```

Trace both sort keys and record the complete item order.

A. Peanuts, Chips, Cookies, Fudge — Salty before Sweet, higher price first.  
B. Chips, Peanuts, Fudge, Cookies — ascending price inside each category here.  
C. Cookies, Fudge, Peanuts, Chips — Sweet sorts first.  
D. Chips, Cookies, Peanuts, Fudge — the original table order.

### 10. What the keyword collapses

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DISTINCT  
**Is Curriculum Based:** No  
**Assessment type:** Concept identification

A delivery log stores one row per completed trip:

| trip_id | rider_name |
|---|---|
| T1 | Asha |
| T2 | Asha |
| T3 | Bilal |

The real table has 200 rows and many repeated rider names. A report adds `DISTINCT` to its selected `rider_name`.

Classify the result-level effect of `DISTINCT`.

A. Deletes the duplicate rows from the table permanently and irreversibly.  
B. Hides the rider from future queries.  
C. Sorts the names alphabetically.  
D. Collapses repeated result rows so each distinct value appears once.

### 11. The whole table, please

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The SELECT Statement  
**Is Curriculum Based:** No  
**Assessment type:** Syntax-meaning identification

A ferry table contains:

| sailing_id | route | departs_at |
|---|---|---|
| S1 | Harbour–Island | `08:00` |
| S2 | Harbour–Island | `12:00` |

The clerk runs `SELECT * FROM sailings;`.

Complete the projection meaning of the asterisk.

A. Only the primary-key column.  
B. Every column of every row in `sailings`.  
C. A random sample of rows.  
D. The table's definition rather than its actual data content.

### 12. The single letter that stands for a table

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Column and Table Aliases  
**Is Curriculum Based:** No  
**Assessment type:** Table-alias reading

A resort stores one row per reservation, with `guest_name` and `nights` as columns. Its query reads:

```sql
SELECT r.guest_name, r.nights FROM reservations r;
```

Identify the role played by `r` for the lifetime of this query.

A. A column of the reservations table.  
B. A syntax error the database ignores.  
C. A table alias — a short temporary name for `reservations`.  
D. A built-in keyword meaning “recent rows” and automatically choosing the newest reservations.

### 13. Combinations, not columns

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DISTINCT  
**Is Curriculum Based:** No  
**Assessment type:** Multi-column DISTINCT tracing

A ride-hailing operator tracks which city each cab in its fleet serves and its fuel type.

`cab_fleet`

| cab_id | city | fuel_type |
|---|---|---|
| 1 | Pune | CNG |
| 2 | Pune | EV |
| 3 | Pune | CNG |
| 4 | Surat | EV |

```sql
SELECT DISTINCT city, fuel_type FROM cab_fleet;
```

Count unique combinations rather than unique values from either column alone.

A. 3 — the distinct (city, fuel_type) pairs.  
B. 2 — the two distinct cities.  
C. 4 — `DISTINCT` applies independently to each source row.  
D. 2 — the two distinct fuel types.

### 14. Grams beside the name

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Expressions and Calculated Columns  
**Is Curriculum Based:** No  
**Assessment type:** Mixed-column tracing

A courier service records the weight of each parcel it ships.

`parcels`

| parcel_code | weight_kg |
|---|---|
| PX-1 | 2.5 |
| PX-2 | 0.8 |

```sql
SELECT parcel_code, weight_kg * 1000 AS weight_g FROM parcels;
```

Trace both selected expressions for the first parcel.

A. (2500, PX-1), reversed order.  
B. (PX-1, 2.5)  
C. (PX-1, 1000), using the wrong conversion factor entirely.  
D. (PX-1, 2500), the computed grams value.

### 15. No direction given

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Sorting Results  
**Is Curriculum Based:** No  
**Assessment type:** Default-direction identification

A seed archive contains:

| variety |
|---|
| Zinnia |
| Amaranth |
| Marigold |

The librarian runs `SELECT variety FROM seeds ORDER BY variety;` with no explicit direction.

Apply PostgreSQL's default sort direction to the shown values.

A. Descending — Z to A.  
B. Ascending — A to Z, default when no direction given.  
C. In insertion order.  
D. In an undefined direction because omitting `ASC` disables sorting.

### 16. Three of the many

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Limiting Results  
**Is Curriculum Based:** No  
**Assessment type:** LIMIT mechanics

A job board's query plan is:

| Stage | Clause |
|---|---|
| Rank postings | `ORDER BY posted_on DESC` |
| Trim result | `LIMIT 3` |
| Available rows | 500 |

Complete the job-board result promise.

A. Three random postings.  
B. All 500 postings, marked in threes.  
C. Exactly the 3 most recent postings, first three rows kept.  
D. Postings 498, 499, and 500 in original table order, unsorted.

### 17. Why one sort key wasn't enough

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Sorting Results  
**Is Curriculum Based:** No  
**Assessment type:** Multi-key rationale

A marathon page currently uses one sort key:

| runner | city | finish_time |
|---|---|---|
| Mira | Pune | `03:42:10` |
| Zoya | Pune | `03:38:20` |
| Arun | Surat | `03:51:00` |

Within Pune, the order is not defined by the query.

Select the smallest repair that makes tied city groups deterministic.

A. Add a second sort key: `ORDER BY city, finish_time`.  
B. Remove ORDER BY entirely so the database picks a natural order.  
C. Sort in the application instead; SQL cannot sort twice.  
D. Use DISTINCT to remove the tied runners.

### 18. "Top five" of nothing in particular

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Limiting Results  
**Is Curriculum Based:** No  
**Assessment type:** LIMIT-without-order critique

A sales dashboard shows:

| Widget promise | Current query |
|---|---|
| Five highest-value deals | `SELECT deal_name, amount FROM deals LIMIT 5;` |
| Explicit ranking clause | None |

Some runs therefore include small deals.

Diagnose why the widget cannot honestly promise “Top 5.”

A. LIMIT 5 needs parentheses.  
B. The deals table is too small.  
C. PostgreSQL does not permit the value 5 after `LIMIT`, because only powers of ten are supported.  
D. Without ORDER BY, LIMIT slices five arbitrary, unsorted rows.

### 19. The two-column surprise

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DISTINCT  
**Is Curriculum Based:** No  
**Assessment type:** Misconception correction

A dealership sample contains:

| brand | model |
|---|---|
| Tata | Nexon |
| Tata | Punch |
| Tata | Nexon |
| Kia | Seltos |

The analyst runs `SELECT DISTINCT brand, model FROM cars;` but expected one row per brand.

Correct the analyst's unit of distinctness.

A. DISTINCT is broken for text columns.  
B. The query should have used LIMIT.  
C. DISTINCT applies to the combination of selected columns.  
D. `DISTINCT` works only when every selected column is numeric.

### 20. One column, repeats and all

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The SELECT Statement  
**Is Curriculum Based:** No  
**Assessment type:** Plain-projection tracing

A webinar platform logs which topic each signup registered interest in.

`webinar_signups`

| signup_id | topic |
|---|---|
| 1 | Pricing |
| 2 | Onboarding |
| 3 | Pricing |
| 4 | Pricing |

```sql
SELECT topic FROM webinar_signups;
```

Trace the plain projection without silently adding `DISTINCT`.

A. Two rows — Pricing and Onboarding.  
B. Four rows: Pricing, Onboarding, Pricing, Pricing.  
C. One row containing all four topics.  
D. An error because a SELECT list must contain at least two columns.

### 21. The keyword you may omit but shouldn't

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Column and Table Aliases  
**Is Curriculum Based:** No  
**Assessment type:** Convention judgment

A marina compares two successful queries:

```sql
SELECT berth_fee * 1.18 AS fee_with_tax FROM berths;
SELECT berth_fee * 1.18 fee_with_tax FROM berths;
```

| Version | Result header |
|---|---|
| With `AS` | `fee_with_tax` |
| Without `AS` | `fee_with_tax` |

Choose the comparison that separates valid syntax from preferred readability.

A. The second version computes a different tax.  
B. The first is invalid because PostgreSQL forbids `AS` before a column alias.  
C. Only the first returns a named column.  
D. AS is optional — both alias the column identically — but worth writing.

### 22. When collapsing hides the truth

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DISTINCT  
**Is Curriculum Based:** No  
**Assessment type:** Appropriateness judgment

A pharmacy records one row per completed sale:

| sale_id | product_name |
|---|---|
| S1 | Paracetamol |
| S2 | Paracetamol |
| S3 | Bandage |

A trainee selects only `product_name` with `DISTINCT` and calls the shorter output a cleaned sales listing.

Decide whether the shorter result still represents the sales log truthfully.

A. DISTINCT was the wrong tool; each repeat is a real sale.  
B. The trainee is right because every repeated product name represents duplicate data.  
C. DISTINCT malfunctioned and needs reinstalling.  
D. The log table itself should be deduplicated instead.

### 23. The discount that changed nothing

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Expressions and Calculated Columns  
**Is Curriculum Based:** No  
**Assessment type:** Side-effect reasoning

A boutique compares source and query result:

| dress_name | Stored `price` | Calculated `sale_price` |
|---|---:|---:|
| Linen Wrap | 2000 | 1800 |

The result came from `SELECT dress_name, price * 0.9 AS sale_price FROM dresses;`. Reopening `dresses` still shows 2000.

Explain why the preview did not mutate the source value.

A. The query failed silently.  
B. The discount rounds to zero.  
C. Expressions compute values in the result only, not written back.  
D. Numeric columns cannot be changed by any SQL statement, so every calculation is permanently read-only.

### 24. Freshest first

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Sorting Results  
**Is Curriculum Based:** No  
**Assessment type:** Date-sort tracing

A fishing cooperative logs which boat landed its catch and on what date.

`catch_log`

| boat | landed_on |
|---|---|
| Tern | 2025-06-01 |
| Gull | 2025-06-14 |
| Heron | 2025-05-28 |

```sql
SELECT boat FROM catch_log ORDER BY landed_on DESC;
```

Identify the first boat after sorting the dates newest to oldest.

A. Tern  
B. Gull — 14 June is the latest date, DESC first.  
C. Heron  
D. PostgreSQL cannot sort columns containing dates.

### 25. Skipping the podium

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Limiting Results  
**Is Curriculum Based:** No  
**Assessment type:** OFFSET tracing

A trivia night tracks each player's final score.

`quiz_scores`

| player | score |
|---|---|
| Vik | 92 |
| Nia | 88 |
| Raj | 85 |
| Zoe | 80 |
| Kim | 76 |

```sql
SELECT player FROM quiz_scores ORDER BY score DESC LIMIT 2 OFFSET 2;
```

Skip the requested ranks, then collect the next two players.

A. Vik and Nia — the top two.  
B. Zoe and Kim — the bottom two.  
C. Nia and Raj — `OFFSET 2` skips only the first row and begins collecting at rank two.  
D. Raj and Zoe — OFFSET skips two, LIMIT takes next two.

### 26. Page three of the catalogue

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Limiting Results  
**Is Curriculum Based:** No  
**Assessment type:** Pagination construction

An antique catalogue defines:

| Setting | Value |
|---|---:|
| Rows per page | 10 |
| Requested page | 3 |
| Stable order | Item name ascending |
| Rows already shown | 20 |

Calculate the page-three offset and select the matching clause pair.

A. `LIMIT 3 OFFSET 10`, far too few items shown here.  
B. `LIMIT 30 OFFSET 0`, way too many items shown.  
C. `LIMIT 10 OFFSET 20`, skipping pages one and two.  
D. `LIMIT 10 OFFSET 3`

### 27. The clause that names the source

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The SELECT Statement  
**Is Curriculum Based:** No  
**Assessment type:** Clause-role identification

A glider database parses this query:

| Clause | Text |
|---|---|
| Selected field | `tail_number` |
| Source clause | `FROM gliders` |

What role does the source clause perform?

A. Filters out old rows.  
B. Names the table the query reads from.  
C. Sorts the results.  
D. Renames `tail_number` in the stored table.

### 28. Building the label in one expression

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Expressions and Calculated Columns  
**Is Curriculum Based:** No  
**Assessment type:** Expression construction

A courier has one row:

| full_name | flat_no | area | Required label |
|---|---|---|---|
| Meera Shah | Flat 4B | Baner | Meera Shah, Flat 4B, Baner |

Complete the label expression using PostgreSQL's text-concatenation operator.

A. `full_name || ', ' || flat_no || ', ' || area AS label`.  
B. `full_name + flat_no + area AS label`  
C. `CONCAT ALL columns AS label`  
D. `full_name AND flat_no AND area AS label` — invalid, wrong operator.

### 29. Columns in the order you asked

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The SELECT Statement  
**Is Curriculum Based:** No  
**Assessment type:** Projection-order tracing

A kayak rental shop tracks each kayak's colour and length.

`kayaks`

| kayak_id | colour | length_cm |
|---|---|---|
| 1 | Red | 320 |

```sql
SELECT length_cm, colour FROM kayaks;
```

Record the output columns in the order dictated by the SELECT list.

A. `kayak_id, colour, length_cm` — table order always wins.  
B. `colour, length_cm` — alphabetical order.  
C. Undefined; column order is random.  
D. `length_cm, colour` — the SELECT list's order wins.

### 30. Shortening the long name

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Column and Table Aliases  
**Is Curriculum Based:** No  
**Assessment type:** Alias-rewrite selection

A warehouse query needs two fields from a long table name:

| Source table | Required fields | Desired alias |
|---|---|---|
| `warehouse_stock_movements` | `qty`, `moved_on` | `m` |

Approve the rewrite that declares and then consistently uses alias `m`.

A. `SELECT qty FROM warehouse_stock_movements RENAME m;` — invalid keyword.  
B. `SELECT m.qty FROM m.warehouse_stock_movements;`  
C. `SELECT m.qty, m.moved_on FROM warehouse_stock_movements m;`.  
D. `ALIAS warehouse_stock_movements AS m; SELECT qty;`

### 31. Two routes, three rows

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DISTINCT  
**Is Curriculum Based:** No  
**Assessment type:** Combination counting

A campus shuttle service logs each run's route and day of the week.

`shuttle_runs`

| run_id | route | day |
|---|---|---|
| 1 | R1 | Mon |
| 2 | R1 | Tue |
| 3 | R2 | Mon |
| 4 | R1 | Mon |

An operations head expects `SELECT DISTINCT route, day FROM shuttle_runs;` to return 2 rows "because there are 2 routes," but it returns 3.

Enumerate the distinct route-day pairs remaining after the duplicate collapses.

A. R1 and R2 — the head was right after all.  
B. (R1, Mon), (R1, Tue), (R2, Mon) — the distinct pairs remaining.  
C. All four rows — DISTINCT never removes anything.  
D. (Mon), (Tue) — `DISTINCT` discards every selected column except the last.

### 32. The margin column that isn't stored

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Expressions and Calculated Columns  
**Is Curriculum Based:** No  
**Assessment type:** Expression tracing

A consignment shop tracks each item's sale price and what it cost to acquire.

`consignments`

| item | sale_price | cost |
|---|---|---|
| Vintage radio | 2400 | 1500 |
| Brass lamp | 900 | 700 |

```sql
SELECT item, sale_price - cost AS margin FROM consignments;
```

Trace the subtraction for the Vintage radio row.

A. 900 — 2400 minus 1500, computed on the fly.  
B. 3900 — the two values summed.  
C. 2400 — subtraction expressions return the left operand unchanged.  
D. NULL — subtraction needs a stored column.

### 33. Tie on the ratings

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Sorting Results  
**Is Curriculum Based:** No  
**Assessment type:** Mixed-direction multi-sort tracing

A food-review app tracks each café's rating and average bill.

`cafes`

| name | rating | avg_bill |
|---|---|---|
| Brew Lab | 4.5 | 300 |
| Roast Row | 4.7 | 250 |
| Steep House | 4.5 | 200 |

```sql
SELECT name FROM cafes ORDER BY rating DESC, avg_bill ASC;
```

Apply the primary sort and then use the bill amount only to break the rating tie.

A. Brew Lab, Roast Row, Steep House — table order.  
B. Steep House, Brew Lab, Roast Row — cheapest first overall.  
C. Roast Row, Brew Lab, Steep House — higher bill breaks the tie first here.  
D. Roast Row, Steep House, Brew Lab — highest rating, then ascending bill.

### 34. Asking for more rows than exist

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Limiting Results  
**Is Curriculum Based:** No  
**Assessment type:** Edge-case mechanics

A stall directory's query state is:

| Available rows | Requested ceiling |
|---:|---:|
| 4 | `LIMIT 10` |

Record the edge-case result when the ceiling exceeds the available rows.

A. An error because `LIMIT` may not exceed the available row count.  
B. All 4 rows return, without error; LIMIT is a ceiling only.  
C. The 4 rows repeat until 10 are shown.  
D. Six blank rows pad the result.

### 35. The order that vanished by morning

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Sorting Results  
**Is Curriculum Based:** No  
**Assessment type:** Scope-of-effect reasoning

An auction log records:

| Session | Query |
|---|---|
| Today | `SELECT lot_no FROM lots ORDER BY lot_no;` |
| Tomorrow | Colleague runs `SELECT lot_no FROM lots;` |

Correct the auctioneer's assumption about the scope of `ORDER BY`.

A. The table is now permanently sorted for everyone.  
B. The sort persists until the next insert.  
C. ORDER BY arranges only the query's result set at query time.  
D. The next session automatically reuses the previous session's sort.

### 36. Three cheapest, by construction

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Limiting Results  
**Is Curriculum Based:** No  
**Assessment type:** Query construction

A camping site has:

| model | price |
|---|---:|
| Solo | 3200 |
| Ridge | 4800 |
| Family | 7200 |
| Trail | 3900 |

It needs exactly the three cheapest models, cheapest first.

Approve the query whose sort direction defines “cheapest” before limiting.

A. `SELECT model, price FROM tents ORDER BY price ASC LIMIT 3;`.  
B. `SELECT model, price FROM tents LIMIT 3 ORDER BY price;`  
C. `SELECT model, price FROM tents ORDER BY price DESC LIMIT 3;` — wrong direction.  
D. `SELECT DISTINCT price FROM tents LIMIT 3;`

### 37. Order the tax onto the header

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Column and Table Aliases  
**Is Curriculum Based:** No  
**Assessment type:** Alias-construction selection

A taxi report specifies:

| Stored column | Required expression | Required header |
|---|---|---|
| `fare` | `fare * 1.05` | `fare_with_tax` |

Complete the calculated column and assign its required header.

A. `SELECT fare * 1.05 FROM trips;`  
B. `SELECT fare * 1.05 AS fare_with_tax FROM trips;`.  
C. `SELECT fare_with_tax FROM trips;`  
D. `SELECT fare AS fare * 1.05 FROM trips;` — invalid alias placement.

### 38. One row, three outputs

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Expressions and Calculated Columns  
**Is Curriculum Based:** No  
**Assessment type:** Multi-expression tracing

A comedy club tracks the base ticket price and booking fee for each show.

`tickets`

| show | base_price | booking_fee |
|---|---|---|
| Comedy Night | 400 | 50 |

```sql
SELECT show,
       base_price + booking_fee AS total,
       base_price * 0.05 AS artist_levy
FROM tickets;
```

Evaluate both expressions independently and preserve SELECT-list order.

A. (Comedy Night, 400, 50), wrong total.  
B. (450, 20, Comedy Night), wrong column order entirely here.  
C. (Comedy Night, 450, 25), wrong levy amount.  
D. (Comedy Night, 450, 20), computed independently.

### 39. Sort the timetable properly

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Sorting Results  
**Is Curriculum Based:** No  
**Assessment type:** Clause construction

A yoga timetable contains:

| class_name | class_date | starts_at |
|---|---|---|
| Flow | 2026-08-12 | 18:00 |
| Basics | 2026-08-12 | 08:00 |
| Restore | 2026-08-13 | 07:30 |

The result must order dates earliest first, then times earliest first within each date.

Construct the two-key timetable ordering.

A. `ORDER BY starts_at, class_date`  
B. `ORDER BY class_date DESC, starts_at DESC` — wrong direction entirely.  
C. `ORDER BY class_date ASC, starts_at ASC`, date then time.  
D. `ORDER BY class_name`

### 40. The leaderboard's second screen

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Limiting Results  
**Is Curriculum Based:** No  
**Assessment type:** Integrated construction

An arcade's pagination contract is:

| Setting | Value |
|---|---|
| Ranking | Highest score first |
| Rows per screen | 5 |
| Requested screen | 2 |
| Rows to skip | 5 |

Approve the query that defines the ranking before applying the second-screen slice.

A. `SELECT player, score FROM arcade_scores ORDER BY score DESC LIMIT 5 OFFSET 5;`.  
B. `SELECT player, score FROM arcade_scores LIMIT 5 OFFSET 5;`  
C. `SELECT player, score FROM arcade_scores ORDER BY score DESC LIMIT 10;`  
D. `SELECT player, score FROM arcade_scores ORDER BY score ASC LIMIT 5 OFFSET 5;` — wrong direction.

---

## Instructor Key

### 1. A

Naming two columns projects just those two; every row still participates. Four plants in, four two-column rows out.

### 2. D

The alias gives the calculated output the header `yearly_price`, while `plan_name` keeps its stored name. Without an alias, PostgreSQL may supply an implementation-generated heading such as `?column?`; the stored `monthly_price` column is never renamed.

### 3. B

DISTINCT collapses the five city values to their three distinct members. Option C reflects a common misread — DISTINCT keeps one copy of everything, including values that never repeated.

### 4. C

The expression evaluates per row: 4 × 75 = 300 on the Marker set row. Each row's `line_total` is its own qty × price, not a shared figure.

### 5. B

DESC means largest first: 90 leads. Option A states ascending behaviour under a descending label — the exact confusion the two keywords exist to settle.

### 6. A

The sort ranks 4.9, 4.8, 4.2, 3.9; LIMIT 2 keeps the first two of that ranking — Velvet Horns, then Brass Monkeys. LIMIT slices the *ordered* result, not the table's storage order (B).

### 7. D

Two documented costs: hauling unneeded data, and silent coupling — `SELECT *` changes meaning whenever the table changes shape, which is how the rename broke the dashboard. Explicit columns make the query say what it needs.

### 8. C

Concatenation joins the pieces in written order: value, literal space, value — `Anita Rao`. The literals supply exactly the characters the values lack (B).

### 9. A

The first key groups: Salty before Sweet. The second orders within each group, descending: Peanuts (45) before Chips (30); Cookies (50) before Fudge (40). Option B applies ASC where DESC was written.

### 10. D

DISTINCT is a result-shaping keyword: repeated result rows collapse to one. The stored 200 rows remain — reading never edits (A).

### 11. B

The asterisk is shorthand for "every column"; with no other clauses, every row comes too. It requests data, not the definition (D).

### 12. C

Declaring `reservations r` creates a query-lifetime nickname. Every `r.` reference reads as "of reservations" — brevity without ambiguity.

### 13. A

Multi-column DISTINCT deduplicates the tuples: cab 3 repeats (Pune, CNG) and collapses; three distinct pairs remain. Options B and D each imagine one column deduplicated alone.

### 14. D

Ordinary columns and expressions mix freely in one SELECT: the code passes through, the multiplication computes 2500 beside it, and the result's column order follows the SELECT list.

### 15. B

Unspecified direction is ascending — A to Z, small to large, early to late. The default is defined, not random (D).

### 16. C

The result is built ordered-then-cut: newest postings first, and the knife falls after three. Which three rows arrive is entirely the ORDER BY's decision — that is why the pairing is meaningful.

### 17. A

Rows tied on the sort key have no promised order, and may shuffle between runs. A second key gives the ties their own rule — determinism restored inside each city group.

### 18. D

LIMIT alone answers "any five," not "top five." The widget's instability is the arbitrariness made visible; ORDER BY is the missing definition of "top."

### 19. C

DISTINCT's unit is the whole selected tuple. Six models of one brand are six distinct pairs, all legitimately present. Expecting per-column deduplication is the classic first misreading.

### 20. B

Plain projection preserves the row count: four rows, however repetitive. Deduplication is a separate, opt-in keyword — this query never asked for it.

### 21. D

Both parse identically; AS is grammar sugar. The chapter's advice is readability economics: one optional word, and every future reader instantly sees "this is a renaming."

### 22. A

Each log row is an event; repetition *is* the data. DISTINCT belongs where duplicates are noise (listing which topics exist), not where they are the count of things that happened. Tool correct, application wrong.

### 23. C

SELECT is read-only: expressions compute into the result set and vanish with it. Changing stored prices is a different statement's job entirely — which is a safety feature, not a limitation.

### 24. B

Dates sort like values: 14 June is the largest, and DESC surfaces it first. Heron's May date sorts last.

### 25. D

The ordered list is Vik, Nia, Raj, Zoe, Kim. OFFSET 2 discards Vik and Nia; LIMIT 2 then keeps Raj and Zoe — the classic "next page" slice.

### 26. C

Pages one and two consumed 20 ordered rows; page three starts at row 21. OFFSET counts the skipped rows (20), LIMIT counts the page size (10) — option D swaps their roles.

### 27. B

FROM supplies the source. In a single-table SELECT its whole job is naming which table's rows flow into the rest of the query.

### 28. A

`||` chains values and literals left to right; the `', '` literals provide the punctuation between the three column values. `+` (B) is arithmetic, not text joining.

### 29. D

The SELECT list is also the layout: columns appear in the order asked, regardless of the table's stored order. Queries own their result's shape.

### 30. C

The alias is declared by apposition — table name, space, alias — and then used as the prefix. Options A, B, and D invent syntax around the right idea.

### 31. B

DISTINCT judged the pairs: run 4's (R1, Mon) duplicates run 1's and collapses; (R1, Tue) differs on day and survives. Two routes but three route-day combinations — the query answered the question actually asked of it.

### 32. A

The expression subtracts per row: 2400 − 1500 = 900, labelled `margin` for this result only. Nothing is stored; the column exists for the length of the answer.

### 33. D

Rating ranks first: Roast Row (4.7) leads. The 4.5 tie is handed to the second key, ascending bill: Steep House (200) before Brew Lab (300). Each key rules only where the previous one tied.

### 34. B

LIMIT caps, never demands: a 4-row result under a 10-row ceiling passes through whole. No error, no padding, no recycling.

### 35. C

Result sets are ordered; tables are not. ORDER BY is an instruction about the answer's presentation, evaluated fresh per query — nothing about storage changed, so there is nothing to inherit.

### 36. A

Cheapest-first ascending sort makes the first three rows the three cheapest; LIMIT harvests exactly them. Option C's DESC would deliver the three *most expensive* — the same knife on the wrong end.

### 37. B

The requirement is a computed value under a required name: expression plus alias. Option C asks for a column that doesn't exist; option A leaves the header as raw formula text.

### 38. D

Each output is computed independently from the row: the text passes through, 400 + 50 makes 450, and 400 × 0.05 makes 20. Option C mistakenly levies the total rather than the base price.

### 39. C

Two requirements, two keys, both ascending: date groups the timetable, time orders within the day. Option A inverts the hierarchy — time would outrank date.

### 40. A

Three pieces, all load-bearing: DESC defines the ranking, OFFSET 5 skips screen one, LIMIT 5 sizes screen two. Option B forgets the ranking; option D ranks from the bottom.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Result tracing over shown data | 1, 2, 3, 4, 5, 6, 8, 9, 13, 14, 20, 24, 25, 29, 31, 32, 33, 38 |
| Query and clause construction | 26, 28, 30, 36, 37, 39, 40 |
| Misconception correction and critique | 7, 18, 19, 21, 22, 23, 35 |
| Mechanics and edge cases | 10, 11, 12, 15, 16, 17, 27, 34 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| The SELECT Statement | 1, 7, 11, 20, 27, 29 | 6 |
| Column and Table Aliases | 2, 12, 21, 30, 37 | 5 |
| DISTINCT | 3, 10, 13, 19, 22, 31 | 6 |
| Expressions and Calculated Columns | 4, 8, 14, 23, 28, 32, 38 | 7 |
| Sorting Results | 5, 9, 15, 17, 24, 33, 35, 39 | 8 |
| Limiting Results | 6, 16, 18, 25, 26, 34, 36, 40 | 8 |

Questions 1–10 collectively cover all six Topic 3.2 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (1, 3, 10, 11, 15, 16, 24, 27, 29, 34)
- Intermediate: 29 questions
- Advanced: 1 question (40)
- Correct option A: 10 questions (1, 6, 9, 13, 17, 22, 28, 32, 36, 40)
- Correct option B: 10 questions (3, 5, 11, 15, 20, 24, 27, 31, 34, 37)
- Correct option C: 10 questions (4, 8, 12, 16, 19, 23, 26, 30, 35, 39)
- Correct option D: 10 questions (2, 7, 10, 14, 18, 21, 25, 29, 33, 38)
- Longest consecutive run of one correct letter: below 3 throughout
