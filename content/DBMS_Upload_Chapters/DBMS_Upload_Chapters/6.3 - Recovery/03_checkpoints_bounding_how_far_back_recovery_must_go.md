## Introduction

- `Write-ahead logging` guarantees that every change is recorded before it is applied, but it leaves an obvious question unanswered: if the log records every change forever, a `database` that has been running for months would have to replay months of log entries after every single crash, which would make `recovery` take longer and longer the older the system got.
- This is the problem a **checkpoint** solves: a periodic marker that says "everything up to this point has definitely been written to the actual data files," so `recovery` only ever has to replay the log starting from the most recent checkpoint, not from the very beginning of time.

**Definition:** A checkpoint marks a point where every previously logged change is guaranteed to already be written to the actual data files, giving `recovery` a recent, known starting point instead of forcing it to replay a `database`'s entire history after every crash, at the cost of periodic disk activity that has to be balanced against how quickly the system needs to recover.

## What a Checkpoint Actually Does

A checkpoint is a point in time where the `database` guarantees that every change logged before that point has also been fully written out to the real data files on disk, not just recorded in the log.

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
 src="https://onecompiler.com/embed/postgresql/44vkaf5em" 
 width="100%"
></iframe>

Expected observation: PostgreSQL completes `CHECKPOINT` without returning a business-data table. The important result is that dirty pages are flushed and the recovery starting point advances.

Running `CHECKPOINT` explicitly forces PostgreSQL to flush every pending change out to its actual data files immediately, rather than waiting for its normal automatic schedule. Once this completes, the `database` can be certain of two things:

- Everything committed before this point is safely reflected in the data files themselves.
- That safety no longer depends on merely being recoverable by replaying the log.

## Why Checkpoints Bound Recovery Time

Without a checkpoint, a `database` restarting after a crash would have no way to know how far back its data files were already up to date, so it would have to replay every single log record ever written, from the very start of the log, just to be safe. A checkpoint gives `recovery` a known, recent starting line.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf5r5" 
 width="100%"
></iframe>

Expected observation: PostgreSQL completes `CHECKPOINT` without returning a business-data table. The important result is that dirty pages are flushed and the recovery starting point advances.

The two updates before `CHECKPOINT` are guaranteed to already be reflected in the data files themselves the moment the checkpoint completes. Only the change logged after the checkpoint is at risk of existing only in the log and not yet in the data files, which is exactly the portion `recovery` would need to replay if a crash happened right after it.

![Checkpoint marking which logged changes are already safely on disk](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_checkpoint_bounds_recovery_timeline.png)

## Why Checkpoints Happen Automatically, Not Just on Demand

Running `CHECKPOINT` by hand is useful for understanding what it does, but in practice, PostgreSQL runs checkpoints automatically on a regular schedule, controlled by settings like how much time has passed or how much log activity has accumulated since the last one.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf63z" 
 width="100%"
></iframe>

Expected output:

| checkpoint_timeout |
| --- |
| 5min |

- `checkpoint_timeout` reports how long PostgreSQL waits, at most, between automatic checkpoints, 5 minutes by default.
- This is a deliberate trade-off: checkpointing more frequently keeps `recovery` time shorter after a crash, since less log needs replaying, but each checkpoint itself costs time and disk activity while it runs, so checkpointing too aggressively can slow down the `database`'s normal, everyday operation.

![Checkpoint frequency balancing shorter recovery against normal-operation cost](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_checkpoint_frequency_tradeoff.png)

## The Trade-off Checkpoints Represent

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Checkpoint frequency</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Recovery time after a crash</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cost during normal operation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More frequent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shorter, less log to replay</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Higher, more frequent disk activity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less frequent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Longer, more log to replay</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lower, less frequent disk activity</td>
    </tr>
  </tbody>
</table>

## Your Turn

Run several updates against the `accounts` `table` above, issue a `CHECKPOINT`, run one more update, and write a comment explaining exactly which of these updates `recovery` would need to replay from the log if a crash happened immediately after the final update.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf6g3" 
 width="100%"
></iframe>

Expected result and verification:

If three updates run, then `CHECKPOINT`, then one more update, only that last update, logged after the checkpoint, is at risk of not yet being in the data files the three updates before the checkpoint are guaranteed already durable in the actual data, so `recovery` would only need to replay the single post-checkpoint change.

## Conclusion

A checkpoint marks a point where every previously logged change is guaranteed to already be written to the actual data files, giving `recovery` a recent, known starting point instead of forcing it to replay a `database`'s entire history after every crash, at the cost of periodic disk activity that has to be balanced against how quickly the system needs to recover.

With logging and checkpoints both covered, the next lesson looks at exactly what `recovery` does with the log once a crash actually happens: replaying some changes forward and undoing others.
