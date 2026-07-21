## Introduction

Everything in this unit so far has been demonstrated by typing `BEGIN`, some statements, and `COMMIT` or `ROLLBACK` directly into a SQL editor. Real applications rarely work that way; a web server handling a checkout request does not have a human deciding, statement by statement, whether to commit or roll back. That decision has to be made in application code, based on whether the surrounding logic succeeded or threw an error.

Closing out this unit means connecting everything learned about `transactions`, ACID, concurrency, and `recovery`, back to the actual pattern a developer writes day to day.

**Definition:** Every guarantee this unit has built, atomicity, consistency, isolation, durability, concurrency control, and crash `recovery`, ultimately exists so that application code can follow one simple, disciplined pattern: begin a `transaction` around exactly the statements that must succeed or fail together, commit only when all of them succeed, roll back on any failure, keep the `transaction` short, and retry safely when a deadlock is the cause.

![Intro visual for transactions in application code](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_intro_transactions_in_application_code.png)

## Auto-commit: The Default Behavior Worth Knowing About

Most `database` client libraries default to auto-commit mode, where every individual statement is automatically wrapped in its own tiny `transaction` and committed immediately, unless the code explicitly starts a `transaction` itself.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `accounts`

| account_id | balance |
| --- | --- |
| 1 | 5000.00 |
| 2 | 3000.00 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    balance NUMERIC(10, 2) CHECK (balance >= 0)
);

INSERT INTO accounts (account_id, balance) VALUES (1, 5000.00), (2, 3000.00);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaezan" 
 width="100%"
></iframe>

Expected output:



| account_id | balance |
| --- | --- |
| 1 | 4500.00 |
| 2 | 3500.00 |

Run without an explicit `BEGIN`, each `UPDATE` here commits on its own, immediately, the moment it finishes, exactly the atomicity gap the very first lesson of this unit opened with.

This is the behavior every application-level bug about "half a transfer went through" traces back to:

- Code that assumed two statements would be treated as one.
- That code running under a client library's default auto-commit setting instead.

## Wrapping Related Statements Explicitly

The fix, already demonstrated throughout this unit, is for application code to explicitly start a `transaction` before the first related statement and commit only after the last one succeeds.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaezm3" 
 width="100%"
></iframe>

Expected output:



| account_id | balance |
| --- | --- |
| 1 | 4500.00 |
| 2 | 3500.00 |

In real application code, this pattern is usually expressed with a try-and-catch style structure, roughly: open a `connection`, begin a `transaction`, run the statements the business operation requires, and commit only if every one of them succeeded; if any step raises an error, catch it and roll back instead of committing. Written as pseudocode alongside the SQL it wraps, the shape looks like this:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaezw8" 
 width="100%"
></iframe>

Expected output:



| account_id | balance |
| --- | --- |
| 1 | 4500.00 |
| 2 | 3500.00 |

The `COMMIT` only ever runs if both statements succeeded without error; any exception raised by the `database`, a `constraint` violation, a deadlock, a lost `connection`, skips straight to the `ROLLBACK` branch instead, guaranteeing the `transaction` never commits a partial result.

![Application transaction flow committing on success and rolling back on error](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_app_transaction_commit_or_rollback_flow.png)

## Keeping Transactions Short

Every `lock` a `transaction` holds, covered in the concurrency control chapter, stays held until that `transaction` commits or rolls back. A `transaction` left open for a long time, whether because it is doing slow, unrelated work in between statements or because a bug forgot to commit at all, holds its `locks` the entire time, potentially blocking every other `transaction` that needs the same `rows`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf27u" 
 width="100%"
></iframe>

Expected output:



| balance |
| --- |
| 5000.00 |

The practical rule that follows directly from everything covered in this unit is: a `transaction` should contain only the `database` statements that genuinely need to succeed or fail together, and nothing slow or unrelated, such as calling an external payment gateway or waiting on user input, should ever happen while a `transaction` sits open holding `locks`.

## Letting a Failed Transaction Retry Safely

Some failures covered in this unit, deadlocks in particular, are expected to happen occasionally under normal concurrent load and are meant to be retried, not treated as a fatal application error.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf2h3" 
 width="100%"
></iframe>

Expected output:



| account_id | balance |
| --- | --- |
| 1 | 4800.00 |
| 2 | 3200.00 |

Because a deadlock victim's `transaction` is guaranteed to have been fully rolled back by the `database`, retrying it from scratch is always safe the application simply repeats the same `BEGIN` through `COMMIT` sequence again, and it typically succeeds the second time, once whatever `transaction` it was competing with has already finished.

![Application retrying the entire transaction after a deadlock rollback](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_retry_transaction_after_deadlock_rollback.png)

## Transactions in Application Code at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Practice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explicitly <code>BEGIN</code> related statements, do not rely on auto-commit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevents partial operations from committing individually</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commit only after every statement succeeds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preserves atomicity at the application level</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Roll back on any error, including unexpected ones</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Guarantees no partial result is ever committed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep transactions short, no slow external calls inside</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minimizes how long <code>locks</code> are held, reducing contention</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retry on deadlock, not on every error</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deadlock victims are always safely rollbackable; other errors may indicate a real bug</td>
    </tr>
  </tbody>
</table>

## Your Turn

Write the try-and-catch style pseudocode pattern, in SQL with comments, for a `transaction` that inserts a new account and immediately transfers 100.00 into it from account 1, including a rollback branch for any failure.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf2t5" 
 width="100%"
></iframe>

Expected result and verification:

A correct pattern opens with `-- try:` and `BEGIN;`, runs `INSERT INTO accounts (account_id, balance) VALUES (3, 0.00);` followed by the two balance-adjusting `UPDATE` statements, then `COMMIT;`, with a trailing `-- except: ROLLBACK;` comment noting that any failure at any point before `COMMIT` should `trigger` a full rollback rather than a partial commit.

## Conclusion

Every guarantee this unit has built, atomicity, consistency, isolation, durability, concurrency control, and crash `recovery`, ultimately exists so that application code can follow one simple, disciplined pattern: begin a `transaction` around exactly the statements that must succeed or fail together, commit only when all of them succeed, roll back on any failure, keep the `transaction` short, and retry safely when a deadlock is the cause.

With reliability covered from the ground up, the course now turns to making a correctly behaving `database` fast as well as correct.
