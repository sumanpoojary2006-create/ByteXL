import random
import openpyxl

random.seed(113)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

DATABASE_FAILURES = [
    (
        "A CHECK constraint violation, a deadlock that forces one transaction to abort, and an explicit ROLLBACK all fall into the same category of failure.\n\nWhat is this category called, and what's its scope?",
        "Transaction failure, the narrowest kind of failure, affecting a single transaction without touching the rest of the system at all — every other transaction and the rest of the server remain completely unaffected.",
        "easy", "understand", "database-failures",
        "Transaction failure, the narrowest scope, affecting only a single transaction while the rest of the system is unaffected",
        ["System crash, which affects everything currently in memory across the whole server", "Media failure, which can destroy data that was already safely committed", "Deadlock failure, a fourth category separate from the other three"],
    ),
    (
        "During a system crash, the entire database server process or the machine it runs on stops unexpectedly.\n\nWhat happens to a transaction that was mid-flight, uncommitted, at the exact moment of the crash?",
        "It's expected to simply vanish once the system restarts, exactly what atomicity already promises — the database's recovery process makes sure of this automatically on startup, without a human needing to manually clean anything up.",
        "easy", "understand", "database-failures",
        "It's expected to vanish entirely on restart, consistent with atomicity's guarantee, handled automatically by the recovery process",
        ["It's expected to partially apply, with whichever statements completed before the crash surviving", "It's expected to be manually reviewed and completed by a database administrator", "It's expected to automatically retry from where it left off once the system restarts"],
    ),
    (
        "The harder question a system crash raises is about transactions that had already committed right before the crash.\n\nWhich earlier-covered guarantee promises those survive, and what mechanism actually delivers on that promise after a restart?",
        "Durability is the guarantee that committed transactions survive a crash, and recovery is the mechanism that actually delivers on that guarantee after a restart, by replaying the log to reconstruct any committed work not yet fully applied to the data files.",
        "medium", "analyze", "database-failures",
        "Durability is the guarantee; recovery is the mechanism that actually delivers on it after a restart",
        ["Consistency is the guarantee; locking is the mechanism that delivers on it", "Atomicity is the guarantee; checkpoints are the mechanism that delivers on it", "Isolation is the guarantee; deadlock detection is the mechanism that delivers on it"],
    ),
    (
        "A media failure means the physical storage itself, a hard drive or solid-state disk, is damaged or fails, potentially destroying data that had already been safely written and committed.\n\nWhy can't write-ahead logging alone solve this kind of failure?",
        "The log itself typically lives on the same physical storage as the data files, so if that storage fails entirely, both the data and the log meant to recover it could be lost together — protecting against this requires separate strategies like replication to a different physical disk or server, and backups.",
        "medium", "apply", "database-failures",
        "The write-ahead log typically lives on the same physical storage as the data, so a media failure can destroy both together; separate strategies like replication and backups are needed instead",
        ["Write-ahead logging actually does fully solve media failures on its own", "Media failures never actually destroy data that was already committed", "Write-ahead logging only protects against transaction failures, never system crashes or media failures at all"],
    ),
    (
        "Unlike a system crash, where the data files themselves are intact and just need replaying up to date, what's different about a media failure?",
        "A media failure can mean the data files are genuinely gone — if the physical disk holding a table failed entirely, a query against it would find nothing to read at all, not even a stale value, since there would be no data files left to read from.",
        "medium", "understand", "database-failures",
        "The data files themselves may be genuinely destroyed, not just out of date, unlike a system crash where they remain intact and recoverable via replay",
        ["A media failure is actually less severe than a system crash, since it only affects one table", "A media failure only ever affects the write-ahead log, never the actual data files", "There's no real difference; both are resolved identically by replaying the log"],
    ),
    (
        "According to the \"Database failures at a glance\" table, what is the primary defense for each of the three failure types (transaction failure, system crash, media failure), respectively?",
        "Atomicity and ROLLBACK for transaction failure; write-ahead logging (replayed on restart) for system crash; replication and backups (not the log alone) for media failure — each scope of failure has a distinct primary defense mechanism.",
        "medium", "remember", "database-failures",
        "Atomicity/ROLLBACK for transaction failure; write-ahead logging for system crash; replication and backups for media failure",
        ["Write-ahead logging handles all three failure types equally and completely", "Replication and backups are the primary defense for all three failure types", "Atomicity and ROLLBACK are the primary defense for all three failure types"],
    ),
    (
        "An intentional transaction violating the `balance >= 0` constraint is rejected outright, affecting nothing beyond that one statement.\n\nHow does the lesson say this differs in scope from a full system crash?",
        "A system crash would require the database to recover its state across every transaction that was in progress anywhere on the server at the moment of the crash, a much broader scope than a single rejected statement affecting only its own transaction.",
        "medium", "apply", "database-failures",
        "A system crash requires recovering state across every transaction in progress anywhere on the server, unlike a single rejected statement affecting only its own transaction",
        ["There's no real difference in scope; both affect the entire server equally", "A constraint violation actually has a broader scope than a system crash", "A system crash only affects the specific table involved in the violation"],
    ),
]

WRITE_AHEAD_LOGGING = [
    (
        "Write-ahead logging's name describes its rule precisely: before any change is applied to the actual data files on disk, a record of that change is written ahead of it, to a separate, append-only log.\n\nWhy is a simpler approach, writing directly to data files the moment a transaction commits, not enough?",
        "Updating a data file on disk is not instantaneous or atomic at the hardware level; it can involve rewriting a whole page of data, and a crash occurring midway through that write could leave the page itself corrupted, not just outdated — a separate, sequential log write is far cheaper and safer to make durable quickly.",
        "easy", "understand", "write-ahead-logging",
        "Writing directly to data files isn't atomic at the hardware level, and a mid-write crash could corrupt the page itself, unlike a cheap, sequential log write",
        ["Writing directly to data files is actually just as safe, but slower for no real reason", "Data files cannot be written to at all without first going through the log, by database design convention", "Writing directly to data files would violate the CHECK constraints on the table"],
    ),
    (
        "The core rule of write-ahead logging is: a change to a data page is never written to permanent storage until the log record describing that change has already been written to permanent storage first.\n\nWhy does this ordering let COMMIT safely report success immediately?",
        "By the time COMMIT returns success, the log record describing the change has already been durably written, even if the actual data file hasn't been updated yet — the log, not the data file, is what recovery actually depends on, so success can be reported the moment the log is safe.",
        "medium", "analyze", "write-ahead-logging",
        "COMMIT can report success as soon as the log record is durably written, since recovery depends on the log, not on the data file being updated yet",
        ["COMMIT actually waits for the full data file update to complete before reporting success", "COMMIT reports success immediately regardless of whether the log or the data file has been touched at all", "The ordering has no effect on when COMMIT reports success; it's purely about data integrity"],
    ),
    (
        "`pg_current_wal_lsn()` returns PostgreSQL's current position in its write-ahead log, a steadily advancing marker.\n\nWhat causes this marker to advance?",
        "Every change made to the database advances this marker, since every change is first recorded in the log before it ever touches the actual table's data files on disk.",
        "medium", "understand", "write-ahead-logging",
        "Every database change advances the marker, since every change is recorded in the log before it touches the actual data files",
        ["Only COMMIT statements advance the marker; individual UPDATE statements do not", "Only CHECKPOINT commands advance the marker; ordinary changes do not", "The marker only advances once per day, on a fixed schedule"],
    ),
    (
        "If the server crashes at any point after COMMIT returns, the data file on disk might genuinely not yet reflect the change, since writing the full data file can be deferred and batched for efficiency.\n\nWhat does the recovery process do on restart to handle this gap?",
        "It reads the log on restart and reapplies, or \"replays,\" any change whose log record exists but whose effect had not yet made it into the data files — this is exactly how durability is delivered in practice, not by guaranteeing instant data file writes, but by guaranteeing the log record exists first and can always be replayed.",
        "medium", "apply", "write-ahead-logging",
        "Recovery reads the log on restart and replays any change whose log record exists but hasn't yet been applied to the data files",
        ["Recovery simply reports an error and refuses to start until an administrator manually fixes the data files", "Recovery discards any change that hadn't reached the data files, even if it was committed", "Recovery re-runs every transaction from the very beginning of the database's history"],
    ),
    (
        "An INSERT followed by a DELETE of the same row, moments apart, each still generates their own separate log entry, with the WAL position advancing after each one.\n\nWhat does this reveal about what the log actually records?",
        "The log records the sequence of changes, not just the final resulting state — even a row inserted and then deleted moments later still passes through the log along the way, confirming the log tracks every individual change, not a summary of the net effect.",
        "hard", "analyze", "write-ahead-logging",
        "The log records the full sequence of individual changes, not just a summary of the final net state, even when changes cancel each other out",
        ["The log only records the net effect, so an insert-then-delete of the same row would generate no log entries at all", "Only the INSERT generates a log entry; the DELETE is considered redundant and skipped", "The log only records changes to rows that still exist at the time of a checkpoint"],
    ),
    (
        "According to the \"Write-ahead logging at a glance\" table, what does this mechanism enable, in one phrase?",
        "Recovery can replay any committed change whose log record exists but whose data file write had not completed — the core payoff of the log-before-data ordering rule.",
        "medium", "remember", "write-ahead-logging",
        "Recovery can replay any committed change whose log record exists but whose data file write hadn't completed yet",
        ["It enables the database to skip writing to data files entirely, using only the log", "It enables transactions to commit without ever needing to satisfy CHECK constraints", "It enables multiple transactions to bypass isolation levels for faster performance"],
    ),
    (
        "Checking pg_current_wal_lsn(), then running BEGIN; INSERT INTO accounts (...) VALUES (3, 7000.00); COMMIT;, then checking pg_current_wal_lsn() again shows the second position further along than the first.\n\nWhat does this confirm?",
        "It confirms the INSERT's log record was appended as part of the commit — every change-making statement generates a log record before it's considered complete, and the advancing WAL position is direct evidence of that log entry being written.",
        "medium", "apply", "write-ahead-logging",
        "It confirms the INSERT's log record was appended as part of the commit, advancing the WAL position",
        ["It confirms the INSERT failed and had to be logged as an error", "It confirms the accounts table was completely rewritten to disk", "It confirms a checkpoint occurred automatically during the INSERT"],
    ),
]

CHECKPOINTS = [
    (
        "If the log records every change forever, a database running for months would have to replay months of log entries after every single crash, making recovery take longer and longer over time.\n\nWhat mechanism solves this specific problem?",
        "A checkpoint — a periodic marker that says \"everything up to this point has definitely been written to the actual data files,\" so recovery only ever has to replay the log starting from the most recent checkpoint, not from the very beginning of time.",
        "easy", "understand", "checkpoints",
        "A checkpoint, a periodic marker confirming everything before it is already safely on disk, bounding how far back recovery must replay",
        ["A deadlock, which forces one transaction to abort and free up log space", "An isolation level change, which reduces how much gets logged", "A media failure, which forces the log to be rebuilt from scratch"],
    ),
    (
        "Running CHECKPOINT explicitly forces PostgreSQL to flush every pending change out to its actual data files immediately.\n\nOnce this completes, what two things can the database be certain of?",
        "Everything committed before this point is safely reflected in the data files themselves, and that safety no longer depends on merely being recoverable by replaying the log — the checkpoint marks a genuine, verified state on disk, not just a promise in the log.",
        "medium", "understand", "checkpoints",
        "Everything committed before the checkpoint is genuinely reflected in the data files, and no longer depends on being recoverable only via log replay",
        ["Every transaction currently open will be automatically committed by the checkpoint", "The write-ahead log is deleted entirely and no longer needed after a checkpoint", "Every isolation level is reset to READ COMMITTED after a checkpoint"],
    ),
    (
        "Two updates run, then CHECKPOINT runs, then a third update runs. If a crash happened right after the third update, which updates would recovery need to replay?",
        "Only the third update, the one logged after the checkpoint — the two updates before CHECKPOINT are guaranteed to already be reflected in the data files themselves the moment the checkpoint completes, so only the change after it is at risk of existing only in the log.",
        "medium", "apply", "checkpoints",
        "Only the third update, since the first two are already guaranteed to be safely on disk before the checkpoint completed",
        ["All three updates, since a crash always requires replaying everything since the database started", "None of the updates, since CHECKPOINT guarantees nothing can ever be lost after it runs", "Only the first two updates, since they were the most recently confirmed by the checkpoint"],
    ),
    (
        "PostgreSQL runs checkpoints automatically on a regular schedule, controlled by settings like `checkpoint_timeout` (5 minutes by default), rather than relying solely on manual CHECKPOINT commands.\n\nWhat trade-off does the checkpoint frequency setting represent?",
        "Checkpointing more frequently keeps recovery time shorter after a crash, since less log needs replaying, but each checkpoint itself costs time and disk activity while it runs, so checkpointing too aggressively can slow down the database's normal, everyday operation.",
        "medium", "analyze", "checkpoints",
        "More frequent checkpoints shorten recovery time but cost more disk activity during normal operation; less frequent checkpoints do the reverse",
        ["Checkpoint frequency has no real trade-off; more frequent checkpoints are always strictly better", "More frequent checkpoints slow down recovery but speed up normal operation, the reverse of the actual trade-off", "Checkpoint frequency only affects disk space usage, not recovery time or normal operation cost"],
    ),
    (
        "According to the \"trade-off checkpoints represent\" table, what happens to recovery time and normal-operation cost under a LESS frequent checkpoint schedule?",
        "Recovery time becomes longer, since more log needs replaying after a crash, while the cost during normal operation becomes lower, since disk activity from checkpointing happens less often.",
        "medium", "remember", "checkpoints",
        "Recovery time becomes longer (more log to replay); normal-operation cost becomes lower (less frequent disk activity)",
        ["Recovery time becomes shorter, and normal-operation cost becomes higher, the reverse of the actual trade-off", "Both recovery time and normal-operation cost become lower with less frequent checkpoints", "Checkpoint frequency has no effect on either recovery time or normal-operation cost"],
    ),
    (
        "Three updates run, then CHECKPOINT, then one more update. Why does the lesson conclude that recovery would only need to replay the single post-checkpoint change if a crash happened immediately after that final update?",
        "The three updates before the checkpoint are guaranteed already durable in the actual data files, since a checkpoint confirms everything before it has been fully written out, so only the one update logged after the checkpoint is at risk of not yet being reflected in the data files and needing replay.",
        "medium", "apply", "checkpoints",
        "The pre-checkpoint updates are already guaranteed durable in the data files, so only the post-checkpoint update remains at risk and needs replaying",
        ["All four updates would need replaying, since a checkpoint doesn't actually guarantee anything about prior updates", "None of the updates would need replaying, since the checkpoint itself acts as a full backup", "Only the very first update would need replaying, since it's the oldest change in the log"],
    ),
    (
        "Without a checkpoint, a database restarting after a crash would have no way to know how far back its data files were already up to date.\n\nWhat would it be forced to do instead, and why does a checkpoint prevent this?",
        "It would have to replay every single log record ever written, from the very start of the log, just to be safe — a checkpoint gives recovery a known, recent starting line, so it never needs to look further back than the most recent checkpoint.",
        "medium", "understand", "checkpoints",
        "It would have to replay the entire log from the very beginning; a checkpoint provides a known, recent starting point instead",
        ["It would simply refuse to restart until an administrator manually intervened", "It would restore from the most recent backup instead of replaying any log at all", "It would skip recovery entirely and start with an empty database"],
    ),
]

UNDO_AND_REDO = [
    (
        "The log holds records from both transactions that had already committed before a crash, and transactions that were still in progress, uncommitted, at the exact moment of the crash.\n\nWhy must recovery treat these two kinds of entries completely differently?",
        "Committed work must be preserved, since durability demands it; uncommitted work must be discarded, since atomicity demands it — the two guarantees pull in opposite directions for these two kinds of log entries, requiring two distinct passes over the log.",
        "easy", "understand", "undo-and-redo",
        "Durability requires committed work to be preserved, while atomicity requires uncommitted work to be discarded, so the two kinds of entries need opposite treatment",
        ["Both kinds of entries actually need identical treatment; the distinction is purely for documentation purposes", "Uncommitted work must always be preserved, while committed work is discarded on every crash", "The distinction only matters for entries older than the most recent checkpoint"],
    ),
    (
        "Redo walks forward through the log from the last checkpoint and reapplies every change belonging to a transaction that committed.\n\nWhat specific gap does redo close, based on the earlier write-ahead logging lesson?",
        "A COMMIT can return success once its log record is durable, even before the actual data file has been updated — if a crash happens in that gap, the change is safely logged but not yet reflected in the data files; redo closes this gap by bringing the data files up to date with everything the log promised had already succeeded.",
        "medium", "analyze", "undo-and-redo",
        "It closes the gap between a COMMIT reporting success (once the log is durable) and the data file actually being updated, which a crash could otherwise leave unresolved",
        ["Redo closes the gap between two different checkpoints running too far apart", "Redo closes the gap caused by a deadlock that was never properly resolved", "Redo closes the gap between two transactions using different isolation levels"],
    ),
    (
        "Undo is the pass that walks through the log looking for transactions with no matching commit record, and reverses any of their changes that made it into the data files before the crash.\n\nWhy does undo need to reverse changes that \"made it into the data files\" specifically, rather than just ignoring uncommitted log entries?",
        "Even though a transaction never committed, some of its changes could have been written to the data files before the crash occurred (since data file writes can happen before COMMIT, following the write-ahead rule of logging first), so undo must actively reverse those partial effects to guarantee atomicity, not just skip replaying them.",
        "medium", "apply", "undo-and-redo",
        "Some uncommitted changes could have already reached the data files before the crash, so undo must actively reverse those partial effects, not just skip them",
        ["Undo never actually needs to touch the data files, since uncommitted changes never reach them", "Undo only needs to delete the log entries themselves, with no effect on the data files", "Undo is only needed if the transaction used an explicit ROLLBACK before the crash"],
    ),
    (
        "Recovery always performs redo first, across the entire log since the last checkpoint, before performing undo on the specific transactions that never committed.\n\nWhy does redoing everything first, including eventually-undone work, make sense rather than being wasteful?",
        "Redoing everything first gives the undo pass a single, consistent, fully-replayed state to work from, rather than trying to reason about a data file that is only partially updated — establishing one complete, known baseline state before selectively reversing the uncommitted portions.",
        "hard", "analyze", "undo-and-redo",
        "It gives undo a single, consistent, fully-replayed state to reason about, rather than a partially updated, ambiguous data file",
        ["Redoing everything first is actually wasteful, and the lesson describes this as a known inefficiency", "Redo must run first because undo is only possible after a checkpoint has completed", "Redoing first prevents any need for undo to run at all in most cases"],
    ),
    (
        "According to the \"Redo and undo at a glance\" table, what does redo apply to, and what does undo apply to, respectively?",
        "Redo applies to transactions that committed before the crash, reapplying their logged changes to guarantee durability; undo applies to transactions that never committed before the crash, reversing any changes that reached the data files to guarantee atomicity.",
        "medium", "remember", "undo-and-redo",
        "Redo applies to committed transactions (guaranteeing durability); undo applies to transactions that never committed (guaranteeing atomicity)",
        ["Redo applies to uncommitted transactions; undo applies to committed transactions, the reverse of their actual roles", "Both redo and undo apply exclusively to committed transactions, just at different points in the log", "Redo and undo both apply only to transactions that used an explicit ROLLBACK"],
    ),
    (
        "One transaction commits a balance change, and a second transaction makes a change but rolls back instead. If this had been a genuine crash rather than explicit COMMIT/ROLLBACK commands, which recovery pass would be responsible for each transaction's correct outcome?",
        "The committed transaction's effect would be guaranteed by the redo pass, reapplying its logged change if it hadn't yet reached the data file, while the rolled-back transaction's effect would be reversed by the undo pass, which recognizes it has no matching commit record and discards its partial changes.",
        "medium", "apply", "undo-and-redo",
        "Redo guarantees the committed transaction's effect; undo reverses the rolled-back (uncommitted) transaction's effect",
        ["Undo guarantees the committed transaction's effect; redo reverses the rolled-back transaction's effect, the reverse of their actual roles", "Both transactions' outcomes are guaranteed entirely by redo, with undo playing no role", "Both transactions' outcomes are guaranteed entirely by undo, with redo playing no role"],
    ),
    (
        "An explicit ROLLBACK after an uncommitted UPDATE demonstrates the same outcome undo would achieve automatically after a crash.\n\nWhy would no ROLLBACK ever actually be issued by anyone in a genuine crash scenario, and how does undo still achieve the same result?",
        "In a genuine crash, the whole application vanished along with the server, so nobody is present to issue a ROLLBACK command; PostgreSQL's undo pass performs the identical reversal automatically during recovery, simply by recognizing that a transaction's log entries have no corresponding commit record.",
        "medium", "analyze", "undo-and-redo",
        "In a real crash, the application itself is gone, so no one can issue ROLLBACK; undo instead automatically reverses any transaction whose log entries lack a matching commit record",
        ["A ROLLBACK is always issued automatically by the operating system during a crash", "Undo cannot actually replicate what an explicit ROLLBACK does; they produce different results", "The application always survives a crash and can issue ROLLBACK once the server restarts"],
    ),
]

TRANSACTIONS_IN_APPLICATION_CODE = [
    (
        "Most database client libraries default to auto-commit mode, where every individual statement is automatically wrapped in its own tiny transaction and committed immediately, unless the code explicitly starts a transaction itself.\n\nWhat kind of bug does this default behavior commonly cause?",
        "The exact atomicity gap the very first lesson of this unit opened with: code that assumed two statements would be treated as one, but ran under a client library's default auto-commit setting instead, letting each UPDATE commit independently and immediately.",
        "easy", "understand", "transactions-in-application-code",
        "\"Half a transfer went through\" bugs, where code assumed two statements would be treated as one but each committed independently under auto-commit",
        ["Deadlock errors, since auto-commit mode always triggers a deadlock between statements", "Constraint violations, since auto-commit mode disables all CHECK constraints", "Data type mismatches, since auto-commit mode converts every column to text"],
    ),
    (
        "The fix demonstrated throughout the unit is for application code to explicitly start a transaction before the first related statement and commit only after the last one succeeds, typically using a try-and-catch style structure.\n\nWhat does that structure do if any statement raises an error partway through?",
        "It catches the error and skips straight to a ROLLBACK branch instead of committing, guaranteeing the transaction never commits a partial result — COMMIT only ever runs if every statement in the sequence succeeded without error.",
        "medium", "understand", "transactions-in-application-code",
        "It catches the error and rolls back instead of committing, ensuring no partial result is ever committed",
        ["It skips the failing statement and commits everything else that succeeded", "It automatically retries the failing statement up to three times before rolling back", "It ignores the error and proceeds to COMMIT regardless of what failed"],
    ),
    (
        "Every lock a transaction holds stays held until that transaction commits or rolls back. A transaction left open for a long time, whether doing slow, unrelated work or because a bug forgot to commit, holds its locks the entire time.\n\nWhat practical rule follows from this, regarding what should happen inside an open transaction?",
        "A transaction should contain only the database statements that genuinely need to succeed or fail together, and nothing slow or unrelated, such as calling an external payment gateway or waiting on user input, should ever happen while a transaction sits open holding locks.",
        "medium", "apply", "transactions-in-application-code",
        "A transaction should contain only the statements that must succeed or fail together, with no slow external calls or waiting happening while locks are held",
        ["A transaction should always include as many unrelated statements as possible to minimize the number of BEGIN/COMMIT pairs", "A transaction should always wait for user confirmation before committing, regardless of how long that takes", "A transaction should never use FOR UPDATE, since it always causes unnecessary delays"],
    ),
    (
        "A deadlock victim's transaction is guaranteed to have been fully rolled back by the database.\n\nWhy does the lesson say retrying that transaction from scratch is \"always safe,\" and why does it typically succeed the second time?",
        "Because the deadlock victim's transaction was fully rolled back, retrying it from the beginning is safe (there's no partial state to worry about), and it typically succeeds the second time because whatever transaction it was originally competing with has usually already finished by the time the retry runs.",
        "medium", "analyze", "transactions-in-application-code",
        "The rolled-back transaction leaves no partial state, making a retry safe, and it typically succeeds because the competing transaction has usually finished by then",
        ["Retrying is safe only because deadlocks are extremely rare and unlikely to recur", "The retry succeeds because the database automatically raises the retried transaction's isolation level", "Retrying is safe because deadlock victims are always given priority over other transactions on the next attempt"],
    ),
    (
        "According to the \"Transactions in application code at a glance\" table, what's the reasoning behind \"retry on deadlock, not on every error\"?",
        "Deadlock victims are always safely rollbackable, and retrying them is expected, routine behavior under normal concurrent load; other errors may indicate a real bug in the application logic, so blindly retrying every kind of error could mask genuine problems rather than fixing a transient conflict.",
        "hard", "analyze", "transactions-in-application-code",
        "Deadlock victims are always safely rollbackable and expected to occur under load, while other errors may indicate a real bug that retrying would only mask rather than fix",
        ["All errors should actually be retried identically, and this distinction is a minor stylistic preference", "Deadlock errors are the only kind of error that can never be safely retried", "Retrying on any error, deadlock or otherwise, always risks committing a partial result"],
    ),
    (
        "A transaction inserts a new account and immediately transfers 100.00 into it from account 1, using a try-and-catch pseudocode pattern with a rollback branch for any failure.\n\nWhat does the closing comment about the rollback branch emphasize should trigger a full rollback?",
        "Any failure at any point before COMMIT should trigger a full rollback rather than a partial commit — the same discipline covered throughout the unit, where the transaction either fully succeeds and commits, or any failure at all discards everything attempted so far.",
        "medium", "apply", "transactions-in-application-code",
        "Any failure at any point before COMMIT, ensuring a full rollback rather than allowing a partial commit",
        ["Only a failure in the INSERT statement specifically should trigger a rollback", "Only a failure in the second UPDATE statement should trigger a rollback", "Only a failure that occurs after COMMIT has already been called should trigger a rollback"],
    ),
    (
        "Two UPDATE statements run without an explicit BEGIN each commit on their own, immediately, the moment they finish.\n\nWhat does the lesson call this default behavior, and what specific atomicity gap does it reopen?",
        "Auto-commit mode — every individual statement is automatically wrapped in its own tiny transaction and committed immediately, reopening the exact atomicity gap the unit's very first lesson described, where a partial transfer could leave money deducted from one account without being credited to another.",
        "medium", "understand", "transactions-in-application-code",
        "Auto-commit mode, which reopens the exact atomicity gap from the unit's opening lesson, since each statement commits independently rather than as one unit",
        ["Isolation mode, which reopens the dirty-read gap from the concurrency chapter", "Checkpoint mode, which reopens the recovery-time gap from the checkpoints lesson", "Durability mode, which reopens the crash-survival gap from the durability lesson"],
    ),
]

SYNTHESIS = [
    (
        "The database failures lesson distinguishes transaction failure (handled by atomicity/ROLLBACK) from system crash (handled by write-ahead logging). The write-ahead logging lesson then explains the log-before-data rule that makes crash recovery possible at all.\n\nHow do these two lessons connect: why does a system crash specifically need write-ahead logging, when a transaction failure does not?",
        "A transaction failure is resolved live, in the moment, by simply not letting the failing transaction's changes take effect (atomicity/ROLLBACK, no crash involved). A system crash wipes out everything in memory at once, including the ability to know what any transaction was doing, so recovery needs a separate, already-durable record (the write-ahead log) to reconstruct what happened after the fact, once the system restarts.",
        "medium", "analyze", "write-ahead-logging",
        "A transaction failure is resolved live without any memory loss; a system crash wipes out memory entirely, so recovery needs the durable write-ahead log to reconstruct what happened after restarting",
        ["Both failure types are handled by exactly the same mechanism, making this distinction unnecessary", "Transaction failure actually requires write-ahead logging, while system crash does not", "Write-ahead logging is only relevant to media failure, not to system crash at all"],
    ),
    (
        "Checkpoints bound how far back recovery must replay the log. Redo and undo are the two passes recovery actually performs once a crash happens. How does a checkpoint change the starting point for both the redo and undo passes after a crash?",
        "Since a checkpoint guarantees everything logged before it is already durably written to the data files, both redo and undo only need to examine the log starting from the most recent checkpoint forward — redo doesn't need to replay anything from before the checkpoint (it's already safely applied), and undo only needs to look for uncommitted transactions active in that same post-checkpoint window.",
        "hard", "analyze", "undo-and-redo",
        "Both redo and undo only need to examine the log from the most recent checkpoint forward, since everything before it is already guaranteed durably applied to the data files",
        ["Checkpoints only affect the redo pass; undo must always scan the entire log regardless of any checkpoint", "Checkpoints only affect the undo pass; redo must always scan the entire log regardless of any checkpoint", "Checkpoints have no effect on either the redo pass or the undo pass, only on disk space usage"],
    ),
    (
        "The application-code lesson emphasizes keeping transactions short because every lock a transaction holds stays held until commit or rollback. The concurrency control chapter (from the previous chapter in this unit) explained that locks block other transactions from touching the same rows.\n\nHow does the recovery chapter's emphasis on short transactions connect back to the concurrency control chapter's concerns, even though recovery is nominally about crash survival?",
        "A long-running, open transaction doesn't just hold locks that block other transactions (a concurrency control concern); it also means more work is sitting uncommitted, in-progress, and at risk of being lost or needing to be undone if a crash happens during that window (a recovery concern) — the application-level discipline of keeping transactions short serves both goals simultaneously, since a shorter transaction both blocks less and has less to lose in a crash.",
        "hard", "understand", "transactions-in-application-code",
        "Keeping transactions short reduces both how long locks are held (a concurrency concern) and how much uncommitted work is at risk if a crash happens mid-transaction (a recovery concern), serving both goals at once",
        ["Short transactions only matter for concurrency control and have no connection to recovery at all", "Short transactions only matter for recovery and have no connection to concurrency control at all", "The two chapters address completely unrelated concerns with no meaningful overlap"],
    ),
    (
        "Across the recovery chapter, transaction failure is handled instantly and locally; system crashes are handled by write-ahead logging, checkpoints, and the redo/undo passes together; and media failure requires replication or backups entirely outside the transaction log.\n\nWhat single principle explains why the database's response scales up in complexity across these three failure types, from simplest to most involved?",
        "The response's complexity scales with how much trusted information survives the failure: a transaction failure leaves everything else intact (simple rollback suffices); a system crash destroys memory but leaves the durable log and data files intact (log replay via redo/undo suffices); a media failure can destroy the log and data files themselves, leaving nothing trustworthy on that storage to recover from at all, requiring an entirely separate copy of the data elsewhere.",
        "hard", "analyze", "database-failures",
        "The complexity scales with how much trusted information survives each failure — a transaction failure loses nothing durable, a crash loses only memory (log and data survive), and a media failure can destroy the log and data together, requiring an entirely separate copy elsewhere",
        ["The complexity scales purely with how often each failure type occurs, not with what data survives", "All three failure types actually require exactly the same level of response; the distinction is only theoretical", "The complexity scales with how many tables are involved in each specific failure"],
    ),
    (
        "The write-ahead logging lesson establishes \"log before data\" as the core rule. The checkpoints lesson then introduces a mechanism that flushes pending changes out to the actual data files. The undo/redo lesson explains recovery replaying from the log.\n\nHow does a checkpoint's action (flushing changes to data files) relate to the very gap that write-ahead logging's \"log first\" rule was designed to tolerate?",
        "Write-ahead logging tolerates a gap between a durably logged change and that change actually reaching the data files (deferring the slower data file write for efficiency); a checkpoint is precisely the mechanism that periodically closes that gap by forcing all pending changes through to the data files at once, which is exactly why recovery can trust that everything before a checkpoint no longer depends on the log at all.",
        "hard", "analyze", "checkpoints",
        "A checkpoint periodically closes the very gap write-ahead logging tolerates (log written but data file not yet updated), by flushing all pending changes to the data files at once",
        ["A checkpoint actually widens the gap between the log and the data files, making recovery slower", "Checkpoints and write-ahead logging address completely unrelated gaps with no connection to each other", "A checkpoint replaces the need for write-ahead logging entirely, making the log unnecessary afterward"],
    ),
]

SET1_SOURCES = [
    (DATABASE_FAILURES, 0),
    (WRITE_AHEAD_LOGGING, 0),
    (CHECKPOINTS, 0),
    (UNDO_AND_REDO, 0),
    (TRANSACTIONS_IN_APPLICATION_CODE, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    DATABASE_FAILURES[1:]
    + WRITE_AHEAD_LOGGING[1:]
    + CHECKPOINTS[1:]
    + UNDO_AND_REDO[1:]
    + TRANSACTIONS_IN_APPLICATION_CODE[1:]
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
            "topics": "transactions-and-reliability",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 6.3.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 6.3.2")
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
ws.title = "DBMS - MCQ - Unit 6.3"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 6 - Transactions and Reliability/6.3 - Recovery - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
