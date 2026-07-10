## Introduction

Every `CREATE TABLE` and `ALTER TABLE` in this course has been run once, by hand, against a single database. A real application's `schema` changes constantly over its lifetime, new columns, new tables, new `constraint`s, and that `schema` has to change consistently across a developer's laptop, a testing environment, and a live production database serving real users, all without anyone manually re-typing the same `ALTER TABLE` statements in three different places and hoping they match. A **database migration** is a versioned, ordered, tracked script that applies exactly one `schema` change, and the discipline built around running them is called `schema` versioning.

## The Problem Migrations Solve

Without any tracking, it is easy to lose track of which environment has which `schema` changes already applied.

```postgresql file=migrations_demo.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);
```

```postgresql with=migrations_demo.sql
-- A developer, working directly, might run this by hand on their laptop:
ALTER TABLE shipments ADD COLUMN priority TEXT DEFAULT 'normal';

SELECT * FROM shipments;
```

This works perfectly on this one database. The problem appears the moment there is more than one database involved: did this same `ALTER TABLE` get run against the testing environment. Against production. In what order, if there were several changes made this week. Without a system tracking exactly which changes have been applied where, the honest answer is often "nobody is entirely sure," which is precisely the uncertainty migrations exist to remove.

## Tracking Applied Migrations with a Version Table

The standard solution is a dedicated table, present in every environment, that records exactly which migrations have already run there.

```postgresql with=migrations_demo.sql
CREATE TABLE schema_migrations (
    version TEXT PRIMARY KEY,
    applied_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO schema_migrations (version) VALUES ('0001_create_shipments');
INSERT INTO schema_migrations (version) VALUES ('0002_add_priority_column');

SELECT * FROM schema_migrations ORDER BY version;
```

Every migration gets a unique, ordered identifier, here `0001_create_shipments` and `0002_add_priority_column`, and a migration tool checks this table before running anything:

- If a version is already recorded, that migration is skipped, since it has already been applied.
- If it is missing, the tool runs it and then records it. This is what makes it safe to run the exact same migration tool command against a fresh database, a testing database with some migrations already applied, and production, all at once, since each one only ever runs the migrations it is genuinely missing.

## Writing a Migration as a Deliberate, Reviewable Step

A migration is typically a small, single-purpose script, reviewed like any other code change, rather than an ad-hoc command typed directly against a live database.

```postgresql with=migrations_demo.sql
-- Migration 0003_add_delivery_deadline.sql
ALTER TABLE shipments ADD COLUMN delivery_deadline DATE;

INSERT INTO schema_migrations (version) VALUES ('0003_add_delivery_deadline');

SELECT * FROM shipments;
SELECT * FROM schema_migrations ORDER BY version;
```

Writing the `ALTER TABLE` and the corresponding insert into `schema_migrations` together, as one unit, keeps the `schema` change and its record of having happened tightly coupled, exactly the kind of pairing a transaction, covered in an earlier unit, is well suited to wrap, so that either both take effect or neither does, never leaving the `schema` changed without the tracking table reflecting it.

## Why Migrations Should Avoid Destructive Shortcuts

A tempting but dangerous migration pattern is dropping and recreating a table to make a structural change, which discards every row of existing data along with it. A properly written migration changes structure while preserving data, using `ALTER TABLE ADD COLUMN`, `ALTER TABLE ALTER COLUMN`, and similar structure-preserving statements, exactly the commands covered when SQL data definition was first introduced early in this course, rather than `DROP TABLE` followed by a fresh `CREATE TABLE`.

```postgresql with=migrations_demo.sql
-- A dangerous shortcut, never appropriate for a production migration:
-- DROP TABLE shipments;
-- CREATE TABLE shipments (shipment_id INTEGER PRIMARY KEY, status TEXT, priority TEXT);
-- This silently destroys every existing row.

-- The safe, structure-preserving alternative, already demonstrated above:
ALTER TABLE shipments ADD COLUMN new_notes TEXT;
```

This distinction, preserving data versus discarding it, is the single most important discipline in writing a safe migration, and it is exactly why migrations against a production database always deserve careful review before being applied, the same caution this course has emphasized around any `DROP` or `DELETE` since the modifying-data chapter early on.

## Database Migrations at a Glance

| Concept | Detail |
|---|---|
| Migration | A small, versioned, single-purpose `schema` change script |
| `schema_migrations` table | Tracks which migrations have already run in a given database |
| Idempotent application | Running the same migration tool anywhere only applies what is genuinely missing |
| Safe migrations | Use `ALTER TABLE`, preserve existing data; avoid `DROP TABLE` and recreate patterns |

## Your Turn

Write a migration named `0004_add_carrier_column` that adds a `carrier` text column to `shipments`, and record it in `schema_migrations`, following the pattern established above.

```postgresql with=migrations_demo.sql
-- Write your migration below
```

A correct migration runs `ALTER TABLE shipments ADD COLUMN carrier TEXT;` followed by `INSERT INTO schema_migrations (version) VALUES ('0004_add_carrier_column');`, and a final `SELECT * FROM schema_migrations ORDER BY version;` confirms all four migrations are now recorded in order, with the underlying `shipments` table's structure matching exactly what that history implies.

## Conclusion

A database migration is a small, versioned, tracked script that applies exactly one `schema` change, recorded in a dedicated table so the same set of migrations can be safely and consistently applied across a developer's laptop, a testing environment, and production, with structure-preserving statements protecting existing data rather than destructive shortcuts that discard it. With connecting, `prepared statements`, transactions, pooling, ORMs, and migrations all covered from the application's side, the next chapter turns to a concern that touches every one of them: keeping a database secure.
