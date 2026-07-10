## Introduction

Every mechanism covered in this chapter, `locking`, `isolation levels`, and deadlock detection, exists to serve one underlying standard, first mentioned in this chapter's opening lesson: whatever order transactions actually run in, overlapping, interleaved, racing against each other, the final result must match some outcome that could have happened if those same transactions had instead run one at a time, in some sequence, with no overlap at all. This standard has a name, **serializability**, and understanding it precisely is what ties together why `locking`, `isolation levels`, and deadlock resolution all exist in the first place.

## What "Equivalent to Some Serial Order" Means

The `accounts` table sets up two transactions whose combined effect depends entirely on execution order.

```postgresql file=accounts_serializability.sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    balance NUMERIC(10, 2)
);

INSERT INTO accounts (account_id, balance) VALUES (1, 1000.00);
```

```postgresql with=accounts_serializability.sql
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

Running Transaction A completely, then Transaction B completely, as this script does, produces 1050.00:

1. The 10% bonus applied first brings the balance to 1100.00.
2. The flat deduction then brings it to 1050.00.

Running them in the opposite order, B first then A, would instead produce `(1000.00 - 50.00) * 1.10`, which is 1045.00, a genuinely different final number. Both orderings are individually valid and internally correct; they simply produce different, equally legitimate results, since multiplication and subtraction do not commute. Serializability does not demand a single specific answer; it demands that whatever result a concurrent execution produces must match one of these valid serial orderings, not some third, impossible value that neither ordering could have produced.

## Why This Standard Matters for Correctness

If two transactions run concurrently and the database allows a result that does not correspond to any possible one-at-a-time ordering, something has gone wrong that no individual transaction's own logic could have predicted or accounted for. The `lost update` from earlier in this chapter is a clear example: neither "A then B" nor "B then A" would have caused one sale's stock reduction to vanish entirely, since a strictly sequential execution guarantees each transaction sees the previous one's completed result before making its own change. A `lost update` is not just an inconvenient bug; it is a violation of serializability, a result that no valid serial ordering could ever have produced.

## Serializability as the Target, Not a Setting

`SERIALIZABLE`, the `isolation level` covered earlier in this chapter, is the one level that fully guarantees serializability for every transaction run under it. The other levels, `READ COMMITTED` and `REPEATABLE READ`, are deliberate, named exceptions to full serializability, each one permitting specific, well-understood anomalies, such as non-repeatable reads, in exchange for better performance. This is the precise relationship between the two ideas covered across this chapter: serializability is the theoretical gold standard for what "correct under concurrency" means, and `isolation levels` are the practical, named trade-offs a database offers between that gold standard and real-world speed.

## Verifying the Trade-off Directly

```postgresql with=accounts_serializability.sql
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT balance FROM accounts WHERE account_id = 1;
COMMIT;
```

Running a transaction under `SERIALIZABLE` guarantees, for every transaction that also runs under `SERIALIZABLE` concurrently with it, that the combined result will always be equivalent to some serial ordering of them, at the cost of the database sometimes forcibly aborting one of the transactions and requiring a retry, exactly the trade-off discussed when `isolation levels` were first introduced.

## Serializability at a Glance

| Concept | Detail |
|---|---|
| Serializability | The result of concurrent transactions must match some valid one-at-a-time ordering |
| Guaranteed by | The `SERIALIZABLE` isolation level |
| Violated by | Lost updates and similar anomalies that no serial ordering could produce |
| Not guaranteed by | Weaker isolation levels, which permit specific, named anomalies deliberately |

## Your Turn

Using the `accounts` table above, reset the balance to 1000.00, then run Transaction A's 10% bonus and Transaction B's flat 50.00 deduction in the reverse order from the first example, confirming the result matches the "B then A" calculation described earlier.

```postgresql with=accounts_serializability.sql
-- Write your queries below
```

If you reset the balance with `UPDATE accounts SET balance = 1000.00 WHERE account_id = 1;`, then run the flat deduction first (`UPDATE accounts SET balance = balance - 50.00 ...`) followed by the 10% bonus (`UPDATE accounts SET balance = balance * 1.10 ...`), the final balance is 1045.00, confirming this is a different, but equally valid, serial ordering from the 1050.00 result seen when the bonus ran first.

## Conclusion

Serializability is the standard every mechanism in this chapter ultimately serves: a guarantee that concurrent transactions, however they actually interleave in real time, produce a result equivalent to running them one at a time in some order, and `locking`, `isolation levels`, and deadlock detection are all the practical machinery a database uses to approach or fully guarantee that standard. With concurrency control covered from the problem it solves through to the standard it targets, the final chapter in this unit turns to what happens when a transaction survives not just concurrent access, but an outright system failure.
