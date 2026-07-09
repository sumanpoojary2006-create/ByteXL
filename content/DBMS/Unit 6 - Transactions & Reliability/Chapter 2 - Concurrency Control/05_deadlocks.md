## Introduction

`Locking` prevents two transactions from conflicting over the same row, but it introduces a new failure mode of its own: two transactions can each hold a `lock` the other one needs, with neither willing to let go until it gets what it is waiting for. Picture Transaction A `locking` account 1 and then trying to `lock` account 2, while at nearly the same moment, Transaction B has already `locked` account 2 and is now trying to `lock` account 1. Each transaction is waiting on the other, forever, unless something intervenes. This standoff is called a **deadlock**, and every production database includes a mechanism specifically to detect and break it.

## How a Deadlock Forms

The `accounts` table sets up the scenario, two accounts that two different transfer transactions both need to touch, in opposite order.

```postgresql file=accounts_deadlock.sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner_name TEXT,
    balance NUMERIC(10, 2)
);

INSERT INTO accounts (account_id, owner_name, balance) VALUES
(1, 'Meera Iyer', 50000.00),
(2, 'Sanjay Rathi', 12000.00);
```

```postgresql with=accounts_deadlock.sql
-- Transaction A: transferring from account 1 to account 2
BEGIN;
UPDATE accounts SET balance = balance - 1000.00 WHERE account_id = 1;
-- Transaction A now holds a lock on account 1, and next wants account 2.

-- Transaction B, running concurrently: transferring from account 2 to account 1
-- BEGIN;
-- UPDATE accounts SET balance = balance - 500.00 WHERE account_id = 2;
-- Transaction B now holds a lock on account 2, and next wants account 1.

-- Transaction A tries to continue:
-- UPDATE accounts SET balance = balance + 1000.00 WHERE account_id = 2;
-- This would need to wait for Transaction B's lock on account 2 to release.

-- Transaction B tries to continue:
-- UPDATE accounts SET balance = balance + 500.00 WHERE account_id = 1;
-- This would need to wait for Transaction A's lock on account 1 to release.

-- Neither transaction can proceed, and neither will release its lock until it does.
-- This is a deadlock.

ROLLBACK;
```

Each transaction is individually doing something perfectly reasonable, `locking` one row and then requesting a second row it needs, but the two together form a cycle: A waits on B, and B waits on A, with no possible way for either to naturally continue.

## How the Database Breaks a Deadlock

A database does not simply let two transactions wait forever. PostgreSQL, like other production databases, continuously watches for exactly this kind of waiting cycle, and once it detects one:

1. It forcibly aborts one of the two transactions.
2. It rolls that transaction back and raises a deadlock error.
3. The other transaction is freed to continue.

```postgresql with=accounts_deadlock.sql
-- If a real deadlock were detected here, the database's response would look like:
-- ERROR: deadlock detected
-- DETAIL: Process 1234 waits for ShareLock on transaction 5678; blocked by process 5678.
--         Process 5678 waits for ShareLock on transaction 1234; blocked by process 1234.
-- HINT: See server log for query details.

SELECT * FROM accounts;
```

The specific transaction chosen as the "victim" is typically whichever one the database determines is cheapest to roll back, and the application on the receiving end of that error is expected to catch it and retry the whole transaction from the beginning, this time likely succeeding, since the other transaction has usually finished by the time the retry runs.

## Preventing Deadlocks Through Consistent Lock Ordering

The most reliable way to avoid deadlocks in application code is to make sure every transaction that touches multiple rows always `locks` them in the same, consistent order, for example, always `locking` the account with the lower `account_id` first, regardless of which direction money is moving.

```postgresql with=accounts_deadlock.sql
-- A deadlock-safe version of both transfer transactions, always locking
-- the lower account_id first:
BEGIN;
SELECT * FROM accounts WHERE account_id = 1 FOR UPDATE;
SELECT * FROM accounts WHERE account_id = 2 FOR UPDATE;

UPDATE accounts SET balance = balance - 1000.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 1000.00 WHERE account_id = 2;

COMMIT;
```

If every transaction, regardless of which direction it transfers money, always `locks` account 1 before account 2 whenever both are involved, the circular waiting pattern from the earlier example can never form: whichever transaction gets to account 1 first simply makes the other one wait its turn, in a straight line rather than a cycle.

## Deadlocks at a Glance

| Concept | Detail |
|---|---|
| Deadlock | Two or more transactions waiting on `locks` held by each other, in a cycle |
| Detection | The database actively watches for waiting cycles |
| Resolution | One transaction is automatically rolled back to break the cycle |
| Application's responsibility | Catch the deadlock error and retry the transaction |
| Best prevention | Always `lock` multiple rows in the same, consistent order |

## Your Turn

Rewrite a two-account transfer transaction against the `accounts` table above so that it `locks` both rows with `FOR UPDATE` in ascending `account_id` order before making any changes, regardless of which account the money is conceptually coming from.

```postgresql with=accounts_deadlock.sql
-- Write your transaction below
```

A deadlock-safe version `locks` the lower id first regardless of transfer direction: `BEGIN; SELECT * FROM accounts WHERE account_id = 1 FOR UPDATE; SELECT * FROM accounts WHERE account_id = 2 FOR UPDATE; UPDATE accounts SET balance = balance + 500.00 WHERE account_id = 1; UPDATE accounts SET balance = balance - 500.00 WHERE account_id = 2; COMMIT;`, and following this same ordering convention everywhere in the application prevents the circular wait that causes a deadlock.

## Conclusion

A deadlock forms when two transactions each hold a `lock` the other needs, a cycle the database detects automatically and breaks by rolling back one of the two transactions, leaving the application to retry, and the most reliable prevention is `locking` multiple rows in a consistent order across every transaction in the system. With `locking`, `isolation levels`, and deadlocks all covered, the final piece is naming the standard every one of these mechanisms is ultimately working to uphold.
