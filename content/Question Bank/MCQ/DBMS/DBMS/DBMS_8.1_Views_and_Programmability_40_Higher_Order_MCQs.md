# DBMS 8.1: Views and Programmability — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Going to Production
- **Chapter:** Views and Programmability
- **Scope:** Views: Naming and Reusing Queries; Updatable Views and Their Limitations; Materialized Views; Stored Procedures; User-Defined Functions; Triggers
- **SQL dialect:** PostgreSQL
- **Format:** Four plausible options with exactly one best answer
- **Is Curriculum Based:** No
- **Coverage rule:** Questions 1–10 collectively cover all six chapter subtopics.
- **Design standard:** Questions use supplied tables, SQL, state changes, missing code, and realistic production decisions.
- **Answer-quality controls:** A/B/C/D are each correct exactly 10 times; no answer letter occurs more than twice consecutively.

---

## Questions

### 1. One definition for every logistics dashboard

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Views: Naming and Reusing Queries  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a reusable structure

Five dashboards repeat the same join and the exact filter `status = 'in_transit'`. Small spelling differences have already caused inconsistent totals.

Which database object gives the query one reusable name while continuing to read current base-table data?

A. A materialized view refreshed once per month  
B. A stored procedure called separately by each dashboard  
C. An ordinary view containing the shared join and filter  
D. A trigger attached to every dashboard query

### 2. Updating through a simple view

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Updatable Views and Their Limitations  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a write-through view

```sql
CREATE VIEW in_transit_shipments AS
SELECT shipment_id, driver_id, destination
FROM shipments
WHERE status = 'in_transit';

UPDATE in_transit_shipments
SET destination = 'Thane'
WHERE shipment_id = 1;
```

Shipment 1 is in transit. What state should a later query of `shipments` show?

A. Shipment 1 has destination `Thane`, because the simple view maps to one base row.  
B. No change, because all views are read-only snapshots.  
C. A new shipment row with destination `Thane`.  
D. The view changes, but `shipments` retains the old destination.

### 3. June remains stale

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Materialized Views  
**Is Curriculum Based:** No  
**Assessment type:** Predicting stored-summary state

A materialized view currently contains:

| shipped_month | total_shipments | delayed_shipments |
|---|---:|---:|
| 2025-06-01 | 417 | 0 |

One delayed June shipment is inserted into the base table. No refresh follows. What does the next query of the materialized view return for June?

A. `418, 1`, because every view is automatically current.  
B. `417, 1`, because only the delayed count updates automatically.  
C. No row, because inserts invalidate materialized views.  
D. `417, 0`, because it still exposes the previously stored result.

### 4. Packaging an update and its audit entry

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Stored Procedures  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the appropriate routine

Marking a shipment delivered must update `shipments` and insert a row into `shipment_log`. Several applications must perform the same two-statement operation explicitly.

Which structure is the best match?

A. A scalar function used once per result row  
B. A stored procedure invoked with `CALL`  
C. An ordinary view over the two tables  
D. A materialized summary refreshed afterward

### 5. A calculation used inside every report row

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** User-Defined Functions  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a callable structure

Each shipment report must calculate `distance × 8.5`, plus 500 when the package is oversized. The result must appear as a computed column in `SELECT`.

Which implementation fits that use?

A. A `BEFORE UPDATE` trigger on shipments  
B. A procedure that commits after every row  
C. A function returning a numeric value from distance and oversized inputs  
D. A materialized view with no parameters

### 6. Logging even when callers bypass the procedure

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Triggers  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an automatic mechanism

The audit rule must run after every shipment status update—including direct SQL issued by future tools that do not call the approved procedure.

Which design provides that guarantee?

A. Attach an `AFTER UPDATE` trigger to `shipments`.  
B. Ask every tool to query an audit view after updating.  
C. Put the logging statement in one application's source code.  
D. Refresh an audit materialized view each night.

### 7. The named query sees a base-table change

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Views: Naming and Reusing Queries  
**Is Curriculum Based:** No  
**Assessment type:** Tracing current view results

`active_shipments` filters `status='in_transit'`. It initially contains shipment IDs 1 and 3. The base table is then updated:

```sql
UPDATE shipments SET status='delivered' WHERE shipment_id=1;
SELECT shipment_id FROM active_shipments ORDER BY shipment_id;
```

Which result follows?

A. `1, 3`, until the view is refreshed  
B. `1` only, because the update reverses the filter  
C. `3` only, because the ordinary view reruns against current data  
D. No rows, because an update invalidates the view

### 8. A count cannot identify one row to edit

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Updatable Views and Their Limitations  
**Is Curriculum Based:** No  
**Assessment type:** Explaining a rejected update

```sql
CREATE VIEW driver_shipment_counts AS
SELECT driver_id, COUNT(*) AS shipment_count
FROM shipments
GROUP BY driver_id;
```

Why can PostgreSQL not directly perform `UPDATE driver_shipment_counts SET shipment_count=5 WHERE driver_id=1`?

A. `COUNT` accepts no integer replacement value.  
B. One count represents several base rows, so no single stored value maps to the requested assignment.  
C. A view may expose only text columns when it is updated.  
D. `GROUP BY` views become writable after their first query.

### 9. Keeping the dashboard readable during refresh

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Materialized Views  
**Is Curriculum Based:** No  
**Assessment type:** Completing a production-safe refresh

A dashboard must remain readable while `monthly_shipment_summary` is refreshed. A unique index already exists on `shipped_month`.

Complete the command:

```sql
REFRESH MATERIALIZED VIEW ______ monthly_shipment_summary;
```

A. `NOWAIT`  
B. `ASYNC`  
C. `DEFERRED`  
D. `CONCURRENTLY`

### 10. Calling the action, not selecting it

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Stored Procedures  
**Is Curriculum Based:** No  
**Assessment type:** Completing invocation syntax

The database contains `mark_shipment_delivered(p_shipment_id INTEGER)` as a procedure. Which statement performs the operation for shipment 2?

A. `CALL mark_shipment_delivered(2);`  
B. `SELECT FROM mark_shipment_delivered(2);`  
C. `RUN PROCEDURE mark_shipment_delivered = 2;`  
D. `EXEC FUNCTION mark_shipment_delivered(2);`

### 11. Completing a reusable view

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Views: Naming and Reusing Queries  
**Is Curriculum Based:** No  
**Assessment type:** Filling missing SQL

Complete the definition that saves the query under `delayed_shipments`.

```sql
_____ delayed_shipments AS
SELECT shipment_id, destination
FROM shipments
WHERE status='delayed';
```

A. `SAVE QUERY`  
B. `CREATE VIEW`  
C. `CREATE FUNCTION`  
D. `MATERIALIZE TABLE`

### 12. Changing the shared definition

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Views: Naming and Reusing Queries  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest definition repair

`active_shipments` must now include both `in_transit` and `delayed` rows and expose a new `status` column. Existing reports should keep using the same object name.

Which operation directly meets that requirement?

A. Drop every report that queries the view.  
B. Update rows stored inside `active_shipments`.  
C. Rename the base table to `active_shipments`.  
D. Use `CREATE OR REPLACE VIEW active_shipments AS ...`.

### 13. Dropping the window, not the data behind it

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Views: Naming and Reusing Queries  
**Is Curriculum Based:** No  
**Assessment type:** Predicting object state

After `DROP VIEW active_shipments;`, which object is removed?

A. The saved view definition; the `shipments` and `drivers` rows remain.  
B. Every base row previously visible through the view.  
C. The base tables and all dependent data.  
D. Only the view's most recently displayed result rows.

### 14. Refresh changes the stored June summary

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Materialized Views  
**Is Curriculum Based:** No  
**Assessment type:** Tracing refresh behaviour

Starting materialized row: June has 417 shipments, 0 delayed. A delayed June row is inserted, then this runs:

```sql
REFRESH MATERIALIZED VIEW monthly_shipment_summary;
```

What should June show afterward?

A. 417 total and 0 delayed  
B. 418 total and 1 delayed  
C. 417 total and 1 delayed  
D. 418 total and 0 delayed

### 15. Choosing freshness or stored speed

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Materialized Views  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two implementations

Report P must reflect a status update immediately. Report Q performs a costly historical aggregate, may be up to one hour old, and is opened hundreds of times per hour.

Which pairing best matches the requirements?

A. Materialized views for both reports  
B. Ordinary views for both reports  
C. P: ordinary view; Q: hourly refreshed materialized view  
D. P: trigger; Q: stored procedure

### 16. A missing prerequisite for concurrent refresh

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Materialized Views  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest repair

This command is rejected because the materialized view has no qualifying unique index:

```sql
REFRESH MATERIALIZED VIEW CONCURRENTLY monthly_shipment_summary;
```

Which repair matches the lesson?

A. Add an ordinary non-unique index on `status`.  
B. Convert the object into a stored procedure.  
C. Place the refresh inside a user-defined function.  
D. Create a unique index that uniquely identifies materialized-view rows, then retry.

### 17. One call, two table changes

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Stored Procedures  
**Is Curriculum Based:** No  
**Assessment type:** Tracing procedure effects

`mark_shipment_delivered(1)` updates shipment 1 and inserts a log action. Before the call:

| Table | Relevant state |
|---|---|
| `shipments` | `(1, 'in_transit')` |
| `shipment_log` | empty |

After `CALL mark_shipment_delivered(1)`, which state is expected?

A. Shipment 1 is `delivered`, and one matching log row exists.  
B. Shipment 1 changes, but procedures cannot insert into another table.  
C. The log row exists, but the shipment remains in transit.  
D. Neither change occurs until the procedure is selected from.

### 18. Dollar quotes protect the procedure body

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Stored Procedures  
**Is Curriculum Based:** No  
**Assessment type:** Interpreting routine syntax

Why is a PL/pgSQL body commonly enclosed by `$$ ... $$`?

A. It converts every expression inside the body to currency.  
B. It delimits a body containing semicolons and quoted strings from the outer statement.  
C. It commits each enclosed statement independently.  
D. It marks the routine as a set-returning function.

### 19. Tracing a scalar function

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** User-Defined Functions  
**Is Curriculum Based:** No  
**Assessment type:** Calculating a returned value

The function computes `distance * 8.5` and adds 500 when `oversized` is true.

What value does `SELECT calculate_shipping_cost(200.00, TRUE);` return?

A. 1,700  
B. 2,000  
C. 2,200  
D. 8,700

### 20. The transaction command that does not belong

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** User-Defined Functions  
**Is Curriculum Based:** No  
**Assessment type:** Spotting an invalid routine design

A developer places `COMMIT;` inside a function called from a `SELECT`.

Why is that design invalid?

A. Functions may return text but not numeric values.  
B. A function must be called using `CALL`, not `SELECT`.  
C. Functions may contain only one expression.  
D. A function runs within its caller's transaction and cannot manage its own commit.

### 21. Returning rows rather than one scalar

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** User-Defined Functions  
**Is Curriculum Based:** No  
**Assessment type:** Completing a set-returning function call

`oversized_shipments()` is declared with `RETURNS TABLE (shipment_id INTEGER, distance_km NUMERIC)`.

Which call consumes its returned rows?

A. `SELECT * FROM oversized_shipments();`  
B. `CALL oversized_shipments INTO shipments;`  
C. `REFRESH FUNCTION oversized_shipments();`  
D. `UPDATE oversized_shipments() SET ...;`

### 22. The two pieces of a PostgreSQL trigger

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Triggers  
**Is Curriculum Based:** No  
**Assessment type:** Completing an implementation

A developer has written a special function `log_status_change()` that `RETURNS TRIGGER`, but updates still create no log rows.

What missing step arms the behaviour?

A. Call the function after every update from application code.  
B. Create a trigger on the required table/event that executes the function.  
C. Convert `shipment_log` into a materialized view.  
D. Select the function once when the server starts.

### 23. OLD and NEW tell the audit story

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Triggers  
**Is Curriculum Based:** No  
**Assessment type:** Tracing trigger values

Shipment 1 changes from `in_transit` to `delivered`. An `AFTER UPDATE` row trigger inserts `OLD.status` and `NEW.status` into the log.

Which audit pair is inserted?

A. `(delivered, delivered)`  
B. `(in_transit, in_transit)`  
C. `(in_transit, delivered)`  
D. `(NULL, delivered)`

### 24. Rejecting an invalid status before storage

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Triggers  
**Is Curriculum Based:** No  
**Assessment type:** Selecting trigger timing

An incoming row must be rejected with a custom exception when status is not in the approved list, before the invalid value reaches `shipments`.

Which trigger timing fits?

A. `AFTER SELECT`  
B. `AFTER UPDATE`  
C. `INSTEAD OF SELECT`  
D. `BEFORE INSERT OR UPDATE`

### 25. Making a joined view writable deliberately

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Updatable Views and Their Limitations  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a controlled repair

A joined view exposes shipment and driver details. Direct updates are ambiguous, but the team has a precise rule for translating a destination change to `shipments`.

Which mechanism can encode that translation?

A. An `AFTER SELECT` trigger on the base table  
B. An `INSTEAD OF UPDATE` trigger on the view  
C. A refresh of the ordinary view after each write  
D. A unique index on the view's displayed columns

### 26. A row trigger fires once per changed row

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Triggers  
**Is Curriculum Based:** No  
**Assessment type:** Identifying a final row count

`trg_log_status_change` is `AFTER UPDATE ... FOR EACH ROW`. The log is empty. This statement changes three rows:

```sql
UPDATE shipments SET status='delivered'
WHERE shipment_id IN (1,2,3);
```

Assuming the trigger inserts one log row each time it fires, how many log rows result?

A. 0  
B. 1  
C. 3  
D. 6

### 27. A procedure is not an unconditional audit guarantee

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Triggers  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two implementations

Version P logs only inside `CALL update_status(...)`. Version T logs with an `AFTER UPDATE` trigger on `shipments`.

A maintenance script issues a direct `UPDATE`. Which comparison is correct?

A. Only P logs because procedures intercept all table writes.  
B. Both log because PostgreSQL redirects updates through procedures.  
C. Neither logs unless the script calls both routines.  
D. T logs automatically; P can be bypassed when callers update directly.

### 28. Two versions with different freshness

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Materialized Views  
**Is Curriculum Based:** No  
**Assessment type:** Deciding whether versions are equivalent

Version V is an ordinary view; Version M is a materialized view built from the same aggregation. A base row is inserted after both objects are created and before M is refreshed.

Are `SELECT` results guaranteed to be equivalent at that moment?

A. No. V reads current base data, while M can still show its stored pre-insert result.  
B. Yes. Sharing the same definition guarantees identical freshness.  
C. Yes, unless the inserted row contains `NULL`.  
D. No, because ordinary views cannot contain aggregation.

### 29. Reusing a query and extending it

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Views: Naming and Reusing Queries  
**Is Curriculum Based:** No  
**Assessment type:** Applying a view as a building block

`active_shipments` already contains current in-transit shipments and driver names. A new report needs a count per driver without repeating the underlying join or status rule.

Which query uses the view as intended?

A. `CALL active_shipments();`  
B. `SELECT driver_name, COUNT(*) FROM active_shipments GROUP BY driver_name;`  
C. `REFRESH MATERIALIZED VIEW active_shipments;`  
D. `CREATE TRIGGER ON active_shipments COUNT ROWS;`

### 30. Function or procedure?

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** User-Defined Functions  
**Is Curriculum Based:** No  
**Assessment type:** Matching structures to requirements

Task X computes one discounted amount inside a query. Task Y performs an update and audit insert as one named action and may control transaction boundaries.

Which pairing is most appropriate?

A. X: view; Y: trigger function only  
B. X: procedure; Y: scalar function  
C. X: materialized view; Y: ordinary view  
D. X: function; Y: procedure

### 31. When stored results justify staleness

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Materialized Views  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the appropriate programming structure

Which workload is the strongest candidate for a materialized view?

A. A costly monthly aggregate read frequently, with an accepted hourly refresh delay  
B. A current shipment status that must reflect every update immediately  
C. A parameterized calculation used with different inputs per row  
D. Validation that must reject an invalid status before insertion

### 32. Updating only rows visible through a view

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Updatable Views and Their Limitations  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a filtered update

The base table contains:

| shipment_id | status | destination |
|---|---|---|
| 1 | in_transit | Mumbai |
| 2 | delivered | Pune |

`in_transit_shipments` is a simple view filtered to `status='in_transit'`. What does this statement change?

```sql
UPDATE in_transit_shipments
SET destination='Thane'
WHERE shipment_id IN (1,2);
```

A. Both base rows, because the `WHERE` mentions both IDs  
B. Only shipment 2, because it is already delivered  
C. No rows, because a filtered view cannot be updated  
D. Only shipment 1, because shipment 2 is not a row of the view

### 33. The smallest repair for a joined-view update

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Updatable Views and Their Limitations  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest correct repair

An update fails only because `shipments_with_driver` joins `shipments` and `drivers`. The desired change is clearly just `shipments.destination`.

What is the smallest repair when no reusable view-write interface is required?

A. Replace both base tables with a materialized view.  
B. Update `shipments` directly using the shipment ID.  
C. Add `GROUP BY` to make the view's rows unique.  
D. Refresh the joined view before retrying the update.

### 34. Commits inside a batch procedure

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Stored Procedures  
**Is Curriculum Based:** No  
**Assessment type:** Analysing transaction boundaries

A procedure loops through shipment IDs and executes `COMMIT` after each successful update and log insert. Shipment 1 commits, then processing shipment 2 later fails.

Which consequence follows from the design taught in the chapter?

A. Shipment 1 is automatically undone with shipment 2.  
B. Both shipments commit because the procedure started them together.  
C. Shipment 1's committed work can remain even though later work fails.  
D. The procedure syntax is invalid because procedures cannot commit.

### 35. Returning the accepted row from a BEFORE trigger

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Triggers  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing trigger code

A `BEFORE INSERT OR UPDATE` trigger validates `NEW.status`. When the row is valid, which missing statement allows that row to proceed?

```sql
BEGIN
  IF NEW.status NOT IN ('in_transit','delivered','delayed','cancelled') THEN
    RAISE EXCEPTION 'Invalid status';
  END IF;
  _____
END;
```

A. `COMMIT;`  
B. `CALL NEW;`  
C. `REFRESH NEW;`  
D. `RETURN NEW;`

### 36. Attaching the function to the correct event

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Triggers  
**Is Curriculum Based:** No  
**Assessment type:** Completing missing trigger SQL

`log_new_shipment()` inserts `NEW.shipment_id`, `NULL`, and `NEW.status` into `shipment_log`. Complete the attachment so it runs after each inserted shipment.

A. `CREATE TRIGGER t AFTER INSERT ON shipments FOR EACH ROW EXECUTE FUNCTION log_new_shipment();`  
B. `CREATE VIEW t AFTER INSERT AS log_new_shipment();`  
C. `CALL log_new_shipment() AFTER shipments;`  
D. `CREATE TRIGGER t BEFORE SELECT ON shipment_log EXECUTE PROCEDURE shipments;`

### 37. A set-returning function with one oversized row

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** User-Defined Functions  
**Is Curriculum Based:** No  
**Assessment type:** Predicting returned rows

`oversized_shipments()` returns `(shipment_id, distance_km)` where `is_oversized=TRUE`.

| shipment_id | distance_km | is_oversized |
|---|---:|---|
| 1 | 120 | FALSE |
| 2 | 450 | TRUE |
| 3 | 30 | FALSE |

What does `SELECT * FROM oversized_shipments();` return?

A. All three rows, because functions ignore filters  
B. Only `(2, 450)`  
C. Only the two non-oversized rows  
D. One scalar containing the number 1

### 38. Refresh timeline

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Materialized Views  
**Is Curriculum Based:** No  
**Assessment type:** Tracing multiple state changes

A materialized count starts at 100. Two base rows are inserted; it is refreshed; then three more base rows are inserted without another refresh.

What count does the materialized view show at the end?

A. 100  
B. 105  
C. 102  
D. 103

### 39. Repairing a function declaration

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** User-Defined Functions  
**Is Curriculum Based:** No  
**Assessment type:** Completing a missing declaration

A routine must return one numeric discounted amount. Which header correctly fills the missing portion?

```sql
CREATE FUNCTION apply_discount(amount NUMERIC, pct NUMERIC)
_____
LANGUAGE plpgsql
AS $$ ... $$;
```

A. `CALLS NUMERIC`  
B. `OUTPUT TABLE`  
C. `RETURNS NUMERIC`  
D. `PROCEDURE NUMERIC`

### 40. Combining validation and audit behaviour

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Triggers  
**Is Curriculum Based:** No  
**Assessment type:** Applying multiple mechanisms

Requirements for `shipments`:

1. Reject an unapproved status before it is stored.
2. After an accepted status update, record `OLD.status` and `NEW.status`.
3. Apply both rules even to direct updates.

Which design satisfies all three?

A. A `BEFORE INSERT OR UPDATE` validation trigger and an `AFTER UPDATE` audit trigger  
B. One procedure that every current application promises to call  
C. A scalar function in reports plus an index on `status`  
D. One ordinary view and one nightly materialized-view refresh

---

## Instructor Key

### 1. C
An ordinary view names the shared query and reruns it against current base data whenever queried.

### 2. A
This single-table, non-aggregate view maps shipment 1 directly to its base row, so the destination update passes through.

### 3. D
A materialized view stores its earlier result. Base-table inserts do not appear until an explicit refresh.

### 4. B
A procedure is a named multi-statement action invoked with `CALL`, suitable for an update plus its log insert.

### 5. C
A scalar function accepts row values and returns a numeric result usable as a computed `SELECT` column.

### 6. A
A table trigger fires for the specified event regardless of which application or SQL path issued the update.

### 7. C
An ordinary view stores no rows; reevaluating its filter after the update leaves only shipment 3.

### 8. B
The count is computed from multiple rows rather than stored in one row, so assigning a replacement count has no unambiguous base update.

### 9. D
`CONCURRENTLY` keeps the existing materialized result readable during recomputation and requires the appropriate unique index.

### 10. A
PostgreSQL procedures are invoked with `CALL procedure_name(arguments)`.

### 11. B
`CREATE VIEW name AS query` saves the supplied `SELECT` under the chosen view name.

### 12. D
`CREATE OR REPLACE VIEW` changes the shared definition while retaining the object name used by downstream reports.

### 13. A
Dropping an ordinary view removes its saved definition, not the rows owned by its underlying tables.

### 14. B
Refresh recomputes the stored aggregate after the insert, increasing both June's total and delayed counts by one.

### 15. C
The ordinary view gives P immediate freshness; the scheduled materialized view lets Q trade one hour of freshness for cheaper repeated reads.

### 16. D
Concurrent refresh requires a suitable unique index on the materialized view so PostgreSQL can identify its rows.

### 17. A
The procedure body performs both statements, leaving the shipment delivered and one corresponding audit entry.

### 18. B
Dollar quoting safely encloses a procedural body that contains its own semicolons and string quotes.

### 19. C
`200 × 8.5 = 1700`; adding the oversized surcharge of 500 produces 2200.

### 20. D
A function participates in the transaction of its calling statement and cannot issue its own `COMMIT` or `ROLLBACK`.

### 21. A
A `RETURNS TABLE` function can appear in `FROM`, so `SELECT * FROM oversized_shipments()` consumes its rows.

### 22. B
The trigger function defines the action; a separate `CREATE TRIGGER` binds it to a table, event, timing, and firing level.

### 23. C
`OLD` captures the pre-update value `in_transit`, while `NEW` captures the accepted replacement `delivered`.

### 24. D
A `BEFORE` trigger can inspect the proposed row and raise an exception before either an insert or update is applied.

### 25. B
An `INSTEAD OF` trigger replaces a view update with explicit logic that targets the intended base table.

### 26. C
`FOR EACH ROW` fires once for each of the three rows changed by the statement, producing three log rows.

### 27. D
The table trigger observes the direct update automatically; procedure-based logging works only when callers use that procedure.

### 28. A
The ordinary view immediately includes current base data, while the materialized view remains at its last stored refresh state.

### 29. B
Views can be queried and further aggregated like tables, letting this report reuse the existing join and active-status rule.

### 30. D
A function supplies a value inside a query; a procedure performs the reusable multi-step, transaction-aware action.

### 31. A
Frequent reads, expensive recomputation, and an accepted refresh delay are the central materialized-view trade-off.

### 32. D
Only shipment 1 is visible through the filtered view, so only that base row participates in the update.

### 33. B
When only one direct change is needed, updating the unambiguous base-table row is smaller than adding custom view-write machinery.

### 34. C
Each explicit commit saves that iteration. A failure in a later iteration does not undo work already committed.

### 35. D
Returning `NEW` from the valid path allows the proposed row, including any permitted modifications, to continue to the write.

### 36. A
The statement binds the trigger function to `AFTER INSERT` on `shipments` and fires it once for each inserted row.

### 37. B
Only shipment 2 satisfies `is_oversized=TRUE`, so the set-returning function emits its ID and distance.

### 38. C
The refresh incorporates the first two inserts, storing 102. The final three remain invisible until the next refresh.

### 39. C
`RETURNS NUMERIC` declares the single value produced by the function.

### 40. A
The `BEFORE` trigger rejects invalid incoming states, while the `AFTER` trigger records accepted changes; both attach to the table itself.

---

## Coverage summary

| Subtopic | Questions |
|---|---|
| Views: Naming and Reusing Queries | 1, 7, 11, 12, 13, 29 |
| Updatable Views and Their Limitations | 2, 8, 25, 32, 33 |
| Materialized Views | 3, 9, 14, 15, 16, 28, 31, 38 |
| Stored Procedures | 4, 10, 17, 18, 34 |
| User-Defined Functions | 5, 19, 20, 21, 30, 37, 39 |
| Triggers | 6, 22, 23, 24, 26, 27, 35, 36, 40 |
