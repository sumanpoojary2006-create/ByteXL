## Introduction

The `lost update` from the previous lesson happened because two `transactions` both read the same stock count and both wrote a new value based on that same stale reading, with neither `transaction` aware the other was doing the same thing at the same time.

The fix is not clever application logic checking timestamps after the fact; it is stopping the second `transaction` from reading and acting on that value until the first `transaction` has finished with it entirely. This is what **locking** does: a `transaction` can claim a `lock` on a `row`, blocking other `transactions` from making conflicting changes to that same `row` until the `lock` is released.

**Definition:** `Locking` gives a `transaction` exclusive claim over a `row` it intends to change, forcing other `transactions` that want to touch the same `row` to wait until the `lock` is released, which is what actually prevents `lost updates` and similar conflicts rather than just naming them.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_locking.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: The lost update from the previous lesson happened because two transactions both read the same stock count and both wrote a new value based on that same stale reading, with neither transaction aware the other was doing the same thing at the same time. The fix.

ON-IMAGE TEXT: show a short bold title "Locking" plus only these few labels, large and legible: Transaction, Locking, Update. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for locking](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_intro_locking_actual3d_95393697.png)

## Locking a Row for Update

The `inventory` `table` from the previous lesson is the setup again.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `inventory`

| product_id | product_name | stock_count |
| --- | --- | --- |
| 1 | Wireless Mouse | 50 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE TABLE inventory (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    stock_count INTEGER
);

INSERT INTO inventory (product_id, product_name, stock_count) VALUES
(1, 'Wireless Mouse', 50);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
BEGIN;

SELECT stock_count FROM inventory WHERE product_id = 1 FOR UPDATE;

UPDATE inventory SET stock_count = stock_count - 5 WHERE product_id = 1;

COMMIT;

SELECT stock_count FROM inventory WHERE product_id = 1;
```

Expected output 1:



| stock_count |
| --- |
| 50 |

Expected output 2:



| stock_count |
| --- |
| 45 |

- `FOR UPDATE`, added to the end of a `SELECT`, tells the `database` that this `transaction` intends to modify the `row` it just read, and claims a `lock` on that `row` immediately.
- Any other `transaction` that also tries one of these is forced to wait until this `transaction` either commits or rolls back and releases the `lock`:

![SELECT FOR UPDATE placing an exclusive row lock while another transaction waits](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_select_for_update_row_lock.png)

- `SELECT ... FOR UPDATE` on the same `row`
- An `UPDATE` directly against it If a second sale `transaction` had tried to `lock` and read product 1's stock count while this `transaction` was still open, it would simply pause, then proceed only once this one finished, at which point it would correctly see 45, not the stale 50, avoiding the `lost update` entirely.

## Why FOR UPDATE Solves the Lost Update Problem

- `Locking` directly closes the gap that caused the `lost update` in the previous lesson.
- Without a `lock`, both `transactions` could read 50 at nearly the same instant, before either had written anything back.
- With `FOR UPDATE`, whichever `transaction` reaches the `row` first `locks` it, and the second `transaction`'s own `SELECT ...
- FOR UPDATE` blocks until the first is completely finished, guaranteeing the second `transaction`'s read reflects the first `transaction`'s already-committed result, not a stale value both `transactions` raced to read at the same moment.

## Shared Locks vs. Exclusive Locks

Not every `lock` blocks every other operation equally. A shared `lock`, taken automatically by an ordinary read in most `databases`, allows other `transactions` to also read the same `row` concurrently, since reading alongside reading causes no conflict.

An exclusive `lock`, the kind `FOR UPDATE` takes, blocks any other `transaction` from reading with intent to modify or from writing to that `row` at all, since two `transactions` both planning to change the same `row` is exactly the conflict that needs preventing.

```postgresql with=init.sql
BEGIN;
SELECT stock_count FROM inventory WHERE product_id = 1;
-- An ordinary SELECT like this takes no exclusive lock; other transactions
-- can freely read this same row concurrently without being blocked.
COMMIT;
```

Expected output:



| stock_count |
| --- |
| 50 |

An ordinary `SELECT`, without `FOR UPDATE`, does not block other readers or even other writers under PostgreSQL's default `isolation level`, which is why `FOR UPDATE` has to be requested explicitly the moment a `transaction` plans to act on what it just read.

## Locking Only Locks What It Needs To

`Locking` in a well-behaved system is scoped as narrowly as possible, typically to individual `rows`, rather than to an entire `table`, so that unrelated `transactions` touching different `rows` never have to wait on each other.

```postgresql with=init.sql
INSERT INTO inventory (product_id, product_name, stock_count) VALUES (2, 'USB Cable', 200);

BEGIN;
SELECT stock_count FROM inventory WHERE product_id = 1 FOR UPDATE;
-- This locks only the row for product_id = 1.
-- A separate transaction working with product_id = 2 is never blocked by this lock.
COMMIT;
```

Expected output:



| stock_count |
| --- |
| 50 |

This `row`-level scope is what makes `locking` practical at real-world scale: a busy inventory system can have thousands of concurrent `transactions`, each safely `locking` only the specific `rows` it touches, without the whole `table` grinding to a halt waiting on unrelated updates.

![Row-level locking blocking product 1 while unrelated product rows continue](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_row_level_lock_scope.png)

## Locking at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>SELECT ... FOR UPDATE</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reads a row and claims an exclusive <code>lock</code> on it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared <code>lock</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Taken by ordinary reads; allows concurrent reading</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exclusive <code>lock</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Taken by <code>FOR UPDATE</code> or a write; blocks other <code>locks</code> on that row</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>Lock</code> released</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automatically, when the transaction commits or rolls back</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Typically per row, so unrelated transactions are not blocked</td>
    </tr>
  </tbody>
</table>

## Your Turn

Write a `transaction` that `locks` product 1's `row` with `FOR UPDATE`, deducts 8 units, and commits, then confirm the final stock count with a `SELECT`.

```postgresql with=init.sql
-- Write your transaction below
```

Expected result and verification:

If your `transaction` runs:

```sql
BEGIN;
SELECT stock_count FROM inventory WHERE product_id = 1 FOR UPDATE;
UPDATE inventory SET stock_count = stock_count - 8 WHERE product_id = 1;
COMMIT;
```

the closing `SELECT` shows 37, eight less than the 45 already left over from the earlier `FOR UPDATE` example in this lesson, and any concurrent transaction attempting the same `lock` on product 1 would have had to wait until this one finished.

## Conclusion

`Locking` gives a `transaction` exclusive claim over a `row` it intends to change, forcing other `transactions` that want to touch the same `row` to wait until the `lock` is released, which is what actually prevents `lost updates` and similar conflicts rather than just naming them. Rahul's inventory system can now safely handle two sales of the same product arriving at nearly the same instant. `Locking` is not applied uniformly everywhere; how much of it happens automatically depends on a per-`transaction` setting, isolation levels, which the next lesson examines directly.
