## Introduction

Marking a shipment delivered, in Devraj's system, is never just one `UPDATE`. It means changing the shipment's status, and also inserting a row into a separate audit log recording who marked it and when, two statements that always need to run together, the exact kind of grouped operation the transactions unit covered in depth. Rather than trusting every script and every developer to remember both statements and wrap them correctly, a **`stored procedure`** lets Devraj define this logic once, inside the database itself, as a named, callable unit.

## Creating a Simple Procedure

The `shipments` and `shipment_log` tables set up the two-statement operation a procedure will wrap.

```postgresql file=procedures_demo.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

CREATE TABLE shipment_log (
    log_id SERIAL PRIMARY KEY,
    shipment_id INTEGER,
    action TEXT,
    logged_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'in_transit');
```

```postgresql with=procedures_demo.sql
CREATE PROCEDURE mark_shipment_delivered(p_shipment_id INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE shipments SET status = 'delivered' WHERE shipment_id = p_shipment_id;
    INSERT INTO shipment_log (shipment_id, action) VALUES (p_shipment_id, 'marked delivered');
END;
$$;
```

`CREATE PROCEDURE mark_shipment_delivered(p_shipment_id INTEGER)` defines a named routine, written in `plpgsql`, PostgreSQL's own procedural extension of SQL:

- It accepts one parameter and runs both statements inside it every time it is called.
- The `$$ ... $$` markers, called dollar-quoting, wrap the procedure's body, letting it contain semicolons and even quoted strings of its own without confusing the outer `CREATE PROCEDURE` statement's own boundaries.

## Calling a Procedure

A procedure is invoked with `CALL`, not `SELECT`, since it performs actions rather than returning a result set the way a query does.

```postgresql with=procedures_demo.sql
CALL mark_shipment_delivered(1);

SELECT * FROM shipments;
SELECT * FROM shipment_log;
```

One call to `mark_shipment_delivered(1)` ran both the `UPDATE` and the `INSERT` from the procedure's body, and both tables now reflect that single logical operation, exactly the two-statements-together guarantee Devraj wanted, now enforced automatically by the procedure itself rather than relying on every caller to remember both steps.

## Procedures Can Manage Their Own Transactions

Unlike a plain SQL script, a procedure written in `plpgsql` is allowed to issue its own `COMMIT` or `ROLLBACK` partway through its body, useful for long-running procedures that need to save progress incrementally rather than treating the whole procedure as one giant, indivisible transaction.

```postgresql with=procedures_demo.sql
CREATE PROCEDURE mark_multiple_delivered(shipment_ids INTEGER[])
LANGUAGE plpgsql
AS $$
DECLARE
    sid INTEGER;
BEGIN
    FOREACH sid IN ARRAY shipment_ids
    LOOP
        UPDATE shipments SET status = 'delivered' WHERE shipment_id = sid;
        INSERT INTO shipment_log (shipment_id, action) VALUES (sid, 'marked delivered (batch)');
        COMMIT;
    END LOOP;
END;
$$;

CALL mark_multiple_delivered(ARRAY[2]);

SELECT * FROM shipments;
```

`FOREACH sid IN ARRAY shipment_ids LOOP ... END LOOP` is `plpgsql`'s looping construct, iterating over every value passed in, and the `COMMIT` inside the loop saves each shipment's update independently, rather than risking the entire batch being rolled back together if one shipment far down the list ran into a problem. This ability to commit mid-procedure is a capability plain SQL functions, covered in the next lesson, do not have.

## Why Wrap Logic in a Procedure at All

The alternative to a procedure is writing the same `UPDATE` and `INSERT` pair directly in application code, wrapped in a `BEGIN`/`COMMIT` transaction, exactly the pattern covered in the previous unit's lesson on transactions in application code. A procedure moves that logic into the database itself, which means every caller, whether a Python script, a reporting tool, or a different application entirely, gets the identical, correct behavior automatically, without needing to reimplement the same two-statement sequence and its transaction boundaries in every single client.

## Stored Procedures at a Glance

| Concept | Detail |
|---|---|
| `CREATE PROCEDURE` | Defines a named, callable routine, written in a procedural language like `plpgsql` |
| Invoked with | `CALL procedure_name(args)`, not `SELECT` |
| Can manage transactions | Yes, including its own `COMMIT` or `ROLLBACK` mid-procedure |
| Typical use | Multi-statement operations that must always run together, reused across many callers |

## Your Turn

Write a procedure named `cancel_shipment` that takes a `shipment_id`, sets its status to `'cancelled'`, and logs the action as `'cancelled'` in `shipment_log`, then call it for shipment 2.

```postgresql with=procedures_demo.sql
-- Write your procedure and call below
```

A correct procedure follows the same shape as `mark_shipment_delivered`, replacing the update value and the logged action text with `'cancelled'`; calling `CALL cancel_shipment(2);` afterward updates shipment 2's status and adds a matching log entry, confirmed by selecting from both tables.

## Conclusion

A `stored procedure`, invoked with `CALL`, wraps multiple statements into a single, named, reusable routine defined once inside the database, capable of managing its own transaction boundaries including mid-procedure commits, which guarantees every caller gets identical, correct behavior without reimplementing the same logic client by client. Devraj's shipment-delivery logic now lives in exactly one place, called consistently from anywhere. The next lesson covers a closely related but distinct kind of routine, one built specifically to compute and return a value for use inside a query.
