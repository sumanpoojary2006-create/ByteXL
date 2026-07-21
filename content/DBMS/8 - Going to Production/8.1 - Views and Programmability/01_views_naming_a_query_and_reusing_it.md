## Introduction

Devraj maintains reporting for a logistics company, and one particular `query`, `join`ing shipments to drivers and filtering for anything still in transit, gets copy-pasted into nearly every dashboard, script, and ad-hoc report his team writes. Every copy is a chance for someone to introduce a small inconsistency, one analyst filters on `status = 'in_transit'`, another accidentally types `'In Transit'`, and now two reports disagree about the same underlying data.

A **`view`** solves this by giving a `query` a permanent name in the `database` itself, so that everyone references the same saved definition instead of retyping it.

**Definition:** A `view` saves a `query` under a reusable name, always re-running against current data rather than storing a snapshot, which turns a frequently repeated, error-prone `query` into a single, consistently defined building block every downstream report can rely on.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_views_naming_a_query_and_reusing_it.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Devraj maintains reporting for a logistics company, and one particular query, joining shipments to drivers and filtering for anything still in transit, gets copy-pasted into nearly every dashboard, script, and ad-hoc report his team writes. Every copy is a.

ON-IMAGE TEXT: show a short bold title "Views Naming A Query And Reusing It" plus only these few labels, large and legible: Query, Join, View. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for views naming a query and reusing it](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_views_naming_a_query_and_reusing_it.png)

## Creating a View from an Existing Query

The `shipments` and `drivers` `tables` set up the recurring `query` Devraj's team keeps duplicating.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `drivers`

| driver_id | driver_name |
| --- | --- |
| 1 | Manoj Yadav |
| 2 | Farah Ali |
| 3 | Sunil Chauhan |

### `shipments`

| shipment_id | driver_id | status | destination |
| --- | --- | --- | --- |
| 1 | 1 | in_transit | Mumbai |
| 2 | 2 | delivered | Pune |
| 3 | 1 | in_transit | Nagpur |
| 4 | 3 | delayed | Nashik |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
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

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
CREATE VIEW active_shipments AS
SELECT s.shipment_id, d.driver_name, s.destination
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id
WHERE s.status = 'in_transit';

SELECT * FROM active_shipments;
```

Expected output:

| shipment_id | driver_name | destination |
| --- | --- | --- |
| 1 | Manoj Yadav | Mumbai |
| 3 | Manoj Yadav | Nagpur |

`CREATE VIEW active_shipments AS` saves the `join` and filter as a named object in the `database`. From that point on:

- `SELECT * FROM active_shipments` runs exactly as if `active_shipments` were a real `table`, even though it is really just this saved `query`, re-executed fresh every time it is referenced.
- Anyone on Devraj's team can write `SELECT * FROM active_shipments` instead of retyping the `join` and the exact spelling of the status filter, eliminating the inconsistency risk entirely.

![A view saves one named query definition that many reports can reuse](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_view_named_query_reused_by_reports.png)

## A View Always Reflects Current Data

A `view` does not store a snapshot of data from when it was created; it is only a saved `query` definition, run fresh every single time it is selected from.

```postgresql with=init.sql
CREATE VIEW active_shipments AS
SELECT s.shipment_id, d.driver_name, s.destination
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id
WHERE s.status = 'in_transit';

SELECT * FROM active_shipments;

UPDATE shipments SET status = 'delivered' WHERE shipment_id = 1;

SELECT * FROM active_shipments;
```

Expected output (from the second `SELECT`, after the `UPDATE`):

| shipment_id | driver_name | destination |
| --- | --- | --- |
| 3 | Manoj Yadav | Nagpur |

After Manoj's Mumbai shipment is marked delivered, querying `active_shipments` again immediately reflects that change, showing only the one remaining in-transit shipment, even though nothing about the `view` itself was touched. This is the core behavior that distinguishes a plain `view` from the `materialized view` covered later in this chapter: a plain `view` has no storage of its own and is always exactly as current as the underlying `tables`.

![An ordinary view stores no data and always reflects the current base tables](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_ordinary_view_no_storage_always_current.png)

## Views Can Be Queried Like Any Table

Because a `view` behaves like a `table` for `SELECT` purposes, it can be filtered, `join`ed, or aggregated further, exactly like any real `table`, letting a saved `view` serve as a clean, reusable building block for other `queries`.

```postgresql with=init.sql
CREATE VIEW active_shipments AS
SELECT s.shipment_id, d.driver_name, s.destination
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id
WHERE s.status = 'in_transit';

SELECT * FROM active_shipments;

SELECT driver_name, COUNT(*) AS active_shipment_count
FROM active_shipments
GROUP BY driver_name;
```

Expected output:

| driver_name | active_shipment_count |
| --- | ---: |
| Manoj Yadav | 2 |

This groups directly on top of `active_shipments`, without ever repeating the underlying `join` or filter condition, demonstrating exactly the reuse a `view` is meant to provide: the complexity of "what counts as an active shipment" is defined once, in the `view`, and every downstream `query` simply builds on top of that single, agreed-upon definition.

## Replacing or Removing a View

A `view`'s definition can be updated with `CREATE OR REPLACE VIEW`, and removed entirely with `DROP VIEW`, without affecting the underlying `tables` at all, since a `view` never owns any data of its own.

```postgresql with=init.sql
CREATE VIEW active_shipments AS
SELECT s.shipment_id, d.driver_name, s.destination
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id
WHERE s.status = 'in_transit';

SELECT * FROM active_shipments;

CREATE OR REPLACE VIEW active_shipments AS
SELECT s.shipment_id, d.driver_name, s.destination, s.status
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id
WHERE s.status IN ('in_transit', 'delayed');

SELECT * FROM active_shipments;
```

Expected output (from the final `SELECT`, against the redefined `view`):

| shipment_id | driver_name | destination | status |
| --- | --- | --- | --- |
| 1 | Manoj Yadav | Mumbai | in_transit |
| 3 | Manoj Yadav | Nagpur | in_transit |
| 4 | Sunil Chauhan | Nashik | delayed |

Redefining the `view` to also include delayed shipments changes what every downstream `query` built on top of `active_shipments` sees, immediately and consistently, without anyone needing to hunt down and update every copy-pasted version of the original `query` scattered across scripts and dashboards, exactly the maintenance problem a `view` exists to solve.

## Views at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CREATE VIEW name AS (query)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Saves a query under a reusable name</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Storage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">None; a <code>view</code> re-runs its underlying query every time it is selected from</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Freshness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always reflects the current state of the underlying tables</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CREATE OR REPLACE VIEW</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Updates the saved definition for everyone referencing it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>DROP VIEW</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removes the saved definition; underlying tables are untouched</td>
    </tr>
  </tbody>
</table>

## Your Turn

Create a `view` named `driver_shipment_summary` that shows each driver's name alongside their total shipment count, across all statuses, using the `drivers` and `shipments` `tables` above.

```postgresql with=init.sql
CREATE VIEW active_shipments AS
SELECT s.shipment_id, d.driver_name, s.destination
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id
WHERE s.status = 'in_transit';

SELECT * FROM active_shipments;

CREATE OR REPLACE VIEW active_shipments AS
SELECT s.shipment_id, d.driver_name, s.destination, s.status
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id
WHERE s.status IN ('in_transit', 'delayed');

SELECT * FROM active_shipments;

-- Write your view below
```

Expected result and verification:

If your `view` is `CREATE VIEW driver_shipment_summary AS SELECT d.driver_name, COUNT(s.shipment_id) AS total_shipments FROM drivers d LEFT JOIN shipments s ON d.driver_id = s.driver_id GROUP BY d.driver_name;`, selecting from it returns every driver, including any with zero shipments, thanks to the `LEFT JOIN` covered earlier in this course.

## Conclusion

A `view` saves a `query` under a reusable name, always re-running against current data rather than storing a snapshot, which turns a frequently repeated, error-prone `query` into a single, consistently defined building block every downstream report can rely on. Devraj's team can now agree on what "active" means for a shipment in exactly one place.

Not every `view` can be written to directly the same way it can be read from, and the next lesson looks closely at where that boundary sits.
