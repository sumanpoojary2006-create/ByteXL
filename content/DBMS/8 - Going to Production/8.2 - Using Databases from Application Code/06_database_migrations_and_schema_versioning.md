## Introduction

Every `CREATE TABLE` and `ALTER TABLE` in this course has been run once, by hand, against a single `database`.

A real application's `schema` changes constantly over its lifetime, new `columns`, new `tables`, new `constraint`s, and that `schema` has to change consistently across a developer's laptop, a testing environment, and a live production `database` serving real users, all without anyone manually re-typing the same `ALTER TABLE` statements in three different places and hoping they match.

A **`database` migration** is a versioned, ordered, tracked script that applies exactly one `schema` change, and the discipline built around running them is called `schema` versioning.

**Definition:** A `database` migration is a small, versioned, tracked script that applies exactly one `schema` change, recorded in a dedicated `table` so the same set of migrations can be safely and consistently applied across a developer's laptop, a testing environment, and production, with structure-preserving statements protecting existing data rather than destructive shortcuts that discard it.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_database_migrations_and_schema_versioning.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Every CREATE TABLE and ALTER TABLE in this course has been run once, by hand, against a single database. A real application's schema changes constantly over its lifetime, new columns, new tables, new constraints, and that schema has to change consistently.

ON-IMAGE TEXT: show a short bold title "Database Migrations And Schema Versioning" plus only these few labels, large and legible: Table, Schema, Migrations. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for database migrations and schema versioning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_intro_database_migrations_and_schema_versioning_matched_3e34de5a.png)

## The Problem Migrations Solve

Without any tracking, it is easy to lose track of which environment has which `schema` changes already applied.

## Source Data Used in This Lesson

The setup also creates the following empty supporting tables. Later statements populate them as the operation runs.

### Empty `shipments` table

| Column | Definition in the setup |
| --- | --- |
| `shipment_id` | `INTEGER PRIMARY KEY` |
| `status` | `TEXT` |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
-- A developer, working directly, might run this by hand on their laptop:
ALTER TABLE shipments ADD COLUMN priority TEXT DEFAULT 'normal';

SELECT * FROM shipments;
```

Expected output:

| shipment_id | status | priority |
| --- | --- | --- |
| *(no rows)* | | |

`shipments` was created empty by `init.sql`, so `ALTER TABLE ... ADD COLUMN priority` only changes the `table`'s structure, adding an empty `priority` `column` with a `'normal'` default for any future `row`; there is no data yet for the `SELECT` to return. This works perfectly on this one `database`. The problem appears the moment there is more than one `database` involved: did this same `ALTER TABLE` get run against the testing environment.

Against production. In what order, if there were several changes made this week.

Without a system tracking exactly which changes have been applied where, the honest answer is often "nobody is entirely sure," which is precisely the uncertainty migrations exist to remove.

## Tracking Applied Migrations with a Version Table

The standard solution is a dedicated `table`, present in every environment, that records exactly which migrations have already run there.

```postgresql with=init.sql
CREATE TABLE schema_migrations (
    version TEXT PRIMARY KEY,
    applied_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO schema_migrations (version) VALUES ('0001_create_shipments');
INSERT INTO schema_migrations (version) VALUES ('0002_add_priority_column');

SELECT * FROM schema_migrations ORDER BY version;
```

Expected output:

| version | applied_at |
| --- | --- |
| 0001_create_shipments | *(timestamp of the `INSERT`)* |
| 0002_add_priority_column | *(timestamp of the `INSERT`)* |

Every migration gets a unique, ordered identifier, here `0001_create_shipments` and `0002_add_priority_column`, and a migration tool checks this `table` before running anything:

- If a version is already recorded, that migration is skipped, since it has already been applied.
- If it is missing, the tool runs it and then records it. This is what makes it safe to run the exact same migration tool command against a fresh `database`, a testing `database` with some migrations already applied, and production, all at once, since each one only ever runs the migrations it is genuinely missing.

![Migrations apply ordered schema changes consistently across dev, test, and production](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_migrations_versioned_across_environments.png)

## Writing a Migration as a Deliberate, Reviewable Step

A migration is typically a small, single-purpose script, reviewed like any other code change, rather than an ad-hoc command typed directly against a live `database`.

```postgresql with=init.sql
CREATE TABLE schema_migrations (
    version TEXT PRIMARY KEY,
    applied_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO schema_migrations (version) VALUES ('0001_create_shipments');
INSERT INTO schema_migrations (version) VALUES ('0002_add_priority_column');

SELECT * FROM schema_migrations ORDER BY version;

-- Migration 0003_add_delivery_deadline.sql
ALTER TABLE shipments ADD COLUMN delivery_deadline DATE;

INSERT INTO schema_migrations (version) VALUES ('0003_add_delivery_deadline');

SELECT * FROM shipments;
SELECT * FROM schema_migrations ORDER BY version;
```

Expected output:

`shipments` still has no rows, but now carries the `delivery_deadline` `column`:

| shipment_id | status | priority | delivery_deadline |
| --- | --- | --- | --- |
| *(no rows)* | | | |

`schema_migrations` now records all three migrations:

| version | applied_at |
| --- | --- |
| 0001_create_shipments | *(timestamp of the `INSERT`)* |
| 0002_add_priority_column | *(timestamp of the `INSERT`)* |
| 0003_add_delivery_deadline | *(timestamp of the `INSERT`)* |

Writing the `ALTER TABLE` and the corresponding insert into `schema_migrations` together, as one unit, keeps the `schema` change and its record of having happened tightly coupled, exactly the kind of pairing a `transaction`, covered in an earlier unit, is well suited to wrap, so that either both take effect or neither does, never leaving the `schema` changed without the tracking `table` reflecting it.

## Why Migrations Should Avoid Destructive Shortcuts

A tempting but dangerous migration pattern is dropping and recreating a `table` to make a structural change, which discards every `row` of existing data along with it.

A properly written migration changes structure while preserving data, using `ALTER TABLE ADD COLUMN`, `ALTER TABLE ALTER COLUMN`, and similar structure-preserving statements, exactly the commands covered when SQL data definition was first introduced early in this course, rather than `DROP TABLE` followed by a fresh `CREATE TABLE`.

```postgresql with=init.sql
CREATE TABLE schema_migrations (
    version TEXT PRIMARY KEY,
    applied_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO schema_migrations (version) VALUES ('0001_create_shipments');
INSERT INTO schema_migrations (version) VALUES ('0002_add_priority_column');

SELECT * FROM schema_migrations ORDER BY version;

-- A dangerous shortcut, never appropriate for a production migration:
-- DROP TABLE shipments;
-- CREATE TABLE shipments (shipment_id INTEGER PRIMARY KEY, status TEXT, priority TEXT);
-- This silently destroys every existing row.

-- The safe, structure-preserving alternative, already demonstrated above:
ALTER TABLE shipments ADD COLUMN new_notes TEXT;
```

Expected output (from the `SELECT` earlier in this block, before the structure-preserving `ALTER TABLE` runs):

| version | applied_at |
| --- | --- |
| 0001_create_shipments | *(timestamp of the `INSERT`)* |
| 0002_add_priority_column | *(timestamp of the `INSERT`)* |

The final `ALTER TABLE shipments ADD COLUMN new_notes TEXT` returns no rows of its own; it just adds the `column` while leaving every existing `row` intact, in contrast with the commented-out `DROP TABLE` shortcut above it. This distinction, preserving data versus discarding it, is the single most important discipline in writing a safe migration, and it is exactly why migrations against a production `database` always deserve careful review before being applied, the same caution this course has emphasized around any `DROP` or `DELETE` since the modifying-data chapter early on.

![Safe migrations preserve existing data, while drop-and-recreate shortcuts destroy it](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_safe_migration_preserves_data.png)

## Database Migrations at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Migration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A small, versioned, single-purpose <code>schema</code> change script</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>schema_migrations</code> table</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tracks which migrations have already run in a given database</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Idempotent application</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Running the same migration tool anywhere only applies what is genuinely missing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safe migrations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use <code>ALTER TABLE</code>, preserve existing data; avoid <code>DROP TABLE</code> and recreate patterns</td>
    </tr>
  </tbody>
</table>

## Your Turn

Write a migration named `0004_add_carrier_column` that adds a `carrier` text `column` to `shipments`, and record it in `schema_migrations`, following the pattern established above.

```postgresql with=init.sql
CREATE TABLE schema_migrations (
    version TEXT PRIMARY KEY,
    applied_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO schema_migrations (version) VALUES ('0001_create_shipments');
INSERT INTO schema_migrations (version) VALUES ('0002_add_priority_column');

SELECT * FROM schema_migrations ORDER BY version;

-- Write your migration below
```

Expected result and verification:

A correct migration runs `ALTER TABLE shipments ADD COLUMN carrier TEXT;` followed by `INSERT INTO schema_migrations (version) VALUES ('0004_add_carrier_column');`, and a final `SELECT * FROM schema_migrations ORDER BY version;` confirms all four migrations are now recorded in order, with the underlying `shipments` `table`'s structure matching exactly what that history implies.

## Conclusion

A `database` migration is a small, versioned, tracked script that applies exactly one `schema` change, recorded in a dedicated `table` so the same set of migrations can be safely and consistently applied across a developer's laptop, a testing environment, and production, with structure-preserving statements protecting existing data rather than destructive shortcuts that discard it.

With connecting, `prepared statements`, `transactions`, pooling, ORMs, and migrations all covered from the application's side, the next chapter turns to a concern that touches every one of them: keeping a `database` secure.
