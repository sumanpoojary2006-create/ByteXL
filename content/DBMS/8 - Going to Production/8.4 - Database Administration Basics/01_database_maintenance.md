## Introduction

Every `UPDATE` and `DELETE` covered across this entire course has been described as if the old row's space simply disappears the moment the statement finishes. In PostgreSQL specifically, that is not quite what happens: an updated or deleted row's old version is marked as no longer current, but its physical space is not immediately reclaimed, since other concurrent transactions, under the isolation guarantees covered in an earlier unit, might still need to see that older version. Left unmanaged, this leftover space accumulates, and **database maintenance** is the ongoing work of cleaning it up, keeping a production database healthy as it runs for months and years, not just correct at the moment each query executes.

## Why Updates and Deletes Leave Behind Dead Rows

PostgreSQL's approach to updates, called MVCC, multiversion concurrency control, is what makes isolation between concurrent transactions possible in the first place, and it has a direct physical consequence.

```postgresql file=maintenance_demo.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status)
SELECT i, 'in_transit' FROM generate_series(1, 5000) AS i;
```

```postgresql with=maintenance_demo.sql
SELECT pg_size_pretty(pg_relation_size('shipments')) AS size_before_updates;

UPDATE shipments SET status = 'delivered' WHERE shipment_id <= 4000;

SELECT pg_size_pretty(pg_relation_size('shipments')) AS size_after_updates;
```

Even though this `UPDATE` did not add a single new row, the table's physical size grows. Here is why:

- PostgreSQL writes each updated row as a new version alongside the old one, rather than overwriting it in place.
- The old, no-longer-current versions, called dead tuples, keep occupying disk space until something explicitly reclaims it.

## Reclaiming Space with VACUUM

`VACUUM` is the command that scans a table for dead tuples and marks their space as reusable for future inserts and updates.

```postgresql with=maintenance_demo.sql
VACUUM shipments;

SELECT pg_size_pretty(pg_relation_size('shipments')) AS size_after_vacuum;
```

A plain `VACUUM` marks dead space as reusable for this table's own future writes, without necessarily shrinking the file on disk immediately, since PostgreSQL generally prefers to reuse that reclaimed space internally rather than pay the cost of physically returning it to the operating system. `VACUUM FULL` goes further, actually rewriting the table to reclaim disk space visibly, at the cost of `lock`ing the table exclusively while it runs, which is why `VACUUM FULL` is typically reserved for planned maintenance windows rather than run routinely against a live, busy table.

## Keeping Statistics Current with ANALYZE

The query optimizer, covered in the performance unit, relies on table and column statistics to estimate costs and choose plans, and those statistics do not update themselves automatically after a large batch of changes.

```postgresql with=maintenance_demo.sql
ANALYZE shipments;

SELECT relname, n_live_tup, n_dead_tup FROM pg_stat_user_tables WHERE relname = 'shipments';
```

`ANALYZE` refreshes PostgreSQL's internal statistics about the table's data distribution, and `n_live_tup` and `n_dead_tup` in `pg_stat_user_tables` show, respectively, the estimated count of current, valid rows and dead, reclaimable rows PostgreSQL is currently tracking. Stale statistics, left unrefreshed after significant data changes, can mislead the optimizer into choosing a worse plan than it otherwise would, exactly the risk noted when the optimizer was first introduced.

## Autovacuum: Maintenance Running Automatically

Running `VACUUM` and `ANALYZE` manually after every change would be impractical, which is why PostgreSQL runs a background process, autovacuum, that performs both automatically once a table's dead-tuple count or data changes cross a configured threshold.

```postgresql with=maintenance_demo.sql
SHOW autovacuum;
```

`autovacuum` reports whether this automatic background process is enabled, `on` by default in a standard PostgreSQL installation. Autovacuum handles routine maintenance for the vast majority of tables without any manual intervention at all; manual `VACUUM` or `ANALYZE` becomes relevant mainly for large, one-off batch operations where waiting for autovacuum's next scheduled pass is not acceptable, or for the exclusive-`lock` `VACUUM FULL` case, which autovacuum never performs on its own due to its `lock`ing cost.

## Database Maintenance at a Glance

| Concept | Detail |
|---|---|
| Dead tuples | Old row versions left behind by `UPDATE`/`DELETE`, due to PostgreSQL's MVCC design |
| `VACUUM` | Marks dead tuple space as reusable; does not always shrink the file on disk |
| `VACUUM FULL` | Physically reclaims disk space, but `lock`s the table exclusively while running |
| `ANALYZE` | Refreshes statistics the query optimizer relies on |
| Autovacuum | A background process running `VACUUM` and `ANALYZE` automatically, on by default |

## Your Turn

Delete a large portion of the `shipments` table, check `n_dead_tup` before running `VACUUM`, then run it and check again, confirming the dead tuple count drops.

```postgresql with=maintenance_demo.sql
-- Write your queries below
```

Running `DELETE FROM shipments WHERE shipment_id > 3000;` followed by `SELECT n_dead_tup FROM pg_stat_user_tables WHERE relname = 'shipments';` shows a large dead-tuple count; after `VACUUM shipments;`, the same query shows that count drop close to zero, confirming the space has been marked reusable.

## Conclusion

Because PostgreSQL keeps old row versions around to support concurrent, isolated reads, routine maintenance, reclaiming dead tuple space with `VACUUM` and keeping the optimizer's statistics current with `ANALYZE`, is essential to keeping a database healthy over time, and autovacuum handles this automatically for the large majority of real-world cases without manual intervention. With the mechanics of keeping a database clean covered, the next lesson turns to protecting its data against loss entirely, through backups.
