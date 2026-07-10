## Introduction

`Write-ahead logging` guarantees that every change is recorded before it is applied, but it leaves an obvious question unanswered: if the log records every change forever, a database that has been running for months would have to replay months of log entries after every single crash, which would make recovery take longer and longer the older the system got. This is the problem a **checkpoint** solves: a periodic marker that says "everything up to this point has definitely been written to the actual data files," so recovery only ever has to replay the log starting from the most recent checkpoint, not from the very beginning of time.

## What a Checkpoint Actually Does

A checkpoint is a point in time where the database guarantees that every change logged before that point has also been fully written out to the real data files on disk, not just recorded in the log.

```postgresql file=checkpoint_demo.sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    balance NUMERIC(10, 2)
);

INSERT INTO accounts (account_id, balance) VALUES (1, 5000.00);
```

```postgresql with=checkpoint_demo.sql
CHECKPOINT;
```

Running `CHECKPOINT` explicitly forces PostgreSQL to flush every pending change out to its actual data files immediately, rather than waiting for its normal automatic schedule. Once this completes, the database can be certain of two things:

- Everything committed before this point is safely reflected in the data files themselves.
- That safety no longer depends on merely being recoverable by replaying the log.

## Why Checkpoints Bound Recovery Time

Without a checkpoint, a database restarting after a crash would have no way to know how far back its data files were already up to date, so it would have to replay every single log record ever written, from the very start of the log, just to be safe. A checkpoint gives recovery a known, recent starting line.

```postgresql with=checkpoint_demo.sql
UPDATE accounts SET balance = balance - 500.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance - 200.00 WHERE account_id = 1;

CHECKPOINT;

UPDATE accounts SET balance = balance - 100.00 WHERE account_id = 1;
-- If a crash happened right here, recovery would only need to replay
-- the log starting from the CHECKPOINT above, since everything before
-- it is already guaranteed to be safely on disk in the data files.
-- Only the final -100.00 change, logged after the checkpoint, would
-- need to be replayed on restart.

SELECT balance FROM accounts WHERE account_id = 1;
```

The two updates before `CHECKPOINT` are guaranteed to already be reflected in the data files themselves the moment the checkpoint completes. Only the change logged after the checkpoint is at risk of existing only in the log and not yet in the data files, which is exactly the portion recovery would need to replay if a crash happened right after it.

## Why Checkpoints Happen Automatically, Not Just on Demand

Running `CHECKPOINT` by hand is useful for understanding what it does, but in practice, PostgreSQL runs checkpoints automatically on a regular schedule, controlled by settings like how much time has passed or how much log activity has accumulated since the last one.

```postgresql with=checkpoint_demo.sql
SHOW checkpoint_timeout;
```

`checkpoint_timeout` reports how long PostgreSQL waits, at most, between automatic checkpoints, 5 minutes by default. This is a deliberate trade-off: checkpointing more frequently keeps recovery time shorter after a crash, since less log needs replaying, but each checkpoint itself costs time and disk activity while it runs, so checkpointing too aggressively can slow down the database's normal, everyday operation.

## The Trade-off Checkpoints Represent

| Checkpoint frequency | Recovery time after a crash | Cost during normal operation |
|---|---|---|
| More frequent | Shorter, less log to replay | Higher, more frequent disk activity |
| Less frequent | Longer, more log to replay | Lower, less frequent disk activity |

## Your Turn

Run several updates against the `accounts` table above, issue a `CHECKPOINT`, run one more update, and write a comment explaining exactly which of these updates recovery would need to replay from the log if a crash happened immediately after the final update.

```postgresql with=checkpoint_demo.sql
-- Write your queries and comment below
```

If three updates run, then `CHECKPOINT`, then one more update, only that last update, logged after the checkpoint, is at risk of not yet being in the data files; the three updates before the checkpoint are guaranteed already durable in the actual data, so recovery would only need to replay the single post-checkpoint change.

## Conclusion

A checkpoint marks a point where every previously logged change is guaranteed to already be written to the actual data files, giving recovery a recent, known starting point instead of forcing it to replay a database's entire history after every crash, at the cost of periodic disk activity that has to be balanced against how quickly the system needs to recover. With logging and checkpoints both covered, the next lesson looks at exactly what recovery does with the log once a crash actually happens: replaying some changes forward and undoing others.
