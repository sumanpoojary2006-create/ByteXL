## Introduction

Devraj's ordinary `view`s, covered so far in this chapter, always re-run their underlying query on every single `SELECT`, which is exactly what keeps them current, but it also means a `view` built on a genuinely expensive aggregate, summarizing millions of historical shipments, pays that full computation cost every single time anyone queries it, even if the underlying data has not changed in hours. A **`materialized view`** solves this by actually storing the query's result on disk, like a real table, and only recomputing it when explicitly refreshed, trading perfect freshness for dramatically faster reads.

## Creating a Materialized View

The setup mirrors the ordinary `view` from earlier in this chapter, but the underlying data here represents a much larger, slower-to-aggregate history.

```postgresql file=matview_demo.sql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    driver_id INTEGER,
    status TEXT,
    shipped_month DATE
);

INSERT INTO shipments (shipment_id, driver_id, status, shipped_month)
SELECT i, (i % 20) + 1,
       CASE WHEN i % 15 = 0 THEN 'delayed' ELSE 'delivered' END,
       DATE '2025-01-01' + ((i % 12) * INTERVAL '1 month')
FROM generate_series(1, 5000) AS i;
```

```postgresql with=matview_demo.sql
CREATE MATERIALIZED VIEW monthly_shipment_summary AS
SELECT shipped_month, COUNT(*) AS total_shipments,
       COUNT(*) FILTER (WHERE status = 'delayed') AS delayed_shipments
FROM shipments
GROUP BY shipped_month;

SELECT * FROM monthly_shipment_summary ORDER BY shipped_month;
```

`CREATE MATERIALIZED VIEW` does two things, in order:

1. Runs the aggregate query once, immediately.
2. Physically stores its result.

Selecting from `monthly_shipment_summary` afterward reads that stored result directly, the same way reading from a real table would, without recomputing the `GROUP BY` and `COUNT` over all 5000 rows again.

## A Materialized View Does Not Automatically Stay Current

Unlike an ordinary `view`, new data added to the underlying table does not appear in a `materialized view` until it is explicitly refreshed.

```postgresql with=matview_demo.sql
INSERT INTO shipments (shipment_id, driver_id, status, shipped_month)
VALUES (5001, 5, 'delayed', '2025-06-01');

SELECT * FROM monthly_shipment_summary WHERE shipped_month = '2025-06-01';
```

This new delayed shipment for June does not appear in `monthly_shipment_summary`'s June row, because the `materialized view` is still showing its stored result from when it was created, before this insert ever happened. This staleness is not a bug; it is the entire point of a `materialized view`, avoiding the cost of recomputing the aggregate on every read, in exchange for accepting that reads may be out of date until a refresh runs.

## Refreshing a Materialized View

`REFRESH MATERIALIZED VIEW` recomputes the stored result from scratch, bringing it back in line with the underlying tables' current state.

```postgresql with=matview_demo.sql
REFRESH MATERIALIZED VIEW monthly_shipment_summary;

SELECT * FROM monthly_shipment_summary WHERE shipped_month = '2025-06-01';
```

After the refresh, June's row correctly reflects the newly inserted delayed shipment. In a real production system, this refresh is typically scheduled, run every hour, every night, or after a known batch of data loads, rather than run manually, which is a deliberate design decision about how stale the summary is allowed to get before it matters.

## Refreshing Without Blocking Reads

A plain `REFRESH MATERIALIZED VIEW` `lock`s the `view` against reads while it recomputes, which can be a problem for a dashboard that needs to stay available. PostgreSQL supports a concurrent refresh option for this, at the cost of requiring a unique `index` on the `materialized view` first.

```postgresql with=matview_demo.sql
CREATE UNIQUE INDEX idx_monthly_summary_month ON monthly_shipment_summary (shipped_month);

REFRESH MATERIALIZED VIEW CONCURRENTLY monthly_shipment_summary;
```

`REFRESH MATERIALIZED VIEW CONCURRENTLY` recomputes the result in the background while the existing stored data remains fully readable, only swapping over once the new computation is complete, at the cost of taking somewhat longer overall than a plain refresh, since it has to do extra work to keep the old version available throughout.

## Ordinary Views vs. Materialized Views at a Glance

| | Ordinary `view` | Materialized `view` |
|---|---|---|
| Storage | None, recomputes every query | Stores the result physically |
| Freshness | Always current | Current as of the last refresh |
| Read cost | Full underlying query cost, every time | Fast, just reading stored data |
| Update mechanism | Automatic, implicit | Explicit `REFRESH`, on a schedule or on demand |

## Your Turn

Create a `materialized view` named `driver_shipment_totals` summarizing total shipment counts per driver, insert one more shipment, and confirm the `materialized view` is stale until refreshed.

```postgresql with=matview_demo.sql
-- Write your queries below
```

If your `materialized view` is `CREATE MATERIALIZED VIEW driver_shipment_totals AS SELECT driver_id, COUNT(*) AS total FROM shipments GROUP BY driver_id;`, inserting a new shipment for `driver_id = 5` does not change `driver_shipment_totals`'s count for driver 5 until `REFRESH MATERIALIZED VIEW driver_shipment_totals;` is explicitly run.

## Conclusion

A `materialized view` stores its query's result physically rather than recomputing it on every read, dramatically speeding up expensive aggregate or summary queries, at the cost of only being as current as its most recent explicit refresh, with `REFRESH MATERIALIZED VIEW CONCURRENTLY` available when the `view` needs to stay readable during that refresh. Devraj's monthly shipment dashboard can now load instantly, refreshed on a schedule that matches how current the business actually needs it to be. With `view`s and `materialized view`s both covered, the next lesson introduces reusable, callable procedures for logic that goes beyond a single query.
