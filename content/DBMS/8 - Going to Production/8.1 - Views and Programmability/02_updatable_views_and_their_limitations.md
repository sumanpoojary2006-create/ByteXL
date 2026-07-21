## Introduction

Devraj's `active_shipments` `view` has been used for `SELECT` `queries` so far, but a colleague asks a natural next question: can a driver's dispatcher just `UPDATE active_shipments` directly to change a shipment's destination, instead of going back to the underlying `shipments` `table`? Sometimes yes, and sometimes no, depending on exactly how the `view` is built.

A `view` built simply enough can be genuinely **updatable**, passing writes straight through to its underlying `table`, while a `view` involving a `join`, an aggregate, or certain other constructs cannot be written to directly at all.

**Definition:** A `view` built from a single `table` with no aggregation is updatable automatically, since a `row` in the `view` maps unambiguously to one `row` in one underlying `table`, while a `view` involving a `join` or an aggregate cannot be written to directly, since that mapping becomes ambiguous or nonexistent, though `INSTEAD OF` `trigger`s exist as a deliberate way to bridge that gap when genuinely needed.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_updatable_views_and_their_limitations.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Devraj's activeshipments view has been used for SELECT queries so far, but a colleague asks a natural next question: can a driver's dispatcher just UPDATE activeshipments directly to change a shipment's destination, instead of going back to the underlying.

ON-IMAGE TEXT: show a short bold title "Updatable Views And Their Limitations" plus only these few labels, large and legible: Table, View, Select. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for updatable views and their limitations](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_intro_updatable_views_and_their_limitations_matched_99c00476.png)

## A Simple View Is Updatable by Default

A `view` built from a single `table`, with a straightforward `SELECT` and no aggregation, is updatable without any special setup.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `shipments`

| shipment_id | driver_id | status | destination |
| --- | --- | --- | --- |
| 1 | 1 | in_transit | Mumbai |
| 2 | 2 | delivered | Pune |
| 3 | 1 | in_transit | Nagpur |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    driver_id INTEGER,
    status TEXT,
    destination TEXT
);

INSERT INTO shipments (shipment_id, driver_id, status, destination) VALUES
(1, 1, 'in_transit', 'Mumbai'),
(2, 2, 'delivered', 'Pune'),
(3, 1, 'in_transit', 'Nagpur');

CREATE VIEW in_transit_shipments AS
SELECT shipment_id, driver_id, destination
FROM shipments
WHERE status = 'in_transit';
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
UPDATE in_transit_shipments SET destination = 'Thane' WHERE shipment_id = 1;

SELECT * FROM shipments WHERE shipment_id = 1;
```

Expected output:

| shipment_id | driver_id | status | destination |
| --- | --- | --- | --- |
| 1 | 1 | in_transit | Thane |

The `UPDATE` was issued against `in_transit_shipments`, the `view`, not `shipments` directly, and the underlying `table`'s `row` genuinely changed, confirmed by the final `SELECT` against `shipments` itself. PostgreSQL is able to translate this write for two reasons:

1. `in_transit_shipments` maps unambiguously back to exactly one `row` in exactly one `table`.

2. There is no doubt about which `row` in `shipments` this update was meant for.

![A simple view can pass an update through to exactly one base table row](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_simple_updatable_view_one_to_one_mapping.png)

## A View with a Join Is Generally Not Updatable

The `active_shipments` `view` from the previous lesson `join`s `shipments` to `drivers`, and that `join` is exactly what breaks direct updatability, since a single `row` in the `view`'s result could conceptually correspond to changes in either underlying `table`, and the `database` has no reliable way to know which one was intended.

```postgresql with=init.sql
CREATE TABLE drivers (
    driver_id INTEGER PRIMARY KEY,
    driver_name TEXT
);

INSERT INTO drivers (driver_id, driver_name) VALUES (1, 'Manoj Yadav'), (2, 'Farah Ali');

CREATE VIEW shipments_with_driver AS
SELECT s.shipment_id, d.driver_name, s.destination
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id;

-- This update would fail because the joined view is not directly updatable:
-- UPDATE shipments_with_driver SET destination = 'Thane' WHERE shipment_id = 1;

SELECT * FROM shipments_with_driver;
```

Expected output:

| shipment_id | driver_name | destination |
| --- | --- | --- |
| 1 | Manoj Yadav | Mumbai |
| 2 | Farah Ali | Pune |
| 3 | Manoj Yadav | Nagpur |

This `UPDATE` fails, since PostgreSQL refuses to guess how to translate a write against a `join`ed `view` back into the correct underlying `table` and `row`. The rule is not about the `view` being "too complicated" in a vague sense; it is specifically about whether the mapping from a `view` `row` back to exactly one underlying `table` `row` is unambiguous, and a `join` between two `tables` inherently breaks that guarantee.

## A View with Aggregation Is Never Updatable

A `view` built with `GROUP BY` or an `aggregate function` faces an even more fundamental problem: a single `row` in its result may represent many underlying `rows` collapsed together, so there is no single `row` to even target with a write.

```postgresql with=init.sql
CREATE TABLE drivers (
    driver_id INTEGER PRIMARY KEY,
    driver_name TEXT
);

INSERT INTO drivers (driver_id, driver_name) VALUES (1, 'Manoj Yadav'), (2, 'Farah Ali');

CREATE VIEW shipments_with_driver AS
SELECT s.shipment_id, d.driver_name, s.destination
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id;

-- This update would fail because the joined view is not directly updatable:
-- UPDATE shipments_with_driver SET destination = 'Thane' WHERE shipment_id = 1;

SELECT * FROM shipments_with_driver;

CREATE VIEW driver_shipment_counts AS
SELECT driver_id, COUNT(*) AS shipment_count
FROM shipments
GROUP BY driver_id;

-- This update would fail because shipment_count is computed:
-- UPDATE driver_shipment_counts SET shipment_count = 5 WHERE driver_id = 1;

SELECT * FROM driver_shipment_counts;
```

Expected output (from the final `SELECT`, against `driver_shipment_counts`):

| driver_id | shipment_count |
| --- | ---: |
| 1 | 2 |
| 2 | 1 |

This fails for a more fundamental reason than the `join` case: `shipment_count` is not a stored value at all, it is calculated fresh from however many `rows` currently match, so "setting" it to 5 is not a meaningful operation the `database` could even attempt to translate into a real change.

![Joined and aggregate views are not directly updatable because the target row is ambiguous or computed](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_join_and_aggregate_views_not_directly_updatable.png)

## Making a Join-Based View Writable with INSTEAD OF Triggers

For genuinely complex cases where writable access to a `join`ed or computed `view` is worth the effort, PostgreSQL supports `INSTEAD OF` `trigger`s, custom logic telling the `database` exactly how to translate a write against the `view` into specific changes on the correct underlying `tables`.

This is a deliberate, hand-written escape hatch rather than something PostgreSQL infers automatically, and it is covered in full once `trigger`s themselves are introduced later in this chapter.

## Updatable Views at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"><code>View</code> built from</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Updatable directly?</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single table, no aggregation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, automatically</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A <code>join</code> across multiple tables</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No, ambiguous which table a write targets</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>GROUP BY</code> or aggregate functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No, rows do not map to single underlying rows</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A <code>join</code> or aggregate, with <code>INSTEAD OF</code> <code>trigger</code>s</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, but only through custom, hand-written logic</td>
    </tr>
  </tbody>
</table>

## Your Turn

Create a simple, single-`table` `view` named `delivered_shipments` filtering `shipments` for `status = 'delivered'`, then update a shipment's `destination` through that `view`, and confirm the change landed on the underlying `shipments` `table`.

```postgresql with=init.sql
CREATE TABLE drivers (
    driver_id INTEGER PRIMARY KEY,
    driver_name TEXT
);

INSERT INTO drivers (driver_id, driver_name) VALUES (1, 'Manoj Yadav'), (2, 'Farah Ali');

CREATE VIEW shipments_with_driver AS
SELECT s.shipment_id, d.driver_name, s.destination
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id;

-- This update would fail because the joined view is not directly updatable:
-- UPDATE shipments_with_driver SET destination = 'Thane' WHERE shipment_id = 1;

SELECT * FROM shipments_with_driver;

CREATE VIEW driver_shipment_counts AS
SELECT driver_id, COUNT(*) AS shipment_count
FROM shipments
GROUP BY driver_id;

-- This update would fail because shipment_count is computed:
-- UPDATE driver_shipment_counts SET shipment_count = 5 WHERE driver_id = 1;

SELECT * FROM driver_shipment_counts;

-- Write your view and update below
```

Expected result and verification:

If your `view` is `CREATE VIEW delivered_shipments AS SELECT shipment_id, destination FROM shipments WHERE status = 'delivered';` followed by `UPDATE delivered_shipments SET destination = 'Kothrud' WHERE shipment_id = 2;`, a `SELECT * FROM shipments WHERE shipment_id = 2;` confirms the underlying `row`'s destination genuinely changed to Kothrud.

## Conclusion

A `view` built from a single `table` with no aggregation is updatable automatically, since a `row` in the `view` maps unambiguously to one `row` in one underlying `table`, while a `view` involving a `join` or an aggregate cannot be written to directly, since that mapping becomes ambiguous or nonexistent, though `INSTEAD OF` `trigger`s exist as a deliberate way to bridge that gap when genuinely needed.

Devraj now knows exactly which of his team's `view`s a dispatcher can safely write through directly. The next lesson introduces a different kind of `view` entirely, one that does store its own data rather than recomputing on every `query`.
