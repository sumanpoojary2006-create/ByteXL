## Introduction

- `Locking` prevents two `transactions` from conflicting over the same `row`, but it introduces a new failure mode of its own: two `transactions` can each hold a `lock` the other one needs, with neither willing to let go until it gets what it is waiting for.
- Picture Transaction A `locking` account 1 and then trying to `lock` account 2, while at nearly the same moment, Transaction B has already `locked` account 2 and is now trying to `lock` account 1.
- Each `transaction` is waiting on the other, forever, unless something intervenes.
- This standoff is called a **deadlock**, and every production `database` includes a mechanism specifically to detect and break it.

**Definition:** A deadlock forms when two `transactions` each hold a `lock` the other needs, a cycle the `database` detects automatically and breaks by rolling back one of the two `transactions`, leaving the application to retry, and the most reliable prevention is `locking` multiple `rows` in a consistent order across every `transaction` in the system.

![Intro visual for deadlocks](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_intro_deadlocks.png)

## How a Deadlock Forms

The `accounts` `table` sets up the scenario, two accounts that two different transfer `transactions` both need to touch, in opposite order.

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
 src="https://onecompiler.com/embed/postgresql/44vkafcf5" 
 width="100%"
></iframe>

Expected observation: PostgreSQL completes the transaction-control statements. Use the following explanation and any closing `SELECT` to verify whether the changes were committed or rolled back.

Each `transaction` is individually doing something perfectly reasonable, `locking` one `row` and then requesting a second `row` it needs, but the two together form a cycle: A waits on B, and B waits on A, with no possible way for either to naturally continue.

![A deadlock cycle where Transaction A waits for B and Transaction B waits for A](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_deadlock_wait_cycle.png)

## How the Database Breaks a Deadlock

A `database` does not simply let two `transactions` wait forever. PostgreSQL, like other production `databases`, continuously watches for exactly this kind of waiting cycle, and once it detects one:

1. It forcibly aborts one of the two `transactions`.

2. It rolls that `transaction` back and raises a deadlock error.

3. The other `transaction` is freed to continue.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafcrr" 
 width="100%"
></iframe>

Expected output:



| account_id | owner_name | balance |
| --- | --- | --- |
| 1 | Meera Iyer | 50000.00 |
| 2 | Sanjay Rathi | 12000.00 |

The specific `transaction` chosen as the "victim" is typically whichever one the `database` determines is cheapest to roll back, and the application on the receiving end of that error is expected to catch it and retry the whole `transaction` from the beginning, this time likely succeeding, since the other `transaction` has usually finished by the time the retry runs.

## Preventing Deadlocks Through Consistent Lock Ordering

The most reliable way to avoid deadlocks in application code is to make sure every `transaction` that touches multiple `rows` always `locks` them in the same, consistent order, for example, always `locking` the account with the lower `account_id` first, regardless of which direction money is moving.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafd2x" 
 width="100%"
></iframe>

Expected output 1:



| account_id | owner_name | balance |
| --- | --- | --- |
| 1 | Meera Iyer | 50000.00 |

Expected output 2:



| account_id | owner_name | balance |
| --- | --- | --- |
| 2 | Sanjay Rathi | 12000.00 |

If every `transaction`, regardless of which direction it transfers money, always `locks` account 1 before account 2 whenever both are involved, the circular waiting pattern from the earlier example can never form: whichever `transaction` gets to account 1 first simply makes the other one wait its turn, in a straight line rather than a cycle.

![Preventing deadlocks by locking accounts in the same consistent order](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_deadlock_prevention_same_lock_order.png)

## Deadlocks at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deadlock</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two or more transactions waiting on <code>locks</code> held by each other, in a cycle</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The database actively watches for waiting cycles</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resolution</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One transaction is automatically rolled back to break the cycle</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Application&#x27;s responsibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Catch the deadlock error and retry the transaction</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Best prevention</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always <code>lock</code> multiple rows in the same, consistent order</td>
    </tr>
  </tbody>
</table>

## Your Turn

Rewrite a two-account transfer `transaction` against the `accounts` `table` above so that it `locks` both `rows` with `FOR UPDATE` in ascending `account_id` order before making any changes, regardless of which account the money is conceptually coming from.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafdd2" 
 width="100%"
></iframe>

Expected result and verification:

A deadlock-safe version `locks` the lower id first regardless of transfer direction:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/mysql/44vkafdp5" 
 width="100%"
></iframe>

Following this same ordering convention everywhere in the application prevents the circular wait that causes a deadlock.

## Conclusion

A deadlock forms when two `transactions` each hold a `lock` the other needs, a cycle the `database` detects automatically and breaks by rolling back one of the two `transactions`, leaving the application to retry, and the most reliable prevention is `locking` multiple `rows` in a consistent order across every `transaction` in the system. With `locking`, `isolation levels`, and deadlocks all covered, the final piece is naming the standard every one of these mechanisms is ultimately working to uphold.
