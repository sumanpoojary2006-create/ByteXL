## Introduction

The `recovery` mechanisms covered in an earlier unit, `write-ahead logging`, checkpoints, redo and undo, all protect against a server crash where the data files themselves remain intact. They offer no protection at all against the media failure named in that same unit: a disk that is physically destroyed, or a `table` dropped by mistake with no `transaction` left open to roll back.

The only real defense against losing data entirely is having a separate copy of it somewhere else, and a **`backup` strategy** is the deliberate plan for how, how often, and where that copy is kept.

**Definition:** A `backup` strategy is the deliberate answer to how, how often, and where a `database`'s data is copied somewhere safe, with logical `backups` like `pg_dump` offering portability and physical `backups` like `pg_basebackup` offering speed, and full versus incremental approaches trading simplicity against storage and time efficiency, all shaped by how much data loss is actually acceptable and how far back a `restore` might realistically need to reach.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_backup_strategies.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: The recovery mechanisms covered in an earlier unit, write-ahead logging, checkpoints, redo and undo, all protect against a server crash where the data files themselves remain intact. They offer no protection at all against the media failure named in that same.

ON-IMAGE TEXT: show a short bold title "Backup Strategies" plus only these few labels, large and legible: Table, Backup, Transaction. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for backup strategies](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_intro_backup_strategies_actual3d_58caf797.png)

## Logical Backups: A Portable Copy of the Data Itself

A logical `backup` captures the actual data and `schema` as a set of SQL statements or a portable data format, independent of the specific server it came from. PostgreSQL's `pg_dump` is the standard tool for this, run from outside the `database` as a command-line utility rather than as SQL itself.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `shipments`

| shipment_id | status |
| --- | --- |
| 1 | in_transit |
| 2 | delivered |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'delivered');
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
-- pg_dump runs outside of SQL itself, from a terminal, roughly like:
-- pg_dump -U postgres -d shipments_prod -f backup_2025_06_15.sql
-- This produces a plain-text file containing CREATE TABLE, COPY, and other
-- statements sufficient to fully recreate the database's current state
-- on a fresh server. A simplified illustration of the same idea, entirely
-- within SQL, is the COPY command, exporting a table's data directly:
COPY shipments TO STDOUT WITH (FORMAT csv, HEADER true);
```

Expected output (streamed as CSV text rather than a query result table):

```
shipment_id,status
1,in_transit
2,delivered
```

`pg_dump` produces a file that is, at its core, a script: running it against an empty `database` recreates three things exactly as they existed at the moment the dump was taken:

1. Every `table`

2. Every `constraint`

3. Every `row`

`COPY shipments TO STDOUT` demonstrates the same underlying idea in miniature and in pure SQL, exporting a `table`'s actual data in a portable format, though a real `pg_dump` captures the entire `database`'s `schema` and data together, not just one `table`'s `rows`.

## Physical Backups: A Copy of the Actual Files

A physical `backup`, using a tool like `pg_basebackup`, copies the `database`'s actual underlying data files directly, rather than translating them into portable SQL statements.

It is generally faster to produce and `restore` for very large `databases`, since it skips the work of translating data into and out of SQL text, but the resulting `backup` is tied to the exact same `database` version and is not as portable across different environments as a logical `backup`.

```postgresql with=init.sql
-- pg_basebackup also runs outside of SQL, roughly like:
-- pg_basebackup -U postgres -D /backups/full_2025_06_15 -Fp -P
-- This copies the actual data directory's files, combined with the
-- write-ahead log covered in the recovery unit, to reconstruct an
-- exact physical copy of the database as of that point in time.
SELECT current_setting('data_directory') AS data_directory_location;
```

Expected observation: PostgreSQL completes the statement, and the explanation below identifies the database object, permission, or operational effect to verify.

`current_setting('data_directory')` reports where PostgreSQL's actual physical data files live on this server, the same files a physical `backup` would copy directly, in contrast to a logical `backup`'s portable, `database`-independent SQL text.

![Logical backups capture portable data, while physical backups copy the database files](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_logical_vs_physical_backups.png)

## Full Backups vs. Incremental Backups

A full `backup` captures the entire `database` every time it runs, simple to reason about but potentially slow and storage-heavy for a large `database` backed up frequently.

An incremental `backup` captures only what has changed since the last `backup`, dramatically reducing both the time and storage each individual `backup` requires, at the cost of needing the full chain of `backups`, the last full one plus every incremental since, to perform a complete `restore`.

```postgresql with=init.sql
SELECT pg_current_wal_lsn() AS current_wal_position;
```

Expected result: PostgreSQL returns the rows described below. Compare the visible columns and row-level effect with the explanation, since security and administration settings may make some values environment-dependent.

The `write-ahead log` position, covered in depth in the `recovery` unit, is exactly what makes incremental, point-in-time `backup` strategies possible: rather than repeatedly copying the entire `database`, an incremental approach can archive just the log records generated since the last `backup`, later replaying them forward from a known full-`backup` starting point to reconstruct any specific moment in time.

![A full backup plus incremental WAL backups forms a recoverable timeline](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_full_backup_incremental_wal_chain.png)

## Choosing a Backup Frequency and Retention Policy

How often to back up, and how long to keep each `backup`, is a deliberate trade-off between the acceptable amount of data loss in the worst case and the storage cost of keeping many `backups` around.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Factor</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Consideration</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Backup frequency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How much data can this application afford to lose if the most recent backup is the only thing left, the gap since that backup determines the answer</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retention period</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How far back might a restore genuinely be needed, a single accidental deletion discovered a week later needs a week-old backup still available</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Storage cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More frequent backups and longer retention both directly increase the storage required to keep them all</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Backup location</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Storing a backup on the same server or disk as the live database defeats its purpose against a media failure entirely; it belongs somewhere physically separate</td>
    </tr>
  </tbody>
</table>

## Backup Strategies at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Captures</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Best for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logical (<code>pg_dump</code>)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Portable SQL/data representation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Portability across versions and environments, selective restores</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Physical (<code>pg_basebackup</code>)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Actual data files directly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speed, especially for very large databases</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Full</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The entire database, every time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simplicity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Incremental</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only what changed since the last backup</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduced time and storage cost for frequent backups</td>
    </tr>
  </tbody>
</table>

## Your Turn

Using the `shipments` `table` above, write the `COPY` command that would export the `table`'s data to a CSV format, and add a comment describing whether this represents a logical or physical `backup` approach, and why.

```postgresql with=init.sql
-- Write your COPY command and comment below
```

Expected result and verification:

`COPY shipments TO STDOUT WITH (FORMAT csv, HEADER true);` is a logical export, since it produces a portable representation of the data itself, in a format independent of PostgreSQL's own internal file structure, the same category `pg_dump` belongs to, as opposed to a physical `backup`, which would instead copy the actual underlying data files directly.

## Conclusion

A `backup` strategy is the deliberate answer to how, how often, and where a `database`'s data is copied somewhere safe, with logical `backups` like `pg_dump` offering portability and physical `backups` like `pg_basebackup` offering speed, and full versus incremental approaches trading simplicity against storage and time efficiency, all shaped by how much data loss is actually acceptable and how far back a `restore` might realistically need to reach.

Having a `backup` is only useful if it can actually be restored correctly, which is exactly what the next lesson covers.
