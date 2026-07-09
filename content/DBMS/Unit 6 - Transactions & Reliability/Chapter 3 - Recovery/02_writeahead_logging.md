## Introduction

Durability, covered earlier in this unit, promised that a committed transaction survives a crash, and briefly mentioned the mechanism behind that promise without explaining it in depth: `write-ahead logging`. The name describes the rule precisely: before any change is applied to the actual data files on disk, a record of that change is written ahead of it, to a separate, append-only log. This ordering, log first, data files second, is the entire foundation of how a database recovers correctly after a crash, and it is worth understanding exactly why the order matters.

## Why Writing Directly to Data Files Is Not Enough

It might seem simpler for a database to just write a change straight to its data files the moment a transaction commits. The problem is that updating a data file on disk is not instantaneous or atomic at the hardware level:

- It can involve rewriting a whole page of data.
- A crash occurring midway through that write could leave the page itself corrupted, not just outdated.

A separate, simpler, sequential log write is far cheaper and safer to make durable quickly than a full, scattered update to the actual data file structure.

```postgresql file=wal_demo.sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    balance NUMERIC(10, 2)
);

INSERT INTO accounts (account_id, balance) VALUES (1, 5000.00);
```

```postgresql with=wal_demo.sql
SELECT pg_current_wal_lsn();
```

`pg_current_wal_lsn()` returns PostgreSQL's current position in its `write-ahead log`, a steadily advancing marker. Every change made to the database advances this marker, since every change is first recorded in the log before it ever touches the actual table's data files on disk.

## The Rule: Log Before Data

The core rule of `write-ahead logging` is simple to state: a change to a data page is never written to permanent storage until the log record describing that change has already been written to permanent storage first.

```postgresql with=wal_demo.sql
BEGIN;
UPDATE accounts SET balance = balance - 500.00 WHERE account_id = 1;
COMMIT;

SELECT pg_current_wal_lsn();
```

By the time this `COMMIT` returns success to the caller, PostgreSQL guarantees the log record describing "subtract 500.00 from account 1's balance" has already been durably written, even if the actual data file holding the `accounts` table's page has not been updated on disk yet. The second `SELECT` shows the WAL position has advanced past where it was before, confirming a new record was appended.

This is why `COMMIT` can safely report success immediately: the log, not the data file, is what recovery actually depends on.

## Why Logging First Makes Recovery Possible

If the server crashes at any point after `COMMIT` returns, the data file on disk might genuinely not yet reflect the balance change, since writing the log is fast and writing the full data file can be deferred and batched for efficiency. But because the log record was guaranteed to be durable before `COMMIT` ever returned, the database's recovery process can:

1. Read that log on restart.
2. Reapply, or "replay," any change whose log record exists but whose effect had not yet made it into the data files.

This is exactly how durability is delivered in practice: not by guaranteeing every data file write happens instantly, but by guaranteeing the log record exists first and can always be replayed if needed.

## What Gets Written to the Log

Every change-making statement, `INSERT`, `UPDATE`, `DELETE`, and even structural changes like `CREATE TABLE`, generates a log record describing exactly what changed, before that change is considered complete.

```postgresql with=wal_demo.sql
INSERT INTO accounts (account_id, balance) VALUES (2, 3000.00);
DELETE FROM accounts WHERE account_id = 2;

SELECT pg_current_wal_lsn();
```

Both the `INSERT` and the `DELETE` here each generate their own log entry, and the WAL position advances after each one, confirming that even a row inserted and then deleted moments later still passed through the log along the way, since the log records the sequence of changes, not just the final resulting state.

## Write-Ahead Logging at a Glance

| Concept | Detail |
|---|---|
| Core rule | A log record for a change is written durably before the change itself is applied to data files |
| Why | Log writes are cheap and sequential; data file writes can be deferred safely once the log exists |
| What it enables | Recovery can replay any committed change whose log record exists but whose data file write had not completed |
| PostgreSQL term | WAL, short for Write-Ahead Log |

## Your Turn

Check the current WAL position, run a transaction that inserts a new account and commits, and check the WAL position again, confirming it has advanced.

```postgresql with=wal_demo.sql
-- Write your queries below
```

If you run `SELECT pg_current_wal_lsn();`, then `BEGIN; INSERT INTO accounts (account_id, balance) VALUES (3, 7000.00); COMMIT;`, then `SELECT pg_current_wal_lsn();` again, the second position is further along than the first, confirming the `INSERT`'s log record was appended as part of the commit.

## Conclusion

`Write-ahead logging` guarantees that a durable record of every change exists before the change is considered complete, which is what allows a database to safely defer the slower work of updating actual data files while still guaranteeing that a crash can never lose a committed transaction's effect. The log itself would grow forever and take longer to replay with every passing day if nothing ever bounded it, which is exactly the problem the next lesson's mechanism, checkpoints, exists to solve.
