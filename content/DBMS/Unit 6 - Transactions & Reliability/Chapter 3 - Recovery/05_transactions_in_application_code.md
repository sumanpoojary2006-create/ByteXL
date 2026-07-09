## Introduction

Everything in this unit so far has been demonstrated by typing `BEGIN`, some statements, and `COMMIT` or `ROLLBACK` directly into a SQL editor. Real applications rarely work that way; a web server handling a checkout request does not have a human deciding, statement by statement, whether to commit or roll back. That decision has to be made in application code, based on whether the surrounding logic succeeded or threw an error. Closing out this unit means connecting everything learned about transactions, ACID, concurrency, and recovery, back to the actual pattern a developer writes day to day.

## Auto-commit: The Default Behavior Worth Knowing About

Most database client libraries default to auto-commit mode, where every individual statement is automatically wrapped in its own tiny transaction and committed immediately, unless the code explicitly starts a transaction itself.

```postgresql file=app_transactions.sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    balance NUMERIC(10, 2) CHECK (balance >= 0)
);

INSERT INTO accounts (account_id, balance) VALUES (1, 5000.00), (2, 3000.00);
```

```postgresql with=app_transactions.sql
UPDATE accounts SET balance = balance - 500.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 500.00 WHERE account_id = 2;

SELECT * FROM accounts;
```

Run without an explicit `BEGIN`, each `UPDATE` here commits on its own, immediately, the moment it finishes, exactly the atomicity gap the very first lesson of this unit opened with.

This is the behavior every application-level bug about "half a transfer went through" traces back to:

- Code that assumed two statements would be treated as one.
- That code running under a client library's default auto-commit setting instead.

## Wrapping Related Statements Explicitly

The fix, already demonstrated throughout this unit, is for application code to explicitly start a transaction before the first related statement and commit only after the last one succeeds.

```postgresql with=app_transactions.sql
BEGIN;
UPDATE accounts SET balance = balance - 500.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 500.00 WHERE account_id = 2;
COMMIT;

SELECT * FROM accounts;
```

In real application code, this pattern is usually expressed with a try-and-catch style structure, roughly: open a connection, begin a transaction, run the statements the business operation requires, and commit only if every one of them succeeded; if any step raises an error, catch it and roll back instead of committing. Written as pseudocode alongside the SQL it wraps, the shape looks like this:

```postgresql with=app_transactions.sql
-- try:
BEGIN;
UPDATE accounts SET balance = balance - 500.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 500.00 WHERE account_id = 2;
COMMIT;
-- except any error during the above:
--     ROLLBACK;
--     re-raise or report the failure to the caller

SELECT * FROM accounts;
```

The `COMMIT` only ever runs if both statements succeeded without error; any exception raised by the database, a `constraint` violation, a deadlock, a lost connection, skips straight to the `ROLLBACK` branch instead, guaranteeing the transaction never commits a partial result.

## Keeping Transactions Short

Every `lock` a transaction holds, covered in the concurrency control chapter, stays held until that transaction commits or rolls back. A transaction left open for a long time, whether because it is doing slow, unrelated work in between statements or because a bug forgot to commit at all, holds its `locks` the entire time, potentially blocking every other transaction that needs the same rows.

```postgresql with=app_transactions.sql
BEGIN;
SELECT balance FROM accounts WHERE account_id = 1 FOR UPDATE;
-- A well-behaved application does the minimum necessary work here,
-- then commits quickly, rather than pausing for a slow external call,
-- like a network request or a user confirmation, while still holding this lock.
UPDATE accounts SET balance = balance - 100.00 WHERE account_id = 1;
COMMIT;
```

The practical rule that follows directly from everything covered in this unit is: a transaction should contain only the database statements that genuinely need to succeed or fail together, and nothing slow or unrelated, such as calling an external payment gateway or waiting on user input, should ever happen while a transaction sits open holding `locks`.

## Letting a Failed Transaction Retry Safely

Some failures covered in this unit, deadlocks in particular, are expected to happen occasionally under normal concurrent load and are meant to be retried, not treated as a fatal application error.

```postgresql with=app_transactions.sql
-- try:
BEGIN;
UPDATE accounts SET balance = balance - 200.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 200.00 WHERE account_id = 2;
COMMIT;
-- except deadlock error specifically:
--     ROLLBACK;
--     wait a short, small random delay;
--     retry the entire transaction from the beginning

SELECT * FROM accounts;
```

Because a deadlock victim's transaction is guaranteed to have been fully rolled back by the database, retrying it from scratch is always safe; the application simply repeats the same `BEGIN` through `COMMIT` sequence again, and it typically succeeds the second time, once whatever transaction it was competing with has already finished.

## Transactions in Application Code at a Glance

| Practice | Why |
|---|---|
| Explicitly `BEGIN` related statements, do not rely on auto-commit | Prevents partial operations from committing individually |
| Commit only after every statement succeeds | Preserves atomicity at the application level |
| Roll back on any error, including unexpected ones | Guarantees no partial result is ever committed |
| Keep transactions short, no slow external calls inside | Minimizes how long `locks` are held, reducing contention |
| Retry on deadlock, not on every error | Deadlock victims are always safely rollbackable; other errors may indicate a real bug |

## Your Turn

Write the try-and-catch style pseudocode pattern, in SQL with comments, for a transaction that inserts a new account and immediately transfers 100.00 into it from account 1, including a rollback branch for any failure.

```postgresql with=app_transactions.sql
-- Write your transaction below
```

A correct pattern opens with `-- try:` and `BEGIN;`, runs `INSERT INTO accounts (account_id, balance) VALUES (3, 0.00);` followed by the two balance-adjusting `UPDATE` statements, then `COMMIT;`, with a trailing `-- except: ROLLBACK;` comment noting that any failure at any point before `COMMIT` should trigger a full rollback rather than a partial commit.

## Conclusion

Every guarantee this unit has built, atomicity, consistency, isolation, durability, concurrency control, and crash recovery, ultimately exists so that application code can follow one simple, disciplined pattern: begin a transaction around exactly the statements that must succeed or fail together, commit only when all of them succeed, roll back on any failure, keep the transaction short, and retry safely when a deadlock is the cause. With reliability covered from the ground up, the course now turns to making a correctly behaving database fast as well as correct.
