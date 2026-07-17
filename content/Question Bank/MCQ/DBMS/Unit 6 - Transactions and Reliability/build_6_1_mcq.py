import random
import openpyxl

random.seed(101)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

WHAT_IS_A_TRANSACTION = [
    (
        "Rahul writes a money transfer as two separate UPDATE statements: subtract from one account, add to another. If the connection drops between the two statements, money vanishes entirely.\n\nWhat SQL concept exists specifically to prevent this?",
        "A transaction — a group of one or more statements that the database guarantees will either all succeed together or all fail together, with no in-between state ever left visible.",
        "easy", "understand", "what-is-a-transaction",
        "A transaction, which guarantees a group of statements either all succeed or all fail together",
        ["A foreign key, which ensures the two accounts reference each other correctly", "An index, which speeds up the two UPDATE statements", "A view, which combines the two accounts into one virtual table"],
    ),
    (
        "`BEGIN; UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1; UPDATE accounts SET balance = balance + 5000.00 WHERE account_id = 2; COMMIT;`\n\nWhat do BEGIN and COMMIT each do here?",
        "BEGIN starts a transaction, binding everything that follows into a single, indivisible unit; COMMIT ends the transaction, making every change inside permanent all at once, only once it runs successfully.",
        "easy", "remember", "what-is-a-transaction",
        "BEGIN starts the transaction; COMMIT makes every change inside it permanent all at once",
        ["BEGIN reads the current balances; COMMIT writes new balances without checking them", "BEGIN and COMMIT both just log the statements for debugging purposes", "BEGIN locks the table permanently; COMMIT unlocks it after each statement"],
    ),
    (
        "Inside a transaction, a SELECT run immediately after the two UPDATE statements (but before COMMIT) shows the changed balances (45000.00 and 17000.00). Then ROLLBACK runs, and a final SELECT shows the original balances again (50000.00 and 12000.00).\n\nWhat does this sequence demonstrate about what a connection can see of its own uncommitted work, and what ROLLBACK does?",
        "A connection can see its own uncommitted changes within the same transaction (hence the first SELECT showing 45000.00 and 17000.00), but ROLLBACK discards every change made since BEGIN entirely, as if none of it had ever happened, restoring the original values.",
        "medium", "analyze", "what-is-a-transaction",
        "A transaction can see its own uncommitted changes; ROLLBACK then discards all of those changes as if they never happened",
        ["A transaction cannot see its own changes until COMMIT runs; ROLLBACK has no visible effect", "ROLLBACK only undoes the first statement in a transaction, not all of them", "The SELECT before ROLLBACK actually shows the original values, and ROLLBACK changes them"],
    ),
    (
        "The lesson lists creating an order while reducing stock, registering a student while updating a seat count, and moving a support ticket between queues as examples beyond banking.\n\nWhat do all of these examples have in common that makes a transaction the right tool?",
        "In each case, two or more changes must succeed or fail together — whenever an application needs \"these changes happen together, or not at all,\" a transaction is the tool that guarantees it, regardless of the specific business domain.",
        "medium", "understand", "what-is-a-transaction",
        "Each involves two or more changes that must succeed or fail together as one unit, regardless of the specific business domain",
        ["Each one only ever involves a single UPDATE statement, making transactions unnecessary", "Each one requires a foreign key constraint to work correctly", "Each one is an example where ROLLBACK should never be used"],
    ),
    (
        "If the connection dropped after the first UPDATE ran but before the second one did, in a version of Rahul's transfer with no BEGIN/COMMIT wrapping at all, what would the database have no way of knowing?",
        "That Sanjay's credit was ever supposed to happen — with no transaction boundary, the database treats each UPDATE as its own independent unit, so it has no way of knowing the two statements were meant to be linked, and 5000.00 would simply be gone.",
        "medium", "apply", "what-is-a-transaction",
        "That the second UPDATE (crediting the other account) was ever supposed to happen at all, since nothing links the two statements together",
        ["That the first UPDATE had a syntax error, since the database always detects such errors automatically", "That the accounts table needed a CHECK constraint added to it", "That the connection itself had dropped, since databases cannot detect connection loss"],
    ),
    (
        "According to the \"Transactions at a glance\" summary, what happens to changes made between BEGIN and COMMIT before COMMIT actually runs?",
        "They are provisional — visible only within this transaction until committed, meaning other connections cannot see them yet, and they aren't permanent until COMMIT actually completes.",
        "medium", "remember", "what-is-a-transaction",
        "They are provisional and visible only within this transaction until COMMIT actually runs",
        ["They are immediately permanent and visible to every other connection", "They are discarded automatically unless ROLLBACK is called within one second", "They are written to a separate table until COMMIT merges them into the real one"],
    ),
    (
        "Meera wants to send 2000.00 to Sanjay but decides midway through to cancel the transfer entirely, using BEGIN, two UPDATE statements, and then ROLLBACK.\n\nWhat would a final SELECT show for both balances after this sequence?",
        "Both balances unchanged from their original values, since ROLLBACK discards every change made since BEGIN as if none of it had ever happened, confirming the cancelled transfer left no trace at all.",
        "medium", "apply", "what-is-a-transaction",
        "Both balances would show their original, unchanged values, since ROLLBACK discarded the transfer entirely",
        ["Meera's balance would show the deduction, but Sanjay's would not show the credit", "Both balances would reflect the 2000.00 transfer, since the UPDATE statements already ran", "The account rows would be deleted entirely since the transaction was cancelled"],
    ),
]

ATOMICITY = [
    (
        "A transaction with a CHECK constraint (balance >= 0) tries an UPDATE that would push a balance to -10000.00. The database rejects the statement, and the transaction fails as a whole, even though nobody typed ROLLBACK.\n\nWhat does this demonstrate about atomicity beyond explicit ROLLBACK?",
        "Atomicity is the promise that a transaction's changes are indivisible regardless of how or why the transaction failed to finish — an unplanned failure, like a constraint violation, triggers the exact same all-or-nothing guarantee as an explicit ROLLBACK would.",
        "easy", "understand", "atomicity-all-or-nothing",
        "Atomicity's all-or-nothing guarantee applies to unplanned failures like constraint violations, not just explicit ROLLBACK commands",
        ["Atomicity only applies when ROLLBACK is explicitly called by the application", "A constraint violation always allows the transaction to partially commit", "Atomicity has no effect on constraint violations; only consistency does"],
    ),
    (
        "A transaction consisting of just `BEGIN; UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1; COMMIT;` is described as \"perfectly atomic\" even though it deducts money without crediting it anywhere.\n\nWhy is this not an atomicity failure?",
        "Atomicity only guarantees that a transaction's own set of changes are indivisible; it says nothing about whether those changes, once committed, make logical sense — it's still the application's responsibility to group the correct statements together in the first place, and this is a logic bug, not an atomicity failure.",
        "medium", "analyze", "atomicity-all-or-nothing",
        "Atomicity only guarantees indivisibility of whatever statements were grouped together; it can't detect that the wrong statements were grouped in the first place",
        ["It actually is an atomicity failure, and the lesson describes an edge case where atomicity breaks down", "Atomicity would have automatically added a matching credit statement if configured correctly", "This transaction violates atomicity because it only contains one statement instead of two"],
    ),
    (
        "A three-statement transaction opens a new account for Farah Ali (INSERT) and funds it by deducting from Meera's account (UPDATE) and crediting the new account (UPDATE). If the INSERT fails because account_id = 3 already exists, what happens to the two UPDATE statements?",
        "Neither UPDATE takes effect either — atomicity applies to however many statements sit between BEGIN and COMMIT, not just two, so all three statements succeed together or none of them take effect, keeping Meera's balance untouched rather than deducting money toward an account that was never created.",
        "medium", "apply", "atomicity-all-or-nothing",
        "Neither UPDATE takes effect, since all three statements in the transaction succeed together or fail together",
        ["Both UPDATEs still commit normally, since only the INSERT failed", "Only the UPDATE crediting the new account fails; the deduction from Meera still commits", "The transaction succeeds by skipping the failed INSERT and running only the UPDATEs"],
    ),
    (
        "According to the \"Atomicity at a glance\" table, what's the difference in outcome between \"any statement fails, for any reason\" and \"a committed transaction later turns out to be the wrong logic\"?",
        "When any statement fails for any reason, every change in that transaction is discarded — that's atomicity working. But a committed transaction with flawed logic is not an atomicity issue at all, since atomicity only protects the grouping of statements, not the correctness of what was grouped.",
        "medium", "understand", "atomicity-all-or-nothing",
        "A failed statement causes the whole transaction to be discarded (atomicity working); a committed transaction with bad logic is not an atomicity issue, since atomicity doesn't judge correctness",
        ["Both scenarios are treated identically by atomicity, which reverses any bad outcome automatically", "A committed transaction with wrong logic is always automatically rolled back by atomicity", "Atomicity only concerns itself with logic correctness, not statement grouping"],
    ),
    (
        "Attempting to move 100000.00 from Sanjay's account (which only has 12000.00) to Meera's account, under the balance_not_negative constraint, is rejected. The transaction fails as a whole.\n\nWhat confirms that Sanjay's balance is genuinely unaffected, rather than partially deducted?",
        "A closing SELECT confirms Sanjay's balance is still 12000.00 — since the statement violated the constraint, the transaction failed as a whole and the UPDATE never took effect at all, exactly the atomicity guarantee in action.",
        "medium", "apply", "atomicity-all-or-nothing",
        "A closing SELECT showing Sanjay's balance unchanged at 12000.00, confirming the rejected UPDATE never partially applied",
        ["Nothing confirms this; the balance could theoretically be partially deducted with no way to check", "The balance would show a negative number temporarily before resetting to 12000.00", "The account row would be deleted entirely rather than left unchanged"],
    ),
    (
        "The conclusion of the atomicity lesson notes it's \"still up to the application to decide which statements belong grouped together in the first place.\"\n\nWhat responsibility does this leave with the application developer, distinct from what the database guarantees?",
        "The database guarantees that whatever statements are grouped inside BEGIN and COMMIT happen together, but the developer is responsible for correctly identifying and grouping the statements that actually need to succeed or fail together for a given business operation — atomicity can't infer that on its own.",
        "hard", "analyze", "atomicity-all-or-nothing",
        "The developer must correctly identify which statements belong together for a business operation; the database only guarantees that whatever is grouped happens together",
        ["The application must manually implement atomicity itself; the database provides no help at all", "The developer is responsible only for writing the COMMIT statement; grouping is automatic", "Atomicity guarantees correct grouping automatically, removing this responsibility from the developer"],
    ),
    (
        "The atomicity lesson distinguishes an explicit ROLLBACK from an unplanned constraint violation as two different triggers for the same underlying guarantee.\n\nAccording to the \"Atomicity at a glance\" table, do both triggers produce the same discard behavior?",
        "Yes — both an explicit ROLLBACK and any statement failing for any reason produce the exact same outcome: every change in that transaction is discarded, whether the discard was triggered deliberately or by an unplanned error.",
        "medium", "understand", "atomicity-all-or-nothing",
        "Yes, both an explicit ROLLBACK and an unplanned failure produce the same discard behavior for the whole transaction",
        ["No, an explicit ROLLBACK discards everything, but a constraint violation only discards the failing statement", "No, a constraint violation discards everything, but an explicit ROLLBACK only discards the most recent statement", "No, only an explicit ROLLBACK is guaranteed to discard changes; failures are handled inconsistently"],
    ),
]

CONSISTENCY = [
    (
        "\"A transaction could atomically commit a balance of -500.00 if nothing was stopping it, perfectly all-or-nothing, and perfectly wrong.\"\n\nWhat guarantee closes this gap that atomicity alone leaves open?",
        "Consistency — the guarantee that a transaction can only move a database from one valid state to another valid state, never into a state that breaks the rules the database has been told to enforce, such as a CHECK constraint against negative balances.",
        "easy", "understand", "consistency-valid-states-only",
        "Consistency, which ensures a transaction can only move the database between states that satisfy its declared rules",
        ["Isolation, which hides the negative balance from other transactions", "Durability, which ensures the negative balance survives a crash", "Atomicity, which already prevents negative balances on its own"],
    ),
    (
        "A CHECK (balance >= 0) constraint blocks a transaction from pushing Meera's balance to -10000.00, and the whole transaction rolls back as a result.\n\nHow does the lesson describe atomicity and consistency working together in this scenario?",
        "Atomicity ensures the rejected statement does not leave a half-applied transaction behind, while consistency is the reason the statement was rejected in the first place, since it would have produced an invalid row — the two guarantees serve distinct but complementary roles.",
        "medium", "understand", "consistency-valid-states-only",
        "Consistency is why the statement gets rejected (it would create an invalid state); atomicity ensures the rejection doesn't leave a half-applied transaction behind",
        ["Atomicity is why the statement gets rejected; consistency ensures no half-applied transaction remains", "The two guarantees do exactly the same thing in this scenario, making one of them redundant", "Consistency only applies after COMMIT, so it plays no role in this rejection"],
    ),
    (
        "A transaction tries to INSERT an order referencing customer_id 99, which doesn't exist in the customers table.\n\nWhat kind of constraint causes this to be rejected, and what does the lesson say this illustrates about what \"consistency\" covers beyond CHECK constraints?",
        "A foreign key constraint causes the rejection — the lesson emphasizes that foreign keys are just as much a consistency rule as CHECK constraints, since consistency covers every declared rule (CHECK, foreign keys, NOT NULL, UNIQUE) that defines what a valid database state looks like.",
        "medium", "apply", "consistency-valid-states-only",
        "A foreign key constraint; consistency covers foreign keys just as much as CHECK constraints, since both define what counts as a valid state",
        ["A UNIQUE constraint; consistency only ever applies to CHECK and UNIQUE, never foreign keys", "No constraint is involved; this failure is purely an atomicity issue", "A NOT NULL constraint on the customer_id column specifically"],
    ),
    (
        "A transaction deducts 5000.00 from Meera's account without crediting it anywhere. It commits successfully, since balance >= 0 still holds, but the total money across the bank has silently decreased.\n\nWhy couldn't the database's consistency guarantee catch this?",
        "Database-level consistency only enforces what has been explicitly declared as a constraint; \"total money across all accounts must never change\" was never expressed as a constraint, so the database has no way to know about or protect that particular business rule.",
        "medium", "analyze", "consistency-valid-states-only",
        "The rule was never declared as a database constraint, and consistency can only enforce rules the database has been explicitly told about",
        ["The database's consistency guarantee is broken and needs to be fixed by the vendor", "This is actually a violation the database should have caught automatically, regardless of constraints", "Consistency only applies to single-row constraints, never to sums across multiple rows"],
    ),
    (
        "According to the \"Consistency at a glance\" table, who is responsible for enforcing \"business rules with no matching constraint,\" such as \"total money in the system stays constant\"?",
        "The application, by grouping the right statements into one transaction — since the database can only enforce rules it has been explicitly told about through declared constraints, any rule without a matching constraint falls to the application to protect.",
        "medium", "remember", "consistency-valid-states-only",
        "The application, by correctly grouping the statements that together satisfy the business rule into one transaction",
        ["The database, automatically, exactly like CHECK constraints and foreign keys", "Neither the database nor the application; such rules simply cannot be enforced at all", "The database administrator, by manually auditing every transaction after it commits"],
    ),
    (
        "Why is consistency described as \"a shared responsibility\" between the database and the application, rather than something the database alone guarantees?",
        "The database automatically enforces every rule it has been explicitly told about through constraints (CHECK, foreign keys, NOT NULL, UNIQUE), but any business rule that was never expressed as a constraint remains entirely the application's responsibility to protect, typically by correctly grouping statements into transactions.",
        "hard", "analyze", "consistency-valid-states-only",
        "The database enforces declared constraints automatically, but any business rule not expressed as a constraint is left entirely to the application to protect",
        ["The application enforces all constraints, while the database only handles business rules", "Consistency is entirely the database's responsibility, and the application plays no role at all", "The two share responsibility by each enforcing exactly half of every declared constraint"],
    ),
    (
        "A CHECK constraint requiring `amount > 0` is added to an orders table, and a transaction attempts to insert an order with `amount = -200.00`.\n\nWhat happens, and what does the closing SELECT confirm?",
        "The INSERT is rejected for violating the constraint, the transaction commits nothing, and a closing SELECT confirms the orders table is still empty, exactly the consistency guarantee preventing an invalid row from ever being committed.",
        "medium", "apply", "consistency-valid-states-only",
        "The INSERT is rejected, nothing commits, and the closing SELECT confirms the table remains empty",
        ["The INSERT succeeds, but the amount is automatically corrected to a positive value", "The INSERT succeeds with the negative amount, since CHECK only warns rather than blocks", "The entire orders table is dropped as a result of the constraint violation"],
    ),
]

ISOLATION = [
    (
        "Within a single transaction, a SELECT run right after an UPDATE (but before COMMIT) correctly shows the reduced balance.\n\nWhat does the lesson clarify isolation is NOT about, based on this example?",
        "Isolation is not about hiding a transaction's work from itself — a transaction always sees its own uncommitted changes; isolation is specifically about what a completely different, concurrently running transaction on a separate connection is allowed to see before this one commits.",
        "easy", "understand", "isolation-running-transactions-safely",
        "Isolation isn't about hiding a transaction's own changes from itself; it's about what other, concurrent transactions can see before this one commits",
        ["Isolation prevents a transaction from ever seeing its own uncommitted changes", "Isolation only applies once a transaction has already committed", "Isolation has nothing to do with concurrent transactions at all"],
    ),
    (
        "A second banking session checks Meera's balance while a transfer is still in progress, sitting between its UPDATE and its COMMIT.\n\nWith isolation guaranteed, what does the second session see, and why?",
        "It sees the balance left over from the already-committed prior state, not the in-progress uncommitted value, for as long as the first transaction remains uncommitted — only once COMMIT actually runs does the second session's next read see the new value.",
        "medium", "apply", "isolation-running-transactions-safely",
        "The previously committed balance, not the in-progress uncommitted change, until the first transaction actually commits",
        ["The in-progress, uncommitted balance, since isolation guarantees real-time visibility across sessions", "A blank or NULL value, since the row is locked during the transfer", "Whichever value the second session happened to read first, cached from an earlier query"],
    ),
    (
        "`SHOW transaction_isolation;` reports \"read committed\" as PostgreSQL's default.\n\nWhat does this default level already guarantee, according to the lesson?",
        "That a transaction never sees another transaction's uncommitted changes — exactly the behavior demonstrated with the concurrent balance check, where the second session only sees the committed value, never the in-progress one.",
        "medium", "understand", "isolation-running-transactions-safely",
        "That a transaction never sees another transaction's uncommitted changes",
        ["That every transaction automatically runs in complete isolation with zero possible interference of any kind", "That a transaction can see other transactions' uncommitted changes, but only read-only ones", "That isolation level has no effect unless explicitly configured by the developer"],
    ),
    (
        "Why does the lesson say isolation matters \"for correctness, not just comfort\"?",
        "Without isolation, a concurrent balance check could read a value that later gets rolled back, and any decision made based on that reading, such as approving a withdrawal because a balance looked sufficient, would be based on data that never actually existed as far as the database is concerned.",
        "medium", "analyze", "isolation-running-transactions-safely",
        "Without isolation, decisions could be made based on data that might later be rolled back and never actually existed",
        ["Isolation only affects how fast a query runs, with no bearing on correctness", "Isolation is purely a convenience feature with no real risk if disabled", "Isolation matters only for banking applications specifically, not general correctness"],
    ),
    (
        "According to the \"Isolation at a glance\" table, is a rolled-back change ever visible to any other transaction?",
        "No — a rolled-back change was never visible to any other transaction in the first place, since isolation ensures uncommitted (and thus potentially-to-be-rolled-back) work stays private until it actually commits.",
        "medium", "remember", "isolation-running-transactions-safely",
        "No, a rolled-back change was never visible to any other transaction in the first place",
        ["Yes, but only for the brief moment before the ROLLBACK command actually runs", "Yes, any transaction that happened to be reading at that exact instant would see it", "It depends entirely on the isolation level, with no guarantee under any of them"],
    ),
    (
        "What is an isolation level, according to the lesson's brief introduction of the term?",
        "A named setting, per database connection, that controls exactly how much of one transaction's in-progress work a concurrent transaction is allowed to see — the specific named levels and the problems each prevents are covered in more depth in a later chapter.",
        "medium", "understand", "isolation-running-transactions-safely",
        "A per-connection setting that controls how much of a transaction's in-progress work concurrent transactions are allowed to see",
        ["A fixed, unchangeable property of the database that cannot be configured", "A setting that controls how many transactions can run at the same time in total", "A measurement of how many statements a single transaction is allowed to contain"],
    ),
    (
        "Checking the current isolation level with SHOW transaction_isolation, then running a transaction that updates Sanjay's balance by 1000.00 without committing, a SELECT within that same transaction shows the updated balance (13000.00).\n\nWhy does this SELECT show the new value even though COMMIT hasn't run yet?",
        "A transaction always sees its own uncommitted changes, regardless of isolation level — isolation governs what other, separate transactions can see, not what a transaction can see of its own in-progress work.",
        "medium", "apply", "isolation-running-transactions-safely",
        "A transaction always sees its own uncommitted changes; isolation only restricts what other, separate transactions can see",
        ["It shouldn't show the new value; this would actually be a bug in the database", "It only works because the isolation level was set to the loosest possible option", "SELECT always shows the new value regardless of which transaction made the change"],
    ),
]

DURABILITY = [
    (
        "Once COMMIT finishes for a balance transfer, what does durability guarantee about the new balance, even if the server loses power one second later?",
        "The change is not sitting only in server memory waiting to disappear; the database has already made sure this change is recorded somewhere that survives a crash, before it ever reported success back to the application.",
        "easy", "understand", "durability-surviving-a-crash",
        "The change is already recorded somewhere durable, not just in memory, guaranteeing it survives even an immediate crash",
        ["The change is guaranteed only if the server happens to be backed up that day", "Durability only applies to changes older than 24 hours, not immediate ones", "The change is safe only if no other transaction has run since the COMMIT"],
    ),
    (
        "How does the lesson distinguish durability's promise from isolation's promise?",
        "Isolation was about what other transactions can see while a transaction is still in progress; durability is about what happens to a transaction's result after it has already finished successfully — two different points in a transaction's lifecycle.",
        "medium", "analyze", "durability-surviving-a-crash",
        "Isolation concerns visibility during a transaction's progress; durability concerns what happens to the result after it has already finished",
        ["The two guarantees are identical, just applied to different tables", "Isolation applies after COMMIT; durability applies before COMMIT, the reverse of their actual roles", "Durability is a stricter version of isolation with no independent meaning"],
    ),
    (
        "What technique do most relational databases, including PostgreSQL, use to deliver on the durability promise, and what's the core rule behind it?",
        "Write-ahead logging — before a transaction is allowed to report success, its changes are first written to a durable log on disk; if the server crashes immediately after, that log is what the database replays on restart to reconstruct any committed work not yet fully applied to the main data files.",
        "medium", "understand", "durability-surviving-a-crash",
        "Write-ahead logging: changes are written to a durable log before a transaction is allowed to report success, letting a crash-time replay reconstruct committed work",
        ["In-memory caching: changes are kept in RAM and periodically saved, with no log involved", "Automatic table backups taken once per day at a scheduled time", "Replication to a second server that runs entirely independently"],
    ),
    (
        "PostgreSQL's `synchronous_commit` setting, when turned off, would make commits faster but reopen a specific risk.\n\nWhat risk does turning this setting off reintroduce?",
        "A very recent commit could theoretically be lost if the server crashed in the narrow window before its record was actually written to durable storage — turning off synchronous_commit trades away part of the durability guarantee for speed.",
        "medium", "apply", "durability-surviving-a-crash",
        "A very recent commit could be lost if the server crashed before its record was actually written to durable storage",
        ["No risk at all; synchronous_commit only affects how fast queries display results", "The risk of a deadlock forming between two concurrent transactions", "The risk that a constraint violation would be silently ignored instead of rejected"],
    ),
    (
        "\"A crash during an uncommitted transaction is expected to lose that transaction's work entirely, which is exactly what atomicity already promises.\"\n\nWhat does this reveal about the boundary between where atomicity's job ends and durability's job begins?",
        "Durability only ever protects a transaction once it has fully committed; a transaction that never reaches COMMIT is supposed to disappear on failure (whether an explicit ROLLBACK or a crash), which is atomicity's job — durability's job begins exactly where atomicity's job for that transaction ends.",
        "hard", "analyze", "durability-surviving-a-crash",
        "Durability protects a transaction only after it has committed; atomicity is responsible for ensuring uncommitted work disappears cleanly on any kind of failure, including a crash",
        ["Durability and atomicity both protect uncommitted work equally, with full overlap", "Durability is responsible for uncommitted work, and atomicity only applies after COMMIT, the reverse of their actual roles", "There is no boundary; the two properties are identical in scope"],
    ),
    (
        "According to the \"ACID at a glance, all four properties together\" summary, what does durability guarantee specifically?",
        "Once committed, a transaction's changes survive any crash — the fourth and final property, closing the loop that atomicity, consistency, and isolation open by ensuring a committed result is truly permanent.",
        "medium", "remember", "durability-surviving-a-crash",
        "Once a transaction commits, its changes survive any crash",
        ["A transaction's statements always succeed together or fail together", "A transaction can only move the database between valid states", "Concurrent transactions never see each other's uncommitted changes"],
    ),
    (
        "After checking synchronous_commit and then committing a transaction that adds 500.00 to Sanjay's balance, the lesson asks why that result would still hold even if the server crashed the instant after COMMIT returned.\n\nWhat's the reasoning behind why the balance can be trusted?",
        "COMMIT would not have returned successfully until the change was already recorded somewhere a crash cannot erase — durability guarantees that the success signal itself only comes after the change is durably logged, so an immediate crash afterward cannot undo it.",
        "medium", "apply", "durability-surviving-a-crash",
        "COMMIT only reports success after the change is already durably recorded, so an immediate crash afterward cannot undo it",
        ["The balance would only be safe if a manual backup had been taken that same day", "COMMIT reports success immediately, before any durability guarantee applies, so the result would be lost", "The balance is only safe because synchronous_commit was turned off for speed"],
    ),
]

SYNTHESIS = [
    (
        "Atomicity groups statements together, consistency defines what a valid resulting state looks like, isolation controls what concurrent transactions can see mid-flight, and durability guarantees a committed result survives a crash.\n\nWhich ACID property would be violated if a transaction committed a balance of -500.00, when a CHECK (balance >= 0) constraint exists?",
        "None of them would actually allow this — consistency specifically prevents a transaction from committing a state that violates a declared constraint like CHECK (balance >= 0); the transaction would be rejected before it could ever reach that invalid committed state.",
        "medium", "analyze", "consistency-valid-states-only",
        "None; consistency would prevent this by rejecting the transaction before it could commit an invalid state",
        ["Atomicity would be violated, since the transaction technically completed", "Isolation would be violated, since another transaction might see the negative balance first", "Durability would be violated, since the negative balance would need to survive a crash"],
    ),
    (
        "Rahul's earlier lesson showed a transaction failing due to a CHECK constraint violation, with the whole transaction rolling back automatically (atomicity). The isolation lesson showed a concurrent session unable to see an in-progress, uncommitted transfer.\n\nHow do atomicity and isolation work together to protect a concurrent balance check from ever seeing a transaction that will eventually fail and roll back?",
        "Isolation ensures the concurrent session never sees the uncommitted, in-progress change in the first place (since uncommitted work stays invisible to others); atomicity then guarantees that if the transaction does fail, none of its changes ever become permanent — together, a concurrent reader is protected both from seeing premature work and from that work ever becoming a committed reality if it fails.",
        "hard", "analyze", "isolation-running-transactions-safely",
        "Isolation hides uncommitted, in-progress work from concurrent transactions; atomicity ensures that if the transaction fails, none of its changes become permanent — together they prevent a concurrent reader from ever seeing or acting on work that will fail",
        ["Isolation and atomicity are unrelated; only durability protects concurrent readers", "Atomicity hides in-progress work, and isolation guarantees rollback on failure, the reverse of their actual roles", "Only isolation matters here; atomicity has no bearing on what a concurrent transaction sees"],
    ),
    (
        "Durability's write-ahead logging ensures a committed change is recorded somewhere a crash cannot erase, before COMMIT reports success. Atomicity ensures an uncommitted transaction's partial work disappears on a crash.\n\nWhat would happen to a transaction that was mid-flight (past its first UPDATE but before COMMIT) at the exact moment of a server crash, combining what both lessons establish?",
        "The transaction's work would be lost entirely, and correctly so: durability makes no promise about uncommitted work, since it only protects transactions that have already committed, and atomicity already guarantees that an incomplete transaction should never partially survive — the two properties agree on this outcome rather than conflicting.",
        "hard", "analyze", "durability-surviving-a-crash",
        "The transaction's work would be entirely and correctly lost, since durability only protects committed work, and atomicity guarantees incomplete transactions never partially survive",
        ["Durability would still preserve whatever part of the transaction had already run before the crash", "Atomicity and durability would conflict, leaving the database in an undefined state", "The transaction would be automatically retried and completed by the recovery process"],
    ),
    (
        "Across all four ACID properties, which one is uniquely concerned with the interaction between multiple transactions running at the same time, rather than the correctness of a single transaction on its own?",
        "Isolation — atomicity, consistency, and durability all describe guarantees about a single transaction's own correctness (its statements succeeding together, its result being valid, and its result surviving a crash), while isolation is the one property specifically about what concurrently running transactions are allowed to see of each other.",
        "medium", "understand", "isolation-running-transactions-safely",
        "Isolation, since atomicity, consistency, and durability all describe a single transaction's own correctness, while isolation specifically governs concurrent interaction",
        ["Atomicity, since it involves grouping multiple statements together", "Consistency, since it involves multiple constraints working together", "Durability, since it involves the log and the data files working together"],
    ),
    (
        "Rahul's transfer feature, by the end of this chapter, groups statements atomically, only ever commits valid states, isolates concurrent transactions, and survives a crash once committed.\n\nWhich single sentence best captures what the four ACID properties together let Rahul promise a customer?",
        "That a completed transfer, once confirmed, genuinely happened exactly as described, with no partial effects, no invalid states, no interference from other simultaneous transfers, and no risk of vanishing due to a crash — the combination of all four properties is what makes \"your transfer succeeded\" a statement that can be trusted unconditionally.",
        "medium", "understand", "durability-surviving-a-crash",
        "A completed transfer genuinely happened exactly as described, with no partial effects, invalid states, concurrent interference, or risk of loss from a crash",
        ["That a transfer will always complete successfully, with failures being impossible", "That a transfer will run faster than it would without any of the four properties", "That a transfer only needs one of the four properties to be trustworthy, with the others being optional"],
    ),
]

SET1_SOURCES = [
    (WHAT_IS_A_TRANSACTION, 0),
    (ATOMICITY, 0),
    (CONSISTENCY, 0),
    (ISOLATION, 0),
    (DURABILITY, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    WHAT_IS_A_TRANSACTION[1:]
    + ATOMICITY[1:]
    + CONSISTENCY[1:]
    + ISOLATION[1:]
    + DURABILITY[1:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 6.1.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 6.1.2")
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
ws.title = "DBMS - MCQ - Unit 6.1"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 6 - Transactions and Reliability/6.1 - Transactions and ACID - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
