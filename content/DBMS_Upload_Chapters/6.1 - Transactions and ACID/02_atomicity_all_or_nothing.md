## Introduction

- The previous lesson showed a transaction rolling back cleanly, by choice, with an explicit `ROLLBACK` command.
- Real failures are rarely that polite.
- A server can lose power mid-transaction, a network cable can be unplugged, an application process can crash.
- Rahul needs to know: does the database still guarantee "all or nothing" when the failure is not a graceful `ROLLBACK` but a genuinely unexpected crash?
- The answer is yes, and that guarantee has a name: **atomicity**, the first letter in ACID.
- Atomicity is the promise that a transaction's changes are indivisible, either every one of them takes effect, or none of them do, regardless of how or why the transaction failed to finish.

**Definition:** Atomicity guarantees that every statement inside a transaction commits together or fails together, whether the failure comes from an explicit `ROLLBACK` or an unplanned error like a constraint violation, though it is still up to the application to decide which statements belong grouped together in the first place.

![Intro visual for atomicity all or nothing](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_intro_atomicity_all_or_nothing_actual3d_fa767ec0.png)

## Atomicity Protects Against More Than Explicit Rollbacks

The `accounts` table from the previous lesson is the setup here again.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `accounts`

| account_id | owner_name | balance |
| --- | --- | --- |
| 1 | Meera Iyer | 50000.00 |
| 2 | Sanjay Rathi | 12000.00 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

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

A constraint violation partway through a transaction is one common, entirely unplanned way for a transaction to fail. Suppose a `CHECK` constraint requires a balance to never go negative.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahx9e" 
 width="100%"
></iframe>

Expected result: the constraint is added successfully, and the final `SELECT` still shows the original account balances. If the commented invalid transfer is enabled, PostgreSQL rejects it because it would create a negative balance.

This transaction fails in a chain:

1. The first `UPDATE` would push Meera's balance to -10000.00, violating the constraint just added.

2. The database rejects that statement immediately, and because it happened inside a transaction, the transaction as a whole fails.

3. The second `UPDATE` never runs, and `COMMIT` has nothing to commit.

The closing `SELECT` shows both balances completely untouched, exactly as atomicity promises, even though nobody typed `ROLLBACK` by hand. The failure itself triggered the same all-or-nothing guarantee.

![Atomicity discarding the whole transaction when one statement fails](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_atomicity_failure_discards_transaction.png)

## What Atomicity Does Not Protect Against

It is worth being precise about what atomicity actually guarantees, since it is easy to expect too much from it. Atomicity only guarantees that a transaction's own set of changes are indivisible; it says nothing about whether those changes, once committed, make logical sense.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahxj8" 
 width="100%"
></iframe>

Expected observation: PostgreSQL completes the transaction-control statements. Use the following explanation and any closing `SELECT` to verify whether the changes were committed or rolled back.

This transaction is perfectly atomic: it either commits this single `UPDATE` or it does not. But it deducts 5000.00 from Meera without crediting it anywhere, which is a logic bug, not an atomicity failure. Atomicity guarantees that whatever statements are grouped inside `BEGIN` and `COMMIT` happen together; it is still the application's responsibility to group the correct statements together in the first place.

Rahul's earlier two-statement transfer was correct because both necessary statements were inside the same transaction, not because atomicity somehow inferred that a credit needed to accompany the debit.

## Atomicity and Multi-Statement Transactions

Atomicity applies to however many statements sit between `BEGIN` and `COMMIT`, not just two. A transaction with five statements offers the same guarantee as one with two: all five succeed together, or none of them take effect.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahxvu" 
 width="100%"
></iframe>

Expected output:



| account_id | owner_name | balance |
| --- | --- | --- |
| 1 | Meera Iyer | 49000.00 |
| 2 | Sanjay Rathi | 12000.00 |
| 3 | Farah Ali | 1000.00 |

This transaction opens a new account for Farah Ali and funds it from Meera's account, three statements acting as one atomic unit. If the `INSERT` for the new account had failed, for instance because `account_id = 3` already existed, neither `UPDATE` would take effect either, keeping Meera's balance untouched rather than deducting money toward an account that was never actually created.

![Atomicity treating many statements as one all-or-nothing unit](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_atomicity_all_statements_one_unit.png)

## Atomicity at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Scenario</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Outcome</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All statements in the transaction succeed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every change commits together</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any statement fails, for any reason</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every change in that transaction is discarded</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explicit <code>ROLLBACK</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Same discard behavior, triggered on purpose</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A committed transaction later turns out to be the wrong logic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not an atomicity issue; atomicity only protects the grouping, not the correctness of what was grouped</td>
    </tr>
  </tbody>
</table>

## Your Turn

Using the `balance_not_negative` constraint already added earlier in this lesson, attempt a transaction that tries to move 100000.00 from Sanjay's account (which only has 12000.00) to Meera's account. Confirm afterward that Sanjay's balance is unaffected.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahy85" 
 width="100%"
></iframe>

Expected result and verification:

If your transaction attempts `UPDATE accounts SET balance = balance - 100000.00 WHERE account_id = 2;` inside a `BEGIN`/`COMMIT` block, the statement is rejected for violating `balance_not_negative`, the transaction fails as a whole, and a closing `SELECT` confirms Sanjay's balance is still 12000.00.

## Conclusion

Atomicity guarantees that every statement inside a transaction commits together or fails together, whether the failure comes from an explicit `ROLLBACK` or an unplanned error like a constraint violation, though it is still up to the application to decide which statements belong grouped together in the first place. Rahul's transfer feature is now protected against partial failures of every kind, not just the ones he anticipates.

Atomicity handles the transaction as a unit; the next property in ACID concerns whether the data stays logically valid throughout.
