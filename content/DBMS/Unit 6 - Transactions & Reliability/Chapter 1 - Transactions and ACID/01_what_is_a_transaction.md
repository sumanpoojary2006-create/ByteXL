## Introduction

Rahul is building the money-transfer feature for a banking app, and the logic sounds simple: subtract the amount from one account, add it to another. Written as two separate `UPDATE` statements, it works perfectly in every test he runs, until he imagines the app crashing, or the network dropping, in the split second between those two statements. If the first `UPDATE` completes and the second never runs, money has vanished from the system entirely, deducted from one account and credited to nowhere. This is not a hypothetical edge case; it is the exact kind of failure real systems must survive. The database's answer to this problem is the **transaction**: a group of one or more statements that the database guarantees will either all succeed together or all fail together, with no in-between state ever left visible.

## Two Statements That Need to Move as One

The `accounts` table holds a simple balance per account, the starting point for Rahul's transfer feature.

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

```postgresql with=accounts.sql
UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 5000.00 WHERE account_id = 2;

SELECT account_id, owner_name, balance FROM accounts;
```

Run on their own, these two statements move 5000.00 from Meera's account to Sanjay's, and the final balances look correct: 45000.00 and 17000.00. But nothing here tells the database that these two statements belong together as a single unit of work. If the connection dropped after the first `UPDATE` ran but before the second one did, the database would have no way of knowing that Sanjay's credit was ever supposed to happen, and 5000.00 would simply be gone.

## Wrapping Statements in a Transaction

`BEGIN` starts a transaction, and `COMMIT` ends it, making every change inside permanent all at once. Everything between those two commands is treated as a single, indivisible unit.

```postgresql with=accounts.sql
BEGIN;

UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 5000.00 WHERE account_id = 2;

COMMIT;

SELECT account_id, owner_name, balance FROM accounts;
```

The two `UPDATE` statements are now bound together by `BEGIN` and `COMMIT`. If anything went wrong between them, a crash, a `constraint` violation, an explicit cancellation, the database guarantees that neither change takes effect, not just the first one, not just the second. Only once `COMMIT` runs successfully does either change become permanent and visible to anyone else looking at the table.

## Undoing a Transaction with ROLLBACK

If something inside a transaction turns out to be wrong before `COMMIT` runs, `ROLLBACK` discards every change made since `BEGIN`, as if none of it had ever happened.

```postgresql with=accounts.sql
BEGIN;

UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 5000.00 WHERE account_id = 2;

SELECT account_id, balance FROM accounts;

ROLLBACK;

SELECT account_id, balance FROM accounts;
```

The `SELECT` immediately after the two `UPDATE` statements, while still inside the transaction, shows the changed balances, 45000.00 and 17000.00, because within the same transaction, a connection can see its own uncommitted changes. But once `ROLLBACK` runs, those changes are discarded entirely, and the final `SELECT` shows both accounts back at their original values, 50000.00 and 12000.00, exactly as if the transaction had never happened.

## Why Transactions Matter Beyond Money

Bank transfers are the classic example, but the same problem shows up anywhere two or more changes must succeed or fail together:

- Creating an order and reducing stock at the same time
- Registering a student for a course and updating a seat count
- Moving a support ticket between two queues

Any time an application needs "these changes happen together, or not at all," a transaction is the tool that guarantees it.

## Transactions at a Glance

| Command | Effect |
|---|---|
| `BEGIN` | Starts a new transaction |
| Statements in between | Changes are provisional, visible only within this transaction until committed |
| `COMMIT` | Makes every change in the transaction permanent, all at once |
| `ROLLBACK` | Discards every change made since `BEGIN`, as if it never happened |

## Your Turn

Meera wants to send 2000.00 to Sanjay, but decides midway through to cancel the transfer entirely. Write a transaction against the `accounts` table above that performs both balance updates, then rolls the whole thing back, and confirm with a final `SELECT` that both balances are unchanged.

```postgresql with=accounts.sql
-- Write your transaction below
```

If your transaction runs `BEGIN`, the two `UPDATE` statements adjusting 2000.00 in opposite directions, then `ROLLBACK`, the closing `SELECT` shows Meera still at 50000.00 and Sanjay still at 12000.00, confirming the cancelled transfer left no trace.

## Conclusion

A transaction groups one or more statements into a single unit that either commits entirely or rolls back entirely, closing the gap where a partial failure could otherwise leave data in a broken, half-changed state. Rahul's transfer feature can now guarantee that money is never deducted from one account without being credited to another. This all-or-nothing guarantee has a name, atomicity, and it is the first of four properties that define what makes a transaction trustworthy.
