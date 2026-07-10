## Introduction

The `lost update` from the previous lesson happened because two transactions both read the same stock count and both wrote a new value based on that same stale reading, with neither transaction aware the other was doing the same thing at the same time. The fix is not clever application logic checking timestamps after the fact; it is stopping the second transaction from reading and acting on that value until the first transaction has finished with it entirely. This is what **locking** does: a transaction can claim a `lock` on a row, blocking other transactions from making conflicting changes to that same row until the `lock` is released.

## Locking a Row for Update

The `inventory` table from the previous lesson is the setup again.

```postgresql file=inventory_locking.sql
CREATE TABLE inventory (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    stock_count INTEGER
);

INSERT INTO inventory (product_id, product_name, stock_count) VALUES
(1, 'Wireless Mouse', 50);
```

```postgresql with=inventory_locking.sql
BEGIN;

SELECT stock_count FROM inventory WHERE product_id = 1 FOR UPDATE;

UPDATE inventory SET stock_count = stock_count - 5 WHERE product_id = 1;

COMMIT;

SELECT stock_count FROM inventory WHERE product_id = 1;
```

`FOR UPDATE`, added to the end of a `SELECT`, tells the database that this transaction intends to modify the row it just read, and claims a `lock` on that row immediately. Any other transaction that also tries one of these is forced to wait until this transaction either commits or rolls back and releases the `lock`:

- `SELECT ... FOR UPDATE` on the same row
- An `UPDATE` directly against it If a second sale transaction had tried to `lock` and read product 1's stock count while this transaction was still open, it would simply pause, then proceed only once this one finished, at which point it would correctly see 45, not the stale 50, avoiding the `lost update` entirely.

## Why FOR UPDATE Solves the Lost Update Problem

`Locking` directly closes the gap that caused the `lost update` in the previous lesson. Without a `lock`, both transactions could read 50 at nearly the same instant, before either had written anything back. With `FOR UPDATE`, whichever transaction reaches the row first `locks` it, and the second transaction's own `SELECT ... FOR UPDATE` blocks until the first is completely finished, guaranteeing the second transaction's read reflects the first transaction's already-committed result, not a stale value both transactions raced to read at the same moment.

## Shared Locks vs. Exclusive Locks

Not every `lock` blocks every other operation equally. A shared `lock`, taken automatically by an ordinary read in most databases, allows other transactions to also read the same row concurrently, since reading alongside reading causes no conflict. An exclusive `lock`, the kind `FOR UPDATE` takes, blocks any other transaction from reading with intent to modify or from writing to that row at all, since two transactions both planning to change the same row is exactly the conflict that needs preventing.

```postgresql with=inventory_locking.sql
BEGIN;
SELECT stock_count FROM inventory WHERE product_id = 1;
-- An ordinary SELECT like this takes no exclusive lock; other transactions
-- can freely read this same row concurrently without being blocked.
COMMIT;
```

An ordinary `SELECT`, without `FOR UPDATE`, does not block other readers or even other writers under PostgreSQL's default `isolation level`, which is why `FOR UPDATE` has to be requested explicitly the moment a transaction plans to act on what it just read.

## Locking Only Locks What It Needs To

`Locking` in a well-behaved system is scoped as narrowly as possible, typically to individual rows, rather than to an entire table, so that unrelated transactions touching different rows never have to wait on each other.

```postgresql with=inventory_locking.sql
INSERT INTO inventory (product_id, product_name, stock_count) VALUES (2, 'USB Cable', 200);

BEGIN;
SELECT stock_count FROM inventory WHERE product_id = 1 FOR UPDATE;
-- This locks only the row for product_id = 1.
-- A separate transaction working with product_id = 2 is never blocked by this lock.
COMMIT;
```

This row-level scope is what makes `locking` practical at real-world scale: a busy inventory system can have thousands of concurrent transactions, each safely `locking` only the specific rows it touches, without the whole table grinding to a halt waiting on unrelated updates.

## Locking at a Glance

| Concept | Detail |
|---|---|
| `SELECT ... FOR UPDATE` | Reads a row and claims an exclusive `lock` on it |
| Shared `lock` | Taken by ordinary reads; allows concurrent reading |
| Exclusive `lock` | Taken by `FOR UPDATE` or a write; blocks other `locks` on that row |
| `Lock` released | Automatically, when the transaction commits or rolls back |
| Scope | Typically per row, so unrelated transactions are not blocked |

## Your Turn

Write a transaction that `locks` product 1's row with `FOR UPDATE`, deducts 8 units, and commits, then confirm the final stock count with a `SELECT`.

```postgresql with=inventory_locking.sql
-- Write your transaction below
```

If your transaction runs `BEGIN; SELECT stock_count FROM inventory WHERE product_id = 1 FOR UPDATE; UPDATE inventory SET stock_count = stock_count - 8 WHERE product_id = 1; COMMIT;`, the closing `SELECT` shows 37, eight less than the 45 already left over from the earlier `FOR UPDATE` example in this lesson, and any concurrent transaction attempting the same `lock` on product 1 would have had to wait until this one finished.

## Conclusion

`Locking` gives a transaction exclusive claim over a row it intends to change, forcing other transactions that want to touch the same row to wait until the `lock` is released, which is what actually prevents `lost updates` and similar conflicts rather than just naming them. Rahul's inventory system can now safely handle two sales of the same product arriving at nearly the same instant. `Locking` is not applied uniformly everywhere; how much of it happens automatically depends on a per-transaction setting, isolation levels, which the next lesson examines directly.
