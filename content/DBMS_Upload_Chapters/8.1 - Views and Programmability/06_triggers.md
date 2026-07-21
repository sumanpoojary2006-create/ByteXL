## Introduction

The `mark_shipment_delivered` procedure from earlier in this chapter guarantees a log entry is created, but only if every caller remembers to use that procedure instead of writing a plain `UPDATE` directly against `shipments`. Devraj wants a stronger guarantee: no matter how a shipment's status changes, a log entry should always be created automatically:

- Through the procedure
- Through a direct `UPDATE`
- Through a future script nobody has written yet

A **trigger** delivers exactly this: a piece of logic the database runs automatically whenever a specified event, an insert, update, or delete, happens on a table, with no possibility of a caller forgetting to invoke it.

**Definition:** A trigger runs automatically in response to an insert, update, or delete, with `BEFORE` triggers able to validate or reject a change before it happens, `AFTER` triggers able to react once a change has completed, and `INSTEAD OF` triggers able to make an otherwise non-writable view accept writes, all without requiring any cooperation from whoever issues the original statement.

![Intro visual for triggers](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_intro_triggers.png)

## Creating a Trigger Function and Attaching It

A trigger is built from two pieces: a special kind of function describing what to do, and a `CREATE TRIGGER` statement attaching that function to a specific table and event.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `shipments`

| shipment_id | status |
| --- | --- |
| 1 | in_transit |
| 2 | in_transit |

The setup also creates the following empty supporting tables. Later statements populate them as the operation runs.

### Empty `shipment_log` table

| Column | Definition in the setup |
| --- | --- |
| `log_id` | `SERIAL PRIMARY KEY` |
| `shipment_id` | `INTEGER` |
| `old_status` | `TEXT` |
| `new_status` | `TEXT` |
| `logged_at` | `TIMESTAMP DEFAULT NOW()` |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

CREATE TABLE shipment_log (
    log_id SERIAL PRIMARY KEY,
    shipment_id INTEGER,
    old_status TEXT,
    new_status TEXT,
    logged_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'in_transit');
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagmvp" 
 width="100%"
></iframe>

Expected result: `CREATE FUNCTION` and `CREATE TRIGGER` return no rows; they arm the logging trigger on `shipments` without touching any data yet. The next section fires an `UPDATE` and shows the row it writes into `shipment_log`.

- `RETURNS TRIGGER` marks this as a special function meant to be called by a trigger, not directly by a `SELECT`.
- Inside it, `OLD` refers to the row's values before the change, and `NEW` refers to its values after, both automatically available inside a trigger function without being declared anywhere.
- `CREATE TRIGGER trg_log_status_change AFTER UPDATE ON shipments FOR EACH ROW` attaches this function so it runs automatically, once per changed row, immediately after any `UPDATE` on `shipments` completes.

## Watching the Trigger Fire Automatically

Once created, the trigger requires no cooperation from whoever writes the `UPDATE`; it fires regardless of how the update was issued.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagn74" 
 width="100%"
></iframe>

Expected output:

| log_id | shipment_id | old_status | new_status | logged_at |
| --- | --- | --- | --- | --- |
| 1 | 1 | in_transit | delivered | *(timestamp of the `UPDATE`)* |

A plain `UPDATE`, with no procedure, no special syntax, no cooperation from Devraj's colleague required, produced a log entry automatically, capturing both the old status, `in_transit`, and the new one, `delivered`. This is the core advantage a trigger has over the procedure from earlier in this chapter: the logging behavior is now a property of the table itself, impossible to accidentally skip.

![A trigger automatically creates a log entry when the table is updated](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_trigger_update_creates_log_automatically.png)

## BEFORE Triggers Can Validate or Modify a Row

An `AFTER` trigger, like the one above, runs once a change has already happened, suitable for logging. A `BEFORE` trigger runs before the change is applied, and can inspect, reject, or even alter the incoming row.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagngp" 
 width="100%"
></iframe>

Expected output:

| shipment_id | status |
| --- | --- |
| 2 | in_transit |

Shipment 2 is still shown at its original status because the invalid `UPDATE` above is commented out rather than actually run; had it run, `trg_validate_status` would have raised `Invalid status: lost_in_space` and left shipment 2 exactly this way anyway, since the rejected write never reaches the table. This `UPDATE` is rejected outright, with the trigger's own `RAISE EXCEPTION` message, before the invalid status ever reaches the table, since `BEFORE UPDATE` runs ahead of the actual write and can refuse it entirely by raising an error. This is a form of validation logic that goes beyond what a plain `CHECK` constraint can express, since it can reference custom error messages and arbitrary procedural logic, not just a fixed boolean condition.

## Triggers Can Make a Joined View Writable

The `INSTEAD OF` trigger mentioned when updatable views were covered earlier in this chapter is simply a third trigger timing, used specifically on views rather than tables, replacing the write entirely with custom logic instead of running before or after it.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagnt5" 
 width="100%"
></iframe>

Expected output:

| shipment_id | status |
| --- | --- |
| 1 | delayed |

The `UPDATE` against `shipment_status_view` never touches the view directly; `trg_instead_of_update` intercepts it and runs the underlying `UPDATE shipments SET status = 'delayed' WHERE shipment_id = 1` instead, so `shipments` itself now shows shipment 1 as `delayed`. Here `shipment_status_view` is a simple enough view to be updatable on its own, but the pattern generalizes directly to the join-based views that cannot be, letting an `INSTEAD OF` trigger define exactly how a write against a complex view should be translated into changes on the real underlying tables.

![Trigger timing options: BEFORE validates, AFTER audits, and INSTEAD OF redirects view writes](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_trigger_timing_before_after_instead_of.png)

## Triggers at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"><code>Trigger</code> timing</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Runs</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>BEFORE</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Before the change is applied</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Validation, rejecting or modifying the incoming row</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>AFTER</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">After the change has completed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logging, auditing, cascading updates to other tables</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>INSTEAD OF</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">In place of the change, on a <code>view</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Making a non-updatable <code>view</code> writable</td>
    </tr>
  </tbody>
</table>

## Your Turn

Create an `AFTER INSERT` trigger on `shipments` that logs new shipments into `shipment_log`, with `old_status` as `NULL` and `new_status` set to the newly inserted status, then insert a new shipment and confirm the log entry.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagp45" 
 width="100%"
></iframe>

Expected result and verification:

A correct trigger function inserts into `shipment_log` using `NEW.shipment_id` and `NEW.status`, with `old_status` left as `NULL`, attached via `CREATE TRIGGER ... AFTER `INSERT` ON shipments FOR EACH ROW EXECUTE FUNCTION ...`; inserting a new shipment afterward produces a matching log row automatically, with no explicit logging statement needed at the call site.

## Conclusion

A trigger runs automatically in response to an insert, update, or delete, with `BEFORE` triggers able to validate or reject a change before it happens, `AFTER` triggers able to react once a change has completed, and `INSTEAD OF` triggers able to make an otherwise non-writable view accept writes, all without requiring any cooperation from whoever issues the original statement.

Devraj's shipment status changes are now logged unconditionally, a guarantee no procedure alone could offer. With views, `materialized views`, procedures, functions, and triggers all covered, the next chapter turns to how an actual application connects to and uses a database like this one from real code.
