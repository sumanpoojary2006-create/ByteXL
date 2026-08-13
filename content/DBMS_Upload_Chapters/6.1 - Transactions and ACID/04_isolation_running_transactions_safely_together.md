## Introduction

Every transaction covered so far has run alone, one connection, one sequence of statements, nothing else touching the database at the same time. A real banking system is never that quiet: hundreds of transfers, deposits, and balance checks can hit the same accounts within the same second.

The third letter in ACID, **isolation**, is the guarantee that concurrently running transactions do not interfere with each other in ways that produce incorrect results, specifically, that one transaction's in-progress, uncommitted changes stay invisible to every other transaction until they are actually committed.

**Definition:** Isolation guarantees that concurrently running transactions do not see each other's uncommitted, potentially-to-be-rolled-back changes, keeping a transaction's in-progress work private until it actually commits, which is what makes it safe for a real system to run many transactions against the same data at once.

![Intro visual for isolation running transactions safely together](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_intro_isolation_running_transactions_safely_together_actual3d_11c6b763.png)

## What a Transaction Can See of Its Own Changes

The `accounts` table is the familiar one from earlier in this chapter.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `accounts`

| account_id | owner_name | balance |
| --- | --- | --- |
| 1 | Meera Iyer | 50000.00 |
| 2 | Sanjay Rathi | 12000.00 |

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner_name TEXT,
    balance NUMERIC(10, 2)
);

INSERT INTO accounts (account_id, owner_name, balance) VALUES
(1, 'Meera Iyer', 50000.00),
(2, 'Sanjay Rathi', 12000.00);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahykc" 
 width="100%"
></iframe>

Expected output:

| balance |
| --- |
| 45000.00 |

Within this single transaction, the `SELECT` after the `UPDATE` correctly shows 45000.00, the reduced balance, since a transaction always sees its own uncommitted changes. Two things are true at once here:

- Isolation is not about hiding a transaction's work from itself.
- It is about what a completely different, concurrently running transaction, on a separate connection, is allowed to see before this one commits.

![Isolation letting one transaction see its own change while hiding it from another session](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_isolation_sessions_uncommitted_private.png)

## What a Concurrent Transaction Should Not See

Picture a second banking session, running at the exact same moment, checking Meera's balance while the transfer above is still in progress, sitting between its `UPDATE` and its `COMMIT`. Without isolation, that second session could read 40000.00, a balance that might still get rolled back and never actually become real.

With isolation guaranteed, the second session instead sees 45000.00, Meera's balance left over from the already-committed transfer earlier in this lesson, for as long as this transaction remains uncommitted, and only sees 40000.00 once `COMMIT` actually runs.

The following illustrates the two sessions side by side, as comments, since a single script can only run one session's statements in real sequence.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahyv4" 
 width="100%"
></iframe>

Expected output:

| balance |
| --- |
| 45000.00 |

The final `SELECT` in this script, running after `COMMIT`, correctly shows 40000.00, confirming the change is now permanent and visible to any session, including a completely fresh one that started with no knowledge of the transaction at all.

## Checking the Current Isolation Level

Every database connection operates under an `isolation level`, a named setting that controls exactly how much of one transaction's in-progress work a concurrent transaction is allowed to see. The next lesson in this course covers the specific problems isolation prevents, and a later unit covers the named levels in depth, but the setting itself can be checked right now.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahz6p" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns one row containing the current server or transaction setting. The exact value depends on the PostgreSQL environment, so compare the setting name and meaning rather than memorizing a particular value.

This reports the `isolation level` the current session is using for its transactions, `read committed` by default in PostgreSQL, which already guarantees that a transaction never sees another transaction's uncommitted changes, exactly the behavior demonstrated above.

![An isolation level dial blocking uncommitted changes from other sessions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_isolation_level_blocks_uncommitted.png)

## Why Isolation Matters for Correctness, Not Just Comfort

Without isolation, a concurrent balance check could read a value that later gets rolled back, and any decision made based on that reading, such as approving a withdrawal because a balance looked sufficient, would be based on data that never actually existed as far as the database is concerned.

Isolation is what makes it safe to run many transactions against the same data at the same time without each one having to worry about catching every other transaction mid-change.

## Isolation at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Guarantee</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A transaction sees its own changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always true, even before <code>COMMIT</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Other transactions see uncommitted changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented, under standard isolation levels</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A rolled-back change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Was never visible to any other transaction in the first place</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolation level</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A per-session setting controlling exactly how strict this separation is</td>
    </tr>
  </tbody>
</table>

## Your Turn

Check the current transaction `isolation level` for this session, then run a transaction that updates Sanjay's balance by 1000.00 without committing, and confirm within the same transaction that the change is visible there.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahzma" 
 width="100%"
></iframe>

Expected result and verification:

If you run `SHOW transaction_isolation;` followed by:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/mysql/44vkahzwr" 
 width="100%"
></iframe>

the `isolation level` reports as `read committed`, and the `SELECT` shows 13000.00, the updated balance, visible within this same transaction even before a `COMMIT` is issued.

## Conclusion

Isolation guarantees that concurrently running transactions do not see each other's uncommitted, potentially-to-be-rolled-back changes, keeping a transaction's in-progress work private until it actually commits, which is what makes it safe for a real system to run many transactions against the same data at once.

Rahul's banking app can now trust that a balance check running alongside a transfer will never read a value that might not actually stick. Isolation is a guarantee against interference; the final property in ACID guarantees that a committed transaction survives even a crash.
