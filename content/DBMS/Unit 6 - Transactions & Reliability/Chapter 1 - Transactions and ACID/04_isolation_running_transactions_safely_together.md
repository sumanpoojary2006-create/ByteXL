## Introduction

Every transaction covered so far has run alone, one connection, one sequence of statements, nothing else touching the database at the same time. A real banking system is never that quiet: hundreds of transfers, deposits, and balance checks can hit the same accounts within the same second. The third letter in ACID, **isolation**, is the guarantee that concurrently running transactions do not interfere with each other in ways that produce incorrect results, specifically, that one transaction's in-progress, uncommitted changes stay invisible to every other transaction until they are actually committed.

## What a Transaction Can See of Its Own Changes

The `accounts` table is the familiar one from earlier in this chapter.

```postgresql file=accounts_isolation.sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner_name TEXT,
    balance NUMERIC(10, 2)
);

INSERT INTO accounts (account_id, owner_name, balance) VALUES
(1, 'Meera Iyer', 50000.00),
(2, 'Sanjay Rathi', 12000.00);
```

```postgresql with=accounts_isolation.sql
BEGIN;

UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;

SELECT balance FROM accounts WHERE account_id = 1;

COMMIT;
```

Within this single transaction, the `SELECT` after the `UPDATE` correctly shows 45000.00, the reduced balance, since a transaction always sees its own uncommitted changes. Two things are true at once here:

- Isolation is not about hiding a transaction's work from itself.
- It is about what a completely different, concurrently running transaction, on a separate connection, is allowed to see before this one commits.

## What a Concurrent Transaction Should Not See

Picture a second banking session, running at the exact same moment, checking Meera's balance while the transfer above is still in progress, sitting between its `UPDATE` and its `COMMIT`. Without isolation, that second session could read 45000.00, a balance that might still get rolled back and never actually become real. With isolation guaranteed, the second session instead sees the original 50000.00 for as long as the first transaction remains uncommitted, and only sees 45000.00 once `COMMIT` actually runs. The following illustrates the two sessions side by side, as comments, since a single script can only run one session's statements in real sequence.

```postgresql with=accounts_isolation.sql
-- Session A (the transfer in progress)
BEGIN;
UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;
-- Session A has not committed yet.

-- Session B (a concurrent balance check, running at this exact moment)
-- SELECT balance FROM accounts WHERE account_id = 1;
-- With isolation, Session B sees 50000.00 here, not 45000.00,
-- because Session A's change is not committed yet and stays invisible to others.

-- Session A finishes:
COMMIT;
-- Only now would Session B's next SELECT see 45000.00.

SELECT balance FROM accounts WHERE account_id = 1;
```

The final `SELECT` in this script, running after `COMMIT`, correctly shows 45000.00, confirming the change is now permanent and visible to any session, including a completely fresh one that started with no knowledge of the transaction at all.

## Checking the Current Isolation Level

Every database connection operates under an `isolation level`, a named setting that controls exactly how much of one transaction's in-progress work a concurrent transaction is allowed to see. The next lesson in this course covers the specific problems isolation prevents, and a later unit covers the named levels in depth, but the setting itself can be checked right now.

```postgresql with=accounts_isolation.sql
SHOW transaction_isolation;
```

This reports the `isolation level` the current session is using for its transactions, `read committed` by default in PostgreSQL, which already guarantees that a transaction never sees another transaction's uncommitted changes, exactly the behavior demonstrated above.

## Why Isolation Matters for Correctness, Not Just Comfort

Without isolation, a concurrent balance check could read a value that later gets rolled back, and any decision made based on that reading, such as approving a withdrawal because a balance looked sufficient, would be based on data that never actually existed as far as the database is concerned. Isolation is what makes it safe to run many transactions against the same data at the same time without each one having to worry about catching every other transaction mid-change.

## Isolation at a Glance

| Guarantee | Detail |
|---|---|
| A transaction sees its own changes | Always true, even before `COMMIT` |
| Other transactions see uncommitted changes | Prevented, under standard isolation levels |
| A rolled-back change | Was never visible to any other transaction in the first place |
| Isolation level | A per-session setting controlling exactly how strict this separation is |

## Your Turn

Check the current transaction `isolation level` for this session, then run a transaction that updates Sanjay's balance by 1000.00 without committing, and confirm within the same transaction that the change is visible there.

```postgresql with=accounts_isolation.sql
-- Write your queries below
```

If you run `SHOW transaction_isolation;` followed by `BEGIN; UPDATE accounts SET balance = balance + 1000.00 WHERE account_id = 2; SELECT balance FROM accounts WHERE account_id = 2;`, the `isolation level` reports as `read committed`, and the `SELECT` shows 13000.00, the updated balance, visible within this same transaction even before a `COMMIT` is issued.

## Conclusion

Isolation guarantees that concurrently running transactions do not see each other's uncommitted, potentially-to-be-rolled-back changes, keeping a transaction's in-progress work private until it actually commits, which is what makes it safe for a real system to run many transactions against the same data at once. Rahul's banking app can now trust that a balance check running alongside a transfer will never read a value that might not actually stick. Isolation is a guarantee against interference; the final property in ACID guarantees that a committed transaction survives even a crash.
