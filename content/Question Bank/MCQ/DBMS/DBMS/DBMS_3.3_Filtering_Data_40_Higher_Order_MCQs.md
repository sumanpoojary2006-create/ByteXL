# DBMS 3.3: Filtering Data — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** SQL Essentials
- **Chapter:** Filtering Data
- **Scope:** All five Topic 3.3 subtopics in the attached course blueprint (The WHERE Clause; Comparison Operators; Logical Operators; Pattern Matching; Working with NULL)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Questions begin with a recognisable data task. Whenever an answer depends on stored values, the relevant table, field meanings, and sample rows are shown so the result can be verified.
- **Evidence rule:** Students must inspect data, trace predicates, complete or repair SQL, compare implementations, or choose a defect-revealing test—not recall isolated definitions.
- **Scope guard:** Only filtering concepts taught in Topic 3.3 are assessed; tables provide context rather than introducing untaught SQL.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all five Topic 3.3 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Count the northern flights

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The WHERE Clause  
**Is Curriculum Based:** No  
**Assessment type:** Filter tracing

A drone delivery service logs every completed flight, recording the zone it flew over and how long the flight took.

`drone_flights`

| flight_id | zone | duration_min |
|---|---|---|
| 1 | North | 22 |
| 2 | South | 15 |
| 3 | North | 31 |
| 4 | East | 18 |
| 5 | South | 26 |

```sql
SELECT flight_id FROM drone_flights WHERE zone = 'North';
```

How many flights logged in the North zone does this query return?

A. 5 — every stored flight is retained.  
B. 1 — processing stops after the first matching row.  
C. 3 — every flight outside the South zone is retained.  
D. 2 — flights 1 and 3 satisfy the zone condition.

### 2. Ten years, on the line

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Comparison Operators  
**Is Curriculum Based:** No  
**Assessment type:** Boundary tracing

A shipping line awards long-service medals to crew with ten **or more** years aboard.

`crew`

| name | years_service |
|---|---|
| Dsouza | 9 |
| Iyer | 10 |
| Fernandes | 12 |

```sql
SELECT name FROM crew WHERE years_service >= 10;
```

Which crew members qualify for the long-service medal?

A. Fernandes only, because the boundary value is excluded.  
B. Iyer and Fernandes, since `>=` includes the boundary.  
C. All three — nine rounds up.  
D. Dsouza only.

### 3. The AND that got there first

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Logical Operators  
**Is Curriculum Based:** No  
**Assessment type:** Precedence tracing

A food-festival app curates a shortlist of stalls for its city guide, tracking each stall's city and its customer rating.

`food_stalls`

| name | city | rating |
|---|---|---|
| Wok Box | Pune | 3.5 |
| Dosa Den | Surat | 4.5 |
| Chai Stop | Surat | 3.0 |
| Momo Hut | Pune | 4.8 |

```sql
SELECT name FROM food_stalls
WHERE city = 'Pune' OR city = 'Surat' AND rating > 4;
```

Which stalls make it into the app's shortlist?

A. Wok Box, Momo Hut, and Dosa Den — AND binds before OR here.  
B. Dosa Den and Momo Hut — the rating test applies to both cities.  
C. All four stalls.  
D. Momo Hut only.

### 4. Names that end the same way

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Pattern Matching  
**Is Curriculum Based:** No  
**Assessment type:** Pattern tracing

A bank's teller portal lets staff search account holders by partial name spelling.

`account_holders`

| holder |
|---|
| Wilson |
| Sonia |
| Jackson |
| Sonu |

```sql
SELECT holder FROM account_holders WHERE holder LIKE '%son';
```

Which account holders turn up in the teller's search?

A. Sonia and Sonu — matching is based on pronunciation rather than spelling.  
B. All four names.  
C. Wilson and Jackson — `%son` requires the name to end in "son".  
D. No names; LIKE needs exact text.

### 5. Awaiting inspection

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Working with NULL  
**Is Curriculum Based:** No  
**Assessment type:** NULL-test tracing

A public-works department tracks the last inspection date recorded for each bridge it maintains.

`bridges`

| bridge | inspected_on |
|---|---|
| River Arch | 2025-04-11 |
| Mill Span | NULL |
| High Gate | 2025-06-02 |
| Old Iron | NULL |

```sql
SELECT bridge FROM bridges WHERE inspected_on IS NULL;
```

Which bridges does the department's query flag as never inspected?

A. Mill Span and Old Iron, no inspection date on file.  
B. River Arch and High Gate.  
C. All four bridges.  
D. An error because a missing date cannot participate in a condition.

### 6. When nothing matches

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The WHERE Clause  
**Is Curriculum Based:** No  
**Assessment type:** Empty-result mechanics

A theatre's `bookings` table holds 300 rows, none for the date 2025-12-25. A clerk runs `SELECT * FROM bookings WHERE show_date = '2025-12-25';`.

What does the clerk's query return for that date?

A. A runtime error because the predicate has no true result.  
B. All 300 rows because WHERE is ignored when there is no match.  
C. One row containing NULL values as an empty-result placeholder.  
D. A valid result containing the columns but zero data rows.

### 7. Everything but the cancelled

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Comparison Operators  
**Is Curriculum Based:** No  
**Assessment type:** Not-equal tracing

A community center tracks the registration status of every enrichment workshop it runs.

`workshops`

| title | status |
|---|---|
| Pottery Basics | confirmed |
| Glass Blowing | cancelled |
| Wood Turning | confirmed |
| Silk Dyeing | cancelled |
| Leather Craft | waitlist |

```sql
SELECT title FROM workshops WHERE status <> 'cancelled';
```

How many workshops remain once the cancelled ones are excluded?

A. 2 — only the cancelled pair remains.  
B. 5 — the operator leaves every status unchanged.  
C. 3 — Pottery Basics, Wood Turning, and Leather Craft.  
D. 0 — a not-equal condition cannot retain text values.

### 8. NOT diesel

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Logical Operators  
**Is Curriculum Based:** No  
**Assessment type:** NOT tracing

A logistics company records the fuel type used by each van in its delivery fleet.

`delivery_vans`

| van | fuel |
|---|---|
| V-1 | diesel |
| V-2 | electric |
| V-3 | cng |
| V-4 | diesel |

```sql
SELECT van FROM delivery_vans WHERE NOT (fuel = 'diesel');
```

Which vans in the fleet run on something other than diesel?

A. V-1 and V-4 — NOT preserves rows satisfying the inner test.  
B. V-2 and V-3.  
C. All four vans.  
D. None; NOT cancels the whole query.

### 9. One character, no more

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Pattern Matching  
**Is Curriculum Based:** No  
**Assessment type:** Underscore-wildcard tracing

A warehouse labels every storage bin with a short alphanumeric code.

`bin_codes`

| code |
|---|
| A4 |
| B44 |
| C4 |
| D14 |

```sql
SELECT code FROM bin_codes WHERE code LIKE '_4';
```

Which bin codes match the search pattern?

A. All four codes, because the pattern searches for a 4 at any position.  
B. B44 and D14 — the longer codes.  
C. Only A4 — the first match wins.  
D. A4 and C4 — `_` stands for exactly one character before the 4.

### 10. The filter that found no one

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Working with NULL  
**Is Curriculum Based:** No  
**Assessment type:** Misconception correction

A clinic's `lab_reports` table has several rows whose `result_value` is NULL, yet `SELECT * FROM lab_reports WHERE result_value = NULL;` returns zero rows.

Why does this query fail to find the NULL results?

A. `= NULL` evaluates to unknown, not true.  
B. The NULLs were deleted by the query.  
C. The equals sign is misspelled.  
D. NULL rows require elevated access before they can be selected.

### 11. Which invoices clear the bar

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The WHERE Clause  
**Is Curriculum Based:** No  
**Assessment type:** Filter tracing

An accounts team reviews client invoices to flag the larger ones for follow-up.

`invoices`

| invoice_no | client | amount |
|---|---|---|
| N-1 | Crane Bros | 500 |
| N-2 | Marsh & Co | 1500 |
| N-3 | Delta Print | 2200 |

```sql
SELECT client FROM invoices WHERE amount > 1000;
```

Which clients have an invoice large enough to need follow-up?

A. Crane Bros only.  
B. All three clients.  
C. Marsh & Co and Delta Print, both exceeding 1000.  
D. Delta Print only, because filtering retains only the largest value.

### 12. Before the first of June

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Comparison Operators  
**Is Curriculum Based:** No  
**Assessment type:** Date-comparison tracing

A sailing club logs the date each boat registered for its upcoming regatta.

`regatta_entries`

| boat | registered_on |
|---|---|
| Kestrel | 2025-05-20 |
| Osprey | 2025-06-03 |
| Petrel | 2025-05-30 |

```sql
SELECT boat FROM regatta_entries WHERE registered_on < '2025-06-01';
```

Which boats registered before the regatta's cutoff date?

A. Osprey only.  
B. Kestrel and Petrel.  
C. All three boats.  
D. None, because `<` cannot be applied to date values.

### 13. Both conditions or nothing

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Logical Operators  
**Is Curriculum Based:** No  
**Assessment type:** AND tracing

A fitness chain tracks which amenities are available at each of its branches.

`gyms`

| branch | has_pool | open_24h |
|---|---|---|
| Lakeview | true | false |
| Central | true | true |
| Airport | false | true |

```sql
SELECT branch FROM gyms WHERE has_pool = true AND open_24h = true;
```

Which branch should the chain recommend to a member who wants both a pool and 24-hour access?

A. Lakeview and Central — each has a pool.  
B. All three — each satisfies something.  
C. Lakeview and Airport, each satisfying one of the two conditions.  
D. Central only — AND demands both conditions true on the same row.

### 14. Codes from the PX line

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Pattern Matching  
**Is Curriculum Based:** No  
**Assessment type:** Prefix-pattern tracing

A parts supplier assigns every part it stocks a product-line code.

`parts`

| part_code |
|---|
| PX-1 |
| PX-9 |
| QX-2 |

```sql
SELECT part_code FROM parts WHERE part_code LIKE 'PX-%';
```

Which parts belong to the PX product line?

A. PX-1 and PX-9 — the pattern anchors the start to "PX-".  
B. QX-2 only.  
C. All three codes.  
D. Nothing, because `%` must occur at the beginning of a pattern.

### 15. Zero is an answer, NULL is a shrug

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Working with NULL  
**Is Curriculum Based:** No  
**Assessment type:** Zero-versus-NULL discrimination

A club records the membership fee owed by each member; a fee of zero means the member is exempt, not unbilled.

`membership_fees`

| member | fee |
|---|---|
| Kavya | 0 |
| Dinesh | NULL |
| Sameer | 250 |

```sql
SELECT member FROM membership_fees WHERE fee IS NULL;
```

Whose fee status is unrecorded, and why don't the other two match?

A. Kavya and Dinesh, because zero and NULL are treated as the same value.  
B. Nobody; the column has values.  
C. Dinesh only — his fee is unrecorded; Kavya's is a real zero.  
D. Sameer only — the only real fee.

### 16. Either coast will do

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Logical Operators  
**Is Curriculum Based:** No  
**Assessment type:** OR tracing

A delivery firm assigns every courier to a coverage zone.

`couriers`

| courier | zone |
|---|---|
| Rina | East |
| Tanay | North |
| Bala | West |
| Sana | East |

```sql
SELECT courier FROM couriers WHERE zone = 'East' OR zone = 'West';
```

How many couriers cover the East or West zones?

A. 1 — OR requires both comparisons to be true on the same row.  
B. 3 — Rina, Bala, and Sana; OR admits either condition.  
C. 4 — each stored row needs to satisfy only one condition.  
D. 0 — a zone cannot equal two values.

### 17. Somewhere in the middle

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Pattern Matching  
**Is Curriculum Based:** No  
**Assessment type:** Contains-pattern tracing

A music school catalogs the instruments it has available for lessons.

`instruments`

| name |
|---|
| rebab |
| tabla |
| sitar |
| veena |

```sql
SELECT name FROM instruments WHERE name LIKE '%ab%';
```

Which instruments in the catalogue match the search pattern?

A. rebab and tabla — `%ab%` matches "ab" anywhere inside.  
B. tabla only, because the letters must be exactly in the centre.  
C. sitar and veena.  
D. All four names.

### 18. Two clauses, two different jobs

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The WHERE Clause  
**Is Curriculum Based:** No  
**Assessment type:** Clause-role discrimination

An observatory runs:

```sql
SELECT telescope_name FROM observations WHERE sky_clarity = 'excellent';
```

The table has 9 columns and 2,000 rows; 130 rows have excellent clarity.

Which description of the result matches what WHERE and SELECT each did here?

A. 130 rows and 9 columns; WHERE trimmed both dimensions.  
B. 2,000 rows and 1 column; WHERE picked the column.  
C. 130 rows and 9 columns; the SELECT list removed rows with other clarity values.  
D. 130 rows and 1 column — WHERE picks rows, SELECT picks columns.

### 19. No heavier than the limit

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Comparison Operators  
**Is Curriculum Based:** No  
**Assessment type:** Spec-to-operator mapping

A cable car's rule: baggage weighing **no more than** 500 hectograms rides free.

Which condition finds the free baggage, including a bag of exactly 500?

A. `weight_hg < 500`, excluding the boundary value.  
B. `weight_hg <= 500`, including the boundary.  
C. `weight_hg > 500`  
D. `weight_hg = 500`

### 20. Punctuate the policy

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Logical Operators  
**Is Curriculum Based:** No  
**Assessment type:** Parenthesization construction

A talent agency's shortlist policy: performers based in Mumbai **or** Goa, but in either case only those currently available.

Which WHERE clause enforces the policy?

A. `city = 'Mumbai' OR city = 'Goa' AND available = true`  
B. `city = 'Mumbai' AND city = 'Goa' AND available = true` — impossible condition.  
C. `(city = 'Mumbai' OR city = 'Goa') AND available = true`, grouped.  
D. `NOT (city = 'Mumbai' OR available = true)`

### 21. The second letter is "a"

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Pattern Matching  
**Is Curriculum Based:** No  
**Assessment type:** Pattern construction

A registry wants all breed names whose **second** character is `a` (as in "Labrador").

Which pattern finds breed names with "a" as the second letter?

A. `LIKE '_a%'`: one char, then `a`, then rest.  
B. `LIKE 'a%'` — starts with the letter a directly.  
C. `LIKE '%a'` — ends with a.  
D. `LIKE '%a%'` — contains a.

### 22. The proof of delivery

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Working with NULL  
**Is Curriculum Based:** No  
**Assessment type:** IS NOT NULL tracing

A logistics company tracks the delivery timestamp recorded for each consignment it ships.

`consignments`

| consignment | delivered_at |
|---|---|
| C-11 | 2025-07-01 10:20 |
| C-12 | NULL |
| C-13 | 2025-07-02 16:45 |
| C-14 | NULL |

```sql
SELECT consignment FROM consignments WHERE delivered_at IS NOT NULL;
```

Which consignments has the company already delivered?

A. C-12 and C-14 — the pending pair.  
B. All four consignments.  
C. Nothing, because timestamps cannot be checked for NULL.  
D. C-11 and C-13 — the rows where a delivery time exists.

### 23. The lowercase city that matched nothing

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The WHERE Clause  
**Is Curriculum Based:** No  
**Assessment type:** Case-sensitivity diagnosis

A relocation firm's table stores `city` values like `Pune` and `Nagpur`. The query `SELECT * FROM clients WHERE city = 'pune';` returns zero rows, though dozens of Pune clients exist.

What is the explanation?

A. The stored values were normalised to lowercase before comparison.  
B. Text equality is case-sensitive, so `Pune` and `pune` differ.  
C. WHERE cannot filter on city columns.  
D. The table needs re-sorting first.

### 24. The row that answers neither question

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Working with NULL  
**Is Curriculum Based:** No  
**Assessment type:** Unknown-result reasoning

A price-check tool runs two queries on a catalogue: `WHERE price < 100` and then `WHERE price >= 100`. A row whose `price` is NULL appears in **neither** result.

Why does the NULL-priced row appear in neither result?

A. The row was locked between queries.  
B. NULL prices are treated as zero by both comparisons.  
C. Both comparisons evaluate to unknown.  
D. The tool ran the queries in the wrong order.

### 25. The clause in the wrong seat

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The WHERE Clause  
**Is Curriculum Based:** No  
**Assessment type:** Smallest-repair selection

A box-office analyst's query fails with a syntax error:

```sql
SELECT film, tickets_sold FROM screenings
ORDER BY tickets_sold DESC
WHERE hall = 'IMAX';
```

What is the repair?

A. Delete `ORDER BY`; a filtered query cannot also be sorted.  
B. Change WHERE to WHICH.  
C. Wrap the whole query in parentheses.  
D. Move WHERE before ORDER BY.

### 26. Filtering on arithmetic

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Comparison Operators  
**Is Curriculum Based:** No  
**Assessment type:** Expression-filter tracing

A street-food festival records each stall's units sold and price per unit to rank the top earners.

`stall_sales`

| stall | qty | unit_price |
|---|---|---|
| Pickle Cart | 3 | 400 |
| Jam Stand | 2 | 450 |

```sql
SELECT stall FROM stall_sales WHERE qty * unit_price > 1000;
```

Which stalls cleared the festival's revenue threshold?

A. Both stalls.  
B. Pickle Cart only — 3 × 400 = 1200 clears the bar.  
C. Jam Stand only.  
D. Neither; arithmetic expressions cannot be used inside WHERE.

### 27. Everyone except the government domain

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Logical Operators  
**Is Curriculum Based:** No  
**Assessment type:** NOT-LIKE tracing

A newsletter platform stores the email address of every subscriber on its list.

`subscribers`

| email |
|---|
| riya@mail.com |
| desk@transport.gov.in |
| leo@quickpost.net |

```sql
SELECT email FROM subscribers WHERE email NOT LIKE '%.gov.in';
```

Which subscribers are not on a government email domain?

A. Only the .gov.in address.  
B. All three addresses.  
C. The two non-government addresses, via NOT LIKE inversion.  
D. Nothing, because NOT cannot be combined with a pattern predicate.

### 28. One wildcard is choosier than the other

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Pattern Matching  
**Is Curriculum Based:** No  
**Assessment type:** Wildcard discrimination

A depot's codes include `A9` and `A99`. Two patterns are tested: `LIKE 'A_'` and `LIKE 'A%'`.

Which statement is correct?

A. `'A_'` matches only `A9`; `'A%'` matches both codes.  
B. Both patterns match both codes.  
C. `'A_'` matches both codes; `'A%'` matches only `A99`.  
D. Neither pattern matches either code.

### 29. A display label without changing the stored data

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Working with NULL  
**Is Curriculum Based:** No  
**Assessment type:** Output prediction and misconception check

An applicant dashboard reads `interview_date` as the scheduled interview date. A NULL means no date is currently recorded.

`applications`

| candidate | interview_date |
|---|---|
| Mira | 2025-08-14 |
| Zubin | NULL |

```sql
SELECT candidate, COALESCE(interview_date::text, 'Not scheduled') AS interview
FROM applications;
```

Record the displayed value for Zubin and its effect on the stored row.

A. `2025-08-14`; COALESCE copies Mira's date into Zubin's row.  
B. `NULL`; COALESCE cannot provide text for a missing date.  
C. `Not scheduled`; evaluating COALESCE updates Zubin's stored value.  
D. `Not scheduled`; the stored NULL remains unchanged.

### 30. Swapped, but the same

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Logical Operators  
**Is Curriculum Based:** No  
**Assessment type:** Equivalence judgment

Two versions of a warehouse query:

```sql
WHERE aisle = 'A' AND weight_kg > 50
WHERE weight_kg > 50 AND aisle = 'A'
```

Are they equivalent?

A. No — the leftmost condition determines the result first.  
B. Yes — AND requires both conditions regardless of order.  
C. No — reversing the conditions also admits aisle B.  
D. Only on tables with fewer than 100 rows.

### 31. Exactly four characters

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Pattern Matching  
**Is Curriculum Based:** No  
**Assessment type:** Length-pattern construction

A gym issues a locker code to each member for the day.

`lockers`

| code |
|---|
| KL7 |
| MN42 |
| PQR85 |

A facilities app must select codes of exactly four characters.

Which pattern does it, and what matches here?

A. `LIKE '%%%%'` — four percents, matching any length really.  
B. `LIKE '____%'` — at least four.  
C. `LIKE '____'` — four underscores, exactly four characters.  
D. `LIKE '4'` — the digit four.

### 32. Two tests on every row

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The WHERE Clause  
**Is Curriculum Based:** No  
**Assessment type:** Combined-filter tracing

A mandi (grain market) operator records the market and traded amount for each grain lot passing through it.

`grain_lots`

| lot | mandi | amount |
|---|---|---|
| L1 | Indore | 700 |
| L2 | Indore | 400 |
| L3 | Ujjain | 900 |
| L4 | Indore | 520 |

```sql
SELECT lot FROM grain_lots WHERE mandi = 'Indore' AND amount > 500;
```

Which grain lots pass both the market and amount checks?

A. L1 and L4 — the Indore lots above 500 in amount.  
B. L1, L2, and L4 — all of Indore.  
C. L1 and L3, because the two largest amounts pass independently.  
D. All four lots.

### 33. The kilogram that shouldn't pay

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Comparison Operators  
**Is Curriculum Based:** No  
**Assessment type:** Defect-exposing input selection

A freight rule says parcels **heavier than** 20 kg pay a surcharge. The implemented filter is `WHERE weight_kg >= 20`.

Which test parcel exposes the bug?

A. A 25 kg parcel, which both conditions surcharge.  
B. A 5 kg parcel, which both conditions exempt.  
C. A 19.99 kg parcel — just under.  
D. A parcel of exactly 20 kg.

### 34. The test row that catches the OR

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Logical Operators  
**Is Curriculum Based:** No  
**Assessment type:** Defect-exposing input selection

Policy: refunds go only to orders that are both `damaged = true` **and** `reported_within_7d = true`. A developer mistakenly wrote `WHERE damaged = true OR reported_within_7d = true`.

Which test order exposes the mistake?

A. An order with both flags true.  
B. An order with both flags false.  
C. A damaged order reported late.  
D. An order with no flags recorded.

### 35. Preserve a case-insensitive search

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Pattern Matching  
**Is Curriculum Based:** No  
**Assessment type:** Smallest-repair selection

A support directory stores the agent name exactly as entered.

`agents`

| agent_name |
|---|
| Anika Rao |
| ANIKA SEN |
| anita shah |
| Rohan Das |

A user types `anika`, and the application must find names that begin with those letters regardless of case. The current PostgreSQL filter is:

```sql
WHERE agent_name LIKE 'anika%'
```

Choose the smallest correction that returns both Anika rows without admitting Anita.

A. `WHERE agent_name LIKE '%anika%'`  
B. `WHERE agent_name ILIKE 'anika%'`  
C. `WHERE agent_name = 'anika%'`  
D. `WHERE agent_name ILIKE 'ani%'`

### 36. The rows that fell out of both buckets

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Working with NULL  
**Is Curriculum Based:** No  
**Assessment type:** NULL-aware repair

A store's report splits products into "discounted" (`discount_pct > 0`) and "not discounted" (`discount_pct <= 0`). Products whose `discount_pct` is NULL appear in neither bucket, and the two reports no longer add up to the catalogue.

Which repair puts the NULL products into the "not discounted" bucket?

A. `WHERE discount_pct <= 0 OR discount_pct IS NULL`  
B. Change the first filter to `> NULL`.  
C. Sort by discount before filtering.  
D. Change the second filter to `WHERE NOT (discount_pct > 0)`.

### 37. NULL meets NULL

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Working with NULL  
**Is Curriculum Based:** No  
**Assessment type:** NULL-comparison prediction

In a reconciliation check, both `ledger_ref` and `bank_ref` are NULL on one row. An auditor expects `WHERE ledger_ref = bank_ref` to match it, "since both are equally empty."

What actually happens?

A. The row matches; NULL equals NULL.  
B. The query errors on the double NULL.  
C. The row matches only when both columns were declared nullable.  
D. The row does not match; `NULL = NULL` is unknown, not true.

### 38. Check whether a rewrite changes the selected rows

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Comparison Operators  
**Is Curriculum Based:** No  
**Assessment type:** Implementation-equivalence tracing

In a quality-control table, `score` is the measured inspection score; NULL means the inspection has not been completed.

`inspections`

| batch | score |
|---|---:|
| B1 | 92 |
| B2 | 80 |
| B3 | 61 |
| B4 | NULL |

Two developers propose these filters for batches scoring above 80:

```sql
-- Version 1
WHERE score > 80

-- Version 2
WHERE NOT (score <= 80)
```

Decide whether the versions are equivalent for the shown data, including B4.

A. No; Version 2 also returns B2 because 80 satisfies `<=`.  
B. No; Version 2 returns B4 because NOT turns NULL into true.  
C. Yes; both return only B1.  
D. Yes; both return B1 and B4 because NULL has no numeric value.

### 39. Filter, then rank, then cut

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The WHERE Clause  
**Is Curriculum Based:** No  
**Assessment type:** Combined-clause tracing

A real-estate listing site tracks the monthly rent for each apartment unit available.

`apartments`

| unit | rent |
|---|---|
| 2A | 12000 |
| 3C | 18000 |
| 4B | 15000 |
| 1D | 9000 |

```sql
SELECT unit FROM apartments
WHERE rent < 16000
ORDER BY rent DESC
LIMIT 2;
```

Which two apartments does the listing show, and in what order?

A. 3C, 4B — the two highest rents before filtering.  
B. 4B, 2A.  
C. 1D, 2A — cheapest first.  
D. 2A, 3C — table order.

### 40. Write the fee window

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Comparison Operators  
**Is Curriculum Based:** No  
**Assessment type:** Spec-to-clause construction

A co-working directory must list plans whose monthly fee is **at least 250 and at most 400**, both ends included.

Which WHERE clause is correct?

A. `WHERE fee >= 250 AND fee <= 400` — inclusive on both boundary fees.  
B. `WHERE fee > 250 AND fee < 400` — the boundaries fall out.  
C. `WHERE fee >= 250 OR fee <= 400` — every fee satisfies one side here.  
D. `WHERE fee = 250 AND fee = 400` — no fee equals both.

---

## Instructor Key

### 1. D

WHERE tests each of the five rows; flights 1 and 3 carry 'North' and survive. The clause is a per-row gate, not a first-match search (B).

### 2. B

"Ten or more" includes ten, and `>=` is the operator that honours the boundary. Iyer at exactly 10 is the row that distinguishes `>=` from `>`.

### 3. A

Without parentheses AND evaluates first, so the predicate is "Pune, or (Surat and above 4)": both Pune stalls regardless of rating, plus Dosa Den. Momo Hut alone (D) would require the parenthesized reading the query doesn't have.

### 4. C

`%son` anchors "son" to the end and lets `%` absorb any prefix: Wil-son, Jack-son. Sonia and Sonu contain the letters but don't end with them (A).

### 5. A

IS NULL is the dedicated test for absent values: the two uninspected bridges match. Their blankness is exactly what the operator exists to find.

### 6. D

A filter matching nothing is a valid, empty answer — zero rows, no error, no fallback. The empty set is information: no bookings exist for that date.

### 7. C

`<>` keeps every status other than 'cancelled' — including 'waitlist', which is the row that tests whether the reader treats `<>` as "the opposite value" (A) or correctly as "anything but."

### 8. B

NOT inverts the parenthesized test: diesel rows fail, everything else passes. Electric and CNG are the survivors.

### 9. D

`_` is the one-character wildcard: the pattern describes exactly two characters ending in 4. B44 and D14 have three characters — one too many for the single underscore to absorb.

### 10. A

NULL is not a value to equal — any `=` against it returns unknown, which WHERE treats as failure. `IS NULL` exists precisely because equality cannot ask this question.

### 11. C

Each row's amount is tested against 1000: 1500 and 2200 pass, 500 fails. Two clients emerge — WHERE keeps all passers, not just the largest (D).

### 12. B

Dates compare chronologically: 20 May and 30 May are "less than" 1 June. Osprey's 3 June is not.

### 13. D

AND is a conjunction on one row: pool *and* round-the-clock. Central alone has both flags true; Lakeview and Airport each carry one true and one false.

### 14. A

The literal prefix pins the start; `%` absorbs whatever follows. QX-2 fails on its first character — patterns are anchored unless a wildcard says otherwise.

### 15. C

The distinction the row-pair teaches: 0 is a known value (Kavya's fee is *zero*), NULL is no value at all (Dinesh's fee is *unknown*). IS NULL finds the unknown, not the zero.

### 16. B

OR admits a row when either side holds: two East couriers and one West. Tanay's North satisfies neither.

### 17. A

`%ab%` frees both ends: r-eb-ab (ends with it), t-ab-la (middle). The pattern asks only that "ab" occur somewhere.

### 18. D

Two independent dimensions: WHERE selected the 130 excellent-clarity rows; the SELECT list narrowed the display to one column. Confusing which clause trims which dimension is the classic early error.

### 19. B

"No more than" is inclusive language, and only `<=` includes the 500 boundary. Option A silently charges the exactly-500 bag.

### 20. C

The policy applies availability to *both* cities, which requires grouping the OR before the AND touches it. Ungrouped (A), precedence hands availability to Goa alone — Mumbai's unavailable performers leak through.

### 21. A

Position is encoded by wildcard order: `_` consumes exactly the first character, the literal `a` then sits second, `%` takes the rest.

### 22. D

IS NOT NULL keeps rows where the timestamp exists: the two delivered consignments. The NULLs — still on the road — are excluded.

### 23. B

'pune' and 'Pune' are different strings, and text equality compares exactly. The filter is correct machinery aimed at a value that never occurs.

### 24. C

NULL escapes both `<` and `>=` because each comparison evaluates to unknown. A row can fail two complementary filters only by answering neither — which is NULL's defining behaviour.

### 25. D

Clause order is fixed grammar: WHERE follows FROM and precedes ORDER BY. The repair is relocation, not deletion (A) — both clauses are wanted, in their seats.

### 26. B

WHERE evaluates the expression per row: 1200 passes, 900 fails. Filters are not restricted to raw columns — computed conditions are tested the same way.

### 27. C

NOT LIKE excludes the pattern's matches: the government address drops, the other two stay. It is the pattern test with its verdict flipped.

### 28. A

The wildcards differ in appetite: `_` eats exactly one character, `%` any number. `A9` satisfies both patterns; `A99` overflows the underscore and only `%` swallows it.

### 29. D

COALESCE returns its first non-NULL argument, so Zubin is displayed as `Not scheduled`. Because this is a SELECT expression rather than an UPDATE, the stored `interview_date` remains NULL.

### 30. B

AND is symmetric: both conditions must hold, and "both" has no order. The rewritten clause admits exactly the same rows — condition order is a style choice, not a semantic one.

### 31. C

Each `_` demands one character, so four of them demand exactly four: MN42 fits, KL7 is short, PQR85 is long. Option B's trailing `%` turns "exactly" into "at least."

### 32. A

Each row faces both tests: L1 (Indore, 700) and L4 (Indore, 520) pass both; L2 fails on amount, L3 on mandi. AND's verdict is per-row, both-or-nothing.

### 33. D

The bug lives only on the boundary: above 20 both versions charge, below 20 both don't. Exactly 20 kg is the single input where `>` and `>=` disagree — which is why boundary values are the test cases that matter.

### 34. C

Rows satisfying both or neither condition cannot tell AND from OR — the two agree there. Only the one-condition row (damaged, late) splits them: AND denies, OR refunds. Test design is choosing the row where the versions disagree.

### 35. B

PostgreSQL `ILIKE` performs the required case-insensitive pattern match, while `anika%` preserves the exact prefix. Option D broadens the prefix to `ani` and would also admit Anita.

### 36. A

NULL rows fail every ordinary comparison, so a bucket meant to catch them must name them: the added `IS NULL` arm routes the unknowns into "not discounted" explicitly, and the two reports sum to the catalogue again.

### 37. D

Equality compares values, and NULL supplies none — `NULL = NULL` is unknown, not true. Two missing references are two unanswered questions, and the database refuses to declare unanswered questions equal.

### 38. C

For 92, the inner `<= 80` is false and NOT makes it true; 80 and 61 fail both versions. For NULL, both predicates evaluate to unknown, so WHERE excludes B4 in either version.

### 39. B

The pipeline runs filter → sort → cut: WHERE removes 3C (18000), the survivors sort 15000, 12000, 9000, and LIMIT keeps the first two — 4B then 2A. Option A forgets the filter ran first.

### 40. A

An inclusive window is two inclusive comparisons joined by AND. Strict operators (B) exclude the boundary fees; OR (C) admits every non-NULL numeric fee because any number satisfies at least one side.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Filter and predicate tracing over shown data | 1, 2, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 26, 27, 32, 38, 39 |
| Construction and spec-to-clause mapping | 19, 20, 21, 31, 40 |
| Defect-exposing input selection | 33, 34 |
| Misconception correction and diagnosis | 3, 10, 23, 24, 25, 28, 30, 37, 38 |
| Mechanics and repair | 6, 18, 36 |
| Display fallback and case-insensitive search repair | 29, 35 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| The WHERE Clause | 1, 6, 11, 18, 23, 25, 32, 39 | 8 |
| Comparison Operators | 2, 7, 12, 19, 26, 33, 38, 40 | 8 |
| Logical Operators | 3, 8, 13, 16, 20, 27, 30, 34 | 8 |
| Pattern Matching | 4, 9, 14, 17, 21, 28, 31, 35 | 8 |
| Working with NULL | 5, 10, 15, 22, 24, 29, 36, 37 | 8 |

Questions 1–10 collectively cover all five Topic 3.3 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 8 questions (1, 10, 12, 14, 16, 21, 22, 24)
- Intermediate: 29 questions
- Advanced: 3 questions (3, 20, 34)
- Correct option A: 10 questions (3, 5, 10, 14, 17, 21, 28, 32, 36, 40)
- Correct option B: 10 questions (2, 8, 12, 16, 19, 23, 26, 30, 35, 39)
- Correct option C: 10 questions (4, 7, 11, 15, 20, 24, 27, 31, 34, 38)
- Correct option D: 10 questions (1, 6, 9, 13, 18, 22, 25, 29, 33, 37)
- Longest consecutive run of one correct letter: below 3 throughout
