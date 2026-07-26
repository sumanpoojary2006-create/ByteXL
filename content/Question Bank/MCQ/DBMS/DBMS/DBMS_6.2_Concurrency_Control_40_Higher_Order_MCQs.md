# DBMS 6.2: Concurrency Control — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Transactions & Reliability
- **Chapter:** Concurrency Control
- **Scope:** All six Topic 6.2 subtopics in the attached course blueprint (Why Concurrency Control is Needed; Concurrency Problems; Locking; Isolation Levels; Deadlocks; Serializability)
- **SQL dialect:** PostgreSQL
- **Dialect note:** Executable SQL uses PostgreSQL. Concept-classification questions may describe anomalies permitted by other SQL systems; PostgreSQL-specific prevention is stated wherever it affects the answer.
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Questions begin with a recognisable DBMS situation and identify what each table or field represents. Interleaving questions show the starting rows, isolation level when relevant, and both sessions' steps in time order.
- **Evidence rule:** Students never need to invent an unstated starting value, commit status, lock owner, transaction order, or PostgreSQL isolation setting.
- **Scope guard:** Questions use only Topic 6.2 material. Later recovery mechanisms and concurrency features not taught in this chapter are excluded.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all six Topic 6.2 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. One seat, two happy customers

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Why Concurrency Control is Needed  
**Is Curriculum Based:** No  
**Assessment type:** Race tracing

A sleeper-bus database stores the remaining capacity of each service in `bus_services.berths_left`.

| service_id | berths_left |
|---|---:|
| B41 | 1 |

| Step | Clerk X's transaction | Clerk Y's transaction |
|---:|---|---|
| 1 | Reads B41 → 1 | |
| 2 | | Reads B41 → 1 |
| 3 | Writes 0; confirms X | |
| 4 | | Writes 0; confirms Y |

Diagnose the combined outcome.

A. Two confirmations for one berth, caused by interleaved reads and writes.  
B. One valid booking and one rejected booking, because the second read must see zero.  
C. A dirty read, because Y observed X's uncommitted value at step 2.  
D. A deadlock, because both sessions requested the same row during the sequence.

### 2. Acting on money that never existed

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Concurrency Problems  
**Is Curriculum Based:** No  
**Assessment type:** Dirty-read tracing

A training trace from a database system that permits dirty reads shows a loyalty member whose `members.points` balance begins at 2,000.

| Step | Transaction T1 | Transaction T2 |
|---:|---|---|
| 1 | Adds 5,000 → 7,000; no COMMIT | |
| 2 | | Reads 7,000 and issues a voucher |
| 3 | `ROLLBACK;` restores 2,000 | |

Assign the precise anomaly name to T2's observation.

A. A lost update — T2's voucher was overwritten.  
B. A phantom read — new rows appeared.  
C. A dirty read — T2 read uncommitted data that was later rolled back.  
D. A non-repeatable read — T2 read one committed row twice and saw two values.

### 3. Readers together, writers alone

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Locking  
**Is Curriculum Based:** No  
**Assessment type:** Lock-type discrimination

A reporting dashboard and an order updater touch the same exchange-rate row. The architect is documenting which operations may coexist. Select the accurate lock pairing.

A. Shared locks allow one reader only; exclusive locks allow several writers together.  
B. A shared lock lets many read at once; an exclusive lock, one writer, blocks others.  
C. Shared and exclusive locks differ in name but block the same operations.  
D. Shared locks permit writers; exclusive locks restrict only other ordinary readers.

### 4. The four rungs of the ladder

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation Levels  
**Is Curriculum Based:** No  
**Assessment type:** Level enumeration

A platform team arranges the SQL-standard isolation choices on a configuration guide from least protection to greatest protection. Select the correctly ordered row.

A. READ COMMITTED, READ UNCOMMITTED, REPEATABLE READ, SERIALIZABLE  
B. READ UNCOMMITTED, REPEATABLE READ, READ COMMITTED, SERIALIZABLE  
C. READ UNCOMMITTED, READ COMMITTED, SERIALIZABLE, REPEATABLE READ  
D. READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE

### 5. Each holding what the other wants

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Deadlocks  
**Is Curriculum Based:** No  
**Assessment type:** Deadlock-formation tracing

At a payments processor, both transfer transactions need accounts A and B.

| Step | Transaction T1 | Transaction T2 |
|---:|---|---|
| 1 | Locks A | |
| 2 | | Locks B |
| 3 | Requests B; waits for T2 | |
| 4 | | Requests A; waits for T1 |

Classify the wait pattern formed at step 4.

A. A lost update — one debit vanished.  
B. A deadlock — a circular wait, each holding what the other needs.  
C. A dirty read — locks leaked data.  
D. A one-way lock queue in which T1 can finish and release A without T2 acting.

### 6. Equivalent to *some* serial order

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Serializability  
**Is Curriculum Based:** No  
**Assessment type:** Definition interpretation

A reward account starts at 1,000. Transaction T1 adds 100; transaction T2 deducts 40. Their statements overlap, but the final balance is 1,060—the same result produced by running either complete transaction before the other.

Select why this concurrent execution can be described as *serializable*.

A. The outcome matches what some serial ordering would produce.  
B. The transactions must have run without any overlap in real time.  
C. Both transactions used the SERIALIZABLE keyword, regardless of their outcome.  
D. Their statements appeared in account-ID order in the database log.

### 7. Forty tyres, two mechanics, one missing decrement

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Concurrency Problems  
**Is Curriculum Based:** No  
**Assessment type:** Lost-update tracing

A garage stores the available tyre count in `parts.stock`.

| part_id | item | stock |
|---|---|---:|
| T9 | Tyre | 40 |

| Step | Session A | Session B |
|---:|---|---|
| 1 | Reads 40 | |
| 2 | | Reads 40 |
| 3 | Writes 36; commits | |
| 4 | | Writes 34; commits |

Ten tyres physically left the garage. Record the database value and anomaly.

A. 30 — both deductions were preserved as though the sales ran serially.  
B. 36 — the later write was rejected.  
C. 34 — session B's stale write overwrote A's update; a lost update.  
D. 40 — neither write landed.

### 8. The SELECT that stakes a claim

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Locking  
**Is Curriculum Based:** No  
**Assessment type:** FOR-UPDATE mechanism

To stop the tyre incident from recurring, the garage must complete the marked clause so the first sale claims product T9's row before calculating its new stock.

```sql
BEGIN;
SELECT stock FROM parts WHERE part_id = 'T9' ____;
UPDATE parts SET stock = stock - 4 WHERE part_id = 'T9';
COMMIT;
```

Select the clause and its effect.

A. `FOR SHARE`; it prevents every other session from reading T9.  
B. `NOWAIT`; it lets both sessions calculate from 40 without blocking.  
C. `FOR READ`; it converts the following UPDATE into an ordinary read-only SELECT.  
D. `FOR UPDATE`; the read locks T9, so a conflicting second session waits.

### 9. The level that keeps its answers

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation Levels  
**Is Curriculum Based:** No  
**Assessment type:** Level-guarantee identification

An auditor's transaction reads `funds.balance` several times while producing one report. Other sessions may commit updates during the report, but every re-read of the same row must return the auditor's original value.

Choose the least level taught in the chapter that provides this guarantee.

A. REPEATABLE READ — a re-run read returns the same data it saw first.  
B. READ UNCOMMITTED — it reads whatever is newest.  
C. No level can do this.  
D. READ COMMITTED — each statement sees the latest committed value and therefore repeats the first answer.

### 10. Four perfect transactions, one broken outcome

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Why Concurrency Control is Needed  
**Is Curriculum Based:** No  
**Assessment type:** Problem-boundary identification

Each transaction in the berth-overselling incident was individually atomic, consistent with all constraints, and durable — yet the combined result was wrong.

Select the conclusion the engineering team should carry into its repair.

A. Atomicity must be removed so only one booking statement executes.  
B. A non-negative capacity constraint alone coordinates both decisions.  
C. Correct individual transactions aren't enough; interactions are separate.  
D. Durability should be disabled because permanent confirmations caused the conflict.

### 11. Two users, then two thousand

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Why Concurrency Control is Needed  
**Is Curriculum Based:** No  
**Assessment type:** Scale reasoning

A startup's booking app never hit a race condition in its two-user pilot. At launch, 2,000 users arrive.

Select the operational explanation for the changed risk.

A. More rows make every correct UPDATE internally inconsistent.  
B. Rare race windows are struck constantly at scale.  
C. The risk stays identical because transaction interleaving depends only on table size.  
D. PostgreSQL disables transaction isolation after a system reaches 1,000 sessions.

### 12. Same question, two answers, one transaction

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Concurrency Problems  
**Is Curriculum Based:** No  
**Assessment type:** Non-repeatable-read tracing

`products.price` stores the amount currently charged for a product.

| product_id | price before T1 |
|---|---:|
| P8 | 800 |

T1 runs at `READ COMMITTED`.

| Step | Transaction T1 | Transaction T2 |
|---:|---|---|
| 1 | Reads P8 → 800 | |
| 2 | | Updates P8 to 950; commits |
| 3 | Reads P8 again → 950 | |

Assign the precise anomaly name to T1's two answers.

A. A dirty read — 950 was uncommitted.  
B. A deadlock in slow motion.  
C. A lost update — T1 wrote a value that erased T2's committed update.  
D. A non-repeatable read: a value T1 read changed mid-transaction.

### 13. Locking the row, not the room

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Locking  
**Is Curriculum Based:** No  
**Assessment type:** Granularity reasoning

A hotel stores one row per room. T1 holds an exclusive lock on room 204 while T2 updates room 305.

| room_id | status |
|---:|---|
| 204 | Cleaning |
| 305 | Available |

T2 succeeds without waiting. Select the locking principle demonstrated.

A. An exclusive row lock blocks every write to the entire table until T1 ends.  
B. The lock on 204 was released automatically when T2 chose a different room.  
C. Locks are taken at the needed granularity; T1 locked one row only.  
D. PostgreSQL ignores exclusive locks whenever another transaction targets a higher key.

### 14. Requesting stricter rules

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation Levels  
**Is Curriculum Based:** No  
**Assessment type:** Syntax selection

A reconciliation job must keep repeated reads stable. Complete the blank at the start of its transaction:

```sql
BEGIN;
____;
SELECT stock_count FROM inventory WHERE product_id = 1;
COMMIT;
```

A. `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ`  
B. `SHOW transaction_isolation`  
C. `SET TRANSACTION ISOLATION LEVEL READ COMMITTED` for the reconciliation transaction  
D. `SELECT REPEATABLE READ FROM inventory`

### 15. The referee's whistle

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Deadlocks  
**Is Curriculum Based:** No  
**Assessment type:** Resolution-mechanism identification

The two payment transactions from the earlier deadlock cannot both proceed. Left alone, they would wait forever.

What does the database actually do?

A. Leaves both sessions waiting until one application's connection times out.  
B. It detects the cycle, aborts one transaction as the victim.  
C. Releases one requested lock while preserving all of that transaction's earlier changes.  
D. Commits both transactions up to their waiting statements and discards the remainder.

### 16. The gold standard is not on the menu

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Serializability  
**Is Curriculum Based:** No  
**Assessment type:** Concept-role discrimination

The chapter calls serializability "the target, not a setting."

What does that framing mean?

A. Serializability names the syntax used to lock one individual row.  
B. Serializability is one anomaly that weaker isolation levels deliberately permit.  
C. Serializability applies only when transactions actually execute one after another.  
D. Serializability is the standard every isolation level is measured against.

### 17. Where the danger actually lives

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Why Concurrency Control is Needed  
**Is Curriculum Based:** No  
**Assessment type:** Risk-source identification

Two sessions each run correct SQL against the same rows at the same time.

Where does the danger come from?

A. Each SQL statement becomes incorrect merely because another session exists.  
B. The two sessions use different transaction IDs for otherwise identical statements.  
C. The interleaving of the two sessions' steps produces combined outcomes.  
D. The database makes committed writes temporary whenever two users access one table.

### 18. The count that grew between glances

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Concurrency Problems  
**Is Curriculum Based:** No  
**Assessment type:** Phantom-read discrimination

A compliance transaction runs at `READ COMMITTED` and uses the predicate `amount > 1000000` to count high-value trades.

| Step | Transaction T1 | Transaction T2 |
|---:|---|---|
| 1 | Runs COUNT → 14 | |
| 2 | | Inserts two 2-million trades; commits |
| 3 | Re-runs identical COUNT → 16 | |

No existing row changed. Diagnose why the result set grew.

A. A phantom read: the set of matching rows changed, not a value.  
B. A non-repeatable read: one of the original 14 rows changed its amount.  
C. A dirty read — the inserts were uncommitted.  
D. A lost update — the count overwrote itself.

### 19. Waiting its turn

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Locking  
**Is Curriculum Based:** No  
**Assessment type:** Block-behaviour identification

T1 holds an exclusive lock on a courier's row. T2 issues an UPDATE against that same row.

What happens to T2?

A. T2 calculates its update immediately, then silently discards the result at COMMIT.  
B. T2's statement waits until T1's lock releases.  
C. T2 receives an immediate error.  
D. T2 writes a private copy that later replaces T1's row without conflict checking.

### 20. What the default does and doesn't stop

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation Levels  
**Is Curriculum Based:** No  
**Assessment type:** Level-boundary identification

PostgreSQL sessions run at READ COMMITTED unless told otherwise.

Choose the accurate boundary of the default level.

A. Prevents dirty and non-repeatable reads, but permits phantom reads between statements.  
B. Prevents non-repeatable reads, but permits dirty and phantom reads.  
C. Prevents deadlocks, but permits every read anomaly in the standard.  
D. Prevents dirty reads; non-repeatable and phantom reads can still occur.

### 21. Everyone reaches for A before B

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Deadlocks  
**Is Curriculum Based:** No  
**Assessment type:** Prevention-pattern reasoning

After repeated transfer deadlocks, the payments team compares two lock sequences:

| transfer | Current order | Proposed order |
|---|---|---|
| 17 → 42 | 17, then 42 | 17, then 42 |
| 42 → 17 | 42, then 17 | 17, then 42 |

Select why the proposed order is the smallest effective repair.

A. Ascending keys make each UPDATE atomic even without a transaction.  
B. The proposal removes one of the two required row locks from each transfer.  
C. The circular wait can't form; both take account 17 first.  
D. The proposal guarantees both transfers commit simultaneously without either waiting.

### 22. The result no serial world allows

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Serializability  
**Is Curriculum Based:** No  
**Assessment type:** Serializability testing

`parking_lots.spots_left` begins at 1. T1 and T2 each check availability and create a confirmed booking when the value they read is positive. The concurrent execution ends with two confirmations.

Test the result against both possible serial orders.

A. No serial ordering could produce two bookings for one spot.  
B. The result matches T1 then T2 because the second serial transaction would still read one.  
C. The result is serializable whenever both transactions individually commit successfully.  
D. Exact timestamps, rather than possible serial outcomes, determine serializability.

### 23. The gap ACID left open

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Why Concurrency Control is Needed  
**Is Curriculum Based:** No  
**Assessment type:** Property-gap analysis

In the tyre incident, both sessions' transactions were atomic (fully applied), consistent (stock stayed non-negative), and durable. Yet four tyres vanished from the books.

Which gap did the incident fall through?

A. Durability — the writes evaporated.  
B. Coordination between transactions — the anomaly was in their interleaving.  
C. Atomicity — one write half-applied.  
D. Consistency, because a non-negative CHECK must detect every stale calculation.

### 24. Four incidents, four names

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Concurrency Problems  
**Is Curriculum Based:** No  
**Assessment type:** Anomaly classification

Four incidents at a trading firm:

1. A report used a figure from a transaction that later rolled back.  
2. Two clerks' balance updates collided; one silently vanished.  
3. A transaction re-read a bond's price mid-flight and got a different number.  
4. A twice-run "positions over 1M" query found *new rows* the second time.

Which incident is the **phantom read**?

A. Incident 1 — a transaction consumed another transaction's uncommitted figure.  
B. Incident 2 — the vanished update.  
C. Incident 3 — the changed price.  
D. Incident 4 — the matching set gained members between queries.

### 25. Reading side by side

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Locking  
**Is Curriculum Based:** No  
**Assessment type:** Shared-lock behaviour

Five analysts' read-only transactions all take shared locks on the same exchange-rate row at once.

What happens?

A. One analyst reads while the remaining four wait for that shared lock to release.  
B. The first shared lock is upgraded to exclusive because five readers requested it.  
C. All five read concurrently; shared locks coexist without conflict.  
D. Every reader receives an error because shared locks conflict with other shared locks.

### 26. Why the strictest level isn't the default

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation Levels  
**Is Curriculum Based:** No  
**Assessment type:** Cost-benefit judgment

A cautious lead proposes running *every* transaction at SERIALIZABLE, "since it's the safest."

What is the chapter's counterweight?

A. Safety has a price: conflicting SERIALIZABLE work may abort and require retry, reducing throughput.  
B. SERIALIZABLE prevents dirty reads but permits every other anomaly listed in the chapter.  
C. SERIALIZABLE changes only read-only transactions, so write-heavy workloads gain no protection under load.  
D. SERIALIZABLE eliminates waiting and retries, but requires more storage for each transaction.

### 27. The error worth retrying

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Deadlocks  
**Is Curriculum Based:** No  
**Assessment type:** Application-response reasoning

A checkout service occasionally receives "deadlock detected" — its transaction was chosen as the victim.

What is the correct application response?

A. Retry only the statement that was waiting, then commit the victim transaction's earlier work.  
B. Catch the error and retry the whole transaction from scratch.  
C. Treat the deadlock message as success because the other transaction was allowed to continue.  
D. Reconnect and issue COMMIT for the transaction the database already rolled back.

### 28. What the standard buys

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Serializability  
**Is Curriculum Based:** No  
**Assessment type:** Benefit identification

Suppose every execution in a system is guaranteed serializable.

What does that guarantee buy the developers?

A. Every transaction completes without waiting, aborting, or retrying.  
B. Every interleaving produces one fixed result, regardless of transaction order.  
C. The database can reconstruct missing WHERE clauses from transaction intent.  
D. They can reason about correctness one transaction at a time.

### 29. Which workload needs the referee?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Why Concurrency Control is Needed  
**Is Curriculum Based:** No  
**Assessment type:** Contention discrimination

Two systems at a media company:

1. A read-only archive of past broadcasts, queried by many, written by none.  
2. A live ad-slot counter that hundreds of sales sessions decrement simultaneously.

Where does concurrency control earn its keep, and why?

A. System 1 — concurrent readers overwrite each other's archived rows.  
B. Both equally — read-only access creates the same write collision as repeated decrements.  
C. System 2 — many writers on the same rows is where collisions happen.  
D. Neither — transaction interleaving cannot affect a value stored in an integer column.

### 30. The voucher that should never have printed

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Concurrency Problems  
**Is Curriculum Based:** No  
**Assessment type:** Symptom-to-anomaly classification

A cross-platform post-mortem from a system that permits reading uncommitted data finds: "the cashback engine read a deposit that was still uncommitted; the depositing transaction later rolled back, but the cashback had already been issued."

Which anomaly does the post-mortem describe, and what made it possible?

A. A dirty read — the engine saw another transaction's uncommitted write.  
B. A phantom read — the engine repeated a filtered query and gained committed rows.  
C. A deadlock — each transaction waited for a lock held by the other.  
D. A non-repeatable read — one transaction read the same committed value twice.

### 31. When the lock lets go

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Locking  
**Is Curriculum Based:** No  
**Assessment type:** Lock-lifetime identification

T1 updates a row (acquiring its exclusive lock) and then continues with other statements in the same open transaction.

When does that row lock release?

A. Immediately after the UPDATE statement finishes, even though T1 remains open.  
B. When T1 ends, at COMMIT or ROLLBACK, and not before; locks live that long.  
C. When T1 begins its next SQL statement inside the same transaction.  
D. When another transaction first requests the row and needs the lock.

### 32. The re-read that stayed put

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation Levels  
**Is Curriculum Based:** No  
**Assessment type:** REPEATABLE-READ tracing

A stocktake reads the number of bins recorded for warehouse W. T1 runs at `REPEATABLE READ`.

| Step | Transaction T1 | Transaction T2 |
|---:|---|---|
| 1 | Reads W → 100 | |
| 2 | | Updates W to 120; commits |
| 3 | Reads W again | |

Complete T1's step-3 result.

A. No row, because T2's commit invalidates T1's earlier snapshot.  
B. 120, because every committed update replaces T1's transaction snapshot.  
C. An error, because REPEATABLE READ forbids concurrent sessions from updating the row.  
D. 100 — REPEATABLE READ holds T1 to its starting data snapshot.

### 33. Find the fatal move

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Deadlocks  
**Is Curriculum Based:** No  
**Assessment type:** Cycle-point identification

A warehouse system's timeline:

1. T1 locks the `pallets` row P-9.  
2. T2 locks the `bays` row B-2.  
3. T1 requests B-2 and begins waiting.  
4. T2 requests P-9.

At which step does the deadlock actually come into existence, and why not earlier?

A. Step 2 — holding different locks already creates a circular wait.  
B. Step 1 — the first exclusive lock is itself a deadlock.  
C. Step 4 — the crossed request closes the circle, forming mutual wait.  
D. At COMMIT — PostgreSQL checks for wait cycles only when transactions finish.

### 34. Interleaved, yet innocent

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Serializability  
**Is Curriculum Based:** No  
**Assessment type:** Equivalence application

T1 updates courier fees; T2 totals invoice amounts. Their steps interleaved heavily in time — yet the final state and both results match exactly what running T1 completely, then T2 completely, would have produced.

How is this execution classified?

A. Serializable — equivalence to some serial order is the whole test.  
B. Non-serializable, because any overlap disqualifies an execution regardless of outcome.  
C. A dirty execution, because interleaved statements necessarily read uncommitted values.  
D. Unclassifiable, because serializability can be tested only from the physical lock log.

### 35. The window between look and leap

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Why Concurrency Control is Needed  
**Is Curriculum Based:** No  
**Assessment type:** Race-window identification

Every incident in this chapter's opening — the double-booking, the tyre loss — shares one structural feature.

Select the shared structural defect.

A. Both operations relied on a constraint to serialize their application decisions.  
B. A gap between reading a value and writing a decision based on it.  
C. Each operation used a single atomic arithmetic UPDATE with no preceding read.  
D. Both incidents required one transaction to read another's uncommitted value.

### 36. Name that anomaly — precisely

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Concurrency Problems  
**Is Curriculum Based:** No  
**Assessment type:** Fine-grained discrimination

Two bug tickets:

- Ticket 1: "My transaction read row R twice and got different values; the other transaction's change was committed."  
- Ticket 2: "My transaction and another both read row R, then both wrote it; my colleague's write disappeared."

Which classification is correct?

A. Ticket 1 is a dirty read; Ticket 2 is a non-repeatable read in both transactions.  
B. Ticket 1 is a lost update; Ticket 2 is a phantom read.  
C. Ticket 1 is a phantom read; Ticket 2 is a deadlock.  
D. Ticket 1 is a non-repeatable read; ticket 2 is a lost update.

### 37. One lock, one buyer, zero oversells

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Locking  
**Is Curriculum Based:** No  
**Assessment type:** FOR-UPDATE sequence tracing

The parking app is rebuilt. One spot remains (`spots_left = 1`), and both sessions use PostgreSQL's default `READ COMMITTED` level:

1. T1: `BEGIN; SELECT spots_left FROM lots WHERE lot_id = 7 FOR UPDATE;` → 1, row locked  
2. T2: issues the identical FOR UPDATE select — and blocks  
3. T1: books, sets `spots_left = 0`, COMMITs  
4. T2: unblocks, its SELECT now returns…

What does T2 see, and what is the outcome?

A. 1 — T2 evaluated the SELECT when it was issued, before waiting for T1's COMMIT.  
B. No row — changing `spots_left` to zero deletes the locked lot row.  
C. 0 — T2's read waited out T1, sees committed truth, declines it.  
D. A deadlock error — any two `FOR UPDATE` requests for one row form a wait cycle.

### 38. Proving the trade-off at the keyboard

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Isolation Levels  
**Is Curriculum Based:** No  
**Assessment type:** Experimental-verification reasoning

An engineer compares two otherwise identical two-terminal runs:

| Run | T1 level | First read | T2 action | T1 second read |
|---|---|---:|---|---:|
| A | READ COMMITTED | 50 | Commits 40 | 40 |
| B | REPEATABLE READ | 50 | Commits 40 | 50 |

Choose the conclusion directly supported by the comparison.

A. That isolation levels are real, observable behaviour switches.  
B. That T2 failed to commit in Run B, because otherwise T1 would have to read 40.  
C. That READ COMMITTED permits dirty reads, since T1's second result changed.  
D. That REPEATABLE READ blocks every concurrent UPDATE until T1 commits.

### 39. Deadlock, in one honest sentence

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Deadlocks  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

A support engineer must distinguish a deadlock from an ordinary slow statement. Select the description that justifies a deadlock diagnosis.

A. One transaction waits behind a lock whose holder can continue and eventually commit.  
B. Two or more transactions each waiting for a lock the other holds.  
C. One transaction performs a long calculation before requesting any lock.  
D. Two transactions read the same row concurrently without requesting conflicting locks.

### 40. The chapter, assembled

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Serializability  
**Is Curriculum Based:** No  
**Assessment type:** Integrated synthesis

An architect must map the chapter's standard, configurable trade-off, and enforcement mechanism. Select the accurate mapping.

A. Locking is the correctness standard; serializability is one optional row-lock command used in every workload.  
B. Isolation levels define four storage engines, each with a separate transaction log.  
C. Serializability removes the need for locks, waiting, deadlock detection, and retries.  
D. Serializability is the standard; levels trade protection for concurrency; locks enforce it.

---

## Instructor Key

### 1. A

Neither clerk did anything wrong in isolation; the oversell lives entirely in the interleaving — both reads landed before either write. Coordinating exactly such sequences is concurrency control's founding problem.

### 2. C

T2 consumed a value that was never committed and was later revoked. Acting on provisional data that officially never existed is the dirty read — the anomaly that even the default isolation level exists to prevent.

### 3. B

Reading is compatible with reading, so shared locks stack; writing is compatible with nothing, so the exclusive lock stands alone. The pairing is the basis of every finer rule in the chapter.

### 4. D

The SQL-standard ladder is READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE. PostgreSQL accepts all four names but treats READ UNCOMMITTED like READ COMMITTED, so it has three distinct behaviours in practice.

### 5. B

Step 4 closes the circle: T1 waits on T2's lock while T2 waits on T1's. Mutual crossed waiting is the deadlock signature — and it is stable: no timeout of politeness resolves it.

### 6. A

Serializability judges outcomes, not timing: interleaving is fine so long as the result matches *some* serial arrangement. Actually running serially (B) is one way to be serializable, not the definition.

### 7. C

B computed 34 from a reading taken before A's write, so committing it erased A's decrement — 40 became 34 when it should be 30. The silent overwrite of a concurrent update is the lost update, and the books are now four tyres wrong.

### 8. D

FOR UPDATE moves the lock to the *read* — the front of the read-modify-write sequence. A second session issuing the same `FOR UPDATE` read must wait until the first finishes, so its computation starts from a fresh committed value.

### 9. A

Stable answers within one transaction is REPEATABLE READ's defining offer. The default (D) refreshes to the latest committed state per statement — exactly what the auditor must not see.

### 10. C

ACID governs each transaction; the oversell happened *between* transactions. The four letters were all honoured, and the result was still wrong — which is why interleaving control is its own discipline.

### 11. B

The race window's width never changed; the traffic through it did. Rare coincidence at two users becomes steady collision at thousands — scale converts "possible" into "daily."

### 12. D

The value T1 had already read changed under it, courtesy of a committed concurrent update. That is the non-repeatable read: legal at READ COMMITTED, eliminated at REPEATABLE READ.

### 13. C

Locking is deliberately narrow: one contested row, not the whole table. T2's instant success on another row is the design working — protection where needed, concurrency everywhere else.

### 14. A

The missing command is `SET TRANSACTION ISOLATION LEVEL REPEATABLE READ`, placed before the transaction's first query. `SHOW` only reports a level, while READ COMMITTED would retain the default behaviour the job is trying to strengthen.

### 15. B

Databases resolve deadlocks by execution: detect the cycle, abort a victim, free its locks. The victim's error is not a malfunction — it is the referee's whistle.

### 16. D

The standard/settings distinction: serializability defines *correct*; the levels are purchasable distances from it. Naming the trade-off is what lets teams choose it deliberately rather than inherit it unknowingly.

### 17. C

Each session's steps were individually fine; the weave was not. Concurrency bugs are properties of orderings — which is why they are invisible in single-user testing and why control must target the interleaving itself.

### 18. A

No row changed value; the *membership* of the matching set changed. Phantoms are arrivals and departures, non-repeatable reads are renovations — the distinction matters because stricter machinery is needed to fence a set than a row.

### 19. B

Exclusive locks make later writers queue, not fail: T2 blocks until the lock frees, then applies its update to the settled row. Waiting is the default texture of lock conflicts.

### 20. D

READ COMMITTED's line: nothing uncommitted is ever visible (no dirty reads), but each statement sees the newest committed world — so values may change between reads (non-repeatable) and sets may gain rows (phantoms).

### 21. C

Deadlock needs a cycle, and a cycle needs crossed acquisition orders. One global order makes crossing impossible: contention becomes a queue at the first common lock, and queues clear.

### 22. A

The serial-outcome set for one spot contains only "one booking succeeds." An execution that lands outside the set of all serial outcomes is, by definition, not equivalent to any serial order — the double booking is the violation made visible.

### 23. B

The failure lived in the interleaving between two otherwise complete transactions. Hiding uncommitted data was not enough; the read-decide-write sequences needed coordination through locking or an appropriate isolation strategy.

### 24. D

Incident 4 is the set changing between identical queries — the phantom. The other three are the chapter's remaining rogues' gallery in order: dirty read, lost update, non-repeatable read.

### 25. C

Shared locks coexist: five readers, five simultaneous grants, zero queueing. The queue begins only when a writer's exclusive request arrives.

### 26. A

SERIALIZABLE's protection is bought with aborts and retries and reduced parallelism. For workloads whose transactions genuinely collide, the price is right; for those that never touch the same rows, it is pure overhead — level choice is workload analysis.

### 27. B

Deadlock victims are cleanly rolled back, and the conflict that killed them is gone by the time they retry. Catch, retry, succeed is the standard pattern — the error is a routing instruction, not a disaster report.

### 28. D

Serializability collapses the reasoning problem: prove each transaction correct alone, and concurrency adds no new outcomes to check. Without it, correctness would require reasoning about every possible interleaving — an explosion no team can audit.

### 29. C

Contention is writers converging on the same data: hundreds of sessions read-modify-writing one counter. Pure concurrent readers (system 1) interleave harmlessly — there is nothing their orderings can corrupt.

### 30. A

"Read a deposit that was still uncommitted" is the dirty read verbatim. The enabling condition was visibility of uncommitted work — which READ COMMITTED and every stricter level rule out.

### 31. B

Locks are transaction-scoped: acquired as needed, held to the end, released at COMMIT/ROLLBACK. This is also the practical argument for keeping transactions short.

### 32. D

REPEATABLE READ pins T1 to its opening snapshot: 100 the first time, 100 every time, regardless of concurrent commits. The parenthetical contrast with READ COMMITTED is the two-level experiment in miniature.

### 33. C

Deadlock is a *cycle*, and the cycle completes only at step 4: T2's crossed request while T1 already waits. Everything before is ordinary lock traffic that could still have drained normally.

### 34. A

The test is outcome equivalence, not step choreography. This execution's results sit exactly on "T1 then T2," so it is serializable — heavy interleaving and all.

### 35. B

Every opening incident is the same shape: look, then leap, with an unguarded gap between. Concurrency control's various tools — locks, FOR UPDATE, stricter levels — are all ways of sealing that gap.

### 36. D

Ticket 1: same row, two reads, committed change between — non-repeatable read. Ticket 2: concurrent read-modify-write, one write silently gone — lost update. Precise names matter because the fixes differ (snapshot isolation versus locking the read).

### 37. C

T2's blocked SELECT resumed *after* T1's commit and read 0 — the decision logic then declines cleanly. The lock forced the two look-then-leap sequences into single file; with the read serialized, the oversell has no path to exist.

### 38. A

The experiment shows the levels as behaviour, not doctrine: identical interleaving, different outcome, switched by one setting. That observability is what makes isolation levels an engineering choice rather than folklore.

### 39. B

The definition needs a wait cycle: each transaction is blocked by a lock held by another member of the cycle. A one-way queue can drain normally, while concurrent non-conflicting reads do not create a wait at all.

### 40. D

Three layers, correctly stacked: the standard (serializability) defines correct; the levels price the distance from it; the mechanisms (locks and friends) enforce whichever position is chosen. The chapter in one sentence.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Interleaving, state, and wait tracing | 1, 2, 5, 7, 12, 18, 22, 32, 33, 37 |
| Anomaly classification and discrimination | 24, 30, 36 |
| Missing SQL and smallest-repair selection | 8, 14, 21, 27 |
| Lock mechanics and behaviour | 3, 13, 19, 25, 31 |
| Level guarantees, comparisons, and trade-offs | 4, 9, 20, 26, 38 |
| Deadlock formation, resolution, and prevention | 15, 39 |
| Serializability and synthesis | 6, 16, 28, 34, 40 |
| Necessity and boundary reasoning | 10, 11, 17, 23, 29, 35 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| Why Concurrency Control is Needed | 1, 10, 11, 17, 23, 29, 35 | 7 |
| Concurrency Problems | 2, 7, 12, 18, 24, 30, 36 | 7 |
| Locking | 3, 8, 13, 19, 25, 31, 37 | 7 |
| Isolation Levels | 4, 9, 14, 20, 26, 32, 38 | 7 |
| Deadlocks | 5, 15, 21, 27, 33, 39 | 6 |
| Serializability | 6, 16, 22, 28, 34, 40 | 6 |

Questions 1–10 collectively cover all six Topic 6.2 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (3, 4, 10, 11, 17, 19, 25, 28, 31, 39)
- Intermediate: 24 questions
- Advanced: 6 questions (22, 24, 33, 36, 37, 40)
- Correct option A: 10 questions (1, 6, 9, 14, 18, 22, 26, 30, 34, 38)
- Correct option B: 10 questions (3, 5, 11, 15, 19, 23, 27, 31, 35, 39)
- Correct option C: 10 questions (2, 7, 10, 13, 17, 21, 25, 29, 33, 37)
- Correct option D: 10 questions (4, 8, 12, 16, 20, 24, 28, 32, 36, 40)
- Longest consecutive run of one correct letter: below 3 throughout
