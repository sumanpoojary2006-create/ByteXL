## Introduction

Durability, covered earlier in this unit, promised that a committed transaction survives a crash, and briefly mentioned the mechanism behind that promise without explaining it in depth: `write-ahead logging`. The name describes the rule precisely: before any change is applied to the actual data files on disk, a record of that change is written ahead of it, to a separate, append-only log.

This ordering, log first, data files second, is the entire foundation of how a database recovers correctly after a crash, and it is worth understanding exactly why the order matters.

**Definition:** `Write-ahead logging` guarantees that a durable record of every change exists before the change is considered complete, which is what allows a database to safely defer the slower work of updating actual data files while still guaranteeing that a crash can never lose a committed transaction's effect.

![Intro visual for writeahead logging](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_intro_writeahead_logging.png)

## Why Writing Directly to Data Files Is Not Enough

It might seem simpler for a database to just write a change straight to its data files the moment a transaction commits. The problem is that updating a data file on disk is not instantaneous or atomic at the hardware level:

- It can involve rewriting a whole page of data.
- A crash occurring midway through that write could leave the page itself corrupted, not just outdated.

A separate, simpler, sequential log write is far cheaper and safer to make durable quickly than a full, scattered update to the actual data file structure.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `accounts`

| account_id | balance |
| --- | --- |
| 1 | 5000.00 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    balance NUMERIC(10, 2)
);

INSERT INTO accounts (account_id, balance) VALUES (1, 5000.00);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf34n" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns a WAL location such as `0/16B6C50`. The exact value is server-specific; after a committed write, a later location should be equal to or ahead of the earlier one.

- `pg_current_wal_lsn()` returns PostgreSQL's current position in its `write-ahead log`, a steadily advancing marker.
- Every change made to the database advances this marker, since every change is first recorded in the log before it ever touches the actual table's data files on disk.

## The Rule: Log Before Data

The core rule of `write-ahead logging` is simple to state: a change to a data page is never written to permanent storage until the log record describing that change has already been written to permanent storage first.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf3gt" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns a WAL location such as `0/16B6C50`. The exact value is server-specific; after a committed write, a later location should be equal to or ahead of the earlier one.

By the time this `COMMIT` returns success to the caller, PostgreSQL guarantees the log record describing "subtract 500.00 from account 1's balance" has already been durably written, even if the actual data file holding the `accounts` table's page has not been updated on disk yet. The second `SELECT` shows the `WAL` position has advanced past where it was before, confirming a new record was appended.

This is why `COMMIT` can safely report success immediately: the log, not the data file, is what recovery actually depends on.

![Write-ahead logging records the log before the data page is written](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_wal_log_before_data_page.png)

## Why Logging First Makes Recovery Possible

If the server crashes at any point after `COMMIT` returns, the data file on disk might genuinely not yet reflect the balance change, since writing the log is fast and writing the full data file can be deferred and batched for efficiency. But because the log record was guaranteed to be durable before `COMMIT` ever returned, the database's recovery process can:

1. Read that log on restart.

2. Reapply, or "replay," any change whose log record exists but whose effect had not yet made it into the data files.

This is exactly how durability is delivered in practice: not by guaranteeing every data file write happens instantly, but by guaranteeing the log record exists first and can always be replayed if needed.

![WAL replay restoring committed changes after a crash](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_wal_replay_after_crash.png)

## What Gets Written to the Log

Every change-making statement, `INSERT`, `UPDATE`, `DELETE`, and even structural changes like `CREATE TABLE`, generates a log record describing exactly what changed, before that change is considered complete.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf3te" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns a WAL location such as `0/16B6C50`. The exact value is server-specific; after a committed write, a later location should be equal to or ahead of the earlier one.

Both the `INSERT` and the `DELETE` here each generate their own log entry, and the `WAL` position advances after each one, confirming that even a row inserted and then deleted moments later still passed through the log along the way, since the log records the sequence of changes, not just the final resulting state.

## Write-Ahead Logging at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Core rule</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A log record for a change is written durably before the change itself is applied to data files</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Why</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Log writes are cheap and sequential; data file writes can be deferred safely once the log exists</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What it enables</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recovery can replay any committed change whose log record exists but whose data file write had not completed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PostgreSQL term</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">WAL, short for Write-Ahead Log</td>
    </tr>
  </tbody>
</table>

## Your Turn

Check the current `WAL` position, run a transaction that inserts a new account and commits, and check the `WAL` position again, confirming it has advanced.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf44g" 
 width="100%"
></iframe>

Expected result and verification:

If you run `SELECT pg_current_wal_lsn();`, then `BEGIN; INSERT INTO accounts (account_id, balance) VALUES (3, 7000.00); COMMIT;`, then `SELECT pg_current_wal_lsn();` again, the second position is further along than the first, confirming the `INSERT`'s log record was appended as part of the commit.

## Conclusion

`Write-ahead logging` guarantees that a durable record of every change exists before the change is considered complete, which is what allows a database to safely defer the slower work of updating actual data files while still guaranteeing that a crash can never lose a committed transaction's effect. The log itself would grow forever and take longer to replay with every passing day if nothing ever bounded it, which is exactly the problem the next lesson's mechanism, checkpoints, exists to solve.
