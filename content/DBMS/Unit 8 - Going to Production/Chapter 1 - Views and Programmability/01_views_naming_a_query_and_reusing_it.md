## Introduction

Devraj maintains reporting for a logistics company, and one particular query, `join`ing shipments to drivers and filtering for anything still in transit, gets copy-pasted into nearly every dashboard, script, and ad-hoc report his team writes. Every copy is a chance for someone to introduce a small inconsistency, one analyst filters on `status = 'in_transit'`, another accidentally types `'In Transit'`, and now two reports disagree about the same underlying data. A **`view`** solves this by giving a query a permanent name in the database itself, so that everyone references the same saved definition instead of retyping it.

## Creating a View from an Existing Query

The `shipments` and `drivers` tables set up the recurring query Devraj's team keeps duplicating.

```postgresql file=views_demo.sql
CREATE TABLE drivers (
    driver_id INTEGER PRIMARY KEY,
    driver_name TEXT
);

CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    driver_id INTEGER REFERENCES drivers(driver_id),
    status TEXT,
    destination TEXT
);

INSERT INTO drivers (driver_id, driver_name) VALUES
(1, 'Manoj Yadav'), (2, 'Farah Ali'), (3, 'Sunil Chauhan');

INSERT INTO shipments (shipment_id, driver_id, status, destination) VALUES
(1, 1, 'in_transit', 'Mumbai'),
(2, 2, 'delivered', 'Pune'),
(3, 1, 'in_transit', 'Nagpur'),
(4, 3, 'delayed', 'Nashik');
```

```postgresql with=views_demo.sql
CREATE VIEW active_shipments AS
SELECT s.shipment_id, d.driver_name, s.destination
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id
WHERE s.status = 'in_transit';

SELECT * FROM active_shipments;
```

`CREATE VIEW active_shipments AS` saves the `join` and filter as a named object in the database. From that point on:

- `SELECT * FROM active_shipments` runs exactly as if `active_shipments` were a real table, even though it is really just this saved query, re-executed fresh every time it is referenced.
- Anyone on Devraj's team can write `SELECT * FROM active_shipments` instead of retyping the `join` and the exact spelling of the status filter, eliminating the inconsistency risk entirely.

## A View Always Reflects Current Data

A `view` does not store a snapshot of data from when it was created; it is only a saved query definition, run fresh every single time it is selected from.

```postgresql with=views_demo.sql
UPDATE shipments SET status = 'delivered' WHERE shipment_id = 1;

SELECT * FROM active_shipments;
```

After Manoj's Mumbai shipment is marked delivered, querying `active_shipments` again immediately reflects that change, showing only the one remaining in-transit shipment, even though nothing about the `view` itself was touched. This is the core behavior that distinguishes a plain `view` from the `materialized view` covered later in this chapter: a plain `view` has no storage of its own and is always exactly as current as the underlying tables.

## Views Can Be Queried Like Any Table

Because a `view` behaves like a table for `SELECT` purposes, it can be filtered, `join`ed, or aggregated further, exactly like any real table, letting a saved `view` serve as a clean, reusable building block for other queries.

```postgresql with=views_demo.sql
SELECT driver_name, COUNT(*) AS active_shipment_count
FROM active_shipments
GROUP BY driver_name;
```

This groups directly on top of `active_shipments`, without ever repeating the underlying `join` or filter condition, demonstrating exactly the reuse a `view` is meant to provide: the complexity of "what counts as an active shipment" is defined once, in the `view`, and every downstream query simply builds on top of that single, agreed-upon definition.

## Replacing or Removing a View

A `view`'s definition can be updated with `CREATE OR REPLACE VIEW`, and removed entirely with `DROP VIEW`, without affecting the underlying tables at all, since a `view` never owns any data of its own.

```postgresql with=views_demo.sql
CREATE OR REPLACE VIEW active_shipments AS
SELECT s.shipment_id, d.driver_name, s.destination, s.status
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id
WHERE s.status IN ('in_transit', 'delayed');

SELECT * FROM active_shipments;
```

Redefining the `view` to also include delayed shipments changes what every downstream query built on top of `active_shipments` sees, immediately and consistently, without anyone needing to hunt down and update every copy-pasted version of the original query scattered across scripts and dashboards, exactly the maintenance problem a `view` exists to solve.

## Views at a Glance

| Concept | Detail |
|---|---|
| `CREATE VIEW name AS (query)` | Saves a query under a reusable name |
| Storage | None; a `view` re-runs its underlying query every time it is selected from |
| Freshness | Always reflects the current state of the underlying tables |
| `CREATE OR REPLACE VIEW` | Updates the saved definition for everyone referencing it |
| `DROP VIEW` | Removes the saved definition; underlying tables are untouched |

## Your Turn

Create a `view` named `driver_shipment_summary` that shows each driver's name alongside their total shipment count, across all statuses, using the `drivers` and `shipments` tables above.

```postgresql with=views_demo.sql
-- Write your view below
```

If your `view` is `CREATE VIEW driver_shipment_summary AS SELECT d.driver_name, COUNT(s.shipment_id) AS total_shipments FROM drivers d LEFT JOIN shipments s ON d.driver_id = s.driver_id GROUP BY d.driver_name;`, selecting from it returns every driver, including any with zero shipments, thanks to the `LEFT JOIN` covered earlier in this course.

## Conclusion

A `view` saves a query under a reusable name, always re-running against current data rather than storing a snapshot, which turns a frequently repeated, error-prone query into a single, consistently defined building block every downstream report can rely on. Devraj's team can now agree on what "active" means for a shipment in exactly one place. Not every `view` can be written to directly the same way it can be read from, and the next lesson looks closely at where that boundary sits.
