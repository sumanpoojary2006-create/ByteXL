import random
import openpyxl

random.seed(181)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

VIEWS_NAMING_A_QUERY = [
    (
        "Devraj's team keeps copy-pasting the same join between shipments and drivers, filtered for in-transit status, into every dashboard, and one analyst types the filter as 'In Transit' instead of 'in_transit', causing two reports to disagree.\n\nHow does creating a view solve this specific problem?",
        "A view gives the query a permanent, saved name in the database itself, so everyone references that one saved definition instead of retyping the join and filter, eliminating the risk of small inconsistencies between copies.",
        "easy", "understand", "views-naming-a-query-and-reusing-it",
        "A view saves the query under a permanent name in the database, so everyone references the same definition instead of retyping it with room for inconsistency",
        ["A view automatically fixes any typos in every report that queries the underlying tables", "A view physically merges the shipments and drivers tables into one combined table", "A view only helps if every analyst manually copies the view's SQL text into their own scripts"],
    ),
    (
        "After `CREATE VIEW active_shipments AS SELECT ... WHERE s.status = 'in_transit'`, the lesson says `SELECT * FROM active_shipments` runs \"exactly as if active_shipments were a real table, even though it is really just this saved query, re-executed fresh every time it is referenced.\"\n\nWhat does \"re-executed fresh every time\" mean for how a view behaves?",
        "A view is not a stored snapshot; it has no storage of its own, and the underlying query actually runs again each time the view is selected from, meaning it always reflects whatever the underlying tables currently contain.",
        "easy", "understand", "views-naming-a-query-and-reusing-it",
        "The view has no storage of its own and reruns its underlying query every time it's selected from, so it always reflects the underlying tables' current data",
        ["The view caches its result the first time it's queried and reuses that same cached result forever after", "The view re-executes only once per day, on a fixed schedule, regardless of how many times it's queried", "The view stores a permanent snapshot that must be manually deleted and recreated to update"],
    ),
    (
        "After Manoj's Mumbai shipment (shipment_id 1) is marked delivered with a plain UPDATE against the shipments table, querying active_shipments again immediately shows only the one remaining in-transit shipment, even though nothing about the view itself was touched.\n\nWhy does the view's result change without the view being redefined?",
        "Since a view has no storage of its own and reruns its underlying query fresh on every SELECT, any change to the underlying shipments table is automatically reflected the next time the view is queried, with no need to touch the view's own definition.",
        "medium", "apply", "views-naming-a-query-and-reusing-it",
        "The view reruns its underlying query fresh on every SELECT, so changes to the underlying table are automatically reflected without redefining the view itself",
        ["The database automatically detects the UPDATE and silently redefines the view to match", "The view's result only changes because CREATE OR REPLACE VIEW was implicitly triggered by the UPDATE", "This behavior is a bug; views are supposed to only reflect data from when they were created"],
    ),
    (
        "`SELECT driver_name, COUNT(*) AS active_shipment_count FROM active_shipments GROUP BY driver_name;` groups directly on top of the active_shipments view, without repeating the underlying join or filter condition.\n\nWhat does this demonstrate about how a view can be used inside other queries?",
        "Because a view behaves like a table for SELECT purposes, it can be filtered, joined, or aggregated further just like any real table, letting a saved view serve as a clean, reusable building block that other queries build on top of, rather than needing to repeat its logic.",
        "medium", "understand", "views-naming-a-query-and-reusing-it",
        "A view behaves like a table for SELECT purposes and can be further filtered, joined, or aggregated, letting other queries build cleanly on top of it without repeating its logic",
        ["Views can only ever be queried with a plain SELECT * and cannot be aggregated or filtered further", "GROUP BY only works on views if the view itself already contains a GROUP BY clause", "This query fails, since views cannot be referenced inside another query's FROM clause"],
    ),
    (
        "Devraj's colleague redefines active_shipments with `CREATE OR REPLACE VIEW active_shipments AS ... WHERE s.status IN ('in_transit', 'delayed')`, changing what every downstream query built on top of it sees, immediately and consistently.\n\nWhat problem does CREATE OR REPLACE VIEW solve here that copy-pasted queries could not?",
        "It updates the saved definition in exactly one place, so every downstream query automatically sees the new logic immediately, without anyone needing to hunt down and manually update every copy-pasted version of the original query scattered across scripts and dashboards.",
        "medium", "understand", "views-naming-a-query-and-reusing-it",
        "It updates the view's definition in one place, so every downstream query sees the change immediately, without anyone needing to hunt down and update scattered copy-pasted versions",
        ["CREATE OR REPLACE VIEW only affects new queries written after the change, not any existing dashboards", "It requires manually re-running every downstream report's code to pick up the new definition", "CREATE OR REPLACE VIEW silently fails if any downstream query currently depends on the view"],
    ),
    (
        "According to the \"Views at a Glance\" table, what happens to the underlying tables when a view is removed with DROP VIEW?",
        "DROP VIEW removes only the saved query definition; the underlying tables and their data are completely untouched, since a view never owns any data of its own in the first place.",
        "medium", "remember", "views-naming-a-query-and-reusing-it",
        "The underlying tables are untouched; DROP VIEW only removes the saved query definition, since a view owns no data of its own",
        ["DROP VIEW also deletes every row in the underlying tables that the view's query referenced", "DROP VIEW is not allowed unless the underlying tables are dropped first", "DROP VIEW converts the underlying tables into a single merged table permanently"],
    ),
]

UPDATABLE_VIEWS = [
    (
        "Running `UPDATE in_transit_shipments SET destination = 'Thane' WHERE shipment_id = 1;` against a view built from a single table with a straightforward SELECT and no aggregation genuinely changes the underlying shipments row.\n\nWhat two conditions does the lesson give for why PostgreSQL can translate this write successfully?",
        "The view maps unambiguously back to exactly one row in exactly one table, and there is no doubt about which row in the underlying table the update was meant for, together making the write's target completely unambiguous.",
        "easy", "understand", "updatable-views-and-their-limitations",
        "The view maps unambiguously to exactly one row in exactly one table, and there is no doubt about which underlying row the update targets",
        ["The view was created using CREATE OR REPLACE VIEW instead of plain CREATE VIEW", "The view includes an ORDER BY clause, which is required for any view to be updatable", "The underlying table has no primary key, which simplifies the update translation"],
    ),
    (
        "`shipments_with_driver`, built by joining shipments to drivers, rejects `UPDATE shipments_with_driver SET destination = 'Thane' WHERE shipment_id = 1;` outright.\n\nWhy does a join specifically break direct updatability, according to the lesson?",
        "A single row in the joined view's result could conceptually correspond to changes in either underlying table, and the database has no reliable way to know which one was intended, so it refuses to guess rather than risk writing to the wrong place.",
        "medium", "understand", "updatable-views-and-their-limitations",
        "A row in a joined view could conceptually map to either underlying table, and the database has no reliable way to know which one a write was meant for, so it refuses to guess",
        ["Joins are technically forbidden inside any CREATE VIEW statement, so this view would fail to even be created", "The join fails because drivers and shipments do not share a foreign key relationship", "PostgreSQL simply has not implemented join support for views yet, unlike other database systems"],
    ),
    (
        "`driver_shipment_counts`, built with `GROUP BY driver_id` and `COUNT(*) AS shipment_count`, rejects `UPDATE driver_shipment_counts SET shipment_count = 5 WHERE driver_id = 1;`.\n\nThe lesson says this fails \"for a more fundamental reason than the join case.\" What is that reason?",
        "shipment_count is not a stored value at all; it is calculated fresh from however many rows currently match the GROUP BY, so \"setting\" it to a fixed number is not a meaningful operation the database could even attempt to translate into a real underlying change.",
        "medium", "analyze", "updatable-views-and-their-limitations",
        "shipment_count is a computed value, not a stored one, recalculated fresh from matching rows, so setting it to a fixed number isn't a meaningful operation the database could translate into a real change",
        ["The reason is identical to the join case; both fail purely because of ambiguity about which table to target", "GROUP BY views fail only because COUNT(*) is not a supported aggregate function in updatable contexts", "The update fails simply because driver_id 1 does not exist in the underlying shipments table"],
    ),
    (
        "For genuinely complex cases where writable access to a joined or computed view is worth the effort, the lesson mentions INSTEAD OF triggers as an escape hatch.\n\nHow does the lesson characterize this mechanism, compared to PostgreSQL automatically inferring updatability for a simple view?",
        "It's described as a deliberate, hand-written escape hatch, custom logic telling the database exactly how to translate a write against the view into specific changes on the correct underlying tables, rather than something PostgreSQL infers automatically the way it does for a simple single-table view.",
        "medium", "understand", "updatable-views-and-their-limitations",
        "It's a deliberate, hand-written mechanism where custom logic tells the database how to translate a view write into underlying table changes, unlike the automatic inference for simple views",
        ["INSTEAD OF triggers work automatically and require no custom logic to be written at all", "INSTEAD OF triggers only apply to single-table views, the same category that's already automatically updatable", "INSTEAD OF triggers are a deprecated feature no longer recommended for production use"],
    ),
    (
        "According to the \"Updatable Views at a Glance\" table, is a view built from a join across multiple tables updatable directly, and why?",
        "No, it is not updatable directly, because it's ambiguous which table a write actually targets, since a row in the joined result could correspond to either underlying table.",
        "medium", "remember", "updatable-views-and-their-limitations",
        "No — a join across multiple tables makes it ambiguous which underlying table a write should target",
        ["Yes, automatically, since joins between two tables are always unambiguous by definition", "Yes, but only if the join uses an INNER JOIN rather than a LEFT JOIN", "No, because joins are not allowed inside a view's SELECT statement at all"],
    ),
    (
        "The \"Your Turn\" exercise creates `delivered_shipments` as a simple, single-table view filtering for status = 'delivered', then runs `UPDATE delivered_shipments SET destination = 'Kothrud' WHERE shipment_id = 2;` followed by a SELECT against the underlying shipments table.\n\nWhy does this update succeed where the earlier join-based and aggregate-based examples failed?",
        "delivered_shipments is built from a single table with a straightforward filter and no aggregation, so each row maps unambiguously back to exactly one row in shipments, meeting exactly the criteria the lesson identifies for automatic updatability.",
        "medium", "apply", "updatable-views-and-their-limitations",
        "It's a single-table view with no aggregation, so each row maps unambiguously to exactly one underlying row, meeting the criteria for automatic updatability",
        ["It succeeds only because the WHERE clause happens to filter for the word 'delivered' specifically", "It succeeds because shipment_id 2 has no matching row, so the update has nothing to actually change", "It succeeds because the view was created with the CONCURRENTLY keyword, unlike the earlier examples"],
    ),
]

MATERIALIZED_VIEWS = [
    (
        "An ordinary view built on a genuinely expensive aggregate, summarizing millions of historical shipments, re-runs that full computation every single time anyone queries it, even if the underlying data hasn't changed in hours.\n\nWhat does a materialized view do differently to solve this specific cost problem?",
        "A materialized view actually stores the query's result physically on disk, like a real table, and only recomputes it when explicitly refreshed, trading perfect freshness for dramatically faster reads.",
        "easy", "understand", "materialized-views",
        "It physically stores the query's result on disk and only recomputes when explicitly refreshed, trading perfect freshness for much faster reads",
        ["It automatically indexes the underlying table so the same aggregate query runs faster every time", "It runs the aggregate query in parallel across multiple servers instead of just one", "It compresses the underlying table's data so the aggregate computation needs less memory"],
    ),
    (
        "After creating `monthly_shipment_summary` and inserting a new delayed shipment for June, querying the materialized view for June still shows the old totals, not the new shipment.\n\nWhy does the lesson insist this staleness \"is not a bug\"?",
        "Staleness is the entire point of a materialized view: avoiding the cost of recomputing the aggregate on every single read is exactly the trade being made, in exchange for accepting that reads may be out of date until an explicit refresh runs.",
        "medium", "analyze", "materialized-views",
        "Staleness is the intentional trade-off: avoiding recomputation cost on every read, in exchange for accepting the result may be out of date until explicitly refreshed",
        ["It's not a bug because materialized views are actually incapable of ever storing new data at all", "It's not a bug because the insert itself silently failed due to the existing materialized view", "It's not a bug because materialized views automatically refresh themselves every few seconds in the background"],
    ),
    (
        "Running `REFRESH MATERIALIZED VIEW monthly_shipment_summary;` after the new June shipment was inserted makes June's row correctly reflect the new delayed shipment.\n\nWhat does the lesson say about when this refresh typically runs in a real production system?",
        "In a real production system, the refresh is typically scheduled, run every hour, every night, or after a known batch of data loads, rather than run manually, a deliberate design decision about how stale the summary is allowed to get before it matters.",
        "medium", "understand", "materialized-views",
        "It's typically scheduled (hourly, nightly, or after known batch loads) rather than run manually, a deliberate decision about how stale the data is allowed to get",
        ["It must always be run manually by a database administrator immediately after every single insert", "PostgreSQL automatically schedules the refresh the moment the materialized view is first created", "The refresh only ever runs once, at creation time, and can never be run again afterward"],
    ),
    (
        "A plain `REFRESH MATERIALIZED VIEW` locks the view against reads while it recomputes, which can be a problem for a dashboard that needs to stay available. `REFRESH MATERIALIZED VIEW CONCURRENTLY` avoids this, but requires a unique index on the materialized view first.\n\nWhat trade-off does the concurrent refresh make in exchange for keeping the view readable throughout?",
        "It recomputes the result in the background while the existing stored data remains fully readable, only swapping over once the new computation completes, at the cost of taking somewhat longer overall than a plain refresh, since it has to do extra work to keep the old version available throughout.",
        "medium", "apply", "materialized-views",
        "It takes somewhat longer overall than a plain refresh, since it does extra work to keep the old stored version readable until the new computation is ready to swap in",
        ["It has no trade-off at all; concurrent refresh is strictly faster and better in every way", "It sacrifices correctness, sometimes producing a result that mixes old and new rows permanently", "It requires dropping the materialized view entirely and recreating it from scratch each time"],
    ),
    (
        "According to the \"Ordinary Views vs. Materialized Views at a Glance\" table, how does read cost differ between the two?",
        "An ordinary view pays the full underlying query cost every single time it's read, while a materialized view is fast to read, since it's just reading already-stored data rather than recomputing anything.",
        "medium", "remember", "materialized-views",
        "An ordinary view pays the full underlying query cost on every read; a materialized view is fast to read, since it just reads already-stored data",
        ["Both have identical read costs, since materialized views still recompute their query on every SELECT", "An ordinary view is faster to read, since materialized views must first check for staleness on every read", "Read cost is not a meaningful distinction between the two kinds of views"],
    ),
    (
        "The \"Your Turn\" exercise creates `driver_shipment_totals` as a materialized view summarizing shipment counts per driver, then inserts a new shipment for driver_id 5, and observes the count for driver 5 does not change until REFRESH MATERIALIZED VIEW is explicitly run.\n\nWhat core materialized-view behavior does this exercise reinforce?",
        "It reinforces that a materialized view's stored result is fixed at creation (or last refresh) time and does not automatically incorporate new data, no matter how the underlying table changes, until an explicit REFRESH MATERIALIZED VIEW is run.",
        "medium", "apply", "materialized-views",
        "A materialized view's stored result stays fixed until an explicit REFRESH is run, regardless of how the underlying table changes in the meantime",
        ["It reinforces that materialized views automatically detect and incorporate new inserts within a few seconds", "It reinforces that materialized views cannot be created on tables that receive frequent inserts", "It reinforces that inserting new data into the base table always fails once a materialized view exists"],
    ),
]

STORED_PROCEDURES = [
    (
        "Marking a shipment delivered in Devraj's system requires both an UPDATE to shipments and an INSERT into shipment_log, two statements that always need to run together.\n\nWhy does the lesson introduce a stored procedure instead of relying on every script and developer to remember both statements?",
        "Rather than trusting every script and developer to remember both statements and wrap them correctly, a stored procedure lets this logic be defined once, inside the database itself, as a named, callable unit that guarantees both steps happen together every time.",
        "easy", "understand", "stored-procedures",
        "A stored procedure defines the two-statement logic once inside the database as a named, callable unit, rather than trusting every script or developer to remember and correctly wrap both statements",
        ["A stored procedure is required because PostgreSQL cannot execute two statements in the same transaction otherwise", "A stored procedure automatically converts any single UPDATE into two separate statements", "A stored procedure exists mainly to make the shipments table read-only for all other callers"],
    ),
    (
        "`CREATE PROCEDURE mark_shipment_delivered(p_shipment_id INTEGER) LANGUAGE plpgsql AS $$ ... $$;` uses `$$ ... $$` markers around its body.\n\nWhat is the purpose of this dollar-quoting, according to the lesson?",
        "Dollar-quoting wraps the procedure's body, letting it contain semicolons and even quoted strings of its own without confusing the outer CREATE PROCEDURE statement's own boundaries.",
        "medium", "understand", "stored-procedures",
        "It lets the procedure's body contain semicolons and quoted strings of its own without confusing where the outer CREATE PROCEDURE statement itself begins and ends",
        ["Dollar-quoting is required syntax that tells PostgreSQL the procedure returns a NUMERIC value", "Dollar-quoting encrypts the procedure's body so its logic cannot be viewed by other users", "Dollar-quoting marks the boundaries of a transaction, equivalent to writing BEGIN and COMMIT"],
    ),
    (
        "A procedure is invoked with `CALL mark_shipment_delivered(1);`, not with SELECT.\n\nWhy does the lesson say CALL, not SELECT, is the correct way to invoke it?",
        "A procedure performs actions rather than returning a result set the way a query does, so it is invoked with CALL, which fits its role as something that does things (an UPDATE and an INSERT here) rather than something that produces rows to read.",
        "medium", "understand", "stored-procedures",
        "A procedure performs actions rather than returning a result set like a query does, so CALL fits its role, unlike SELECT which expects rows back",
        ["SELECT is reserved exclusively for querying tables and views, and procedures are neither of those things syntactically", "CALL and SELECT are fully interchangeable for invoking a procedure; either one works identically", "CALL is required only because mark_shipment_delivered accepts a parameter; parameterless procedures use SELECT"],
    ),
    (
        "`mark_multiple_delivered` loops with `FOREACH sid IN ARRAY shipment_ids LOOP ... COMMIT; END LOOP;`, committing after each shipment inside the batch rather than treating the whole procedure as one transaction.\n\nWhy is committing mid-loop useful here, according to the lesson?",
        "The COMMIT inside the loop saves each shipment's update independently, rather than risking the entire batch being rolled back together if one shipment far down the list ran into a problem, useful for long-running procedures that need to save progress incrementally.",
        "medium", "analyze", "stored-procedures",
        "It saves each shipment's update independently, rather than risking the entire batch being rolled back together if a problem occurs with one shipment later in the list",
        ["Committing mid-loop is required syntax and has no actual effect on transaction behavior", "It prevents the FOREACH loop from running more than once per procedure call", "It is used to automatically retry any shipment update that initially fails"],
    ),
    (
        "The lesson notes this ability to commit mid-procedure \"is a capability plain SQL functions, covered in the next lesson, do not have.\"\n\nWhat does this specifically foreshadow about the difference between procedures and functions?",
        "It foreshadows that functions, unlike procedures, cannot manage their own transactions, always running instead as part of whatever transaction the calling statement is already inside, a restriction procedures do not share.",
        "medium", "understand", "stored-procedures",
        "It foreshadows that functions cannot manage their own transactions and always run as part of the caller's existing transaction, unlike procedures which can commit or roll back mid-execution",
        ["It foreshadows that functions will be able to accept arrays as parameters, unlike procedures", "It foreshadows that functions run faster than procedures because they skip transaction overhead entirely", "It foreshadows that functions cannot be written in the plpgsql language, unlike procedures"],
    ),
    (
        "According to the \"Stored Procedures at a Glance\" table, what is the \"typical use\" listed for a procedure?",
        "Multi-statement operations that must always run together, reused across many callers, exactly the shape of Devraj's mark-delivered-and-log operation.",
        "medium", "remember", "stored-procedures",
        "Multi-statement operations that must always run together, reused across many callers",
        ["Computing and returning a single reusable value for use inside a SELECT statement", "Validating incoming data before it is written to a table", "Storing the result of an expensive query for faster repeated reads"],
    ),
]

USER_DEFINED_FUNCTIONS = [
    (
        "Devraj's shipping cost calculation, a base rate plus an oversized surcharge, is copy-pasted, slightly differently, into three different reports.\n\nWhy does the lesson frame this as \"a 'compute one value from some inputs' problem,\" distinct from the stored-procedure problem in the previous lesson?",
        "Unlike marking a shipment delivered, this is not a \"run these statements together\" problem; it's meant to be used inside a SELECT, not called on its own as an action, which is exactly the shape a function fits: a routine that takes inputs and returns a single computed value.",
        "easy", "understand", "user-defined-functions",
        "It's meant to be used inside a SELECT to compute a value, not called as a standalone action, which fits a function's shape rather than a procedure's",
        ["Both problems are identical in shape, and either a procedure or a function would work equally well here", "It's framed this way because functions cannot accept more than one input parameter, unlike procedures", "It's framed this way because shipping cost calculations always require a stored procedure by convention"],
    ),
    (
        "`CREATE FUNCTION calculate_shipping_cost(distance NUMERIC, oversized BOOLEAN) RETURNS NUMERIC LANGUAGE plpgsql AS $$ ... $$;` declares a RETURNS NUMERIC clause.\n\nWhat does this declaration guarantee about the function's behavior?",
        "It declares that this routine always produces exactly one NUMERIC value, distinguishing it from the procedure in the previous lesson, which performed actions and returned nothing.",
        "easy", "understand", "user-defined-functions",
        "It guarantees the function always produces exactly one NUMERIC value, unlike a procedure, which performs actions and returns nothing",
        ["It guarantees the function will always return exactly the value 0 if no explicit RETURN is reached", "It declares that the function's DECLARE section must contain a variable named NUMERIC", "It means the function can only accept NUMERIC-typed parameters, never BOOLEAN ones"],
    ),
    (
        "`SELECT shipment_id, distance_km, is_oversized, calculate_shipping_cost(distance_km, is_oversized) AS shipping_cost FROM shipments;` calls the function once per row, using that row's own column values as arguments.\n\nWhat makes this pattern useful for Devraj's original copy-paste problem?",
        "The shipping-cost logic now lives in one place, and every report that needs it simply calls the function rather than re-deriving the formula, the same reuse benefit a view provides for a saved query, but for a computed value instead.",
        "medium", "apply", "user-defined-functions",
        "The shipping-cost logic lives in one place, and every report simply calls the function instead of re-deriving the formula independently, eliminating the copy-paste inconsistency risk",
        ["This pattern only works if the function is called exactly once per query, never per row", "It's useful because functions automatically cache their result across all rows in a single query", "It's useful only because BOOLEAN parameters are converted to TEXT automatically inside functions"],
    ),
    (
        "The lesson states a function \"cannot issue its own COMMIT or ROLLBACK; it always runs as part of whatever transaction the calling statement is already inside.\"\n\nWhy does this restriction make sense given how a function like calculate_shipping_cost is actually used?",
        "A function is meant to be called from within a SELECT, potentially many times in a single query, one call per row, and allowing it to independently commit or roll back partway through would make no sense in that context, since a single SELECT cannot be partially committed row by row.",
        "medium", "analyze", "user-defined-functions",
        "A function may be called many times within a single SELECT, once per row, and a single SELECT can't be partially committed row by row, so allowing independent commits inside it wouldn't make sense",
        ["The restriction exists only because functions written in plpgsql are read-only and cannot modify any data at all", "It makes sense because functions are always called outside of any transaction context entirely", "It makes sense because COMMIT and ROLLBACK are reserved keywords that functions are syntactically forbidden from containing"],
    ),
    (
        "`oversized_shipments()` is declared with `RETURNS TABLE (shipment_id INTEGER, distance_km NUMERIC)` and uses `RETURN QUERY` inside its body, then is called as `SELECT * FROM oversized_shipments();`.\n\nHow does calling this function compare to selecting from a view, according to the lesson?",
        "Calling oversized_shipments() in FROM behaves exactly like selecting from a view, except this one can accept parameters and contain more elaborate procedural logic than a plain view's single query allows.",
        "medium", "understand", "user-defined-functions",
        "It behaves exactly like selecting from a view, except a table-returning function can accept parameters and contain more elaborate procedural logic than a plain view's single query allows",
        ["It behaves completely differently from a view and cannot be used inside a FROM clause at all", "It is identical to a view in every respect, including being unable to accept any parameters", "RETURN QUERY converts the function permanently into a materialized view once called"],
    ),
    (
        "According to the \"Functions vs. Procedures at a Glance\" table, what does a function return, compared to a procedure?",
        "A function returns a value, or a set of rows, while a procedure returns nothing, unless it uses OUT parameters, reflecting their fundamentally different purposes: computing a value versus performing an action.",
        "medium", "remember", "user-defined-functions",
        "A function returns a value or a set of rows; a procedure returns nothing, unless it uses OUT parameters",
        ["A function always returns nothing, and only a procedure can return a value", "Both a function and a procedure always return exactly one row, by definition", "A function returns a Boolean success flag, while a procedure returns the number of rows affected"],
    ),
]

TRIGGERS = [
    (
        "The mark_shipment_delivered procedure guarantees a log entry, but only if every caller remembers to use that procedure instead of writing a plain UPDATE directly against shipments.\n\nWhat stronger guarantee does Devraj want that leads him to triggers instead?",
        "He wants a log entry created automatically no matter how a shipment's status changes, whether through the procedure, a direct UPDATE, or a future script nobody has written yet, a guarantee with no possibility of a caller forgetting to invoke it.",
        "easy", "understand", "triggers",
        "A guarantee that a log entry is created automatically regardless of how the status change happens, with no possibility of a caller forgetting to invoke the logging logic",
        ["He wants the shipments table to become entirely read-only so no status changes are possible at all", "He wants every status change to require explicit administrator approval before being applied", "He wants to prevent the mark_shipment_delivered procedure from ever being called directly again"],
    ),
    (
        "`log_status_change()` is declared with `RETURNS TRIGGER`, and inside its body references both OLD and NEW without declaring them anywhere.\n\nWhat do OLD and NEW represent inside a trigger function, according to the lesson?",
        "OLD refers to the row's values before the change, and NEW refers to its values after, both automatically available inside a trigger function without being declared anywhere, letting the function compare or log both states.",
        "medium", "understand", "triggers",
        "OLD refers to the row's values before the change and NEW refers to its values after, both automatically made available inside a trigger function",
        ["OLD and NEW refer to the oldest and newest rows in the entire table, not the row being changed", "OLD refers to the previous trigger that fired, and NEW refers to the current one", "OLD and NEW must be manually declared with DECLARE before they can be referenced in a trigger function"],
    ),
    (
        "`CREATE TRIGGER trg_log_status_change AFTER UPDATE ON shipments FOR EACH ROW EXECUTE FUNCTION log_status_change();` is created, and afterward a plain UPDATE with no procedure and no special syntax still produces a log entry automatically.\n\nWhat core advantage does this demonstrate a trigger has over the mark_shipment_delivered procedure from the previous lesson?",
        "The logging behavior is now a property of the table itself, impossible to accidentally skip, unlike the procedure, which only guaranteed logging if a caller specifically chose to invoke it rather than writing a plain UPDATE directly.",
        "medium", "analyze", "triggers",
        "The logging is now a property of the table itself and impossible to skip, unlike the procedure, whose guarantee only held if a caller specifically chose to invoke it instead of a plain UPDATE",
        ["Triggers run faster than procedures because they skip the transaction system entirely", "Triggers can be called directly with CALL, while procedures cannot be invoked at all", "The advantage is that triggers do not require any function to be defined beforehand"],
    ),
    (
        "`prevent_invalid_status()` is attached as a `BEFORE INSERT OR UPDATE` trigger and calls `RAISE EXCEPTION` when NEW.status is not one of the allowed values, causing an update to 'lost_in_space' to fail before it ever reaches the table.\n\nWhy must this validation logic run BEFORE the change, rather than AFTER like the logging trigger?",
        "A BEFORE trigger runs ahead of the actual write and can inspect, reject, or alter the incoming row before it's applied, letting it refuse an invalid change entirely by raising an error, something an AFTER trigger couldn't do since the change would already have happened by then.",
        "medium", "analyze", "triggers",
        "A BEFORE trigger runs ahead of the actual write, letting it reject an invalid change before it's applied; an AFTER trigger would run only once the change has already happened, too late to prevent it",
        ["BEFORE and AFTER triggers behave identically; the choice here is purely a stylistic preference", "BEFORE triggers are required because RAISE EXCEPTION cannot be called from an AFTER trigger for syntax reasons", "AFTER triggers cannot reference NEW.status at all, only BEFORE triggers can access it"],
    ),
    (
        "`trg_instead_of_update`, attached with `INSTEAD OF UPDATE ON shipment_status_view`, translates a write against the view into `UPDATE shipments SET status = NEW.status WHERE shipment_id = OLD.shipment_id;`.\n\nThe lesson notes this view is \"simple enough to be updatable on its own,\" yet still uses an INSTEAD OF trigger. Why does the lesson introduce it here anyway?",
        "The lesson uses this simple case to demonstrate the pattern clearly, noting it \"generalizes directly to the join-based views that cannot be\" automatically updatable, so an INSTEAD OF trigger can define exactly how a write against a genuinely complex view should be translated into changes on the real underlying tables.",
        "hard", "analyze", "triggers",
        "It demonstrates the INSTEAD OF pattern on a simple case first, noting the same technique generalizes directly to join-based views that cannot be automatically updatable",
        ["INSTEAD OF triggers are mandatory on every view, even ones that are already automatically updatable", "The lesson is demonstrating a bug where INSTEAD OF triggers accidentally work on simple views", "It's shown here because BEFORE and AFTER triggers cannot be attached to views at all, only INSTEAD OF can"],
    ),
    (
        "According to the \"Triggers at a Glance\" table, what is the typical use of an AFTER trigger, compared to a BEFORE trigger?",
        "AFTER is typically used for logging, auditing, or cascading updates to other tables, since it runs once the change has already completed, while BEFORE is typically used for validation, rejecting or modifying the incoming row before it's applied.",
        "medium", "remember", "triggers",
        "AFTER is typically used for logging, auditing, or cascading updates to other tables, since it runs after the change completes; BEFORE is used for validation before the change is applied",
        ["AFTER is used exclusively for validation, and BEFORE is used exclusively for logging, the reverse of their actual roles", "AFTER and BEFORE triggers are functionally identical and differ only in naming convention", "AFTER triggers can only be attached to views, while BEFORE triggers can only be attached to tables"],
    ),
]

SYNTHESIS = [
    (
        "The views lesson shows a plain view always re-running its query fresh. The materialized-views lesson shows a materialized view storing a result that goes stale until refreshed. Both solve a reuse problem, but trade off differently.\n\nHow would you decide which of the two to use for a given reporting need, based on what these two lessons establish?",
        "If the query is cheap enough to re-run on every read and the data must always be current, a plain view fits; if the query is expensive (like a large aggregate) and the report can tolerate being current only as of the last refresh, a materialized view trades that staleness for dramatically faster reads — the choice hinges on balancing freshness needs against read cost.",
        "medium", "analyze", "materialized-views",
        "A plain view suits a cheap query needing always-current data; a materialized view suits an expensive query where staleness until the next refresh is an acceptable trade for much faster reads",
        ["The two are functionally identical, and the choice between them never actually matters in practice", "A materialized view should always be preferred, since it is strictly faster in every situation", "A plain view should always be preferred, since materialized views cannot be queried with SELECT"],
    ),
    (
        "The updatable-views lesson shows a join-based view rejecting a direct UPDATE, and mentions INSTEAD OF triggers as the escape hatch. The triggers lesson later shows trg_instead_of_update actually implementing that escape hatch concretely.\n\nHow do these two lessons connect to show INSTEAD OF triggers solving the exact limitation the earlier lesson identified?",
        "The updatable-views lesson identifies the problem: a join-based view's row doesn't map unambiguously to one underlying row, so PostgreSQL can't automatically translate a write; the triggers lesson then shows the actual mechanism, custom procedural logic inside an INSTEAD OF trigger, that lets a developer manually define exactly how such a write should be translated, directly closing the gap the earlier lesson left open.",
        "hard", "analyze", "triggers",
        "The updatable-views lesson identifies the ambiguity problem with join-based views; the triggers lesson shows INSTEAD OF triggers as the concrete mechanism for manually defining how such a write should be translated to underlying tables",
        ["The two lessons are unrelated, and INSTEAD OF triggers actually solve a completely different problem", "INSTEAD OF triggers make every join-based view automatically updatable without requiring any custom logic", "The connection is that INSTEAD OF triggers convert a join-based view into a materialized view instead"],
    ),
    (
        "The stored-procedures lesson shows mark_multiple_delivered committing mid-loop, something a function can't do per the functions lesson. The functions lesson shows calculate_shipping_cost being called once per row inside a single SELECT.\n\nHow does the reason functions can't manage transactions directly explain why calculate_shipping_cost is safe to call many times within one query, while a procedure couldn't be used the same way?",
        "A function is designed to be called potentially many times within a single SELECT, one call per row, and staying purely part of the caller's existing transaction (no independent commits) is exactly what makes that safe; a procedure's ability to commit or roll back independently would make no sense called repeatedly inside a single SELECT's row-by-row evaluation, which is why procedures are invoked separately with CALL rather than embedded in a query.",
        "hard", "analyze", "user-defined-functions",
        "A function staying part of the caller's transaction (no independent commits) is what makes it safe to call many times within one SELECT; a procedure's ability to commit independently wouldn't make sense in that row-by-row context, which is why procedures use CALL instead",
        ["Functions and procedures are actually interchangeable in this context, and either could be embedded in a SELECT", "The reason is unrelated to transactions; functions simply run faster than procedures in every case", "calculate_shipping_cost is safe only because it happens to not modify any data, unlike every procedure"],
    ),
    (
        "Across this chapter: a view reuses a query, a materialized view reuses an expensive query's result, a procedure wraps multi-statement actions, a function computes reusable values, and a trigger runs automatically on table events. Devraj's shipment system ends up using several of these together (a view, a procedure, and a trigger, for instance).\n\nWhat single principle do all five of these objects share, despite their different mechanics?",
        "Each one moves a piece of logic that would otherwise be duplicated, forgotten, or inconsistently applied across many callers or copy-pasted scripts into exactly one place inside the database itself, so every caller, present or future, automatically gets the same correct, consistent behavior.",
        "medium", "understand", "views-naming-a-query-and-reusing-it",
        "Each moves logic that would otherwise be duplicated or inconsistently applied across callers into one place inside the database itself, so every caller automatically gets the same consistent behavior",
        ["All five objects share the principle that they must always be invoked with the CALL statement", "All five objects share the principle that none of them can ever modify data, only read it", "All five objects share the principle that they only work correctly inside a single transaction"],
    ),
]

SET1_SOURCES = [
    (VIEWS_NAMING_A_QUERY, 0),
    (UPDATABLE_VIEWS, 0),
    (MATERIALIZED_VIEWS, 0),
    (STORED_PROCEDURES, 0),
    (USER_DEFINED_FUNCTIONS, 0),
    (TRIGGERS, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    VIEWS_NAMING_A_QUERY[1:]
    + UPDATABLE_VIEWS[1:]
    + MATERIALIZED_VIEWS[1:]
    + STORED_PROCEDURES[1:]
    + USER_DEFINED_FUNCTIONS[1:]
    + TRIGGERS[1:]
)

assert len(SET1) == 10, len(SET1)
assert len(SET2) == 30, len(SET2)


def build_rows(items, set_label, title_prefix):
    positions = [(i % 4) + 1 for i in range(len(items))]
    random.shuffle(positions)

    rows = []
    for idx, (desc, expl, diff, bloom, subtopic, correct, distractors) in enumerate(items, start=1):
        pos = positions[idx - 1]
        options = distractors[:]
        options.insert(pos - 1, correct)
        rows.append({
            "title": f"{title_prefix}.{idx}",
            "description": desc,
            "explanation": expl,
            "score": 1,
            "status": "published",
            "difficulty": diff,
            "bloomTaxonomy": bloom,
            "tags": f"dbms - {set_label}",
            "subjects": "dbms",
            "topics": "going-to-production",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 8.1.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 8.1.2")
all_rows = rows1 + rows2


def summarize(name, rs):
    diff, bloom, sub, ans = {}, {}, {}, {1: 0, 2: 0, 3: 0, 4: 0}
    for r in rs:
        diff[r["difficulty"]] = diff.get(r["difficulty"], 0) + 1
        bloom[r["bloomTaxonomy"]] = bloom.get(r["bloomTaxonomy"], 0) + 1
        sub[r["subTopics"]] = sub.get(r["subTopics"], 0) + 1
        ans[r["answer"]] += 1
    print(name, "diff:", diff)
    print(name, "bloom:", bloom)
    print(name, "subtopics:", sub)
    print(name, "answers:", ans)


summarize("SET1", rows1)
summarize("SET2", rows2)

descs = [r["description"] for r in all_rows]
assert len(descs) == len(set(descs)), "duplicate description found"
for r in all_rows:
    opts = [r["option1"], r["option2"], r["option3"], r["option4"]]
    assert len(set(opts)) == 4, f"duplicate option in {r['title']}: {opts}"

headers = ["title", "description", "explanation", "score", "status", "difficulty", "bloomTaxonomy",
           "tags", "subjects", "topics", "subTopics", "companies",
           "option1", "option2", "option3", "option4", "answer"]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "DBMS - MCQ - Unit 8.1"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 8 - Going to Production/8.1 - Views and Programmability - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
