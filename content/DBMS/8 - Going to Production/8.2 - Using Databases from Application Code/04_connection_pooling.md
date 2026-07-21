## Introduction

Opening a `connection` has a real cost, covered when connecting from application code was first introduced, and a busy web application might handle hundreds of requests per second, each one potentially wanting to talk to the `database`.

Opening and closing a brand new `connection` for every single one of those requests would mean paying that `connection` cost constantly, and it would also risk overwhelming the `database` server, which can only sustain a limited number of simultaneous `connections`. **`Connection pooling`** solves both problems: instead of opening a fresh `connection` per request, an application keeps a pool of already-open `connections` ready to be borrowed, used, and returned.

**Definition:** `Connection pooling` reuses a fixed set of already-open `connections` across many requests instead of opening and closing one per request, avoiding both the repeated `connection` cost and the risk of exhausting the `database`'s shared `max_connections` limit, with careful attention needed to ensure a `connection` is always returned to the pool in a clean, `transaction`-free state.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_connection_pooling.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Opening a connection has a real cost, covered when connecting from application code was first introduced, and a busy web application might handle hundreds of requests per second, each one potentially wanting to talk to the database. Opening and closing a.

ON-IMAGE TEXT: show a short bold title "Connection Pooling" plus only these few labels, large and legible: Connection, Pooling, Opening. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for connection pooling](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_intro_connection_pooling_matched_f6417918.png)

## Why a Database Cannot Handle Unlimited Connections

Every open `connection` consumes real memory and resources on the `database` server itself, which is why PostgreSQL enforces a hard limit on how many `connections` it will accept at once.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The table below shows the rows loaded by the setup file.

### `shipments`

| shipment_id | status |
| --- | --- |
| 1 | in_transit |
| 2 | in_transit |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed table. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql file=init.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit'), (2, 'in_transit');
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

```postgresql with=init.sql
SHOW max_connections;

SELECT count(*) AS current_connections FROM pg_stat_activity;
```

Expected observation: PostgreSQL returns live server metadata. Values differ across OneCompiler runs, so verify the meaning of each column and the trend described below rather than matching a fixed number.

- `max_connections` reports the server's configured ceiling, commonly 100 in a default installation, and the current `connection` count shows how much of that ceiling is already in use.
- If an application, or many application instances together, tried to open a new `connection` per incoming request under real traffic, it could exhaust this limit quickly, and every `connection` attempt beyond it would fail outright, taking down the whole application's ability to reach the `database` at all.

## The Pooling Pattern: Borrow, Use, Return

A `connection pool` maintains a fixed, modest number of already-open `connections`, and application code borrows one from the pool when it needs to run a `query`, then returns it when finished, rather than closing it.

```postgresql with=init.sql
-- Conceptually, application code using a pool looks like this pseudocode,
-- shown alongside the SQL it wraps:
-- connection = pool.borrow_connection()
-- try:
BEGIN;
UPDATE shipments SET status = 'delivered' WHERE shipment_id = 1;
SELECT * FROM shipments;
COMMIT;
-- finally:
--     pool.return_connection(connection)
-- The connection itself was never closed; it goes back into the pool,
-- already open and authenticated, ready for the next request to borrow it.
```

Expected output:

| shipment_id | status |
| --- | --- |
| 1 | delivered |
| 2 | in_transit |

Because the `connection` was never actually closed, the next request that needs the `database` can borrow that same already-open `connection` instantly, skipping the network round trip and authentication handshake that opening a brand new one would require. The `SELECT` confirms shipment 1's update committed inside the borrowed `connection`, exactly as an ordinary `transaction` would, while shipment 2 is untouched.

The pool typically maintains a fixed size, say 20 `connections`, regardless of how many requests the application is simultaneously handling. Two things make that work:

1. 20 open `connections` can serve far more than 20 requests over time.

2. Each individual `query` has to finish quickly and return its `connection` promptly for that to hold.

![A connection pool lets requests borrow, use, and return already-open connections](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_connection_pool_borrow_use_return.png)

## Why a Connection Must Be Returned in a Clean State

A returned `connection` has to be ready for a completely different, unrelated request to borrow next, which means it must never be handed back mid-`transaction` or holding onto leftover session state from whatever the previous request was doing.

```postgresql with=init.sql
BEGIN;
UPDATE shipments SET status = 'cancelled' WHERE shipment_id = 2;
-- Imagine the connection being returned to the pool right here, before COMMIT or ROLLBACK.

SELECT pid, state FROM pg_stat_activity WHERE state = 'idle in transaction';
```

Expected observation: PostgreSQL returns live server metadata. Values differ across OneCompiler runs, so verify the meaning of each column and the trend described below rather than matching a fixed number.

The "idle in `transaction`" danger covered in the previous lesson becomes especially serious in a pooled setup: a `connection` returned to the pool while still mid-`transaction` would hand the next, completely unrelated request a `connection` that is unexpectedly holding `lock`s and half-finished work from a previous, unrelated operation, a bug that can be extremely confusing to track down.

This makes the bug hard to trace, because the request seeing the strange behavior is not the request that caused it.

```postgresql with=init.sql
ROLLBACK;
```

Expected result: `ROLLBACK` discards shipment 2's uncommitted `'cancelled'` update and releases its `lock`s, returning the `connection` to a clean state, exactly what must happen before that `connection` goes back into the pool for another request to borrow.

![A pooled connection must be returned clean, with no open transaction or leftover locks](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_return_pooled_connection_clean.png)

## Pool Size Is a Deliberate Trade-off

A pool that is too small forces requests to wait for a `connection` to become available, adding latency under load. A pool that is too large risks exhausting the `database`'s `max_connections` limit, especially once multiple application instances each maintain their own pool against the same `database` server.

```postgresql with=init.sql
SELECT usename, count(*) AS connections_per_user
FROM pg_stat_activity
GROUP BY usename;
```

Expected observation: PostgreSQL returns live server metadata. Values differ across OneCompiler runs, so verify the meaning of each column and the trend described below rather than matching a fixed number.

In a real production setup, this kind of `query`, grouping open `connections` by which application or user opened them, is a standard way to monitor whether pool sizes across an organization's various services are collectively approaching the `database`'s overall `connection` ceiling, since `max_connections` is a single, shared limit across every application talking to that `database`, not a per-application allowance.

## Connection Pooling at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Without pooling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new connection opened and closed per request, paying full connection cost every time</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">With pooling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A fixed set of connections reused across many requests, borrowed and returned</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>max_connections</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The database server&#x27;s hard ceiling on simultaneous connections, shared across all applications</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pool size trade-off</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too small adds waiting; too large risks exhausting the server&#x27;s connection limit</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Returning a connection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Must be in a clean state, no open transaction, no leftover session state</td>
    </tr>
  </tbody>
</table>

## Your Turn

Check the current `max_connections` setting and the current number of active `connections`, then write a comment estimating what percentage of the limit is currently in use.

```postgresql with=init.sql
-- Write your queries and comment below
```

Running `SHOW max_connections;` alongside `SELECT count(*) FROM pg_stat_activity;` gives both numbers needed to compute this percentage directly; in a real production system, alerting is typically configured once this percentage crosses a threshold like 80%, giving operators time to investigate before `connections` actually start being refused.

## Conclusion

`Connection pooling` reuses a fixed set of already-open `connections` across many requests instead of opening and closing one per request, avoiding both the repeated `connection` cost and the risk of exhausting the `database`'s shared `max_connections` limit, with careful attention needed to ensure a `connection` is always returned to the pool in a clean, `transaction`-free state. The next lesson steps back to compare two fundamentally different styles of writing the `database`-facing code that actually runs on top of these `connections`: raw SQL and an object-relational mapper.
