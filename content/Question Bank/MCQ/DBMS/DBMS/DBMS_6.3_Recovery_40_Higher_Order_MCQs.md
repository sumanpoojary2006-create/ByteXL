# DBMS 6.3: Recovery — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Transactions & Reliability
- **Chapter:** Recovery
- **Scope:** All five Topic 6.3 subtopics in the attached course blueprint (Database Failures; Write-Ahead Logging; Checkpoints; Undo and Redo; Transactions in Application Code)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every question begins with a recognisable database or application situation and identifies what each field, log entry, or recovery status means.
- **Evidence rule:** Recovery traces explicitly show transaction commit status, whether WAL is durable, whether the data page reached disk, the latest checkpoint, and the exact crash point whenever those facts determine the answer.
- **Scope guard:** Questions use only Topic 6.3 material. Detailed backup procedures, point-in-time recovery commands, replication administration, and recovery algorithms beyond the taught redo-then-undo model are excluded.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all five Topic 6.3 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Three bad days, three different sizes

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Database Failures  
**Is Curriculum Based:** No  
**Assessment type:** Failure classification

Three incidents at a logistics firm:

| incident | observed scope |
|---:|---|
| 1 | One booking hits a constraint violation and aborts; other sessions continue |
| 2 | A power cut wipes server memory; the disks remain healthy |
| 3 | A storage array fails and destroys its data files |

Match each incident to the scope the recovery team must handle.

A. 1: transaction failure; 2 and 3: system crashes because both stop normal processing.  
B. 1: system crash; 2: media failure; 3: transaction failure.  
C. 1: transaction failure; 2: system crash; 3: media failure — ascending severity.  
D. 1 and 2: transaction failures; 3: system crash because only the server was damaged.

### 2. The rule in three words

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Write-Ahead Logging  
**Is Curriculum Based:** No  
**Assessment type:** Rule statement

A storage engineer compares four proposed physical write orders for an UPDATE.

Select the order required by write-ahead logging.

A. Data before log — flush the changed page, then record what the page now contains.  
B. Log before data — the log record reaches disk before the data pages.  
C. Commit before log — acknowledge the transaction, then create its recovery record.  
D. Either order — recovery works as long as both writes eventually reach the same disk.

### 3. Why the replay has a starting line

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Checkpoints  
**Is Curriculum Based:** No  
**Assessment type:** Purpose reasoning

A database has run for months:

| recovery marker | WAL position |
|---|---|
| Latest completed checkpoint | L900 |
| Crash point | L960 |

Choose the recovery starting point and the reason for it.

A. Start at the beginning of the database history because every old record must be replayed.  
B. Start at L960 because recovery examines only the record written at the crash point.  
C. Skip WAL entirely because a completed checkpoint makes later logging unnecessary.  
D. Start from L900 because earlier logged changes are guaranteed to be in the data files.

### 4. The committed change that hadn't landed

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Undo and Redo  
**Is Curriculum Based:** No  
**Assessment type:** Redo identification

At crash time, the recovery inventory contains:

| transaction | commit record durable? | updated data page on disk? |
|---|---|---|
| Toll payment T8 | Yes | No |

Assign the required recovery action to T8.

A. Redo — the log record replays into data files as committed.  
B. Undo — the absent data-page write proves the transaction never committed.  
C. Ignore it — recovery trusts the data file more than a durable commit record.  
D. Roll back T8 and ask the application to issue the payment again after startup.

### 5. The commit nobody typed

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Transactions in Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Auto-commit identification

A maintenance script runs:

```sql
UPDATE branches SET open = false WHERE branch_id = 10;
UPDATE branches SET open = false WHERE branch_id = 20;
UPDATE branches SET open = false WHERE branch_id = 30;
```

The client is using its default auto-commit mode, and no explicit `BEGIN` appears.

Select the transaction boundary the client effectively used.

A. All three statements bypassed transaction processing and wrote directly to table files.  
B. The client kept one implicit transaction open until the connection closed.  
C. PostgreSQL grouped the statements because they target the same table.  
D. Auto-commit: each standalone statement runs as its own transaction.

### 6. Why the names matter

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Database Failures  
**Is Curriculum Based:** No  
**Assessment type:** Distinction rationale

A trainee asks why the chapter bothers distinguishing transaction failure, system crash, and media failure.

Select the response that connects each scope to its appropriate defence.

A. All three begin by restoring a full backup, even when only one transaction failed.  
B. All three are handled by replaying local WAL, including destroyed storage media.  
C. Each failure size has its own remedy: rollback, recovery, or backups.  
D. The only meaningful difference is how long the database remains unavailable.

### 7. Why writing the tables directly isn't enough

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Write-Ahead Logging  
**Is Curriculum Based:** No  
**Assessment type:** Necessity reasoning

A storage design proposes writing changed pages directly to scattered data-file locations and keeping no durable change log.

Identify the failure window this design cannot repair reliably.

A. A crash mid-write leaves torn pages; the log records what happened.  
B. The design prevents SELECT statements from reading a page until the next checkpoint.  
C. The design guarantees every data page is atomic, but makes INSERT statements slower.  
D. The design is equally recoverable because the partly written page describes its own missing bytes.

### 8. Which team plays first

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Undo and Redo  
**Is Curriculum Based:** No  
**Assessment type:** Ordering rationale

After a crash, the log since the checkpoint contains committed and uncommitted changes, while the data files contain only some of those changes.

Select the recovery order and rationale taught in the chapter.

A. Undo first removes open transactions; redo then reapplies every log record, including those just undone.  
B. Redo first rebuilds from the log; undo reverses what never committed.  
C. Either order produces the same state without examining commit records.  
D. Redo and undo run only for media failure, not for an ordinary system crash.

### 9. What the checkpoint actually does

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Checkpoints  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism identification

At 14:00, PostgreSQL executes `CHECKPOINT;` after several committed updates have left dirty pages in memory.

Choose the effect that creates a dependable recovery starting line.

A. Copying the entire database to independent backup media.  
B. Deleting WAL records immediately, including records after 14:00.  
C. Flushing dirty pages from memory to disk, a sync point.  
D. Marking every open transaction as committed before flushing its pages.

### 10. Drawing the box in code

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Transactions in Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Pattern selection

An app's refund routine must insert a refund row and update the order's status as one unit. Complete the error branch:

```text
begin()
try:
    insert_refund()
    mark_order_refunded()
    commit()
except error:
    ________
```

A. `rollback()` so neither statement remains after a failure  
B. `commit()` so the successful statement is preserved  
C. `insert_refund()` so only the first statement is retried  
D. `begin()` so the failed transaction is nested inside a new one

### 11. The smallest failure of all

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Database Failures  
**Is Curriculum Based:** No  
**Assessment type:** Scope identification

A single order transaction at a florist aborts on a deadlock while two hundred other sessions carry on untouched.

What characterizes this *transaction failure*?

A. Crash recovery must replay WAL for every transaction on the server.  
B. The data files and local log must be restored from another machine.  
C. Every session must roll back because one deadlock victim was selected.  
D. Its blast radius is one transaction, rolled back automatically.

### 12. What one log record holds

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Write-Ahead Logging  
**Is Curriculum Based:** No  
**Assessment type:** Content identification

Recovery must be able to re-apply a change (redo) or reverse it (undo) from the log alone.

What must the log therefore record about each change?

A. Only the SQL command name, without the affected row or its values.  
B. Enough to reconstruct the change either way, replay or restore.  
C. Only the final table state after every transaction in the server commits.  
D. Only the user's original SQL text, regardless of what rows it actually changed.

### 13. Nobody schedules them by hand

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Checkpoints  
**Is Curriculum Based:** No  
**Assessment type:** Automation rationale

A new DBA asks when they are supposed to run checkpoints.

What is the answer?

A. The database schedules them itself, automatically, based on time or WAL activity.  
B. The DBA must issue `CHECKPOINT` after every individual committed transaction.  
C. They run only after an unclean shutdown, immediately before recovery begins.  
D. One checkpoint is created when PostgreSQL is installed and reused indefinitely for all later restarts.

### 14. The insert that never finished

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Undo and Redo  
**Is Curriculum Based:** No  
**Assessment type:** Undo identification

At crash time, a hotel's rate-change transaction was still open — never committed.

What does recovery do with its changes?

A. Redo preserves them because every logged UPDATE is treated as committed.  
B. Recovery leaves any on-disk portion and discards only changes still in memory.  
C. Undo reverses the uncommitted transaction's changes, like a rollback.  
D. Recovery waits for the disconnected hotel application to choose COMMIT or ROLLBACK.

### 15. Safe to try again

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Transactions in Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Retry-safety reasoning

A parcel app's transaction fails mid-way with a deadlock error, and the code catches it.

Why is simply re-running the *whole transaction* a safe response?

A. The database remembers the application's intent and suppresses every statement in the retry.  
B. Only the statement that encountered the deadlock was reversed; earlier statements remain committed.  
C. The retry resumes after the failed statement because the error contains a continuation point.  
D. The failed attempt was rolled back completely; no residue remains.

### 16. Everything in memory, gone at once

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Database Failures  
**Is Curriculum Based:** No  
**Assessment type:** System-crash characterization

A kernel panic reboots a database server. RAM's contents — caches, in-flight work, unwritten pages — are gone. The disks are fine.

What kind of failure is this, and what answers it?

A. A media failure, because loss of RAM means the durable table files were destroyed.  
B. A system crash — memory lost, storage survives, recovery follows.  
C. A transaction failure, because only the transaction running at the instant of reboot matters.  
D. A media failure that can be repaired only from an off-site backup.

### 17. The log as the recovery script

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Write-Ahead Logging  
**Is Curriculum Based:** No  
**Assessment type:** Enabling-role reasoning

After a crash, the data files are a mixture: some committed changes present, some absent, some uncommitted changes present.

Why does logging *first* make this mess recoverable?

A. Because the log is a trustworthy record recovery reads as a script.  
B. Because WAL is a complete independent backup that survives destruction of the local disk.  
C. Because the existence of a log prevents partially written data pages during power loss.  
D. Because recovery can infer commit status from whichever value happens to remain in each page.

### 18. Paying a little always, or a lot once

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Checkpoints  
**Is Curriculum Based:** No  
**Assessment type:** Trade-off analysis

A DBA tunes checkpoint frequency and notices: frequent checkpoints add steady background I/O during normal operation; infrequent ones make the system lighter day-to-day but slower to recover after a crash.

Select the policy conclusion supported by both observations.

A. More frequent checkpoints reduce both normal I/O and recovery work simultaneously.  
B. Less frequent checkpoints shorten recovery because older WAL records replay faster.  
C. Checkpoint frequency trades runtime cost against recovery time directly.  
D. Checkpoint frequency changes backup freshness but does not change crash-recovery work.

### 19. Two transactions, one crash, two fates

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Undo and Redo  
**Is Curriculum Based:** No  
**Assessment type:** Combined-recovery tracing

At the moment a ticketing server crashes, recovery records:

| transaction | status at crash | data-page state |
|---|---|---|
| T1: seat sale | COMMIT record durable | sale not yet on disk |
| T2: price update | no COMMIT record | price change already on disk |

Assign the correct recovery action to both transactions.

A. Undo both because neither result can be trusted after a system crash.  
B. Redo both because every logged change is preserved after replay.  
C. Leave both unchanged because the current data pages are the recovery authority.  
D. Redo for T1's committed sale; undo for T2's uncommitted change.

### 20. Why the box should be small

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Transactions in Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Practice rationale

A code reviewer flags a transaction that begins, makes one update, then calls a slow third-party API for eight seconds before committing.

Why does the chapter insist transactions stay short?

A. Long transactions generate no WAL, so their updates cannot be recovered.  
B. An open transaction holds its locks, blocking others for eight seconds.  
C. PostgreSQL automatically rolls back every transaction lasting more than five seconds.  
D. External API calls become part of WAL and must be replayed after a crash.

### 21. The failure the log cannot fix alone

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Database Failures  
**Is Curriculum Based:** No  
**Assessment type:** Boundary identification

A burst pipe destroys a server's storage — data files *and* the local log disk.

Why does this media failure exceed ordinary crash recovery, and what does it require?

A. Crash recovery needs the log and files; copies must live elsewhere.  
B. The local WAL alone is sufficient even though it was destroyed with the data files.  
C. Restart recovery recreates both the missing data files and WAL from server memory.  
D. Rebuilding the schema constraints reconstructs the committed rows without a backup.

### 22. When "committed" becomes true

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Write-Ahead Logging  
**Is Curriculum Based:** No  
**Assessment type:** Commit-point identification

Under normal PostgreSQL durability settings, a payment transaction reaches the following physical state:

| event | completed? |
|---|---|
| WAL change and COMMIT records flushed | Yes |
| Updated account data page flushed | No |
| COMMIT success returned to application | Yes |

Choose why the acknowledgment remains compatible with durability.

A. It is not compatible; COMMIT must wait for the table page itself in every WAL system.  
B. The account balance is recoverable from application memory after the reboot.  
C. Because the commit's log record reached durable storage before acknowledging.  
D. Because checkpoints guarantee all future data pages before those pages are changed.

### 23. Five minutes versus three days

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Checkpoints  
**Is Curriculum Based:** No  
**Assessment type:** Recovery-window comparison

Two identical, equally busy databases crash at noon:

| database | latest completed checkpoint | crash time |
|---|---|---|
| A | 11:55 today | 12:00 today |
| B | 12:00 Monday | 12:00 Thursday |

Compare their recovery windows, assuming comparable WAL generation rates.

A. B replays less WAL because an older checkpoint covers a larger portion of history.  
B. Both begin at the crash point, so checkpoint age cannot change recovery work.  
C. A must restore a backup because a five-minute checkpoint interval is too short.  
D. A replays roughly five minutes of log; B replays three days before opening.

### 24. Six-fifty, restored

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Undo and Redo  
**Is Curriculum Based:** No  
**Assessment type:** Redo-outcome tracing

Before a crash, the wallet recovery evidence is:

| evidence | balance/status |
|---|---|
| Data page | 500 |
| WAL top-up result | 650 |
| Transaction status | COMMITTED |

Record the balance after recovery completes.

A. 500 — the data file wins.  
B. 650 — redo replayed the committed change from the log.  
C. 1150 — redo adds the page value and the logged result together.  
D. 0 — recovery clears any page whose value differs from a WAL record.

### 25. Three statements, three little commits

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Transactions in Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Auto-commit consequence tracing

A fund-transfer client uses auto-commit and starts with:

| account | balance |
|---|---:|
| Sender | 2000 |
| Receiver | 800 |

It executes a 300 debit as one bare UPDATE. The process dies before issuing the separate credit UPDATE.

Choose the state left by the actual transaction boundaries.

A. Sender 1700, Receiver 800 — the debit auto-committed; the credit never ran.  
B. Sender 2000, Receiver 800 — both bare statements formed one automatic transaction.  
C. Sender 2000, Receiver 1100 — recovery infers and applies the missing credit.  
D. Sender 1700, Receiver 1100 — auto-commit completes unissued statements after a crash.

### 26. Match the failure to its size

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Database Failures  
**Is Curriculum Based:** No  
**Assessment type:** At-a-glance matching

Three descriptions:

1. One unit of work fails; a rollback cleans it up.  
2. Memory is lost; the log rebuilds correctness on restart.  
3. Durable storage itself is lost; backups must step in.

Which naming is correct?

A. 1: media failure; 2: transaction failure; 3: system crash.  
B. 1: system crash, 2: media, 3: transaction.  
C. 1: transaction failure, 2: system crash, 3: media failure, ascending.  
D. 1 and 2: system crashes; 3: transaction failure because the database process stopped.

### 27. First the note, then the deed

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Write-Ahead Logging  
**Is Curriculum Based:** No  
**Assessment type:** Write-sequence ordering

A transaction updates a row. Under write-ahead logging, which sequence of physical events is correct?

A. Flush the data page first, then create the WAL record only if the transaction commits.  
B. Start both physical writes together; whichever finishes first defines recovery order.  
C. Keep both only in memory until a checkpoint writes the page and log simultaneously.  
D. The log record reaches durable storage first; the data page follows later.

### 28. What the checkpoint is not

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Checkpoints  
**Is Curriculum Based:** No  
**Assessment type:** Boundary discrimination

A manager hears "the database checkpoints every few minutes" and concludes backups are unnecessary.

What is the correction?

A. Correct — a checkpoint preserves a second independent copy of every data file.  
B. A checkpoint synchronizes memory with the same disks the database lives on.  
C. A checkpoint copies WAL to off-site storage and can replace media-failure protection.  
D. Checkpoints and backups both restore destroyed disks, but checkpoints restore them faster.

### 29. The rate change that evaporated

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Undo and Redo  
**Is Curriculum Based:** No  
**Assessment type:** Undo-outcome tracing

Before a crash, the hostel recovery evidence is:

| evidence | value/status |
|---|---|
| Original nightly rate | 1200 |
| Data page at crash | 900 |
| Rate transaction | No COMMIT record |

Record the nightly rate after recovery.

A. 1200 — undo reversed the uncommitted change using the log.  
B. 900 — recovery preserves any value that already reached a data page.  
C. 1050 — recovery combines the before and uncommitted values to avoid choosing one.  
D. No value — undo removes the entire hotel row rather than reversing the field change.

### 30. The shape of the safety net

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Transactions in Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Code-pattern selection

Two implementations attempt to make booking insertion and seat decrement share one fate. Select the version with the correct success and error paths.

A. `commit(); insert_booking(); decrement_seats(); begin();` so the boundary surrounds the work in reverse  
B. `insert_booking(); commit(); decrement_seats(); commit();` so each successful statement remains independently durable  
C. `begin(); try { insert_booking(); decrement_seats(); commit(); } catch (error) { rollback(); }`  
D. `try { insert_booking(); } finally { decrement_seats(); }` so the decrement runs even after insertion failure

### 31. Choose the remedy for the ruin

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Database Failures  
**Is Curriculum Based:** No  
**Assessment type:** Response matching

A fire destroys a trading firm's database server, including both its data files and local WAL. The firm also maintains a separate off-site copy of its data.

Select the response consistent with the chapter's media-failure boundary.

A. Restart the damaged server and rely on its destroyed local WAL to recreate every file.  
B. Issue ROLLBACK because media failure affects only the transaction active during the fire.  
C. Run `CHECKPOINT` after restart so empty replacement disks acquire the lost rows.  
D. Recover from the separate backup or replica; local crash recovery alone has no source.

### 32. Why the tables can afford to wait

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Write-Ahead Logging  
**Is Curriculum Based:** No  
**Assessment type:** Deferral justification

Under WAL, a database often leaves committed changes sitting in memory for a while before writing them to the data files.

Why is that delay safe?

A. Committed data pages may be lost because COMMIT promises only logical visibility.  
B. Because the log already holds the change durably for redo to use.  
C. RAM survives ordinary power loss longer than the database's storage devices.  
D. Checkpoints guarantee every future committed change before its WAL record exists.

### 33. Setting the dial for the emergency room

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Checkpoints  
**Is Curriculum Based:** No  
**Assessment type:** Requirement-driven tuning

An emergency-dispatch database has a strict requirement: after any crash, it must be answering calls again within two minutes.

Choose the policy direction and the trade-off it accepts.

A. Checkpoint more frequently to shorten WAL replay, accepting more routine disk activity.  
B. Checkpoint less frequently so recovery scans fewer but older WAL records after a crash.  
C. Disable checkpoints and rely on replaying the complete database history within two minutes.  
D. Keep the frequency unchanged because checkpoints influence backups but not restart time.

### 34. The two verbs of recovery

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Undo and Redo  
**Is Curriculum Based:** No  
**Assessment type:** Definition pairing

Which pairing states redo and undo correctly?

A. Redo repeats every SQL query, while undo removes every table touched since the checkpoint.  
B. Redo reverses committed work, while undo preserves uncommitted changes already on disk.  
C. Redo replays committed changes not on disk; undo reverses uncommitted ones.  
D. Both passes restore backup files and do not inspect transaction commit records.

### 35. The transfer with commits in the middle

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Transactions in Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Code-review diagnosis

A code review finds this in a wallet service:

```
debit_sender();      // runs, auto-commits
credit_receiver();   // runs, auto-commits
```

Each function issues one bare SQL statement. Select the defect and smallest correct repair.

A. Reverse the functions so a missing debit is safer than a missing credit.  
B. Keep auto-commit but retry only whichever statement did not run.  
C. Add a comment declaring both auto-committed statements to be one business operation.  
D. Begin before the debit, commit after the credit, and roll back the pair on error.

### 36. Rebooted, and whole again

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Database Failures  
**Is Curriculum Based:** No  
**Assessment type:** Automatic-recovery expectation

After a power cut, an operations engineer restarts the database server. The disks are healthy. Nobody runs any special restore.

What happens, and why is no manual restore needed?

A. The database opens immediately with whichever partial pages happened to reach disk.  
B. On startup the database notices the unclean shutdown and runs crash recovery itself, from the log.  
C. The database requires a backup restore because every system crash is a media failure.  
D. The engineer must choose committed transactions manually, using the application audit log as the only recovery source.

### 37. The half-written page

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Write-Ahead Logging  
**Is Curriculum Based:** No  
**Assessment type:** Torn-write reasoning

Power fails while the database is midway through writing a data page: the page on disk is now half old bytes, half new — internally inconsistent.

Why doesn't this corrupt the database permanently?

A. Because the log's record, flushed before the write, tells recovery the truth.  
B. Because recovery treats every half-written page as committed without consulting WAL.  
C. Because disk hardware reconstructs the missing half from the unchanged bytes automatically.  
D. Because the next checkpoint discards the page and all transactions that ever changed it.

### 38. Checkpoint, in one sentence

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Checkpoints  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

A new operator must distinguish a checkpoint from a backup and a transaction boundary. Select the accurate description.

A. A validation step that approves each transaction before COMMIT.  
B. An independent copy of the database stored away from the primary disks.  
C. A moment where the database flushes changes to the data files.  
D. A boundary that rolls back every transaction still open when the checkpoint begins.

### 39. The full restart, walked through

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Undo and Redo  
**Is Curriculum Based:** No  
**Assessment type:** Recovery-sequence tracing

A database restarts after a crash and examines:

| transaction | COMMIT before crash? | changes fully in data files? |
|---|---|---|
| P | Yes | No |
| Q | Yes | No |
| R | No | Some |

Complete the taught redo-then-undo sequence.

A. Undo P and Q because their pages are incomplete; redo R because some of its writes reached disk.  
B. Redo replays P and Q's changes; undo reverses R's on-disk changes.  
C. Redo P, Q, and R and preserve every replayed result, regardless of commit status.  
D. Leave all three as found because recovery does not modify data files automatically.

### 40. The application's half of the bargain

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Transactions & Reliability  
**Subtopic:** Transactions in Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Integrated pattern selection

A payments team must debit a wallet and insert an order as one operation. Its client may report constraint errors or deadlock errors.

Select the complete application-side design.

A. Auto-commit both statements and retry only the statement that reports an error.  
B. Begin at application startup and commit at shutdown so every checkout and unrelated request during the day shares one transaction fate.  
C. Use one explicit transaction but commit its successful statements before handling an error.  
D. Wrap the statements in one BEGIN/COMMIT with rollback on error, keep it short, and retry on deadlocks.

---

## Instructor Key

### 1. C

The three failures differ by what is lost: one transaction's work, the memory's contents, or the durable data itself. The ascending order matters because each size summons different machinery.

### 2. B

The rule is ordering: the log's account of a change becomes durable before the change itself does. Everything else in the chapter — redo, undo, deferred writes — leans on that one guarantee.

### 3. D

The checkpoint certifies "disk is current up to here," so recovery's replay starts there instead of at the log's birth. Without checkpoints, recovery time would grow with the age of the database.

### 4. A

Committed-but-not-yet-in-the-files is redo's exact clientele: the log has the durable proof, and replay applies it. Durability is delivered *by* this mechanism, not despite the crash.

### 5. D

Auto-commit is the default contract: statement succeeds, statement commits. The persistence the script observed is transactions working invisibly — one per statement.

### 6. C

The taxonomy is operational: rollback for one failed transaction, log-driven restart recovery for a system crash, and a separate backup or replica for lost storage. Naming the failure is choosing the response.

### 7. A

Direct writes leave no way to distinguish a finished write from an interrupted one — a torn page is just bytes. The log exists to be the account that survives: what changed, to what, and whether it committed.

### 8. B

Recovery first completes the record (redo everything logged), then subtracts the losers (undo the uncommitted). Working from a rebuilt, complete picture is what makes the reversal precise.

### 9. C

A checkpoint is a synchronization event: dirty pages flushed, log position marked. It is housekeeping with a purpose — establishing the starting line that bounds future recovery.

### 10. A

`rollback()` completes the missing error branch. It discards any successful step from the failed attempt; committing there would preserve a partial refund, while beginning again would leave the failed transaction unresolved.

### 11. D

Transaction failure is the everyday, contained case: one unit rolls back via the normal machinery while the system runs on. Its remedy is the smallest one — and often invisible to everyone else.

### 12. B

The log must support both verbs: replay (new state) and reversal (old state), tied to the owning transaction and its outcome. A record that supports only one direction would cripple half of recovery.

### 13. A

The replay window is a liability that grows by the minute, so bounding it cannot depend on human memory. The database checkpoints on its own schedule; manual requests are a supplement, not the system.

### 14. C

Never-committed means never-happened: recovery's undo delivers the same outcome a rollback would have. The crash changed *when* the reversal ran, not *whether*.

### 15. D

The retry is safe because the first attempt left nothing behind — atomicity's clean rollback is what makes "just run it again" a correct strategy rather than a gamble.

### 16. B

Memory lost, disks intact is the system crash profile. The log makes it self-service: restart, automatic recovery, reopen — backups stay on the shelf for the day the *disks* fail.

### 17. A

The mess is recoverable because an authority exists outside it: the log, complete and durable, written ahead of every change. Recovery is the act of making the data files agree with that account.

### 18. C

Checkpoints convert recovery time into runtime overhead at an adjustable rate. Neither extreme is "correct" — the dial is set by the business's tolerance for downtime versus its tolerance for steady I/O.

### 19. D

One crash, two verdicts: T1's commit makes its work sacred (redo restores it); T2's lack of one makes its work void (undo removes it, even the parts that reached disk). The reopened database is the last committed state, exactly.

### 20. B

An open transaction is a held claim: locks that block others and provisional work that recovery may someday reverse. Idling inside one — waiting on an external API — pays those costs for nothing.

### 21. A

Local crash recovery presumes the data files and WAL survived. When both are destroyed, the recovery source must already exist elsewhere, such as a separate backup or replica.

### 22. C

The commit's truth lives in the flushed log record, not the data page. With that record durable, every crash is survivable by replay — which is precisely why the acknowledgment may precede the table write honestly.

### 23. D

Same crash, same machinery, different starting line: five minutes of log versus three days of it. Checkpoint interval is the single knob behind that difference in downtime.

### 24. B

Redo notices the gap between the log (650, committed) and the data file (500) and closes it. The customer's money was protected by a log record, and recovery cashes that protection in.

### 25. A

Without BEGIN, each statement sealed itself: the debit's auto-commit was final before the credit ever ran. The half-transfer is not bad luck — it is the precise hazard explicit wrapping exists to remove.

### 26. C

Rollback-sized, log-sized, backup-sized: transaction failure, system crash, media failure. The remedies name the failures.

### 27. D

Note first, deed later: the log record is flushed ahead, and the data page follows at the database's convenience. The interval between them is exactly the exposure the log's priority covers.

### 28. B

Checkpoints and backups share a reassuring sound and nothing else: one shortens crash recovery on the same disks, the other survives those disks' destruction. Retiring backups because checkpoints exist confuses the two failure classes.

### 29. A

Undo is powered by the log's memory of the before-image: 1200 returns, the uncommitted 900 vanishes. That the wrong value had reached disk is precisely why undo exists.

### 30. C

The pattern needs all four parts: open, do related work, commit on success, roll back on failure. Option B's mid-sequence commits dissolve the unit; option D's `finally` guarantees the second statement even when the first failed.

### 31. D

The local recovery inputs burned with the server, so ordinary restart recovery has nothing to read. The chapter's boundary is the important point: media failure requires a separate backup or replica, not the destroyed local WAL.

### 32. B

The log's durable promise underwrites the data files' laziness: any committed change not yet in the files is reconstructible by redo. Deferral is a performance freedom the WAL rule purchased.

### 33. A

A hard recovery-time objective works backwards to a checkpoint interval: short window, short replay, requirement met — paid for in steady background I/O. Tuning direction follows the requirement, not the preference for quiet disks.

### 34. C

Redo completes what was promised (committed, not yet on disk); undo erases what was never promised (uncommitted, prematurely on disk). Their joint destination is the last committed state.

### 35. D

Two auto-commits make two independent units of what the business defines as one. The review's fix is structural, not stylistic: one explicit transaction restores the atomicity the money movement requires.

### 36. B

Unclean shutdown triggers recovery automatically at startup: redo, undo, then open. The engineer's restart was the entire manual procedure — the log did the rest.

### 37. A

The torn page is untrusted and rebuilt: the log, flushed before the page write began, holds the authoritative version of what the page should say. WAL's ordering rule is exactly what makes "half-written" a repairable condition.

### 38. C

A checkpoint is a synchronization moment with a bookmark: memory flushed to files, position marked in the log. Future recovery starts at the bookmark.

### 39. B

The two-phase pass in one scenario: redo installs P and Q (committed, incomplete on disk), undo strips R (uncommitted, partially on disk). Reopen at the last committed state — no choices, no residue.

### 40. D

The chapter's application-side discipline in one pattern: explicit boundaries around related work, brevity inside them, and principled retry on retryable errors. Each of the other options abandons at least one of the three.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Failure classification and response matching | 1, 6, 11, 16, 21, 26, 31, 36 |
| WAL mechanism and ordering reasoning | 2, 7, 12, 17, 22, 27, 32, 37 |
| Checkpoint purpose, trade-off, and tuning | 3, 9, 13, 18, 23, 28, 33, 38 |
| Redo/undo state and sequence tracing | 4, 8, 14, 19, 24, 29, 34, 39 |
| Missing code and smallest application repair | 10, 30, 35, 40 |
| Auto-commit, retry, and transaction-scope reasoning | 5, 15, 20, 25 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| Database Failures | 1, 6, 11, 16, 21, 26, 31, 36 | 8 |
| Write-Ahead Logging | 2, 7, 12, 17, 22, 27, 32, 37 | 8 |
| Checkpoints | 3, 9, 13, 18, 23, 28, 33, 38 | 8 |
| Undo and Redo | 4, 8, 14, 19, 24, 29, 34, 39 | 8 |
| Transactions in Application Code | 5, 10, 15, 20, 25, 30, 35, 40 | 8 |

Questions 1–10 collectively cover all five Topic 6.3 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (2, 5, 10, 11, 14, 20, 25, 26, 34, 38)
- Intermediate: 24 questions
- Advanced: 6 questions (19, 23, 31, 37, 39, 40)
- Correct option A: 10 questions (4, 7, 10, 13, 17, 21, 25, 29, 33, 37)
- Correct option B: 10 questions (2, 8, 12, 16, 20, 24, 28, 32, 36, 39)
- Correct option C: 10 questions (1, 6, 9, 14, 18, 22, 26, 30, 34, 38)
- Correct option D: 10 questions (3, 5, 11, 15, 19, 23, 27, 31, 35, 40)
- Longest consecutive run of one correct letter: below 3 throughout
