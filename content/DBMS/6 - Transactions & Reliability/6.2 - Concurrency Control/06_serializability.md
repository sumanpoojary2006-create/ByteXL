## Introduction

Every mechanism covered in this chapter, `locking`, `isolation levels`, and deadlock detection, exists to serve one underlying standard, first mentioned in this chapter's opening lesson: whatever order `transactions` actually run in, overlapping, interleaved, racing against each other, the final result must match some outcome that could have happened if those same `transactions` had instead run one at a time, in some sequence, with no overlap at all.

This standard has a name, **serializability**, and understanding it precisely is what ties together why `locking`, `isolation levels`, and deadlock resolution all exist in the first place.

**Definition:** Serializability is the standard every mechanism in this chapter ultimately serves: a guarantee that concurrent `transactions`, however they actually interleave in real time, produce a result equivalent to running them one at a time in some order, and `locking`, `isolation levels`, and deadlock detection are all the practical machinery a `database` uses to approach or fully guarantee that standard.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_serializability.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Every mechanism covered in this chapter, locking, isolation levels, and deadlock detection, exists to serve one underlying standard, first mentioned in this chapter's opening lesson: whatever order transactions actually run in, overlapping, interleaved.

ON-IMAGE TEXT: show a short bold title "Serializability" plus only these few labels, large and legible: Order, Result, Serializability. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for serializability](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_intro_serializability.png)

## What "Equivalent to Some Serial Order" Means

The `accounts` `table` sets up two `transactions` whose combined effect depends entirely on execution order.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `accounts`

| account_id | balance |
| --- | --- |
| 1 | 1000.00 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    balance NUMERIC(10, 2)
);

INSERT INTO accounts (account_id, balance) VALUES (1, 1000.00);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
-- Transaction A: apply a 10% bonus
BEGIN;
UPDATE accounts SET balance = balance * 1.10 WHERE account_id = 1;
COMMIT;

-- Transaction B: apply a flat 50.00 deduction
BEGIN;
UPDATE accounts SET balance = balance - 50.00 WHERE account_id = 1;
COMMIT;

SELECT balance FROM accounts WHERE account_id = 1;
```

Expected output:



| balance |
| --- |
| 1050.00 |

Running Transaction A completely, then Transaction B completely, as this script does, produces 1050.00:

1. The 10% bonus applied first brings the balance to 1100.00.

2. The flat deduction then brings it to 1050.00.

Running them in the opposite order, B first then A, would instead produce `(1000.00 - 50.00) * 1.10`, which is 1045.00, a genuinely different final number. Both orderings are individually valid and internally correct; they simply produce different, equally legitimate results, since multiplication and subtraction do not commute.

Serializability does not demand a single specific answer; it demands that whatever result a concurrent execution produces must match one of these valid serial orderings, not some third, impossible value that neither ordering could have produced.

## Why This Standard Matters for Correctness

If two `transactions` run concurrently and the `database` allows a result that does not correspond to any possible one-at-a-time ordering, something has gone wrong that no individual `transaction`'s own logic could have predicted or accounted for.

The `lost update` from earlier in this chapter is a clear example: neither "A then B" nor "B then A" would have caused one sale's stock reduction to vanish entirely, since a strictly sequential execution guarantees each `transaction` sees the previous one's completed result before making its own change.

A `lost update` is not just an inconvenient bug; it is a violation of serializability, a result that no valid serial ordering could ever have produced.

![Serializability requiring an interleaved execution to match some serial order](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_serializability_equivalent_serial_order.png)

## Serializability as the Target, Not a Setting

- `SERIALIZABLE`, the `isolation level` covered earlier in this chapter, is the one level that fully guarantees serializability for every `transaction` run under it.
- The other levels, `READ COMMITTED` and `REPEATABLE READ`, are deliberate, named exceptions to full serializability, each one permitting specific, well-understood anomalies, such as non-repeatable reads, in exchange for better performance.
- This is the precise relationship between the two ideas covered across this chapter: serializability is the theoretical gold standard for what "correct under concurrency" means, and `isolation levels` are the practical, named trade-offs a `database` offers between that gold standard and real-world speed.

## Verifying the Trade-off Directly

```postgresql with=init.sql
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT balance FROM accounts WHERE account_id = 1;
COMMIT;
```

Expected observation: the isolation-level command completes inside the transaction. Its effect becomes visible when the same read is tested from two concurrent sessions, as explained below.

Running a `transaction` under `SERIALIZABLE` guarantees, for every `transaction` that also runs under `SERIALIZABLE` concurrently with it, that the combined result will always be equivalent to some serial ordering of them, at the cost of the `database` sometimes forcibly aborting one of the `transactions` and requiring a retry, exactly the trade-off discussed when `isolation levels` were first introduced.

![Serializable isolation preserving correctness by forcing a retry when needed](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/13_serializable_retry_tradeoff.png)

## Serializability at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Serializability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The result of concurrent transactions must match some valid one-at-a-time ordering</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Guaranteed by</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The <code>SERIALIZABLE</code> isolation level</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Violated by</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lost updates and similar anomalies that no serial ordering could produce</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not guaranteed by</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weaker isolation levels, which permit specific, named anomalies deliberately</td>
    </tr>
  </tbody>
</table>

## Your Turn

Using the `accounts` `table` above, reset the balance to 1000.00, then run Transaction A's 10% bonus and Transaction B's flat 50.00 deduction in the reverse order from the first example, confirming the result matches the "B then A" calculation described earlier.

```postgresql with=init.sql
-- Write your queries below
```

Expected result and verification:

First, reset the balance with `UPDATE accounts SET balance = 1000.00 WHERE account_id = 1;`. Next, run the flat deduction first: `UPDATE accounts SET balance = balance - 50.00 ...`.

Then run the 10% bonus: `UPDATE accounts SET balance = balance * 1.10 ...`. The final balance is 1045.00, confirming a different but equally valid serial ordering from the 1050.00 result produced when the bonus ran first.

## Conclusion

Serializability is the standard every mechanism in this chapter ultimately serves: a guarantee that concurrent `transactions`, however they actually interleave in real time, produce a result equivalent to running them one at a time in some order, and `locking`, `isolation levels`, and deadlock detection are all the practical machinery a `database` uses to approach or fully guarantee that standard.

With concurrency control covered from the problem it solves through to the standard it targets, the final chapter in this unit turns to what happens when a `transaction` survives not just concurrent access, but an outright system failure.
