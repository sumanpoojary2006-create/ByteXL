import random
import openpyxl

random.seed(184)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

DATABASE_MAINTENANCE = [
    (
        "Even though `UPDATE shipments SET status = 'delivered' WHERE shipment_id <= 4000;` does not add a single new row, the table's physical size grows afterward.\n\nWhy does the lesson say this happens, given how PostgreSQL handles updates?",
        "PostgreSQL writes each updated row as a new version alongside the old one, rather than overwriting it in place, and the old, no-longer-current versions, called dead tuples, keep occupying disk space until something explicitly reclaims it.",
        "easy", "understand", "database-maintenance",
        "PostgreSQL writes each updated row as a new version alongside the old one rather than overwriting in place, and the old versions (dead tuples) keep occupying space until reclaimed",
        ["The table grows because UPDATE always adds a duplicate row for backup purposes", "The table grows only because an index was automatically created during the update", "This growth is a bug specific to tables using generate_series for their initial data"],
    ),
    (
        "The old, no-longer-current row versions left behind by UPDATE or DELETE are called dead tuples, kept around because \"other concurrent transactions... might still need to see that older version.\"\n\nWhat mechanism does the lesson say is responsible for this behavior?",
        "MVCC, multiversion concurrency control, PostgreSQL's approach to updates that makes isolation between concurrent transactions possible in the first place, with dead tuples as its direct physical consequence.",
        "medium", "understand", "database-maintenance",
        "MVCC (multiversion concurrency control), which makes isolation between concurrent transactions possible, with dead tuples as its direct physical consequence",
        ["Autovacuum, which intentionally creates dead tuples before cleaning them up later", "Write-ahead logging, which duplicates every row for crash recovery purposes", "Connection pooling, which requires keeping old row versions for each pooled connection"],
    ),
    (
        "A plain `VACUUM shipments;` marks dead space as reusable but does not necessarily shrink the file on disk immediately, while `VACUUM FULL` \"goes further, actually rewriting the table to reclaim disk space visibly, at the cost of locking the table exclusively while it runs.\"\n\nWhy is VACUUM FULL typically reserved for planned maintenance windows rather than run routinely against a live, busy table?",
        "Its exclusive lock while running would block other activity on that table for the duration, so running it against a live, busy table risks disrupting normal operations, unlike a plain VACUUM which reuses reclaimed space internally without needing that exclusive lock.",
        "medium", "analyze", "database-maintenance",
        "Its exclusive lock blocks other activity on the table for the duration it runs, making it disruptive against a live, busy table unlike a plain VACUUM which avoids that exclusive lock",
        ["VACUUM FULL is reserved for maintenance windows only because it requires a password reset first", "VACUUM FULL is slower than plain VACUUM only because it also runs ANALYZE automatically", "There's no real reason for the distinction; both commands behave identically in production"],
    ),
    (
        "`ANALYZE shipments;` refreshes PostgreSQL's internal statistics about the table's data distribution, statistics the lesson says \"do not update themselves automatically after a large batch of changes.\"\n\nWhy does this matter for the query optimizer specifically, based on what the performance unit covered?",
        "The query optimizer relies on table and column statistics to estimate costs and choose plans, and stale statistics, left unrefreshed after significant data changes, can mislead the optimizer into choosing a worse plan than it otherwise would.",
        "medium", "apply", "database-maintenance",
        "The optimizer relies on these statistics to estimate costs and choose plans, so stale, unrefreshed statistics after major changes can mislead it into choosing a worse plan than it otherwise would",
        ["ANALYZE only affects how VACUUM FULL locks a table, with no connection to the optimizer at all", "Stale statistics cause queries to return incorrect results, not just worse-performing plans", "The optimizer ignores statistics entirely and always chooses the same plan regardless of ANALYZE"],
    ),
    (
        "`SHOW autovacuum;` reports whether the automatic background process is enabled, on by default in a standard PostgreSQL installation, running VACUUM and ANALYZE automatically once a table's dead-tuple count or data changes cross a configured threshold.\n\nAccording to the lesson, when does manual VACUUM or ANALYZE actually become relevant, given autovacuum handles the vast majority of tables automatically?",
        "Manual VACUUM or ANALYZE becomes relevant mainly for large, one-off batch operations where waiting for autovacuum's next scheduled pass is not acceptable, or for the exclusive-lock VACUUM FULL case, which autovacuum never performs on its own due to its locking cost.",
        "medium", "understand", "database-maintenance",
        "Manual intervention matters for large, one-off batch operations that can't wait for autovacuum's next pass, or for VACUUM FULL specifically, which autovacuum never runs on its own due to its locking cost",
        ["Manual VACUUM is required every single time, since autovacuum only handles ANALYZE, never VACUUM itself", "Manual intervention is never actually needed, since autovacuum performs VACUUM FULL automatically too", "Manual VACUUM is relevant only when a table has zero rows, since autovacuum skips empty tables"],
    ),
    (
        "The \"Your Turn\" exercise deletes a large portion of shipments, checks `n_dead_tup` before running VACUUM, then runs it and checks again, confirming the dead tuple count drops close to zero.\n\nWhat does this exercise directly demonstrate about VACUUM's effect?",
        "VACUUM scans a table for dead tuples left behind by DELETE (or UPDATE) and marks their space as reusable, which is why n_dead_tup drops sharply after VACUUM runs, reusable space no longer counted as dead.",
        "medium", "apply", "database-maintenance",
        "VACUUM scans for dead tuples and marks their space reusable, which is why n_dead_tup drops sharply after it runs, since that space is no longer counted as dead",
        ["It demonstrates that DELETE never actually creates any dead tuples in the first place", "It demonstrates that VACUUM permanently deletes the shipments table and must be recreated", "It demonstrates that n_dead_tup only tracks rows added by INSERT, not DELETE"],
    ),
    (
        "The \"Database Maintenance at a Glance\" table lists dead tuples, VACUUM, VACUUM FULL, ANALYZE, and autovacuum as five related concepts.\n\nAccording to that table, what specifically distinguishes plain VACUUM from VACUUM FULL in terms of disk space?",
        "VACUUM marks dead tuple space as reusable but does not always shrink the file on disk, while VACUUM FULL physically reclaims disk space, but locks the table exclusively while running.",
        "medium", "remember", "database-maintenance",
        "VACUUM marks dead space reusable without always shrinking the file on disk, while VACUUM FULL physically reclaims disk space but locks the table exclusively while running",
        ["VACUUM physically shrinks the file immediately, while VACUUM FULL only marks space as reusable", "Both commands behave identically; the only difference is that VACUUM FULL also runs ANALYZE afterward", "VACUUM FULL never actually reclaims any disk space; only plain VACUUM can do so"],
    ),
]

BACKUP_STRATEGIES = [
    (
        "The recovery mechanisms covered in an earlier unit (write-ahead logging, checkpoints, redo/undo) protect against a server crash where data files remain intact, but offer \"no protection at all\" against a disk physically destroyed or a table dropped by mistake with no transaction left open to roll back.\n\nWhat does the lesson say is \"the only real defense against losing data entirely\"?",
        "Having a separate copy of the data somewhere else, with a backup strategy being the deliberate plan for how, how often, and where that copy is kept.",
        "easy", "understand", "backup-strategies",
        "Having a separate copy of the data somewhere else, governed by a deliberate backup strategy covering how, how often, and where that copy is kept",
        ["Running VACUUM FULL more frequently to prevent any possibility of data loss", "Enabling row-level security on every table to protect against physical disk failure", "Increasing max_connections so more replicas can be connected simultaneously"],
    ),
    (
        "`pg_dump` produces a file that is described as \"at its core, a script\": running it against an empty database recreates every table, every constraint, and every row exactly as they existed at the moment the dump was taken.\n\nWhat category of backup is pg_dump, and what makes it distinct from a physical backup?",
        "pg_dump produces a logical backup, capturing the actual data and schema as a set of SQL statements or a portable data format, independent of the specific server it came from, unlike a physical backup which copies the database's actual underlying data files directly.",
        "easy", "understand", "backup-strategies",
        "pg_dump produces a logical backup, capturing data and schema as portable SQL/data independent of the specific server, unlike a physical backup which copies the actual data files directly",
        ["pg_dump produces a physical backup, since it copies the database's raw files exactly as stored on disk", "pg_dump only backs up table structures, never any actual row data", "pg_dump is distinct because it runs as SQL inside the database, not as an external command-line tool"],
    ),
    (
        "A physical backup, using a tool like pg_basebackup, is described as \"generally faster to produce and restore for very large databases,\" but \"tied to the exact same database version and is not as portable across different environments as a logical backup.\"\n\nWhat specifically explains why a physical backup is faster but less portable?",
        "It copies the database's actual underlying data files directly rather than translating them into portable SQL statements, skipping the translation work (which makes it faster) but tying the result to the exact same internal file structure and version (which makes it less portable).",
        "medium", "analyze", "backup-strategies",
        "It copies the actual data files directly, skipping SQL translation (making it faster) but tying the backup to the exact same internal file structure and version (making it less portable)",
        ["It's faster only because it excludes constraints and indexes entirely from the backup", "It's less portable only because pg_basebackup requires a graphical interface unavailable on some servers", "Physical backups are actually just as portable as logical backups; the lesson states no real difference"],
    ),
    (
        "A full backup captures the entire database every time it runs, while an incremental backup captures only what has changed since the last backup, at the cost of \"needing the full chain of backups, the last full one plus every incremental since, to perform a complete restore.\"\n\nWhat makes point-in-time, incremental backup strategies possible, according to the lesson?",
        "The write-ahead log position: rather than repeatedly copying the entire database, an incremental approach can archive just the log records generated since the last backup, later replaying them forward from a known full-backup starting point to reconstruct any specific moment in time.",
        "medium", "understand", "backup-strategies",
        "The write-ahead log, which lets an incremental approach archive just the log records since the last backup and replay them forward from a known starting point to reconstruct any specific moment",
        ["Incremental backups are made possible by disabling autovacuum during the backup window", "Incremental backups rely entirely on VACUUM FULL to compact the database before each backup", "Point-in-time strategies require converting every physical backup into a logical one first"],
    ),
    (
        "The \"Choosing a Backup Frequency and Retention Policy\" table lists backup location as a factor, noting \"storing a backup on the same server or disk as the live database defeats its purpose against a media failure entirely.\"\n\nWhy does storing a backup on the same disk as the live database specifically undermine its value against media failure?",
        "A media failure, like a disk being physically destroyed, would destroy both the live database and any backup stored on that same disk simultaneously, since a backup's purpose against this specific threat depends on it being physically separate from whatever could take out the original data.",
        "medium", "analyze", "backup-strategies",
        "A single media failure (like a destroyed disk) would destroy both the live database and a co-located backup at once, since protection against that threat requires the backup to be physically separate",
        ["It undermines the backup's value only because same-disk backups take longer to create", "It undermines the backup's value only because same-disk storage costs more than remote storage", "There's no real issue; the lesson states backup location doesn't meaningfully affect safety"],
    ),
    (
        "According to the \"Backup Strategies at a Glance\" table, what is a full backup \"best for,\" compared to what an incremental backup is best for?",
        "A full backup is best for simplicity, since it's the entire database every time, while an incremental backup is best for reduced time and storage cost specifically for frequent backups, since it only captures what changed since the last one.",
        "medium", "remember", "backup-strategies",
        "A full backup is best for simplicity; an incremental backup is best for reduced time and storage cost when backups are taken frequently",
        ["A full backup is best for reduced storage cost, while an incremental backup is best for simplicity, the reverse of their actual strengths", "Both are equally simple and equally storage-efficient, with no meaningful trade-off between them", "A full backup is best only for logical restores, and incremental backups are best only for physical restores"],
    ),
    (
        "The \"Choosing a Backup Frequency and Retention Policy\" table lists retention period as a factor, giving the example that \"a single accidental deletion discovered a week later needs a week-old backup still available.\"\n\nWhat does this example illustrate about how retention period should be decided?",
        "Retention period should reflect how far back a restore might genuinely be needed, since a problem isn't always discovered immediately, so keeping backups only briefly could mean the specific backup needed to recover from a delayed discovery no longer exists by the time it's needed.",
        "medium", "apply", "backup-strategies",
        "Retention should reflect how far back a restore might genuinely be needed, since a problem discovered after a delay requires a backup from before that delay to still exist",
        ["Retention period should always be set to exactly 24 hours regardless of the application", "The example illustrates that backup frequency and retention period are actually the same setting", "Retention period only matters for physical backups, never for logical ones like pg_dump"],
    ),
]

RESTORE_AND_RECOVERY = [
    (
        "The lesson opens by stating a backup that has never been tested by actually restoring it is \"in a very real sense, unverified: it might be corrupted, incomplete, or simply fail to apply cleanly,\" and that this discovery at the moment of genuine need is \"the worst possible time.\"\n\nWhat practice does the lesson insist restore and recovery should be, rather than something attempted for the first time during an emergency?",
        "It should be rehearsed deliberately, practiced ahead of time in a controlled setting, rather than attempted for the very first time during a real emergency when the stakes and pressure are highest.",
        "easy", "understand", "restore-and-recovery",
        "It should be rehearsed deliberately ahead of time, in a controlled setting, rather than attempted for the very first time during a genuine, high-pressure emergency",
        ["It should be automated entirely so no human ever needs to test or verify it manually", "It should only be performed once, immediately after the very first backup is taken", "It should be skipped entirely if the backup tool reports no errors during backup creation"],
    ),
    (
        "A logical restore, produced from a pg_dump backup, is described as running the dump's CREATE TABLE and data-loading statements \"directly against a fresh, empty target database.\"\n\nWhat does this process actually recreate, based on the lesson's description of what a logical restore does?",
        "Both the tables (structure) and the rows (data) get recreated, since the dump script contains both the CREATE TABLE statements defining structure and the data-loading statements reloading every row, run together against the fresh target.",
        "medium", "understand", "restore-and-recovery",
        "Both structure and data are recreated together, since the dump script contains CREATE TABLE statements plus data-loading statements run against the fresh target database",
        ["Only the table structure is recreated; the actual row data must be reloaded through a completely separate process", "Only the row data is recreated; the target database must already have matching tables created manually first", "Only indexes and constraints are recreated, with actual data intentionally left out of a logical restore"],
    ),
    (
        "The lesson explains that a full backup alone only restores to the exact moment it was taken, but a real incident like an accidental DELETE with no WHERE clause often needs recovery \"to a specific moment just before the mistake happened, not all the way back to last night's full backup, which would also lose every legitimate change made since then.\"\n\nHow does point-in-time recovery (PITR) solve this specific problem?",
        "PITR combines a full backup with the write-ahead log archive, replaying logged changes forward from that backup up to, but not including, the moment of the mistake, recovering to an exact point in time rather than only to the last full backup's fixed moment.",
        "medium", "apply", "restore-and-recovery",
        "PITR combines a full backup with the archived write-ahead log, replaying changes forward up to but not including the moment of the mistake, recovering to an exact point rather than only the last full backup's moment",
        ["PITR solves this by taking a new full backup automatically the instant a mistake is detected", "PITR solves this by preventing the accidental DELETE from running in the first place", "PITR only works if the mistake happened less than five seconds after the last full backup"],
    ),
    (
        "The lesson connects point-in-time recovery back to write-ahead logging, saying it's \"precisely why write-ahead logging... matters beyond crash recovery: the same log that lets a database recover from a power loss is what makes it possible to recover to an arbitrary moment in time.\"\n\nWhat condition does the lesson attach to this capability, regarding the WAL segments themselves?",
        "The relevant log segments must have been archived somewhere durable rather than discarded once no longer needed for ordinary crash recovery, since PITR depends on those historical WAL records still being available to replay.",
        "medium", "analyze", "restore-and-recovery",
        "The relevant WAL segments must be archived somewhere durable, rather than discarded once no longer needed for ordinary crash recovery, since PITR depends on those historical records being replayable",
        ["The condition is that autovacuum must be disabled for the entire duration the WAL segments are being generated", "The condition is that the primary server must remain online throughout the entire recovery process", "There is no condition; PITR works regardless of whether WAL segments were ever archived"],
    ),
    (
        "The lesson lists checking row counts, spot-checking specific known values, and confirming constraints and indexes rebuilt correctly as part of a disciplined restore-testing practice, calling skipping this verification \"one of the most common, and most costly, gaps in a team's backup strategy.\"\n\nWhy does the lesson consider a backup file that merely \"exists\" insufficient on its own?",
        "A backup file existing is not proof a restore will actually work, since corruption, an incomplete transfer, or a subtly incompatible database version can all silently break a backup's usefulness without ever showing an obvious error at backup time, leaving teams unaware their backups don't actually work until they're desperately needed.",
        "hard", "analyze", "restore-and-recovery",
        "A backup file existing doesn't prove a restore will work, since corruption, incomplete transfers, or version incompatibilities can silently break it without any obvious error at backup time, leaving teams unaware until it's desperately needed",
        ["A backup file is always sufficient on its own; the lesson only recommends testing as an optional extra step", "The concern only applies to physical backups, never to logical backups produced by pg_dump", "Verification is unnecessary once autovacuum confirms the backup completed without errors"],
    ),
    (
        "According to the \"Restore and Recovery at a Glance\" table, what does point-in-time recovery combine to \"recover to an exact moment\"?",
        "A full backup combined with archived WAL (write-ahead log), replaying the logged changes forward from that backup to reach any specific point in time rather than just the backup's own fixed moment.",
        "medium", "remember", "restore-and-recovery",
        "A full backup combined with archived write-ahead log (WAL), replaying changes forward from the backup to reach any specific point in time",
        ["A logical backup combined with a physical backup taken at the exact same moment", "Two full backups taken a fixed interval apart, interpolated to estimate the moment in between", "A backup combined with the database's current connection pool state at the time of restore"],
    ),
    (
        "The lesson describes a disciplined operations practice as periodically performing a real, full restore \"into a separate, isolated environment,\" rather than testing directly against the live production database.\n\nWhy does restoring into a separate, isolated environment matter for this kind of test?",
        "Testing in an isolated environment lets the restore be verified realistically without risking any disruption to the live, production database that real users and applications currently depend on, keeping the verification process itself safe.",
        "medium", "understand", "restore-and-recovery",
        "It lets the restore be verified realistically without risking any disruption to the live production database that real users and applications currently depend on",
        ["It matters only because pg_dump cannot run more than once against the same database", "Isolated environments are required because logical restores are illegal to run against production directly", "It matters only for physical restores; logical restores can safely be tested directly in production"],
    ),
]

DATABASE_MONITORING = [
    (
        "Every diagnostic tool used across the course, EXPLAIN ANALYZE, pg_stat_activity, pg_relation_size, has been reached for \"reactively, after a specific query was already suspected of being slow.\"\n\nHow does the lesson say database monitoring \"flips that around\"?",
        "Monitoring continuously watches key health metrics so a genuine problem, a connection pool nearing its limit, a table bloating with dead tuples, a query running slower than usual, is caught and addressed before it becomes an outage, rather than diagnosed only after users are already affected.",
        "easy", "understand", "database-monitoring",
        "Monitoring continuously watches health metrics so problems are caught and addressed before becoming an outage, rather than being diagnosed reactively only after a query is already suspected of being slow",
        ["Monitoring flips this around by replacing EXPLAIN ANALYZE entirely with a faster diagnostic tool", "Monitoring flips this around by disabling reactive diagnostics once continuous tracking begins", "Monitoring flips this around by only checking database health once per month instead of continuously"],
    ),
    (
        "A monitoring query computes `percent_used` from current connections against max_connections, meant to run \"on a regular interval, minutes or even seconds apart,\" tracking the value over time and alerting once it crosses a concerning threshold.\n\nWhat specific problem, covered in an earlier lesson, does this continuous tracking catch \"while there is still time to investigate\"?",
        "A connection leak, covered in the pooling lesson, caught through continuous tracking of percent_used rather than discovering it only once new connections start being refused outright, when it's already too late to investigate calmly.",
        "medium", "apply", "database-monitoring",
        "A connection leak, caught through continuous tracking rather than discovered only once new connections start being refused outright, when there's no time left to investigate calmly",
        ["A missing index, caught by tracking connection percentages rather than sequential scan ratios", "An SQL injection attempt, caught by monitoring the ratio of connections to max_connections", "A replication lag spike, caught through the same connection-tracking query used for pooling"],
    ),
    (
        "Tracking `dead_tuple_percent` and `last_autovacuum` across a database's busiest tables reveals \"whether autovacuum is genuinely keeping pace with write activity, or whether a table is quietly accumulating bloat faster than it is being cleaned.\"\n\nWhy does the lesson describe this as \"a slow-building problem that gradually degrades query performance long before it becomes an obvious emergency\"?",
        "Because dead tuple accumulation happens gradually over time as writes outpace cleanup, its effect on query performance also degrades gradually and subtly, rather than causing a sudden, obvious failure, making continuous tracking necessary to catch the trend before it compounds into a serious problem.",
        "medium", "analyze", "database-monitoring",
        "Because dead tuple accumulation happens gradually as writes outpace cleanup, its performance impact also degrades gradually and subtly rather than failing suddenly, making continuous tracking necessary to catch the trend early",
        ["It's described this way because dead tuples only affect performance once VACUUM FULL is explicitly disabled", "It's described this way because dead_tuple_percent only updates once every calendar month by design", "The gradual nature is irrelevant; the lesson states this problem always appears as a sudden, obvious outage"],
    ),
    (
        "A healthy, well-provisioned database typically sustains a cache hit ratio well above 90%. A ratio that \"drops noticeably, tracked over time rather than as a single snapshot,\" can signal a specific capacity issue.\n\nWhat does a declining cache hit ratio signal, according to the lesson, and why does the lesson specify tracking it over time rather than as a single snapshot?",
        "It can signal that the database's available memory is no longer large enough for its actual working data set, a capacity signal worth acting on before it manifests as widespread query slowdowns; tracking over time reveals a meaningful trend rather than a possibly misleading single moment's reading.",
        "medium", "analyze", "database-monitoring",
        "It can signal that available memory is no longer large enough for the actual working data set; tracking over time (rather than one snapshot) reveals a genuine trend worth acting on before it causes widespread slowdowns",
        ["A declining cache hit ratio signals that autovacuum has been disabled on every table in the database", "A declining ratio signals a successful backup was just completed, temporarily reducing available cache", "Snapshot versus over-time tracking makes no real difference for interpreting this particular metric"],
    ),
    (
        "A monitoring query filters `pg_stat_activity` for `state != 'idle' AND now() - query_start > INTERVAL '5 seconds'`, including `wait_event_type` and `wait_event` in its output.\n\nWhat do wait_event_type and wait_event specifically reveal about a long-running query, according to the lesson?",
        "They reveal specifically what a query is stuck waiting on, if anything, such as a lock held by another transaction, exactly the kind of contention the concurrency control unit covered, distinguishing a query that's genuinely working from one that's blocked waiting on something else.",
        "medium", "understand", "database-monitoring",
        "They reveal specifically what a query is stuck waiting on, such as a lock held by another transaction, distinguishing a genuinely running query from one blocked on contention",
        ["They reveal only the total number of rows the query has processed so far", "They reveal the exact cost estimate EXPLAIN would have produced for that query", "They reveal which physical disk sector the query's data currently resides on"],
    ),
    (
        "According to the \"Database Monitoring at a Glance\" table, what does the \"Long-running or blocked queries\" metric, sourced from pg_stat_activity and wait_event, signal?",
        "Runaway queries or lock contention needing attention, the specific health issue this particular monitored metric is designed to surface early.",
        "medium", "remember", "database-monitoring",
        "Runaway queries or lock contention needing attention",
        ["Whether the database's available memory matches its working data set", "Whether maintenance (VACUUM/ANALYZE) is keeping pace with write activity", "The risk of exhausting the database's connection limit"],
    ),
    (
        "The \"Your Turn\" exercise builds a query ranking tables by `scan_imbalance` (sequential scans minus index scans), surfacing tables where sequential scans dominate, described as \"exactly the missing-index bottleneck covered in the performance unit, now framed as something to monitor continuously.\"\n\nWhat shift does this reframing represent, compared to how the missing-index bottleneck was originally covered?",
        "It shifts a bottleneck originally diagnosed reactively, after a specific query was already reported slow, into something tracked continuously and proactively, catching a missing-index pattern developing across a database's tables before any single query is specifically flagged as a problem.",
        "medium", "analyze", "database-monitoring",
        "It shifts the missing-index bottleneck from something diagnosed reactively after a query is already reported slow into something tracked continuously, catching the pattern developing before any specific query is flagged",
        ["The reframing means missing indexes are no longer considered a performance problem once monitored", "It shifts the bottleneck from a performance issue into a security issue instead", "This reframing only applies to write-heavy tables, not to tables that are mostly read"],
    ),
]

REPLICATION_AND_READ_REPLICAS = [
    (
        "A production system serving real, sustained traffic eventually outgrows what one server can comfortably handle, and \"cannot afford for that one server to be a single point of total failure.\"\n\nWhat two concerns does the lesson say replication addresses together?",
        "Replication continuously copies a database's changes to one or more additional servers (replicas), which can take over if the primary fails (availability) and can also absorb read traffic that would otherwise all fall on a single machine (scaling).",
        "easy", "understand", "replication-and-read-replicas",
        "Replication addresses both availability (replicas can take over if the primary fails) and scaling (replicas can absorb read traffic that would otherwise fall on one machine)",
        ["Replication addresses only backup storage cost and query optimizer accuracy", "Replication addresses only SQL injection risk and connection pool exhaustion", "Replication addresses only table bloat and the need for manual VACUUM"],
    ),
    (
        "The lesson says PostgreSQL's standard replication approach relies on \"exactly the mechanism covered in the recovery unit: the write-ahead log,\" with a replica continuously receiving and replaying the same WAL records the primary generates.\n\nWhy does the lesson describe replication as \"recovery's mechanism, run continuously against a live server rather than only after a crash\"?",
        "A replica replaying streamed WAL records performs effectively the same redo process recovery uses after a crash, except continuously, in near real time, against a running, healthy primary, rather than as a one-time recovery action following a failure.",
        "medium", "analyze", "replication-and-read-replicas",
        "A replica replaying streamed WAL performs the same redo process recovery uses after a crash, except continuously and in near real time against a healthy, running primary rather than as a one-time post-crash action",
        ["It's described this way because replication only activates automatically after the primary actually crashes", "It's described this way because WAL records are deleted immediately once replication begins", "The connection to recovery is purely coincidental and has no real mechanical basis"],
    ),
    (
        "`pg_stat_replication` shows `sent_lsn` (how far the primary has sent WAL) and `replay_lsn` (how far a replica has actually applied it), with `sent_lsn - replay_lsn` representing replication lag.\n\nWhat does this lag specifically represent, according to the lesson?",
        "The gap between \"happened on the primary\" and \"visible on this replica,\" since a replica applies changes slightly after the primary generates them, meaning a query reading from a replica can, in principle, see slightly stale data.",
        "medium", "understand", "replication-and-read-replicas",
        "The gap between a change happening on the primary and that same change becoming visible on the replica, since replay always trails slightly behind the primary's WAL generation",
        ["The lag represents the total storage difference in bytes between the primary and replica databases", "The lag represents how many queries the replica has queued waiting to be executed", "The lag represents the number of tables that have not yet been created on the replica"],
    ),
    (
        "The lesson explains a query reading from a replica \"can, in principle, see slightly stale data, a deliberate trade-off in exchange for spreading read load across more than one server,\" and that replicas are typically used for workloads like \"dashboards, analytics, reporting.\"\n\nWhy are these specific workloads a good fit for querying a replica instead of the primary?",
        "These workloads can tolerate a small amount of staleness, since a dashboard or report being a few seconds or milliseconds behind the true current state rarely matters, unlike writes or reads that absolutely require the most current possible data, which continue to go to the primary.",
        "medium", "apply", "replication-and-read-replicas",
        "These workloads can tolerate a small amount of staleness, since dashboards and reports being slightly behind the true current state rarely matters, unlike writes or time-sensitive reads which stay on the primary",
        ["These workloads are a good fit only because replicas process them faster than the primary ever could", "These workloads are chosen because dashboards and reports never actually query real table data", "The fit is arbitrary; any workload type could equally well be directed to either the primary or a replica"],
    ),
    (
        "The lesson distinguishes two purposes of replication as \"worth keeping separate\": using replicas to absorb read traffic is a scaling strategy, while using a replica as a standby ready to be promoted to primary if the original fails is an availability strategy.\n\nWhy does the lesson say \"a well-designed production deployment often uses replication for both purposes simultaneously\"?",
        "The same replicas can serve read traffic day to day, providing the scaling benefit, while also standing ready to take over if the primary ever goes down, providing the availability benefit, so a single replication setup can deliver both distinct benefits at once rather than needing separate infrastructure for each.",
        "medium", "analyze", "replication-and-read-replicas",
        "The same replicas can serve read traffic day to day (scaling) while also standing ready to take over if the primary fails (availability), so one replication setup delivers both benefits at once",
        ["Because scaling and availability are actually the exact same concept described with different terminology", "Because a replica used for scaling automatically loses its ability to ever be promoted for availability", "Because production deployments are legally required to implement both purposes for compliance reasons"],
    ),
    (
        "According to the \"Replication and Read Replicas at a Glance\" table, what does the \"Mechanism\" row describe replication as streaming?",
        "The same write-ahead log a crashed server would use for recovery, streamed continuously from the primary to replicas rather than only replayed after a crash.",
        "medium", "remember", "replication-and-read-replicas",
        "The same write-ahead log a crashed server would use for recovery, streamed continuously from the primary to replicas",
        ["A compressed snapshot of the entire database taken once per hour", "The primary's connection pool state, streamed to keep replica pool sizes in sync", "A list of every query executed against the primary, replayed in the same order on each replica"],
    ),
    (
        "The lesson's closing \"Your Turn\" exercise asks for a query reporting replication lag in seconds via `replay_lag`, alongside a comment on why a reporting dashboard might be deliberately directed to a replica instead of the primary.\n\nWhat reasoning does the lesson give for that deliberate choice?",
        "A reporting dashboard's workload is read-only and can comfortably tolerate a few seconds of staleness, freeing the primary to dedicate its full capacity to the writes and time-sensitive reads that genuinely need up-to-the-moment accuracy.",
        "medium", "apply", "replication-and-read-replicas",
        "A reporting dashboard's workload is read-only and can tolerate a few seconds of staleness, freeing the primary's full capacity for writes and time-sensitive reads that need up-to-the-moment accuracy",
        ["The dashboard is directed to a replica because the primary cannot process GROUP BY queries at all", "The dashboard is directed to a replica only because pg_stat_replication requires it for logging purposes", "There's no real reason; directing reporting queries to a replica is simply an arbitrary convention"],
    ),
]

SYNTHESIS = [
    (
        "The maintenance lesson explains VACUUM reclaims dead-tuple space left behind by MVCC, while ANALYZE refreshes statistics the query optimizer relies on. The monitoring lesson tracks dead_tuple_percent and last_autovacuum as ongoing health signals.\n\nHow does the monitoring lesson's tracking of these specific metrics build directly on the maintenance lesson's explanation of why they matter in the first place?",
        "The maintenance lesson establishes that dead tuples accumulate as a normal consequence of MVCC and that autovacuum handles cleanup automatically for most cases; the monitoring lesson then builds on that foundation by continuously watching whether autovacuum is genuinely keeping pace with write activity on the busiest tables, turning the maintenance lesson's one-time explanatory concept into an ongoing, trackable signal that catches a table quietly falling behind before it becomes a performance emergency.",
        "medium", "analyze", "database-monitoring",
        "The maintenance lesson explains dead tuples accumulate under MVCC and autovacuum normally cleans them up; monitoring builds on this by continuously tracking whether autovacuum is genuinely keeping pace, catching a table falling behind before it becomes a performance emergency",
        ["The two lessons are unrelated, since monitoring only tracks connections, not anything related to VACUUM or ANALYZE", "Monitoring replaces the need for VACUUM and ANALYZE entirely, making the maintenance lesson's techniques obsolete", "Dead tuple tracking in monitoring only applies to tables that have never had autovacuum enabled"],
    ),
    (
        "The backup-strategies lesson introduces the write-ahead log as what makes incremental, point-in-time backup strategies possible. The restore-and-recovery lesson shows PITR replaying archived WAL forward from a full backup to reach an exact moment. The replication lesson shows a replica continuously replaying the same WAL the primary generates.\n\nWhat single underlying mechanism connects all three of these lessons, and how does each lesson use it differently?",
        "The write-ahead log is the shared mechanism across all three: the backup lesson uses it to make incremental backups possible without repeatedly copying the whole database; the restore lesson uses archived WAL to replay forward from a full backup to an exact point-in-time; and the replication lesson uses it to continuously stream and replay changes to a live replica in near real time, the same underlying redo mechanism applied to three different problems, incremental backup, point-in-time recovery, and live replication.",
        "hard", "analyze", "replication-and-read-replicas",
        "The write-ahead log is the shared mechanism: backups use it to avoid repeatedly copying the whole database, restore uses archived WAL to replay forward to an exact point-in-time, and replication uses it to continuously stream and replay changes to a live replica — one mechanism applied to three different problems",
        ["The three lessons actually rely on entirely separate, unrelated mechanisms with no shared foundation", "Only the restore-and-recovery lesson uses WAL; the backup and replication lessons rely on VACUUM instead", "The shared mechanism is autovacuum, not the write-ahead log, across all three lessons"],
    ),
    (
        "The restore-and-recovery lesson insists a backup must be tested through an actual restore to be trusted, since \"an unverified backup offers only the appearance of safety rather than the real thing.\" The replication lesson notes a replica can be promoted to primary as an availability strategy during failover.\n\nHow does the discipline of \"testing\" apply differently, but for a related underlying reason, to backups versus to a failover-ready replica?",
        "Both a backup and a standby replica are meant to serve as a safety net if something goes wrong with the primary system, and in both cases, the safety net's reliability is unproven until it's actually exercised; an untested backup might fail to restore cleanly, and an untested failover process might reveal unexpected problems only during a real crisis, so both need deliberate rehearsal beforehand rather than being trusted purely because they exist on paper.",
        "hard", "analyze", "restore-and-recovery",
        "Both a backup and a standby replica serve as safety nets whose reliability is unproven until actually exercised; an untested backup might fail to restore cleanly and an untested failover might reveal problems only during a real crisis, so both need rehearsal beforehand rather than blind trust that they exist",
        ["Testing applies only to backups; the lesson explicitly states replicas never need any failover testing at all", "Backups and replicas are entirely unrelated concepts, and there's no meaningful parallel between the two", "Testing a replica's failover would require destroying the primary permanently, unlike testing a backup restore"],
    ),
    (
        "Across this chapter: maintenance keeps a running database healthy day to day, backups create a recoverable copy, restore-and-recovery proves that copy actually works, monitoring catches problems continuously, and replication spreads load and provides failover. The lesson closes the entire course by saying this chapter covers \"the programmability, security, and operational discipline a real, production database runs on every single day.\"\n\nWhat progression do these five lessons follow, from the routine, everyday concern to the most catastrophic scenario a database operator has to prepare for?",
        "The progression moves from routine, everyday upkeep (maintenance, keeping the database clean as it runs), to protecting against catastrophic data loss (backups and their verification through restore), to continuous early-warning detection (monitoring, catching problems before they escalate), to surviving the complete loss of the primary server itself (replication and failover) — an escalating sequence from ordinary housekeeping to surviving total server loss.",
        "medium", "understand", "database-maintenance",
        "The progression escalates from routine upkeep (maintenance) to protecting against catastrophic data loss (backup/restore) to continuous early detection (monitoring) to surviving total primary server loss (replication/failover)",
        ["The progression is arbitrary, and the five lessons could be reordered with no change in meaning", "The progression moves from most catastrophic to least serious, the reverse of the actual chapter structure", "All five lessons address exactly the same scenario: recovering from an accidental DELETE statement"],
    ),
    (
        "The maintenance lesson shows n_dead_tup and n_live_tup in pg_stat_user_tables as maintenance signals. The monitoring lesson later queries the exact same pg_stat_user_tables columns to compute dead_tuple_percent as a continuously tracked health metric.\n\nWhat does this shared data source reveal about the relationship between the diagnostic tools introduced earlier in the course and the monitoring discipline covered in this final chapter?",
        "Monitoring doesn't require entirely new tools or data sources; it reframes the same underlying system views and columns already introduced for one-off diagnosis, like pg_stat_user_tables, pg_stat_activity, and pg_statio_user_tables, into queries run continuously and tracked over time, turning existing diagnostic building blocks into an ongoing early-warning system rather than replacing them with something new.",
        "hard", "analyze", "database-monitoring",
        "Monitoring reuses the same underlying system views and columns already introduced for one-off diagnosis (like pg_stat_user_tables), running them continuously and tracking them over time, rather than requiring entirely new tools",
        ["The shared data source is a coincidence; monitoring actually uses a completely separate internal data source", "pg_stat_user_tables was created specifically for the monitoring lesson and has no role in the maintenance lesson", "Monitoring only works if the maintenance lesson's dead-tuple tracking is first disabled entirely"],
    ),
]

SET1_SOURCES = [
    (DATABASE_MAINTENANCE, 0),
    (BACKUP_STRATEGIES, 0),
    (RESTORE_AND_RECOVERY, 0),
    (DATABASE_MONITORING, 0),
    (REPLICATION_AND_READ_REPLICAS, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    DATABASE_MAINTENANCE[1:]
    + BACKUP_STRATEGIES[1:]
    + RESTORE_AND_RECOVERY[1:]
    + DATABASE_MONITORING[1:]
    + REPLICATION_AND_READ_REPLICAS[1:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 8.4.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 8.4.2")
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
ws.title = "DBMS - MCQ - Unit 8.4"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 8 - Going to Production/8.4 - Database Administration Basics - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
