## Introduction

Every query in this course so far has run inside an editor already connected to a database, with connection details handled invisibly. A real application never gets that convenience for free; before it can run a single `SELECT`, it has to establish a **connection**, a live, authenticated link between the application process and the database server, and that connection has its own setup cost, its own configuration, and its own failure modes worth understanding before writing a line of query code.

## What a Connection String Actually Contains

An application typically opens a connection using a `connection string`, a compact format bundling everything the database needs to know: where the server is, which database to use, and who is connecting.

```postgresql file=connection_demo.sql
CREATE TABLE app_config (
    config_key TEXT PRIMARY KEY,
    config_value TEXT
);

INSERT INTO app_config (config_key, config_value) VALUES
('host', 'db.internal.example.com'),
('port', '5432'),
('database', 'shipments_prod'),
('user', 'app_service_account');
```

```postgresql with=connection_demo.sql
SELECT * FROM app_config;
```

A real `connection string` built from values like these would look something like `postgresql://app_service_account:password@db.internal.example.com:5432/shipments_prod`, bundling four pieces into one string most database client libraries accept directly:

1. The host
2. The port
3. The database name
4. The credentials

The `app_config` table above is only illustrative, showing the pieces such a string is made of; a production application would never store a raw password in a plain table like this, and the security chapter of this unit covers exactly why, and what to do instead.

## Why Every Connection Involves a Real Cost

Opening a connection is not free: it typically means a network round trip to the server, an authentication handshake, and the server allocating resources on its side to track that connection. This is the reason a well-built application does not open a brand new connection for every single query it runs.

```postgresql with=connection_demo.sql
SELECT count(*) AS active_connections FROM pg_stat_activity;
```

`pg_stat_activity` is a real, queryable `view` showing every connection currently open to the database, a useful way to see this cost made concrete: each row represents a live connection the server is actively tracking and maintaining resources for, not a free, weightless link.

## Closing a Connection Matters as Much as Opening One

A connection that is opened but never properly closed continues consuming server-side resources indefinitely, even after the application code that opened it has long since finished using it, or crashed without cleaning up.

```postgresql with=connection_demo.sql
SELECT pid, state, query, now() - query_start AS running_for
FROM pg_stat_activity
WHERE state = 'idle';
```

A connection sitting in the `idle` state, especially one that has been idle for a long time, is exactly this kind of leak: application code that opened it, ran a query, and then never closed it, leaving the server holding onto that connection's resources for no active purpose. Well-written application code always ensures a connection is closed once it is no longer needed, typically through a pattern the connecting language provides for guaranteed cleanup, even if an error occurs partway through.

## A Connection Failure Is Not the Same as a Query Failure

It matters to distinguish, in application code, between a connection that fails to open at all, the database is down, unreachable, or credentials are wrong, and a query that fails after a connection is already successfully open, a syntax error or a `constraint` violation. The two call for different handling: a connection failure often means retrying after a delay or alerting that the database itself is unreachable, while a query failure, covered throughout this course through `constraint` violations and rollbacks, is about the specific statement, not the link to the database itself.

## Connecting to a Database at a Glance

| Concept | Detail |
|---|---|
| Connection string | Bundles host, port, database name, and credentials |
| Cost of opening | Network round trip, authentication, server-side resource allocation |
| `pg_stat_activity` | Shows every currently open connection to the server |
| Closing a connection | Essential; an unclosed connection leaks server resources |
| Connection failure vs. query failure | Different causes, different handling in application code |

## Your Turn

Query `pg_stat_activity` for the current database, filtering to just this session's own connection, and identify which columns describe the connection itself versus the query currently running on it.

```postgresql with=connection_demo.sql
-- Write your query below
```

`SELECT pid, usename, datname, state, query FROM pg_stat_activity WHERE pid = pg_backend_pid();` isolates this exact session's own row; `pid`, `usename`, and `datname` describe the connection itself, while `state` and `query` describe what that connection is currently doing, a distinction worth keeping clear when reasoning about connection versus query behavior.

## Conclusion

A connection is a real, costly, stateful link between an application and a database, requiring a `connection string` to establish, real server-side resources to maintain, and deliberate closing to avoid leaking those resources, with connection failures and query failures representing genuinely different problems that call for different handling in application code. The next lesson looks at a related concern: how application code should safely build the actual SQL text it sends across an established connection.
