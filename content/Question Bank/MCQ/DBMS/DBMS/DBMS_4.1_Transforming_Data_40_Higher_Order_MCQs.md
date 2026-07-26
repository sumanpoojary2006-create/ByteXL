# DBMS 4.1: Transforming Data — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** SQL for Data Retrieval and Analytics
- **Chapter:** Transforming Data
- **Scope:** All five Topic 4.1 subtopics in the attached course blueprint (String Functions; Numeric Functions; Date and Time Functions; NULL-Handling Functions; Conditional Logic)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every item begins with a recognisable reporting or cleanup task. Whenever an answer depends on stored values, the relevant field meaning and source rows are visible.
- **Evidence rule:** Students must trace a transformation, complete or repair an expression, compare implementations, expose a boundary defect, or diagnose branch order—not recall an isolated function definition.
- **Scope guard:** Only functions and conditional-logic behaviour taught in Topic 4.1 are assessed; source tables provide context without introducing later analytics topics.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all five Topic 4.1 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Clean it, then shout it

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** String Functions  
**Is Curriculum Based:** No  
**Assessment type:** Nested-function tracing

A travel-booking form saved the destination as `'  goa  '` — stray spaces on both sides, lowercase throughout.

```sql
SELECT UPPER(TRIM('  goa  '));
```

Trace the nested calls and record the final text.

A. `'  GOA  '` — UPPER changes case before TRIM can see the value.  
B. `'GOA'` — TRIM strips whitespace, then UPPER capitalizes.  
C. `'goa'` — the functions cancel out.  
D. An error; functions cannot nest.

### 2. Two decimal places, properly

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Numeric Functions  
**Is Curriculum Based:** No  
**Assessment type:** Rounding tracing

A currency-conversion service computes a fee of `47.6789`.

```sql
SELECT ROUND(47.6789, 2);
```

Round the fee exactly as PostgreSQL will.

A. 47.67 — the extra digits are cut off.  
B. 48, because ROUND ignores the requested decimal precision.  
C. 47.7 — one decimal place.  
D. 47.68.

### 3. Just the year, please

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Date and Time Functions  
**Is Curriculum Based:** No  
**Assessment type:** EXTRACT tracing

A vintage-car registry stores:

`cars`

| car_id | model | first_registered |
|---:|---|---|
| 17 | Premier Padmini | 2024-11-05 |

```sql
SELECT EXTRACT(YEAR FROM first_registered) FROM cars;
```

Record the extracted field for car 17.

A. `'2024-11-05'`, the complete stored date.  
B. 11 — the month.  
C. 2024.  
D. 5 — the day.

### 4. The nickname that wasn't there

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** NULL-Handling Functions  
**Is Curriculum Based:** No  
**Assessment type:** COALESCE tracing

A podcast production logs each host's legal name and their on-air name, if one was chosen.

`podcast_hosts`

| full_name | on_air_name |
|---|---|
| Devika Iyer | Dev |
| Arjun Bhatt | NULL |

```sql
SELECT COALESCE(on_air_name, full_name) AS display FROM podcast_hosts;
```

Resolve the fallback for Arjun's display name.

A. `Arjun Bhatt`, since his on-air name is NULL here.  
B. NULL — COALESCE passes it along.  
C. `Dev`, because COALESCE searches earlier result rows for a value.  
D. An empty string.

### 5. The branch that got there first

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Conditional Logic  
**Is Curriculum Based:** No  
**Assessment type:** CASE-order tracing

A gem-grading table contains:

`gems`

| gem_id | clarity_score |
|---:|---:|
| 51 | 85 |

```sql
SELECT CASE
    WHEN clarity_score >= 60 THEN 'Standard'
    WHEN clarity_score >= 80 THEN 'Premium'
    ELSE 'Reject'
END AS grade
FROM gems;
```

Trace the conditions in execution order and assign the label.

A. 'Premium', because the most restrictive true condition takes priority.  
B. 'Reject' — 85 matches no branch.  
C. Both labels at once.  
D. 'Standard' — CASE takes the first true branch it finds.

### 6. The first two letters of the plate

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** String Functions  
**Is Curriculum Based:** No  
**Assessment type:** SUBSTRING tracing

A parking system reads the state code off plate `'MH12AB3344'`.

```sql
SELECT SUBSTRING('MH12AB3344' FROM 1 FOR 2);
```

Extract the requested state-code characters.

A. `'12'` — the first digits.  
B. `'MH'`, two characters starting at position 1.  
C. `'MH12'` — FROM and FOR add up.  
D. `'44'` — a negative-direction substring takes the final characters.

### 7. Boxes don't come in fractions

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Numeric Functions  
**Is Curriculum Based:** No  
**Assessment type:** CEIL application

A candle workshop needs 7.2 shipping cartons' worth of stock packed. Partial cartons must become whole ones.

```sql
SELECT CEIL(7.2);
```

Translate the fractional capacity into the required carton count.

A. 8 — CEIL always rounds up, needing a whole carton.  
B. 7 — the fraction is dropped.  
C. 7.5 — CEIL rounds to halves.  
D. 72 — CEIL removes the decimal separator without changing digits.

### 8. A week after the demo

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Date and Time Functions  
**Is Curriculum Based:** No  
**Assessment type:** Date-arithmetic tracing

A software vendor records a demo at 10:00 on 1 March and schedules its follow-up exactly seven days later.

```sql
SELECT TIMESTAMP '2025-03-01 10:00:00' + INTERVAL '7 days';
```

Calculate the scheduled follow-up timestamp.

A. `2025-03-01 10:00:00`, because adding an interval does not alter timestamps.  
B. `2025-10-01 10:00:00` — the interval value is interpreted as months.  
C. `2025-03-08 10:00:00` — the timestamp moves forward by seven days.  
D. An error.

### 9. Turning the placeholder into a proper blank

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** NULL-Handling Functions  
**Is Curriculum Based:** No  
**Assessment type:** NULLIF tracing

A legacy import produced:

`leads`

| lead_id | branch |
|---:|---|
| 71 | UNKNOWN |
| 72 | Pune |

```sql
SELECT NULLIF(branch, 'UNKNOWN') FROM leads;
```

Record the transformed branch value for lead 71.

A. `'UNKNOWN'`, because NULLIF preserves equal arguments.  
B. NULL.  
C. An error.  
D. The word `'BRANCH'`.

### 10. What CASE actually is

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Conditional Logic  
**Is Curriculum Based:** No  
**Assessment type:** Concept identification

A logistics report adds a `speed_band` column using CASE WHEN.

Classify CASE according to the role it plays in the query.

A. A write command that stores each calculated category in the table.  
B. A loop that repeats a query per category.  
C. A table-creation command.  
D. A per-row conditional expression.

### 11. Assemble the greeting

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** String Functions  
**Is Curriculum Based:** No  
**Assessment type:** Concatenation tracing

A wedding venue prints a personalized welcome badge for each guest at check-in.

`guests`

| first_name | last_name |
|---|---|
| Rhea | Menon |

```sql
SELECT first_name || ' ' || last_name AS full FROM guests;
```

Assemble the calculated `full` value.

A. `Rhea Menon`, joined with the literal space between them.  
B. `RheaMenon` — no space is possible.  
C. `first_name last_name` — literally the column names themselves.  
D. `Menon Rhea` — last name first.

### 12. Seven degrees off, either way

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Numeric Functions  
**Is Curriculum Based:** No  
**Assessment type:** ABS tracing

A greenhouse controller computes deviation from the 22° target; tonight's reading gives `22 - 29 = -7`.

```sql
SELECT ABS(22 - 29);
```

Calculate the magnitude used by the controller.

A. -7 — ABS preserves the sign.  
B. 0, because ABS replaces every negative input with zero.  
C. 7.  
D. 49 — ABS squares.

### 13. What "today" returns

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Date and Time Functions  
**Is Curriculum Based:** No  
**Assessment type:** Function discrimination

A gym's sign-in sheet stamps each entry with `CURRENT_DATE`.

Choose the value shape supplied by CURRENT_DATE.

A. The date the database was installed.  
B. Today's calendar date without a time component.  
C. The current date *and* the current time to the second.  
D. A random recent date.

### 14. Three phones, none answered

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** NULL-Handling Functions  
**Is Curriculum Based:** No  
**Assessment type:** Multi-argument COALESCE tracing

A procurement system stores each supplier's mobile and landline numbers.

`suppliers`

| supplier | mobile | landline |
|---|---|---|
| Kanti Traders | NULL | NULL |

```sql
SELECT COALESCE(mobile, landline, 'no contact on file') FROM suppliers;
```

Follow the fallback chain to its displayed result.

A. NULL — two NULLs beat one string.  
B. An error because COALESCE accepts exactly two arguments.  
C. An empty string.  
D. `no contact on file`, COALESCE's literal fallback reached.

### 15. The size that sets the price

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Conditional Logic  
**Is Curriculum Based:** No  
**Assessment type:** Simple-CASE tracing

A T-shirt printer receives:

`print_orders`

| order_id | size |
|---:|---|
| 301 | M |

It prices the row using:

```sql
SELECT CASE size
    WHEN 'S' THEN 199
    WHEN 'M' THEN 229
    WHEN 'L' THEN 259
    ELSE 289
END AS price
FROM print_orders;
```

Trace order 301 through the simple CASE.

A. 229.  
B. 199 — the first branch always wins.  
C. 289 — ELSE applies to listed sizes too.  
D. 259, because CASE continues to the final matching size.

### 16. Three spellings, one city

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** String Functions  
**Is Curriculum Based:** No  
**Assessment type:** Case-normalization application

A survey table's `city` column holds `'Goa'`, `'GOA'`, and `'goa'` across rows, splitting one city's responses three ways in reports.

Select the smallest transformation that normalises all three spellings.

A. `TRIM(city)` — whitespace is the issue.  
B. `SUBSTRING(city FROM 1 FOR 1)` — reducing every city to its initial.  
C. `LOWER(city)`, normalizing every spelling to be identical.  
D. `city || 'goa'`.

### 17. The crates that didn't fill a stack

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Numeric Functions  
**Is Curriculum Based:** No  
**Assessment type:** MOD tracing

A depot records:

`arrivals`

| delivery_id | crates | crates_per_pallet |
|---:|---:|---:|
| 81 | 17 | 5 |

```sql
SELECT MOD(17, 5);
```

Interpret the returned number in pallet terms.

A. 3.4 — pallets needed.  
B. 3 — full pallets.  
C. 5 — the divisor is returned instead of the remainder.  
D. 2 — the remainder, two crates left over here.

### 18. Which warranties have lapsed?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Date and Time Functions  
**Is Curriculum Based:** No  
**Assessment type:** Date-comparison tracing

A home-appliance retailer tracks the warranty end date for each unit it has sold. For this test run, the database server's `CURRENT_DATE` is 2025-07-24.

`appliances`

| appliance | warranty_end |
|---|---|
| Dishwasher | 2025-06-30 |
| Geyser | 2026-01-15 |
| Chimney | 2025-07-23 |

```sql
SELECT appliance FROM appliances WHERE warranty_end < CURRENT_DATE;
```

Trace the date predicate and list the selected appliances.

A. Geyser only.  
B. Dishwasher and Chimney — both end dates fall before today.  
C. All three.  
D. Chimney only, because only the nearest past date is retained.

### 19. Discount unknown, price intact

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** NULL-Handling Functions  
**Is Curriculum Based:** No  
**Assessment type:** COALESCE-in-arithmetic tracing

A boutique tracks each sari's price and any discount applied.

`saris`

| item | price | discount |
|---|---|---|
| Kanjivaram | 500 | NULL |

```sql
SELECT price - COALESCE(discount, 0) AS payable FROM saris;
```

Compare the payable value with and without the fallback.

A. 500 — COALESCE turned the NULL discount into 0 first.  
B. NULL either way.  
C. 0 — the discount wins.  
D. 500 either way because arithmetic treats a missing numeric value as zero.

### 20. What TRIM does and doesn't touch

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** String Functions  
**Is Curriculum Based:** No  
**Assessment type:** Behaviour discrimination

An address import contains:

| address_id | raw_city |
|---:|---|
| 9 | `  New  Delhi ` |

Preserve or remove each space according to TRIM's actual scope.

A. `'NewDelhi'` — all spaces removed.  
B. `'  New  Delhi '` — TRIM measures whitespace without removing it.  
C. `'New  Delhi'` — TRIM strips the ends only, not the interior.  
D. `'New Delhi'` — interior spaces collapse to one.

### 21. Round or floor: one rupee apart

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Numeric Functions  
**Is Curriculum Based:** No  
**Assessment type:** Function discrimination

A toll table contains:

| journey_id | raw_toll |
|---:|---:|
| 501 | 9.99 |

The report evaluates `ROUND(raw_toll)` and `FLOOR(raw_toll)`.

Compare the two function results for journey 501.

A. Both return 10.  
B. ROUND returns 10; FLOOR returns 9.  
C. Both return 9.  
D. ROUND gives 9, while FLOOR gives 10.

### 22. June renewals only

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Date and Time Functions  
**Is Curriculum Based:** No  
**Assessment type:** EXTRACT-filter tracing

A gym tracks the renewal date for each member's membership.

`memberships`

| member | renews_on |
|---|---|
| Farhan | 2025-06-11 |
| Leela | 2025-07-02 |
| Omar | 2024-06-30 |

```sql
SELECT member FROM memberships WHERE EXTRACT(MONTH FROM renews_on) = 6;
```

Identify every member admitted by this month-only condition.

A. Farhan only, because EXTRACT(MONTH) also restricts the current year.  
B. Leela only.  
C. All three members.  
D. Farhan and Omar.  

### 23. Blank is not an answer

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** NULL-Handling Functions  
**Is Curriculum Based:** No  
**Assessment type:** Combined NULLIF-COALESCE tracing

A signup form sometimes submits an empty string instead of NULL.

`signups`

| signup_id | city |
|---:|---|
| 41 | `''` |
| 42 | Jaipur |

The display query is:

```sql
SELECT COALESCE(NULLIF(city, ''), 'Not provided') FROM signups;
```

Trace signup 41 through the nested functions.

A. NULLIF turns the empty string to NULL; COALESCE fills the fallback.  
B. The empty string prints as a blank cell.  
C. An error; the functions conflict.  
D. 'Not provided' appears only when the stored value was originally NULL.

### 24. The fragile fee gets the careful multiplier

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Conditional Logic  
**Is Curriculum Based:** No  
**Assessment type:** CASE-with-calculation tracing

A courier service tracks the base fee for each shipment and whether it's marked fragile.

`shipments`

| item | base_fee | fragile |
|---|---|---|
| Mirror | 400 | true |
| Blanket | 300 | false |

```sql
SELECT item,
       CASE WHEN fragile THEN base_fee * 1.5 ELSE base_fee END AS final_fee
FROM shipments;
```

Calculate both final fees.

A. Mirror 400, Blanket 300, because THEN cannot contain arithmetic.  
B. 600 and 450 — both marked up.  
C. Mirror 600, Blanket 300 — the fragile branch computes 400 × 1.5.  
D. Mirror 400, Blanket 450.

### 25. Stitch the ticket code

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** String Functions  
**Is Curriculum Based:** No  
**Assessment type:** Concatenation construction

A box-office system must produce codes like `TX-2025` from `prefix = 'TX'` and `season = '2025'`.

Complete the ticket-code expression.

A. `prefix - season`  
B. `prefix || '-' || season`, joined around a hyphen.  
C. `prefix AND season`  
D. `'prefix' || 'season'` — producing the literal text `prefixseason`.

### 26. The moment versus the day

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Date and Time Functions  
**Is Curriculum Based:** No  
**Assessment type:** Function discrimination

A courier app logs pickup events and needs the exact clock time, not just the day.

Select the function that preserves the full pickup moment.

A. CURRENT_DATE — dates include time invisibly.  
B. EXTRACT(DAY ...) — the day number preserves the timestamp internally.  
C. Either works identically.  
D. NOW() — it returns the current date and time, the full moment.

### 27. The sum that came back empty

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** NULL-Handling Functions  
**Is Curriculum Based:** No  
**Assessment type:** NULL-poisoning repair

A contractor's quotation tool breaks down each job's cost by category. The quotation table contains:

| quote_id | material_cost | labour_cost | transport_cost |
|---:|---:|---:|---:|
| 8 | 1200 | 500 | NULL |

The tool computes `material_cost + labour_cost + transport_cost`, and this quote displays a blank total.

Choose the expression-level repair that keeps known costs usable.

A. Apply `COALESCE(x, 0)` to each nullable cost.  
B. Add the same three columns in a different order.  
C. Multiply instead of add.  
D. Delete quotes with missing parts.

### 28. The branch no row can reach

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Conditional Logic  
**Is Curriculum Based:** No  
**Assessment type:** Unreachable-branch diagnosis

A donation platform contains:

| donor | amount |
|---|---:|
| Amrita | 8000 |

It labels the row using:

```sql
CASE
    WHEN amount > 100 THEN 'Supporter'
    WHEN amount > 5000 THEN 'Patron'
    ELSE 'Friend'
END
```

Diagnose why the 8,000 donation is labelled `Supporter`.

A. 8,000 fails the Patron comparison because the value is formatted with a comma.  
B. The ELSE intercepts large gifts.  
C. The 'Patron' branch is unreachable; the wider condition fires first.  
D. CASE cannot compare against 5000.

### 29. Middle of the invoice code

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** String Functions  
**Is Curriculum Based:** No  
**Assessment type:** SUBSTRING positioning

An invoice table contains:

| invoice_id | invoice_code |
|---:|---|
| 881 | INV24-881 |

Characters 4 and 5 carry the year.

```sql
SELECT SUBSTRING('INV24-881' FROM 4 FOR 2);
```

Extract the year fragment from invoice 881.

A. `'INV2'` — four characters beginning at position one.  
B. `'4-'` — position counts from zero.  
C. `'881'` — the tail.  
D. `'24'`.  

### 30. Points don't round up

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Numeric Functions  
**Is Curriculum Based:** No  
**Assessment type:** FLOOR application

A fuel-station record contains:

| fill_id | amount | raw_points |
|---:|---:|---:|
| 62 | 4590 | 45.9 |

The scheme grants one point per complete 100 rupees.

```sql
SELECT FLOOR(45.9);
```

Convert the raw points into the earned whole-point value.

A. 46 — nearest whole number.  
B. 45.  
C. 45.9, because FLOOR changes only negative numbers.  
D. 50 — FLOOR rounds to tens.

### 31. Days between two stamps

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Date and Time Functions  
**Is Curriculum Based:** No  
**Assessment type:** Date-difference tracing

A repair shop records:

| job_id | received_on | returned_on |
|---:|---|---|
| B-18 | 2025-07-10 | 2025-07-24 |

```sql
SELECT DATE '2025-07-24' - DATE '2025-07-10';
```

Calculate the elapsed whole days.

A. 14.  
B. 2 — only the month positions are subtracted.  
C. `'2025-07-14'` — a new date.  
D. An error; dates cannot be subtracted.

### 32. Dividing by a day with no rides

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** NULL-Handling Functions  
**Is Curriculum Based:** No  
**Assessment type:** NULLIF-guard application

A scooter-share table contains:

| service_date | total_revenue | ride_count |
|---|---:|---:|
| 2025-07-20 | 0 | 0 |

The report computes revenue per ride and crashes on this row.

```sql
SELECT total_revenue / NULLIF(ride_count, 0) FROM daily_stats;
```

Trace the zero-ride row through NULLIF and division.

A. It still crashes.  
B. It returns 0 because NULLIF replaces zero with another numeric zero.  
C. It returns NULL for that day, via NULLIF converting first.  
D. It skips the day's row entirely.

### 33. When no branch matches and nothing else is said

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Conditional Logic  
**Is Curriculum Based:** No  
**Assessment type:** Missing-ELSE prediction

A weather station contains:

| observed_at | wind_kmh |
|---|---:|
| 08:00 | 10 |

It bands the row using:

```sql
CASE
    WHEN wind_kmh >= 90 THEN 'Storm'
    WHEN wind_kmh >= 50 THEN 'Gale'
END
```

With no ELSE present, determine the value assigned to the calm row.

A. 'Gale', because CASE selects the closest available threshold.  
B. 0.  
C. An error.  
D. NULL, since no branch matches and there's no ELSE here.

### 34. Buses for the fan club

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Numeric Functions  
**Is Curriculum Based:** No  
**Assessment type:** CEIL application in context

A fan club plans:

| travellers | seats_per_bus |
|---:|---:|
| 130 | 40 |

```sql
SELECT CEIL(130 / 40.0);
```

Convert the capacity calculation into a bus count.

A. 3 — only completely filled buses are counted.  
B. 4 buses.  
C. 3.25 — CEIL preserves fractions.  
D. 5 — CEIL adds one extra vehicle after rounding up.

### 35. Two tools for two kinds of missing

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** NULL-Handling Functions  
**Is Curriculum Based:** No  
**Assessment type:** Function-role discrimination

A data-cleaning checklist has two jobs:

1. Where a value is NULL, substitute a display default.  
2. Where a column holds a placeholder value that *should* be treated as missing, convert it to NULL.

Map each cleanup job to its appropriate function.

A. COALESCE for both.  
B. NULLIF for job 1 and COALESCE for job 2.  
C. Job 1: COALESCE; job 2: NULLIF.  
D. Neither; only CASE can do these.

### 36. Value match or condition match?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Conditional Logic  
**Is Curriculum Based:** No  
**Assessment type:** CASE-form selection

Two labelling needs at a courier firm:

1. Map each `service_code` ('EXP', 'STD', 'ECO') to its display name.  
2. Band each `weight_kg` into ranges (under 5, 5–20, over 20).

Match each requirement to the most appropriate CASE form.

A. Simple CASE for job 1; searched CASE for job 2.  
B. The searched form for both because simple CASE cannot compare text.  
C. The simple form for both; ranges are values too.  
D. Neither need can use CASE.

### 37. Three parcels through the bands

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Conditional Logic  
**Is Curriculum Based:** No  
**Assessment type:** Full-CASE tracing

A courier company bands each parcel by weight to determine its shipping tier.

`parcels`

| parcel | weight_kg |
|---|---|
| P1 | 5 |
| P2 | 25 |
| P3 | 60 |

```sql
SELECT parcel, CASE
    WHEN weight_kg > 50 THEN 'freight'
    WHEN weight_kg > 20 THEN 'heavy'
    ELSE 'standard'
END AS band
FROM parcels;
```

Trace all three parcels through the ordered conditions.

A. All three 'standard'.  
B. P1 'heavy', P2 'freight', P3 'freight'.  
C. P1 'freight', P2 'heavy', P3 'standard' — interpreting conditions bottom-up.  
D. P1 'standard', P2 'heavy', P3 'freight' — matched in order.

### 38. From messy input to clean code

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** String Functions  
**Is Curriculum Based:** No  
**Assessment type:** Pipeline construction

A form field arrives as `'  mh '` and must become the clean state code `'MH'`.

Select the complete cleanup pipeline.

A. `SUBSTRING('  mh ' FROM 1 FOR 2)` — returning the two leading spaces.  
B. `LOWER(TRIM('  mh '))` — clean but the wrong case.  
C. `UPPER(TRIM('  mh '))` — TRIM removes spaces, then UPPER lifts to `MH`.  
D. `TRIM(UPPER)` — functions need no arguments.

### 39. How far off was the delivery?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Numeric Functions  
**Is Curriculum Based:** No  
**Assessment type:** ABS application

A procurement audit receives:

`po_lines`

| line_id | ordered | delivered |
|---:|---:|---:|
| 1 | 120 | 132 |
| 2 | 80 | 71 |

The report needs each discrepancy's magnitude, ignoring direction.

```sql
SELECT ABS(ordered - delivered) FROM po_lines;
```

Calculate both displayed discrepancy magnitudes.

A. -12 and 9 — keeping the original signs.  
B. 12 and 9, ABS stripping the sign, leaving 9 unchanged.  
C. 12 and -9 — reversing the sign of only the second result.  
D. 0 and 0.

### 40. Expiring within the month

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Date and Time Functions  
**Is Curriculum Based:** No  
**Assessment type:** Integrated date-logic construction

An insurance dashboard must list policies expiring in the next 30 days — not already expired, not further out.

Complete the two-sided date window.

A. `WHERE expiry_date >= CURRENT_DATE AND expiry_date <= CURRENT_DATE + INTERVAL '30 days'`.  
B. `WHERE expiry_date <= CURRENT_DATE + 30` — expired policies flood in.  
C. `WHERE EXTRACT(DAY FROM expiry_date) <= 30` — matches almost every date.  
D. `WHERE expiry_date = CURRENT_DATE + INTERVAL '30 days' OR expiry_date < CURRENT_DATE OR expiry_date IS NULL`.

---

## Instructor Key

### 1. B

Functions nest inside-out: TRIM produces `'goa'`, UPPER lifts it to `'GOA'`. The spaces are gone because the inner function ran first.

### 2. D

The second argument sets the precision: two decimal places. The discarded `89` begins with 8, so the second decimal rounds up from 7 to 8: 47.68. Option A describes truncation, which ROUND does not do.

### 3. C

EXTRACT pulls one named field from the date as a number — here the year, 2024. The date itself is unchanged and un-returned.

### 4. A

COALESCE returns its first non-NULL argument. Arjun's on-air name is NULL, so the scan moves to `full_name` and finds a value. Devika's row, by contrast, stops at 'Dev'.

### 5. D

CASE evaluates top-down and commits to the first true condition. 85 satisfies `>= 60` immediately, so 'Premium' is never tested — the classic ordering bug. Correct grading lists the narrowest (highest) band first.

### 6. B

`FROM 1 FOR 2` means: start at character 1, take 2. Characters count from one, so the result is the state code `'MH'`.

### 7. A

CEIL rounds toward positive infinity: 7.2 becomes 8. The business rule — a partial carton is still a carton you must pack — is exactly the "always up" behaviour, which ROUND (to nearest) would get wrong for 7.2.

### 8. C

Adding `INTERVAL '7 days'` shifts the timestamp by exactly seven days while preserving its 10:00 time. The resulting timestamp is 8 March at 10:00.

### 9. B

NULLIF(a, b) returns NULL when a equals b, and a otherwise. The 'UNKNOWN' sentinel matches and becomes genuine NULL; real branch names pass through untouched.

### 10. D

CASE is an expression, not a statement: it computes a value per row inside the query's result. The stored table is never modified (A) — the categories exist only in the output.

### 11. A

`||` joins left to right: the first name, a literal space, the last name. The space appears because it was explicitly supplied — concatenation adds nothing on its own.

### 12. C

ABS is distance from zero: −7 becomes 7. The controller cares how far the temperature strayed, not which direction — exactly the sign-discarding ABS provides.

### 13. B

CURRENT_DATE is the calendar date only. The time-of-day belongs to NOW() — the distinction matters the moment events within one day must be ordered.

### 14. D

COALESCE scans left to right for the first non-NULL: mobile fails, landline fails, and the string literal — which can never be NULL — wins. The fallback-last pattern guarantees the report never shows a blank.

### 15. A

The simple CASE form compares `size` to each WHEN value in turn: 'M' matches the second branch, returning 229. ELSE fires only when no listed value matches.

### 16. C

The three values differ only in case, so case normalization is the cure: LOWER maps all three spellings to one value. TRIM (A) fixes a problem this data doesn't have.

### 17. D

MOD returns the remainder of the division: 17 = 3 × 5 + **2**. The 2 is what the foreman must find space for — the full pallets are 17/5's whole part, not MOD's answer (B).

### 18. B

`<` on dates means "earlier than": 30 June and 23 July both precede 24 July. The Chimney's near-miss by one day is exactly why date comparisons need no special casing — chronology is the ordering.

### 19. A

COALESCE substitutes 0 for the NULL discount before the subtraction, keeping the arithmetic alive: 500 − 0 = 500. Without it, `500 - NULL` is NULL — option D's belief that NULL "acts as zero" is precisely the misconception this pattern exists to fix.

### 20. C

TRIM's jurisdiction is the ends of the string. Leading and trailing spaces go; the interior double space stays. Collapsing interior whitespace (D) would require a different tool.

### 21. B

ROUND goes to the *nearest* whole (9.99 → 10); FLOOR goes *down* regardless (9.99 → 9). Values just under a whole number are where the two visibly part ways.

### 22. D

EXTRACT(MONTH ...) reads the month field alone: 6 for Farhan's 2025 date and 6 for Omar's 2024 date. The filter never consulted the year — which is the point, and also the caution.

### 23. A

The chain handles both flavours of missing: NULLIF collapses the empty string to NULL, and COALESCE then replaces any NULL — original or newly made — with the display default. Order matters: COALESCE alone (D) would have passed the empty string straight through.

### 24. C

The condition routes each row: the fragile mirror takes the ×1.5 branch (600), the blanket takes the ELSE (300 unchanged). Arithmetic inside CASE branches is ordinary and per-row.

### 25. B

Concatenation with the hyphen as a quoted literal produces `TX-2025`. Option D concatenates the *words* 'prefix' and 'season' — quoting turns identifiers into text.

### 26. D

NOW() carries the full timestamp; CURRENT_DATE only the day. Pickup events need ordering within the day, so the flattening choice (A) would destroy exactly the information required.

### 27. A

NULL poisons arithmetic: one missing component nullifies the sum. Defaulting each nullable input with COALESCE(x, 0) before adding is the standard repair — the quote then reflects the known components.

### 28. C

Branch order is priority order. `> 100` is true for every large gift, so the narrower `> 5000` below it can never fire. CASE bugs of this shape produce no error — only quietly wrong labels — which is why ordering from narrowest to widest is the discipline.

### 29. D

Positions count from 1: character 4 begins `24`, and FOR 2 takes exactly those two. Option B's zero-based instinct comes from programming languages, not SQL.

### 30. B

"Per full 100" is a round-down rule: the incomplete last hundred earns nothing, so FLOOR's unconditional downward step matches the business exactly. ROUND would gift a point at 45.5.

### 31. A

Date minus date yields days elapsed: 14. It is the natural inverse of date-plus-integer from the same lesson.

### 32. C

NULLIF converts the dangerous 0 into NULL, and division by NULL is NULL, not an error. The report survives, and the zero-ride day reads as "no average" — which is the truthful answer.

### 33. D

CASE without ELSE has an implicit `ELSE NULL`. Calm rows match neither band and receive NULL — the blank cells are the missing ELSE made visible.

### 34. B

The division gives 3.25 — a fraction of a bus that still holds real people. CEIL's round-up to 4 is the only answer that seats everyone; FLOOR's 3 (option A) strands ten fans.

### 35. C

The two functions are converses: COALESCE replaces NULL with a value; NULLIF replaces a value with NULL. Job 1 is the former, job 2 the latter — and chained (as in Q23) they clean both problems at once.

### 36. A

The simple form is equality against one column — ideal for code-to-name mapping. Ranges need real conditions, which is the searched form's territory. Using the searched form for both works, but the match of form to job is the lesson.

### 37. D

Trace each weight top-down: 5 fails both tests and takes the ELSE; 25 fails `>50` but passes `>20`; 60 passes `>50` immediately. The bands land as standard, heavy, freight.

### 38. C

Two defects, two functions, right order: TRIM removes the padding, UPPER fixes the case. Option B cleans but lowercases — half a repair.

### 39. B

ABS turns each signed difference into a magnitude: |−12| = 12, |9| = 9. Over-delivery and under-delivery become comparable sizes, which is what an audit ranks.

### 40. A

The window needs both fences: `>= CURRENT_DATE` excludes expired policies, while `<= CURRENT_DATE + INTERVAL '30 days'` excludes dates beyond the window. Option D selects expired, NULL, or exactly-day-30 rows rather than the complete window.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Function-output tracing | 1, 2, 3, 4, 6, 8, 9, 11, 12, 14, 15, 17, 18, 19, 22, 24, 29, 31, 37, 39 |
| Function discrimination and selection | 13, 16, 20, 21, 26, 30, 34, 35, 36 |
| Diagnosis and repair | 5, 23, 27, 28, 32, 33 |
| Construction and integration | 7, 10, 25, 38, 40 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| String Functions | 1, 6, 11, 16, 20, 25, 29, 38 | 8 |
| Numeric Functions | 2, 7, 12, 17, 21, 30, 34, 39 | 8 |
| Date and Time Functions | 3, 8, 13, 18, 22, 26, 31, 40 | 8 |
| NULL-Handling Functions | 4, 9, 14, 19, 23, 27, 32, 35 | 8 |
| Conditional Logic | 5, 10, 15, 24, 28, 33, 36, 37 | 8 |

Questions 1–10 collectively cover all five Topic 4.1 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (3, 7, 10, 11, 12, 13, 16, 25, 26, 31)
- Intermediate: 27 questions
- Advanced: 3 questions (28, 32, 40)
- Correct option A: 10 questions (4, 7, 11, 15, 19, 23, 27, 31, 36, 40)
- Correct option B: 10 questions (1, 6, 9, 13, 18, 21, 25, 30, 34, 39)
- Correct option C: 10 questions (3, 8, 12, 16, 20, 24, 28, 32, 35, 38)
- Correct option D: 10 questions (2, 5, 10, 14, 17, 22, 26, 29, 33, 37)
- Longest consecutive run of one correct letter: below 3 throughout
