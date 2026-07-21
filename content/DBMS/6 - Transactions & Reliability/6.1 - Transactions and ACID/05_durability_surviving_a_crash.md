## Introduction

Rahul's transfer feature now groups statements atomically, keeps the data consistent, and isolates concurrent `transactions` from each other's in-progress work. One question remains, and it is the one that matters most the instant something actually goes wrong: once `COMMIT` has run and told the customer "your transfer succeeded," what happens if the server loses power one second later?

The fourth letter in ACID, **durability**, is the guarantee that once a `transaction` has committed, its changes are permanent, surviving a crash, a power loss, or a restart, even if the change had only existed in memory a moment before.

**Definition:** Durability closes the loop that atomicity, consistency, and isolation open: once a `transaction` commits, its result is guaranteed permanent, surviving any crash, because the `database` records it somewhere durable before ever reporting success.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_durability_surviving_a_crash.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Rahul's transfer feature now groups statements atomically, keeps the data consistent, and isolates concurrent transactions from each other's in-progress work. One question remains, and it is the one that matters most the instant something actually goes wrong.

ON-IMAGE TEXT: show a short bold title "Durability Surviving A Crash" plus only these few labels, large and legible: Transaction, Commit, Durability. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for durability surviving a crash](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_intro_durability_surviving_a_crash_matched_33aa4771.png)

## COMMIT Means Permanent, Not Just Visible

The `accounts` `table` is the same one used throughout this chapter.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `accounts`

| account_id | owner_name | balance |
| --- | --- | --- |
| 1 | Meera Iyer | 50000.00 |
| 2 | Sanjay Rathi | 12000.00 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
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

```postgresql with=init.sql
BEGIN;
UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 5000.00 WHERE account_id = 2;
COMMIT;

SELECT account_id, balance FROM accounts;
```

Expected output:



| account_id | balance |
| --- | --- |
| 1 | 45000.00 |
| 2 | 17000.00 |

Once `COMMIT` finishes here, durability guarantees this new balance is not sitting only in server memory, waiting to disappear the moment power is lost. The `database` has already made sure this change is recorded somewhere that survives a crash, before it ever reported success back to Rahul's application.

![COMMIT writing a transaction result to durable storage so it survives a crash](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_durability_commit_survives_crash.png)

This is a meaningfully different promise from isolation:

- Isolation was about what other `transactions` can see while a `transaction` is still in progress.
- Durability is about what happens to a `transaction`'s result after it has already finished successfully.

## How Databases Deliver on This Promise

A `database` cannot simply keep committed data in memory and hope nothing goes wrong before it eventually gets written to disk, since memory is erased by a power loss. Instead, most relational `databases`, including PostgreSQL, use a technique called `write-ahead logging`: before a `transaction` is allowed to report success, its changes are first written to a durable log on disk.

If the server crashes immediately after, that log is what the `database` replays on restart to reconstruct any committed work that had not yet been fully applied to the main data files. The mechanics of that log are worth a closer look on their own, but the guarantee it exists to provide is simple: `COMMIT` does not return success until the change is already somewhere that a crash cannot erase.

## A Setting That Trades Durability for Speed

Durability is not free; forcing every commit to wait for a disk write takes real time, which is why some `databases` expose a setting to relax this guarantee for performance-sensitive situations. PostgreSQL's `synchronous_commit` setting is one example, and checking it shows how explicit this trade-off is.

```postgresql with=init.sql
SHOW synchronous_commit;
```

Expected observation: PostgreSQL returns one row containing the current server or transaction setting. The exact value depends on the OneCompiler PostgreSQL environment, so compare the setting name and meaning rather than memorizing a particular value.

The default value, `on`, means every `COMMIT` waits until its change is safely recorded before reporting success, the full durability guarantee. Turning this off in a real system would make commits faster, but it would reopen exactly the risk durability exists to close: a very recent commit could theoretically be lost if the server crashed in the narrow window before its record was actually written to durable storage.

This setting is not something a banking application should ever turn off, but it exists precisely because durability, like every guarantee in this chapter, is a deliberate engineering choice, not an automatic law of nature.

## Durability Applies Only After COMMIT

It is worth being precise about the boundary here. Everything before `COMMIT` is provisional, and a crash during an uncommitted `transaction` is expected to lose that `transaction`'s work entirely, which is exactly what atomicity already promises, an incomplete `transaction` should never partially survive.

```postgresql with=init.sql
BEGIN;
UPDATE accounts SET balance = balance - 1000.00 WHERE account_id = 1;
-- A crash here, before COMMIT, is expected to lose this change entirely.
-- Durability makes no promise about uncommitted work; atomicity already
-- guarantees it should not survive in a half-applied state.
```

Expected observation: PostgreSQL completes the transaction-control statements. Use the following explanation and any closing `SELECT` to verify whether the changes were committed or rolled back.

Durability only ever protects a `transaction` once it has fully committed. A `transaction` that never reaches `COMMIT` is supposed to disappear on failure, whether that failure is an explicit `ROLLBACK` or a crash; durability's job begins exactly where atomicity's job for that `transaction` ends.

## ACID at a Glance, All Four Properties Together

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Property</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Guarantee</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Atomicity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A transaction&#x27;s statements succeed together or fail together</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A transaction can only move the database between valid states</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concurrent transactions do not see each other&#x27;s uncommitted changes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Durability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Once committed, a transaction&#x27;s changes survive any crash</td>
    </tr>
  </tbody>
</table>

![The four ACID properties supporting a safe transaction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_acid_four_properties_summary.png)

## Your Turn

Check the current `synchronous_commit` setting, then run a committed `transaction` that adds 500.00 to Sanjay's balance, and confirm the change is reflected with a final `SELECT`, reasoning through why that result would still hold even if the server crashed the instant after `COMMIT` returned.

```postgresql with=init.sql
-- Write your queries below
```

Expected result and verification:

If you run `SHOW synchronous_commit;` followed by:

```sql
BEGIN;
UPDATE accounts SET balance = balance + 500.00 WHERE account_id = 2;
COMMIT;
SELECT balance FROM accounts WHERE account_id = 2;
```

the balance shows 12500.00, and durability is the reason that value can be trusted to still be there even after an immediate crash, since `COMMIT` would not have returned successfully until the change was already recorded somewhere a crash cannot erase.

## Conclusion

Durability closes the loop that atomicity, consistency, and isolation open: once a `transaction` commits, its result is guaranteed permanent, surviving any crash, because the `database` records it somewhere durable before ever reporting success. Together, the four ACID properties are what let Rahul tell a customer "your transfer succeeded" and mean it unconditionally.

With all four properties covered individually, the next chapter looks at what specifically goes wrong when `transactions` run concurrently without enough care, and how a `database` prevents it.
