# DBMS 8.4: Database Administration Basics — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Going to Production
- **Chapter:** Database Administration Basics
- **Scope:** Database Maintenance; Backup Strategies; Restore and Recovery; Database Monitoring; Replication and Read Replicas
- **SQL dialect:** PostgreSQL
- **Format:** Four plausible options with exactly one best answer
- **Is Curriculum Based:** No
- **Coverage rule:** Questions 1–10 collectively cover all five chapter subtopics.
- **Design standard:** Questions depend on operational metrics, command effects, timelines, recovery requirements, or production constraints.
- **Answer-quality controls:** A/B/C/D are each correct exactly 10 times; no answer letter occurs more than twice consecutively.

---

## Questions

### 1. Four thousand updates enlarge the table

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Maintenance  
**Is Curriculum Based:** No  
**Assessment type:** Explaining unexpected physical behaviour

Updating 4,000 of 5,000 shipment rows increases relation size although no logical row was added.

Which explanation fits PostgreSQL MVCC?

A. UPDATE duplicates the entire table definition.  
B. Every update creates a new index automatically.  
C. New row versions are written while obsolete versions remain as dead tuples.  
D. ANALYZE copies all rows before estimating them.

### 2. A portable copy for another environment

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Backup Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a backup type

A team needs a portable schema-and-data backup that can be replayed on another compatible environment.

Which choice is most appropriate?

A. A logical backup produced by `pg_dump`  
B. A cache-hit-ratio snapshot  
C. `VACUUM FULL` output  
D. A read replica without retained backups

### 3. Recovering to one minute before the mistake

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Restore and Recovery  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a recovery approach

At 14:32 an accidental uncommitted rollback is impossible because a destructive statement already committed. The business wants the database state at 14:31:59, not last night’s state.

Which recovery design is required?

A. Plain VACUUM of the damaged table  
B. Only last night’s logical dump  
C. Promotion of any replica regardless of replay position  
D. A prior full backup plus archived WAL replayed to the target time

### 4. Connections approach the server ceiling

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Monitoring  
**Is Curriculum Based:** No  
**Assessment type:** Choosing monitoring evidence

Which comparison provides an early warning that new connections may soon be refused?

A. Live tuples versus dead tuples  
B. `count(*)` from `pg_stat_activity` versus `max_connections`  
C. Cache hits versus WAL position  
D. Full backups versus incremental backups

### 5. A dashboard reads slightly old totals

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Replication and Read Replicas  
**Is Curriculum Based:** No  
**Assessment type:** Explaining replica behaviour

A write commits on the primary. A dashboard routed to a replica immediately omits it, then displays it moments later.

What caused the temporary difference?

A. The primary rolled back the write.  
B. VACUUM hid the row.  
C. The replica had not yet replayed the corresponding WAL records.  
D. Logical backups update replicas on a schedule.

### 6. Reusable space without a visibly smaller file

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Maintenance  
**Is Curriculum Based:** No  
**Assessment type:** Correcting a maintenance expectation

After plain `VACUUM shipments`, dead space becomes reusable but the operating-system file barely shrinks.

Which conclusion is correct?

A. This is normal; plain VACUUM favors internal reuse over returning disk space immediately.  
B. VACUUM only refreshes optimizer statistics.  
C. Dead tuples can never be reclaimed.  
D. The command created a physical backup.

### 7. Logical versus physical evidence

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Backup Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two backup implementations

Version L stores portable SQL/data. Version P copies PostgreSQL’s underlying data files and is tied more closely to server version.

Which mapping is correct?

A. L is incremental; P is full.  
B. L is logical; P is physical.  
C. L is replication; P is monitoring.  
D. L is VACUUM; P is ANALYZE.

### 8. A backup file exists, but confidence does not

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Restore and Recovery  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a validation approach

Nightly backup jobs report success. No backup has ever been restored.

Which next practice supplies real evidence of recoverability?

A. Retain only the newest file.  
B. Periodically restore into isolation and verify rows, constraints, and indexes.  
C. Run ANALYZE against the backup file.  
D. Route production reads to the backup.

### 9. Dead tuples keep rising

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Monitoring  
**Is Curriculum Based:** No  
**Assessment type:** Diagnosing a maintenance trend

For one busy table, `dead_tuple_percent` rises every day and `last_autovacuum` remains old.

Which operational concern is best supported?

A. Replication is perfectly current.  
B. Backup retention is too long.  
C. Cache hit ratio must be 100%.  
D. Maintenance is not keeping pace with write activity.

### 10. Scaling reads versus surviving primary failure

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Replication and Read Replicas  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two replication goals

Which pairing is accurate?

A. Directing tolerant reports to replicas scales reads; promoting a standby supports availability.  
B. Both actions are backup retention policies.  
C. Read replicas accept every write while the primary is healthy.  
D. Failover eliminates all possible replication lag.

### 11. Refreshing optimizer information

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Maintenance  
**Is Curriculum Based:** No  
**Assessment type:** Completing a maintenance action

A bulk load radically changes value distribution. Which command refreshes the statistics used by the optimizer?

A. `VACUUM FULL shipments;`  
B. `ANALYZE shipments;`  
C. `pg_dump shipments;`  
D. `REFRESH REPLICA shipments;`

### 12. Choosing the maintenance window operation

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Maintenance  
**Is Curriculum Based:** No  
**Assessment type:** Evaluating a lock trade-off

A severely bloated table must visibly return disk space to the operating system. An exclusive lock is acceptable during a scheduled outage.

Which operation matches?

A. Plain ANALYZE  
B. Plain VACUUM  
C. Autovacuum only  
D. `VACUUM FULL`

### 13. Autovacuum’s normal role

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Maintenance  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the appropriate structure

Why is manual VACUUM not required after every ordinary update?

A. Autovacuum normally performs routine vacuuming and analysis after thresholds are crossed.  
B. Updates never create dead tuples.  
C. Read replicas remove dead tuples from the primary.  
D. Backups automatically shrink tables.

### 14. The incremental chain is incomplete

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Backup Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Identifying an unreachable restore

A restore needs last Sunday’s full backup plus daily incremental changes through Thursday. Wednesday’s incremental is missing.

What is the central problem?

A. Thursday contains the entire database automatically.  
B. The recovery chain cannot reliably reconstruct Thursday without the missing segment.  
C. Sunday’s full backup can infer Wednesday’s writes.  
D. ANALYZE regenerates the missing backup.

### 15. Frequency follows acceptable data loss

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Backup Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a backup boundary

Business policy permits losing at most 15 minutes of committed data.

Which strategy consideration follows most directly?

A. Keep only one monthly full backup.  
B. Place backups on the same disk.  
C. Capture changes often enough that the recoverable gap is no more than 15 minutes.  
D. Run VACUUM every 15 minutes instead.

### 16. Same disk, same failure

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Backup Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a backup-location defect

The live database and all backups reside on one physical disk.

Why is this misleading protection?

A. Logical backups require SSDs.  
B. Physical backups cannot store rows.  
C. Replicas must share that disk.  
D. One media failure can destroy both live data and every backup.

### 17. Restoring a logical dump

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Restore and Recovery  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the restore method

How is a plain `pg_dump` script normally restored?

A. Run its schema and data statements against a target database, commonly through `psql`.  
B. Replay only cache-hit statistics.  
C. Copy the `pg_stat_activity` view.  
D. Promote the dump file as a replica.

### 18. Verification must inspect more than row count

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Restore and Recovery  
**Is Curriculum Based:** No  
**Assessment type:** Choosing a correct validation approach

A test restore has the expected number of rows. What additional checks make the test stronger?

A. Confirm only the filename date.  
B. Spot-check values and verify constraints and indexes were rebuilt.  
C. Delete the source backup immediately.  
D. Compare connection pool sizes.

### 19. PITR needs durable history

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Restore and Recovery  
**Is Curriculum Based:** No  
**Assessment type:** Completing a recovery prerequisite

Why must WAL segments after the full backup be archived durably for point-in-time recovery?

A. They store user passwords.  
B. They shrink dead tuples.  
C. They provide the ordered changes to replay from the backup to the target moment.  
D. They replace all full backups permanently.

### 20. Monitoring is a trend, not one lucky snapshot

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Monitoring  
**Is Curriculum Based:** No  
**Assessment type:** Comparing monitoring implementations

Version X checks connection usage once after an outage. Version Y samples and alerts on percentage used continuously.

Which advantage does Y provide?

A. It guarantees connections can never fail.  
B. It performs automatic point-in-time recovery.  
C. It removes the server limit.  
D. It can reveal a worsening leak before the ceiling is reached.

### 21. Computing connection pressure

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Monitoring  
**Is Curriculum Based:** No  
**Assessment type:** Calculating a monitored value

`pg_stat_activity` contains 72 connections and `max_connections` is 90. What percentage is used?

A. 80%  
B. 18%  
C. 72%  
D. 125%

### 22. A falling cache-hit ratio

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Monitoring  
**Is Curriculum Based:** No  
**Assessment type:** Interpreting a trend

Cache hit ratio steadily falls while disk reads rise as the working set grows.

Which capacity concern is most plausible?

A. WAL archives are too portable.  
B. Available memory may no longer fit the active working set well.  
C. All indexes have become unique.  
D. Restore tests are running too rarely.

### 23. The query is waiting, not computing

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Monitoring  
**Is Curriculum Based:** No  
**Assessment type:** Tracing wait evidence

`pg_stat_activity` shows a long runtime and a lock-related `wait_event_type`.

What should the investigator infer first?

A. The query is definitely missing a backup.  
B. The cache ratio is exactly zero.  
C. Lock contention, not only CPU work, is delaying the query.  
D. Replication has promoted itself.

### 24. Why thresholds must match the workload

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Monitoring  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a correct alerting approach

A report normally runs 20 seconds, while checkout queries normally run under 100 ms.

Which monitoring policy is most appropriate?

A. Alert on every query lasting over 100 ms.  
B. Never alert on duration.  
C. Use one one-hour threshold for all SQL.  
D. Set reasonable duration thresholds by workload rather than one universal number.

### 25. WAL flows from primary to replica

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Replication and Read Replicas  
**Is Curriculum Based:** No  
**Assessment type:** Completing a replication flow

Which sequence describes streaming replication?

A. Replica generates writes, primary deletes them.  
B. Primary generates WAL; replicas receive and replay it in order.  
C. Backups query the replica for passwords.  
D. VACUUM copies tables between servers.

### 26. Measuring lag in bytes

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Replication and Read Replicas  
**Is Curriculum Based:** No  
**Assessment type:** Interpreting WAL positions

For a replica, `sent_lsn` is ahead of `replay_lsn`.

What does the difference represent?

A. Free disk space on the primary  
B. Number of active connections  
C. WAL sent by the primary but not yet replayed on that replica  
D. Count of dead tuples

### 27. Routing a freshness-sensitive read

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Replication and Read Replicas  
**Is Curriculum Based:** No  
**Assessment type:** Selecting a correct routing approach

A user creates a shipment and the next screen must immediately confirm it.

Where should that freshness-sensitive read go?

A. The primary, unless the application has a stronger replica-consistency mechanism  
B. Any lagging replica chosen at random  
C. Last night’s logical backup  
D. The autovacuum worker

### 28. A replica is not a backup strategy by itself

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Replication and Read Replicas  
**Is Curriculum Based:** No  
**Assessment type:** Spotting a reliability logic bug

An operator says, “We can stop backups because every primary change reaches the replica.”

Why is this unsafe?

A. Replicas never contain tables.  
B. Replication cannot serve reads.  
C. Replicas do not use WAL.  
D. Accidental destructive changes can also replicate; backups preserve recoverable history.

### 29. Promotion changes the availability role

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Replication and Read Replicas  
**Is Curriculum Based:** No  
**Assessment type:** Identifying failover behaviour

The primary fails and an adequately caught-up standby is promoted.

What purpose of replication is being exercised?

A. Logical portability  
B. Table vacuuming  
C. Availability through failover  
D. Query parameterization

### 30. Physical backup suitability

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Backup Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Selecting an appropriate backup structure

A huge database needs fast whole-cluster backup and restore on the same PostgreSQL version; cross-version portability is not required.

Which choice is the natural candidate?

A. A physical backup such as `pg_basebackup`  
B. CSV export of one table only  
C. Cache statistics  
D. An untested materialized view

### 31. Full versus incremental trade-off

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Backup Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Comparing two backup versions

Which statement correctly compares them?

A. Incremental restores need no earlier backup.  
B. Full backups are simpler; incremental backups save repeated time/storage but require a chain.  
C. Full backups contain only changed pages.  
D. Incremental backups are always more portable than logical dumps.

### 32. A manual batch-maintenance decision

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Maintenance  
**Is Curriculum Based:** No  
**Assessment type:** Selecting the smallest correct action

A one-off bulk load changed millions of values, and plan quality must be accurate immediately rather than waiting for autovacuum.

Which targeted action is most direct?

A. Promote a replica.  
B. Delete the WAL archive.  
C. Restore last night’s backup.  
D. Run `ANALYZE` on the affected table.

### 33. Dead tuple percentage boundary

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Monitoring  
**Is Curriculum Based:** No  
**Assessment type:** Calculating a health metric

A table has 8,000 live and 2,000 dead tuples. Using `dead / (live + dead)`, what is the dead-tuple percentage?

A. 25%  
B. 20%  
C. 80%  
D. 2%

### 34. One restore test exposes corruption

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Restore and Recovery  
**Is Curriculum Based:** No  
**Assessment type:** Evaluating backup evidence

Backup A exists and passed no restore test. Backup B was restored in isolation and verified against known counts and values.

Which assessment is strongest?

A. A is safer because it was never altered by a restore.  
B. Both are equally proven because files exist.  
C. B provides evidence of recoverability; A remains unverified.  
D. A can support PITR without WAL.

### 35. Monitoring the five worst bloat candidates

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Monitoring  
**Is Curriculum Based:** No  
**Assessment type:** Completing monitoring SQL

Which ordering surfaces tables with the most dead tuples first?

A. `ORDER BY n_dead_tup DESC LIMIT 5`  
B. `ORDER BY relname LIMIT 5`  
C. `ORDER BY n_live_tup ASC LIMIT 5`  
D. `GROUP BY max_connections`

### 36. A maintenance command that blocks routine traffic

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Maintenance  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an input condition that exposes risk

When is `VACUUM FULL` most likely to cause unacceptable behaviour?

A. On an offline test table  
B. During a planned exclusive maintenance window  
C. On an empty development table  
D. On a busy live table whose reads and writes cannot tolerate its exclusive lock

### 37. Replica monitoring source

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Replication and Read Replicas  
**Is Curriculum Based:** No  
**Assessment type:** Selecting operational evidence

Which primary-side view lists connected replicas and their sent/replayed WAL positions?

A. `pg_stat_user_tables`  
B. `information_schema.columns`  
C. `pg_stat_replication`  
D. `pg_statio_user_tables`

### 38. Restore target after a noon deletion

**Difficulty:** Intermediate  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Restore and Recovery  
**Is Curriculum Based:** No  
**Assessment type:** Choosing an exact recovery boundary

A valid batch completes at 11:58; an accidental deletion commits at 12:00.

What PITR target best preserves the batch while excluding the deletion?

A. Before the 11:58 batch  
B. Exactly after replaying the deletion  
C. A moment after 11:58 but before 12:00  
D. Any time after 12:00

### 39. Cache ratio calculation

**Difficulty:** Foundational  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Database Monitoring  
**Is Curriculum Based:** No  
**Assessment type:** Calculating a monitored value

Statistics show 9,500 cache hits and 500 disk reads. What is `hits / (hits + reads)`?

A. 5%  
B. 50%  
C. 90%  
D. 95%

### 40. A complete operational design

**Difficulty:** Advanced  
**Subject:** DBMS  
**Topic:** Going to Production  
**Subtopic:** Replication and Read Replicas  
**Is Curriculum Based:** No  
**Assessment type:** Applying multiple administration concepts

A production database needs routine health upkeep, recoverability to a recent moment, early warnings, read scaling, and standby availability.

Which design is strongest?

A. Autovacuum/ANALYZE, tested off-server backups plus archived WAL, continuous monitoring, and monitored replicas with lag-aware routing  
B. One same-disk backup, no restore tests, and all reads on an unmonitored replica  
C. Weekly VACUUM FULL during peak traffic and no WAL archive  
D. Replication alone, because it replaces maintenance, backups, and monitoring

---

## Instructor Key

### 1. C
MVCC preserves obsolete row versions temporarily, so heavy updates can create dead tuples and physical growth.
### 2. A
`pg_dump` captures a portable logical representation of schema and data.
### 3. D
PITR restores a base backup and replays archived WAL only to the chosen pre-incident moment.
### 4. B
Current sessions as a percentage of the configured ceiling directly measures connection pressure.
### 5. C
Replication is asynchronous enough that replay may briefly trail the primary’s commit.
### 6. A
Plain VACUUM marks space reusable internally; file shrinkage is not its required visible result.
### 7. B
Logical backups represent data/schema portably; physical backups copy PostgreSQL files.
### 8. B
A real isolated restore plus structural and data checks tests whether recovery can actually succeed.
### 9. D
Rising dead tuples and stale autovacuum evidence indicate cleanup is falling behind.
### 10. A
Read routing addresses scale, while promotion of a standby addresses primary failure.
### 11. B
ANALYZE updates the optimizer statistics affected by the bulk load.
### 12. D
VACUUM FULL rewrites and shrinks the table but requires the accepted exclusive lock.
### 13. A
Autovacuum automates routine VACUUM and ANALYZE work after configured thresholds.
### 14. B
Incremental recovery depends on an unbroken sequence after the full starting backup.
### 15. C
The recoverable history must be captured frequently enough to honor the maximum acceptable loss.
### 16. D
Co-locating copies leaves both exposed to the same physical failure.
### 17. A
A logical dump is restored by executing its object-creation and data-loading content on the target.
### 18. B
Correct counts alone do not prove values, constraints, and indexes were restored correctly.
### 19. C
Archived WAL supplies every ordered change between the base backup and target time.
### 20. D
Continuous sampling exposes the approach toward failure rather than observing only the aftermath.
### 21. A
`72 / 90 × 100 = 80%`.
### 22. B
More disk reads and fewer cache hits can indicate memory pressure relative to the working set.
### 23. C
A lock wait event distinguishes waiting on concurrency from simply spending time computing.
### 24. D
Useful thresholds reflect each workload’s legitimate runtime rather than generating noise or missing incidents.
### 25. B
The primary emits WAL and replicas replay the same ordered records to converge on its state.
### 26. C
The gap is WAL already sent but not yet applied by that replica.
### 27. A
Primary reads avoid the ordinary stale-read window immediately after a write.
### 28. D
Replication can copy mistakes quickly; independent retained backups support recovery to earlier history.
### 29. C
Promoting a standby replaces a failed primary, which is the availability use of replication.
### 30. A
Physical backup is suitable for fast same-version whole-cluster recovery at large scale.
### 31. B
Full copies simplify restoration; incremental efficiency comes with chain dependency.
### 32. D
Immediate plan accuracy after a major change calls for targeted ANALYZE.
### 33. B
`2,000 / 10,000 = 20%`.
### 34. C
B has been exercised and checked; A’s existence alone does not demonstrate successful restoration.
### 35. A
Descending dead-tuple count places the largest cleanup candidates first.
### 36. D
The exclusive lock conflicts most severely with uninterrupted traffic on a busy live table.
### 37. C
`pg_stat_replication` exposes each connected replica’s state and WAL progress from the primary.
### 38. C
The target must include the valid batch while stopping before the destructive commit.
### 39. D
`9,500 / 10,000 = 95%`.
### 40. A
The combined design addresses maintenance, verified recovery history, proactive detection, read scale, lag, and failover.

---

## Coverage summary

| Subtopic | Questions |
|---|---|
| Database Maintenance | 1, 6, 11, 12, 13, 32, 36 |
| Backup Strategies | 2, 7, 14, 15, 16, 30, 31 |
| Restore and Recovery | 3, 8, 17, 18, 19, 34, 38 |
| Database Monitoring | 4, 9, 20, 21, 22, 23, 24, 33, 35, 39 |
| Replication and Read Replicas | 5, 10, 25, 26, 27, 28, 29, 37, 40 |
