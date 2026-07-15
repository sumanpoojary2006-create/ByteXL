## Introduction

- The double-booking scenario from the previous lesson is one specific example of a broader family of problems that show up whenever `transactions` overlap in time.
- Database theory gives each pattern in that family a precise name, so that a specific symptom can be diagnosed and discussed precisely, rather than everyone just calling every concurrency bug "a race condition":

- `Dirty reads`
- `Non-repeatable reads`
- `Phantom reads`
- `Lost updates`

Naming each one clearly is what makes the next lessons, on `locking` and `isolation levels`, possible to reason about at all.

## Dirty Reads: Seeing Data That Was Never Actually Committed

A `dirty read` happens when one `transaction` reads a change made by another `transaction` that has not yet committed, and might still be rolled back.

```postgresql file=inventory.sql
CREATE TABLE inventory (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    stock_count INTEGER
);

INSERT INTO inventory (product_id, product_name, stock_count) VALUES
(1, 'Wireless Mouse', 50);
```

```postgresql with=inventory.sql
-- Transaction A: adjusting stock, not yet committed
BEGIN;
UPDATE inventory SET stock_count = 0 WHERE product_id = 1;
-- Transaction A has NOT committed yet, and may still roll back.

-- Transaction B, if it could read Transaction A's uncommitted change here,
-- would see stock_count = 0 and might tell a customer "out of stock,"
-- even though Transaction A might roll back a moment later and restore
-- the real value of 50. That incorrect, uncommitted read is a dirty read.

ROLLBACK;
-- Transaction A rolled back. If Transaction B had already acted on 0,
-- it acted on data that never actually existed.

SELECT stock_count FROM inventory WHERE product_id = 1;
```

- The final `SELECT` correctly shows 50, since PostgreSQL's default isolation level prevents `dirty reads` entirely, a concurrent `transaction` is never allowed to see this kind of in-progress, uncommitted change, exactly the isolation guarantee covered in the previous chapter.
- `Dirty reads` are catalogued here because some `databases`, or some deliberately relaxed isolation levels, do allow them, and knowing the name of the problem is what makes a setting like "read uncommitted" understandable later in this chapter.

![Dirty read showing one transaction reading an uncommitted value that later rolls back](images/03_dirty_read_uncommitted_then_rollback.png)

## Non-Repeatable Reads: The Same Query, Two Different Answers

A `non-repeatable read` happens when a `transaction` reads the same `row` twice, and gets two different values, because another `transaction` committed a change to that `row` in between the two reads.

```postgresql with=inventory.sql
-- Transaction A, checking stock twice within one longer-running transaction:
BEGIN;
SELECT stock_count FROM inventory WHERE product_id = 1;
-- Reads 50.

-- Transaction B, running fully in between A's two reads:
-- BEGIN;
-- UPDATE inventory SET stock_count = 40 WHERE product_id = 1;
-- COMMIT;
-- Transaction B commits a real, legitimate change here.

SELECT stock_count FROM inventory WHERE product_id = 1;
-- Depending on isolation level, Transaction A might now read 40,
-- a different answer than its own first read, within the same transaction.
COMMIT;
```

- Unlike a `dirty read`, the second read here would reflect genuinely committed data, so nothing incorrect was ever seen
- the issue is that a single `transaction`'s own `view` of the data changed mid-flight, which can be surprising or outright wrong for logic that assumes a value stays stable for the duration of a `transaction`.

## Phantom Reads: A Changing Set of Rows, Not Just a Changing Value

A `phantom read` is the same underlying problem as a non-repeatable read, but at the level of an entire `query`'s `row` count rather than a single `row`'s value: a `transaction` runs the same filtered `query` twice and gets a different number of `rows` back, because another `transaction` inserted or deleted matching `rows` in between.

```postgresql with=inventory.sql
-- Transaction A:
BEGIN;
SELECT COUNT(*) FROM inventory WHERE stock_count < 50;
-- Reads a count of 0, nothing is low on stock yet.

-- Transaction B, committing in between:
-- INSERT INTO inventory (product_id, product_name, stock_count) VALUES (2, 'USB Cable', 5);
-- COMMIT;

SELECT COUNT(*) FROM inventory WHERE stock_count < 50;
-- Transaction A's second identical query might now return a count of 1,
-- a "phantom" row that appeared out of nowhere mid-transaction.
COMMIT;
```

The new `row` was not a value that changed underneath Transaction A, it is an entirely new `row` matching a condition Transaction A was relying on, which is why this gets its own name distinct from a `non-repeatable read`.

![Non-repeatable read changing one row and phantom read adding a new matching row](images/04_nonrepeatable_vs_phantom_read.png)

## Lost Updates: Two Writes, One Silently Overwritten

A `lost update` happens when two `transactions` both read the same value, both calculate a new value based on that same original reading, and both write their result, with the second write silently overwriting the first, so one of the two changes disappears entirely, exactly the double-booking scenario from the previous lesson.

![Lost update where two transactions read the same value and one write overwrites the other](images/05_lost_update_overwritten_write.png)

```postgresql with=inventory.sql
-- Transaction A: sells 5 units, based on a stock reading of 50
-- Transaction B: sells 3 units, also based on the same reading of 50, at nearly the same time
-- If both compute "50 minus their own sale" independently and write it back,
-- whichever COMMIT runs second overwrites the first, and one sale's
-- worth of stock reduction is lost entirely, even though both sales were real.
UPDATE inventory SET stock_count = 50 - 5 WHERE product_id = 1;
UPDATE inventory SET stock_count = 50 - 3 WHERE product_id = 1;

SELECT stock_count FROM inventory WHERE product_id = 1;
```

The final value here is 47, reflecting only the second `UPDATE`; the first sale's reduction of 5 units was computed correctly but never actually preserved, because both updates were based on the same stale reading of 50 rather than each other's results.

## Concurrency Problems at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dirty read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reading another transaction&#x27;s uncommitted, possibly-to-be-rolled-back change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Non-repeatable read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same row read twice within one transaction returns two different values</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Phantom read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same filtered query run twice within one transaction returns a different set of rows</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lost update</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two transactions both read the same value, both write a new value based on it, one write silently disappears</td>
    </tr>
  </tbody>
</table>

## Your Turn

Using the `inventory` `table` above, write a `query` sequence that demonstrates a `lost update` on `stock_count` for product 1, where two separate deductions of 10 and 15 units are both computed from the same starting value of 50, and show what the final stock count incorrectly ends up as.

```postgresql with=inventory.sql
-- Write your queries below
```

If both updates are written as `UPDATE inventory SET stock_count = 50 - 10 WHERE product_id = 1;` and `UPDATE inventory SET stock_count = 50 - 15 WHERE product_id = 1;`, run one after the other, the final stock count is 35, reflecting only the second deduction, with the first 10-unit sale's effect on stock lost entirely.

## Conclusion

- `Dirty reads`, non-repeatable reads, phantom reads, and lost updates each name a specific way concurrent `transactions` can interfere with each other, giving a precise vocabulary for problems that would otherwise all just look like unpredictable bugs under load.
- Recognizing which one is happening is the first step toward choosing the right fix.
- The next lesson covers `locking`, the mechanism a `database` uses to prevent these problems from happening in the first place.
