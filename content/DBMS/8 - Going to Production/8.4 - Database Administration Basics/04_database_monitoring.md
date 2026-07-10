## Introduction

Every diagnostic tool used across this course, `EXPLAIN ANALYZE`, `pg_stat_activity`, `pg_relation_size`, has been reached for reactively, after a specific query was already suspected of being slow. **Database monitoring** flips that around: continuously watching key health metrics so that a genuine problem, a `connection pool` nearing its limit, a table bloating with dead tuples, a query that has quietly started running far slower than usual, is caught and addressed before it becomes an outage, rather than diagnosed only after users are already affected.

## Watching Connection Usage Over Time

The `connection pooling` lesson introduced checking current connections against `max_connections` as a one-time check; monitoring turns that same check into something tracked continuously.

```postgresql file=monitoring_demo.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status)
SELECT i, 'in_transit' FROM generate_series(1, 1000) AS i;
```

```postgresql with=monitoring_demo.sql
SELECT count(*) AS current_connections,
       (SELECT setting::int FROM pg_settings WHERE name = 'max_connections') AS max_connections,
       round(100.0 * count(*) / (SELECT setting::int FROM pg_settings WHERE name = 'max_connections'), 1) AS percent_used
FROM pg_stat_activity;
```

A monitoring system would run a query shaped like this on a regular interval, minutes or even seconds apart:

1. Tracking `percent_used` over time.
2. Alerting once it crosses a concerning threshold.

This catches a `connection leak`, covered in the pooling lesson, while there is still time to investigate, rather than discovering it only once new connections start being refused outright.

## Watching Table Bloat and Maintenance Health

The dead tuples covered in the maintenance lesson are exactly the kind of metric worth tracking continuously, since a table whose dead-tuple count keeps climbing despite autovacuum running is a sign something is preventing cleanup from keeping up.

```postgresql with=monitoring_demo.sql
SELECT relname, n_live_tup, n_dead_tup,
       round(100.0 * n_dead_tup / GREATEST(n_live_tup + n_dead_tup, 1), 1) AS dead_tuple_percent,
       last_autovacuum
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC
LIMIT 5;
```

Tracking `dead_tuple_percent` and `last_autovacuum` across a database's busiest tables over time reveals whether autovacuum is genuinely keeping pace with write activity, or whether a table is quietly accumulating bloat faster than it is being cleaned, a slow-building problem that gradually degrades query performance long before it becomes an obvious emergency.

## Watching Cache Hit Ratio

A database keeps frequently accessed data cached in memory, and how often a query finds what it needs already in that cache, rather than having to read from disk, is one of the clearest overall health signals a running database offers.

```postgresql with=monitoring_demo.sql
SELECT sum(heap_blks_hit) AS cache_hits,
       sum(heap_blks_read) AS disk_reads,
       round(100.0 * sum(heap_blks_hit) / GREATEST(sum(heap_blks_hit) + sum(heap_blks_read), 1), 2) AS cache_hit_ratio
FROM pg_statio_user_tables;
```

A healthy, well-provisioned database typically sustains a cache hit ratio well above 90%, meaning the vast majority of reads are served from fast memory rather than slower disk access. A ratio that drops noticeably, tracked over time rather than as a single snapshot, can signal that the database's available memory is no longer large enough for its actual working data set, a capacity signal worth acting on before it manifests as widespread query slowdowns.

## Watching for Long-Running and Blocked Queries

`pg_stat_activity`, used throughout this unit for one-off checks, is also the foundation for continuously monitoring queries that have been running unusually long, or are stuck waiting on a `lock` held by another session.

```postgresql with=monitoring_demo.sql
SELECT pid, state, wait_event_type, wait_event, now() - query_start AS running_for, query
FROM pg_stat_activity
WHERE state != 'idle' AND now() - query_start > INTERVAL '5 seconds'
ORDER BY running_for DESC;
```

`wait_event_type` and `wait_event` reveal specifically what a query is stuck waiting on, if anything, such as a `lock` held by another transaction, exactly the kind of contention the concurrency control unit covered. A monitoring system alerting on queries that exceed a reasonable running-time threshold, tuned to what "reasonable" actually means for a given application, catches runaway or blocked queries early, rather than letting them silently degrade the whole system's responsiveness.

## Database Monitoring at a Glance

| Metric | Query source | What it signals |
|---|---|---|
| Connection usage | `pg_stat_activity` vs. `max_connections` | Risk of exhausting the connection limit |
| Dead tuple percentage | `pg_stat_user_tables` | Whether maintenance is keeping pace with writes |
| Cache hit ratio | `pg_statio_user_tables` | Whether available memory matches the working data set |
| Long-running or blocked queries | `pg_stat_activity`, `wait_event` | Runaway queries or `lock` contention needing attention |

## Your Turn

Write a monitoring query that reports the five tables in `pg_stat_user_tables` with the lowest cache-friendliness, approximated by the highest ratio of sequential scans to `index scans`, a signal that those tables may be missing a useful `index`.

```postgresql with=monitoring_demo.sql
-- Write your query below
```

`SELECT relname, seq_scan, idx_scan, seq_scan - COALESCE(idx_scan, 0) AS scan_imbalance FROM pg_stat_user_tables ORDER BY scan_imbalance DESC LIMIT 5;` surfaces tables where sequential scans dominate over `index scans`, exactly the missing-`index` bottleneck covered in the performance unit, now framed as something to monitor continuously rather than diagnose only after a specific query is already reported as slow.

## Conclusion

Continuous monitoring of connection usage, table bloat, cache hit ratio, and long-running or blocked queries turns the diagnostic tools used reactively throughout this course into an early-warning system, catching degrading health before it becomes a full outage, rather than only after users are already affected. The final lesson in this unit, and this course, looks at a technique for both improving availability and spreading read load across more than one database server: replication.
