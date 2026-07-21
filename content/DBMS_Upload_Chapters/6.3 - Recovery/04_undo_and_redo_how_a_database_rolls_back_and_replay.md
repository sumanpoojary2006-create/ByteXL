## Introduction

When a database restarts after a crash, the log holds a record of everything that happened since the last checkpoint, but that log contains two very different kinds of entries mixed together: changes from transactions that had already committed before the crash, and changes from transactions that were still in progress, uncommitted, at the exact moment the crash happened. Recovery has to treat these two kinds completely differently.

Committed work must be preserved, durability demands it. Uncommitted work must be discarded, atomicity demands it. This is the job of **redo** and **undo**, the two passes recovery makes over the log every time a database restarts after an unclean shutdown.

**Definition:** Redo reapplies every committed transaction's changes to guarantee durability, and undo reverses every uncommitted transaction's changes to guarantee atomicity, and together the two passes are what actually turn a crashed, potentially inconsistent set of data files back into an exact, correct reflection of every transaction that had genuinely finished before the crash.

![Intro visual for undo and redo how a database rolls back](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_intro_undo_and_redo_how_a_database_rolls_back_and_repl_clean_1011bf80.png)

## Redo: Replaying Committed Work That Never Made It to Disk

Recall from the `write-ahead logging` lesson that a `COMMIT` can return success once its log record is durable, even before the actual data file has been updated. If a crash happens in that gap, the change is safely logged but not yet reflected in the data files.

Redo handles this in two steps:

1. It walks forward through the log from the last checkpoint.

2. It reapplies every change belonging to a transaction that committed, bringing the data files up to date with everything the log promised had already succeeded.

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
 src="https://onecompiler.com/embed/postgresql/44vkaf4fb" 
 width="100%"
></iframe>

Expected output:

| balance |
| --- |
| 4000.00 |

The `SELECT` here shows 4000.00, because in this running session nothing actually crashed.

But conceptually, if power had been lost right after that `COMMIT`, PostgreSQL's redo pass on restart would read the log, see that this transaction committed, and reapply the balance change to the data file, guaranteeing the balance reads as 4000.00 once the database comes back online, exactly the durability guarantee from earlier in this unit, now explained in terms of the actual mechanism that delivers it.

![REDO replaying committed log records into the data file](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_redo_replays_committed_log.png)

## Undo: Reversing Work That Never Committed

The opposite case is a transaction that was still open, uncommitted, at the moment of the crash. Its changes were logged as they happened, following the write-ahead rule, but since it never reached `COMMIT`, atomicity requires that none of its effects survive.

Undo is the pass that walks through the log looking for transactions with no matching commit record, and reverses any of their changes that made it into the data files before the crash.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf4s9" 
 width="100%"
></iframe>

Expected output:

| balance |
| --- |
| 5000.00 |

The explicit `ROLLBACK` here demonstrates the same outcome undo would achieve automatically after a crash: the balance remains 5000.00, as if the 2000.00 deduction never happened.

In a genuine crash scenario, no `ROLLBACK` would ever be issued by anyone, since the whole application vanished along with the server, but PostgreSQL's undo pass performs the identical reversal automatically during recovery, simply by recognizing that this transaction's log entries have no corresponding commit record.

![UNDO reversing uncommitted log records back to the before state](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_undo_reverses_uncommitted_log.png)

## Why Redo Runs Before Undo

Recovery always performs redo first, across the entire log since the last checkpoint, bringing the data files up to exactly the state they would be in if every logged change, committed or not, had been applied. Only after that is undo performed, walking back through the specific changes belonging to transactions that never committed, and reversing exactly those.

Redoing everything first, including eventually-undone work, might sound wasteful, but it gives the undo pass a single, consistent, fully-replayed state to work from, rather than trying to reason about a data file that is only partially updated.

## Redo and Undo at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pass</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Applies to</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effect</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redo</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transactions that committed before the crash</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reapplies their logged changes to the data files, guaranteeing durability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Undo</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transactions that never committed before the crash</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reverses any of their changes that reached the data files, guaranteeing atomicity</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redo always runs first, across everything, then undo reverses only the uncommitted portion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gives undo a consistent state to reason about</td>
    </tr>
  </tbody>
</table>

## Your Turn

Using the `accounts` table above, run one transaction that commits a balance change and a second transaction that makes a change but rolls back instead, then write a comment explaining which pass, redo or undo, would be responsible for each one's outcome if this had instead been a genuine crash rather than explicit `COMMIT`/`ROLLBACK` commands.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf549" 
 width="100%"
></iframe>

Expected result and verification:

The committed transaction's effect would be guaranteed by the redo pass on restart, reapplying its logged change if it had not yet reached the data file, while the rolled-back transaction's effect would be reversed by the undo pass, which recognizes it has no matching commit record in the log and discards whatever partial changes it made.

## Conclusion

Redo reapplies every committed transaction's changes to guarantee durability, and undo reverses every uncommitted transaction's changes to guarantee atomicity, and together the two passes are what actually turn a crashed, potentially inconsistent set of data files back into an exact, correct reflection of every transaction that had genuinely finished before the crash.

With database failures, `write-ahead logging`, checkpoints, and the redo-undo recovery process all covered, the final lesson in this unit turns from database-internal recovery mechanics to how an application developer actually uses transactions in day-to-day code.
