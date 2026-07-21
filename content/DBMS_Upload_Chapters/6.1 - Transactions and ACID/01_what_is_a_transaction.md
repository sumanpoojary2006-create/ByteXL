## Introduction

Rahul is building the money-transfer feature for a banking app, and the logic sounds simple: subtract the amount from one account, add it to another. Written as two separate `UPDATE` statements, it works perfectly in every test he runs, until he imagines the app crashing, or the network dropping, in the split second between those two statements.

If the first `UPDATE` completes and the second never runs, money has vanished from the system entirely, deducted from one account and credited to nowhere. This is not a hypothetical edge case; it is the exact kind of failure real systems must survive.

The database's answer to this problem is the **transaction**: a group of one or more statements that the database guarantees will either all succeed together or all fail together, with no in-between state ever left visible.

**Definition:** A transaction groups one or more statements into a single unit that either commits entirely or rolls back entirely, closing the gap where a partial failure could otherwise leave data in a broken, half-changed state.

![Intro visual for what is a transaction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_what_is_a_transaction.png)

## Two Statements That Need to Move as One

The `accounts` table holds a simple balance per account, the starting point for Rahul's transfer feature.

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

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj4x8" 
 width="100%"
></iframe>

Expected output:



| account_id | owner_name | balance |
| --- | --- | --- |
| 1 | Meera Iyer | 45000.00 |
| 2 | Sanjay Rathi | 17000.00 |

Run on their own, these two statements move 5000.00 from Meera's account to Sanjay's, and the final balances look correct: 45000.00 and 17000.00. But nothing here tells the database that these two statements belong together as a single unit of work.

If the connection dropped after the first `UPDATE` ran but before the second one did, the database would have no way of knowing that Sanjay's credit was ever supposed to happen, and 5000.00 would simply be gone.

## Wrapping Statements in a Transaction

`BEGIN` starts a transaction, and `COMMIT` ends it, making every change inside permanent all at once. Everything between those two commands is treated as a single, indivisible unit.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj58w" 
 width="100%"
></iframe>

Expected output:



| account_id | owner_name | balance |
| --- | --- | --- |
| 1 | Meera Iyer | 45000.00 |
| 2 | Sanjay Rathi | 17000.00 |

The two `UPDATE` statements are now bound together by `BEGIN` and `COMMIT`. If anything went wrong between them, a crash, a constraint violation, an explicit cancellation, the database guarantees that neither change takes effect, not just the first one, not just the second. Only once `COMMIT` runs successfully does either change become permanent and visible to anyone else looking at the table.

![A transaction wrapping debit and credit updates so they move as one unit](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_transaction_wraps_debit_credit.png)

## Undoing a Transaction with ROLLBACK

If something inside a transaction turns out to be wrong before `COMMIT` runs, `ROLLBACK` discards every change made since `BEGIN`, as if none of it had ever happened.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj5jq" 
 width="100%"
></iframe>

Expected output 1:



| account_id | balance |
| --- | --- |
| 1 | 45000.00 |
| 2 | 17000.00 |

Expected output 2:



| account_id | balance |
| --- | --- |
| 1 | 50000.00 |
| 2 | 12000.00 |

The `SELECT` immediately after the two `UPDATE` statements, while still inside the transaction, shows the changed balances, 45000.00 and 17000.00, because within the same transaction, a connection can see its own uncommitted changes. But once `ROLLBACK` runs, those changes are discarded entirely, and the final `SELECT` shows both accounts back at their original values, 50000.00 and 12000.00, exactly as if the transaction had never happened.

![ROLLBACK undoing provisional changes before they are committed](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_rollback_undoes_uncommitted_changes.png)

## Why Transactions Matter Beyond Money

Bank transfers are the classic example, but the same problem shows up anywhere two or more changes must succeed or fail together:

- Creating an order and reducing stock at the same time
- Registering a student for a course and updating a seat count
- Moving a support ticket between two queues

Any time an application needs "these changes happen together, or not at all," a transaction is the tool that guarantees it.

## Transactions at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Command</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effect</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>BEGIN</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Starts a new transaction</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Statements in between</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes are provisional, visible only within this transaction until committed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>COMMIT</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Makes every change in the transaction permanent, all at once</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ROLLBACK</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discards every change made since <code>BEGIN</code>, as if it never happened</td>
    </tr>
  </tbody>
</table>

## Your Turn

Meera wants to send 2000.00 to Sanjay, but decides midway through to cancel the transfer entirely. Write a transaction against the `accounts` table above that performs both balance updates, then rolls the whole thing back, and confirm with a final `SELECT` that both balances are unchanged.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj5uk" 
 width="100%"
></iframe>

Expected result and verification:

If your transaction runs `BEGIN`, the two `UPDATE` statements adjusting 2000.00 in opposite directions, then `ROLLBACK`, the closing `SELECT` shows Meera still at 50000.00 and Sanjay still at 12000.00, confirming the cancelled transfer left no trace.

## Conclusion

A transaction groups one or more statements into a single unit that either commits entirely or rolls back entirely, closing the gap where a partial failure could otherwise leave data in a broken, half-changed state. Rahul's transfer feature can now guarantee that money is never deducted from one account without being credited to another.

This all-or-nothing guarantee has a name, atomicity, and it is the first of four properties that define what makes a transaction trustworthy.
