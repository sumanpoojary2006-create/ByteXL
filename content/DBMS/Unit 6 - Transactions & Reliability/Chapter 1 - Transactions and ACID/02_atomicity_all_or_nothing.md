## Introduction

The previous lesson showed a transaction rolling back cleanly, by choice, with an explicit `ROLLBACK` command. Real failures are rarely that polite. A server can lose power mid-transaction, a network cable can be unplugged, an application process can crash. Rahul needs to know: does the database still guarantee "all or nothing" when the failure is not a graceful `ROLLBACK` but a genuinely unexpected crash? The answer is yes, and that guarantee has a name: **atomicity**, the first letter in ACID. Atomicity is the promise that a transaction's changes are indivisible, either every one of them takes effect, or none of them do, regardless of how or why the transaction failed to finish.

## Atomicity Protects Against More Than Explicit Rollbacks

The `accounts` table from the previous lesson is the setup here again.

```postgresql file=accounts.sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner_name TEXT,
    balance NUMERIC(10, 2)
);

INSERT INTO accounts (account_id, owner_name, balance) VALUES
(1, 'Meera Iyer', 50000.00),
(2, 'Sanjay Rathi', 12000.00);
```

A `constraint` violation partway through a transaction is one common, entirely unplanned way for a transaction to fail. Suppose a `CHECK` `constraint` requires a balance to never go negative.

```postgresql with=accounts.sql
ALTER TABLE accounts ADD CONSTRAINT balance_not_negative CHECK (balance >= 0);

BEGIN;

UPDATE accounts SET balance = balance - 60000.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 60000.00 WHERE account_id = 2;

COMMIT;

SELECT account_id, balance FROM accounts;
```

This transaction fails in a chain:

1. The first `UPDATE` would push Meera's balance to -10000.00, violating the `constraint` just added.
2. The database rejects that statement immediately, and because it happened inside a transaction, the transaction as a whole fails.
3. The second `UPDATE` never runs, and `COMMIT` has nothing to commit.

The closing `SELECT` shows both balances completely untouched, exactly as atomicity promises, even though nobody typed `ROLLBACK` by hand. The failure itself triggered the same all-or-nothing guarantee.

## What Atomicity Does Not Protect Against

It is worth being precise about what atomicity actually guarantees, since it is easy to expect too much from it. Atomicity only guarantees that a transaction's own set of changes are indivisible; it says nothing about whether those changes, once committed, make logical sense.

```postgresql with=accounts.sql
BEGIN;

UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;

COMMIT;
```

This transaction is perfectly atomic: it either commits this single `UPDATE` or it does not. But it deducts 5000.00 from Meera without crediting it anywhere, which is a logic bug, not an atomicity failure. Atomicity guarantees that whatever statements are grouped inside `BEGIN` and `COMMIT` happen together; it is still the application's responsibility to group the correct statements together in the first place. Rahul's earlier two-statement transfer was correct because both necessary statements were inside the same transaction, not because atomicity somehow inferred that a credit needed to accompany the debit.

## Atomicity and Multi-Statement Transactions

Atomicity applies to however many statements sit between `BEGIN` and `COMMIT`, not just two. A transaction with five statements offers the same guarantee as one with two: all five succeed together, or none of them take effect.

```postgresql with=accounts.sql
BEGIN;

INSERT INTO accounts (account_id, owner_name, balance) VALUES (3, 'Farah Ali', 0.00);
UPDATE accounts SET balance = balance - 1000.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 1000.00 WHERE account_id = 3;

COMMIT;

SELECT account_id, owner_name, balance FROM accounts;
```

This transaction opens a new account for Farah Ali and funds it from Meera's account, three statements acting as one atomic unit. If the `INSERT` for the new account had failed, for instance because `account_id = 3` already existed, neither `UPDATE` would take effect either, keeping Meera's balance untouched rather than deducting money toward an account that was never actually created.

## Atomicity at a Glance

| Scenario | Outcome |
|---|---|
| All statements in the transaction succeed | Every change commits together |
| Any statement fails, for any reason | Every change in that transaction is discarded |
| Explicit `ROLLBACK` | Same discard behavior, triggered on purpose |
| A committed transaction later turns out to be the wrong logic | Not an atomicity issue; atomicity only protects the grouping, not the correctness of what was grouped |

## Your Turn

Using the `balance_not_negative` `constraint` already added earlier in this lesson, attempt a transaction that tries to move 100000.00 from Sanjay's account (which only has 12000.00) to Meera's account. Confirm afterward that Sanjay's balance is unaffected.

```postgresql with=accounts.sql
-- Write your transaction below
```

If your transaction attempts `UPDATE accounts SET balance = balance - 100000.00 WHERE account_id = 2;` inside a `BEGIN`/`COMMIT` block, the statement is rejected for violating `balance_not_negative`, the transaction fails as a whole, and a closing `SELECT` confirms Sanjay's balance is still 12000.00.

## Conclusion

Atomicity guarantees that every statement inside a transaction commits together or fails together, whether the failure comes from an explicit `ROLLBACK` or an unplanned error like a `constraint` violation, though it is still up to the application to decide which statements belong grouped together in the first place. Rahul's transfer feature is now protected against partial failures of every kind, not just the ones he anticipates. Atomicity handles the transaction as a unit; the next property in ACID concerns whether the data stays logically valid throughout.
