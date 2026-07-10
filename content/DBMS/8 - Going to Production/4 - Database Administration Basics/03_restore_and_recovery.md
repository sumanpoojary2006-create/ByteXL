## Introduction

A backup that has never been tested by actually restoring it is, in a very real sense, unverified: it might be corrupted, incomplete, or simply fail to apply cleanly, and nobody would know until the moment it is genuinely needed, which is the worst possible time to discover a problem. **Restore and recovery** is the practice of actually reconstructing a working database from a backup, and treating that process as something to rehearse deliberately, not something to attempt for the very first time during a real emergency.

## Restoring from a Logical Backup

A logical backup, produced with `pg_dump` as covered in the previous lesson, is restored by running its contents against a target database, recreating tables and reloading data.

```postgresql file=restore_demo.sql
CREATE TABLE shipments_backup_source (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments_backup_source (shipment_id, status) VALUES (1, 'in_transit'), (2, 'delivered');
```

```postgresql with=restore_demo.sql
-- A real logical restore, run from a terminal, looks roughly like:
-- psql -U postgres -d shipments_restored -f backup_2025_06_15.sql
-- This runs the CREATE TABLE and data-loading statements from the dump
-- file directly against a fresh, empty target database. The SQL-level
-- equivalent, restoring one table's data specifically via COPY, looks
-- like this pair of commands:
CREATE TABLE shipments_restored (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

COPY shipments_restored FROM STDIN WITH (FORMAT csv);
1,in_transit
2,delivered
\.

SELECT * FROM shipments_restored;
```

`COPY shipments_restored FROM STDIN` loads data directly into the freshly created table, mirroring what a full `pg_dump`-produced restore script does at scale, across every table in a database, in one automated pass. The restored table's contents exactly match the original, confirming the restore succeeded.

## Point-in-Time Recovery: Restoring to an Exact Moment

A full backup alone only restores a database to the exact moment that backup was taken, but a real incident, an accidental `DELETE` with no `WHERE` clause, for example, often needs recovery to a specific moment just before the mistake happened, not all the way back to last night's full backup, which would also lose every legitimate change made since then. Point-in-time recovery, or PITR, combines a full backup with the `write-ahead log` archive covered in the recovery unit, replaying logged changes forward from that backup up to, but not including, the moment of the mistake.

```postgresql with=restore_demo.sql
SELECT pg_current_wal_lsn() AS wal_position_now;
```

```postgresql with=restore_demo.sql
-- A real point-in-time recovery is configured roughly like:
-- restore the most recent full backup taken before the incident
-- set recovery_target_time = '2025-06-15 14:32:00'
-- start the server, which replays archived WAL from the backup forward,
-- stopping exactly at the specified target time, just before the mistake
SELECT 'Point-in-time recovery replays WAL up to a specific timestamp, not just to the last full backup' AS pitr_summary;
```

This is precisely why the `write-ahead logging` covered earlier in this course matters beyond crash recovery: the same log that lets a database recover from a power loss is what makes it possible to recover to an arbitrary moment in time, as long as the relevant log segments were archived somewhere durable rather than discarded once no longer needed for ordinary crash recovery.

## Why Restores Must Be Tested, Not Just Backups Taken

A backup file that exists is not proof that a restore will actually work; corruption, an incomplete transfer, or a subtly incompatible database version can all silently break a backup's usefulness without ever showing an obvious error at backup time.

```postgresql with=restore_demo.sql
SELECT COUNT(*) AS row_count_after_restore FROM shipments_restored;
```

A disciplined operations practice periodically performs a real, full restore, into a separate, isolated environment, and then verifies the result:

- Checking row counts
- Spot-checking specific known values
- Confirming `constraint`s and `index`es rebuilt correctly

This is exactly the kind of check the single query above represents in miniature. Skipping this verification step is one of the most common, and most costly, gaps in a team's backup strategy: the backups exist, but nobody actually knows whether they work until the day they are desperately needed and turn out not to.

## Restore and Recovery at a Glance

| Concept | Detail |
|---|---|
| Logical restore | Reapplies a `pg_dump`-produced script against a target database |
| Physical restore | Copies backed-up data files back into place |
| Point-in-time recovery | Combines a full backup with archived WAL to recover to an exact moment |
| Restore testing | Periodically performing and verifying a real restore, not just trusting that a backup exists |

## Your Turn

Simulate a restore by creating a new table `shipments_restored_v2`, loading it with the same two rows from `shipments_backup_source` using `COPY`, and then writing a verification query confirming the row count and contents match the original exactly.

```postgresql with=restore_demo.sql
-- Write your restore and verification below
```

Creating `shipments_restored_v2` with the same structure, loading it via `COPY shipments_restored_v2 FROM STDIN WITH (FORMAT csv);` followed by the same two data rows and `\.`, and then running `SELECT COUNT(*) FROM shipments_restored_v2;` alongside a direct comparison against `shipments_backup_source` is exactly the verification discipline this lesson has been building toward: never trust a restore without checking it.

## Conclusion

Restoring a backup, whether a logical restore reapplying a dump script or a `point-in-time recovery` replaying archived write-ahead logs to an exact moment, is only genuinely useful if it has actually been tested and verified ahead of time, since an unverified backup offers only the appearance of safety rather than the real thing. With maintenance, backups, and restores all covered, the next lesson turns to watching a live database's health continuously, catching problems before a restore is ever needed at all.
