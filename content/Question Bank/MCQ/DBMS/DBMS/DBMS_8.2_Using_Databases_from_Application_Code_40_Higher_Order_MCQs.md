# DBMS 8.2: Using Databases from Application Code — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Going to Production
- **Chapter:** Using Databases from Application Code
- **Scope:** Connecting to a Database from Application Code; Prepared Statements; Managing Transactions from Your Application; Connection Pooling; ORM vs. Raw SQL; Database Migrations and Schema Versioning
- **SQL dialect:** PostgreSQL
- **Format:** Four plausible options with exactly one best answer
- **Is Curriculum Based:** No
- **Coverage rule:** Questions 1–10 collectively cover all six chapter subtopics.
- **Design standard:** Questions use application traces, SQL snippets, connection state, transaction timelines, generated queries, and migration histories.
- **Answer-quality controls:** A/B/C/D are each correct exactly 10 times; no answer letter occurs more than twice consecutively.

---

## Questions

### 1. The application has not reached SQL yet

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connecting to a Database from Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Distinguishing failure stages

An application reports “authentication failed” while opening `postgresql://app@db.internal:5432/shipments_prod`. No session appears for it in `pg_stat_activity`.

Which diagnosis best fits?

A. A `SELECT` has a syntax error.  
B. A row violates a table constraint.  
C. The connection failed before any query could run.  
D. A savepoint used the wrong name.

### 2. Runtime input must remain data

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Prepared Statements  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest secure repair

Application code currently builds:

```text
"SELECT * FROM shipments WHERE shipment_id = " + user_input
```

Which repair prevents input such as `1 OR 1=1` from changing the query structure?

A. Use a parameter placeholder and bind the input as a value.  
B. Add `ORDER BY shipment_id` to the concatenated SQL.  
C. Run the constructed string inside a savepoint.  
D. Open a new connection for each lookup.

### 3. Two connections cannot share one transaction

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Managing Transactions from Your Application  
**Is Curriculum Based:** No  
**Assessment type:** Analysing connection ownership

Connection A runs `BEGIN` and updates shipment 1. Connection B then issues `COMMIT`, expecting to finish A’s work.

What happens conceptually?

A. B commits every open transaction in the database.  
B. B takes ownership because it issued the latest command.  
C. A’s update is committed only if both sessions agree.  
D. B cannot commit A’s transaction; it belongs exclusively to A.

### 4. Reusing authenticated links

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connection Pooling  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an application structure

A web service opens and authenticates a new database connection for every short request. Under load, setup latency rises and the server nears `max_connections`.

Which architecture directly addresses both symptoms?

A. Store every query in a materialized view.  
B. Borrow, use, and return connections from a bounded pool.  
C. Replace all SQL with an ORM.  
D. Place each request in one large shared transaction.

### 5. An innocent property access produces 501 queries

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** ORM vs. Raw SQL  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing generated-query behaviour

An ORM fetches 500 shipments once. Accessing `shipment.driver.name` in a loop then triggers one driver query per shipment.

Which review finding is accurate?

A. The ORM generated one optimized join.  
B. Raw SQL cannot retrieve related rows.  
C. This is N+1 behaviour; eager loading or one explicit join should be evaluated.  
D. Connection pooling automatically combines the 500 child queries.

### 6. The schema differs across three environments

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Migrations and Schema Versioning  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a consistency mechanism

Development has a `priority` column, testing does not, and nobody knows whether production received last week’s change.

Which practice resolves this uncertainty?

A. Apply ordered migration scripts and record their versions in each database.  
B. Ask developers to remember which commands they typed.  
C. Recreate every environment’s tables before each release.  
D. Store schema notes only in application comments.

### 7. A connection string assembled from configuration

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connecting to a Database from Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Completing connection information

Configuration contains host, port, database name, and username. What additional category is normally required to authenticate the application?

A. The text of its first query  
B. The table’s primary-key value  
C. Credentials, such as the account’s password  
D. The current number of pooled connections

### 8. One prepared structure, three values

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Prepared Statements  
**Is Curriculum Based:** No  
**Assessment type:** Tracing repeated execution

```sql
PREPARE get_shipment (INTEGER) AS
SELECT destination FROM shipments WHERE shipment_id=$1;

EXECUTE get_shipment(1);
EXECUTE get_shipment(2);
EXECUTE get_shipment(3);
```

Which part changes between executions?

A. The table definition  
B. Only the value bound to `$1`  
C. The prepared query’s SQL structure  
D. The connection string

### 9. Keeping the first successful update

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Managing Transactions from Your Application  
**Is Curriculum Based:** No  
**Assessment type:** Tracing a savepoint

```sql
BEGIN;
UPDATE shipments SET status='delivered' WHERE shipment_id=1;
SAVEPOINT before_risky;
UPDATE shipments SET status='oops' WHERE shipment_id=2;
ROLLBACK TO SAVEPOINT before_risky;
COMMIT;
```

Both shipments began `in_transit`. What is the final state?

A. Both are `in_transit`.  
B. Both are `delivered`.  
C. Shipment 1 is `oops`; shipment 2 is `in_transit`.  
D. Shipment 1 is `delivered`; shipment 2 is `in_transit`.

### 10. The pool is returned a half-finished request

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connection Pooling  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a lifecycle defect

A request borrows a pooled connection, starts a transaction, updates a row, and returns the connection without commit or rollback.

What is the smallest essential repair in the cleanup path?

A. Guarantee rollback on failure or commit on success before returning the connection.  
B. Increase the pool size so the contaminated connection is rarely reused.  
C. Close and recreate the database server after every request.  
D. Convert the update to an ORM object assignment.

### 11. Identifying connection-string fields

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connecting to a Database from Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Parsing configuration

For `postgresql://app_user:secret@db.internal:5432/shipments_prod`, which mapping is correct?

A. Host `app_user`, port `secret`, database `db.internal`  
B. User `app_user`, host `db.internal`, port `5432`, database `shipments_prod`  
C. User `shipments_prod`, host `5432`, database `app_user`  
D. Host `secret`, port `shipments_prod`, database `5432`

### 12. A leak visible after requests finish

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connecting to a Database from Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an observation that exposes a defect

Traffic has stopped, yet `pg_stat_activity` shows hundreds of long-idle sessions from the service.

Which defect best explains the evidence?

A. Prepared statements are returning too many rows.  
B. Migrations were applied in the wrong order.  
C. The ORM translated a filter incorrectly.  
D. Application paths are opening connections without reliably closing them.

### 13. Completing PostgreSQL PREPARE syntax

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Prepared Statements  
**Is Curriculum Based:** No  
**Assessment type:** Filling missing SQL

```sql
PREPARE get_by_destination (TEXT) AS
SELECT * FROM shipments WHERE destination = _____;
```

A. `$1`  
B. `{destination}`  
C. `?destination?`  
D. `INPUT`

### 14. Deallocating a statement

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Prepared Statements  
**Is Curriculum Based:** No  
**Assessment type:** Identifying final statement state

After `DEALLOCATE get_shipment;`, application code attempts `EXECUTE get_shipment(2);` on the same connection.

Which outcome follows?

A. It silently prepares the statement again.  
B. Execution fails because that prepared statement has been released.  
C. It runs using the most recently supplied value.  
D. It closes the database connection.

### 15. Why planning can be reused

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Prepared Statements  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two implementations

Version P prepares one fixed lookup and executes it 10,000 times with different IDs. Version S constructs 10,000 separate SQL strings.

Which potential advantage does P have in addition to input safety?

A. It guarantees every ID exists.  
B. It avoids all network communication.  
C. The database can reuse parsed/planned query structure across executions.  
D. It converts every query into one transaction automatically.

### 16. Idle in transaction is not harmless idleness

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Managing Transactions from Your Application  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected behaviour

A connection ran `BEGIN`, updated shipment 2, then waited indefinitely without a final command.

Why can this block unrelated application work?

A. Every idle connection locks every table.  
B. PostgreSQL runs the unfinished update repeatedly.  
C. The connection permanently consumes a prepared statement name.  
D. Its open transaction can retain locks until commit or rollback.

### 17. A savepoint is not a second transaction

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Managing Transactions from Your Application  
**Is Curriculum Based:** No  
**Assessment type:** Correcting a transaction model

Which statement correctly describes `ROLLBACK TO SAVEPOINT sp1`?

A. It discards work after `sp1` while keeping the surrounding transaction active.  
B. It commits work before `sp1` immediately.  
C. It transfers the transaction to another connection.  
D. It closes the connection after discarding all work.

### 18. Guaranteed cleanup around transaction code

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Managing Transactions from Your Application  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a correct error-handling approach

An application performs two related updates. The second can raise an exception.

Which control pattern is most appropriate?

A. Commit after the first update so at least one change survives.  
B. Commit on success, roll back on any failure, and release the connection in guaranteed cleanup.  
C. Leave the transaction open so an operator can inspect it later.  
D. Retry the second statement forever on the same open transaction.

### 19. Twenty connections serve more than twenty requests

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connection Pooling  
**Is Curriculum Based:** No  
**Assessment type:** Reasoning about resource reuse

Why can a pool of 20 connections serve thousands of requests over time?

A. Each connection runs every request simultaneously.  
B. PostgreSQL ignores the pool’s configured size.  
C. Requests borrow connections briefly and return them for later requests.  
D. Prepared statements create extra invisible connections.

### 20. Pool sizes across replicas add up

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connection Pooling  
**Is Curriculum Based:** No  
**Assessment type:** Calculating shared capacity

Five application instances each configure a pool maximum of 18. Ignoring other users, how many database connections can they collectively request?

A. 18  
B. 23  
C. 72  
D. 90

### 21. A pool that is too small

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connection Pooling  
**Is Curriculum Based:** No  
**Assessment type:** Identifying a boundary trade-off

The database has capacity, queries finish quickly, but requests regularly wait for a connection because the pool contains only two.

Which first adjustment addresses the observed bottleneck?

A. Increase the pool cautiously and monitor total server connections.  
B. Remove all transaction cleanup.  
C. Open an unlimited number of connections.  
D. Replace the pool with one connection per query.

### 22. ORM code hides database work

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** ORM vs. Raw SQL  
**Is Curriculum Based:** No  
**Assessment type:** Identifying unexpected generated behaviour

The line `print(shipment.driver.name)` looks like property access, but query logs show a `SELECT drivers ...` each time it runs in a loop.

What should the developer infer?

A. The database is executing a trigger on every read.  
B. Lazy relationship access is causing hidden database queries.  
C. The connection pool is duplicating each statement.  
D. A migration converted the property into SQL.

### 23. Choosing raw SQL for precise query shape

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** ORM vs. Raw SQL  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an appropriate implementation

A performance-critical report needs several joins, a window function, aggregation, and precise plan inspection. The ORM expression is harder to understand than the generated SQL.

Which choice is most defensible?

A. Split the report into one ORM query per row.  
B. Avoid querying the database for complex reports.  
C. Use explicit raw SQL with parameter binding for this report.  
D. Add more connections until the ORM expression becomes faster.

### 24. ORM and raw SQL are not opposing religions

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** ORM vs. Raw SQL  
**Is Curriculum Based:** No  
**Assessment type:** Comparing implementation trade-offs

Which architecture reflects the lesson’s balanced recommendation?

A. Raw SQL for every trivial CRUD operation, regardless of maintenance cost.  
B. ORM for all reports, even when generated queries cannot be controlled.  
C. Choose one approach permanently for the entire organization.  
D. Use ORM for routine operations and raw SQL where complexity or performance needs control.

### 25. Counting the hidden N+1 workload

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** ORM vs. Raw SQL  
**Is Curriculum Based:** No  
**Assessment type:** Tracing generated queries

One ORM query loads 40 shipments. A loop lazily fetches one driver for each shipment.

How many total queries are issued?

A. 40  
B. 41  
C. 80  
D. 1,600

### 26. One missing migration in testing

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Migrations and Schema Versioning  
**Is Curriculum Based:** No  
**Assessment type:** Tracing version history

Available migrations are `0001`, `0002`, and `0003`. Testing’s `schema_migrations` table contains `0001` and `0002`.

What should the migration tool do?

A. Reapply all three from the beginning.  
B. Drop the schema and create only version `0003`.  
C. Apply `0003` and record it; skip versions already present.  
D. Record `0003` without executing its schema change.

### 27. Preserving rows while adding a field

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Migrations and Schema Versioning  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest safe migration

Production `shipments` contains two million rows. The next version needs a nullable `carrier TEXT` column.

Which change preserves existing rows?

A. `ALTER TABLE shipments ADD COLUMN carrier TEXT;`  
B. `DROP TABLE shipments; CREATE TABLE shipments (..., carrier TEXT);`  
C. Export only the table definition and replace production.  
D. Delete existing rows before altering the table.

### 28. Schema changed, history did not

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Migrations and Schema Versioning  
**Is Curriculum Based:** No  
**Assessment type:** Spotting an inconsistent migration state

A script adds `delivery_deadline`, then crashes before recording `0003_add_delivery_deadline`. The tool later sees `0003` missing.

What design would have prevented this split state?

A. Use a larger connection pool during deployment.  
B. Express the migration through an ORM model only.  
C. Run the version insert before reviewing the schema SQL.  
D. Couple the schema change and version record in one transaction when supported.

### 29. Connection failure and query failure need different handling

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connecting to a Database from Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a correct handling approach

Case X: the host is unreachable. Case Y: a live connection receives an insert that violates a constraint.

Which response separates the failures appropriately?

A. Treat both as successful empty results.  
B. Retry both statements indefinitely without rollback.  
C. X may warrant delayed reconnect/alerting; Y requires statement or transaction error handling.  
D. Rebuild the database schema for both cases.

### 30. The connection must always be returned

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connection Pooling  
**Is Curriculum Based:** No  
**Assessment type:** Completing application cleanup logic

```text
connection = pool.borrow()
try:
    run_request(connection)
finally:
    ______
```

Assuming transaction success/failure has already been finalized, what belongs in the blank?

A. `pool.return(connection)`  
B. `open_another_connection()`  
C. `begin_transaction(connection)`  
D. `delete_connection_from_server()`

### 31. Prepared input does not become an operator

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Prepared Statements  
**Is Curriculum Based:** No  
**Assessment type:** Reasoning about bound values

A prepared integer lookup binds the user input text `1 OR 1=1` to `$1`.

Why can it not turn the predicate into an always-true expression?

A. PostgreSQL removes every `OR` from all input strings.  
B. The supplied input is treated as one typed value, not parsed into the SQL structure.  
C. The connection pool rejects all strings containing spaces.  
D. A savepoint reverses the extra rows afterward.

### 32. A returned connection carries another request’s transaction

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connection Pooling  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an input sequence that exposes a defect

Which two-request sequence best exposes a pool cleanup bug?

A. Request A performs only `SELECT`; Request B opens a separate database.  
B. Request A commits and returns; Request B reads unrelated data.  
C. Both requests use different pools and close normally.  
D. Request A returns mid-transaction; Request B borrows that same connection and observes its unfinished state.

### 33. A migration is code, not an informal note

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Migrations and Schema Versioning  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the most appropriate workflow

Which artifact best represents `0004_add_carrier_column`?

A. A developer’s message saying the column was added somewhere  
B. A small reviewed script that alters the schema and records ordered version `0004`  
C. A screenshot of the production table  
D. A full database recreation command

### 34. A straightforward ORM translation

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** ORM vs. Raw SQL  
**Is Curriculum Based:** No  
**Assessment type:** Comparing semantic implementations

ORM pseudocode is `Shipment.objects.filter(status='in_transit')`. Which SQL expresses the same operation?

A. `UPDATE shipments SET status='in_transit';`  
B. `SELECT * FROM shipments WHERE status='in_transit';`  
C. `SELECT status, COUNT(*) FROM shipments;`  
D. `DELETE FROM shipments WHERE status<>'in_transit';`

### 35. Why opening is not free

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connecting to a Database from Application Code  
**Is Curriculum Based:** No  
**Assessment type:** Tracing connection setup work

Which work occurs before a newly opened connection can execute its first query?

A. Compilation of all queries the application may ever send  
B. Automatic migration of every application table  
C. Creation of a dedicated database server  
D. Network communication, authentication, and server resource allocation

### 36. Choosing a pool boundary

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Connection Pooling  
**Is Curriculum Based:** No  
**Assessment type:** Evaluating a capacity decision

PostgreSQL permits 100 connections. Four service replicas each propose a pool of 30, before administrative and monitoring sessions are counted.

Which review is correct?

A. Approve it because `max_connections` applies separately to each replica.  
B. Approve it because idle pooled sessions use no server resources.  
C. Reduce and coordinate pool sizes; their potential total already exceeds the shared ceiling.  
D. Disable transaction cleanup to return connections faster.

### 37. Version history predicts schema

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Migrations and Schema Versioning  
**Is Curriculum Based:** No  
**Assessment type:** Identifying an inconsistent environment

Migration history says `0002_add_priority` was applied, but inspection shows no `priority` column.

What does this reveal?

A. The environment is inconsistent: its recorded version and actual schema disagree.  
B. The migration tool should skip every later migration permanently.  
C. The missing column is expected until an ORM accesses it.  
D. Version tables describe application releases, not schema changes.

### 38. Savepoint placement controls what survives

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Managing Transactions from Your Application  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two transaction versions

Version A creates a savepoint after updating shipment 1, then rolls back to it after shipment 2 fails. Version B creates the savepoint before either update and rolls back to it.

Which difference follows?

A. Both versions must preserve shipment 1.  
B. Neither version can continue to commit.  
C. A can preserve shipment 1; B’s rollback also discards shipment 1’s update.  
D. B transfers shipment 1’s update to another connection.

### 39. Parameterization and ORM defaults

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** ORM vs. Raw SQL  
**Is Curriculum Based:** No  
**Assessment type:** Evaluating a safety comparison

Which statement is accurate?

A. Raw SQL is always unsafe, even with bound parameters.  
B. ORM code cannot generate N+1 queries because it parameterizes values.  
C. Connection pooling is the mechanism that prevents injection in both.  
D. ORM operations commonly parameterize values; raw SQL should deliberately use prepared parameters.

### 40. Designing the database boundary for a busy service

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Migrations and Schema Versioning  
**Is Curriculum Based:** No  
**Assessment type:** Applying multiple chapter concepts

A new service handles untrusted shipment IDs, serves high request volume, and must deploy a data-preserving `carrier` column consistently to test and production.

Which combined design is strongest?

A. Bound query parameters, a bounded clean-return connection pool, and a versioned `ALTER TABLE ... ADD COLUMN` migration  
B. SQL string concatenation, one new connection per query, and drop/recreate deployment  
C. ORM lazy loading for every relation and manual production-only schema edits  
D. One global transaction shared by every connection and an untracked schema command

---

## Instructor Key

### 1. C
Authentication failed while establishing the link, so the application never reached query execution.

### 2. A
Binding the input keeps it separate from SQL structure, so hostile text remains a value rather than becoming an operator.

### 3. D
A transaction is connection-local. Commands on B cannot commit or roll back A’s in-progress work.

### 4. B
A bounded pool reuses authenticated connections and limits how many server sessions the application can consume.

### 5. C
One parent query plus one relationship query per object is N+1; eager loading or a set-based join addresses its structure.

### 6. A
Ordered, tracked migrations provide an explicit schema history that each environment can apply consistently.

### 7. C
The connection needs credentials in addition to its network target, database, and account identity.

### 8. B
The prepared SQL remains fixed; only the integer supplied for placeholder `$1` changes.

### 9. D
Rollback to the savepoint removes shipment 2’s later update but keeps shipment 1’s earlier change for the final commit.

### 10. A
Every borrowed connection must have its transaction finalized before return, including rollback on error paths.

### 11. B
The URI identifies `app_user`, the `db.internal` host, port 5432, and database `shipments_prod`.

### 12. D
Long-idle sessions after work ends are direct evidence that some paths are failing to release connections.

### 13. A
PostgreSQL prepared statements use `$1`, `$2`, and later numbered placeholders for typed runtime values.

### 14. B
`DEALLOCATE` releases the named prepared statement, so it cannot be executed again until prepared anew.

### 15. C
Separating fixed structure from changing values allows parsing and planning work to be reused.

### 16. D
An idle open transaction can retain acquired locks and block other transactions that need the same resources.

### 17. A
Rollback to a savepoint reverses only later work and leaves both earlier work and the outer transaction alive.

### 18. B
Success must commit, failure must roll back, and cleanup must release the connection regardless of which path occurs.

### 19. C
Connections are reused sequentially across many short requests rather than being permanently assigned to one request.

### 20. D
Five potential pools of 18 can collectively request `5 × 18 = 90` connections from the shared server.

### 21. A
Careful expansion can reduce waiting, but total usage must still be monitored against the shared server limit.

### 22. B
The ORM’s lazy relationship property is hiding a database call inside what looks like ordinary object access.

### 23. C
Raw SQL gives direct control over the complex statement and plan, while bound parameters preserve safe value handling.

### 24. D
The approaches can coexist: ORM convenience suits routine operations, while raw SQL suits cases needing precise control.

### 25. B
One shipment query plus 40 driver queries produces 41 statements.

### 26. C
The version table shows `0001` and `0002` are complete, leaving only `0003` to execute and record.

### 27. A
`ALTER TABLE ... ADD COLUMN` changes structure without discarding the table’s existing rows.

### 28. D
One transaction can keep the schema change and its version record atomic, preventing one from succeeding without the other.

### 29. C
Unreachability concerns the connection and may justify reconnect handling; a constraint violation concerns a statement and its transaction.

### 30. A
After transaction cleanup, the borrowed live connection should be returned so another request can reuse it.

### 31. B
The parameter is handled as one typed value and is never reparsed as part of the prepared SQL grammar.

### 32. D
Returning a connection mid-transaction allows a later borrower to inherit locks and unfinished state from the earlier request.

### 33. B
A migration is a small, ordered, reviewed schema-change script whose applied version is tracked.

### 34. B
The ORM filter corresponds to selecting shipment rows whose status equals `in_transit`.

### 35. D
Opening a connection requires a network exchange, authentication, and allocation of server-side connection resources.

### 36. C
Four pools of 30 can request 120 connections before other sessions, exceeding one shared limit of 100.

### 37. A
The version record claims a structural change that is absent, so the environment’s history and schema are inconsistent.

### 38. C
A’s savepoint comes after shipment 1, so rollback preserves it; B’s earlier savepoint places both updates in the rollback range.

### 39. D
ORMs typically bind values automatically, while manually written SQL must intentionally use parameters rather than concatenation.

### 40. A
The combination handles unsafe input, connection cost/capacity, clean reuse, and consistent data-preserving schema evolution.

---

## Coverage summary

| Subtopic | Questions |
|---|---|
| Connecting to a Database from Application Code | 1, 7, 11, 12, 29, 35 |
| Prepared Statements | 2, 8, 13, 14, 15, 31 |
| Managing Transactions from Your Application | 3, 9, 16, 17, 18, 38 |
| Connection Pooling | 4, 10, 19, 20, 21, 30, 32, 36 |
| ORM vs. Raw SQL | 5, 22, 23, 24, 25, 34, 39 |
| Database Migrations and Schema Versioning | 6, 26, 27, 28, 33, 37, 40 |
