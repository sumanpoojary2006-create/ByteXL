# DBMS 4.4: Set Operations and Combining Queries — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** SQL for Data Retrieval and Analytics
- **Chapter:** Set Operations and Combining Queries
- **Scope:** All three Topic 4.4 subtopics in the attached course blueprint (UNION and UNION ALL; INTERSECT and EXCEPT; Set Operations vs. Joins)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every item begins with a recognisable data or reporting situation. When an answer depends on values, source rows and column meanings are shown in tables so the result can be checked row by row.
- **Evidence rule:** Students must trace whole-row membership, complete or repair set-operation SQL, test operand direction, compare query versions, diagnose shape mismatches, or select a tool from the required output shape.
- **Scope guard:** Only the behaviours taught in Topic 4.4 are assessed: compatible result shapes, duplicate handling, final-result sorting, UNION/UNION ALL, INTERSECT/EXCEPT, and the choice among set operations, joins, and existence checks.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all three Topic 4.4 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Two doors, one attendance list

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** UNION tracing

A hybrid conference records one attendee name per check-in source.

`online_log`

| attendee |
|---|
| Ria |
| Tom |
| Zed |

`hall_log`

| attendee |
|---|
| Tom |
| May |

```sql
SELECT attendee FROM online_log
UNION
SELECT attendee FROM hall_log;
```

Trace the stacked result and select its count and contents.

A. 4 distinct names — {Ria, Tom, Zed, May}; row order is unspecified.  
B. 5 — both lists end to end.  
C. 2 — only names in both lists.  
D. 1 — only the shared name, since UNION keeps just the one overlap between the two door logs.

### 2. Faithful to both blood banks

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** INTERSECT tracing

Two blood-bank branches record donor names independently.

`city_donors`

| donor |
|---|
| Pia |
| Qadir |
| Renu |

`lakeside_donors`

| donor |
|---|
| Qadir |
| Renu |
| Sam |

```sql
SELECT donor FROM city_donors
INTERSECT
SELECT donor FROM lakeside_donors;
```

Identify the rows that survive the whole-row membership test.

A. All five distinct donors.  
B. Pia and Sam — the loyal singles, each a donor at one branch only, never appearing at the other.  
C. Qadir and Renu — the names common to both.  
D. An empty result.

### 3. Two columns meet three

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Column-rule prediction

A recruiter tries:

```sql
SELECT name, city FROM walk_in_candidates
UNION
SELECT name, city, expected_ctc FROM portal_candidates;
```

Predict the database response before the recruiter runs the statement.

A. The extra column is silently dropped, and the query runs fine without any warning at all.  
B. An error — the two SELECT lists need matching column counts to stack.  
C. NULLs pad the shorter rows.  
D. Only the first query runs.

### 4. Sideways or stacked

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Core-difference identification

A mentor sketches two arrows: one pointing sideways, one pointing down.

Match each arrow to the operation whose output shape it represents.

A. Joins stack rows; set operations widen them.  
B. Both produce identical shapes.  
C. Joins and set operations both only count rows, never actually combining or comparing any of the column values.  
D. Joins combine *sideways* into wider rows; set operations *stack* same-shaped rows.

### 5. Every scan counts

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** UNION ALL tracing

Two turnstiles record every member scan as a separate event.

`east_gate`

| member_code |
|---|
| M-1 |
| M-2 |
| M-3 |

`west_gate`

| member_code |
|---|
| M-2 |
| M-4 |

```sql
SELECT member_code FROM east_gate
UNION ALL
SELECT member_code FROM west_gate;
```

Calculate the resulting event-row count.

A. 4 — duplicates removed.  
B. 5 — UNION ALL stacks everything, repeated M-2 included.  
C. 3 — the larger list only.  
D. 1 — the shared scan, because UNION ALL only reports codes appearing at both gates.

### 6. Subtraction is not commutative

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** Asymmetry tracing

An online seminar compares its registration and attendance records.

`registered`

| participant |
|---|
| Xu |
| Yana |
| Zoya |

`attended`

| participant |
|---|
| Yana |
| Walt |

Evaluate both operand orders and select the paired result that follows subtraction semantics.

A. `registered EXCEPT attended` gives Xu and Zoya; reversing the operands gives Walt instead.  
B. Both directions return Yana.  
C. Both directions return the same rows in different order, since EXCEPT just compares two sets of names.  
D. EXCEPT errors when the lists differ in length, since both sides of a set operation must return the same row count.

### 7. When the wide row is the point

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Tool-fit identification

A report must show each invoice's number beside its client's name and city — columns drawn from two different tables in every row.

Choose the tool whose output shape can place those attributes in the same row.

A. UNION — it combines two tables.  
B. EXCEPT — it filters the invoices.  
C. INTERSECT — invoices and clients overlap enough in their records that a comparison of both lists makes sense.  
D. A join — the requirement is *sideways*: each row needs columns from both tables at once.

### 8. Spring vendors who skipped autumn

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** EXCEPT tracing

A craft-market office stores one vendor name per seasonal roster.

`spring_market`

| vendor |
|---|
| Kala Pots |
| Loom & Co |
| Madder Dyes |

`autumn_market`

| vendor |
|---|
| Loom & Co |

```sql
SELECT vendor FROM spring_market
EXCEPT
SELECT vendor FROM autumn_market;
```

Subtract the second roster from the first and select the remaining vendors.

A. Loom & Co — the returning vendor, since EXCEPT reports names that appear in both markets.  
B. All four names.  
C. Kala Pots and Madder Dyes — the spring vendors absent from autumn.  
D. An empty result.

### 9. Text meets money

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Type-rule prediction

An intern tries to union a list of supplier *names* (text) with a list of invoice *amounts* (numeric), one column each.

Determine whether column-count compatibility alone is sufficient for this operation.

A. The union is rejected — matching column counts isn't enough; the types must be compatible too.  
B. The amounts convert to words automatically, since PostgreSQL coerces numeric values to text on union.  
C. The union succeeds with mixed types.  
D. The names become zero.

### 10. Same shape, one pile

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Tool-fit identification

Two queries each return `(volunteer_name, phone)` — one from the flood-relief roster, one from the ambulance roster. The coordinator wants one combined contact list.

Select the construction that matches a vertical, same-shaped combination.

A. A self join on volunteer_name.  
B. An inner join between the rosters.  
C. A CROSS product of the two lists, pairing every roster entry with every other roster entry.  
D. A set operation — same-shaped results, stacked into one list with UNION.

### 11. What UNION promises

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Behaviour identification

A data engineer reviews four descriptions before merging two compatible result sets. Select the one that predicts `UNION` correctly.

A. It pairs rows from two tables on a key.  
B. It stacks two queries' results into one pile and removes the duplicates.  
C. It returns rows found in both queries only.  
D. It subtracts the second query from the first, the way EXCEPT is commonly but incorrectly described.

### 12. The fair that ran in both months

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** Multi-column INTERSECT tracing

Two queries return complete `(city, day)` pairs for craft fairs.

`jan_fairs`

| city | day |
|---|---|
| Pune | Sat |
| Surat | Sun |

`feb_fairs`

| city | day |
|---|---|
| Pune | Sat |
| Pune | Sun |

```sql
SELECT city, day FROM jan_fairs
INTERSECT
SELECT city, day FROM feb_fairs;
```

Compare both columns together and select the surviving row set.

A. Three distinct pairs, counting every city-day combination that shows up across both months' fairs.  
B. `(Pune, Sat)` and `(Pune, Sun)`.  
C. Only `(Pune, Sat)` — intersection compares whole rows, and only that pair recurs.  
D. `(Surat, Sun)`.

### 13. Just answer yes or no

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Tool-fit discrimination

A dashboard tile needs each supplier flagged if they have *any* open dispute — no dispute details, no combined lists, just membership per supplier.

Choose the structure that answers the membership test without importing dispute columns.

A. UNION ALL of suppliers and disputes, stacking every supplier row directly on top of every dispute row with nothing filtered out.  
B. INTERSECT of the two tables' names.  
C. A FULL OUTER JOIN of everything.  
D. EXISTS — a yes/no membership check per row, not a stack or a widening.

### 14. Merging logs where repeats are real

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Variant selection

A plant's two production lines each log `(item_code, produced_on)` rows. Head office merges the two logs for a volume report — and the same item code legitimately appears many times, once per unit produced.

Select the operator that preserves the meaning of each logged production event.

A. UNION ALL — every row is a real event; UNION's dedup would collapse identical runs.  
B. UNION — duplicates are always noise.  
C. INTERSECT — the common items matter.  
D. EXCEPT — remove the second line's rows, leaving only items unique to the first line's own production run.

### 15. One sort for the whole pile

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** ORDER-BY placement

Two regional queries are combined with UNION, and the final contact list must be alphabetical.

Place `ORDER BY` where it controls the presentation of the entire combined result.

A. Inside each branch, so each sorts itself before the two ordered pieces are stacked together.  
B. Once, at the very end — it sorts the single combined result the UNION produced.  
C. It cannot be used with UNION.  
D. Before the first SELECT.

### 16. The untrained remainder

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** Anti-join-as-EXCEPT construction

A refinery must list staff who have **not** completed safety training: `all_staff(staff_name)` and `trained_staff(staff_name)`.

Complete the subtraction so that the first operand represents the population being screened.

A. `SELECT staff_name FROM trained_staff EXCEPT SELECT staff_name FROM all_staff;`  
B. `SELECT staff_name FROM all_staff INTERSECT SELECT staff_name FROM trained_staff;` — returns only staff appearing in both tables, which isn't what's needed.  
C. `SELECT staff_name FROM all_staff EXCEPT SELECT staff_name FROM trained_staff;` — everyone minus the trained.  
D. `SELECT staff_name FROM all_staff UNION SELECT staff_name FROM trained_staff;` — stacks both rosters into one combined name list.

### 17. Merge the two branch registers

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Tool selection

The east and west branches of a pharmacy chain each keep a `(customer_name, phone)` register. Head office wants one combined register, each person once.

Choose the operation that stacks both registers and removes exact duplicate contact rows.

A. UNION — same-shape lists stacked into one.  
B. INNER JOIN on phone.  
C. EXCEPT east from west.  
D. A self join of either register, matching each customer's row against every other row in that same table.

### 18. The join that should have been a stack

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Mis-tool diagnosis

To merge last year's and this year's `(sponsor_name, tier)` lists into one, an analyst wrote a JOIN between the two tables on sponsor_name — and got a *wide* result with doubled columns, missing all sponsors who appear in only one year.

Diagnose the mismatch between the required output shape and the chosen operation.

A. The join needed to be RIGHT instead.  
B. The lists were too long to join.  
C. The ON clause was misspelled, which is why the sponsor names failed to line up correctly across years.  
D. Wrong shape: the need was vertical stacking (UNION), not a join's sideways matching.

### 19. "In both" without the machinery

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Tool-fit reasoning

Two same-shaped queries list `(member_email)` for a book club's 2024 and 2025 rosters. The renewal report needs members present in both years.

Select the explanation that follows from the report asking only about whole-row membership.

A. Joins cannot compare emails.  
B. INTERSECT is always faster.  
C. The question is purely which rows appear in both results — INTERSECT states that directly.  
D. INTERSECT also returns the join's wide columns, since it likewise combines fields from both source tables.

### 20. Count after the collapse

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Dedup-scope tracing

Two shifts record each submitted sign-in row, including repeated submissions.

`morning_signins`

| name |
|---|
| Ana |
| Bo |
| Ana |
| Cy |

`evening_signins`

| name |
|---|
| Bo |
| Di |

```sql
SELECT name FROM morning_signins
UNION
SELECT name FROM evening_signins;
```

Determine the size of the deduplicated combined result.

A. 6 — everything kept, because UNION only removes duplicates that occur between the two separate sheets.  
B. 4 — Ana, Bo, Cy, Di; UNION deduplicates the entire combined pile, cross-list and within-list alike.  
C. 5 — only cross-list duplicates collapse.  
D. 2 — only duplicated names survive.

### 21. Which direction answers the question?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** Operand-order construction

The security desk compares the invitation roster with the entrance scan.

`invited`

| guest |
|---|
| Asha |
| Bo |
| Chen |

`checked_in`

| guest |
|---|
| Bo |
| Chen |
| Divya |

The desk asks: “Who walked in **without** an invitation?”

Choose the operand order that leaves `Divya`.

A. `invited EXCEPT checked_in` — the no-shows.  
B. `invited INTERSECT checked_in` — the well-behaved guests who both received an invite and actually checked in.  
C. `invited UNION checked_in` — everyone.  
D. `checked_in EXCEPT invited` — start from those present, subtract the invited; the gatecrashers remain.

### 22. Name beside amount

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Requirement-to-tool mapping

Requirement: one row per payout, showing the artist's *name* (from `artists`) beside the payout *amount* (from `payouts`).

Select the structure that can attach each payout amount to its related artist name.

A. A join on the artist key — each row needs columns from both tables side by side.  
B. UNION of names and amounts.  
C. EXCEPT of payouts from artists, leaving only artists absent from the payout rows.  
D. INTERSECT of the two tables.

### 23. Who names the columns?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Output-header reasoning

A combined report stacks `SELECT emp_name, city FROM north_staff` over `SELECT full_name, base_city FROM south_staff` with UNION — the columns align by position and type, but the two queries use different column names.

Predict the two headers exposed to the report consumer.

A. Both sets of names, hyphenated together into combined headers like `emp_name-full_name`.  
B. The first query's — `emp_name` and `city`; headers come from the leading SELECT.  
C. The second query's names.  
D. The union fails over the name mismatch.

### 24. Subtracting a superset

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** Empty-result tracing

The aviation office compares two one-column rosters.

`certified_pilots`

| pilot |
|---|
| Jai |
| Kiran |

`active_pilots`

| pilot |
|---|
| Jai |
| Kiran |
| Lena |

```sql
SELECT pilot FROM certified_pilots
EXCEPT
SELECT pilot FROM active_pilots;
```

Evaluate the first-list-minus-second-list result.

A. Lena.  
B. Jai and Kiran.  
C. Empty, since every certified pilot also appears in the active list.  
D. All three pilots, since EXCEPT here just reports the union of both certified and active rosters.

### 25. What ALL buys you

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Variant discrimination

A logging-team reviewer must preserve repeated events. Select the statement that distinguishes the two stacking operators correctly.

A. UNION ALL sorts; UNION does not, which is why UNION always needs an explicit ORDER BY clause added.  
B. UNION combines three or more queries; UNION ALL only two.  
C. They are interchangeable in every query.  
D. UNION deduplicates the combined result; UNION ALL skips that pass and keeps every stacked row.

### 26. Shapes that don't line up

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Precondition reasoning

A team wants to "union" `drivers(driver_id, name, licence_class)` with `vehicles(vehicle_id, model, capacity, fuel)`.

Judge the proposed operation from both row shape and business meaning.

A. Union them; the database aligns by meaning.  
B. Not a stacking situation — different shapes; any relationship is a join question, not a union.  
C. Add filler columns to drivers until the counts match.  
D. Convert both tables to text first, so that the mismatched driver and vehicle columns can line up.

### 27. Two verbs for two jobs

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Summary discrimination

Select the summary that lets a developer choose from the required output shape.

A. Joins are for reading, set operations for writing, a split that maps onto SELECT versus INSERT statements.  
B. Joins replace set operations in modern SQL.  
C. Joins *relate* rows into wider rows; set operations *combine* same-shaped sets into a taller list.  
D. Both exist only for performance tuning.

### 28. Three sources, one ballot

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Chained-union construction

A housing society collected votes by paper, app, and email — three tables, each queried as `(flat_no, choice)`. All three must combine into one deduplicated list.

Complete the three-source combination without widening the vote rows.

A. `SELECT flat_no, choice FROM paper_votes UNION SELECT flat_no, choice FROM app_votes UNION SELECT flat_no, choice FROM email_votes;` — chains three UNIONs into one stack.  
B. Set operations accept exactly two queries, so three sources cannot combine.  
C. A three-way join on flat_no, matching each paper vote against its corresponding app vote and its corresponding email vote all at once, widening every row instead of stacking them.  
D. Three separate reports stapled together.

### 29. Nothing in common

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** Empty-intersection tracing

Two menu queries expose the following rows.

`veg_menu`

| dish |
|---|
| Falafel Bowl |
| Paneer Wrap |

`seafood_menu`

| dish |
|---|
| Prawn Roll |
| Fish Curry |

```sql
SELECT dish FROM veg_menu INTERSECT SELECT dish FROM seafood_menu;
```

Record the outcome when no whole row belongs to both inputs.

A. All four dishes, since INTERSECT here simply reports the union of the veg and seafood menus.  
B. The first list.  
C. An error.  
D. An empty result — no dish appears in both lists, so the intersection is legitimately empty.

### 30. Two spellings of "never"

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Rewrite equivalence

`branches.branch_name` is declared `PRIMARY KEY`, and `drops.branch_name` is declared `NOT NULL`. Two queries aim to list clinic branches that received no supply drop this week:

```sql
-- Version 1
SELECT branch_name FROM branches b
WHERE NOT EXISTS (SELECT 1 FROM drops d WHERE d.branch_name = b.branch_name);

-- Version 2
SELECT branch_name FROM branches
EXCEPT
SELECT branch_name FROM drops;
```

Under those key and NULL constraints, decide whether the two versions return the same branch names.

A. Version 1 finds different branches than Version 2.  
B. Version 2 is invalid SQL.  
C. They express the same anti-join idea two ways, just written differently.  
D. Version 1 modifies data; Version 2 does not, since EXCEPT can only ever read from tables, never write.

### 31. Guaranteed arithmetic

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Count-prediction discrimination

A festival's two ticket queries return 120 and 85 rows. Both operators are considered.

Choose the count claim guaranteed without inspecting any row values.

A. UNION returns exactly 205 rows.  
B. UNION ALL returns exactly 205 (120 + 85); UNION returns *at most* that many.  
C. Both return exactly 205.  
D. UNION ALL returns 120, the larger list, since UNION ALL only ever reports the bigger of the two inputs.

### 32. Same name, different shift

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** Whole-row-matching tracing

Two monthly duty rosters expose complete `(guard_name, shift)` rows.

`jan_roster`

| guard_name | shift |
|---|---|
| Bala | night |
| Chand | day |

`feb_roster`

| guard_name | shift |
|---|---|
| Bala | day |
| Chand | day |

```sql
SELECT guard_name, shift FROM jan_roster
EXCEPT
SELECT guard_name, shift FROM feb_roster;
```

Trace the whole-row subtraction and select what survives.

A. `(Bala, night)` survives — EXCEPT matches whole rows, and Bala's shift changed between months.  
B. Nothing; both guards recur, because EXCEPT here only cares about the guard's name, not the shift column.  
C. `(Chand, day)`.  
D. Both January rows.

### 33. Membership across different shapes

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Tool-boundary reasoning

A fleet manager wants vans that appear in the accident register. The vans query returns five columns; the register has a completely different shape, sharing only the registration number.

Explain why keeping the five-column van row changes the appropriate structure.

A. INTERSECT is deprecated.  
B. EXISTS returns wider rows.  
C. Accident data cannot be subqueried, since register tables are entirely excluded from PostgreSQL's subquery and EXISTS support altogether.  
D. INTERSECT demands same shapes on both sides; this need keeps its own columns, which calls for EXISTS instead.

### 34. Different labels, same kind of thing

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Compatibility judgment

Query one returns `(shop_name TEXT, town TEXT)` from a franchise table; query two returns `(outlet TEXT, city TEXT)` from a partners table.

Determine whether positional compatibility is satisfied despite the different labels.

A. No — column names must match exactly.  
B. Yes — the rule is positional: two text columns stacking onto two text columns, names aside.  
C. No — different tables can never union.  
D. Only after renaming the tables to match, since PostgreSQL unions are matched by table name, not position.

### 35. Three questions, three operators

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Operator-to-question matching

Two same-shaped queries list this year's and last year's `(exhibitor_name)` at a trade fair. Three reports are wanted:

1. Everyone who exhibited in either year.  
2. The regulars — exhibited both years.  
3. The newcomers — this year but not last.

Map each business set to the operator and operand direction that produces it.

A. 1: INTERSECT, 2: UNION, 3: EXCEPT.  
B. 1: UNION ALL, 2: EXCEPT, 3: INTERSECT.  
C. 1: UNION, 2: INTERSECT, 3: this_year EXCEPT last_year — either, both, and first-minus-second.  
D. All three need joins, since exhibitor names must be matched across the two years' tables directly.

### 36. Last year's givers, gone quiet

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** Business-application construction

A charity's re-engagement campaign targets **lapsed donors**: people who gave last year but not this year. Queries exist for `last_year_donors(email)` and `this_year_donors(email)`.

Choose the subtraction whose first operand is the campaign's starting population.

A. `SELECT email FROM last_year_donors EXCEPT SELECT email FROM this_year_donors;` — minus repeat givers leaves the lapsed.  
B. `SELECT email FROM this_year_donors EXCEPT SELECT email FROM last_year_donors;` — the brand-new donors.  
C. `SELECT email FROM last_year_donors INTERSECT SELECT email FROM this_year_donors;` — the loyal.  
D. `SELECT email FROM last_year_donors UNION SELECT email FROM this_year_donors;` — everyone, which defeats the entire point of a targeted re-engagement campaign.

### 37. The union that OR could have been

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Design-appropriateness judgment

A `customers` table has unique, non-NULL `customer_id` values. A developer writes:

```sql
SELECT customer_id FROM customers WHERE city = 'Pune'
UNION
SELECT customer_id FROM customers WHERE signup_year = 2025;
```

A reviewer proposes:

```sql
SELECT customer_id
FROM customers
WHERE city = 'Pune' OR signup_year = 2025;
```

Compare the two versions under the stated key constraint.

A. The UNION version is wrong and returns different rows.  
B. The OR version misses customers matching both conditions.  
C. UNION is required whenever two conditions exist, since WHERE clauses cannot combine more than one filter.  
D. Both are correct here, but OR is simpler for one table; UNION matters when sources genuinely differ.

### 38. Say each one's job

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** UNION and UNION ALL  
**Is Curriculum Based:** No  
**Assessment type:** Definition pairing

A monitoring engineer must choose whether repeated alert rows remain visible. Select the accurate operator pairing.

A. UNION: keeps duplicates; UNION ALL: removes them, the reverse of what the keyword ALL actually suggests.  
B. UNION: sorts descending; UNION ALL: ascending.  
C. UNION: stack and deduplicate; UNION ALL: stack and keep everything.  
D. They differ only in speed of typing.

### 39. The report that listed the wrong people

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** INTERSECT and EXCEPT  
**Is Curriculum Based:** No  
**Assessment type:** Direction-bug diagnosis

A training coordinator compares these fire-drill rosters:

`enrolled`

| emp |
|---|
| Isha |
| Jatin |
| Kora |

`attended`

| emp |
|---|
| Isha |
| Noor |
| Pavel |
| Quinn |

The intended report is “enrolled but never attended,” but the query written was:

```sql
SELECT emp FROM attended EXCEPT SELECT emp FROM enrolled;
```

The output lists `Noor`, `Pavel`, and `Quinn`. Diagnose that result and identify the required repair.

A. The contractors hacked the drill, sneaking their names into the enrolled table without anyone noticing beforehand.  
B. The operands are reversed: this computes attended minus enrolled — walk-ins — not enrolled minus attended.  
C. EXCEPT malfunctioned on names.  
D. The data was stale.

### 40. Stack them, then screen them

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL for Data Retrieval and Analytics  
**Subtopic:** Set Operations vs. Joins  
**Is Curriculum Based:** No  
**Assessment type:** Integrated composition

A venue stores these one-column lists:

`gala`

| guest |
|---|
| Aditi |
| Bilal |
| Chao |

`afterparty`

| guest |
|---|
| Bilal |
| Deepa |

`blocklist`

| name |
|---|
| Bilal |
| Farah |

The compliance job must merge the guest lists into one deduplicated list and retain only actual guests who also occur on the blocklist.

Select the composition that returns only `Bilal`.

A. `(SELECT guest FROM gala UNION SELECT guest FROM afterparty) INTERSECT SELECT name FROM blocklist;` — union then screens against the blocklist.  
B. `SELECT guest FROM gala EXCEPT SELECT name FROM blocklist;`  
C. `SELECT guest FROM gala JOIN afterparty ON TRUE;`  
D. `SELECT name FROM blocklist UNION ALL SELECT guest FROM gala;` — stacks the blocklist directly on top of the gala guest list, treating every blocked name as if it were an actual guest.

---

## Instructor Key

### 1. A

UNION stacks the lists and removes duplicates from the pile: Tom's two appearances become one. Four distinct attendees remain; without `ORDER BY`, their presentation order is not guaranteed.

### 2. C

INTERSECT keeps rows present in *both* results — Qadir and Renu. Pia and Sam each appear on only one side and fall away.

### 3. B

Stacking requires alignment: same column count, compatible types, position by position. Two columns cannot stack onto three, and the database refuses rather than guesses (A, C).

### 4. D

The chapter's core picture: joins widen (columns from both tables, matched sideways), set operations pile (same-shaped rows, stacked vertically). Choosing between them starts with which direction the requirement points.

### 5. B

UNION ALL is stacking without the deduplication pass: 3 + 2 = 5 rows, M-2's repeat intact. For scan logs, that repeat is data, not noise.

### 6. A

EXCEPT keeps the first result's rows absent from the second — so each direction answers a different business question (no-shows versus walk-ins). The computed sets {Xu, Zoya} and {Walt} make the asymmetry concrete.

### 7. D

Columns from two tables in one row is the sideways requirement — a join's defining service. No stacking operator can place a client's city beside an invoice number.

### 8. C

Spring minus autumn: Loom & Co is subtracted, leaving Kala Pots and Madder Dyes. EXCEPT answers "in the first, not the second."

### 9. A

Column-count parity is necessary but not sufficient — the stacked values must be of compatible types, since each output column holds values from both queries. Text over numbers has no meaningful combined column.

### 10. D

Same shape, one list wanted: the textbook stacking scenario. UNION merges the rosters and collapses volunteers who serve in both.

### 11. B

UNION = stack + deduplicate. Pairing on a key (A) is a join; both-only (C) is INTERSECT; subtraction (D) is EXCEPT.

### 12. C

Set operators compare entire rows. `(Pune, Sat)` occurs in both months; February's `(Pune, Sun)` has no January twin. One pair survives the intersection.

### 13. D

The need is a per-supplier yes/no against another table — not a combined list (stacking) and not a widened row (joining). EXISTS is the chapter's named tool for exactly this membership check.

### 14. A

Each row is one unit produced; identical rows are separate events. UNION's deduplication would merge them and understate output — the ALL variant's whole purpose is preserving such genuine repeats.

### 15. B

The union produces one result set, and one ORDER BY at the end sorts it. Sorting the branches individually (A) cannot order the combined pile.

### 16. C

Anti-join as subtraction: everyone minus the trained leaves the untrained. Option A subtracts in the wrong direction and returns nobody (assuming trained ⊆ all).

### 17. A

Same shape, combine, each person once: UNION verbatim. The join options impose matching questions the requirement never asked.

### 18. D

The symptom (wide columns, only cross-list matches) is the join doing its sideways job faithfully — on a stacking problem. Tool-shape mismatch, not tool malfunction: the fix is UNION, not a different join type.

### 19. C

When both sides are same-shaped lists and the question is pure co-membership, INTERSECT is the direct expression: no keys, no aliases, no widened row to trim back down.

### 20. B

UNION deduplicates the entire combined result — including duplicates that originated within a single source. Ana's double signature and Bo's cross-shift appearances both collapse: four distinct names.

### 21. D

"Present but uninvited" starts from the present: checked_in minus invited. Option A answers the *opposite* audit (invited no-shows) — with EXCEPT, operand order is the question being asked.

### 22. A

One row per payout with columns from two tables: the sideways signature again. Options B–D all stack or compare same-shaped lists, which this requirement is not.

### 23. B

The combined result takes its column names from the first SELECT; subsequent queries contribute rows by position. The differing names are cosmetic, not structural (D).

### 24. C

Every row of the first result also appears in the second, so subtraction leaves nothing. Empty is a valid, informative answer: no certified pilot is missing from the active roster.

### 25. D

The ALL is literal: keep all stacked rows. UNION spends work removing duplicates; UNION ALL skips both the removal and the cost — the right default whenever repeats carry meaning.

### 26. B

Set operations precondition on same-shaped results describing the same kind of thing. Drivers and vehicles are different entities — any true relationship between them is key-based, which is join territory. Filler columns (C) fake the shape without creating the meaning.

### 27. C

Relate versus combine: joins build wider rows from related tables; set operations build taller lists from same-shaped results. The two verbs cover different requirements, not different eras (B).

### 28. A

Set operators chain left to right, each result being a valid operand for the next — three same-shaped sources stack into one deduplicated ballot in a single statement.

### 29. D

Disjoint lists intersect to the empty set. Like Q24's empty subtraction, an empty result is the correct report — the menus genuinely share nothing.

### 30. C

The primary key prevents duplicate branch names, `NOT NULL` removes the relevant NULL-semantics difference, and both versions compare the same single value. Under those stated constraints, the per-row `NOT EXISTS` check and whole-set `EXCEPT` subtraction produce the same branch names.

### 31. B

UNION ALL's count is pure arithmetic: 120 + 85 = 205, guaranteed. UNION's count depends on the data — 205 minus however many duplicates the pile contains, which cannot be known from the counts alone.

### 32. A

EXCEPT subtracts only exact whole-row matches. Chand's `(day)` row recurs identically and vanishes; Bala's January `(night)` row has no February twin — his shift changed — so it survives. Row-level matching is the whole story.

### 33. D

INTERSECT's precondition — same shape both sides — fails here, and forcing it would discard the vans' columns. EXISTS checks membership per row while the outer query keeps its own shape: the boundary between the tools, drawn on one example.

### 34. B

The union rule is positional and typed, not nominal: two text columns stack onto two text columns. Headers come from the first query; nothing else cares what the columns were called.

### 35. C

The three canonical set questions in business clothing: either (UNION), both (INTERSECT), first-without-second (EXCEPT, in that order). Option A scrambles the mapping.

### 36. A

Lapsed = gave last year, absent this year: last year's list minus this year's. Options B, C, and D compute the newcomers, the loyal, and the everyone — each a real list, none the campaign's.

### 37. D

Both versions produce each qualifying `customer_id` once: the key is unique, `UNION` removes overlap between the filters, and `OR` tests both conditions on the same row. The single `WHERE` is clearer here; `UNION` remains useful when genuinely separate result sources must be stacked.

### 38. C

One pair, one distinction: deduplicate or don't. The ALL keyword is the explicit opt-out of the collapse.

### 39. B

The contractors are the fingerprint of the reversed subtraction: attended-minus-enrolled surfaces walk-ins. Because EXCEPT is asymmetric, swapping operands doesn't reorder the answer — it answers a different question entirely. The intended list needs enrolled first.

### 40. A

Composability closes the chapter: the union's output is itself a result set, and the intersection accepts it as an operand. Merge, then screen — two set operations, one statement, no joins required.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Operation tracing over shown lists | 1, 2, 5, 6, 8, 12, 20, 24, 29, 32 |
| Rule and precondition prediction | 3, 9, 15, 23, 26, 31, 34 |
| Construction and operand-order reasoning | 16, 21, 28, 36, 40 |
| Tool-fit selection and discrimination | 4, 7, 10, 11, 13, 17, 19, 22, 25, 27, 33, 35, 38 |
| Diagnosis and equivalence judgment | 14, 18, 30, 37, 39 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| UNION and UNION ALL | 1, 3, 5, 9, 11, 14, 15, 20, 23, 25, 28, 31, 34, 38 | 14 |
| INTERSECT and EXCEPT | 2, 6, 8, 12, 16, 21, 24, 29, 32, 36, 39 | 11 |
| Set Operations vs. Joins | 4, 7, 10, 13, 17, 18, 19, 22, 26, 27, 30, 33, 35, 37, 40 | 15 |

Questions 1–10 collectively cover all three Topic 4.4 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (3, 7, 10, 11, 17, 25, 27, 29, 34, 38)
- Intermediate: 27 questions
- Advanced: 3 questions (30, 37, 40)
- Correct option A: 10 questions (1, 6, 9, 14, 17, 22, 28, 32, 36, 40)
- Correct option B: 10 questions (3, 5, 11, 15, 20, 23, 26, 31, 34, 39)
- Correct option C: 10 questions (2, 8, 12, 16, 19, 24, 27, 30, 35, 38)
- Correct option D: 10 questions (4, 7, 10, 13, 18, 21, 25, 29, 33, 37)
- Longest consecutive run of one correct letter: below 3 throughout
