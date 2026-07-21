## Introduction

Every lesson in this course has run against a single `database` server.

A production system serving real, sustained traffic eventually outgrows what one server can comfortably handle, and it also cannot afford for that one server to be a single point of total failure. **Replication** addresses both concerns: continuously copying a `database`'s changes to one or more additional servers, called `replicas`, which can take over if the primary fails, and can also absorb read traffic that would otherwise all fall on a single machine.

**Definition:** Replication streams a primary `database`'s `write-ahead log` to one or more `replicas`, which replay it to stay continuously in sync, enabling both read scaling, directing tolerant read traffic away from the primary, and availability, standing ready to take over if the primary fails, at the cost of a small, measurable lag that every application using a `replica` has to account for.

![Intro visual for replication and read replicas](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_intro_replication_and_read_replicas.png)

## How Streaming Replication Works, Conceptually

PostgreSQL's standard replication approach relies on exactly the mechanism covered in the `recovery` unit: the `write-ahead log`. A `replica` continuously receives the same `WAL` records the primary server generates, and replays them, effectively performing the same redo process `recovery` uses after a crash, except continuously, in near real time, against a running, healthy primary.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `shipments`

| shipment_id | status |
| --- | --- |
| 1 | in_transit |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status) VALUES (1, 'in_transit');
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahake" 
 width="100%"
></iframe>

Expected result: PostgreSQL returns the rows described below. Compare the visible columns and row-level effect with the explanation, since security and administration settings may make some values environment-dependent.

Every change made on the primary, this `INSERT` included, generates `WAL` records exactly as covered in the `recovery` unit. In a replicated setup:

1. Those same records are streamed to every `replica`.

2. Each `replica` applies them in the same order, arriving at the identical data a moment later.

This is why replication is often described as `recovery`'s mechanism, run continuously against a live server rather than only after a crash.

![Streaming replication sends WAL from the primary to replicas, which replay it](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_streaming_replication_wal_to_replicas.png)

## Monitoring Replication from the Primary

A running PostgreSQL primary tracks every connected `replica` directly, exposing exactly how far behind each one currently is.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahavb" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns live server metadata. Values differ across OneCompiler runs, so verify the meaning of each column and the trend described below rather than matching a fixed number.

- `pg_stat_replication` would list one `row` per connected `replica` in a real replicated deployment
- this example environment has none connected, so the `query` returns no `rows`, but the `columns` themselves describe exactly what matters: `sent_lsn` is how far the primary has sent `WAL`, `replay_lsn` is how far a given `replica` has actually applied it, and the difference between them is `replication lag`, the gap between "happened on the primary" and "visible on this `replica`."

## Why Replication Lag Matters

Because a `replica` applies changes slightly after the primary generates them, there is always some delay, however small, between a change committing on the primary and that same change becoming visible on a `replica`. A `query` reading from a `replica` can, in principle, see slightly stale data, a deliberate trade-off in exchange for spreading read load across more than one server.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahb65" 
 width="100%"
></iframe>

Expected output:

| status | count |
| --- | ---: |
| in_transit | 1 |

This is why `replicas` are typically used for read traffic that can tolerate a small amount of staleness, dashboards, analytics, reporting, exactly the kind of workload this course has repeatedly used as its running examples, while writes, and any read that absolutely requires the most current possible data, continue to go to the primary.

![Writes go to the primary, while read-heavy dashboards can query replicas with some lag](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_read_replicas_reads_primary_writes_lag.png)

## Read Replicas for Scaling, Failover for Availability

Replication serves two distinct purposes that are worth keeping separate. Using `replicas` to absorb read traffic, spreading load across several machines so no single server bears the full weight of every `query`, is a scaling strategy. Using a `replica` as a standby ready to be promoted to primary if the original primary fails is an availability strategy, protecting against the single point of failure a lone `database` server represents.

A well-designed production deployment often uses replication for both purposes simultaneously, the same `replicas` serving read traffic day to day while also standing ready to take over if the primary ever goes down.

## Replication and Read Replicas at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mechanism</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Streaming the same write-ahead log a crashed server would use for recovery</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>pg_stat_replication</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shows each connected replica&#x27;s status and lag, from the primary&#x27;s side</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replication lag</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The gap between a change committing on the primary and appearing on a replica</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read replica use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scaling read-heavy workloads that can tolerate slight staleness</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Standby/failover use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Availability, promoting a replica to primary if the original fails</td>
    </tr>
  </tbody>
</table>

## Your Turn

Write the `query` that would report `replication lag` in seconds rather than bytes, using `pg_stat_replication`'s `replay_lag` `column`, and add a comment explaining why a reporting dashboard might be deliberately directed to `query` a `replica` instead of the primary.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahbfu" 
 width="100%"
></iframe>

Expected result and verification:

- `SELECT client_addr, replay_lag FROM pg_stat_replication;` reports lag as a time interval directly
- a reporting dashboard is a strong candidate for querying a `replica` because its workload is read-only and can comfortably tolerate a few seconds of staleness, freeing the primary to dedicate its full capacity to the writes and time-sensitive reads that genuinely need up-to-the-moment accuracy.

## Conclusion

Replication streams a primary `database`'s `write-ahead log` to one or more `replicas`, which replay it to stay continuously in sync, enabling both read scaling, directing tolerant read traffic away from the primary, and availability, standing ready to take over if the primary fails, at the cost of a small, measurable lag that every application using a `replica` has to account for.

This closes out the operational picture this course has built lesson by lesson: from what data and a `database` even are, through `tables`, keys, and relationships, through SQL itself, through `join`s, aggregation, and advanced querying, through the transactional and concurrent guarantees that keep data trustworthy, through the performance techniques that keep `queries` fast, and finally through the programmability, security, and operational discipline a real, production `database` runs on every single day.
