## Introduction

`Role`s, privileges, `least privilege`, row-level security, and injection prevention, everything covered so far in this chapter, works to prevent unwanted access before it happens. **Auditing** is the complementary discipline for after the fact: recording who did what, and when, so that if something does go wrong, or simply needs reviewing later, there is an actual trail to examine, rather than only ever being able to guess.

## Recording Who Changed a Row, Using a Trigger

The `trigger` mechanism from earlier in this course is the natural building block for an audit trail, extended here to capture which `role` made a change, not just what changed.

```postgresql file=audit_demo.sql
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

```postgresql with=audit_demo.sql
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

`TG_OP` is a special variable automatically available inside a `trigger` function, holding the operation that fired it, `'INSERT'`, `'UPDATE'`, or `'DELETE'`. `current_user` captures exactly which `role`'s connection made the change, tying every audit entry back to a specific, accountable identity, exactly the accountability the `role`s lesson argued shared logins destroy. `to_jsonb(OLD)` and `to_jsonb(NEW)` capture the row's full contents before and after the change, as flexible JSON, letting one generic audit table handle any table's structure without needing a matching column-for-column `schema` of its own.

## Watching the Audit Trail Fill In

Every change to `shipments` from this point forward is captured automatically, with no cooperation required from whatever code issues the change.

```postgresql with=audit_demo.sql
UPDATE shipments SET status = 'delivered' WHERE shipment_id = 1;

SELECT table_name, action, changed_by, old_data, new_data FROM audit_log;
```

The audit entry shows `action = 'UPDATE'`, `changed_by` recording exactly which `role` made the change, and both the row's state before, `status: in_transit`, and after, `status: delivered`, preserved in `old_data` and `new_data`. This is a complete, precise record: not just that something changed, but exactly what changed, who changed it, and when.

## Auditing Reads, Not Just Writes

A `trigger` naturally captures `INSERT`, `UPDATE`, and `DELETE`, since those are the events a `trigger` fires on, but auditing "who read this sensitive data" is a genuinely different, harder problem, since a plain `SELECT` does not fire a `trigger` at all. PostgreSQL addresses this through server-level logging configuration and extensions purpose-built for statement auditing, tracking every query executed against the server, not just changes.

```postgresql with=audit_demo.sql
SHOW log_statement;
```

`log_statement` controls what PostgreSQL writes to its own server log, with settings ranging from logging nothing extra, to logging every data-modifying statement, to logging genuinely every statement including plain reads. Enabling comprehensive read-level auditing has a real performance cost, since every single query then incurs additional logging overhead, which is why it is typically reserved for tables holding especially sensitive data, rather than applied database-wide by default.

## Why Auditing Complements, Rather Than Replaces, Prevention

An audit trail does not stop an unauthorized action from happening; row-level security, `least privilege`, and careful `GRANT`s are what actually prevent it. Auditing exists for the cases prevention alone cannot fully cover:

- Detecting misuse by someone who did have legitimate access
- Investigating an incident after the fact to understand exactly what happened
- Satisfying compliance requirements that specifically demand a record of who touched sensitive data, independent of whether that access was ultimately appropriate

## Auditing at a Glance

| Concept | Detail |
|---|---|
| `Trigger`-based auditing | Captures `INSERT`/`UPDATE`/`DELETE`, including old and new row data and the acting `role` |
| `current_user` inside a `trigger` | Records exactly which `role` made a change |
| `TG_OP` | The operation that fired the `trigger`: `INSERT`, `UPDATE`, or `DELETE` |
| Statement/read logging | A server-level setting, needed to audit plain `SELECT` statements, at a real performance cost |
| Auditing's role | Detection and investigation after the fact, complementing prevention, not replacing it |

## Your Turn

Insert a new shipment and then delete it, and confirm the audit log captures both the `INSERT` and the `DELETE` as two separate, distinct entries, each recording the correct `role` and row data.

```postgresql with=audit_demo.sql
-- Write your insert, delete, and query below
```

Running `INSERT INTO shipments (shipment_id, status) VALUES (2, 'in_transit'); DELETE FROM shipments WHERE shipment_id = 2;` followed by `SELECT action, changed_by, old_data, new_data FROM audit_log WHERE (old_data->>'shipment_id')::int = 2 OR (new_data->>'shipment_id')::int = 2;` shows two entries: an `INSERT` with `new_data` populated and `old_data` null, and a `DELETE` with `old_data` populated and `new_data` null, exactly mirroring what genuinely happened to that row.

## Conclusion

Auditing, typically built on the `trigger` mechanism for writes and server-level logging for reads, records who did what and when, providing the after-the-fact trail that prevention mechanisms like row-level security and `least privilege` cannot offer on their own, valuable for detecting misuse, investigating incidents, and meeting compliance requirements. With `role`s, privileges, `least privilege`, row and column security, injection prevention, and auditing all covered, database security has been addressed from every angle this course covers. The final chapter turns to the day-to-day operational work of keeping a database running reliably once it is live.
