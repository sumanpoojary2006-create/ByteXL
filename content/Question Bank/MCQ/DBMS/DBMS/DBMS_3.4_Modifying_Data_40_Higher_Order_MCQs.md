# DBMS 3.4: Modifying Data — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** SQL Essentials
- **Chapter:** Modifying Data
- **Scope:** All six Topic 3.4 subtopics in the attached course blueprint (INSERT; UPDATE; DELETE; The RETURNING Clause; UPSERT and ON CONFLICT; Why Modification Needs Discipline)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every item begins with a recognisable data-changing task. When an answer depends on stored values, the relevant schema, field meaning, and before-state are visible.
- **Evidence rule:** Students must trace a change, complete or repair SQL, compare implementations, select a defect-revealing test, or evaluate a safety decision—not recall an isolated keyword.
- **Scope guard:** Only modification concepts explicitly taught in Topic 3.4 are assessed; contextual tables support reasoning without introducing later DBMS topics.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all six Topic 3.4 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Add the new ferry

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** INSERT  
**Is Curriculum Based:** No  
**Assessment type:** Statement selection

A harbour authority must add the ferry *Sea Sparrow*, capacity 240, to `ferries(ferry_id, name, capacity)` with ID 7.

Select the statement that adds exactly the requested row.

A. `ADD ROW ferries VALUES (7, 'Sea Sparrow', 240);`  
B. `INSERT INTO ferries SET ferry_id = 7, name = 'Sea Sparrow', capacity = 240 RETURNING *;`  
C. `INSERT INTO ferries (ferry_id, name, capacity) VALUES (7, 'Sea Sparrow', 240);`  
D. `UPDATE ferries VALUES (7, 'Sea Sparrow', 240);`

### 2. The price change that hit everything

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Missing-WHERE tracing

A day spa lists its services along with their price.

`spa_services`

| service | price |
|---|---|
| Head massage | 600 |
| Foot therapy | 800 |
| Aroma facial | 1500 |
| Hot stone | 2200 |

A receptionist meant to reprice only the facial but ran:

```sql
UPDATE spa_services SET price = 99;
```

Record the resulting prices after PostgreSQL accepts the statement.

A. All four services now cost 99.  
B. Only Aroma facial costs 99.  
C. PostgreSQL rejects the statement because WHERE is missing.  
D. The table is empty.

### 3. Clearing the expired coupons

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DELETE  
**Is Curriculum Based:** No  
**Assessment type:** Targeted-delete tracing

An online store tracks the status of every coupon code it has issued.

`coupons`

| code | status |
|---|---|
| SAVE10 | active |
| FEST25 | expired |
| WELCOME | active |
| MONSOON | expired |
| VIP40 | active |

```sql
DELETE FROM coupons WHERE status = 'expired';
```

Identify the rows available to the next customer after the cleanup.

A. Only FEST25 and MONSOON.  
B. Nothing remains because DELETE ignores its condition.  
C. All five rows remain because DELETE only hides matching rows.  
D. SAVE10, WELCOME, and VIP40, expired rows removed.

### 4. The ID you need is the ID you just made

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The RETURNING Clause  
**Is Curriculum Based:** No  
**Assessment type:** Purpose identification

A ticket-support app inserts a new case whose `case_id` the database generates, and immediately needs that ID to show the customer.

```sql
INSERT INTO cases (subject) VALUES ('Refund query') RETURNING case_id;
```

Complete the developer's explanation of the clause.

A. Runs a second INSERT and returns that duplicate row's key.  
B. Hands back the new row's generated `case_id` directly.  
C. Returns the row to its previous state.  
D. Prints the whole table.

### 5. The second scan of the same badge

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPSERT and ON CONFLICT  
**Is Curriculum Based:** No  
**Assessment type:** Upsert tracing

A corporate campus logs the last gate where each employee badge was scanned.

`gate_passes` (`badge_id` is the primary key)

| badge_id | last_seen_gate |
|---|---|
| B-12 | North |

A badge scanner runs:

```sql
INSERT INTO gate_passes (badge_id, last_seen_gate)
VALUES ('B-12', 'East')
ON CONFLICT (badge_id) DO UPDATE SET last_seen_gate = 'East';
```

Record the single stored row after the scanner statement completes.

A. A uniqueness error leaves the original B-12 row unchanged.  
B. A second B-12 row is added.  
C. Nothing happens at all.  
D. The existing B-12 row's gate becomes 'East'.

### 6. Why writes deserve more respect than reads

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Why Modification Needs Discipline  
**Is Curriculum Based:** No  
**Assessment type:** Principle identification

A mentor tells a new hire: "Run all the SELECTs you like. But slow down before every INSERT, UPDATE, or DELETE."

Choose the principle behind the mentor's advice.

A. Modification statements use a different storage format from SELECT.  
B. SELECT is newer syntax than the others.  
C. Reads leave the data exactly as it was; writes change stored state.  
D. Writes are slower to type.

### 7. Two rows in one statement

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** INSERT  
**Is Curriculum Based:** No  
**Assessment type:** Multi-row tracing

A trekking tour desk logs each guest's booking and the trail they've chosen.

`trek_bookings`

| booking_id | guest | trail |
|---:|---|---|
| 1 | Isha | Lake Walk |
| 2 | Nikhil | Pine Track |
| 3 | Tara | Valley Path |

A tour desk then runs:

```sql
INSERT INTO trek_bookings (guest, trail) VALUES
('Farah', 'Ridge Loop'),
('Dev', 'Falls Path');
```

Calculate the row count after the statement succeeds.

A. 3 — only the first parenthesised value list is accepted.  
B. 5 — one VALUES list per new row, both added at once.  
C. 2 — the insert replaces the table.  
D. 6 — the comma causes each proposed row to be processed twice.

### 8. Deduct the crates that shipped

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Computed-update tracing

A distribution depot tracks the quantity of stock on hand for each item.

`depot_stock`

| item | qty |
|---|---|
| Apple crates | 40 |
| Mango boxes | 25 |

```sql
UPDATE depot_stock SET qty = qty - 5 WHERE item = 'Mango boxes';
```

Trace the two quantities into their after-state.

A. Apple crates 40, Mango boxes 20 — SET computed from the old value.  
B. Apple crates 35, Mango boxes 20 — both rows deducted.  
C. Mango boxes 5 — qty becomes the subtracted amount.  
D. Apple crates 40, Mango boxes 25 — the expression is calculated but not stored.

### 9. The WHERE that wasn't there

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DELETE  
**Is Curriculum Based:** No  
**Assessment type:** Unqualified-delete consequence

A cleanup script for a photography portal runs `DELETE FROM draft_albums;` — no WHERE clause. The table held 812 rows.

Determine both the fate of the rows and the fate of the table structure.

A. An error; DELETE demands a WHERE clause.  
B. The oldest row is deleted.  
C. All 812 rows are gone; the table remains.  
D. The table itself is removed together with all 812 rows.

### 10. RETURNING is not only for INSERT

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The RETURNING Clause  
**Is Curriculum Based:** No  
**Assessment type:** Applicability identification

A courier platform wants each statement to report what it just did.

Select the complete set of modification statements that can carry RETURNING.

A. INSERT only.  
B. INSERT, UPDATE, and DELETE alike, all can return rows.  
C. SELECT only.  
D. UPDATE and DELETE only; INSERT must use a separate SELECT.

### 11. Three columns, two values

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** INSERT  
**Is Curriculum Based:** No  
**Assessment type:** Mismatch prediction

A clerk at a seed bank runs:

```sql
INSERT INTO varieties (variety_id, name, species) VALUES (12, 'Red Flint');
```

Predict whether PostgreSQL can construct the proposed row.

A. The species becomes 'Red Flint'.  
B. The row is added with the missing value copied from the previous row.  
C. The first two columns fill and the statement waits for more input here.  
D. An error — three columns named but only two values supplied.

### 12. What forty minus five leaves

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Value tracing

A highway toll system tracks the prepaid balance on each vehicle's account.

`toll_accounts`

| vehicle | balance |
|---|---|
| KA-05-MX | 340 |

```sql
UPDATE toll_accounts SET balance = balance - 65 WHERE vehicle = 'KA-05-MX';
```

Compute the value stored after the update.

A. 275 — the right side read the old value, subtracted 65.  
B. 65 — SET stores the amount written.  
C. 340, because the original value cannot appear on the right side of SET.  
D. −65 — the subtraction applies to zero.

### 13. Preserve every completed delivery

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DELETE  
**Is Curriculum Based:** No  
**Assessment type:** Smallest safe repair

A dispatch table records whether a delivery is completed and whether its seven-day audit-retention period has ended.

`delivery_logs`

| log_id | status | retention_ended |
|---|---|---|
| 41 | completed | true |
| 42 | completed | false |
| 43 | failed | true |
| 44 | pending | false |

The cleanup must remove only completed deliveries whose retention has ended. The draft is too broad:

```sql
DELETE FROM delivery_logs
WHERE status = 'completed';
```

Select the smallest repair that protects log 42.

A. Remove the WHERE clause so the cleanup applies consistently.  
B. Add `AND retention_ended = true` to the existing condition.  
C. Replace the condition with `WHERE retention_ended = true`.  
D. Change the statement to UPDATE without specifying a SET clause.

### 14. What DELETE ... RETURNING hands back

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The RETURNING Clause  
**Is Curriculum Based:** No  
**Assessment type:** Output identification

An auction house tracks lots that have been withdrawn from a sale, and which sale each belonged to.

`withdrawn_lots`

| lot_id | sale_id | item |
|---:|---:|---|
| 8 | 44 | Brass compass |
| 9 | 45 | Silver frame |
| 10 | 44 | Railway clock |

```sql
DELETE FROM withdrawn_lots WHERE sale_id = 44 RETURNING *;
```

Describe the result set produced by this statement.

A. The rows that remain in the table after deletion.  
B. Only a count of deleted rows.  
C. The two complete rows it removed.  
D. The table's column definitions.

### 15. The duplicate that declined to shout

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPSERT and ON CONFLICT  
**Is Curriculum Based:** No  
**Assessment type:** DO NOTHING tracing

A newsletter platform records each subscriber's email and signup date. `newsletter_signups` has a UNIQUE rule on `email`.

| email | joined_on |
|---|---|
| mira@wick.net | 2025-06-02 |

The signup form re-submits:

```sql
INSERT INTO newsletter_signups (email) VALUES ('mira@wick.net')
ON CONFLICT (email) DO NOTHING;
```

Determine whether the repeated submission changes the table.

A. The existing row is overwritten using the submitted duplicate.  
B. An error interrupts the signup flow.  
C. A second copy of the email is stored.  
D. The statement completes quietly and the table is unchanged.

### 16. Look before you leap

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Why Modification Needs Discipline  
**Is Curriculum Based:** No  
**Assessment type:** Practice selection

A DBA is about to increase every West-corridor rate by 10%.

`freight_rates`

| route | corridor | rate |
|---|---|---:|
| P–Q | West | 900 |
| R–S | East | 750 |
| T–U | West | 1100 |

The planned modification is `UPDATE freight_rates SET rate = rate * 1.1 WHERE corridor = 'West';`.

Select the preview that checks the same target without changing data.

A. `SELECT * FROM freight_rates WHERE corridor = 'West';`  
B. `SELECT * FROM freight_rates WHERE rate = rate * 1.1;`  
C. `SELECT * FROM freight_rates WHERE corridor <> 'West';`  
D. `UPDATE freight_rates SET rate = rate;`

### 17. A table evolves after deployment

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** INSERT  
**Is Curriculum Based:** No  
**Assessment type:** Implementation comparison

A course table originally had columns in this order:

| position | column |
|---:|---|
| 1 | course_id |
| 2 | title |
| 3 | department |
| 4 | credits |

Two import scripts were written:

```sql
-- Version 1
INSERT INTO courses
VALUES (106, 'Operating Systems', 'Computer Science', 4);

-- Version 2
INSERT INTO courses (course_id, title, department, credits)
VALUES (106, 'Operating Systems', 'Computer Science', 4);
```

Later, the physical column order changes while the column names remain. Choose the defensible maintenance judgment.

A. Version 1 is safer because it contains fewer identifiers.  
B. Both versions map values by column name after any reordering.  
C. Version 2 preserves the mapping by naming its target columns.  
D. Version 2 inserts the same row twice after a schema change.

### 18. Two changes, one statement

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Multi-column syntax selection

A rental table currently contains:

| unit | rent | status |
|---|---:|---|
| 4B | 19500 | available |

The office must set 4B's rent to 21,000 **and** its status to `occupied` in one statement.

Complete the one-statement repair.

A. `UPDATE flats SET rent = 21000 SET status = 'occupied' WHERE unit = '4B';`  
B. `UPDATE flats SET rent = 21000, status = 'occupied' WHERE unit = '4B';`.  
C. `UPDATE flats rent = 21000 AND status = 'occupied' WHERE unit = '4B';`  
D. Two UPDATE statements are the only legal way.

### 19. The filter that was too broad

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DELETE  
**Is Curriculum Based:** No  
**Assessment type:** Over-deletion tracing

A city market tracks which stalls are active or expired across its locations.

`vendor_stalls`

| stall_id | city | status |
|---|---|---|
| 1 | Pune | expired |
| 2 | Pune | active |
| 3 | Nashik | expired |
| 4 | Pune | active |

The intent: remove only Pune's **expired** stalls. The statement actually run:

```sql
DELETE FROM vendor_stalls WHERE city = 'Pune';
```

Identify the actual blast radius.

A. Only stall 1 was deleted, as intended.  
B. Nothing was deleted because both intended conditions were not written.  
C. Stalls 1 and 3 were deleted — the expired pair.  
D. Stalls 1, 2, and 4 are gone.

### 20. One trip to the database, not two

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The RETURNING Clause  
**Is Curriculum Based:** No  
**Assessment type:** Advantage reasoning

Team A inserts a row, then runs a second SELECT to fetch its generated ID. Team B uses `INSERT ... RETURNING id`.

Choose the operational advantage provided by Team B's version.

A. The ID arrives as part of the insert itself, one round trip.  
B. Team B's rows get smaller IDs.  
C. RETURNING postpones constraint checking until after the ID is shown.  
D. None; the patterns are identical in every way.

### 21. Nightly prices, insert-or-update

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPSERT and ON CONFLICT  
**Is Curriculum Based:** No  
**Assessment type:** Use-case matching

A marketplace stores one row per unique SKU.

`products`

| sku | price |
|---|---:|
| K-10 | 450 |
| M-22 | 875 |

Tonight's file contains K-10 at 475 and a new SKU P-30 at 620. Existing SKUs must be updated and new SKUs inserted.

Select the modification structure that satisfies both cases.

A. Delete existing rows first, then load the entire supplier file.  
B. `INSERT ... ON CONFLICT (sku) DO UPDATE`, handling both cases.  
C. Plain INSERT and let the duplicates error out.  
D. Plain UPDATE and lose the new SKUs.

### 22. The preview is larger than the request

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Why Modification Needs Discipline  
**Is Curriculum Based:** No  
**Assessment type:** Pre-execution safety judgment

A DBA expects a correction to touch one loyalty account. Before writing the UPDATE, she runs a SELECT with the planned WHERE condition; the interface reports 4,127 matching rows.

Choose the responsible next action.

A. Run the UPDATE because the preview itself did not change any data.  
B. Add RETURNING but keep the same broad WHERE condition.  
C. Run the preview repeatedly until only one row appears.  
D. Stop, repair the condition, and preview it again.

### 23. The second badge 7

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** INSERT  
**Is Curriculum Based:** No  
**Assessment type:** Constraint-violation prediction

A marathon organizer assigns a unique bib number to each registered runner. `race_bibs` uses `bib_no` as its primary key.

| bib_no | runner |
|---:|---|
| 7 | Asha Jain |
| 8 | Manoj Pillai |

A registration desk runs:

```sql
INSERT INTO race_bibs (bib_no, runner) VALUES (7, 'Kiran Shet');
```

Predict the write result before the clerk submits it.

A. The statement fails with a uniqueness violation, adding nothing.  
B. Kiran replaces the existing bib-7 runner without an UPDATE clause.  
C. A second bib 7 is issued.  
D. The database renumbers Kiran to bib 8.

### 24. The overwrite has no undo button

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Why Modification Needs Discipline  
**Is Curriculum Based:** No  
**Assessment type:** Risk-symmetry reasoning

A junior engineer is careful with DELETE but casual with UPDATE, reasoning "update only changes values, it doesn't destroy anything."

Challenge the engineer's claim using the chapter's safety principle.

A. UPDATE is actually slower than DELETE.  
B. UPDATE cannot use WHERE, so every value change necessarily affects the full table.  
C. UPDATE can replace old values that the system may not preserve.  
D. Nothing; UPDATE is indeed harmless.

### 25. What INSERT does — and doesn't — touch

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** INSERT  
**Is Curriculum Based:** No  
**Assessment type:** Effect identification

An ice-cream bakery tracks the flavours it currently offers. It starts with:

`flavours`

| flavour_id | name |
|---:|---|
| 1 | Vanilla |
| 2 | Cocoa |
| … | four other existing rows |

It successfully inserts `(7, 'Pistachio')`.

Describe the table immediately after the successful insert.

A. The table has 7 rows, renumbered from scratch.  
B. The table has 7 rows; the original 6 stay unchanged.  
C. The oldest flavour was replaced.  
D. The table has 6 rows because the new row replaces the oldest flavour.

### 26. One row changes; its other values survive

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** After-state tracing

A clinic tracks the wing, status, and bed count for each of its rooms.

`clinic_rooms`

| room_id | wing | status | beds |
|---|---|---|---:|
| R1 | East | cleaning | 2 |
| R2 | West | available | 4 |
| R3 | East | occupied | 1 |

```sql
UPDATE clinic_rooms
SET status = 'available'
WHERE room_id = 'R1';
```

Record R1 after the statement.

A. `R1, East, available, NULL` because unmentioned columns are cleared.  
B. `R1, West, available, 4` because values come from another available room.  
C. `R1, East, cleaning, 2` because UPDATE cannot change a single column.  
D. `R1, East, available, 2` because only the named SET column changes.

### 27. Deleting what was never there

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DELETE  
**Is Curriculum Based:** No  
**Assessment type:** Zero-match mechanics

An art gallery tracks which hall each exhibit is displayed in. It contains:

`exhibits`

| exhibit_id | hall |
|---:|---|
| 1 | Main |
| 2 | Annex-A |
| 3 | Main |

It runs `DELETE FROM exhibits WHERE hall = 'Annex-C';`.

Record the database response and resulting row count.

A. It completes normally; all three rows remain.  
B. An error, since nothing matched.  
C. Every exhibit outside Annex-C is deleted instead.  
D. The table locks until a matching row appears.

### 28. Returning more than the key

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The RETURNING Clause  
**Is Curriculum Based:** No  
**Assessment type:** Output-shape tracing

A ride-hailing app tracks each driver's in-app wallet balance.

`cab_wallets`

| driver | balance |
|---|---|
| Ashraf | 900 |

```sql
UPDATE cab_wallets SET balance = balance + 150
WHERE driver = 'Ashraf'
RETURNING driver, balance;
```

Trace the result row produced by RETURNING.

A. One row containing Ashraf and the original balance, 900.  
B. Just the text `UPDATE 1`.  
C. One row: Ashraf, 1050, its new state after the SET.  
D. Two rows: the before and the after.

### 29. Where the conflict is declared

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPSERT and ON CONFLICT  
**Is Curriculum Based:** No  
**Assessment type:** Clause-anatomy understanding

The `stations` table enforces a UNIQUE rule on `call_sign`.

Interpret `(call_sign)` in `INSERT INTO stations (call_sign, freq) VALUES ('RJ-92', 98.3) ON CONFLICT (call_sign) DO UPDATE SET freq = 98.3;`.

A. The column to delete on conflict.  
B. The columns that the DO UPDATE branch is forbidden to modify.  
C. A comment with no effect.  
D. The uniqueness rule used to detect the conflict.

### 30. The safe sequence for a big cleanup

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Why Modification Needs Discipline  
**Is Curriculum Based:** No  
**Assessment type:** Procedure ordering

An ops engineer must purge thousands of stale device registrations from production.

Arrange the cleanup around the chapter's preview-and-verify discipline.

A. Preview with the same WHERE, then verify the DELETE through RETURNING.  
B. Run the DELETE first, then SELECT to see what it did.  
C. Export the table, delete every row, then manually restore wanted rows.  
D. Ask a colleague to run it so responsibility transfers.

### 31. The receipt inside the statement

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The RETURNING Clause  
**Is Curriculum Based:** No  
**Assessment type:** Value tracing

A metro transit system tracks the prepaid balance stored on each rider's card.

`metro_cards`

| card_no | balance |
|---|---|
| MC-881 | 500 |

A top-up gate runs:

```sql
UPDATE metro_cards SET balance = balance - 120
WHERE card_no = 'MC-881'
RETURNING balance;
```

Compute the value delivered to the rider's screen.

A. 500 — the balance before the fare was deducted.  
B. 120 — the fare.  
C. 380 — the updated balance.  
D. 620 — the fare added.

### 32. Why the database obeyed

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Why Modification Needs Discipline  
**Is Curriculum Based:** No  
**Assessment type:** Root-cause analysis

An intern ran `DELETE FROM sessions;` on a live quiz platform, wiping every active session. In the retrospective, someone asks: "Why didn't the database ask, 'are you sure?'"

Choose the technically accurate response for the retrospective.

A. The confirmation feature was misconfigured.  
B. SQL executes exactly what a valid statement says, obediently.  
C. The intern's account had a bug.  
D. Valid DELETE statements require no confirmation only for empty tables.

### 33. Quotes around the right things

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** INSERT  
**Is Curriculum Based:** No  
**Assessment type:** Literal-syntax selection

A kennel adds a boarding record: dog name *Biscuit*, kennel number 12, daily rate 850.50.

Select the VALUES list that represents those three supplied values.

A. `VALUES (Biscuit, '12', '850.50')` — wrong quoting throughout.  
B. `VALUES ("Biscuit", 12, 850.50)`  
C. `VALUES (Biscuit, 12, 850.50)`  
D. `VALUES ('Biscuit', 12, 850.50)`, text quoted, numbers bare.

### 34. Only the overdue in the West

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Compound-target tracing

A municipal utility tracks the payment status of water meters across its service zones.

`water_meters`

| meter_id | zone | status |
|---|---|---|
| M1 | West | overdue |
| M2 | West | paid |
| M3 | East | overdue |
| M4 | West | overdue |

```sql
UPDATE water_meters SET status = 'notice_sent'
WHERE zone = 'West' AND status = 'overdue';
```

Trace the predicate and identify the changed meters.

A. M1 and M4, satisfying both conditions at once.  
B. M1, M2, and M4 — every meter in the West zone.  
C. M1, M3, and M4 — all the overdue.  
D. All four meters.

### 35. Older than the cutoff

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DELETE  
**Is Curriculum Based:** No  
**Assessment type:** Range-delete tracing

An IoT monitoring platform logs the timestamp of each ping received from field sensors.

`sensor_pings`

| ping_id | pinged_on |
|---|---|
| 1 | 2025-03-02 |
| 2 | 2025-06-20 |
| 3 | 2025-01-15 |
| 4 | 2025-07-01 |

```sql
DELETE FROM sensor_pings WHERE pinged_on < '2025-04-01';
```

List the rows still available after the deletion.

A. Pings 1 and 3 — the rows matching the cutoff remain.  
B. All four; date ranges cannot drive deletes.  
C. Pings 2 and 4.  
D. Only ping 4, the newest.

### 36. Check-then-insert versus one statement

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPSERT and ON CONFLICT  
**Is Curriculum Based:** No  
**Assessment type:** Pattern comparison

Version 1: the app SELECTs to see whether a device token exists, then chooses INSERT or UPDATE in code. Version 2: a single `INSERT ... ON CONFLICT ... DO UPDATE`.

Identify the reason Version 2 is safer under concurrent submissions.

A. A preliminary SELECT cannot reliably check whether a row exists.  
B. One atomic statement replaces the check-then-act dance entirely.  
C. Version 2 runs without any constraints.  
D. Version 1 is favoured, actually.

### 37. The row that lost the fight but left its values

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** UPSERT and ON CONFLICT  
**Is Curriculum Based:** No  
**Assessment type:** EXCLUDED-reference understanding

A price catalogue currently contains:

| sku | price |
|---|---:|
| TK-11 | 749 |

The price-sync statement reads:

```sql
INSERT INTO sku_prices (sku, price) VALUES ('TK-11', 799)
ON CONFLICT (sku) DO UPDATE SET price = EXCLUDED.price;
```

Identify the source of `EXCLUDED.price` during the conflict branch.

A. The price already stored in the conflicting table row.  
B. The average of old and new prices.  
C. A price of zero.  
D. The proposed insert's price, 799.

### 38. What separates reading from writing

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Why Modification Needs Discipline  
**Is Curriculum Based:** No  
**Assessment type:** Category discrimination

A change-review board fast-tracks some SQL and scrutinizes the rest.

Classify the statements using whether stored state changes.

A. SELECT is harmless to stored data; writes change state.  
B. Long statements are risky; short ones are safe.  
C. Statements with WHERE are writes; statements without WHERE are reads.  
D. Morning statements are safe; evening ones risky.

### 39. Rows go, table stays

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** DELETE  
**Is Curriculum Based:** No  
**Assessment type:** Scope-of-effect discrimination

After a full `DELETE FROM old_promos;` empties all 200 rows, a marketer asks whether the team must now re-create the table before the next campaign.

Resolve whether the empty table must be re-created.

A. Yes — DELETE removes the table definition with its final row.  
B. Yes — but only the column types survive.  
C. No — DELETE removes rows, never the table itself.  
D. It depends on the number of rows deleted.

### 40. The payroll incident, prevented three ways

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Why Modification Needs Discipline  
**Is Curriculum Based:** No  
**Assessment type:** Integrated discipline synthesis

A payroll UPDATE meant for one contractor hit 3,900 rows last quarter. The post-mortem must name layered controls that would have prevented the broad update or detected it immediately.

Choose the layered controls that directly address the incident.

A. Faster hardware, longer passwords, and a newer SQL client for execution.  
B. Preview with SELECT, review the WHERE, then inspect RETURNING.  
C. Ban UPDATE statements and edit rows one by one in a GUI.  
D. Run payroll updates only on weekends.

---

## Instructor Key

### 1. C

INSERT INTO names the table and columns; VALUES supplies matching data in order. The other forms are invented syntax — and option D confuses adding with modifying.

### 2. A

UPDATE's scope is defined solely by WHERE, and there is none: every row matched, every price became 99. The statement is legal, obedient, and catastrophic — which is the lesson.

### 3. D

The WHERE targets the two expired rows; DELETE removes exactly those. The active three are untouched — deletion is as precise, or as broad, as its filter.

### 4. B

RETURNING turns the insert into its own answer: the generated key comes back as the statement's result. Without it, the app would need a second query to find the row it just made.

### 5. D

The key collision triggers the declared alternative: instead of a duplicate-key error, the DO UPDATE branch runs and the existing row's gate becomes East. One statement, two possible actions, chosen by whether the key already exists.

### 6. C

The asymmetry is about consequences: reads are repeatable and leave no mark; writes overwrite or remove stored state, and the database provides no automatic undo for a statement that did exactly what it said.

### 7. B

Each parenthesized list after VALUES is one new row; the single statement appended two. Three plus two is five.

### 8. A

`qty = qty - 5` reads the current value on each matched row and stores the result: mangoes 25 → 20. Apples never matched the WHERE and keep their 40.

### 9. C

An unqualified DELETE empties the table — all 812 rows — but DELETE operates on rows, never on the table's existence. The structure remains, hollow.

### 10. B

RETURNING attaches to all three modification verbs, reporting the rows each created, changed, or removed. It is the statement's own receipt, whatever the verb.

### 11. D

The column list is a contract: three names promise three values. Two arrive; the statement is rejected whole. Mismatched lists fail loudly rather than guess.

### 12. A

The assignment's right side evaluates against the row's current state: 340 − 65 = 275, then the store happens. Self-reference in SET is not circular — it is the standard way to adjust a value.

### 13. B

The existing status condition already expresses half the policy. Adding the retention test with AND narrows the target to log 41; replacing the condition with retention alone would also remove failed log 43.

### 14. C

`RETURNING *` on a DELETE emits the removed rows in full — the only look anyone will get at them after the statement commits. Option A inverts it: the result is what left, not what stayed.

### 15. D

DO NOTHING converts the would-be duplicate-key error into a quiet no-op: statement succeeds, table unchanged. For an idempotent signup form, silence is exactly the desired behaviour.

### 16. A

The preview discipline reuses the *identical* WHERE in a SELECT: the returned rows are precisely the rows the UPDATE will touch. Any surprise — wrong rows, wrong count — surfaces while everything is still reversible, because nothing has happened yet.

### 17. C

Version 2 explicitly pairs every value with a column name, so a later change in physical order does not change the mapping. Version 1 depends entirely on remembering the table's current positional order.

### 18. B

One UPDATE, one SET, assignments comma-separated. Repeating SET (A) is a syntax error; two statements (D) work but are not required — and lose the all-at-once quality.

### 19. D

The missing second condition halved the WHERE and tripled the damage: every Pune row matched, including two active stalls. The gap between intent and clause is exactly one AND — and the data shows what that AND was worth.

### 20. A

RETURNING fuses the write and the read of its result into one atomic statement: no second round trip, and no reliance on being able to find the row again afterwards.

### 21. B

The nightly file is the canonical upsert workload: unknown mix of new and existing keys. ON CONFLICT DO UPDATE lets one statement resolve each row's case itself — no pre-checking, no duplicate errors, no lost newcomers.

### 22. D

The preview is performing its safety role before any values change. A condition expected to identify one account but matching 4,127 must be repaired and previewed again; RETURNING cannot make an unsafe target safe.

### 23. A

Primary keys are enforced at write time: the duplicate insert fails completely and changes nothing. No overwrite (B), no second row (C), no renumbering (D) — constraints fail statements; they do not negotiate.

### 24. C

UPDATE's loss is quieter but real: it replaces the previous stored values. Unless a transaction, backup, or other recovery mechanism preserves them, a broad incorrect UPDATE can lose history much like a DELETE.

### 25. B

INSERT is purely additive: a new row joins, existing rows are untouched. Any renumbering or replacement behaviour would belong to other statements — and doesn't happen here.

### 26. D

The WHERE isolates R1, and SET names only `status`. UPDATE preserves R1's wing and bed count, so the row becomes `R1, East, available, 2`.

### 27. A

Zero matches is a legitimate result rather than an error. No row satisfies the Annex-C condition, so DELETE changes nothing and all three exhibits remain.

### 28. C

RETURNING reports the row's post-statement state in the named columns: the balance after +150 is 1050. It is a receipt for what the statement *did*, not a snapshot of what it found.

### 29. D

The parenthesized column names the uniqueness being watched: a clash there — and only there — diverts the insert into its DO branch. It is the hinge on which the statement's two behaviours turn.

### 30. A

The sequence brackets the destructive act with evidence: the preview defines the intended target, the identical WHERE executes it, and RETURNING shows the rows actually removed. Option B waits until after the data has changed to discover the target.

### 31. C

The statement subtracts 120 from 500 and reports the new balance — 380 — as its own result. The rider's screen is fed by the write itself.

### 32. B

The database is an executor, not a guardian: a valid unqualified DELETE means "all rows," and it did precisely that. Every safeguard — previews, precise filters, count read-back — is human discipline, which is the chapter's entire thesis.

### 33. D

SQL string literals take single quotes; numeric literals go bare. Double quotes (B) name identifiers, not values, and unquoted text (A, C) reads as a column name that doesn't exist.

### 34. A

AND intersects the two conditions: West and overdue. M1 and M4 satisfy both; M2 is West but paid, M3 overdue but East. Two rows change; two are protected by the precision.

### 35. C

The range condition caught the March and January pings — both before the April cutoff — and removed them. The June and July pings remain: date deletes are just comparisons driving the same row-removal machinery.

### 36. B

The check-then-act pattern has two costs: more code, and a timing gap between the SELECT and the write where reality can change. The single ON CONFLICT statement closes both — the database resolves each row's case at write time, atomically.

### 37. D

EXCLUDED is the name of the row that was proposed but conflicted: its `price` is 799. Referencing it lets the DO UPDATE reuse the incoming values generically — the same statement works for every SKU and price in the file.

### 38. A

The dividing line is state change. Reads can run twice, ten times, on a whim — the data is identical after. Writes alter the stored world, so each gets the full ceremony: preview, precision, verification.

### 39. C

DELETE's domain is rows. The emptied table keeps its name, columns, types, and constraints — the container survives its contents, and tomorrow's campaign can insert into it directly.

### 40. B

The controls work at different moments: the preview exposes the blast radius, WHERE review compares the clause with the request, and RETURNING reveals the affected rows immediately. Their value comes from layering, not assuming one check is infallible.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Before/after state tracing | 2, 3, 5, 7, 8, 9, 12, 15, 19, 26, 28, 31, 34, 35 |
| Statement completion and smallest repair | 1, 11, 13, 18, 21, 33 |
| Modification response and error prediction | 14, 23, 27 |
| Discipline, procedure, and root-cause judgment | 6, 16, 24, 30, 32, 38, 40 |
| Pattern comparison, equivalence, and clause anatomy | 4, 10, 17, 20, 25, 29, 36, 37, 39 |
| Defect-exposing preview and scope validation | 22 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| INSERT | 1, 7, 11, 17, 23, 25, 33 | 7 |
| UPDATE | 2, 8, 12, 18, 26, 34 | 6 |
| DELETE | 3, 9, 13, 19, 27, 35, 39 | 7 |
| The RETURNING Clause | 4, 10, 14, 20, 28, 31 | 6 |
| UPSERT and ON CONFLICT | 5, 15, 21, 29, 36, 37 | 6 |
| Why Modification Needs Discipline | 6, 16, 22, 24, 30, 32, 38, 40 | 8 |

Questions 1–10 collectively cover all six Topic 3.4 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 7 questions (10, 11, 14, 25, 27, 33, 39)
- Intermediate: 31 questions
- Advanced: 2 questions (36, 40)
- Correct option A: 10 questions (2, 8, 12, 16, 20, 23, 27, 30, 34, 38)
- Correct option B: 10 questions (4, 7, 10, 13, 18, 21, 25, 32, 36, 40)
- Correct option C: 10 questions (1, 6, 9, 14, 17, 24, 28, 31, 35, 39)
- Correct option D: 10 questions (3, 5, 11, 15, 19, 22, 26, 29, 33, 37)
- Longest consecutive run of one correct letter: below 3 throughout
