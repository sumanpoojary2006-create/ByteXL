import random
import openpyxl

random.seed(107)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

WHY_CONCURRENCY_CONTROL_NEEDED = [
    (
        "Two passengers both read \"seat 14C: available\" before either one commits, and both proceed to book it. Isolation was never violated, since neither passenger read the other's uncommitted work.\n\nWhat exactly is the problem, if not an isolation violation?",
        "The problem is the gap in time between reading \"available\" and acting on that reading with an UPDATE — both passengers' applications ran the same read-then-write sequence close enough together that both concluded the seat was free before either one's booking became final.",
        "easy", "understand", "why-concurrency-control-is-needed",
        "The gap between reading a value and acting on it lets two transactions both act on the same \"available\" reading before either commits",
        ["Isolation actually was violated, and the lesson misdescribes the scenario", "The problem is that the seats table has no primary key defined", "The problem only occurs because the two passengers used the same database connection"],
    ),
    (
        "Atomicity, consistency, isolation, and durability are all individually satisfied in the double-booking scenario, yet the airline still ends up selling one seat twice.\n\nWhat does this reveal about the relationship between ACID and concurrency control?",
        "None of the ACID guarantees, by themselves, stop two separate, individually well-behaved transactions from both reading the same true statement and both acting on it in a way that conflicts — concurrency control is specifically about coordinating the interaction between transactions, not just protecting each one internally.",
        "medium", "analyze", "why-concurrency-control-is-needed",
        "ACID protects each transaction's own internal correctness, but doesn't by itself coordinate how multiple transactions interact with shared data",
        ["ACID and concurrency control are the same set of guarantees, just named differently", "ACID actually does prevent this, and the double-booking scenario represents a bug in the database", "Concurrency control is a subset of atomicity, not a separate concern"],
    ),
    (
        "The chapter introduces serializability as the standard concurrency control is measured against.\n\nWhat does this standard actually demand?",
        "Whatever order transactions actually execute in, concurrently, interleaved, overlapping, the final result must match some possible outcome of running those same transactions strictly one at a time, in some order.",
        "medium", "understand", "why-concurrency-control-is-needed",
        "The final result of concurrent execution must match some outcome that running the same transactions one at a time, in some order, could have produced",
        ["Every transaction must run in exactly the order it was submitted, with no exceptions", "Every transaction must complete before any other transaction is allowed to begin", "The final result must always be identical, no matter what order transactions run in"],
    ),
    (
        "If Passenger A and Passenger B's bookings had genuinely run one after the other (not overlapping), whichever went second would have seen the seat already taken and been stopped before booking it.\n\nWhat does proper concurrency control guarantee, relative to this serial scenario?",
        "A database with proper concurrency control produces that same correct outcome (one booking succeeds, the other is stopped) even when the two bookings actually overlap in real time, matching what a strictly sequential execution would have produced.",
        "medium", "apply", "why-concurrency-control-is-needed",
        "It produces the same correct outcome as if the bookings had run strictly one after another, even though they actually overlapped in real time",
        ["It guarantees both bookings will always succeed, regardless of overlap", "It guarantees both bookings will always fail if they overlap in time", "It has no effect on the outcome; only application-level checks can fix this"],
    ),
    (
        "Why does the lesson say concurrency control \"stops being an academic concern\" the moment a system serves more than one person at once?",
        "A database with a single user never encounters this class of problem, since there's nothing to run concurrently against — but the moment more than one person uses a system at once, which describes nearly every real application, concurrency control becomes the difference between a system that works under load and one that quietly loses or duplicates data the busier it gets.",
        "medium", "analyze", "why-concurrency-control-is-needed",
        "A single-user database has nothing to run concurrently against, but any multi-user system risks silently losing or duplicating data without concurrency control",
        ["Concurrency control only matters for systems with more than one million users", "It's always an academic concern, regardless of how many users a system has", "Concurrency control only matters for financial applications specifically"],
    ),
    (
        "According to the \"Why concurrency control is needed, at a glance\" table, what determines the result without coordination, versus with concurrency control?",
        "Without coordination, the result depends on unlucky timing; with concurrency control, the result matches some valid one-at-a-time ordering, regardless of how the transactions actually happened to interleave in real time.",
        "medium", "remember", "why-concurrency-control-is-needed",
        "Without coordination, the result depends on unlucky timing; with concurrency control, it matches some valid one-at-a-time ordering",
        ["Without coordination, the result is always wrong; with concurrency control, it's always identical to a fixed baseline", "Both scenarios produce the same result; only the speed differs", "Without coordination, transactions run faster; with concurrency control, they run more slowly with no correctness benefit"],
    ),
]

CONCURRENCY_PROBLEMS = [
    (
        "Transaction A updates stock_count to 0 but has not yet committed, and might still roll back. If Transaction B could read that uncommitted 0 and tell a customer \"out of stock\" before A rolls back and restores 50, what is this problem called?",
        "A dirty read — reading a change made by another transaction that has not yet committed, and might still be rolled back, acting on data that never actually existed once the rollback happens.",
        "easy", "remember", "concurrency-problems",
        "A dirty read",
        ["A phantom read", "A non-repeatable read", "A lost update"],
    ),
    (
        "PostgreSQL's default isolation level prevents dirty reads entirely, so a concurrent transaction is never allowed to see an in-progress, uncommitted change.\n\nWhy does the lesson still catalog dirty reads with a precise name, even though PostgreSQL's default already prevents them?",
        "Some databases, or some deliberately relaxed isolation levels, do allow dirty reads, and knowing the name of the problem is what makes a setting like \"read uncommitted\" understandable later in the chapter.",
        "medium", "understand", "concurrency-problems",
        "Because some databases or relaxed isolation levels do allow dirty reads, and naming the problem is necessary to understand settings like \"read uncommitted\" later",
        ["Dirty reads are actually still possible in PostgreSQL under its default settings", "The name exists purely for historical reasons, with no modern relevance", "PostgreSQL only prevents dirty reads for certain table types, not all of them"],
    ),
    (
        "Transaction A reads stock_count as 50, then Transaction B commits a legitimate change to 40 in between, and Transaction A's second read within the same transaction now sees 40, a different answer than its first read.\n\nWhy is this NOT a dirty read, even though the value changed mid-transaction?",
        "Unlike a dirty read, the second read here reflects genuinely committed data, so nothing incorrect was ever seen — the issue is that a single transaction's own view of the data changed mid-flight, which is exactly what makes it a non-repeatable read instead, a different named problem.",
        "medium", "analyze", "concurrency-problems",
        "The second read reflects genuinely committed data, unlike a dirty read; the issue is that the transaction's own view changed mid-flight, making it a non-repeatable read instead",
        ["It actually is a dirty read, and the lesson's distinction is incorrect", "It's not a real problem at all, since the second value is more up to date", "This scenario can only happen if Transaction A never actually committed"],
    ),
    (
        "Transaction A runs `SELECT COUNT(*) FROM inventory WHERE stock_count < 50;` twice, getting 0 the first time and 1 the second time, because Transaction B inserted a new low-stock row in between.\n\nWhy does this get its own name (phantom read) distinct from a non-repeatable read?",
        "A phantom read is the same underlying problem as a non-repeatable read, but at the level of an entire query's row count rather than a single row's value — the new row was not a value that changed underneath Transaction A, it's an entirely new row matching a condition Transaction A was relying on.",
        "medium", "apply", "concurrency-problems",
        "A phantom read involves a changing set of matching rows (from an insert or delete), rather than a single existing row's value changing, which is what a non-repeatable read describes",
        ["Phantom reads and non-repeatable reads are actually the exact same problem with two different names", "A phantom read only happens when DELETE is used, never INSERT", "A phantom read can only occur if the query has no WHERE clause at all"],
    ),
    (
        "Two separate deductions of 10 and 15 units are both computed from the same starting stock_count of 50, run one after the other as `UPDATE inventory SET stock_count = 50 - 10 ...` and `UPDATE inventory SET stock_count = 50 - 15 ...`.\n\nWhat does the final stock count incorrectly show, and what problem does this illustrate?",
        "The final stock count is 35, reflecting only the second deduction, with the first 10-unit sale's effect on stock lost entirely — this is a lost update, where two transactions both read the same value, both write a new value based on it, and one write silently disappears.",
        "medium", "apply", "concurrency-problems",
        "35, reflecting only the second deduction; this is a lost update, where one write based on a shared stale value silently overwrites another",
        ["25, correctly reflecting both deductions combined; this is not actually a problem", "40, since the database automatically averages conflicting writes; this is a phantom read", "An error, since PostgreSQL rejects conflicting UPDATE statements automatically"],
    ),
    (
        "According to the \"Concurrency problems\" summary table, what specifically distinguishes a non-repeatable read from a phantom read?",
        "A non-repeatable read is the same row read twice within one transaction returning two different values; a phantom read is the same filtered query run twice within one transaction returning a different set of rows — one concerns a single row's value, the other concerns the row count of a query.",
        "medium", "remember", "concurrency-problems",
        "A non-repeatable read changes a single row's value between two reads; a phantom read changes the number of rows a filtered query returns between two runs",
        ["They are identical; the table lists them as the same problem twice", "A non-repeatable read changes row count; a phantom read changes a single value, the reverse of their actual definitions", "A non-repeatable read only applies to INSERT statements, and a phantom read only applies to UPDATE statements"],
    ),
]

LOCKING = [
    (
        "The lost update from the previous lesson happened because two transactions both read the same stock count and both wrote a new value based on that stale reading.\n\nWhat does the lesson say the actual fix is, as opposed to clever application logic checking timestamps after the fact?",
        "Stopping the second transaction from reading and acting on the value until the first transaction has finished with it entirely — this is what locking does, letting a transaction claim a lock on a row that blocks other transactions from making conflicting changes until the lock is released.",
        "easy", "understand", "locking",
        "Locking: stopping the second transaction from reading and acting on the value until the first transaction has fully finished with it",
        ["Adding a timestamp column and comparing timestamps after each write completes", "Increasing the isolation level to the loosest possible setting", "Running both transactions on entirely separate database servers"],
    ),
    (
        "`SELECT stock_count FROM inventory WHERE product_id = 1 FOR UPDATE;` is used inside a transaction before updating that row.\n\nWhat does FOR UPDATE specifically do?",
        "It tells the database that this transaction intends to modify the row it just read, and claims a lock on that row immediately — any other transaction that also tries a SELECT ... FOR UPDATE or a direct UPDATE against that same row is forced to wait until this transaction commits or rolls back.",
        "easy", "understand", "locking",
        "It claims an exclusive lock on the row being read, forcing other transactions wanting to modify it to wait",
        ["It permanently locks the row so no transaction can ever read it again", "It marks the row for deletion once the transaction commits", "It creates a backup copy of the row before any changes are made"],
    ),
    (
        "Without a lock, both transactions could read 50 at nearly the same instant, before either had written anything back. With FOR UPDATE, whichever transaction reaches the row first locks it.\n\nWhat happens to the second transaction's own SELECT ... FOR UPDATE in that case?",
        "It blocks until the first transaction is completely finished, guaranteeing the second transaction's read reflects the first transaction's already-committed result, not a stale value both transactions raced to read at the same moment — this is exactly what closes the gap causing the lost update.",
        "medium", "analyze", "locking",
        "It blocks (waits) until the first transaction finishes, ensuring the second transaction reads the already-updated value rather than a stale one",
        ["It proceeds immediately with the stale value, exactly as it would without FOR UPDATE", "It automatically cancels the first transaction to let the second one proceed", "It raises an immediate error rather than waiting for the lock"],
    ),
    (
        "A shared lock, taken automatically by an ordinary read, allows other transactions to also read the same row concurrently. An exclusive lock, taken by FOR UPDATE, blocks other transactions from reading with intent to modify or writing to that row at all.\n\nWhy does a shared lock allow concurrent reading while an exclusive lock does not?",
        "Reading alongside reading causes no conflict, since neither reader changes the data, but two transactions both planning to change the same row is exactly the conflict that needs preventing, which is why an exclusive lock blocks any other lock attempt on that row.",
        "medium", "apply", "locking",
        "Reading alongside reading causes no conflict; but two transactions both planning to write to the same row is exactly the conflict locking needs to prevent",
        ["Shared locks and exclusive locks actually behave identically in every database", "A shared lock is stricter than an exclusive lock, blocking even other reads", "Exclusive locks only apply to DELETE statements, not UPDATE or SELECT FOR UPDATE"],
    ),
    (
        "Locking a row for product_id = 1 with FOR UPDATE never blocks a separate transaction working with product_id = 2.\n\nWhy is this row-level scope, rather than table-level locking, described as what makes locking \"practical at real-world scale\"?",
        "A busy inventory system can have thousands of concurrent transactions, each safely locking only the specific rows it touches, without the whole table grinding to a halt waiting on unrelated updates — table-level locking would force every transaction to wait on every other one, regardless of whether they actually touch the same data.",
        "hard", "analyze", "locking",
        "Row-level locking lets thousands of concurrent transactions proceed independently as long as they touch different rows, rather than all waiting on each other the way table-level locking would force",
        ["Row-level and table-level locking perform identically at any scale", "Row-level locking is actually slower than table-level locking in every case", "Table-level locking is preferred at scale, and row-level locking is only for small tables"],
    ),
    (
        "According to the \"Locking at a glance\" table, when is a lock released?",
        "Automatically, when the transaction commits or rolls back — a lock is never released manually or on a timer; it's tied directly to the lifecycle of the transaction that holds it.",
        "medium", "remember", "locking",
        "Automatically, when the transaction commits or rolls back",
        ["After a fixed 30-second timeout, regardless of transaction status", "Only when another transaction explicitly requests it be released", "Never automatically; it must always be released manually by the application"],
    ),
]

ISOLATION_LEVELS = [
    (
        "Locking everything as strictly as possible all the time would make a busy database painfully slow, and different applications have different tolerances (a dashboard view count can live with a non-repeatable read that a banking transfer never could).\n\nWhat SQL mechanism exposes this trade-off directly?",
        "Isolation levels — a per-transaction setting that controls exactly which of the concurrency problems (dirty reads, non-repeatable reads, phantom reads) the database is allowed to permit in exchange for less locking and better performance.",
        "easy", "understand", "isolation-levels",
        "Isolation levels, a per-transaction setting trading strictness against concurrency for performance",
        ["Checkpoints, which control how often data is flushed to disk", "Foreign keys, which control which rows can reference each other", "The WAL, which records every change for crash recovery"],
    ),
    (
        "PostgreSQL does not implement READ UNCOMMITTED as a genuinely looser level; it's treated the same as READ COMMITTED.\n\nHow many distinct behaviors does PostgreSQL offer in practice, even though four isolation level names exist in the SQL standard?",
        "Three distinct behaviors — since READ UNCOMMITTED and READ COMMITTED behave identically in PostgreSQL, the four standard names collapse into three genuinely different behaviors: (effectively) READ COMMITTED, REPEATABLE READ, and SERIALIZABLE.",
        "medium", "understand", "isolation-levels",
        "Three, since READ UNCOMMITTED and READ COMMITTED behave identically in PostgreSQL despite being named separately in the standard",
        ["Four, since PostgreSQL implements every named level distinctly", "Two, since PostgreSQL only supports READ COMMITTED and SERIALIZABLE", "One, since PostgreSQL treats all isolation levels identically by default"],
    ),
    (
        "According to the \"What each level actually prevents\" table, REPEATABLE READ prevents dirty reads and non-repeatable reads but leaves phantom reads \"Possible (prevented in PostgreSQL specifically)\".\n\nWhat does this parenthetical reveal about the relationship between the SQL standard and a specific database's actual implementation?",
        "A specific database implementation, like PostgreSQL, can choose to provide stronger guarantees than the SQL standard strictly requires for a given isolation level name — PostgreSQL's REPEATABLE READ happens to prevent phantom reads too, even though the standard only requires that of SERIALIZABLE.",
        "hard", "analyze", "isolation-levels",
        "A database implementation can offer stronger guarantees than the SQL standard strictly requires for a given isolation level name, as PostgreSQL does for REPEATABLE READ",
        ["This is a documentation error; PostgreSQL cannot actually prevent phantom reads under REPEATABLE READ", "The SQL standard and PostgreSQL's implementation are always identical for every isolation level", "PostgreSQL's REPEATABLE READ is actually weaker than the standard requires"],
    ),
    (
        "Under REPEATABLE READ, a transaction reads stock_count as 50, another transaction commits a change to it in between, and the first transaction's second read still returns 50.\n\nWhy does the second read still return the original value?",
        "REPEATABLE READ takes a consistent snapshot of the data as of when the transaction began, and every read within that transaction is served from that same snapshot rather than the constantly updating live data, guaranteeing both reads agree regardless of what any other transaction committed in between.",
        "medium", "apply", "isolation-levels",
        "REPEATABLE READ serves every read within a transaction from a consistent snapshot taken when the transaction began, ignoring changes committed by others afterward",
        ["The second read is actually a bug, and REPEATABLE READ should have shown the updated value", "REPEATABLE READ locks the row so no other transaction can update it at all", "The second read only returns 50 because the other transaction's change happened to fail"],
    ),
    (
        "SERIALIZABLE prevents every concurrency problem covered in this chapter, yet the lesson says it shouldn't always be the default choice.\n\nWhat cost does SERIALIZABLE carry that makes READ COMMITTED the more sensible default for most everyday queries?",
        "SERIALIZABLE transactions can be forced to abort and retry when the database detects that their interleaving with another concurrent transaction could not be made to match any valid one-at-a-time ordering, and stricter levels generally mean more waiting and more retries under heavy concurrent load.",
        "medium", "analyze", "isolation-levels",
        "SERIALIZABLE transactions can be forced to abort and retry under concurrent load, and stricter levels generally mean more waiting overall",
        ["SERIALIZABLE is simply not supported by PostgreSQL in production environments", "SERIALIZABLE requires manually writing lock statements for every table involved", "SERIALIZABLE only works for single-row transactions, never multi-row ones"],
    ),
    (
        "According to the \"Isolation levels at a glance\" table, what's the recommended typical use for REPEATABLE READ versus SERIALIZABLE?",
        "REPEATABLE READ suits reports that must stay internally consistent while running; SERIALIZABLE suits financial transfers, booking systems, and anything where a subtle conflict is unacceptable — matching the strictness of the level to how costly a concurrency problem would actually be for that operation.",
        "medium", "remember", "isolation-levels",
        "REPEATABLE READ for reports needing internal consistency while running; SERIALIZABLE for financial transfers and booking systems where any conflict is unacceptable",
        ["REPEATABLE READ for financial transfers; SERIALIZABLE for everyday reporting queries, the reverse of their actual fit", "Both are recommended for exactly the same use cases with no meaningful difference", "REPEATABLE READ and SERIALIZABLE are never actually recommended for any real use case"],
    ),
]

DEADLOCKS = [
    (
        "Transaction A locks account 1 and then tries to lock account 2, while Transaction B has already locked account 2 and is now trying to lock account 1. Each transaction is waiting on the other, forever, unless something intervenes.\n\nWhat is this standoff called?",
        "A deadlock — two or more transactions each holding a lock the other one needs, with neither willing to let go until it gets what it is waiting for, forming a cycle with no natural way to continue.",
        "easy", "remember", "deadlocks",
        "A deadlock",
        ["A phantom read", "A dirty read", "A checkpoint"],
    ),
    (
        "\"Each transaction is individually doing something perfectly reasonable, locking one row and then requesting a second row it needs, but the two together form a cycle.\"\n\nWhat does this reveal about how a deadlock forms, even when no single transaction did anything obviously wrong?",
        "A deadlock isn't caused by any single transaction misbehaving; it emerges purely from the combination of two individually reasonable transactions requesting the same two resources in opposite orders, forming a circular wait that neither one can escape on its own.",
        "medium", "analyze", "deadlocks",
        "A deadlock emerges from the combination of two individually reasonable transactions requesting the same resources in opposite orders, not from any single transaction's mistake",
        ["A deadlock only happens when a transaction contains a coding error", "A deadlock is always caused by one transaction deliberately blocking another", "A deadlock can only occur when more than two transactions are involved simultaneously"],
    ),
    (
        "Once PostgreSQL detects a deadlock cycle, what three steps does it take, in order?",
        "It forcibly aborts one of the two transactions (typically whichever is cheapest to roll back), rolls that transaction back and raises a deadlock error, and the other transaction is freed to continue.",
        "medium", "understand", "deadlocks",
        "It forcibly aborts and rolls back one transaction (raising a deadlock error), then frees the other transaction to continue",
        ["It pauses both transactions indefinitely until a human administrator intervenes manually", "It rolls back both transactions entirely, requiring both applications to restart from scratch", "It merges the two transactions into one and completes both sets of changes together"],
    ),
    (
        "The application on the receiving end of a deadlock error is expected to catch it and retry the whole transaction from the beginning.\n\nWhy does the lesson say this retry typically succeeds the second time?",
        "The other transaction has usually finished by the time the retry runs, since the deadlock victim was rolled back specifically to let the other transaction proceed and complete, removing the conflicting lock that caused the original standoff.",
        "medium", "apply", "deadlocks",
        "By the time the retry runs, the other transaction has usually already finished, since it was freed to complete once the victim was rolled back",
        ["The retry succeeds only because PostgreSQL disables deadlock detection during a retry", "The retry succeeds because the retried transaction now uses a different isolation level automatically", "The retry always fails on the second attempt too, requiring a third attempt"],
    ),
    (
        "The most reliable prevention technique is making sure every transaction that touches multiple rows always locks them in the same, consistent order (for example, always locking the lower account_id first, regardless of transfer direction).\n\nWhy does this consistent ordering prevent the circular wait pattern that causes a deadlock?",
        "If every transaction, regardless of which direction it transfers money, always locks account 1 before account 2 whenever both are involved, the circular waiting pattern can never form: whichever transaction gets to account 1 first simply makes the other one wait its turn, in a straight line rather than a cycle.",
        "hard", "analyze", "deadlocks",
        "Locking rows in the same order everywhere turns potential circular waits into a straight-line wait, since whichever transaction reaches the shared first resource simply makes the other wait its turn",
        ["Consistent lock ordering has no actual effect on deadlock formation, only on performance", "It prevents deadlocks by removing the need for locks altogether", "It works by allowing each transaction to skip locking whichever row it reaches second"],
    ),
    (
        "According to the \"Deadlocks at a glance\" table, whose responsibility is it to catch a deadlock error and retry the transaction?",
        "The application's responsibility — the database detects and resolves the deadlock automatically by rolling back one transaction, but the application code must catch that specific error and retry the transaction from the beginning.",
        "medium", "remember", "deadlocks",
        "The application's responsibility, to catch the deadlock error and retry the transaction",
        ["The database's responsibility entirely, with no action required from the application", "The database administrator's responsibility, requiring manual intervention every time", "No one's responsibility; deadlocked transactions are simply lost permanently"],
    ),
]

SERIALIZABILITY = [
    (
        "Running Transaction A (a 10% bonus) completely, then Transaction B (a flat 50.00 deduction) completely, produces 1050.00. Running them in the opposite order produces 1045.00, a genuinely different final number.\n\nWhat does serializability actually demand, given that both orderings produce different results?",
        "Serializability does not demand a single specific answer; it demands that whatever result a concurrent execution produces must match one of these valid serial orderings (1050.00 or 1045.00), not some third, impossible value that neither ordering could have produced.",
        "easy", "understand", "serializability",
        "That the result of concurrent execution matches one of the valid serial orderings, not some impossible third value neither ordering could produce",
        ["That both transactions must always produce exactly 1050.00, regardless of order", "That the two transactions can never be allowed to run in different orders", "That the database must always choose the mathematically larger of the two possible results"],
    ),
    (
        "The lesson describes a lost update as \"not just an inconvenient bug; it is a violation of serializability.\"\n\nWhy does a lost update specifically violate serializability, when neither \"A then B\" nor \"B then A\" would have caused it?",
        "A strictly sequential execution guarantees each transaction sees the previous one's completed result before making its own change, so a lost update, a result that no valid serial ordering could ever have produced, is a genuine correctness violation, not just an unlucky outcome.",
        "medium", "analyze", "serializability",
        "Neither valid serial ordering (A-then-B or B-then-A) would ever cause a lost update, since sequential execution guarantees each transaction sees the prior one's completed result — making a lost update a result no serial ordering could produce",
        ["A lost update is actually a valid outcome under one of the two possible serial orderings", "Serializability only concerns dirty reads, not lost updates, so this claim is inaccurate", "A lost update violates atomicity, not serializability, and the lesson conflates the two"],
    ),
    (
        "What is the precise relationship between the SERIALIZABLE isolation level and the concept of serializability itself, according to the lesson?",
        "SERIALIZABLE is the one isolation level that fully guarantees serializability for every transaction run under it; the other levels (READ COMMITTED and REPEATABLE READ) are deliberate, named exceptions to full serializability, each permitting specific, well-understood anomalies in exchange for better performance.",
        "medium", "understand", "serializability",
        "SERIALIZABLE is the one isolation level that fully guarantees serializability; the other levels are deliberate, named exceptions permitting specific anomalies for better performance",
        ["Serializability and the SERIALIZABLE isolation level are unrelated concepts that happen to share a name", "Every isolation level, including READ COMMITTED, fully guarantees serializability", "SERIALIZABLE is a weaker guarantee than what READ COMMITTED provides"],
    ),
    (
        "Running a transaction under SERIALIZABLE guarantees the combined result of concurrent transactions will always be equivalent to some serial ordering of them, at a specific cost.\n\nWhat cost does the lesson identify?",
        "The database sometimes forcibly aborts one of the transactions and requires a retry — exactly the trade-off discussed when isolation levels were first introduced, where stricter guarantees mean more waiting and potential retries under concurrent load.",
        "medium", "apply", "serializability",
        "The database sometimes forcibly aborts a transaction, requiring a retry, in exchange for the full serializability guarantee",
        ["There is no cost at all; SERIALIZABLE is strictly better than every other level with no trade-off", "The cost is that SERIALIZABLE transactions can never involve more than one table", "The cost is that SERIALIZABLE disables write-ahead logging for that transaction"],
    ),
    (
        "The chapter's final lesson describes serializability as \"the standard every mechanism in this chapter ultimately serves.\"\n\nHow do locking, isolation levels, and deadlock detection each relate to this one underlying standard?",
        "Locking, isolation levels, and deadlock detection are all the practical machinery a database uses to approach or fully guarantee the serializability standard, whether by preventing conflicting access (locking), choosing how strictly to enforce it (isolation levels), or breaking cycles that would otherwise stall progress entirely (deadlock detection).",
        "hard", "analyze", "serializability",
        "They are the practical machinery a database uses to approach or fully guarantee the serializability standard, each addressing a different piece of achieving it",
        ["They are three unrelated features that happen to appear in the same chapter by coincidence", "Serializability is only relevant to the SERIALIZABLE isolation level and has no connection to locking or deadlocks", "Locking and deadlock detection replace the need for isolation levels entirely"],
    ),
    (
        "According to the \"Serializability at a glance\" table, what specifically violates serializability?",
        "Lost updates and similar anomalies that no serial ordering could produce — any concurrent execution result that couldn't have arisen from running the same transactions strictly one at a time, in any order, is a serializability violation.",
        "medium", "remember", "serializability",
        "Lost updates and similar anomalies that no valid serial (one-at-a-time) ordering could ever produce",
        ["Any transaction that takes longer than one second to complete", "Any transaction that uses more than one table in its statements", "Any transaction that runs under the READ COMMITTED isolation level"],
    ),
]

SYNTHESIS = [
    (
        "The double-booking scenario (why concurrency control is needed) and the lost update scenario (concurrency problems) both involve a read-then-write gap where a stale value gets acted on.\n\nWhat's the key difference between how each one manifests, given that both stem from the same underlying gap?",
        "The double-booking scenario is about two transactions both reading the same \"available\" state and both proceeding to act on it (a business-level conflict over a boolean flag); the lost update is about two transactions both reading the same numeric value and both computing a new value from it, where one computed result silently overwrites the other — both are instances of the same read-then-write timing gap, just applied to different kinds of data and outcomes.",
        "medium", "analyze", "concurrency-problems",
        "Both stem from the same read-then-write timing gap; double-booking involves two transactions acting on a shared availability flag, while a lost update involves two transactions computing new values from the same stale number",
        ["The two scenarios are actually completely unrelated problems with no shared root cause", "Double-booking is caused by a dirty read, while a lost update is caused by a phantom read", "Only the lost update scenario involves a genuine read-then-write gap; double-booking does not"],
    ),
    (
        "Locking (via FOR UPDATE) directly prevents a lost update by forcing the second transaction to wait. Isolation levels (like REPEATABLE READ) prevent non-repeatable reads by serving a consistent snapshot. Both mechanisms address concurrency problems, but through structurally different means.\n\nWhat's the fundamental difference between how locking and a stricter isolation level each solve their respective problems?",
        "Locking actively blocks a second transaction from proceeding until the first is done, coordinating transactions by making one wait for the other; a stricter isolation level instead changes what a transaction is allowed to see (a fixed snapshot), letting both transactions proceed without blocking each other, just with each one working from a consistent, unchanging view of the data.",
        "hard", "analyze", "isolation-levels",
        "Locking blocks one transaction until another finishes, coordinating through waiting; isolation levels change what a transaction is allowed to see (like a fixed snapshot), avoiding blocking while still ensuring internal consistency",
        ["Locking and isolation levels are two names for exactly the same underlying mechanism", "Isolation levels always block transactions, while locking never does, the reverse of their actual behavior", "Locking only works for SELECT statements, and isolation levels only work for UPDATE statements"],
    ),
    (
        "A deadlock arises specifically when locking is used to solve one problem (like a lost update) but introduces a new risk (two transactions waiting on each other's locks). Consistent lock ordering is the recommended prevention.\n\nWhy is consistent lock ordering described as a discipline the application must follow, rather than something the database enforces automatically?",
        "The database can detect and break a deadlock once it happens (by rolling back one transaction), but it has no way to know in advance what order any given transaction's business logic intends to lock rows in — preventing the cycle from forming in the first place requires the application's own code to consistently choose the same locking order across every transaction that might touch the same set of rows.",
        "hard", "apply", "deadlocks",
        "The database can only detect and break deadlocks after they occur; preventing them requires the application to consistently choose the same lock order in its own business logic, which the database cannot know or enforce on its own",
        ["The database actually does enforce consistent lock ordering automatically in PostgreSQL", "Deadlocks can only be prevented by disabling locking entirely, not by ordering", "Consistent lock ordering is only a suggestion with no actual effect on deadlock formation"],
    ),
    (
        "Serializability is described as the standard that locking, isolation levels, and deadlock detection all ultimately serve. The double-booking problem from the chapter's opening lesson is a serializability violation.\n\nHow would proper concurrency control (locking plus an appropriate isolation level) have prevented the double-booking outcome from the very first lesson, expressed in terms of serializability?",
        "With proper locking (the second passenger's booking attempt blocking until the first's transaction finished) or a strict enough isolation level, the combined result of the two overlapping booking transactions would be forced to match one of the two valid serial orderings, either \"A books, then B is correctly rejected\" or \"B books, then A is correctly rejected\", rather than the invalid outcome where both bookings succeeded, a result no serial ordering could ever produce.",
        "hard", "analyze", "serializability",
        "Proper locking or isolation would force the double-booking outcome to match a valid serial ordering (one passenger books, the other is correctly rejected), rather than the invalid outcome where both succeeded",
        ["Serializability has no actual bearing on the double-booking scenario from the opening lesson", "Proper concurrency control would have allowed both passengers to book the seat successfully", "Serializability only applies to numeric balance transfers, not to boolean availability flags like seat booking"],
    ),
]

SET1_SOURCES = [
    (WHY_CONCURRENCY_CONTROL_NEEDED, 0),
    (CONCURRENCY_PROBLEMS, 0),
    (LOCKING, 0),
    (ISOLATION_LEVELS, 0),
    (DEADLOCKS, 0),
    (SERIALIZABILITY, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    WHY_CONCURRENCY_CONTROL_NEEDED[1:]
    + CONCURRENCY_PROBLEMS[1:]
    + LOCKING[1:]
    + ISOLATION_LEVELS[1:]
    + DEADLOCKS[1:]
    + SERIALIZABILITY[1:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 6.2.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 6.2.2")
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
ws.title = "DBMS - MCQ - Unit 6.2"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 6 - Transactions and Reliability/6.2 - Concurrency Control - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
