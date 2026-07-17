import random
import openpyxl

random.seed(182)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

CONNECTING_TO_A_DATABASE = [
    (
        "Every query written in the course editor so far ran already connected to a database, with connection details handled invisibly.\n\nWhat does the lesson say a real application must do before it can run a single SELECT, that the course editor never required?",
        "It must first establish a connection, a live, authenticated link between the application process and the database server, which has its own setup cost, configuration, and failure modes worth understanding before writing any query code.",
        "easy", "understand", "connecting-to-a-database-from-application-code",
        "It must first establish a connection, a live authenticated link to the database server, with its own setup cost, configuration, and failure modes",
        ["It must first create a new database from scratch for every single query it runs", "It must first convert every query into a stored procedure before it can execute", "It must first request a schema migration to be applied before connecting"],
    ),
    (
        "A real connection string looks like `postgresql://app_service_account:password@db.internal.example.com:5432/shipments_prod`.\n\nWhat four pieces does the lesson say a connection string bundles together?",
        "The host, the port, the database name, and the credentials, four pieces most database client libraries accept directly as one combined string.",
        "easy", "remember", "connecting-to-a-database-from-application-code",
        "The host, the port, the database name, and the credentials",
        ["The table name, the column list, the query text, and the expected result type", "The operating system, the CPU architecture, the driver version, and the timezone", "The transaction isolation level, the lock timeout, the pool size, and the retry count"],
    ),
    (
        "`pg_stat_activity` is described as a real, queryable view showing every connection currently open to the database, with each row representing a live connection the server is actively tracking.\n\nWhy does the lesson use this view to make the cost of opening a connection \"concrete\"?",
        "It shows that each open connection is not a free, weightless link, but something the server is actively maintaining resources for, visible directly as a row in this view, which is why a well-built application does not open a brand new connection for every single query it runs.",
        "medium", "understand", "connecting-to-a-database-from-application-code",
        "It shows each open connection is something the server actively maintains resources for, visible as a row in the view, illustrating why opening a connection per query would be wasteful",
        ["It shows that connections are entirely free and cost nothing to maintain on the server", "pg_stat_activity only tracks connections that have already been closed, not open ones", "It proves that only one connection can ever be open to a database at any given time"],
    ),
    (
        "A query against `pg_stat_activity WHERE state = 'idle'` reveals a connection that has been idle for a long time, described as \"exactly this kind of leak.\"\n\nWhat specifically causes this kind of leak, according to the lesson?",
        "Application code opened the connection, ran a query, and then never closed it, leaving the server holding onto that connection's resources for no active purpose, continuing to consume server-side resources indefinitely.",
        "medium", "analyze", "connecting-to-a-database-from-application-code",
        "Application code opened the connection, ran a query, and never closed it, leaving the server to hold onto that connection's resources indefinitely for no active purpose",
        ["The leak is caused by the database automatically creating duplicate connections for every query", "Idle connections are always caused by a network failure between the client and server", "The leak happens because pg_stat_activity itself opens a new connection every time it's queried"],
    ),
    (
        "The lesson distinguishes a connection that fails to open at all (database down, unreachable, wrong credentials) from a query that fails after a connection is already open (a syntax error or constraint violation).\n\nWhy does the lesson say these two failure types \"call for different handling\" in application code?",
        "A connection failure often means retrying after a delay or alerting that the database itself is unreachable, while a query failure is about the specific statement, not the link to the database itself, and is handled through constraint violations and rollbacks instead.",
        "medium", "understand", "connecting-to-a-database-from-application-code",
        "A connection failure typically calls for retrying or alerting that the database is unreachable, while a query failure is about the specific statement and is handled through constraint violations and rollbacks",
        ["Both failure types are actually identical and should always be handled with the exact same retry logic", "A query failure always means the entire database server has crashed and must be restarted", "Connection failures are only relevant during initial application startup, never afterward"],
    ),
    (
        "According to the \"Connecting to a Database at a Glance\" table, what makes closing a connection \"essential\"?",
        "An unclosed connection leaks server resources, continuing to consume them even after application code has finished using it or crashed without cleaning up.",
        "medium", "remember", "connecting-to-a-database-from-application-code",
        "An unclosed connection leaks server resources, which continue being consumed even after the application is done with it",
        ["Closing a connection is only necessary if the application plans to open a second connection later", "An unclosed connection automatically converts into a prepared statement instead", "Closing a connection is optional in every case and has no real consequence either way"],
    ),
]

PREPARED_STATEMENTS = [
    (
        "Building SQL by pasting `user_input` directly into a string works fine when user_input is `\"1\"`, but if user_input were instead `\"1 OR 1=1\"`, the pasted-together query returns every row in the table instead of just shipment 1.\n\nWhy does this happen, according to the lesson?",
        "The pasted-in text was interpreted as SQL syntax rather than a single value, letting untrusted input change the query's actual structure and logic entirely, rather than being treated as inert data being compared against shipment_id.",
        "easy", "understand", "prepared-statements",
        "The pasted-in text was interpreted as SQL syntax rather than a single inert value, letting untrusted input change the query's actual structure and logic",
        ["The query fails outright with a syntax error whenever user_input contains extra text", "PostgreSQL automatically strips out any text after the first number in a WHERE clause", "This happens only because shipment_id is declared as an INTEGER instead of TEXT"],
    ),
    (
        "`PREPARE get_shipment (INTEGER) AS SELECT * FROM shipments WHERE shipment_id = $1;` followed by `EXECUTE get_shipment(1);` splits a query into two separate pieces.\n\nWhat does each of the two pieces represent?",
        "PREPARE defines the query's fixed structure once, with $1 marking a placeholder for a value to be supplied later, not text to be pasted into the query, and EXECUTE then supplies the actual value entirely separately from that structure.",
        "medium", "understand", "prepared-statements",
        "PREPARE defines the query's fixed structure once with a placeholder ($1); EXECUTE then supplies the actual value entirely separately from that structure",
        ["PREPARE runs the query immediately, and EXECUTE only logs that it ran", "PREPARE defines the value to search for, and EXECUTE defines the query's structure", "Both PREPARE and EXECUTE do the exact same thing, and either one alone would work"],
    ),
    (
        "Even if the value supplied to `EXECUTE get_shipment($1)` were a maliciously crafted string, the lesson says the injection demonstrated with string-pasting \"becomes structurally impossible.\"\n\nWhy specifically does separating structure from value prevent this, rather than just making it less likely?",
        "The supplied value is handled purely as data, a single value being compared against shipment_id, never as SQL syntax that could change what the query does, so there is no mechanism by which a value could alter the query's structure at all, not just a reduced chance of it happening.",
        "medium", "analyze", "prepared-statements",
        "The value is handled purely as data compared against a column, never as SQL syntax, so there's no mechanism for it to alter the query's structure at all, not merely a reduced risk",
        ["It only reduces the likelihood of injection but does not eliminate it entirely", "It prevents injection only for INTEGER-typed parameters, not TEXT-typed ones", "It works by scanning the input value for suspicious keywords like OR and rejecting them"],
    ),
    (
        "The same `get_shipment` prepared statement is executed three times with different values: `EXECUTE get_shipment(1);`, `EXECUTE get_shipment(2);`, `EXECUTE get_shipment(3);`.\n\nWhat does this demonstrate about the relationship between a prepared statement and the values it's executed with?",
        "The same prepared query structure can be executed repeatedly with different values without redefining the query each time, exactly the pattern a real application follows when handling many different incoming requests using the same underlying prepared statement.",
        "medium", "apply", "prepared-statements",
        "The same prepared query structure can be executed repeatedly with different values without redefining the query each time, matching how a real application handles many different requests",
        ["Each EXECUTE call silently redefines the entire prepared statement from scratch", "A prepared statement can only ever be executed once, and PREPARE must be re-run for each new value", "Different values require a completely separate PREPARE statement to be written for each one"],
    ),
    (
        "Beyond the safety benefit, the lesson describes a performance benefit: the database can parse and plan a query's structure once, then reuse that plan across multiple executions with different values.\n\nWhat cost does this reuse specifically avoid, compared to a freshly built SQL string?",
        "It skips the repeated parsing and planning cost that a fresh, newly-built SQL string would incur every single time, since a prepared statement's structure is analyzed and planned only once regardless of how many times it's later executed with different values.",
        "medium", "understand", "prepared-statements",
        "It skips the repeated parsing and planning cost a freshly built SQL string would incur on every single execution, since the structure is analyzed and planned only once",
        ["It avoids the cost of opening a new database connection for each execution", "It eliminates the need for the database to store any data on disk at all", "It avoids the cost of transferring data over the network entirely"],
    ),
    (
        "The conclusion notes that \"every database client library's 'parameterized query' feature is this same mechanism, just expressed through that language's own syntax rather than SQL's PREPARE and EXECUTE directly.\"\n\nWhat does this imply about the relationship between PREPARE/EXECUTE and a client library's parameterized query feature?",
        "They are conceptually the same underlying mechanism, separating query structure from runtime values, just expressed through different syntax; a client library's parameterized query feature isn't a different technique, it's the same one wrapped in that language's own interface.",
        "medium", "analyze", "prepared-statements",
        "They are the same underlying mechanism (separating structure from values), just expressed through different syntax; a library's parameterized queries aren't a different technique, just a different interface to it",
        ["Parameterized queries in client libraries work completely differently from SQL's PREPARE and EXECUTE", "Only PostgreSQL's own PREPARE and EXECUTE actually protect against SQL injection; libraries do not", "Client libraries only support parameterized queries for SELECT statements, never for INSERT or UPDATE"],
    ),
]

MANAGING_TRANSACTIONS = [
    (
        "After `BEGIN;` runs on one connection, the state column in pg_stat_activity for that connection's pid changes to active or idle in transaction, tied specifically to `pg_backend_pid()`.\n\nWhat does the lesson say happens if an application opens a second, separate connection at this exact moment?",
        "That second connection would have no visibility into the first connection's in-progress transaction at all, and could not accidentally commit or roll it back, since a transaction belongs entirely to the specific connection it was started on, not a general, database-wide state.",
        "easy", "understand", "managing-transactions-from-your-application",
        "The second connection would have no visibility into the first connection's transaction and could not affect it, since a transaction belongs entirely to the connection that started it",
        ["The second connection would automatically join and share the first connection's in-progress transaction", "The second connection would be blocked from opening until the first transaction commits or rolls back", "The second connection would see a merged view combining both connections' uncommitted changes"],
    ),
    (
        "If application code calls BEGIN but, due to a bug or unhandled error, never reaches COMMIT or ROLLBACK, the connection is left in a state called \"idle in transaction,\" still holding whatever locks it acquired, indefinitely.\n\nWhy is this dangerous, according to the lesson?",
        "A connection stuck this way continues holding its lock on the affected row for as long as the connection stays open, potentially blocking every other transaction that needs that same row, exactly the kind of contention the concurrency control unit covered.",
        "medium", "analyze", "managing-transactions-from-your-application",
        "The stuck connection continues holding locks indefinitely, potentially blocking every other transaction that needs the same row, the same kind of contention covered in concurrency control",
        ["It's dangerous only because it slowly fills up the server's disk space over time", "It's dangerous because it automatically triggers a full database restart after a timeout", "This state is actually harmless since PostgreSQL automatically releases locks after a few seconds"],
    ),
    (
        "`SAVEPOINT before_risky_step;` is set after updating shipment 1, then shipment 2's update to an invalid status happens, then `ROLLBACK TO SAVEPOINT before_risky_step;` runs, followed by COMMIT.\n\nWhat is the final state of the transaction's changes after this sequence?",
        "Only shipment 1's valid update survives; ROLLBACK TO SAVEPOINT undoes only the changes made after the savepoint (shipment 2's incorrect update), while keeping everything before it fully intact, and the final COMMIT then commits shipment 1's change alone.",
        "medium", "apply", "managing-transactions-from-your-application",
        "Only shipment 1's update survives; the savepoint rollback undoes shipment 2's change while keeping shipment 1's change intact, and COMMIT then finalizes just that surviving change",
        ["Both shipment 1's and shipment 2's updates are discarded entirely by the ROLLBACK TO SAVEPOINT", "Both shipment 1's and shipment 2's updates are committed, since ROLLBACK TO SAVEPOINT has no real effect", "The entire transaction fails and nothing is committed, since a savepoint was rolled back"],
    ),
    (
        "A batch operation sending 50 notifications and logging each one in the same transaction can use a savepoint before each item, so that one item's failure only rolls back that one item's work.\n\nWhat does the lesson say would happen without savepoints in this scenario?",
        "A single failure anywhere in the loop would force the entire transaction, all 50 items, to roll back together, an outcome that is often far more disruptive than necessary, since one bad item would discard 49 otherwise-successful ones too.",
        "medium", "analyze", "managing-transactions-from-your-application",
        "A single failure anywhere in the loop would force the entire transaction, all 50 items, to roll back together, discarding otherwise-successful work along with the one failure",
        ["Without savepoints, the batch operation would simply skip the failing item automatically and continue", "Without savepoints, only the failing item's own change would be affected, identical to using savepoints", "Without savepoints, the transaction would commit successfully regardless of any failures"],
    ),
    (
        "The lesson states well-written application code \"always wraps its transaction logic in a structure that guarantees COMMIT or ROLLBACK runs no matter what, even when an unexpected error occurs.\"\n\nWhat problem does this discipline specifically guard against?",
        "It guards against a connection being left \"idle in transaction\" due to a bug or unhandled error preventing COMMIT or ROLLBACK from ever running, which would otherwise hold locks indefinitely and potentially block other work.",
        "medium", "understand", "managing-transactions-from-your-application",
        "It guards against a connection being left idle in transaction after an unhandled error, which would otherwise hold locks indefinitely and block other work",
        ["It guards against the database running out of disk space during a large transaction", "It guards against SQL injection attacks originating from unvalidated user input", "It guards against the connection pool running out of available connections"],
    ),
    (
        "According to the \"Managing Transactions from an Application at a Glance\" table, what does ROLLBACK TO SAVEPOINT name specifically do?",
        "It undoes changes made after the named savepoint, while keeping the transaction itself and the changes made before that savepoint alive, rather than discarding the entire transaction.",
        "medium", "remember", "managing-transactions-from-your-application",
        "It undoes changes made after the savepoint, while keeping the transaction and earlier changes alive",
        ["It undoes every change made in the transaction, identical in effect to a plain ROLLBACK", "It commits every change made before the savepoint and discards the transaction afterward", "It creates a brand new transaction, separate from the one the savepoint was set in"],
    ),
]

CONNECTION_POOLING = [
    (
        "A busy web application might handle hundreds of requests per second, each one potentially wanting to talk to the database, and opening a brand new connection for every single one would pay that connection cost constantly.\n\nWhat does connection pooling do instead, according to the lesson?",
        "Instead of opening a fresh connection per request, an application keeps a pool of already-open connections ready to be borrowed, used, and returned, avoiding the repeated cost of opening and closing a connection for every request.",
        "easy", "understand", "connection-pooling",
        "It keeps a pool of already-open connections that requests borrow, use, and return, instead of opening a fresh connection for every single request",
        ["It opens exactly one connection and forces every request to run sequentially through that single connection", "It converts every query into a prepared statement automatically to reduce connection overhead", "It creates a brand new database for each incoming request to isolate them completely"],
    ),
    (
        "PostgreSQL enforces a hard limit on how many connections it will accept at once, reported by `SHOW max_connections;`, commonly 100 in a default installation.\n\nWhat does the lesson warn would happen if an application (or many application instances together) opened a new connection per incoming request under real traffic?",
        "It could exhaust the max_connections limit quickly, and every connection attempt beyond it would fail outright, taking down the whole application's ability to reach the database at all.",
        "medium", "analyze", "connection-pooling",
        "It could quickly exhaust the max_connections limit, causing every connection attempt beyond it to fail outright and taking down the application's ability to reach the database",
        ["The database would automatically raise its own max_connections limit to accommodate the load", "Extra connection attempts would simply be queued indefinitely with no risk of failure", "PostgreSQL would silently ignore excess connection attempts with no visible effect"],
    ),
    (
        "The lesson explains a pool typically maintains a fixed size, say 20 connections, regardless of how many requests the application is simultaneously handling, and that \"20 open connections can serve far more than 20 requests over time.\"\n\nWhat second condition does the lesson say must also hold for this to work?",
        "Each individual query has to finish quickly and return its connection promptly, since a fixed pool of 20 connections can only serve many more than 20 requests if each borrowed connection is used briefly and released back for the next request to reuse.",
        "medium", "understand", "connection-pooling",
        "Each individual query has to finish quickly and return its connection promptly, so a fixed-size pool can cycle through serving many more requests than its connection count over time",
        ["The pool must be resized dynamically to match the exact number of simultaneous requests", "Every request must use exactly the same SQL query text for pooling to work correctly", "The database's max_connections setting must be disabled entirely for pooling to function"],
    ),
    (
        "The lesson says a connection returned to the pool while still mid-transaction would hand the next, completely unrelated request a connection unexpectedly holding locks and half-finished work, calling this \"a bug that can be extremely confusing to track down.\"\n\nWhy specifically is this bug hard to trace, according to the lesson?",
        "The request seeing the strange behavior is not the request that caused it, since the leftover transaction state came from a previous, unrelated operation that already finished from the application's point of view, making the actual cause invisible to whoever is debugging the symptom.",
        "hard", "analyze", "connection-pooling",
        "The request seeing the strange behavior is not the request that caused it, since the leftover transaction state came from an earlier, unrelated operation, disconnecting cause from visible symptom",
        ["It's hard to trace because pg_stat_activity cannot show connections that are idle in transaction", "It's hard to trace because the bug only ever happens once and cannot be reproduced", "It's hard to trace because connection pooling disables all logging for pooled connections"],
    ),
    (
        "The lesson describes pool size as \"a deliberate trade-off\": too small forces requests to wait, too large risks exhausting max_connections, especially once multiple application instances each maintain their own pool against the same database server.\n\nWhy does having multiple application instances each with their own pool make the too-large risk worse?",
        "Since max_connections is a single, shared limit across every application talking to that database, not a per-application allowance, each instance's pool adds to the same shared ceiling, so several moderately sized pools across many instances can collectively approach or exceed that one shared limit.",
        "medium", "analyze", "connection-pooling",
        "max_connections is a single limit shared across all applications, not a per-application allowance, so multiple instances' pools all draw from and can collectively exhaust that same shared ceiling",
        ["Each application instance gets its own separate max_connections allowance, so this isn't actually a real risk", "Multiple instances automatically coordinate to share one combined pool, eliminating the risk entirely", "The risk only applies if all instances are running on the exact same physical server"],
    ),
    (
        "According to the \"Connection Pooling at a Glance\" table, what condition must a returned connection meet before it goes back into the pool?",
        "It must be in a clean state, with no open transaction and no leftover session state, ready for a completely different, unrelated request to borrow next.",
        "medium", "remember", "connection-pooling",
        "It must be in a clean state, with no open transaction and no leftover session state",
        ["It must have run at least one successful query before being returned to the pool", "It must be closed and reopened before being placed back into the pool", "It must be assigned to the same user account as the next request that will borrow it"],
    ),
]

ORM_VS_RAW_SQL = [
    (
        "An ORM lets a developer work with database rows as ordinary objects in their programming language, generating the actual SQL behind the scenes.\n\nFor the straightforward filter example shown (`Shipment.objects.filter(status='in_transit')`), what does the lesson say is the ORM's main selling point here?",
        "The developer never has to write or think about SQL text at all; work happens entirely in terms of objects and method calls in their own programming language, with the library handling the translation, and the generated SQL matches exactly what a developer would have written by hand.",
        "easy", "understand", "orm-vs-raw-sql",
        "The developer never has to write or think about SQL text at all, working entirely in objects and method calls while the library handles the translation to matching SQL",
        ["The ORM's main benefit is that it always generates faster SQL than a human developer could write", "The ORM's main benefit is that it eliminates the need for a database connection entirely", "The ORM's main benefit is that it prevents any possibility of a query ever failing"],
    ),
    (
        "Looping over shipments and accessing `shipment.driver.driver_name` inside that loop can silently trigger one additional query per shipment, exactly the N+1 pattern from the performance unit.\n\nWhy does the lesson call this \"exactly the danger\" of an ORM's abstraction?",
        "An ORM's abstraction can hide the fact that a query is happening at all, making it easy to write code that is correct but silently slow, since nothing about `shipment.driver.driver_name` looks like a database performance hazard, reading instead like ordinary property access.",
        "medium", "analyze", "orm-vs-raw-sql",
        "The ORM's abstraction can hide that a query is even happening, since accessing a related object looks like ordinary property access rather than a database call, making correct-but-silently-slow code easy to write",
        ["The danger is that ORMs cannot express filtering conditions like status = 'in_transit' at all", "The danger is that ORM-generated queries always return incorrect results compared to raw SQL", "The danger is that ORMs require a completely separate database connection for every object accessed"],
    ),
    (
        "The fix for the ORM's N+1 hazard is described as requiring \"the developer specifically knows to ask the ORM to fetch related data eagerly, in one combined query, rather than one at a time as each object is touched.\"\n\nWhat does this reveal about the responsibility an ORM shifts onto the developer?",
        "The convenience of not writing SQL doesn't remove the developer's responsibility to understand what queries are actually being generated; avoiding the N+1 hazard requires explicit awareness and deliberate action (requesting eager loading), not just trusting the ORM's default behavior.",
        "hard", "analyze", "orm-vs-raw-sql",
        "Avoiding N+1 still requires the developer to understand what queries the ORM generates and deliberately request eager loading, rather than assuming the ORM's default behavior is automatically efficient",
        ["The ORM entirely removes any need for the developer to think about database performance at all", "This reveals that ORMs are strictly worse than raw SQL in every situation without exception", "It reveals that eager loading is only possible when using raw SQL, never through an ORM"],
    ),
    (
        "For a genuinely complex report involving several joins, window functions, and careful aggregation, the lesson says writing raw SQL directly is \"often more straightforward than coaxing an ORM's object-oriented interface into generating that same precise query.\"\n\nWhat capability does raw SQL offer here that the lesson highlights?",
        "Full control over exactly what plan the database is likely to choose, and something every SQL developer can write directly and reason about precisely, unlike trying to force an ORM's interface to express the same complex logic.",
        "medium", "understand", "orm-vs-raw-sql",
        "Full, precise control over the query's exact shape and the plan the database is likely to choose, which every SQL developer can write and reason about directly",
        ["Raw SQL is highlighted only because ORMs are physically incapable of running any aggregate function", "Raw SQL is highlighted because it always executes faster than any ORM-generated query, without exception", "Raw SQL is highlighted because ORMs cannot connect to a database at all for reporting purposes"],
    ),
    (
        "The lesson states most real applications settle into \"ORM for routine, simple operations, raw SQL for anything genuinely complex or performance-sensitive,\" calling this \"the pragmatic middle ground.\"\n\nWhat does this framing suggest about how the trade-off between ORM and raw SQL should actually be resolved in practice?",
        "Rather than treating it as an all-or-nothing choice between the two approaches, most real applications use both together, choosing whichever fits a given situation, since most ORMs also offer an escape hatch for running raw SQL directly when needed.",
        "medium", "analyze", "orm-vs-raw-sql",
        "Most real applications use both approaches together rather than choosing one exclusively, applying whichever fits a given situation, since ORMs typically offer a raw-SQL escape hatch",
        ["The framing suggests that raw SQL should always be avoided once an ORM has been adopted", "The framing suggests that ORMs should never be used in any application that also needs raw SQL", "The framing suggests the two approaches are functionally identical and the choice never matters"],
    ),
    (
        "According to the \"ORM vs. Raw SQL at a Glance\" table, how does SQL injection protection compare between the two approaches?",
        "An ORM provides SQL injection protection built in by default, while raw SQL requires deliberate use of prepared statements to achieve the same protection.",
        "medium", "remember", "orm-vs-raw-sql",
        "An ORM has SQL injection protection built in by default, while raw SQL requires deliberately using prepared statements to get the same protection",
        ["Raw SQL has SQL injection protection built in by default, while an ORM requires extra configuration", "Neither approach offers any real protection against SQL injection under any circumstances", "Both approaches are equally vulnerable to SQL injection regardless of how they're used"],
    ),
]

MIGRATIONS_AND_SCHEMA_VERSIONING = [
    (
        "A developer runs `ALTER TABLE shipments ADD COLUMN priority TEXT DEFAULT 'normal';` by hand directly on their laptop's database, and it works perfectly there.\n\nWhat problem does the lesson say appears \"the moment there is more than one database is involved\"?",
        "Without a system tracking exactly which changes have been applied where, it becomes unclear whether this same ALTER TABLE was run against testing, against production, and in what order, if there were several changes made — the exact uncertainty migrations exist to remove.",
        "easy", "understand", "database-migrations-and-schema-versioning",
        "It becomes unclear whether the same schema change has been applied to testing and production, and in what order, without a system tracking exactly what's been applied where",
        ["The ALTER TABLE statement itself becomes invalid once a second database exists", "PostgreSQL automatically applies every schema change to all connected databases simultaneously", "The developer's laptop database becomes permanently out of sync and unusable"],
    ),
    (
        "The `schema_migrations` table records each migration's unique, ordered identifier (like `0001_create_shipments`), and a migration tool checks this table before running anything.\n\nWhat does the tool do if a version is already recorded versus if it is missing?",
        "If a version is already recorded, that migration is skipped since it has already been applied; if it is missing, the tool runs it and then records it, making it safe to run the same migration command against a fresh, partially-migrated, or fully up-to-date database alike.",
        "medium", "apply", "database-migrations-and-schema-versioning",
        "If already recorded, the migration is skipped as already applied; if missing, the tool runs it and then records it, making the same command safe to run against any database regardless of its migration state",
        ["The tool always re-runs every migration regardless of whether it's already recorded", "If a version is missing, the tool deletes the table and starts the schema over from scratch", "The tool only checks this table once per day, not before every migration run"],
    ),
    (
        "Migration 0003 writes both `ALTER TABLE shipments ADD COLUMN delivery_deadline DATE;` and the corresponding `INSERT INTO schema_migrations ...` together, described as \"the kind of pairing a transaction is well suited to wrap.\"\n\nWhy does wrapping both statements in a transaction matter here?",
        "So that either both the schema change and its tracking record take effect, or neither does, never leaving the schema changed without the tracking table reflecting it, keeping the two tightly coupled and consistent with each other.",
        "medium", "analyze", "database-migrations-and-schema-versioning",
        "So either both the schema change and its tracking record succeed together, or neither does, preventing the schema from being changed without the tracking table reflecting that fact",
        ["Wrapping them in a transaction makes the ALTER TABLE statement run faster", "It's required because ALTER TABLE cannot run outside of a transaction under any circumstances", "It prevents other connections from ever seeing the shipments table again"],
    ),
    (
        "The lesson calls dropping and recreating a table to make a structural change \"a tempting but dangerous migration pattern,\" contrasted with using `ALTER TABLE ADD COLUMN` and similar structure-preserving statements.\n\nWhat specifically makes the drop-and-recreate approach dangerous?",
        "It discards every row of existing data along with the table, silently destroying data that ALTER TABLE-based structure-preserving statements would have kept intact while still changing the table's structure.",
        "medium", "understand", "database-migrations-and-schema-versioning",
        "It discards every row of existing data along with the table, silently destroying data that structure-preserving ALTER TABLE statements would have kept intact",
        ["It's dangerous only because DROP TABLE requires manual confirmation that slows down deployments", "It's dangerous because ALTER TABLE statements are not supported in PostgreSQL at all", "It's dangerous because it requires taking the entire database server offline for several hours"],
    ),
    (
        "The lesson says migrations against a production database \"always deserve careful review before being applied, the same caution this course has emphasized around any DROP or DELETE since the modifying-data chapter early on.\"\n\nWhat does this callback connect the migrations lesson's caution to?",
        "It connects to the earlier, general discipline this course established around DROP and DELETE statements, treating a destructive migration pattern (drop-and-recreate) as deserving exactly the same careful review and caution as any other data-destroying operation covered earlier in the course.",
        "medium", "analyze", "database-migrations-and-schema-versioning",
        "It connects to the course's earlier general discipline around DROP and DELETE, treating a destructive migration pattern as deserving the same careful review as any other data-destroying operation",
        ["It connects migrations specifically to the transactions unit's discussion of savepoints", "It connects migrations to the connection pooling lesson's discussion of idle connections", "It connects migrations to the ORM lesson's discussion of the N+1 query problem"],
    ),
    (
        "According to the \"Database Migrations at a Glance\" table, what does \"idempotent application\" mean for a migration tool?",
        "Running the same migration tool anywhere only applies what is genuinely missing, since already-applied migrations are recorded and skipped, letting the same command run safely and consistently against any environment.",
        "medium", "remember", "database-migrations-and-schema-versioning",
        "Running the same migration tool anywhere only applies what is genuinely missing, letting the same command run safely and consistently regardless of which migrations already exist there",
        ["It means every migration can only ever be applied to exactly one environment, never more than one", "It means the migration tool automatically undoes the most recent migration each time it runs", "It means migrations must be applied in a random, unordered sequence to remain idempotent"],
    ),
]

SYNTHESIS = [
    (
        "The connecting-to-a-database lesson establishes that opening a connection has a real cost (network round trip, authentication, server resources). The connection-pooling lesson builds directly on that cost to justify pooling.\n\nHow does the earlier lesson's framing of connection cost directly motivate the pooling lesson's solution?",
        "Because opening a connection is genuinely costly, not free, a busy application handling many requests would pay that cost repeatedly and risk exhausting the server's max_connections limit if it opened a fresh connection per request; connection pooling directly addresses this by reusing a fixed set of already-open connections, avoiding the repeated cost the first lesson established as real.",
        "medium", "analyze", "connection-pooling",
        "Because connections are genuinely costly (not free), opening one per request would pay that cost repeatedly and risk exhausting the connection limit; pooling directly solves this by reusing already-open connections",
        ["The two lessons are unrelated, since connection pooling has nothing to do with connection cost", "Connection pooling exists to make opening new connections even more expensive, as a deliberate trade-off", "The earlier lesson's point about cost is actually contradicted by the pooling lesson's approach"],
    ),
    (
        "The managing-transactions lesson warns about a connection left \"idle in transaction,\" holding locks indefinitely. The connection-pooling lesson says this danger \"becomes especially serious in a pooled setup,\" since a connection returned mid-transaction hands the next unrelated request leftover locks and half-finished work.\n\nHow does pooling specifically amplify the idle-in-transaction danger described in the earlier lesson?",
        "Without pooling, an idle-in-transaction connection only affects the one request that caused it and whatever else it blocks; with pooling, that same bug can also corrupt a completely unrelated future request that borrows the same connection next, since the connection is reused rather than closed, spreading the confusion across requests that have no relationship to the original cause.",
        "hard", "analyze", "connection-pooling",
        "Pooling reuses connections rather than closing them, so an idle-in-transaction bug can leak leftover locks and state onto a completely unrelated future request that borrows the same connection next, spreading confusion beyond the original cause",
        ["Pooling actually eliminates the idle-in-transaction danger entirely, contradicting the earlier lesson's warning", "The danger is identical with or without pooling, and the two lessons describe unrelated problems", "Pooling only affects read-only queries, so transactions are never actually impacted by it"],
    ),
    (
        "The prepared-statements lesson shows PREPARE/EXECUTE preventing SQL injection by separating structure from values. The ORM-vs-raw-SQL lesson notes an ORM has \"SQL injection protection built in, by default,\" while raw SQL \"requires deliberate use of prepared statements.\"\n\nHow do these two lessons connect to explain what \"deliberate use\" actually means for a raw-SQL developer?",
        "An ORM automatically applies the structure-versus-values separation the prepared-statements lesson demonstrated, on the developer's behalf, every time; a raw-SQL developer gets no such automatic protection and must consciously choose to use PREPARE/EXECUTE (or a client library's parameterized query equivalent) on every query touching untrusted input, rather than it happening without any decision on their part.",
        "hard", "analyze", "orm-vs-raw-sql",
        "An ORM applies the prepared-statement mechanism automatically on every query; a raw-SQL developer must consciously choose to use PREPARE/EXECUTE (or its equivalent) themselves, since no automatic protection is applied without that deliberate choice",
        ["Deliberate use means raw SQL requires manually re-typing every value directly into the query string", "The two lessons are unrelated, and ORM injection protection works through a completely different mechanism", "It means raw SQL developers must avoid using SELECT statements to prevent injection"],
    ),
    (
        "The migrations lesson pairs a schema change with its tracking-table record inside a transaction, calling it \"the kind of pairing a transaction is well suited to wrap.\" The managing-transactions lesson explains transactions guarantee grouped statements either all happen or none do.\n\nHow does the managing-transactions lesson's core guarantee directly explain why the migrations lesson insists on wrapping the ALTER TABLE and the schema_migrations insert together?",
        "A transaction ensures that either both statements take effect or neither does; applied to a migration, this guarantees the schema is never left changed without the tracking table reflecting it (or vice versa), preventing exactly the kind of drift between actual schema state and recorded migration history that would recreate the original tracking problem migrations were built to solve.",
        "medium", "analyze", "database-migrations-and-schema-versioning",
        "A transaction guarantees either both statements succeed or neither does, ensuring the schema is never changed without the tracking table reflecting it, preventing drift between actual and recorded state",
        ["Transactions have no real bearing on migrations; the pairing is purely a matter of code organization style", "The connection is that transactions make ALTER TABLE statements run in a fraction of the time", "Transactions are mentioned here only because migrations always require multiple separate database connections"],
    ),
]

SET1_SOURCES = [
    (CONNECTING_TO_A_DATABASE, 0),
    (PREPARED_STATEMENTS, 0),
    (MANAGING_TRANSACTIONS, 0),
    (CONNECTION_POOLING, 0),
    (ORM_VS_RAW_SQL, 0),
    (MIGRATIONS_AND_SCHEMA_VERSIONING, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    CONNECTING_TO_A_DATABASE[1:]
    + PREPARED_STATEMENTS[1:]
    + MANAGING_TRANSACTIONS[1:]
    + CONNECTION_POOLING[1:]
    + ORM_VS_RAW_SQL[1:]
    + MIGRATIONS_AND_SCHEMA_VERSIONING[1:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 8.2.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 8.2.2")
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
ws.title = "DBMS - MCQ - Unit 8.2"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 8 - Going to Production/8.2 - Using Databases from Application Code - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
