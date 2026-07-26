# DBMS 6.1: Transactions and ACID — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Transactions & Reliability
- **Chapter:** Transactions and ACID
- **Scope:** All five Topic 6.1 subtopics in the attached course blueprint (What is a Transaction; Atomicity; Consistency; Isolation; Durability)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Questions begin with a recognisable DBMS situation, identify what each table or field represents, and provide the rows, constraints, SQL, session order, or failure point needed to reason to one answer.
- **Evidence rule:** A question never expects a student to invent an unstated starting value, transaction boundary, constraint, commit status, or PostgreSQL setting.
- **Scope guard:** Every question uses only the five ideas taught in Topic 6.1. Later material such as savepoints, deadlocks, locking strategies, and detailed isolation-level anomalies is intentionally excluded.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all five Topic 6.1 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Two statements that must not travel alone

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** What is a Transaction  
**Is Curriculum Based:** No  
**Assessment type:** Necessity reasoning

A mobile-wallet database stores each customer's available money in `wallet_accounts.balance`.

`wallet_accounts`

| account_id | customer | balance |
|---|---|---:|
| W10 | Asif | 2000 |
| W20 | Meera | 1000 |

Transferring 500 from W10 to W20 requires one UPDATE to debit Asif and another to credit Meera. A failure between separately committed statements would leave money missing.

Select the design that preserves the meaning of “one transfer.”

A. Put each UPDATE in its own transaction so each balance is protected independently.  
B. Wrapping both in one transaction makes them a single unit of work — either both effects happen or neither does.  
C. Add `CHECK (balance >= 0)` to both accounts; that alone guarantees the credit follows the debit.  
D. Commit the debit first and retry only the credit after a failure, without treating the pair as one recoverable unit.

### 2. The crash between debit and credit

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Atomicity  
**Is Curriculum Based:** No  
**Assessment type:** Crash-outcome tracing

`accounts`

| holder | balance |
|---|---|
| Asif | 2000 |
| Meera | 1000 |

A transfer transaction begins, executes `UPDATE accounts SET balance = balance - 500 WHERE holder = 'Asif';` — and the server loses power before the credit statement or any COMMIT.

After restart, what does the table show?

A. Asif 1500, Meera 1000 — the completed UPDATE survives without COMMIT.  
B. Asif 1500, Meera 1500 — recovery completes the intended transfer.  
C. Asif 2000, Meera 1500 — recovery applies only the missing credit.  
D. Asif 2000, Meera 1000.

### 3. The rule that defines "valid"

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Consistency  
**Is Curriculum Based:** No  
**Assessment type:** Constraint-role identification

A prepaid-card table declares `CHECK (balance >= 0)`. A purchase transaction attempts to set a card's balance to −150.

Choose the database outcome and the ACID property that explains it.

A. The statement is rejected and the transaction cannot commit that change.  
B. The statement succeeds because CHECK rules are examined only when the table is queried.  
C. The statement succeeds inside the transaction, but COMMIT converts −150 back to zero.  
D. The statement is rejected because atomicity itself knows that negative balances are invalid.

### 4. What the other checkout must not see

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation  
**Is Curriculum Based:** No  
**Assessment type:** Visibility tracing

At a box office, `ticket_prices.price` is the amount currently charged for a show.

`ticket_prices` before either transaction starts:

| show_id | price |
|---|---:|
| S12 | 400 |

| Step | Transaction T1 | Transaction T2 |
|---:|---|---|
| 1 | `BEGIN;` | |
| 2 | Updates S12's price to 450 | |
| 3 | No COMMIT yet | Reads S12's price |

Choose the value returned to T2.

A. 450 — another session may read a value as soon as its UPDATE finishes.  
B. No row — an updated row disappears from other sessions until commit.  
C. 400 — T1's uncommitted change is invisible to others.  
D. The SELECT must wait for T1 even though it only reads the last committed value.

### 5. The reboot after the receipt

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Durability  
**Is Curriculum Based:** No  
**Assessment type:** Post-commit crash tracing

Under normal PostgreSQL durability settings, a food-delivery order is inserted, the transaction COMMITs, and the app shows the customer "Order confirmed." Ninety seconds later the database server reboots from a power fault.

After restart, where is the order?

A. Still there — COMMIT guarantees durability.  
B. Gone — COMMIT controls visibility but not recovery after power loss.  
C. Present only if the application repeats the INSERT during startup.  
D. Uncertain — the promise begins only after a later backup completes.

### 6. The three words around the work

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** What is a Transaction  
**Is Curriculum Based:** No  
**Assessment type:** Missing-boundary completion

A clinic booking must insert an appointment and its audit record as one unit. Complete the two blanks:

```sql
____;
INSERT INTO appointments VALUES (410, '2026-07-28', 'Nila');
INSERT INTO appointment_audit VALUES (410, 'CREATED');
____;
```

A. First blank `COMMIT`; second blank `BEGIN`  
B. First blank `BEGIN`; second blank `COMMIT`  
C. First blank `BEGIN`; second blank `ROLLBACK`  
D. First blank omitted; second blank `COMMIT`

### 7. Change of heart, change of table?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Atomicity  
**Is Curriculum Based:** No  
**Assessment type:** ROLLBACK tracing

`campsite_bookings(booking_id, guest_name)` stores one row per confirmed campsite reservation. It contains 12 committed rows before a clerk runs:

```sql
BEGIN;
INSERT INTO campsite_bookings VALUES (13, 'Rina');
INSERT INTO campsite_bookings VALUES (14, 'Omar');
ROLLBACK;
```

Record the row count after the final statement.

A. 14 — ROLLBACK affects updates but not inserted rows.  
B. 13 — ROLLBACK reverses only the latest insert.  
C. 0 — ROLLBACK restores the table to its state before any historical transaction.  
D. 12 — ROLLBACK undoes everything since BEGIN.

### 8. Seeing your own unfinished work

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation  
**Is Curriculum Based:** No  
**Assessment type:** Self-visibility tracing

A warehouse uses `bin_stock.quantity` for the units physically stored in each bin.

`bin_stock` before the transaction:

| bin_id | quantity |
|---|---:|
| B-4 | 80 |

One session runs:

```sql
BEGIN;
UPDATE bin_stock SET quantity = 65 WHERE bin_id = 'B-4';
SELECT quantity FROM bin_stock WHERE bin_id = 'B-4';
```

Choose the result of that session's SELECT before it commits.

A. 80 — every SELECT uses the last committed value, including the writer's SELECT.  
B. No row — an updated row is hidden until the transaction ends.  
C. 65 — a transaction sees its *own* changes immediately.  
D. The SELECT blocks because the same transaction holds the uncommitted change.

### 9. The order pointing at nobody

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Consistency  
**Is Curriculum Based:** No  
**Assessment type:** FK-enforcement tracing

A marketplace uses `customers.customer_id` to identify registered buyers. `orders.customer_id` is declared as a foreign key to it.

`customers`

| customer_id | name |
|---:|---|
| 81 | Noor |
| 84 | Ishan |

Inside a transaction, the application attempts:

```sql
INSERT INTO orders(order_id, customer_id, total)
VALUES (501, 88, 750);
```

Select the database response supported by the shown rows and constraint.

A. The order is accepted provisionally and the foreign key is checked only when customer 88 is later queried.  
B. The insert fails on the foreign-key constraint.  
C. The database inserts customer 88 automatically, using NULL for the missing customer fields.  
D. The order commits with customer 88 because a transaction temporarily suspends referential checks.

### 10. Durability, in one sentence

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Durability  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

A delivery engineer writes four interpretations of durability in a design review. Select the one the team can safely place in its transaction specification.

A. Once written, a row can never be changed by a later valid transaction.  
B. A transaction is durable only when every table has a second copy.  
C. Durability means concurrent sessions see the same intermediate values.  
D. Once a transaction commits, its changes are permanent.

### 11. Not just for banks

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** What is a Transaction  
**Is Curriculum Based:** No  
**Assessment type:** Scope-of-use reasoning

A junior developer believes transactions "are a banking feature" and skips them in a concert-ticketing app, where booking a seat means: insert the booking, decrement availability, insert an audit row.

Select the response that should replace the junior developer's claim.

A. The junior is right because a failed seat update can be repaired independently of the booking.  
B. Only the availability UPDATE needs a transaction; INSERT statements are already atomic as a group.  
C. Any multi-statement change that must succeed or fail as a whole needs a transaction.  
D. A UNIQUE constraint on the seat makes one transaction around all three statements unnecessary.

### 12. All, or nothing at all

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Atomicity  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

During onboarding, four developers describe what the database promises when several statements share one transaction. Select the description the reviewer should approve as atomicity.

A. A transaction's statements execute as an indivisible unit — all or none.  
B. Every transaction must preserve all declared constraints.  
C. Concurrent transactions must not observe each other's unfinished work in any active session.  
D. A committed transaction must remain after restart.

### 13. From one good state to another

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Consistency  
**Is Curriculum Based:** No  
**Assessment type:** Property statement

A schema review asks what must remain true before and after a successful transaction. Select the statement that captures consistency.

A. Every statement in a transaction takes effect, or none does.  
B. Committed changes remain available after a crash.  
C. Concurrent work behaves as though each transaction were alone, even while their statements overlap in time.  
D. A transaction carries the database from one valid state to another valid state.

### 14. The report that counted phantom money

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation  
**Is Curriculum Based:** No  
**Assessment type:** Correctness-stakes reasoning

A company holds 5,000 across two treasury accounts before a transfer begins.

| account | balance before transfer |
|---|---:|
| Operating | 3000 |
| Reserve | 2000 |

T1 is moving 500 from Operating to Reserve. Its debit has run, its credit has not, and it has not committed. A concurrent report that could read this intermediate state would total 4,500 and trigger a false alarm.

Select the design conclusion supported by this incident.

A. Atomicity alone protects the report because it prevents T1 from having an intermediate state while open.  
B. It protects *correctness*, not just comfort.  
C. Durability protects the report because every UPDATE has already reached persistent storage.  
D. A balance CHECK alone guarantees that a multi-row total cannot observe intermediate work.

### 15. The crash that ate only the unfinished

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Durability  
**Is Curriculum Based:** No  
**Assessment type:** Guarantee-boundary reasoning

At crash time, transaction A had committed and transaction B was still open. After restart, A's changes are present and B's are gone. A trainee calls B's loss "a durability failure."

Select the assessment that respects the exact boundary of durability.

A. The trainee is right because durability begins when the first statement executes.  
B. B should survive because an open transaction is already visible to its own session.  
C. Durability's promise begins at COMMIT — A was covered, B never was.  
D. A should be lost too because recovery must treat all transactions active near the crash alike.

### 16. The undo word

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** What is a Transaction  
**Is Curriculum Based:** No  
**Assessment type:** Missing-statement repair

Halfway through a manual data fix inside an open transaction, a DBA realizes the WHERE clause was wrong. Complete the blank so none of this transaction's changes survives:

```sql
BEGIN;
UPDATE customer_flags SET review_required = true;
____;
```

A. `ROLLBACK`  
B. `COMMIT`  
C. `BEGIN`  
D. `SHOW transaction_isolation`

### 17. More than a manual escape hatch

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Atomicity  
**Is Curriculum Based:** No  
**Assessment type:** Protection-scope reasoning

A developer thinks atomicity "only matters when I type ROLLBACK myself."

Select the additional endings covered by the same all-or-nothing guarantee.

A. Only explicit ROLLBACK; after a crash, durability preserves every statement that had already executed.  
B. A failed statement, but not a crash or lost connection.  
C. A crash, but not a lost client connection.  
D. Involuntary endings too — a crash or a lost connection triggers the same cleanup.

### 18. The rule the database cannot see

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Consistency  
**Is Curriculum Based:** No  
**Assessment type:** Responsibility-boundary judgment

A lending platform's business rule: "a borrower's total exposure across all products must stay under their approved limit" — a rule spanning several tables and a risk formula that no single CHECK constraint can express.

Choose the responsibility model appropriate for this rule.

A. Put the rule in documentation; ACID consistency guarantees documented rules automatically.  
B. Consistency has two guardians: the database and the application share the job.  
C. Replace every table constraint with application checks so responsibility stays in one layer.  
D. Treat the rule as isolation, since reading several tables makes it a concurrency-only concern.

### 19. The in-between world

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** What is a Transaction  
**Is Curriculum Based:** No  
**Assessment type:** State-nature identification

Between BEGIN and COMMIT, a florist's transaction has inserted two delivery rows.

Classify the two rows at this point in the transaction.

A. Permanent, but still hidden from the creating transaction until COMMIT.  
B. Committed for the florist, though other sessions may later reverse them.  
C. Provisional — real to the transaction that made them, invisible to others.  
D. Absent from every read, including reads performed by the creating transaction.

### 20. Three inserts, one stumble

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Atomicity  
**Is Curriculum Based:** No  
**Assessment type:** Multi-statement failure tracing

A payroll system stores one row per employee in `payroll_employees`; `employee_id` is the primary key. The table initially contains employee 300.

```sql
BEGIN;
INSERT INTO payroll_employees VALUES (301, 'Asha');
INSERT INTO payroll_employees VALUES (302, 'Bilal');
INSERT INTO payroll_employees VALUES (300, 'Chen'); -- duplicate key
ROLLBACK;
```

Count how many of the three attempted rows—301, 302, and the duplicate 300—were added by this transaction.

A. Zero — the unit fails as a whole; the two successful inserts are undone.  
B. Two — each successful INSERT commits before the next one begins.  
C. One — ROLLBACK reverses only the statement immediately before the failure.  
D. Three — the duplicate row replaces the earlier employee 300 during recovery.

### 21. The valid-state rulebook

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Consistency  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism identification

A database designer must encode which rows count as valid, rather than leave the rules only in documentation. Select the group of schema features that supplies this rulebook.

A. Indexes, because indexed values are the only values checked at COMMIT.  
B. Views, because every valid state must be exposed through a view.  
C. The transaction log, because logged statements are treated as valid by definition.  
D. Constraints — primary keys, foreign keys, NOT NULL, CHECK rules, and uniqueness.

### 22. Watching the price settle

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation  
**Is Curriculum Based:** No  
**Assessment type:** Commit-visibility sequence tracing

At a fuel depot, `fuel_prices.price` is the current price per litre.

`fuel_prices` before either session starts:

| fuel | price |
|---|---:|
| Diesel | 89 |

T2 uses PostgreSQL's default `READ COMMITTED` isolation level.

| Step | Transaction T1 | Transaction T2 |
|---:|---|---|
| 1 | `BEGIN;` | |
| 2 | Updates Diesel to 92 | |
| 3 | | Reads Diesel → 89 |
| 4 | `COMMIT;` | |
| 5 | | Reads Diesel again |

Complete the observation at step 5.

A. 89 — T2 keeps the value from its first SELECT for every later statement in the session.  
B. 92 — the commit is the visibility switch: the new value becomes what others see.  
C. No row — the commit temporarily hides Diesel while PostgreSQL changes versions.  
D. The SELECT blocks until T2 explicitly starts and commits its own transaction.

### 23. What the promise physically requires

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Durability  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism reasoning

Under PostgreSQL's normal full-durability settings, RAM loses its contents at power-off, yet committed transactions must survive power-off.

Select the action that makes this promise physically possible.

A. Keep the change only in the server process's memory until the next checkpoint.  
B. Make the new row visible to another session, which proves it can survive a crash.  
C. Get a record of the change onto durable storage.  
D. Wait for every open transaction in the database to finish before acknowledging this one.

### 24. The dial that loosens the promise

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Durability  
**Is Curriculum Based:** No  
**Assessment type:** Tradeoff judgment

A telemetry platform ingests millions of low-value sensor pings per hour. It sets `synchronous_commit = off`, allowing COMMIT to acknowledge before the change reaches durable storage. The team accepts that a crash may lose the last moments of acknowledged data in exchange for higher throughput.

Select the accurate engineering assessment.

A. A deliberate trade-off for expendable data.  
B. It preserves the full durability promise because COMMIT was still acknowledged.  
C. It affects visibility only; restart recovery is unchanged.  
D. It makes the whole transaction non-atomic, so partial statements may commit.

### 25. Asking the database how it isolates

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation  
**Is Curriculum Based:** No  
**Assessment type:** Introspection-command selection

An engineer debugging visibility behaviour wants to confirm which isolation level the current session is running under.

How is it checked in PostgreSQL?

A. `SHOW synchronous_commit;` because visibility and disk acknowledgement use the same setting.  
B. `SELECT COUNT(*) FROM open_transactions;` because the count determines the level.  
C. `SHOW transaction_status;` because it reports both level and current transaction state.  
D. `SHOW transaction_isolation;` reports the session's current level.

### 26. Visible is not the same as safe

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Durability  
**Is Curriculum Based:** No  
**Assessment type:** Concept discrimination

A developer argues: "Other sessions can already see my committed row, so it must be durable — visibility proves it's on disk."

Select the correction that separates the two guarantees.

A. Visibility is sufficient evidence of durability because both are controlled by SELECT.  
B. Under normal settings COMMIT provides both, but they remain different promises.  
C. Durability happens before COMMIT, whereas visibility starts only after the next backup.  
D. Isolation guarantees crash survival; durability decides which sessions may read a row.

### 27. The statement that travels alone

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** What is a Transaction  
**Is Curriculum Based:** No  
**Assessment type:** Implicit-transaction reasoning

A dispatcher runs a single UPDATE with no BEGIN or COMMIT around it, and the change persists.

Complete the explanation of why the UPDATE can persist without explicit boundary commands.

A. A single statement bypasses the transaction system because only batches need recovery.  
B. The statement remains provisional until the session eventually issues a manual COMMIT.  
C. The database wrapped it automatically as its own small transaction.  
D. The UPDATE borrowed the most recently committed transaction from another session.

### 28. The mistake atomicity happily commits

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Atomicity  
**Is Curriculum Based:** No  
**Assessment type:** Protection-limit judgment

A payment screen identifies beneficiaries by account ID:

| account_id | beneficiary |
|---|---|
| B17 | Kavya Traders |
| B71 | Kavya Textiles |

The clerk intends B17 but selects B71. The debit and credit of 5,000 both run, the transaction commits, and every declared constraint holds.

Select the conclusion that separates transaction completeness from human intent.

A. Atomicity guarantees completeness, not correctness of intent.  
B. Atomicity failed because it must verify that the chosen beneficiary matches the clerk's intention.  
C. Atomicity guarantees correct beneficiaries only when both account names begin alike.  
D. Atomicity protects intent only for transfers that also violate a declared constraint.

### 29. Minus two seats

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Consistency  
**Is Curriculum Based:** No  
**Assessment type:** Constraint-rejection tracing

`shuttle_runs`

| run_id | seats_left |
|---|---|
| R-7 | 1 |

The table declares `CHECK (seats_left >= 0)`. A transaction tries `UPDATE shuttle_runs SET seats_left = seats_left - 3 WHERE run_id = 'R-7';`

Choose the outcome after the attempted UPDATE.

A. `seats_left` becomes −2 inside the transaction and is corrected automatically at COMMIT.  
B. The UPDATE succeeds because the original value 1 satisfied the CHECK before subtraction.  
C. The UPDATE changes the value to 0 because CHECK rules clamp invalid numeric results.  
D. The statement fails against the CHECK rule — R-7 still shows 1.

### 30. As if each were alone

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation  
**Is Curriculum Based:** No  
**Assessment type:** Property statement

A platform wants concurrent checkouts without letting one checkout observe another's unfinished work. Select the design goal that expresses isolation.

A. Transactions must run one at a time, so concurrency is removed completely.  
B. Concurrent transactions behave as though each had the database to itself.  
C. Concurrent transactions may see unfinished work if each one later commits successfully.  
D. A transaction's rows are stored in a separate table until it finishes.

### 31. The blackout and the boarding pass

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Durability  
**Is Curriculum Based:** No  
**Assessment type:** Guarantee application

Under normal durability settings, a traveller pays for a bus seat; the system commits and the screen shows "Booked." The terminal's power fails moments later.

When systems return, is the seat still booked?

A. Only if the application sends the same booking again after restart.  
B. No — COMMIT makes a booking visible but does not promise restart survival.  
C. Yes — the commit had already made the booking durable.  
D. It depends on whether another traveller queries the seat before recovery completes.

### 32. Where to draw the box

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** What is a Transaction  
**Is Curriculum Based:** No  
**Assessment type:** Boundary-design judgment

A theatre checkout performs: (1) insert the booking, (2) decrement the seat count, (3) insert the payment record — then, separately, (4) send a marketing email.

Draw the transaction boundary around the work that must share one fate.

A. Statements 1–3 inside one transaction; the email (4) stays outside.  
B. Put all four in one database transaction so ROLLBACK can also retract a delivered email.  
C. Give statements 1–3 separate transactions so a payment may remain even if no seat is reserved.  
D. Group only statements 3–4 because payment and marketing communication share the customer's address.

### 33. The failed statement inside the open box

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Atomicity  
**Is Curriculum Based:** No  
**Assessment type:** Error-abort tracing

`race_kits`

| kit_id | runner |
|---|---|
| 1 | Devi |

A volunteer runs:

```sql
BEGIN;
UPDATE race_kits SET runner = 'Devika' WHERE kit_id = 1;
INSERT INTO race_kits VALUES (1, 'Farhan');  -- duplicate key: fails
COMMIT;
```

In PostgreSQL, what is the table's state after the final statement?

A. Kit 1 says Devika because PostgreSQL keeps successful statements before the error.  
B. Kit 1 says Devika and a second kit 1 for Farhan is also stored after COMMIT.  
C. Kit 1 says Farhan because the failed INSERT replaces the row carrying the duplicate key.  
D. Unchanged — kit 1 still says Devi: the failed insert aborted the transaction.

### 34. Consistency wearing a foreign key

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Consistency  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism-to-property mapping

A transaction tries to delete a supplier that 60 purchase orders still reference, and the foreign key blocks it.

Classify what the foreign-key rejection is protecting.

A. It is atomicity: the database rejects every DELETE simply because one statement must be indivisible.  
B. It is consistency in action: the constraint prevents an invalid state.  
C. It is durability: referenced purchase orders must survive every attempted supplier deletion.  
D. It is isolation: the supplier becomes invisible while the purchase orders remain readable.

### 35. Which job needs the box most?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** What is a Transaction  
**Is Curriculum Based:** No  
**Assessment type:** Necessity discrimination

Four jobs at a rental platform:

1. Insert one new property listing.  
2. Read this week's occupancy report.  
3. Move a security deposit: debit the tenant's ledger, credit the escrow ledger.  
4. Update one listing's photo URL.

Select the job that most requires an explicit multi-statement transaction and the reason it does.

A. Job 2 — every read-only report requires BEGIN and COMMIT to produce any result.  
B. Job 1 — all INSERT statements require an explicit transaction even when they stand alone.  
C. Job 3 — it is two statements bound by an invariant.  
D. Job 4 — text values require a transaction boundary that numeric values do not.

### 36. Atomicity, in one sentence

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Atomicity  
**Is Curriculum Based:** No  
**Assessment type:** Definition discrimination

An incident report must tag a half-finished batch with the correct ACID property. Select the guarantee whose violation would allow only some statements in the batch to take effect.

A. All of a transaction's changes take effect, or none do.  
B. A committed batch remains recoverable after power loss.  
C. A successful batch ends in a state satisfying declared constraints.  
D. Concurrent sessions do not observe another transaction's unfinished changes.

### 37. All the rules, all at once

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Consistency  
**Is Curriculum Based:** No  
**Assessment type:** Multi-constraint reasoning

A transaction inserting a warehouse transfer passes the CHECK on quantity (positive), but its `to_warehouse_id` references a warehouse that does not exist.

Does the transaction commit?

A. Yes — satisfying the quantity CHECK compensates for the missing referenced warehouse.  
B. Yes — a foreign key is advisory when another constraint on the row has passed.  
C. Only the positive quantity commits; the warehouse reference is stored as NULL.  
D. No — a valid state means *every* declared rule holds simultaneously.

### 38. The rows that were still there

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation  
**Is Curriculum Based:** No  
**Assessment type:** Uncommitted-delete visibility tracing

An archive's `documents` table contains 1,000 committed rows. Transaction T1 begins and deletes 400 expired documents, but has not committed.

| Step | Transaction T1 | Transaction T2 |
|---:|---|---|
| 1 | `BEGIN;` | |
| 2 | Deletes 400 rows | |
| 3 | No COMMIT yet | Runs `SELECT COUNT(*) FROM documents;` |

Choose T2's result at step 3.

A. 600 — a completed DELETE is visible even while its transaction remains open.  
B. 1,000 — T1's uncommitted deletion is invisible to T2.  
C. No result — every SELECT on the table must wait for T1 to commit or roll back.  
D. 400 — T2 can count only the rows currently being changed by the other transaction.

### 39. What restart day looks like

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Durability  
**Is Curriculum Based:** No  
**Assessment type:** Combined-guarantee application

A parcel hub records scan events in transactions. Its recovery log at the 14:02 crash shows:

| transaction | work | status at crash |
|---|---|---|
| X | insert arrival scan | committed |
| Y | update parcel bay | committed |
| Z | reassign route and add audit row | open after first statement |

Select the state recovery must expose.

A. X and Y's changes are fully present, Z's are fully absent.  
B. X, Y, and Z are all fully present because recovery completes every transaction found in the log.  
C. X, Y, and Z are all absent because a crash restores the state from before the day's work.  
D. X and Y are present, along with Z's first statement because it executed before the crash.

### 40. Name the broken letter

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation  
**Is Curriculum Based:** No  
**Assessment type:** Property-failure classification

Four incidents from four buggy systems:

1. A crash left a transfer's debit applied but not its credit.  
2. A stock quantity of −7 was successfully stored.  
3. A dashboard's total, computed while a transfer was mid-flight, double-counted the moving money.  
4. A committed order vanished after a reboot.

Assign the **isolation** label to the incident it correctly describes.

A. Incident 1 — the transaction ended with only part of its intended work applied.  
B. Incident 2 — a transaction reached a state that violated a declared valid-data rule.  
C. Incident 3 — a concurrent reader observed another transaction's in-progress state.  
D. Incident 4 — a transaction acknowledged as committed did not survive recovery.

---

## Instructor Key

### 1. B

The failure mode is the in-between state becoming final. A transaction removes that possibility by making the two statements one unit: the system can land on "before" or "after," never "half."

### 2. D

Power loss is an involuntary rollback: on restart the uncommitted debit is undone and both balances stand as they began. Option A — the half-applied state — is exactly what atomicity exists to make impossible.

### 3. A

Consistency is enforced through the declared rules, and CHECK (balance >= 0) is such a rule. The invalid target state is refused at the statement; the valid current state survives.

### 4. C

Uncommitted work is private. T2 reads the last committed state — 400 — because isolation makes T1's in-progress change invisible to everyone but T1.

### 5. A

The commit acknowledgment *is* the durability promise taking effect. Whatever happens to the hardware afterwards, recovery restores the committed order.

### 6. B

BEGIN opens the unit of work, the statements run inside it, COMMIT makes their effects permanent together. The other sequences are inventions.

### 7. D

ROLLBACK discards the transaction's provisional work: rows 13 and 14 never became permanent. The table stands at 12, its state as of BEGIN.

### 8. C

Isolation hides work from *others*; the owning transaction sees its own updates at once — otherwise multi-step logic (read what you just changed) would be impossible to write.

### 9. B

Foreign keys are part of the valid-state definition. An order referencing a nonexistent customer is an invalid state, and the constraint stops the transaction at the offending statement.

### 10. D

Durability is the survival promise attached to COMMIT. Options A and B describe immutability and replication — related-sounding, but neither is the guarantee.

### 11. C

The transaction's real subject is invariants, not currency: booking + decrement + audit must move as one. Any domain with multi-statement invariants — seats, stock, appointments — has "money-shaped" problems.

### 12. A

Atomicity is the indivisible, all-or-nothing promise in option A. Options B, C, and D describe consistency, isolation, and durability instead.

### 13. D

Consistency is a bookend guarantee: valid state in, valid state out, with the schema's declared rules as the definition of valid.

### 14. B

The false alarm came from reading a legal-but-in-progress intermediate. Isolation's invisibility rule is what keeps concurrent computation *right*, not merely tidy.

### 15. C

The two properties split cleanly at COMMIT: durability guards what crossed the line; atomicity cleans up what didn't. The observed outcome is both properties working, not either failing.

### 16. A

`ROLLBACK` is the missing command: it discards every change since BEGIN and ends the transaction. `COMMIT` would preserve the unintended mass update instead.

### 17. D

The guarantee is about *any* incomplete ending: crash, dropped connection, failed statement, or explicit ROLLBACK all resolve the same way — unfinished work is undone. The manual command is just one trigger among several.

### 18. B

Constraints can only enforce what they can express. Cross-table business formulas fall to the application's share of the consistency duty — which is why the chapter frames consistency as a partnership, not a database monopoly.

### 19. C

Between BEGIN and COMMIT, changes are real-but-revocable: visible inside, invisible outside, awaiting one of two fates. That provisional zone is what makes ROLLBACK possible at all.

### 20. A

The unit's fate is singular. Two committed inserts beside one failed one would be a partial application of the payroll — the exact outcome the transaction was drawn around to prevent.

### 21. D

Constraints are the codified rulebook: keys, references, presence, ranges, uniqueness. Consistency holds every transaction to this rulebook; indexes and views (A) are machinery, not rules.

### 22. B

Under PostgreSQL's stated `READ COMMITTED` level, each SELECT sees data committed before that statement begins. T2's first SELECT begins before T1's commit and returns 89; its second begins afterwards and returns 92.

### 23. C

The promise must outlive RAM, so its evidence must reach disk before the acknowledgment. That pre-commit durable write is the physical backbone of the D in ACID — and the bridge to write-ahead logging.

### 24. A

The dial is honest engineering: name the data whose tail-seconds are expendable, and buy throughput with precisely that. The same setting under a payments workload would be malpractice — workload decides.

### 25. D

The session simply reports it: `SHOW transaction_isolation;`. Introspection, not archaeology.

### 26. B

Under normal settings, two promises accompany COMMIT: others can see the row and recovery preserves it. The first concerns concurrency; the second concerns durable storage, so visibility alone does not prove durability.

### 27. C

Autocommit closes the model: every statement lives in a transaction, explicit or implicit. BEGIN/COMMIT is the tool for binding *several* statements to one fate, not the price of running any statement at all.

### 28. A

ACID guards the how, not the why. The wrong transfer was complete, valid, isolated, and durable — four properties faithfully serving a human mistake. Intent review belongs to application design, confirmation flows, and audit.

### 29. D

1 − 3 = −2, and −2 fails the CHECK. The statement is refused, the state stands at 1 seat, and the overbooking that the rule exists to prevent never enters the database.

### 30. B

The ideal is *as if alone*: concurrency without interference. One-at-a-time execution (A) would trivially achieve it but is the strawman, not the definition.

### 31. C

The commit preceded the blackout, so the booking was already on the durable side of the line. Recovery's job is to make the restart invisible to committed work — the seat holds.

### 32. A

The box should contain exactly the statements sharing one fate. The email is outside both practically (rollback cannot unsend it) and logically (its failure must not undo a paid booking) — a boundary drawn by consequence, not convenience.

### 33. D

An error inside a PostgreSQL transaction aborts the whole unit; subsequent COMMIT is reported as rollback. The earlier update was part of the aborted unit and dies with it — Devi remains.

### 34. B

The block is the valid-state definition asserting itself mid-delete: no committed state may contain orders that point at nobody. That is consistency, wearing its foreign-key uniform.

### 35. C

Job 3 carries a two-statement invariant — the definition of needing an explicit transaction. Jobs 1 and 4 are single statements already wrapped implicitly; job 2 changes nothing.

### 36. A

Option A is atomicity; B is durability; C is consistency's enforcement; D is isolation. Telling the four apart in one glance is the point of the question.

### 37. D

Validity is conjunctive: all rules at once. One satisfied CHECK cannot offset one violated foreign key — the target state is invalid, and the transaction is refused whole.

### 38. B

An uncommitted delete is as private as an uncommitted update: T2 counts the committed world, so all 1,000 rows remain in its result. Only T1's COMMIT would make the 400 deletions visible to other sessions.

### 39. A

Recovery's contract in one sentence: the last committed state, exactly. X and Y stand (durability); Z is gone without residue (atomicity); "half of Z" (D) is the outcome the two properties jointly forbid.

### 40. C

Incident 3 is a reader observing in-flight work — isolation's failure by definition. Incidents 1, 2, and 4 map to atomicity, consistency, and durability: the four letters, one broken at a time.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Transaction and crash tracing over shown sequences | 2, 4, 5, 7, 8, 20, 22, 29, 33, 38, 39 |
| Definition and property discrimination | 6, 10, 12, 13, 16, 19, 21, 26, 30, 36 |
| Guarantee-boundary and limit judgment | 15, 17, 24, 28, 37 |
| Design and necessity reasoning | 1, 3, 9, 11, 14, 18, 23, 27, 31, 32, 34, 35 |
| Introspection and classification | 25, 40 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| What is a Transaction | 1, 6, 11, 16, 19, 27, 32, 35 | 8 |
| Atomicity | 2, 7, 12, 17, 20, 28, 33, 36 | 8 |
| Consistency | 3, 9, 13, 18, 21, 29, 34, 37 | 8 |
| Isolation | 4, 8, 14, 22, 25, 30, 38, 40 | 8 |
| Durability | 5, 10, 15, 23, 24, 26, 31, 39 | 8 |

Questions 1–10 collectively cover all five Topic 6.1 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (6, 10, 12, 13, 16, 19, 21, 30, 31, 36)
- Intermediate: 26 questions
- Advanced: 4 questions (24, 33, 37, 40)
- Correct option A: 10 questions (3, 5, 12, 16, 20, 24, 28, 32, 36, 39)
- Correct option B: 10 questions (1, 6, 9, 14, 18, 22, 26, 30, 34, 38)
- Correct option C: 10 questions (4, 8, 11, 15, 19, 23, 27, 31, 35, 40)
- Correct option D: 10 questions (2, 7, 10, 13, 17, 21, 25, 29, 33, 37)
- Longest consecutive run of one correct letter: below 3 throughout
