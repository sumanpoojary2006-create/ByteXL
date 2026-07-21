## Introduction

- `Locking` prevents conflicts, but `locking` everything as strictly as possible all the time would make a busy database painfully slow, since every transaction would end up waiting on every other transaction touching nearby data.
- Different applications also have different tolerances: a dashboard showing an approximate view count can live with a non-repeatable read that a banking transfer never could.
- SQL exposes this trade-off directly through **isolation levels**, a per-transaction setting that controls exactly which of the concurrency problems from earlier in this chapter, `dirty reads`, non-repeatable reads, and phantom reads, the database is allowed to permit in exchange for less `locking` and better performance.

**Definition:** `Isolation levels` let a transaction choose exactly how much protection against concurrency problems it needs, trading stricter guarantees for more waiting and potential retries, with `READ COMMITTED` as a sensible everyday default and `SERIALIZABLE` reserved for operations where any interference at all is unacceptable.

![Intro visual for isolation levels](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_intro_isolation_levels_actual3d_bf751c94.png)

## The Four Standard Isolation Levels

The SQL standard defines four `isolation levels`, ordered from loosest to strictest, and each one is a promise about which of the earlier lesson's problems cannot occur.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `inventory`

| product_id | stock_count |
| --- | --- |
| 1 | 50 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE inventory (
    product_id INTEGER PRIMARY KEY,
    stock_count INTEGER
);

INSERT INTO inventory (product_id, stock_count) VALUES (1, 50);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf8n5" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns one row containing the current server or transaction setting. The exact value depends on the OneCompiler PostgreSQL environment, so compare the setting name and meaning rather than memorizing a particular value.

This confirms the default level for a new PostgreSQL session, `read committed`, sitting in the middle of the strictness spectrum, neither the loosest nor the strictest option available.

## Setting the Isolation Level for a Transaction

The `isolation level` can be set explicitly at the start of a transaction, overriding the session default for just that one transaction.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf8x3" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns one row containing the current server or transaction setting. The exact value depends on the OneCompiler PostgreSQL environment, so compare the setting name and meaning rather than memorizing a particular value.

- `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE` requests the strictest level available, for the duration of this one transaction only; the session's default reverts back afterward for the next transaction.
- PostgreSQL does not implement `READ UNCOMMITTED` as a genuinely looser level, it is treated the same as `READ COMMITTED`, so PostgreSQL in practice offers three distinct behaviors even though four names exist in the standard.

## What Each Level Actually Prevents

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Isolation level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Dirty reads</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Non-repeatable reads</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Phantom reads</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read Uncommitted</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read Committed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeatable Read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible (prevented in PostgreSQL specifically)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Serializable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
    </tr>
  </tbody>
</table>

Each level adds one more guarantee on top of the last:

- `READ COMMITTED`, PostgreSQL's default, already guarantees a transaction never sees another transaction's uncommitted work, which is why the `dirty read` demonstration in the previous lesson's `ROLLBACK` example behaved correctly without any special setting.
- `REPEATABLE READ` additionally guarantees that if a transaction reads the same row twice, it gets the same answer both times, even if another transaction commits a change to that row in between.
- `SERIALIZABLE`, the strictest level, guarantees the transaction behaves as if it had run completely alone, with no interleaving effects from any concurrent transaction visible at all.

![Isolation levels as a protection ladder from read committed to serializable](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_isolation_levels_protection_ladder.png)

## Seeing REPEATABLE READ Prevent a Non-Repeatable Read

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf98p" 
 width="100%"
></iframe>

Expected observation: the isolation-level command completes inside the transaction. Its effect becomes visible when the same read is tested from two concurrent sessions, as explained below.

Both reads inside this transaction are guaranteed to agree, because `REPEATABLE READ` takes a consistent snapshot of the data as of when the transaction began, and every read within that transaction is served from that same snapshot rather than the constantly updating live data.

![Repeatable read keeping the same row value stable across two reads](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_repeatable_read_same_row_stays_same.png)

## Why Not Always Use SERIALIZABLE

- If `SERIALIZABLE` prevents every concurrency problem, it might seem like the obvious default for everything.
- The cost is real: `SERIALIZABLE` transactions can be forced to abort and retry when the database detects that their interleaving with another concurrent transaction could not be made to match any valid one-at-a-time ordering, and stricter levels generally mean more waiting and more retries under heavy concurrent load.
- The right choice depends on the operation: a banking transfer or a seat booking justifies the strictest level available, while a page-view counter or an analytics dashboard is often perfectly fine under the default `READ COMMITTED`, trading a small, acceptable chance of a stale read for much better throughput.

## Isolation Levels at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strictness</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read Committed (PostgreSQL default)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moderate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Most everyday application queries</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeatable Read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stricter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reports that must stay internally consistent while running</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Serializable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strictest</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Financial transfers, booking systems, anything where a subtle conflict is unacceptable</td>
    </tr>
  </tbody>
</table>

## Your Turn

Start a transaction under `REPEATABLE READ`, confirm the level with `SHOW transaction_isolation`, read `stock_count` for product 1 twice with an ordinary `SELECT` in between, and commit.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaf9k5" 
 width="100%"
></iframe>

Expected result and verification:

If you run `BEGIN; SET TRANSACTION ISOLATION LEVEL REPEATABLE READ; SHOW transaction_isolation; SELECT stock_count FROM inventory WHERE product_id = 1; SELECT stock_count FROM inventory WHERE product_id = 1; COMMIT;`, the `isolation level` reports as `repeatable read`, and both reads return 50, consistently.

## Conclusion

`Isolation levels` let a transaction choose exactly how much protection against concurrency problems it needs, trading stricter guarantees for more waiting and potential retries, with `READ COMMITTED` as a sensible everyday default and `SERIALIZABLE` reserved for operations where any interference at all is unacceptable. Rahul can now choose the right level for a banking transfer versus a simple analytics query, rather than treating every transaction identically. `Locking` and strict isolation both come with a hazard worth understanding on its own: two transactions can end up waiting on each other in a way that never resolves.
