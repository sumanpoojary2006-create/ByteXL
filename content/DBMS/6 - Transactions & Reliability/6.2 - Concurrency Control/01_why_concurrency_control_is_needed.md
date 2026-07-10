## Introduction

An airline booking system sells the same flight to thousands of people browsing at once, and a single seat, seat 14C, might be looked at by two different passengers within the same second. If both of their booking transactions read "seat 14C: available" before either one commits, both could proceed to book it, and the airline ends up having sold one seat twice. Isolation, covered in the previous chapter, promised that transactions do not see each other's uncommitted changes, but that alone does not automatically prevent two transactions from both reading the same available seat and both deciding to book it. This is the problem **concurrency control** exists to solve: coordinating multiple transactions that touch the same data at the same time, so the end result is exactly as correct as if they had run one after another.

## Simulating the Double-Booking Problem

The `seats` table tracks one row per seat, with a simple availability flag.

```postgresql file=seats.sql
CREATE TABLE seats (
    seat_id TEXT PRIMARY KEY,
    flight_number TEXT,
    is_available BOOLEAN
);

INSERT INTO seats (seat_id, flight_number, is_available) VALUES
('14C', 'AI202', TRUE),
('14D', 'AI202', TRUE);
```

```postgresql with=seats.sql
-- Passenger A's booking transaction:
SELECT is_available FROM seats WHERE seat_id = '14C';
-- Reads TRUE, seat looks available, decides to proceed.

-- Passenger B's booking transaction, arriving at nearly the same moment:
-- SELECT is_available FROM seats WHERE seat_id = '14C';
-- Also reads TRUE, since Passenger A has not committed anything yet.
-- Passenger B also decides to proceed, based on the same "available" reading.

-- Both transactions now attempt to mark the seat unavailable and book it.
BEGIN;
UPDATE seats SET is_available = FALSE WHERE seat_id = '14C';
COMMIT;

SELECT * FROM seats WHERE seat_id = '14C';
```

The `SELECT` step, on its own, is not a mistake, and isolation was never violated, since neither passenger read the other's uncommitted work. The problem is the gap in time between reading "available" and acting on that reading with an `UPDATE`. Here is how that plays out:

1. Both passengers' applications run this same read-then-write sequence close enough together.
2. Both conclude the seat was free before either one's booking became final.
3. Both `UPDATE` statements eventually run, one overwriting the effect of the other.

The result: only one seat's worth of data, but two confirmation emails already sent.

## Why This Is a Different Problem from What ACID Alone Solves

Atomicity, consistency, isolation, and durability, covered in the previous chapter, are all guarantees about a single transaction's own correctness and about hiding uncommitted work from others. None of them, by themselves, stop two separate, individually well-behaved transactions from both reading the same true statement and both acting on it in a way that conflicts. Concurrency control is specifically about coordinating the interaction between transactions, not just protecting each one internally. It answers a different question: given that many transactions want to touch the same data at nearly the same moment, how does the database ensure the combined outcome is still correct.

## The Standard a Database Aims For

The benchmark concurrency control is measured against is called serializability, a term this chapter builds toward in full: the guarantee that whatever order transactions actually execute in, concurrently, interleaved, overlapping, the final result must match some possible outcome of running those same transactions strictly one at a time, in some order. If Passenger A and Passenger B's bookings had genuinely run one after the other, whichever went second would have seen the seat already taken and been stopped before booking it. A database with proper concurrency control produces that same correct outcome even when the two bookings actually overlap in real time.

## Why This Matters More as Systems Grow

A database with a single user never encounters this class of problem at all, since there is nothing to run concurrently against. The moment a system serves more than one person at once, which describes nearly every real application, from a banking app to a ticket-booking site to a shared spreadsheet backend, concurrency control stops being an academic concern and becomes the difference between a system that works under load and one that quietly loses or duplicates data the busier it gets.

## Why Concurrency Control Is Needed, at a Glance

| Without coordination | With concurrency control |
|---|---|
| Two transactions can both read the same "available" state | The database ensures only one can act on it |
| A busier system means more silent conflicts | Correctness holds regardless of how many transactions overlap |
| The result depends on unlucky timing | The result matches some valid one-at-a-time ordering |

## Your Turn

Reason through the seats scenario above for a different flight number, imagining two passengers both trying to book seat `14D` at the same time. Write the same read-then-update sequence for one of the two passengers against the `seats` table above, and note in a comment what would need to be true for the second passenger's booking to be safely rejected.

```postgresql with=seats.sql
-- Write your queries below, plus a comment describing what protects the second booking
```

A safe outcome requires the second passenger's transaction to either wait until the first one has committed and then see `is_available = FALSE`, or be blocked from proceeding at all until the first transaction finishes, which is exactly the kind of coordination the next few lessons in this chapter cover.

## Conclusion

Concurrency control coordinates multiple transactions touching the same data at nearly the same time, aiming for a result that matches what would have happened if those transactions had run one after another, even though in reality they overlap. Without it, a database can end up double-booking a seat, overselling stock, or losing an update, even while every individual transaction obeys every ACID guarantee perfectly on its own. The next lesson catalogs the specific ways this kind of interference shows up, giving each one a precise name.
