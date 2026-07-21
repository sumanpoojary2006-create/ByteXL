## Introduction

The security mechanisms covered so far, `roles`, privileges, `least privilege`, `row-level security`, and injection prevention, all work to prevent unwanted access before it happens. **Auditing** is the complementary discipline for after the fact: recording who did what and when, so that if something goes wrong, or simply needs reviewing later, the team has an actual trail to examine instead of forcing everyone to guess.

**Definition:** Auditing, typically built on the `trigger` mechanism for writes and server-level logging for reads, records who did what and when, providing the after-the-fact trail that prevention mechanisms like `row-level security` and `least privilege` cannot offer on their own, valuable for detecting misuse, investigating incidents, and meeting compliance requirements.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_auditing_and_tracking_data_access.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: The security mechanisms covered so far, roles, privileges, least privilege, row-level security, and injection prevention, all work to prevent unwanted access before it happens. Auditing is the complementary discipline for after the fact: recording who did.

ON-IMAGE TEXT: show a short bold title "Auditing And Tracking Data Access" plus only these few labels, large and legible: Row, Auditing, Tracking. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for auditing and tracking data access](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_intro_auditing_and_tracking_data_access_actual3d_3ba9dd00.png)

## Recording Who Changed a Row, Using a Trigger

The `trigger` mechanism from earlier in this course is the natural building block for an audit trail, extended here to capture which `role` made a change, not just what changed.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `shipments`

| shipment_id | status |
| --- | --- |
| 1 | in_transit |

The setup also creates the following empty supporting tables. Later statements populate them as the operation runs.

### Empty `audit_log` table

| Column | Definition in the setup |
| --- | --- |
| `audit_id` | `SERIAL PRIMARY KEY` |
| `table_name` | `TEXT` |
| `action` | `TEXT` |
| `changed_by` | `TEXT` |
| `changed_at` | `TIMESTAMP DEFAULT NOW()` |
| `old_data` | `JSONB` |
| `new_data` | `JSONB` |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

CREATE TABLE audit_log (
    audit_id SERIAL PRIMARY KEY,
    table_name TEXT,
    action TEXT,
    changed_by TEXT,
    changed_at TIMESTAMP DEFAULT NOW(),
    old_data JSONB,
    new_data JSONB
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit');
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
CREATE FUNCTION audit_shipments_change()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO audit_log (table_name, action, changed_by, old_data, new_data)
    VALUES (
        'shipments',
        TG_OP,
        current_user,
        CASE WHEN TG_OP != 'INSERT' THEN to_jsonb(OLD) ELSE NULL END,
        CASE WHEN TG_OP != 'DELETE' THEN to_jsonb(NEW) ELSE NULL END
    );
    RETURN COALESCE(NEW, OLD);
END;
$$;

CREATE TRIGGER trg_audit_shipments
AFTER INSERT OR UPDATE OR DELETE ON shipments
FOR EACH ROW
EXECUTE FUNCTION audit_shipments_change();
```

Expected result: `CREATE FUNCTION` and `CREATE TRIGGER` return no rows; they arm the audit mechanism on `shipments` without touching any data yet. The next section fires the `trigger` for real and shows the row it writes into `audit_log`.

- `TG_OP` is a special variable automatically available inside a `trigger` `function`, holding the operation that fired it, `'INSERT'`, `'UPDATE'`, or `'DELETE'`. `current_user` captures exactly which `role`'s `connection` made the change, tying every audit entry back to a specific, accountable identity.
- This preserves the accountability that shared logins destroy.
- `to_jsonb(OLD)` and `to_jsonb(NEW)` capture the `row`'s full contents before and after the change as flexible JSON.
- That lets one generic audit `table` handle any `table`'s structure without needing a matching `column`-for-`column` `schema` of its own.

## Watching the Audit Trail Fill In

Every change to `shipments` from this point forward is captured automatically, with no cooperation required from whatever code issues the change.

```postgresql with=init.sql
CREATE FUNCTION audit_shipments_change()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO audit_log (table_name, action, changed_by, old_data, new_data)
    VALUES (
        'shipments',
        TG_OP,
        current_user,
        CASE WHEN TG_OP != 'INSERT' THEN to_jsonb(OLD) ELSE NULL END,
        CASE WHEN TG_OP != 'DELETE' THEN to_jsonb(NEW) ELSE NULL END
    );
    RETURN COALESCE(NEW, OLD);
END;
$$;

CREATE TRIGGER trg_audit_shipments
AFTER INSERT OR UPDATE OR DELETE ON shipments
FOR EACH ROW
EXECUTE FUNCTION audit_shipments_change();

UPDATE shipments SET status = 'delivered' WHERE shipment_id = 1;

SELECT table_name, action, changed_by, old_data, new_data FROM audit_log;
```

Expected output:

| table_name | action | changed_by | old_data | new_data |
| --- | --- | --- | --- | --- |
| shipments | UPDATE | postgres | {"status": "in_transit", "shipment_id": 1} | {"status": "delivered", "shipment_id": 1} |

The audit entry shows `action = 'UPDATE'`, `changed_by` recording exactly which `role` made the change, and both the `row`'s state before, `status: in_transit`, and after, `status: delivered`, preserved in `old_data` and `new_data`. This is a complete, precise record: not just that something changed, but exactly what changed, who changed it, and when.

![A trigger-based audit log records who changed a row and the old and new values](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_audit_trigger_records_who_old_new.png)

## Auditing Reads, Not Just Writes

A `trigger` naturally captures `INSERT`, `UPDATE`, and `DELETE`, since those are the events a `trigger` fires on, but auditing "who read this sensitive data" is a genuinely different, harder problem, since a plain `SELECT` does not fire a `trigger` at all. PostgreSQL addresses this through server-level logging configuration and extensions purpose-built for statement auditing, tracking every `query` executed against the server, not just changes.

```postgresql with=init.sql
CREATE FUNCTION audit_shipments_change()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO audit_log (table_name, action, changed_by, old_data, new_data)
    VALUES (
        'shipments',
        TG_OP,
        current_user,
        CASE WHEN TG_OP != 'INSERT' THEN to_jsonb(OLD) ELSE NULL END,
        CASE WHEN TG_OP != 'DELETE' THEN to_jsonb(NEW) ELSE NULL END
    );
    RETURN COALESCE(NEW, OLD);
END;
$$;

CREATE TRIGGER trg_audit_shipments
AFTER INSERT OR UPDATE OR DELETE ON shipments
FOR EACH ROW
EXECUTE FUNCTION audit_shipments_change();

SHOW log_statement;
```

Expected observation: PostgreSQL returns live server metadata. Values differ across OneCompiler runs, so verify the meaning of each column and the trend described below rather than matching a fixed number.

- `log_statement` controls what PostgreSQL writes to its own server log, with settings ranging from logging nothing extra, to logging every data-modifying statement, to logging genuinely every statement including plain reads.
- Enabling comprehensive read-level auditing has a real performance cost, since every single `query` then incurs additional logging overhead, which is why it is typically reserved for `tables` holding especially sensitive data, rather than applied `database`-wide by default.

## Why Auditing Complements, Rather Than Replaces, Prevention

An audit trail does not stop an unauthorized action from happening; `row-level security`, `least privilege`, and careful `GRANT`s are what actually prevent it. Auditing exists for the cases prevention alone cannot fully cover:

- Detecting misuse by someone who did have legitimate access
- Investigating an incident after the fact to understand exactly what happened
- Satisfying compliance requirements that specifically demand a record of who touched sensitive data, independent of whether that access was ultimately appropriate

![Prevention blocks unwanted access, while auditing records activity for later investigation](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_auditing_complements_prevention.png)

## Auditing at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>Trigger</code>-based auditing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Captures <code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>, including old and new row data and the acting <code>role</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>current_user</code> inside a <code>trigger</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Records exactly which <code>role</code> made a change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>TG_OP</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The operation that fired the <code>trigger</code>: <code>INSERT</code>, <code>UPDATE</code>, or <code>DELETE</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Statement/read logging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A server-level setting, needed to audit plain <code>SELECT</code> statements, at a real performance cost</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Auditing&#x27;s role</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detection and investigation after the fact, complementing prevention, not replacing it</td>
    </tr>
  </tbody>
</table>

## Your Turn

Insert a new shipment and then delete it, and confirm the audit log captures both the `INSERT` and the `DELETE` as two separate, distinct entries, each recording the correct `role` and `row` data.

```postgresql with=init.sql
CREATE FUNCTION audit_shipments_change()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO audit_log (table_name, action, changed_by, old_data, new_data)
    VALUES (
        'shipments',
        TG_OP,
        current_user,
        CASE WHEN TG_OP != 'INSERT' THEN to_jsonb(OLD) ELSE NULL END,
        CASE WHEN TG_OP != 'DELETE' THEN to_jsonb(NEW) ELSE NULL END
    );
    RETURN COALESCE(NEW, OLD);
END;
$$;

CREATE TRIGGER trg_audit_shipments
AFTER INSERT OR UPDATE OR DELETE ON shipments
FOR EACH ROW
EXECUTE FUNCTION audit_shipments_change();

-- Write your insert, delete, and query below
```

Expected result and verification:

Running `INSERT INTO shipments (shipment_id, status) VALUES (2, 'in_transit');` followed by `DELETE FROM shipments WHERE shipment_id = 2;` and then `SELECT action, changed_by, old_data, new_data FROM audit_log WHERE (old_data->>'shipment_id')::int = 2 OR (new_data->>'shipment_id')::int = 2;` gives:

| action | changed_by | old_data | new_data |
| --- | --- | --- | --- |
| INSERT | postgres | *NULL* | {"status": "in_transit", "shipment_id": 2} |
| DELETE | postgres | {"status": "in_transit", "shipment_id": 2} | *NULL* |

Two entries come back: an `INSERT` with `new_data` populated and `old_data` null, and a `DELETE` with `old_data` populated and `new_data` null, exactly mirroring what genuinely happened to that `row`.

## Conclusion

Auditing, typically built on the `trigger` mechanism for writes and server-level logging for reads, records who did what and when, providing the after-the-fact trail that prevention mechanisms like `row-level security` and `least privilege` cannot offer on their own, valuable for detecting misuse, investigating incidents, and meeting compliance requirements. With `role`s, privileges, `least privilege`, `row` and `column` security, injection prevention, and auditing all covered, `database` security has been addressed from every angle this course covers.

The final chapter turns to the day-to-day operational work of keeping a `database` running reliably once it is live.
