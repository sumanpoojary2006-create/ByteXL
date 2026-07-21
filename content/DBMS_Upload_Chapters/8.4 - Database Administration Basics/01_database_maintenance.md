## Introduction

Every `UPDATE` and `DELETE` covered across this entire course has been described as if the old row's space simply disappears the moment the statement finishes.

In PostgreSQL specifically, that is not quite what happens: an updated or deleted row's old version is marked as no longer current, but its physical space is not immediately reclaimed, since other concurrent transactions, under the isolation guarantees covered in an earlier unit, might still need to see that older version.

Left unmanaged, this leftover space accumulates, and **database maintenance** is the ongoing work of cleaning it up, keeping a production database healthy as it runs for months and years, not just correct at the moment each query executes.

**Definition:** Because PostgreSQL keeps old row versions around to support concurrent, isolated reads, routine maintenance, reclaiming dead tuple space with `VACUUM` and keeping the optimizer's statistics current with `ANALYZE`, is essential to keeping a database healthy over time, and autovacuum handles this automatically for the large majority of real-world cases without manual intervention.

![Intro visual for database maintenance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_database_maintenance.png)

## Why Updates and Deletes Leave Behind Dead Rows

PostgreSQL's approach to updates, called `MVCC`, multiversion concurrency control, is what makes isolation between concurrent transactions possible in the first place, and it has a direct physical consequence.

## Source Data Used in This Lesson

Some lessons need a larger dataset to make execution plans or maintenance behavior visible. For those tables, `init.sql` generates the rows instead of listing every row manually.

### Generated `shipments` dataset

| Column | Definition in the setup |
| --- | --- |
| `shipment_id` | `INTEGER PRIMARY KEY` |
| `status` | `TEXT` |

The setup generates 5,000 rows, numbered from 1 through 5000. This scale is intentional because performance behavior is difficult to observe on a tiny table.

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY,
    status TEXT
);

INSERT INTO shipments (shipment_id, status)
SELECT i, 'in_transit' FROM generate_series(1, 5000) AS i;
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahbrv" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns live server metadata. Values differ across OneCompiler runs, so verify the meaning of each column and the trend described below rather than matching a fixed number.

Even though this `UPDATE` did not add a single new row, the table's physical size grows. Here is why:

- PostgreSQL writes each updated row as a new version alongside the old one, rather than overwriting it in place.
- The old, no-longer-current versions, called dead tuples, keep occupying disk space until something explicitly reclaims it.

![VACUUM cleans up dead tuples and marks their space reusable](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_dead_tuples_vacuum_reusable_space.png)

## Reclaiming Space with VACUUM

`VACUUM` is the command that scans a table for dead tuples and marks their space as reusable for future inserts and updates.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahc74" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns live server metadata. Values differ across OneCompiler runs, so verify the meaning of each column and the trend described below rather than matching a fixed number.

- A plain `VACUUM` marks dead space as reusable for this table's own future writes, without necessarily shrinking the file on disk immediately, since PostgreSQL generally prefers to reuse that reclaimed space internally rather than pay the cost of physically returning it to the operating system.
- `VACUUM FULL` goes further, actually rewriting the table to reclaim disk space visibly, at the cost of locking the table exclusively while it runs, which is why `VACUUM FULL` is typically reserved for planned maintenance windows rather than run routinely against a live, busy table.

## Keeping Statistics Current with ANALYZE

The `query optimizer`, covered in the performance unit, relies on table and column statistics to estimate costs and choose plans, and those statistics do not update themselves automatically after a large batch of changes.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahcfx" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns live server metadata. Values differ across OneCompiler runs, so verify the meaning of each column and the trend described below rather than matching a fixed number.

- `ANALYZE` refreshes PostgreSQL's internal statistics about the table's data distribution, and `n_live_tup` and `n_dead_tup` in `pg_stat_user_tables` show, respectively, the estimated count of current, valid rows and dead, reclaimable rows PostgreSQL is currently tracking.
- Stale statistics, left unrefreshed after significant data changes, can mislead the optimizer into choosing a worse plan than it otherwise would, exactly the risk noted when the optimizer was first introduced.

![ANALYZE refreshes table statistics so the optimizer can choose better plans](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_analyze_fresh_stats_autovacuum.png)

## Autovacuum: Maintenance Running Automatically

Running `VACUUM` and `ANALYZE` manually after every change would be impractical, which is why PostgreSQL runs a background process, autovacuum, that performs both automatically once a table's dead-tuple count or data changes cross a configured threshold.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahcrp" 
 width="100%"
></iframe>

Expected observation: PostgreSQL returns live server metadata. Values differ across OneCompiler runs, so verify the meaning of each column and the trend described below rather than matching a fixed number.

- `autovacuum` reports whether this automatic background process is enabled, `on` by default in a standard PostgreSQL installation.
- Autovacuum handles routine maintenance for the vast majority of tables without any manual intervention at all; manual `VACUUM` or `ANALYZE` becomes relevant mainly for large, one-off batch operations where waiting for autovacuum's next scheduled pass is not acceptable, or for the exclusive-lock `VACUUM FULL` case, which autovacuum never performs on its own due to its locking cost.

## Database Maintenance at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concept</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dead tuples</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Old row versions left behind by <code>UPDATE</code>/<code>DELETE</code>, due to PostgreSQL&#x27;s MVCC design</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>VACUUM</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Marks dead tuple space as reusable; does not always shrink the file on disk</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>VACUUM FULL</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Physically reclaims disk space, but <code>lock</code>s the table exclusively while running</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ANALYZE</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refreshes statistics the query optimizer relies on</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Autovacuum</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A background process running <code>VACUUM</code> and <code>ANALYZE</code> automatically, on by default</td>
    </tr>
  </tbody>
</table>

## Your Turn

Delete a large portion of the `shipments` table, check `n_dead_tup` before running `VACUUM`, then run it and check again, confirming the dead tuple count drops.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahd2n" 
 width="100%"
></iframe>

Expected result and verification:

Running `DELETE FROM shipments WHERE shipment_id > 3000;` followed by `SELECT n_dead_tup FROM pg_stat_user_tables WHERE relname = 'shipments';` shows a large dead-tuple count; after `VACUUM shipments;`, the same query shows that count drop close to zero, confirming the space has been marked reusable.

## Conclusion

Because PostgreSQL keeps old row versions around to support concurrent, isolated reads, routine maintenance, reclaiming dead tuple space with `VACUUM` and keeping the optimizer's statistics current with `ANALYZE`, is essential to keeping a database healthy over time, and autovacuum handles this automatically for the large majority of real-world cases without manual intervention. With the mechanics of keeping a database clean covered, the next lesson turns to protecting its data against loss entirely, through backups.
