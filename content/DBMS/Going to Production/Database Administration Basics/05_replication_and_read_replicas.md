## Introduction

Every lesson in this course has run against a single database server. A production system serving real, sustained traffic eventually outgrows what one server can comfortably handle, and it also cannot afford for that one server to be a single point of total failure. **Replication** addresses both concerns: continuously copying a database's changes to one or more additional servers, called replicas, which can take over if the primary fails, and can also absorb read traffic that would otherwise all fall on a single machine.

## How Streaming Replication Works, Conceptually

PostgreSQL's standard replication approach relies on exactly the mechanism covered in the recovery unit: the `write-ahead log`. A replica continuously receives the same WAL records the primary server generates, and replays them, effectively performing the same redo process recovery uses after a crash, except continuously, in near real time, against a running, healthy primary.

```postgresql file=replication_demo.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit');
```

```postgresql with=replication_demo.sql
SELECT pg_current_wal_lsn() AS primary_wal_position;
```

Every change made on the primary, this `INSERT` included, generates WAL records exactly as covered in the recovery unit. In a replicated setup:

1. Those same records are streamed to every replica.
2. Each replica applies them in the same order, arriving at the identical data a moment later.

This is why replication is often described as recovery's mechanism, run continuously against a live server rather than only after a crash.

## Monitoring Replication from the Primary

A running PostgreSQL primary tracks every connected replica directly, exposing exactly how far behind each one currently is.

```postgresql with=replication_demo.sql
SELECT client_addr, state, sent_lsn, replay_lsn,
       sent_lsn - replay_lsn AS replication_lag_bytes
FROM pg_stat_replication;
```

`pg_stat_replication` would list one row per connected replica in a real replicated deployment; this example environment has none connected, so the query returns no rows, but the columns themselves describe exactly what matters: `sent_lsn` is how far the primary has sent WAL, `replay_lsn` is how far a given replica has actually applied it, and the difference between them is replication lag, the gap between "happened on the primary" and "visible on this replica."

## Why Replication Lag Matters

Because a replica applies changes slightly after the primary generates them, there is always some delay, however small, between a change committing on the primary and that same change becoming visible on a replica. A query reading from a replica can, in principle, see slightly stale data, a deliberate trade-off in exchange for spreading read load across more than one server.

```postgresql with=replication_demo.sql
-- A read-heavy reporting query, directed to a replica instead of the primary:
-- SELECT status, COUNT(*) FROM shipments GROUP BY status;
-- This runs identically whether issued against the primary or a replica,
-- but a replica's answer reflects data as of its own replay_lsn, which
-- may lag the primary's true current state by anywhere from milliseconds
-- to, under heavy load or network trouble, much longer.
SELECT status, COUNT(*) FROM shipments GROUP BY status;
```

This is why replicas are typically used for read traffic that can tolerate a small amount of staleness, dashboards, analytics, reporting, exactly the kind of workload this course has repeatedly used as its running examples, while writes, and any read that absolutely requires the most current possible data, continue to go to the primary.

## Read Replicas for Scaling, Failover for Availability

Replication serves two distinct purposes that are worth keeping separate. Using replicas to absorb read traffic, spreading load across several machines so no single server bears the full weight of every query, is a scaling strategy. Using a replica as a standby ready to be promoted to primary if the original primary fails is an availability strategy, protecting against the single point of failure a lone database server represents. A well-designed production deployment often uses replication for both purposes simultaneously, the same replicas serving read traffic day to day while also standing ready to take over if the primary ever goes down.

## Replication and Read Replicas at a Glance

| Concept | Detail |
|---|---|
| Mechanism | Streaming the same write-ahead log a crashed server would use for recovery |
| `pg_stat_replication` | Shows each connected replica's status and lag, from the primary's side |
| Replication lag | The gap between a change committing on the primary and appearing on a replica |
| Read replica use | Scaling read-heavy workloads that can tolerate slight staleness |
| Standby/failover use | Availability, promoting a replica to primary if the original fails |

## Your Turn

Write the query that would report replication lag in seconds rather than bytes, using `pg_stat_replication`'s `replay_lag` column, and add a comment explaining why a reporting dashboard might be deliberately directed to query a replica instead of the primary.

```postgresql with=replication_demo.sql
-- Write your query and comment below
```

`SELECT client_addr, replay_lag FROM pg_stat_replication;` reports lag as a time interval directly; a reporting dashboard is a strong candidate for querying a replica because its workload is read-only and can comfortably tolerate a few seconds of staleness, freeing the primary to dedicate its full capacity to the writes and time-sensitive reads that genuinely need up-to-the-moment accuracy.

## Conclusion

Replication streams a primary database's `write-ahead log` to one or more replicas, which replay it to stay continuously in sync, enabling both read scaling, directing tolerant read traffic away from the primary, and availability, standing ready to take over if the primary fails, at the cost of a small, measurable lag that every application using a replica has to account for. This closes out the operational picture this course has built lesson by lesson: from what data and a database even are, through tables, keys, and relationships, through SQL itself, through `join`s, aggregation, and advanced querying, through the transactional and concurrent guarantees that keep data trustworthy, through the performance techniques that keep queries fast, and finally through the programmability, security, and operational discipline a real, production database runs on every single day.
