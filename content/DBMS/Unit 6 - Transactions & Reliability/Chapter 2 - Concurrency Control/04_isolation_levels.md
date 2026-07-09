## Introduction

`Locking` prevents conflicts, but `locking` everything as strictly as possible all the time would make a busy database painfully slow, since every transaction would end up waiting on every other transaction touching nearby data. Different applications also have different tolerances: a dashboard showing an approximate view count can live with a non-repeatable read that a banking transfer never could. SQL exposes this trade-off directly through **isolation levels**, a per-transaction setting that controls exactly which of the concurrency problems from earlier in this chapter, `dirty reads`, non-repeatable reads, and phantom reads, the database is allowed to permit in exchange for less `locking` and better performance.

## The Four Standard Isolation Levels

The SQL standard defines four `isolation levels`, ordered from loosest to strictest, and each one is a promise about which of the earlier lesson's problems cannot occur.

```postgresql file=isolation_demo.sql
CREATE TABLE inventory (
    product_id INTEGER PRIMARY KEY,
    stock_count INTEGER
);

INSERT INTO inventory (product_id, stock_count) VALUES (1, 50);
```

```postgresql with=isolation_demo.sql
SHOW transaction_isolation;
```

This confirms the default level for a new PostgreSQL session, `read committed`, sitting in the middle of the strictness spectrum, neither the loosest nor the strictest option available.

## Setting the Isolation Level for a Transaction

The `isolation level` can be set explicitly at the start of a transaction, overriding the session default for just that one transaction.

```postgresql with=isolation_demo.sql
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SHOW transaction_isolation;
SELECT stock_count FROM inventory WHERE product_id = 1;
COMMIT;
```

`SET TRANSACTION ISOLATION LEVEL SERIALIZABLE` requests the strictest level available, for the duration of this one transaction only; the session's default reverts back afterward for the next transaction. PostgreSQL does not implement `READ UNCOMMITTED` as a genuinely looser level, it is treated the same as `READ COMMITTED`, so PostgreSQL in practice offers three distinct behaviors even though four names exist in the standard.

## What Each Level Actually Prevents

| Isolation level | Dirty reads | Non-repeatable reads | Phantom reads |
|---|---|---|---|
| Read Uncommitted | Possible | Possible | Possible |
| Read Committed | Prevented | Possible | Possible |
| Repeatable Read | Prevented | Prevented | Possible (prevented in PostgreSQL specifically) |
| Serializable | Prevented | Prevented | Prevented |

Each level adds one more guarantee on top of the last:

- `READ COMMITTED`, PostgreSQL's default, already guarantees a transaction never sees another transaction's uncommitted work, which is why the `dirty read` demonstration in the previous lesson's `ROLLBACK` example behaved correctly without any special setting.
- `REPEATABLE READ` additionally guarantees that if a transaction reads the same row twice, it gets the same answer both times, even if another transaction commits a change to that row in between.
- `SERIALIZABLE`, the strictest level, guarantees the transaction behaves as if it had run completely alone, with no interleaving effects from any concurrent transaction visible at all.

## Seeing REPEATABLE READ Prevent a Non-Repeatable Read

```postgresql with=isolation_demo.sql
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

SELECT stock_count FROM inventory WHERE product_id = 1;
-- Reads 50.

-- If another transaction committed a change to stock_count right now,
-- REPEATABLE READ guarantees this transaction still sees its own
-- consistent snapshot from when it started.

SELECT stock_count FROM inventory WHERE product_id = 1;
-- Reads 50 again, guaranteed identical to the first read within this transaction,
-- regardless of what any other transaction committed in between.

COMMIT;
```

Both reads inside this transaction are guaranteed to agree, because `REPEATABLE READ` takes a consistent snapshot of the data as of when the transaction began, and every read within that transaction is served from that same snapshot rather than the constantly updating live data.

## Why Not Always Use SERIALIZABLE

If `SERIALIZABLE` prevents every concurrency problem, it might seem like the obvious default for everything. The cost is real: `SERIALIZABLE` transactions can be forced to abort and retry when the database detects that their interleaving with another concurrent transaction could not be made to match any valid one-at-a-time ordering, and stricter levels generally mean more waiting and more retries under heavy concurrent load. The right choice depends on the operation: a banking transfer or a seat booking justifies the strictest level available, while a page-view counter or an analytics dashboard is often perfectly fine under the default `READ COMMITTED`, trading a small, acceptable chance of a stale read for much better throughput.

## Isolation Levels at a Glance

| Level | Strictness | Typical use |
|---|---|---|
| Read Committed (PostgreSQL default) | Moderate | Most everyday application queries |
| Repeatable Read | Stricter | Reports that must stay internally consistent while running |
| Serializable | Strictest | Financial transfers, booking systems, anything where a subtle conflict is unacceptable |

## Your Turn

Start a transaction under `REPEATABLE READ`, confirm the level with `SHOW transaction_isolation`, read `stock_count` for product 1 twice with an ordinary `SELECT` in between, and commit.

```postgresql with=isolation_demo.sql
-- Write your transaction below
```

If you run `BEGIN; SET TRANSACTION ISOLATION LEVEL REPEATABLE READ; SHOW transaction_isolation; SELECT stock_count FROM inventory WHERE product_id = 1; SELECT stock_count FROM inventory WHERE product_id = 1; COMMIT;`, the `isolation level` reports as `repeatable read`, and both reads return 50, consistently.

## Conclusion

`Isolation levels` let a transaction choose exactly how much protection against concurrency problems it needs, trading stricter guarantees for more waiting and potential retries, with `READ COMMITTED` as a sensible everyday default and `SERIALIZABLE` reserved for operations where any interference at all is unacceptable. Rahul can now choose the right level for a banking transfer versus a simple analytics query, rather than treating every transaction identically. `Locking` and strict isolation both come with a hazard worth understanding on its own: two transactions can end up waiting on each other in a way that never resolves.
