## Introduction

Devraj's `active_shipments` `view` has been used for `SELECT` queries so far, but a colleague asks a natural next question: can a driver's dispatcher just `UPDATE active_shipments` directly to change a shipment's destination, instead of going back to the underlying `shipments` table? Sometimes yes, and sometimes no, depending on exactly how the `view` is built. A `view` built simply enough can be genuinely **updatable**, passing writes straight through to its underlying table, while a `view` involving a `join`, an aggregate, or certain other constructs cannot be written to directly at all.

## A Simple View Is Updatable by Default

A `view` built from a single table, with a straightforward `SELECT` and no aggregation, is updatable without any special setup.

```postgresql file=updatable_views_demo.sql
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

```postgresql with=updatable_views_demo.sql
UPDATE in_transit_shipments SET destination = 'Thane' WHERE shipment_id = 1;

SELECT * FROM shipments WHERE shipment_id = 1;
```

The `UPDATE` was issued against `in_transit_shipments`, the `view`, not `shipments` directly, and the underlying table's row genuinely changed, confirmed by the final `SELECT` against `shipments` itself. PostgreSQL is able to translate this write for two reasons:

1. `in_transit_shipments` maps unambiguously back to exactly one row in exactly one table.
2. There is no doubt about which row in `shipments` this update was meant for.

## A View with a Join Is Generally Not Updatable

The `active_shipments` `view` from the previous lesson `join`s `shipments` to `drivers`, and that `join` is exactly what breaks direct updatability, since a single row in the `view`'s result could conceptually correspond to changes in either underlying table, and the database has no reliable way to know which one was intended.

```postgresql with=updatable_views_demo.sql
CREATE TABLE drivers (
    driver_id INTEGER PRIMARY KEY,
    driver_name TEXT
);

INSERT INTO drivers (driver_id, driver_name) VALUES (1, 'Manoj Yadav'), (2, 'Farah Ali');

CREATE VIEW shipments_with_driver AS
SELECT s.shipment_id, d.driver_name, s.destination
FROM shipments s
JOIN drivers d ON s.driver_id = d.driver_id;

UPDATE shipments_with_driver SET destination = 'Thane' WHERE shipment_id = 1;
```

This `UPDATE` fails, since PostgreSQL refuses to guess how to translate a write against a `join`ed `view` back into the correct underlying table and row. The rule is not about the `view` being "too complicated" in a vague sense; it is specifically about whether the mapping from a `view` row back to exactly one underlying table row is unambiguous, and a `join` between two tables inherently breaks that guarantee.

## A View with Aggregation Is Never Updatable

A `view` built with `GROUP BY` or an `aggregate function` faces an even more fundamental problem: a single row in its result may represent many underlying rows collapsed together, so there is no single row to even target with a write.

```postgresql with=updatable_views_demo.sql
CREATE VIEW driver_shipment_counts AS
SELECT driver_id, COUNT(*) AS shipment_count
FROM shipments
GROUP BY driver_id;

UPDATE driver_shipment_counts SET shipment_count = 5 WHERE driver_id = 1;
```

This fails for a more fundamental reason than the `join` case: `shipment_count` is not a stored value at all, it is calculated fresh from however many rows currently match, so "setting" it to 5 is not a meaningful operation the database could even attempt to translate into a real change.

## Making a Join-Based View Writable with INSTEAD OF Triggers

For genuinely complex cases where writable access to a `join`ed or computed `view` is worth the effort, PostgreSQL supports `INSTEAD OF` `trigger`s, custom logic telling the database exactly how to translate a write against the `view` into specific changes on the correct underlying tables. This is a deliberate, hand-written escape hatch rather than something PostgreSQL infers automatically, and it is covered in full once `trigger`s themselves are introduced later in this chapter.

## Updatable Views at a Glance

| `View` built from | Updatable directly? |
|---|---|
| A single table, no aggregation | Yes, automatically |
| A `join` across multiple tables | No, ambiguous which table a write targets |
| `GROUP BY` or aggregate functions | No, rows do not map to single underlying rows |
| A `join` or aggregate, with `INSTEAD OF` `trigger`s | Yes, but only through custom, hand-written logic |

## Your Turn

Create a simple, single-table `view` named `delivered_shipments` filtering `shipments` for `status = 'delivered'`, then update a shipment's `destination` through that `view`, and confirm the change landed on the underlying `shipments` table.

```postgresql with=updatable_views_demo.sql
-- Write your view and update below
```

If your `view` is `CREATE VIEW delivered_shipments AS SELECT shipment_id, destination FROM shipments WHERE status = 'delivered';` followed by `UPDATE delivered_shipments SET destination = 'Kothrud' WHERE shipment_id = 2;`, a `SELECT * FROM shipments WHERE shipment_id = 2;` confirms the underlying row's destination genuinely changed to Kothrud.

## Conclusion

A `view` built from a single table with no aggregation is updatable automatically, since a row in the `view` maps unambiguously to one row in one underlying table, while a `view` involving a `join` or an aggregate cannot be written to directly, since that mapping becomes ambiguous or nonexistent, though `INSTEAD OF` `trigger`s exist as a deliberate way to bridge that gap when genuinely needed. Devraj now knows exactly which of his team's `view`s a dispatcher can safely write through directly. The next lesson introduces a different kind of `view` entirely, one that does store its own data rather than recomputing on every query.
