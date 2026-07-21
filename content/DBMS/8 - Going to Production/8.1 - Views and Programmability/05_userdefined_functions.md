## Introduction

Devraj's shipping cost calculation has grown complicated: a base rate depending on distance, a surcharge for oversized packages, and a discount for high-volume drivers, logic currently copy-pasted, slightly differently, into three different reports.

Unlike marking a shipment delivered, this is not a "run these statements together" problem; it is a "compute one value from some inputs" problem, meant to be used inside a `SELECT`, not called on its own as an action. A **user-defined `function`** fits this shape exactly: a named routine that takes inputs and returns a single computed value, usable anywhere a `query` expects a value.

**Definition:** A user-defined `function` computes and returns a value, or a set of `rows`, and is called from within a `query` rather than as a standalone action, always running as part of the caller's own `transaction` rather than managing one of its own, which is the defining difference from the `procedures` covered in the previous lesson.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_userdefined_functions.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Devraj's shipping cost calculation has grown complicated: a base rate depending on distance, a surcharge for oversized packages, and a discount for high-volume drivers, logic currently copy-pasted, slightly differently, into three different reports. Unlike.

ON-IMAGE TEXT: show a short bold title "Userdefined Functions" plus only these few labels, large and legible: Select, Userdefined, Functions. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for userdefined functions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_intro_userdefined_functions_clean_6f5d7f89.png)

## Creating a Simple Function

The `shipments` `table` holds the raw data a shipping-cost calculation depends on.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `shipments`

| shipment_id | distance_km | is_oversized |
| --- | --- | --- |
| 1 | 120.00 | FALSE |
| 2 | 450.00 | TRUE |
| 3 | 30.00 | FALSE |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    distance_km NUMERIC(10, 2),
    is_oversized BOOLEAN
);

INSERT INTO shipments (shipment_id, distance_km, is_oversized) VALUES
(1, 120.00, FALSE),
(2, 450.00, TRUE),
(3, 30.00, FALSE);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
CREATE FUNCTION calculate_shipping_cost(distance NUMERIC, oversized BOOLEAN)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
DECLARE
    base_cost NUMERIC;
BEGIN
    base_cost := distance * 8.5;
    IF oversized THEN
        base_cost := base_cost + 500.00;
    END IF;
    RETURN base_cost;
END;
$$;
```

Expected result: `CREATE FUNCTION` returns no rows; it registers `calculate_shipping_cost` so later statements in this lesson can call it. `CREATE FUNCTION calculate_shipping_cost(...) RETURNS NUMERIC` declares that this routine always produces exactly one `NUMERIC` value. Inside the body:

- `DECLARE` introduces a local variable, `base_cost`, used only within this `function`.
- `RETURN` sends the final computed value back to whatever called the `function`.

Unlike the `procedure` from the previous lesson, which performed actions and returned nothing, a `function`'s entire purpose is to compute and hand back a value.

## Using a Function Inside a Query

Because a `function` returns a value, it can be called directly inside `SELECT`, exactly like a built-in `function` such as `ROUND` or `COALESCE` covered much earlier in this course.

```postgresql with=init.sql
CREATE FUNCTION calculate_shipping_cost(distance NUMERIC, oversized BOOLEAN)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
DECLARE
    base_cost NUMERIC;
BEGIN
    base_cost := distance * 8.5;
    IF oversized THEN
        base_cost := base_cost + 500.00;
    END IF;
    RETURN base_cost;
END;
$$;

SELECT shipment_id, distance_km, is_oversized,
       calculate_shipping_cost(distance_km, is_oversized) AS shipping_cost
FROM shipments;
```

Expected output:

| shipment_id | distance_km | is_oversized | shipping_cost |
| --- | ---: | --- | ---: |
| 1 | 120.00 | FALSE | 1020.000 |
| 2 | 450.00 | TRUE | 4325.000 |
| 3 | 30.00 | FALSE | 255.000 |

- `calculate_shipping_cost(distance_km, is_oversized)` runs once per `row`, taking that `row`'s own `column` values as arguments, and its result appears as an ordinary computed `column`, just like any built-in `function` would.
- This is the behavior that makes `functions` so useful for exactly Devraj's problem: the shipping-cost logic now lives in one place, and every report that needs it simply calls the `function` rather than re-deriving the formula.

![A user-defined function takes inputs and returns a value inside a SELECT](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_user_defined_function_inputs_to_value.png)

## Functions Cannot Manage Their Own Transactions

A `function`, unlike a `procedure`, cannot issue its own `COMMIT` or `ROLLBACK`; it always runs as part of whatever `transaction` the calling statement is already inside.

```postgresql with=init.sql
CREATE FUNCTION calculate_shipping_cost(distance NUMERIC, oversized BOOLEAN)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
DECLARE
    base_cost NUMERIC;
BEGIN
    base_cost := distance * 8.5;
    IF oversized THEN
        base_cost := base_cost + 500.00;
    END IF;
    RETURN base_cost;
END;
$$;

SELECT calculate_shipping_cost(200.00, TRUE);
```

Expected output:

| calculate_shipping_cost |
| ---: |
| 2200.000 |

This restriction exists precisely because a `function` is meant to be called from within a `SELECT`, potentially many times in a single `query`, one call per `row`, and allowing it to independently commit or roll back partway through would make no sense in that context; a single `SELECT` is not something that can be partially committed `row` by `row`.

This is the clearest practical distinction between a `function` and the `procedure` from the previous lesson: a `function` computes a value inside a larger statement, a `procedure` performs a standalone, `transaction`-managing action.

![Functions return values inside SELECT, while procedures perform actions through CALL](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_function_vs_procedure_select_vs_call.png)

## Functions Can Also Return a Set of Rows

While `calculate_shipping_cost` returns a single value, a `function` can also be written to return an entire `table`-like result, usable in `FROM` exactly like the derived `tables` and CTEs covered earlier in this course.

```postgresql with=init.sql
CREATE FUNCTION calculate_shipping_cost(distance NUMERIC, oversized BOOLEAN)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
DECLARE
    base_cost NUMERIC;
BEGIN
    base_cost := distance * 8.5;
    IF oversized THEN
        base_cost := base_cost + 500.00;
    END IF;
    RETURN base_cost;
END;
$$;

CREATE FUNCTION oversized_shipments()
RETURNS TABLE (shipment_id INTEGER, distance_km NUMERIC)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT s.shipment_id, s.distance_km FROM shipments s WHERE s.is_oversized = TRUE;
END;
$$;

SELECT * FROM oversized_shipments();
```

Expected output:

| shipment_id | distance_km |
| --- | ---: |
| 2 | 450.00 |

- `RETURNS TABLE (...)` declares the shape of `rows` this `function` will produce, and `RETURN QUERY` runs an actual `SELECT` inside the `function`, streaming its `rows` back as the `function`'s result.
- Calling `oversized_shipments()` in `FROM` then behaves exactly like selecting from a `view`, except this one can accept parameters and contain more elaborate procedural logic than a plain `view`'s single `query` allows.

## Functions vs. Procedures at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Function</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Procedure</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invoked with</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Used inside <code>SELECT</code>, or called with <code>SELECT function_name(...)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CALL procedure_name(...)</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Returns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A value, or a set of rows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nothing (unless using <code>OUT</code> parameters)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can manage its own transaction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No, always part of the caller&#x27;s transaction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, including mid-procedure <code>COMMIT</code>/<code>ROLLBACK</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Typical use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Computing a reusable value or a reusable result set</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Multi-step actions that must be grouped as a unit</td>
    </tr>
  </tbody>
</table>

## Your Turn

Write a `function` named `apply_discount` that takes an `amount` and a `discount_percent`, both `NUMERIC`, and returns the discounted amount, then use it inside a `SELECT` against the `shipments` `table` above to apply a flat 10 discount percent to each shipment's `distance_km` value, purely as a numeric exercise.

```postgresql with=init.sql
CREATE FUNCTION calculate_shipping_cost(distance NUMERIC, oversized BOOLEAN)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
DECLARE
    base_cost NUMERIC;
BEGIN
    base_cost := distance * 8.5;
    IF oversized THEN
        base_cost := base_cost + 500.00;
    END IF;
    RETURN base_cost;
END;
$$;

CREATE FUNCTION oversized_shipments()
RETURNS TABLE (shipment_id INTEGER, distance_km NUMERIC)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT s.shipment_id, s.distance_km FROM shipments s WHERE s.is_oversized = TRUE;
END;
$$;

SELECT * FROM oversized_shipments();

-- Write your function and query below
```

Expected result and verification:

A correct `function` computes `amount - (amount * discount_percent / 100)` and returns it; calling `SELECT shipment_id, apply_discount(distance_km, 10) AS discounted_distance FROM shipments;` applies it `row` by `row`, exactly the same reusable pattern `calculate_shipping_cost` demonstrated earlier.

## Conclusion

A user-defined `function` computes and returns a value, or a set of `rows`, and is called from within a `query` rather than as a standalone action, always running as part of the caller's own `transaction` rather than managing one of its own, which is the defining difference from the `procedures` covered in the previous lesson. Devraj's shipping-cost formula now lives in one `function`, called consistently everywhere it is needed.

The next lesson introduces a routine that runs automatically, in response to a `table` change, rather than being called explicitly at all.
