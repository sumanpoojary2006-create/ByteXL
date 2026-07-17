import random
import openpyxl

random.seed(137)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

INSIDE_THE_OPTIMIZER = [
    (
        "Priya's team wonders why the same query sometimes uses an index and sometimes doesn't, even though the index still exists.\n\nWhat does the lesson say the query optimizer actually does before running a query?",
        "The optimizer estimates the cost of several different possible plans (using table and index statistics) and picks whichever one it estimates will be cheapest to execute — it doesn't just always use an available index; it decides based on estimated cost.",
        "easy", "understand", "inside-the-query-optimizer",
        "It estimates the cost of several possible plans using statistics, and picks whichever plan it estimates will be cheapest to run",
        ["It always chooses whichever plan uses the most available indexes", "It runs every possible plan once and keeps the fastest actual result", "It always picks the plan that reads the fewest total tables, regardless of cost"],
    ),
    (
        "The optimizer's cost estimates come from statistics gathered by ANALYZE, things like how many distinct values a column has and how the values are distributed.\n\nWhat happens to plan quality if those statistics are stale, for example after a large bulk load that hasn't been followed by a fresh ANALYZE?",
        "The optimizer's cost estimates become inaccurate, since they're based on outdated statistics that no longer reflect the table's actual current size or data distribution, which can lead it to pick a plan that is no longer actually the cheapest one available.",
        "medium", "analyze", "inside-the-query-optimizer",
        "The optimizer's cost estimates become inaccurate, since they no longer reflect the table's real current size or distribution, potentially leading to a worse plan choice",
        ["Nothing changes; the optimizer always re-derives statistics fresh for every single query", "The query fails outright until ANALYZE is manually run again", "Stale statistics only affect INSERT statements, never SELECT query plans"],
    ),
    (
        "Even though an index exists on a column, the optimizer sometimes still chooses a sequential scan over an index scan for a query filtering on that column.\n\nWhy might the optimizer decide a sequential scan is actually the cheaper option here?",
        "If the filter is estimated to match a large fraction of the table's rows, jumping in and out of the index for each match plus the extra step of visiting the heap can end up costing more overall than simply reading straight through the table once — the index doesn't help when a query needs most of the table anyway.",
        "medium", "analyze", "inside-the-query-optimizer",
        "When a filter is estimated to match a large fraction of the table, reading straight through the table can be cheaper overall than repeatedly jumping through the index plus separate heap fetches",
        ["The optimizer only skips indexes when a table is completely empty", "Sequential scans are always chosen whenever a table has any index defined on it", "The optimizer never chooses a sequential scan once an index exists on the filtered column"],
    ),
    (
        "The lesson emphasizes that the optimizer picks the cheapest *estimated* plan, not necessarily the actual fastest one that would run.\n\nWhat does this distinction reveal about why a query can sometimes end up with a genuinely suboptimal plan?",
        "The optimizer's decision is only as good as its cost estimate, which is built from statistics and assumptions, not from actually running the query; if those estimates are wrong, for example due to stale statistics or unusual data distribution, the estimated-cheapest plan can turn out to not be the fastest plan in practice.",
        "medium", "understand", "inside-the-query-optimizer",
        "The optimizer's decision is only as good as its cost estimate, which is based on statistics rather than actually running the query, so a wrong estimate can lead to picking a plan that isn't truly the fastest",
        ["Estimated and actual plans are always identical, so this distinction has no practical consequence", "The optimizer always re-checks its estimate against the actual runtime before finalizing a plan", "This distinction only matters for write queries, never for SELECT statements"],
    ),
    (
        "`SELECT relname, n_live_tup FROM pg_stat_user_tables WHERE relname IN ('customers', 'orders');` is run to inspect the optimizer's row-count tracking.\n\nWhat does n_live_tup represent, and why does the lesson note it \"is not always perfectly up to date\"?",
        "n_live_tup is PostgreSQL's tracked estimate of how many rows a table currently holds, one of the statistics the optimizer consults; it's refreshed by a background process rather than instantly on every change, so a table that changed dramatically without a fresh statistics update can occasionally mislead the optimizer.",
        "medium", "understand", "inside-the-query-optimizer",
        "n_live_tup is the tracked estimate of a table's row count used by the optimizer, refreshed by a background process rather than instantly, so it can occasionally be stale after dramatic changes",
        ["n_live_tup is the exact, always-current row count, guaranteed accurate at every instant", "n_live_tup only tracks rows added in the current transaction, not the whole table", "n_live_tup is a manually maintained value that has nothing to do with the optimizer"],
    ),
    (
        "The \"optimizer's job, summarized\" table lists four steps: parse the query, generate candidate plans, estimate cost of each candidate, choose the cheapest estimated plan.\n\nAccording to that table, what happens during \"generate candidate plans,\" specifically?",
        "The optimizer produces multiple different valid ways to execute the same query, different scan methods, different join orders, and different join algorithms, before any cost estimation happens, giving it several real options to compare.",
        "medium", "remember", "inside-the-query-optimizer",
        "It produces different scan methods, different join orders, and different join algorithms as valid alternative ways to execute the same query, before cost estimation happens",
        ["It runs each candidate plan once to observe its actual real-world execution time", "It selects the final plan directly, skipping any later cost comparison", "It only ever generates one candidate plan per query, since only one plan can be valid"],
    ),
]

READING_EXPLAIN = [
    (
        "An EXPLAIN output line shows `Seq Scan on orders (cost=0.00..180.00 rows=8000 width=48)`.\n\nWhat do the two numbers in cost=0.00..180.00 represent?",
        "The first number (0.00) is the estimated startup cost, the cost before the first row can be returned, and the second number (180.00) is the estimated total cost to run the step to completion and return every row.",
        "easy", "remember", "reading-explain",
        "Estimated startup cost (before the first row is returned) and estimated total cost (to complete the entire step)",
        ["The minimum and maximum possible execution time in milliseconds", "The number of rows read and the number of rows returned", "The disk space used before and after the scan runs"],
    ),
    (
        "That same line reports rows=8000 and width=48.\n\nWhat do these two values tell the reader, according to the lesson?",
        "rows=8000 is the planner's *estimate* of how many rows this step will produce, not a guaranteed exact count, and width=48 is the estimated average size in bytes of each row produced by that step.",
        "easy", "understand", "reading-explain",
        "rows is the planner's estimated row count for that step (not a guaranteed exact number), and width is the estimated average row size in bytes",
        ["rows is the exact, guaranteed number of rows that will be returned, always accurate", "width is the number of columns in the result, and rows is the table's total row count", "Both numbers are only meaningful once the query has actually finished executing"],
    ),
    (
        "A plan shows a Bitmap Heap Scan step indented beneath a Bitmap Index Scan step.\n\nWhat does this indentation convey about how the steps relate to each other?",
        "Indentation reflects the plan's tree structure: an indented (child) step feeds its output up into the step above it (the parent), so the Bitmap Index Scan's results are consumed by the Bitmap Heap Scan above it, rather than the two running as unrelated independent steps.",
        "medium", "understand", "reading-explain",
        "Indentation shows the tree structure of the plan: an indented step feeds its results up into the step directly above it",
        ["Indentation is purely cosmetic formatting with no structural meaning", "Indented steps always run after every non-indented step has fully completed, with no data relationship", "Deeper indentation always means a slower, more expensive step regardless of tree position"],
    ),
    (
        "Comparing two candidate plans for the same query, one reports a total cost of 180.00 and the other reports 950.00, with EXPLAIN run without ANALYZE for both.\n\nWhat can the reader conclude, and what can they NOT yet conclude, from these numbers alone?",
        "They can conclude the optimizer estimated the first plan (cost 180.00) as cheaper than the second; they cannot yet conclude the first plan will actually run faster in practice, since plain EXPLAIN only shows estimates, not the plan actually being executed and timed.",
        "medium", "analyze", "reading-explain",
        "They can conclude the optimizer estimated the first plan as cheaper; they cannot conclude it will actually run faster, since plain EXPLAIN only shows estimates, not real execution timing",
        ["They can directly conclude the first plan will run over five times faster in real wall-clock time", "The two cost numbers are not comparable at all unless the query is first run with ANALYZE", "Cost numbers from EXPLAIN represent actual disk I/O counts, not estimates"],
    ),
    (
        "The lesson stresses that a cost of 8.51 for one query and 8.51 for a completely different query \"does not mean those two queries take the same real time to run.\"\n\nWhat is the correct way to interpret EXPLAIN's cost numbers, according to this point?",
        "Cost numbers are the optimizer's own internal relative units, meant only for comparing candidate plans against each other within the optimizer's own reasoning, not a measurement of actual seconds or milliseconds that can be compared meaningfully across unrelated queries.",
        "medium", "understand", "reading-explain",
        "Cost numbers are the optimizer's own relative units for comparing candidate plans against each other, not a measurement of actual time comparable across unrelated queries",
        ["Cost numbers are always directly proportional to milliseconds, just on a different numeric scale", "Cost numbers are only meaningful when the exact same query is run twice in a row", "Cost numbers represent the number of index entries scanned, nothing else"],
    ),
    (
        "The \"Your Turn\" exercise asks for EXPLAIN on `orders WHERE amount > 205000.00`, given that amount tops out around 210000.00 for the highest order_id.\n\nWhy does this condition produce a low estimated row count and low total cost in the plan?",
        "Since amount only reaches up to about 210000.00 at its highest, the condition amount > 205000.00 matches only a small slice of orders near the very top of the range, so the optimizer estimates very few matching rows, and a correspondingly low total cost, reflecting how selective the condition actually is.",
        "medium", "apply", "reading-explain",
        "The condition matches only a small slice of orders near the top of the amount range, so the optimizer estimates very few matching rows and a correspondingly low total cost",
        ["The low cost is unrelated to selectivity and instead reflects the table having very few total rows", "EXPLAIN always reports a low cost for any condition using a greater-than comparison", "The plan's cost is low because greater-than conditions never use the width value in their calculation"],
    ),
]

READING_EXPLAIN_ANALYZE = [
    (
        "Plain EXPLAIN only estimates a plan; EXPLAIN ANALYZE actually executes the query and reports real measurements alongside the estimates.\n\nWhat new information does EXPLAIN ANALYZE add that plain EXPLAIN does not have?",
        "Actual time (in milliseconds, showing real startup and total time per step) and actual rows and loops, the real measured numbers from actually running the query, compared directly against the planner's earlier estimates.",
        "easy", "understand", "reading-explain-analyze",
        "Actual time and actual rows/loops from really executing the query, shown alongside the planner's original estimates",
        ["A list of every index that could theoretically be created to speed up the query", "The exact SQL text that was rewritten internally by the optimizer", "A prediction of how the query will perform after the next ANALYZE runs"],
    ),
    (
        "A step reports `actual time=0.021..15.402 rows=7998 loops=1`.\n\nWhat does loops=1 tell the reader, and how would loops=3 change the interpretation of the actual time shown?",
        "loops=1 means this step ran once; if it instead showed loops=3, the actual time reported would be the time for a single execution of that step, and the real total cost paid by the query is that time multiplied by the number of loops, since the step ran multiple times (for example, once per outer row in a nested loop).",
        "medium", "analyze", "reading-explain-analyze",
        "loops=1 means the step executed once; loops=3 would mean the shown time is per single execution, and the real total cost is that time multiplied by the loop count",
        ["loops always equals the number of rows returned by that specific step", "loops has no effect on interpreting actual time; the reported time is already a grand total regardless", "loops=3 would mean the query encountered three separate errors before succeeding"],
    ),
    (
        "The lesson specifically warns to be careful running EXPLAIN ANALYZE on an UPDATE, INSERT, or DELETE statement, and recommends wrapping it in a transaction with ROLLBACK.\n\nWhy is this precaution necessary?",
        "EXPLAIN ANALYZE actually executes the query to gather its real measurements, so running it directly on a write statement would truly perform that write against the database; wrapping it in BEGIN ... ROLLBACK lets the real execution (and its real cost measurements) happen while ensuring the data change itself is undone afterward.",
        "medium", "apply", "reading-explain-analyze",
        "EXPLAIN ANALYZE actually executes the statement to measure it, so a write statement would really modify data; wrapping it in a transaction with ROLLBACK lets the measurement happen while undoing the actual change",
        ["EXPLAIN ANALYZE only estimates write statements and never actually runs them, making the precaution unnecessary", "ROLLBACK is needed only to reset the connection's statistics cache, not the data itself", "Write statements cannot be analyzed with EXPLAIN ANALYZE at all, under any circumstances"],
    ),
    (
        "Comparing a step's estimated rows=8000 against its actual rows=50 after running EXPLAIN ANALYZE reveals a large mismatch.\n\nWhat does a gap this large between estimated and actual rows suggest about the plan the optimizer chose?",
        "The optimizer likely built its plan around inaccurate statistics or assumptions, so the plan it judged cheapest based on the (wrong) estimate may not actually be the truly cheapest plan available, since a downstream step sized for 8000 rows but actually handling only 50 may not be the right shape of plan for the real data.",
        "hard", "analyze", "reading-explain-analyze",
        "It suggests the optimizer's plan was built on inaccurate statistics or assumptions, meaning the chosen plan may not actually be the cheapest one for the real data",
        ["It simply means the query returned fewer rows than requested by the LIMIT clause", "A mismatch like this is expected and meaningless, since estimated and actual rows are always different by design", "It indicates the table has been dropped and recreated since the last ANALYZE, with no other implication"],
    ),
    (
        "The comparison table lists plain EXPLAIN as \"Best for: a quick check of the chosen plan\" and EXPLAIN ANALYZE as \"Best for: diagnosing where estimates and reality diverge.\"\n\nWhat distinction between the two tools does this pair of descriptions capture?",
        "Plain EXPLAIN is suited to a fast, low-cost look at which plan the optimizer would choose without paying the cost of actually running the query, while EXPLAIN ANALYZE is suited to deeper diagnostic work, actually executing the query, that specifically investigates whether the optimizer's assumptions matched what really happened.",
        "medium", "understand", "reading-explain-analyze",
        "Plain EXPLAIN suits a fast, low-cost look at the chosen plan without running the query, while EXPLAIN ANALYZE suits deeper diagnostic work that actually executes the query to check estimates against reality",
        ["Both tools are described as equally suited to every use case, with no meaningful distinction", "Plain EXPLAIN is described as the only tool safe to use on write statements, unlike EXPLAIN ANALYZE", "EXPLAIN ANALYZE is described as faster to run than plain EXPLAIN in every case"],
    ),
    (
        "The comparison table's \"Safe for any statement\" row marks plain EXPLAIN as Yes, but marks EXPLAIN ANALYZE as \"Only if wrapped in a transaction with ROLLBACK for write statements.\"\n\nWhy does this asymmetry exist between the two tools specifically for write statements?",
        "Plain EXPLAIN never actually executes the statement, so it can never cause a real data change, making it safe on any statement including writes; EXPLAIN ANALYZE does execute the statement for real, so running it directly on an UPDATE, INSERT, or DELETE would genuinely modify data unless that execution is wrapped in a transaction that gets rolled back afterward.",
        "hard", "analyze", "reading-explain-analyze",
        "Plain EXPLAIN never executes the statement, so it's safe on writes; EXPLAIN ANALYZE does execute for real, so a write statement would genuinely modify data unless wrapped in a rolled-back transaction",
        ["The asymmetry exists because EXPLAIN ANALYZE cannot syntactically accept write statements at all", "Plain EXPLAIN is actually less safe, since it silently commits any write statement given to it", "There is no real asymmetry; both tools carry identical risk on write statements"],
    ),
]

JOIN_ALGORITHMS = [
    (
        "For each row in a small outer table, a nested loop join scans (or index-probes) the inner table looking for matches.\n\nWhen does the lesson say a nested loop join tends to be chosen as the cheapest option?",
        "When at least one side is small, or when an index exists to make each inner lookup cheap, since the cost is roughly the outer row count multiplied by the cost of each inner lookup, so keeping either the row count or the per-lookup cost small keeps the whole join affordable.",
        "medium", "understand", "join-algorithms",
        "When at least one side is small, or an index makes each inner lookup cheap, since cost scales with outer rows times per-lookup cost",
        ["Only when both tables involved have more than a million rows each", "Only when neither table has any index defined on the join column", "Nested loop joins are chosen randomly, independent of table size or indexes"],
    ),
    (
        "A hash join builds an in-memory hash table from one side (usually the smaller one) and then probes it once per row from the other side.\n\nWhy does this approach scale well for joining two large tables without a usable index?",
        "Building the hash table is roughly proportional to one side's size, and each probe against it is fast (close to constant time), so the overall cost stays close to proportional to the combined size of both tables, rather than growing with the product of both tables' sizes the way a naive nested loop without an index would.",
        "medium", "analyze", "join-algorithms",
        "The hash table build cost scales with one side's size, and each probe is fast, keeping overall cost close to proportional to the combined table sizes rather than their product",
        ["A hash join always requires both tables to already be sorted on the join column first", "A hash join only works correctly when both tables fit entirely within a single disk page", "Hash joins scale poorly and are only chosen when tables are small enough to ignore performance"],
    ),
    (
        "A merge join works by walking two inputs that are already sorted (or cheaply sortable) on the join key, advancing through both in lockstep.\n\nWhat property of its inputs makes a merge join an efficient choice?",
        "Because both sides are already sorted on the join key, or a B-tree index can supply that order cheaply, the join can be done in a single pass over both sorted streams without needing to build any large auxiliary structure like a hash table, matching rows as it advances through both.",
        "medium", "understand", "join-algorithms",
        "Both inputs are already sorted (or cheaply sortable, e.g. via a B-tree) on the join key, letting the join complete in a single pass without a large auxiliary structure",
        ["Merge joins require that neither input has any index defined on the join column", "Merge joins are only used when the two tables being joined have identical row counts", "Merge joins always run entirely in memory regardless of how large the inputs are"],
    ),
    (
        "The optimizer picks among nested loop, hash join, and merge join based on estimated cost for the specific tables, sizes, and available indexes involved.\n\nWhat does this imply about trying to memorize \"the best\" join algorithm in general?",
        "There isn't one join algorithm that is universally best; which one is cheapest depends on the specific situation, table sizes, whether an index exists, whether inputs are already sorted, so the optimizer's job (and a tuner's understanding) is situational, not a single fixed rule to memorize.",
        "medium", "analyze", "join-algorithms",
        "There is no universally best join algorithm; the cheapest choice depends on the specific situation (table sizes, indexes, existing sort order), so it's a situational judgment, not a fixed rule",
        ["Hash joins are always the fastest option and should always be forced whenever possible", "Nested loop joins should always be avoided entirely, regardless of table size", "Merge joins are obsolete and never actually chosen by modern optimizers"],
    ),
    (
        "`SET enable_hashjoin = off;` is run before the same unfiltered customers/orders join, forcing the optimizer to pick a different algorithm than its default hash join.\n\nWhat is this technique useful for, and why does the lesson caution against leaving it disabled in a real application?",
        "It's a useful diagnostic technique for directly comparing what the optimizer would otherwise choose against its actual default preference, confirming why one algorithm was picked over another; but leaving hash joins permanently disabled would force the optimizer away from what is normally its genuinely cheapest choice for many real queries, hurting overall performance.",
        "medium", "apply", "join-algorithms",
        "It's useful for directly comparing the optimizer's forced alternative against its default choice as a diagnostic; leaving it disabled permanently would force away from what is normally the cheapest real choice for many queries",
        ["It's meant to be left on permanently, since disabling hash joins always improves performance", "It has no diagnostic value and only exists to reduce memory usage during a session", "It permanently disables hash joins for the entire database cluster, not just the current session"],
    ),
    (
        "The \"Your Turn\" exercise filters the customers/orders join down to `customer_id = 42`, a single customer, and asks which algorithm gets chosen compared to the unfiltered join's choice.\n\nWhy does this filter favor a Nested Loop over the Hash Join used for the unfiltered version?",
        "Filtering down to one customer makes the outer input tiny, exactly the situation described as ideal for a nested loop; using the index on orders for one targeted lookup beats the overhead of building an entire in-memory hash table just to serve a single row's worth of matching.",
        "medium", "apply", "join-algorithms",
        "Filtering to one customer makes the outer input tiny, the situation nested loop favors, since one targeted indexed lookup beats building a whole hash table for a single row",
        ["The filter has no effect on which algorithm is chosen; the optimizer always defaults to Hash Join regardless", "Nested Loop is chosen because customer_id = 42 disables hash joins automatically", "Filtering down to one customer forces a Merge Join, since sorting becomes trivial with one row"],
    ),
]

COMMON_BOTTLENECKS = [
    (
        "A query filtering on a column with no supporting index forces the database into a sequential scan, checking every row even though only a handful match.\n\nWhy does the lesson list a missing index as one of the most common, addressable performance bottlenecks?",
        "Without an index, the database has no way to jump directly to matching rows, so it must check every single row regardless of how few actually match, and this specific problem is directly fixable by creating the right index on the filtered column.",
        "easy", "understand", "common-bottlenecks",
        "Without an index, the database must check every row regardless of how few match, and this problem is directly fixable by adding the right index",
        ["Missing indexes only affect INSERT statements, never SELECT queries", "A missing index cannot be diagnosed with EXPLAIN and requires guesswork instead", "Missing indexes are rare in practice and not worth checking for first"],
    ),
    (
        "An application loop fetches a list of orders, then runs a separate query per order to fetch that order's customer, resulting in one query for the list plus one additional query per row.\n\nWhat is this pattern called, and why is it a bottleneck?",
        "This is called the N+1 queries problem: instead of one efficient query (or join) that fetches everything needed at once, the application pays the fixed overhead of a round trip to the database N extra times, once per row, which adds up quickly as the row count grows.",
        "medium", "understand", "common-bottlenecks",
        "The N+1 queries problem — instead of one efficient query, the application pays a separate round-trip cost once per row, which adds up as row count grows",
        ["This is called a deadlock, caused by two transactions waiting on each other's locks", "This is called index bloat, caused by too many indexes being maintained at once", "This is called a checkpoint storm, caused by too many WAL writes happening simultaneously"],
    ),
    (
        "A query filters with `WHERE CAST(order_date AS TEXT) = '2024-01-15'`, and even though order_date has an index, EXPLAIN shows a sequential scan instead of an index scan.\n\nWhy does wrapping the indexed column in CAST() defeat the index here?",
        "The index is built on the raw order_date values, not on the result of casting them to text; applying a function or cast to the column in the WHERE clause means the database would need to evaluate that transformation for every row to compare it, which the plain index on the untransformed column cannot support, so the optimizer falls back to scanning every row.",
        "medium", "analyze", "common-bottlenecks",
        "The index is built on the raw column values, not on the transformed result; applying CAST() in the WHERE clause means the plain index can't support the comparison, forcing a sequential scan",
        ["CAST() always improves index usage by making comparisons type-safe", "The index becomes permanently corrupted once a CAST() is used in any query against it", "Sequential scans happen here only because order_date lacks a NOT NULL constraint"],
    ),
    (
        "The fix for the CAST()-defeats-index problem generally involves either rewriting the filter to compare against the column's native type directly, or building an expression index matching the exact transformation used.\n\nWhy do both of these fixes work, from the same underlying principle?",
        "Both fixes restore a match between what's actually stored/searchable in an index and what the query is filtering on: rewriting the filter avoids transforming the column at all, while an expression index stores the transformed value directly, so either way, the query's filter condition once again lines up with something the index can actually search on directly.",
        "hard", "analyze", "common-bottlenecks",
        "Both restore alignment between what the index can search on and what the query filters by, either by avoiding the transformation in the query or by indexing the transformed value directly",
        ["Both fixes work by physically converting order_date's column type to TEXT permanently", "Only the expression index fix actually works; rewriting the filter has no real effect", "Both fixes work by disabling the query planner's cost-based optimization for that query"],
    ),
    (
        "The lesson names three recurring bottlenecks: a missing index on a selective column, the N+1 query problem, and a function or cast defeating an index. It notes most real-world performance problems trace back to \"a small handful of recurring patterns, not exotic, one-off causes.\"\n\nWhat practical implication does this framing have for how Priya should approach a slow query?",
        "Rather than assuming a slow query requires some rare, exotic explanation, it's more productive to first check for these few well-understood, common patterns, since they account for most real-world cases, before looking for something unusual.",
        "medium", "understand", "common-bottlenecks",
        "It's more productive to first check for these few common, well-understood patterns before assuming something rare or exotic is the cause, since they explain most real-world slow queries",
        ["It implies every slow query has a unique, unpredictable cause that must be diagnosed from scratch each time", "It implies these three patterns are the only possible causes of any performance problem, with no exceptions", "It implies performance problems are random and cannot be diagnosed systematically at all"],
    ),
    (
        "According to the \"Common Bottlenecks at a Glance\" table, how does a function or cast defeating an index \"show up\" in EXPLAIN, and what's listed as the fix?",
        "It shows up as EXPLAIN reporting a sequential scan despite a relevant index actually existing on the filtered column, and the fix is either removing the cast or function from the query, or building an expression index that matches the exact transformation being applied.",
        "medium", "remember", "common-bottlenecks",
        "EXPLAIN shows a sequential scan despite a relevant index existing; the fix is removing the cast/function, or building an expression index matching it",
        ["It shows up as a syntax error from EXPLAIN, and the fix is dropping the index entirely", "It shows up as an Index Only Scan being chosen incorrectly, and the fix is disabling the index", "It shows up as a much lower estimated cost than expected, and the fix is adding more RAM"],
    ),
]

ITERATIVE_TUNING = [
    (
        "The lesson frames performance tuning as a loop: measure with EXPLAIN ANALYZE, make one change, then measure again to see if it actually helped.\n\nWhy does the lesson insist on measuring again after each change, rather than assuming a change helped?",
        "A change that seems like it should help, like adding an index, isn't guaranteed to actually be used by the optimizer or to meaningfully improve real execution time, so re-measuring with EXPLAIN ANALYZE is the only way to confirm the change had the intended effect rather than assuming it based on intuition.",
        "medium", "understand", "iterative-performance-tuning",
        "A change that seems like it should help isn't guaranteed to actually improve real execution time, so re-measuring confirms the effect instead of relying on assumption",
        ["Re-measuring is only necessary for write queries, never for SELECT statements", "The lesson recommends skipping remeasurement once a change has been made, to save time", "EXPLAIN ANALYZE only needs to be run once per table, not once per change"],
    ),
    (
        "Establishing a baseline EXPLAIN ANALYZE result before making any changes is treated as an essential first step in the tuning loop.\n\nWhat purpose does this baseline serve for every change made afterward?",
        "It gives a concrete, measured starting point to compare every later change against, so it's possible to tell objectively whether a specific change actually improved things, made no real difference, or made things worse, rather than judging purely by feel.",
        "medium", "apply", "iterative-performance-tuning",
        "It gives a concrete starting point to objectively compare later changes against, showing whether each change actually helped, did nothing, or made things worse",
        ["The baseline is only used to decide which table to run VACUUM on", "A baseline is required by PostgreSQL before EXPLAIN ANALYZE can be run at all", "The baseline replaces the need for any further measurement after the first change"],
    ),
    (
        "The lesson recommends changing one thing at a time within the tuning loop, rather than making several changes together and then measuring once.\n\nWhy does changing one thing at a time make the tuning process more reliable?",
        "If several changes are made together and the result improves, there's no way to tell which specific change was responsible, or whether some changes actually hurt while others helped even more, canceling out in the total; isolating one change at a time keeps a clear, attributable link between a specific change and its specific measured effect.",
        "medium", "analyze", "iterative-performance-tuning",
        "Changing several things at once makes it impossible to tell which specific change was responsible for any improvement, or whether some changes actually hurt while others compensated",
        ["Changing one thing at a time is required because PostgreSQL only allows one schema change per session", "Making multiple changes at once always causes the database to reject all of them", "It doesn't actually matter, and the lesson only recommends it as an arbitrary style preference"],
    ),
    (
        "Step Two creates `idx_orders_status_date ON orders (status, order_date)`, a composite index matching both filter columns from the WHERE clause together, as the very first change attempted.\n\nWhy is a single, targeted composite index a reasonable first move here, rather than, say, separately indexing status and separately indexing order_date?",
        "The query filters on status and order_date together, so a single composite index matching both columns can serve that combined filter directly, keeping the change to one deliberate, targeted action, matching the discipline of changing exactly one thing per iteration rather than layering multiple separate indexes at once.",
        "medium", "apply", "iterative-performance-tuning",
        "The query filters on both columns together, so one composite index serving that combined condition keeps the change to a single, targeted action rather than adding multiple separate indexes at once",
        ["A composite index is chosen because PostgreSQL does not support creating two single-column indexes on the same table", "The composite index is unrelated to the query's filter and is added purely as a general best practice", "Separate indexes on status and order_date would have been syntactically invalid in this case"],
    ),
    (
        "In Step Four, if the actual business need only wants the top 10 customers by refund total, adding `LIMIT 10` to the query is treated as \"itself a legitimate next iteration,\" worth measuring separately from the earlier indexing change.\n\nWhat does this reveal about what counts as a valid \"change\" within the tuning loop?",
        "A tuning iteration isn't limited to schema changes like adding indexes; changing the query itself, such as adding a LIMIT that reflects the true business need, is just as legitimate a deliberate change, and its effect should be measured on its own, separately from other changes, to keep each iteration's contribution clearly attributable.",
        "medium", "analyze", "iterative-performance-tuning",
        "A valid tuning iteration isn't limited to schema changes; changing the query itself (like adding a LIMIT reflecting real business need) is equally legitimate, and should be measured separately to keep its effect attributable",
        ["Only changes to the schema, like adding an index, count as valid iterations within the tuning loop", "Adding a LIMIT clause is discouraged by the lesson as an invalid form of tuning", "LIMIT only affects how results are displayed and has no measurable effect worth re-measuring"],
    ),
    (
        "The lesson warns that \"a tuning session that skips measurement and jumps straight to 'add indexes everywhere' risks the over-indexing cost covered earlier in this unit.\"\n\nHow does this warning connect the iterative-tuning discipline back to the earlier when-not-to-index lesson?",
        "Skipping the measure-first discipline and adding indexes reflexively risks paying ongoing write-side overhead for indexes that never actually get used by the query they were meant to help, exactly the overindexing cost the earlier lesson described, so the iterative loop's discipline of measuring before and after each change is what prevents that specific waste.",
        "medium", "analyze", "iterative-performance-tuning",
        "Adding indexes without measuring risks paying ongoing write-side overhead for indexes that never actually help the query, the exact overindexing cost the earlier lesson warned about; measuring first prevents that waste",
        ["The warning is unrelated to overindexing and instead refers to a risk of running out of disk space", "The warning means indexes should never be added during a tuning session, under any circumstances", "The warning only applies to composite indexes, not to single-column indexes added during tuning"],
    ),
]

SYNTHESIS = [
    (
        "The optimizer lesson explains that plans are chosen based on estimated cost from statistics. The join algorithms lesson shows the optimizer choosing among nested loop, hash join, and merge join based on that same kind of cost estimate.\n\nHow does the optimizer's general cost-based decision-making, described in the first lesson, directly explain the specific join-algorithm choice described later?",
        "The same underlying mechanism, estimating cost from statistics and picking the cheapest option, applies uniformly whether the optimizer is choosing between a sequential scan and an index scan, or choosing among nested loop, hash, and merge join; the join algorithm choice is simply one particular application of the general cost-based decision process the first lesson introduces.",
        "medium", "analyze", "join-algorithms",
        "The same cost-based mechanism (estimate cost from statistics, pick the cheapest) applies uniformly to both scan-type decisions and join-algorithm decisions; join selection is one specific application of that general process",
        ["Join algorithm selection is actually unrelated to cost estimation and instead follows a fixed, hardcoded priority order", "The optimizer only uses cost-based reasoning for single-table queries, never for queries involving joins", "Join algorithms are chosen randomly at runtime, unlike scan type decisions which use cost estimates"],
    ),
    (
        "The reading-EXPLAIN lesson shows plain EXPLAIN gives only estimated cost and rows. The reading-EXPLAIN-ANALYZE lesson shows actual time and actual rows from real execution. The common-bottlenecks lesson describes a large estimated-vs-actual mismatch as a warning sign.\n\nHow do these three lessons connect to explain why comparing estimated and actual values is a diagnostic technique, not just two separate numbers?",
        "Plain EXPLAIN's estimates come from the optimizer's assumptions, while EXPLAIN ANALYZE's actual values come from truly running the query; when these disagree significantly, it reveals that the assumptions behind the chosen plan were wrong, directly pointing toward stale statistics or another bottleneck as the underlying cause, rather than being two disconnected pieces of information.",
        "hard", "analyze", "reading-explain-analyze",
        "Estimated values reflect the optimizer's assumptions while actual values reflect real execution; a significant gap between them reveals those assumptions were wrong, pointing toward the underlying cause like stale statistics",
        ["Estimated and actual values are always expected to match exactly, so any gap indicates a software bug", "The two numbers are unrelated and comparing them provides no diagnostic value", "Actual values are simply a more precisely rounded version of the same estimated numbers"],
    ),
    (
        "The common-bottlenecks lesson shows a CAST() in a WHERE clause defeating an otherwise-present index, forcing a sequential scan. The indexes chapter's expression-index lesson shows building an index on LOWER(customer_name) to match a similar pattern.\n\nHow does the expression-index technique directly solve the kind of bottleneck the common-bottlenecks lesson describes?",
        "Both scenarios share the same root cause, a transformation applied to a column in the WHERE clause not matching what a plain index stores, and an expression index solves it by storing the already-transformed value directly, restoring the alignment between what's searchable and what the query filters on, turning a forced sequential scan back into a usable index scan.",
        "hard", "analyze", "common-bottlenecks",
        "Both share the same root cause (a WHERE-clause transformation not matching what a plain index stores); an expression index solves it by storing the transformed value directly, restoring the index's usability",
        ["Expression indexes and the CAST() bottleneck are unrelated topics from entirely different chapters", "Expression indexes solve this by removing the need for a WHERE clause entirely", "The CAST() bottleneck can only be fixed by rewriting the query, and indexes can never help with it"],
    ),
    (
        "The iterative-tuning lesson insists on measuring with EXPLAIN ANALYZE before and after each change. The join-algorithms and common-bottlenecks lessons each describe specific, concrete changes a tuner might make (adding an index, fixing an N+1 pattern, expecting a different join algorithm to be chosen).\n\nHow does the iterative-tuning discipline change how a tuner should treat a fix from either of those other lessons?",
        "Even a fix that matches a well-understood, documented pattern (like adding an index for a missing-index bottleneck) should still be measured before and after applying it, rather than assumed to work just because it matches a known pattern from the lesson, since the specific table's real statistics and data could make its actual effect different from the general case described.",
        "medium", "apply", "iterative-performance-tuning",
        "Even a fix matching a well-documented pattern should still be measured before and after, rather than assumed to work, since the specific table's real data could make its actual effect differ from the general case",
        ["Fixes that match a known pattern from the lesson never need to be measured, since the pattern guarantees the outcome", "The iterative-tuning discipline only applies to index changes, not to fixing N+1 query patterns", "Measuring before and after is only necessary the very first time a tuner ever makes any change"],
    ),
]

SET1_SOURCES = [
    (INSIDE_THE_OPTIMIZER, 0),
    (READING_EXPLAIN, 0),
    (READING_EXPLAIN_ANALYZE, 0),
    (JOIN_ALGORITHMS, 0),
    (COMMON_BOTTLENECKS, 0),
    (ITERATIVE_TUNING, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS[:4])

SET2 = (
    INSIDE_THE_OPTIMIZER[1:]
    + READING_EXPLAIN[1:]
    + READING_EXPLAIN_ANALYZE[1:]
    + JOIN_ALGORITHMS[1:]
    + COMMON_BOTTLENECKS[1:]
    + ITERATIVE_TUNING[1:]
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
            "topics": "performance",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 7.3.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 7.3.2")
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
ws.title = "DBMS - MCQ - Unit 7.3"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 7 - Performance/7.3 - Query Optimization - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
