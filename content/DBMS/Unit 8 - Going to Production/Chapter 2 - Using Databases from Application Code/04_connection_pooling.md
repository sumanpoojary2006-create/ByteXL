## Introduction

Opening a connection has a real cost, covered when connecting from application code was first introduced, and a busy web application might handle hundreds of requests per second, each one potentially wanting to talk to the database. Opening and closing a brand new connection for every single one of those requests would mean paying that connection cost constantly, and it would also risk overwhelming the database server, which can only sustain a limited number of simultaneous connections. **`Connection pooling`** solves both problems: instead of opening a fresh connection per request, an application keeps a pool of already-open connections ready to be borrowed, used, and returned.

## Why a Database Cannot Handle Unlimited Connections

Every open connection consumes real memory and resources on the database server itself, which is why PostgreSQL enforces a hard limit on how many connections it will accept at once.

```postgresql file=pooling_demo.sql
SHOW max_connections;
```

```postgresql with=pooling_demo.sql
SELECT count(*) AS current_connections FROM pg_stat_activity;
```

`max_connections` reports the server's configured ceiling, commonly 100 in a default installation, and the current connection count shows how much of that ceiling is already in use. If an application, or many application instances together, tried to open a new connection per incoming request under real traffic, it could exhaust this limit quickly, and every connection attempt beyond it would fail outright, taking down the whole application's ability to reach the database at all.

## The Pooling Pattern: Borrow, Use, Return

A `connection pool` maintains a fixed, modest number of already-open connections, and application code borrows one from the pool when it needs to run a query, then returns it when finished, rather than closing it.

```postgresql with=pooling_demo.sql
-- Conceptually, application code using a pool looks like this pseudocode,
-- shown alongside the SQL it wraps:
-- connection = pool.borrow_connection()
-- try:
BEGIN;
SELECT count(*) FROM pg_stat_activity;
COMMIT;
-- finally:
--     pool.return_connection(connection)
-- The connection itself was never closed; it goes back into the pool,
-- already open and authenticated, ready for the next request to borrow it.
```

Because the connection was never actually closed, the next request that needs the database can borrow that same already-open connection instantly, skipping the network round trip and authentication handshake that opening a brand new one would require.

The pool typically maintains a fixed size, say 20 connections, regardless of how many requests the application is simultaneously handling. Two things make that work:

1. 20 open connections can serve far more than 20 requests over time.
2. Each individual query has to finish quickly and return its connection promptly for that to hold.

## Why a Connection Must Be Returned in a Clean State

A returned connection has to be ready for a completely different, unrelated request to borrow next, which means it must never be handed back mid-transaction or holding onto leftover session state from whatever the previous request was doing.

```postgresql with=pooling_demo.sql
SELECT pid, state FROM pg_stat_activity WHERE state = 'idle in transaction';
```

The "idle in transaction" danger covered in the previous lesson becomes especially serious in a pooled setup: a connection returned to the pool while still mid-transaction would hand the next, completely unrelated request a connection that is unexpectedly holding `lock`s and half-finished work from a previous, unrelated operation, a bug that can be extremely confusing to track down, since the request experiencing the strange behavior is not the one that caused it.

## Pool Size Is a Deliberate Trade-off

A pool that is too small forces requests to wait for a connection to become available, adding latency under load. A pool that is too large risks exhausting the database's `max_connections` limit, especially once multiple application instances each maintain their own pool against the same database server.

```postgresql with=pooling_demo.sql
SELECT usename, count(*) AS connections_per_user
FROM pg_stat_activity
GROUP BY usename;
```

In a real production setup, this kind of query, grouping open connections by which application or user opened them, is a standard way to monitor whether pool sizes across an organization's various services are collectively approaching the database's overall connection ceiling, since `max_connections` is a single, shared limit across every application talking to that database, not a per-application allowance.

## Connection Pooling at a Glance

| Concept | Detail |
|---|---|
| Without pooling | A new connection opened and closed per request, paying full connection cost every time |
| With pooling | A fixed set of connections reused across many requests, borrowed and returned |
| `max_connections` | The database server's hard ceiling on simultaneous connections, shared across all applications |
| Pool size trade-off | Too small adds waiting; too large risks exhausting the server's connection limit |
| Returning a connection | Must be in a clean state, no open transaction, no leftover session state |

## Your Turn

Check the current `max_connections` setting and the current number of active connections, then write a comment estimating what percentage of the limit is currently in use.

```postgresql with=pooling_demo.sql
-- Write your queries and comment below
```

Running `SHOW max_connections;` alongside `SELECT count(*) FROM pg_stat_activity;` gives both numbers needed to compute this percentage directly; in a real production system, alerting is typically configured once this percentage crosses a threshold like 80%, giving operators time to investigate before connections actually start being refused.

## Conclusion

`Connection pooling` reuses a fixed set of already-open connections across many requests instead of opening and closing one per request, avoiding both the repeated connection cost and the risk of exhausting the database's shared `max_connections` limit, with careful attention needed to ensure a connection is always returned to the pool in a clean, transaction-free state. The next lesson steps back to compare two fundamentally different styles of writing the database-facing code that actually runs on top of these connections: raw SQL and an object-relational mapper.
