## Introduction

The recovery mechanisms covered in an earlier unit, `write-ahead logging`, checkpoints, redo and undo, all protect against a server crash where the data files themselves remain intact. They offer no protection at all against the media failure named in that same unit: a disk that is physically destroyed, or a table dropped by mistake with no transaction left open to roll back. The only real defense against losing data entirely is having a separate copy of it somewhere else, and a **backup strategy** is the deliberate plan for how, how often, and where that copy is kept.

## Logical Backups: A Portable Copy of the Data Itself

A logical backup captures the actual data and `schema` as a set of SQL statements or a portable data format, independent of the specific server it came from. PostgreSQL's `pg_dump` is the standard tool for this, run from outside the database as a command-line utility rather than as SQL itself.

```postgresql file=backup_demo.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'delivered');
```

```postgresql with=backup_demo.sql
-- pg_dump runs outside of SQL itself, from a terminal, roughly like:
-- pg_dump -U postgres -d shipments_prod -f backup_2025_06_15.sql
-- This produces a plain-text file containing CREATE TABLE, COPY, and other
-- statements sufficient to fully recreate the database's current state
-- on a fresh server. A simplified illustration of the same idea, entirely
-- within SQL, is the COPY command, exporting a table's data directly:
COPY shipments TO STDOUT WITH (FORMAT csv, HEADER true);
```

`pg_dump` produces a file that is, at its core, a script: running it against an empty database recreates three things exactly as they existed at the moment the dump was taken:

1. Every table
2. Every `constraint`
3. Every row

`COPY shipments TO STDOUT` demonstrates the same underlying idea in miniature and in pure SQL, exporting a table's actual data in a portable format, though a real `pg_dump` captures the entire database's `schema` and data together, not just one table's rows.

## Physical Backups: A Copy of the Actual Files

A physical backup, using a tool like `pg_basebackup`, copies the database's actual underlying data files directly, rather than translating them into portable SQL statements. It is generally faster to produce and restore for very large databases, since it skips the work of translating data into and out of SQL text, but the resulting backup is tied to the exact same database version and is not as portable across different environments as a logical backup.

```postgresql with=backup_demo.sql
-- pg_basebackup also runs outside of SQL, roughly like:
-- pg_basebackup -U postgres -D /backups/full_2025_06_15 -Fp -P
-- This copies the actual data directory's files, combined with the
-- write-ahead log covered in the recovery unit, to reconstruct an
-- exact physical copy of the database as of that point in time.
SELECT current_setting('data_directory') AS data_directory_location;
```

`current_setting('data_directory')` reports where PostgreSQL's actual physical data files live on this server, the same files a physical backup would copy directly, in contrast to a logical backup's portable, database-independent SQL text.

## Full Backups vs. Incremental Backups

A full backup captures the entire database every time it runs, simple to reason about but potentially slow and storage-heavy for a large database backed up frequently. An incremental backup captures only what has changed since the last backup, dramatically reducing both the time and storage each individual backup requires, at the cost of needing the full chain of backups, the last full one plus every incremental since, to perform a complete restore.

```postgresql with=backup_demo.sql
SELECT pg_current_wal_lsn() AS current_wal_position;
```

The `write-ahead log` position, covered in depth in the recovery unit, is exactly what makes incremental, point-in-time backup strategies possible: rather than repeatedly copying the entire database, an incremental approach can archive just the log records generated since the last backup, later replaying them forward from a known full-backup starting point to reconstruct any specific moment in time.

## Choosing a Backup Frequency and Retention Policy

How often to back up, and how long to keep each backup, is a deliberate trade-off between the acceptable amount of data loss in the worst case and the storage cost of keeping many backups around.

| Factor | Consideration |
|---|---|
| Backup frequency | How much data can this application afford to lose if the most recent backup is the only thing left, the gap since that backup determines the answer |
| Retention period | How far back might a restore genuinely be needed, a single accidental deletion discovered a week later needs a week-old backup still available |
| Storage cost | More frequent backups and longer retention both directly increase the storage required to keep them all |
| Backup location | Storing a backup on the same server or disk as the live database defeats its purpose against a media failure entirely; it belongs somewhere physically separate |

## Backup Strategies at a Glance

| Type | Captures | Best for |
|---|---|---|
| Logical (`pg_dump`) | Portable SQL/data representation | Portability across versions and environments, selective restores |
| Physical (`pg_basebackup`) | Actual data files directly | Speed, especially for very large databases |
| Full | The entire database, every time | Simplicity |
| Incremental | Only what changed since the last backup | Reduced time and storage cost for frequent backups |

## Your Turn

Using the `shipments` table above, write the `COPY` command that would export the table's data to a CSV format, and add a comment describing whether this represents a logical or physical backup approach, and why.

```postgresql with=backup_demo.sql
-- Write your COPY command and comment below
```

`COPY shipments TO STDOUT WITH (FORMAT csv, HEADER true);` is a logical export, since it produces a portable representation of the data itself, in a format independent of PostgreSQL's own internal file structure, the same category `pg_dump` belongs to, as opposed to a physical backup, which would instead copy the actual underlying data files directly.

## Conclusion

A backup strategy is the deliberate answer to how, how often, and where a database's data is copied somewhere safe, with logical backups like `pg_dump` offering portability and physical backups like `pg_basebackup` offering speed, and full versus incremental approaches trading simplicity against storage and time efficiency, all shaped by how much data loss is actually acceptable and how far back a restore might realistically need to reach. Having a backup is only useful if it can actually be restored correctly, which is exactly what the next lesson covers.
