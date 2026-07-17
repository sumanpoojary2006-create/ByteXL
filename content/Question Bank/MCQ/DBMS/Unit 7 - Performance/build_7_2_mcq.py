import random
import openpyxl

random.seed(131)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

WHAT_IS_AN_INDEX = [
    (
        "Finding \"Rathi, Sanjay\" in a phone book doesn't mean reading every entry from the first page onward, since the book is alphabetically sorted.\n\nHow does the lesson use this analogy to describe what a database index does?",
        "A database index does exactly this for a table: a separate structure, built on one or more columns, that lets the database jump directly to matching rows instead of checking every one, the same way alphabetical sorting lets a reader jump straight to the right section.",
        "easy", "understand", "what-is-an-index",
        "An index lets the database jump directly to matching rows, the same way a phone book's alphabetical sorting lets a reader jump to the right section",
        ["An index rewrites the entire table in alphabetical order permanently", "An index is just a shorter copy of the table with fewer columns", "An index only works if the table has fewer than 100 rows"],
    ),
    (
        "Without any structure supporting a search on customer_name, EXPLAIN reports a sequential scan checking all 10000 rows to find one match.\n\nAfter `CREATE INDEX idx_orders_customer_name ON orders (customer_name);`, what does the plan change to, and why?",
        "The plan changes to an Index Scan, using idx_orders_customer_name to jump almost directly to the matching row, since the index itself is sorted by customer_name, letting the database narrow down to matching entries the same way a phone book reader flips to the right section.",
        "easy", "apply", "what-is-an-index",
        "An Index Scan, since the new index is sorted by customer_name and lets the database jump almost directly to the match",
        ["A Bitmap Heap Scan, since indexes always produce that specific plan type", "No change; CREATE INDEX has no effect until the table is manually reorganized", "A Hash Join, since creating an index automatically converts the query into a join"],
    ),
    (
        "An index is described as \"not a copy of the table.\"\n\nWhat is it instead, structurally?",
        "A separate, smaller structure holding just the indexed column's values, sorted, paired with a pointer (the ctid) back to where the full row actually lives on disk — looking up a value in the index gives the database the exact physical location to fetch, instead of checking every row's actual data.",
        "medium", "understand", "what-is-an-index",
        "A separate, smaller sorted structure holding the indexed column's values, each paired with a pointer (ctid) back to the full row's actual location",
        ["A full duplicate of every column in the table, just stored in a different file", "A cached, temporary copy of query results that expires after each session", "A compressed version of the entire table stored in memory only"],
    ),
    (
        "The index takes up its own disk space, separate from the table, confirmed by comparing pg_relation_size for the table versus the index.\n\nWhat trade-off does this represent, according to the lesson?",
        "Extra storage and extra maintenance work, in exchange for dramatically faster lookups on the indexed column — this is the fundamental trade-off every index represents.",
        "medium", "understand", "what-is-an-index",
        "Extra storage and maintenance work, traded for dramatically faster lookups on the indexed column",
        ["No trade-off at all; indexes are purely beneficial with zero cost", "The table shrinks in size once an index is created, with no other cost", "The index replaces the need for the table's own storage entirely"],
    ),
    (
        "After inserting 10000 new rows, `idx_orders_customer_name`'s size visibly grows.\n\nWhat does this growth prove about what happens on every INSERT that touches an indexed column?",
        "Every insert does double work: it adds the new row to the table's heap, and it adds a corresponding entry to the index, keeping the two in sync — the index must stay in sync with the table for every INSERT, UPDATE, or DELETE that touches the indexed column.",
        "medium", "apply", "what-is-an-index",
        "Every insert does double work: adding the row to the table's heap, and adding a matching entry to the index to keep the two in sync",
        ["The index only grows once per day during a scheduled maintenance window", "New rows are added to the table but never reflected in the index until manually rebuilt", "The index shrinks when new rows are added, since it compresses existing entries"],
    ),
    (
        "According to the \"Indexes at a glance\" table, what happens to search cost with an index, compared to without one?",
        "Without an index, every search is a sequential scan with cost growing with table size; with an index, a matching search becomes an index scan with cost growing much more slowly, closer to the size of the result rather than the size of the whole table.",
        "medium", "remember", "what-is-an-index",
        "Cost grows with table size without an index; with an index, cost grows much more slowly, closer to the size of the actual result",
        ["Cost is identical with or without an index; only storage space differs", "Without an index, cost grows with the result size; with an index, cost grows with table size, the reverse of the actual behavior", "Indexes only affect INSERT cost, never SELECT cost"],
    ),
    (
        "Creating an index on the amount column and then running EXPLAIN on `amount = 5000.00` shows the plan switching to an index scan.\n\nWhat specifically enables this switch, compared to before the index existed?",
        "The database can now look up matching rows through the sorted index instead of checking all 10000 rows directly — the new index gives the planner a structure it didn't have before, changing which plan is the cheapest available option.",
        "medium", "apply", "what-is-an-index",
        "The new sorted index gives the database a structure to look up matching rows through, instead of having to check every row directly",
        ["The table itself gets physically reordered by CREATE INDEX, which is what enables the new plan", "EXPLAIN itself changes behavior once any index exists in the database", "The switch only happens because the amount column's data type changed"],
    ),
]

BTREE_INDEXES = [
    (
        "Every index created without specifying a type, like `CREATE INDEX ... ON orders (amount)`, is automatically a B-tree.\n\nWhat does querying pg_indexes confirm about this default?",
        "pg_indexes shows the actual definition of every index, confirming idx_orders_amount uses the btree access method even though CREATE INDEX never mentioned the word \"btree\" explicitly — it's simply assumed unless a different type is requested.",
        "easy", "understand", "btree-indexes",
        "It confirms the index uses the btree access method by default, even though \"btree\" was never explicitly mentioned in the CREATE INDEX statement",
        ["It confirms the index uses a hash access method by default in PostgreSQL", "It confirms no access method is assigned until ANALYZE is run", "It confirms the index type must always be specified explicitly, or CREATE INDEX fails"],
    ),
    (
        "A B-tree is described as \"balanced,\" meaning every leaf sits at the same depth from the root.\n\nWhat does searching a B-tree involve, given this balanced structure?",
        "Starting at the root, comparing the target value, and following exactly one branch downward at each level, narrowing the search space enormously with each step, until reaching the leaf that holds the answer — no particular search path is ever dramatically longer than another.",
        "medium", "understand", "btree-indexes",
        "Starting at the root and following one branch downward at each level, narrowing the search space at each step until reaching the leaf with the answer",
        ["Scanning every leaf node from left to right until a match is found", "Randomly sampling nodes at different depths until a match happens to appear", "Starting at a leaf node and working backward up toward the root"],
    ),
    (
        "Doubling the number of rows in a table typically adds at most one extra level to its B-tree, not double the search steps.\n\nWhy is this the \"core reason B-trees are the default choice\"?",
        "Because each level can branch into many children at once rather than just two, a B-tree's depth (and thus its search cost) grows extremely slowly as the number of entries grows, staying fast even as a table grows from thousands to millions of rows, in a way a sequential scan fundamentally cannot.",
        "medium", "analyze", "btree-indexes",
        "Because each level branches into many children at once, a B-tree's depth grows extremely slowly as entries grow, staying fast at massive scale unlike a sequential scan",
        ["Because B-trees always have exactly the same number of levels regardless of row count", "Because doubling row count always halves the B-tree's total depth", "Because B-trees only work correctly on tables with fewer than a million rows"],
    ),
    (
        "Growing a table tenfold still shows an index scan being used, with the practical number of steps needed growing only marginally, nowhere near proportionally to the tenfold row increase.\n\nWhat does this demonstrate about a B-tree's search cost relative to table size?",
        "A B-tree's search cost grows extremely slowly (roughly logarithmically) relative to the size of the table, a dramatically different relationship than a sequential scan's cost, which grows directly and linearly with table size.",
        "medium", "apply", "btree-indexes",
        "A B-tree's search cost grows very slowly relative to table size, unlike a sequential scan's cost, which grows linearly and directly with table size",
        ["A B-tree's search cost grows at exactly the same rate as a sequential scan's cost", "A B-tree's search cost actually decreases as the table grows larger", "A B-tree's search cost is completely unrelated to how the table is organized"],
    ),
    (
        "Because a B-tree keeps its entries in sorted order at the leaf level, it supports far more than exact-match lookups.\n\nWhat specific query shapes benefit from this sorted structure, according to the lesson?",
        "Range conditions, sorting, and finding the minimum or maximum value can all use the same structure directly — a range query can walk to the start of the range and read forward, and a MAX query can jump straight to the far end of the sorted leaf level.",
        "medium", "understand", "btree-indexes",
        "Range conditions, sorting, and MIN/MAX lookups, since the leaf-level sorted order lets the database walk to a starting point and read forward without a separate sort step",
        ["Only exact-match equality lookups; B-trees provide no benefit for anything else", "Only text-based searches; numeric range queries get no benefit from a B-tree", "Only queries with no WHERE clause at all"],
    ),
    (
        "`EXPLAIN SELECT MAX(amount) FROM orders;` shows the planner using idx_orders_amount, reported as a backward scan of the index.\n\nWhy can a B-tree answer a MAX query without scanning and comparing every row?",
        "Since the B-tree's leaf values are already sorted, the maximum value sits at one end of that sorted order, so the database can jump straight to the far end of the sorted leaf level instead of comparing every row's value to find the largest one.",
        "hard", "analyze", "btree-indexes",
        "The sorted leaf level means the maximum value sits at one end, so the database can jump directly there instead of comparing every row",
        ["MAX queries never actually use an index, and this plan choice is unusual", "The B-tree recalculates MAX every time ANALYZE runs and caches the result", "The database scans every row anyway, but the index just makes each comparison faster"],
    ),
    (
        "According to the \"B-tree indexes at a glance\" table, what is a B-tree \"good for\"?",
        "Equality, ranges (<, >, BETWEEN), sorting, and MIN/MAX — the full range of query shapes that benefit from a sorted, balanced tree structure at the leaf level.",
        "medium", "remember", "btree-indexes",
        "Equality, ranges, sorting, and MIN/MAX queries",
        ["Only equality lookups, with no support for ranges or sorting", "Only range queries, with no support for exact-match equality", "Only queries involving JOIN, not standalone WHERE filters"],
    ),
]

HASH_COMPOSITE_PARTIAL_EXPRESSION = [
    (
        "A hash index built with `CREATE INDEX ... USING hash (customer_name)` supports `WHERE customer_name = 'Customer 7500'` but provides no help for `WHERE customer_name > 'Customer 7500'` or `ORDER BY customer_name`.\n\nWhy is a hash index useless for these range and sorting operations?",
        "A hash index stores entries by their computed hash value rather than in sorted order, and hashing intentionally destroys any sense of order between values — it carries no ordering information whatsoever, making range or sort operations impossible on it.",
        "easy", "understand", "hash-composite-partial-and-expression-indexes",
        "Hashing destroys ordering entirely, so a hash index carries no information about which values come before or after another",
        ["Hash indexes only work on numeric columns, not text columns like customer_name", "Hash indexes are limited to tables with fewer than 10000 rows", "Range and sort operations require a separate ANALYZE to be run first"],
    ),
    (
        "In practice, \"a B-tree index handles equality just as well as a hash index while also supporting ranges,\" which is why hash indexes \"see limited use.\"\n\nWhat's the main lesson the chapter draws from this comparison?",
        "\"Sorted\" and \"searchable by equality\" are not the same requirement — a B-tree already covers equality searches well, so a specialized hash index rarely offers enough exclusive benefit to be worth its range-query limitation in most real situations.",
        "medium", "analyze", "hash-composite-partial-and-expression-indexes",
        "Sorted structures like B-trees already handle equality well too, so hash indexes rarely offer enough unique benefit to be worth their inability to support ranges",
        ["Hash indexes are always faster than B-tree indexes for every kind of query", "B-tree indexes cannot actually perform equality lookups at all, only ranges", "Hash indexes should always be preferred over B-tree indexes for any equality-heavy workload"],
    ),
    (
        "`idx_orders_status_region` is created as `(status, region)`, sorting first by status, then by region within each status value.\n\nWhy can this same index help a query filtering on status alone, but offer little help to a query filtering on region alone?",
        "Column order in a composite index matters: status is the leading column, so a filter on status alone can still use the index's sorted-by-status structure, but the index isn't separately sorted by region on its own, so filtering only on region gets little benefit from it.",
        "medium", "understand", "hash-composite-partial-and-expression-indexes",
        "status is the leading column, so filtering on it alone still works; but the index isn't separately sorted by region, so filtering on region alone gets little help",
        ["Composite indexes only ever help queries that filter on every included column simultaneously", "region actually benefits more than status, since it was listed second in the index definition", "Composite indexes are sorted by whichever column has the most distinct values, not by declaration order"],
    ),
    (
        "`idx_orders_active_amount` is created as `(amount) WHERE status = 'active'`, containing only about 100 rows out of 10000.\n\nWhat's the benefit of this partial index over a full index on amount, and what's the cost of inserting a completed order?",
        "The partial index is a small fraction of the full index's size (roughly 100 entries instead of 10000), making it compact and cheap to maintain, and inserting a completed order never touches this index at all, since only active-status rows are included.",
        "medium", "apply", "hash-composite-partial-and-expression-indexes",
        "The partial index is much smaller and cheaper to maintain than a full index; inserting a completed order doesn't touch it at all, since only active rows are included",
        ["The partial index is exactly the same size as a full index, with no storage benefit", "Every insert, regardless of status, still updates the partial index fully", "The partial index only works for INSERT statements, not for SELECT queries"],
    ),
    (
        "A plain B-tree on customer_name doesn't help a query filtering on `LOWER(customer_name) = 'customer 7500'`.\n\nWhy not, and what does `idx_orders_lower_name` (built with `LOWER(customer_name)`) do differently?",
        "A plain index on customer_name is sorted by the raw column value, not the lowercased result of a function applied to it; idx_orders_lower_name instead stores the already-lowercased value, letting the database use an Index Scan instead of falling back to computing LOWER(customer_name) fresh for every row in a sequential scan.",
        "medium", "analyze", "hash-composite-partial-and-expression-indexes",
        "A plain index is sorted by the raw value, not a computed transformation of it; the expression index stores the already-transformed value, enabling an index scan instead of a sequential scan",
        ["A plain B-tree actually does support LOWER() automatically, and this is a documentation error", "LOWER(customer_name) is computed once and cached permanently regardless of any index", "The expression index converts the entire table to lowercase permanently, not just the index"],
    ),
    (
        "According to the \"Index types at a glance\" table, what is the limitation of a composite index?",
        "Column order matters, and it's less useful for the trailing columns alone — a composite index serves queries filtering on the same multiple columns together, but a query filtering only on a non-leading column gets little benefit.",
        "medium", "remember", "hash-composite-partial-and-expression-indexes",
        "Column order matters, and the index offers little help to queries filtering only on a trailing (non-leading) column",
        ["Composite indexes can only ever include exactly two columns, never more", "Composite indexes cannot be combined with WHERE clauses at all", "Composite indexes only work on numeric columns, never text columns"],
    ),
    (
        "Why does creating an expression index require an extra ANALYZE run, according to the lesson?",
        "An expression index keeps its own statistics on the computed values, gathered the next time ANALYZE runs — since the indexed values are derived (like LOWER(customer_name)), the planner needs fresh statistics specifically about those computed values, not just the raw column.",
        "hard", "analyze", "hash-composite-partial-and-expression-indexes",
        "An expression index keeps its own statistics on the computed values, which need a fresh ANALYZE to be gathered, separate from the raw column's statistics",
        ["ANALYZE is required to physically build the expression index; without it, the index doesn't exist", "Expression indexes are rebuilt entirely every time ANALYZE runs, unlike other index types", "ANALYZE is only needed for expression indexes on text columns, not numeric ones"],
    ),
]

COVERING_INDEXES = [
    (
        "A typical index only stores the indexed column plus a pointer, not the whole row. After finding a matching entry, the database still has to jump over to the actual table to fetch the rest of that row's columns.\n\nWhat is this extra jump called?",
        "A heap fetch — the extra step of visiting the table's heap after finding a match in the index, needed because the index itself doesn't store every column the query might need.",
        "easy", "remember", "covering-indexes-and-index-only-scans",
        "A heap fetch",
        ["A sequential scan", "A merge join", "A checkpoint"],
    ),
    (
        "`idx_orders_status` finds the 20 matching active rows, but the database still has to fetch each row from the table's heap to retrieve order_id and amount.\n\nWhy is this heap fetch necessary here specifically?",
        "idx_orders_status only stores status values and pointers back to matching rows; order_id and amount are columns the index itself does not contain, so the database must visit the actual table to retrieve them for every match.",
        "medium", "understand", "covering-indexes-and-index-only-scans",
        "The index only stores the status value and a pointer; order_id and amount aren't in the index, so the table must be visited to retrieve them",
        ["The heap fetch happens because the query used SELECT * instead of naming specific columns", "The heap fetch is required because status has too many distinct values for an index to handle", "The heap fetch only happens when there are more than 1000 matching rows"],
    ),
    (
        "`CREATE INDEX idx_orders_status_covering ON orders (status) INCLUDE (order_id, amount);` changes the plan from a regular index scan to an \"Index Only Scan.\"\n\nWhat does INCLUDE actually do, and why does it eliminate the heap fetch?",
        "INCLUDE adds extra columns to an index purely for storage alongside the indexed column, without making them part of the searchable, sorted key itself; since order_id and amount are now stored directly in the index, the database can answer the query entirely from the index, with no need to visit the table's heap.",
        "medium", "apply", "covering-indexes-and-index-only-scans",
        "INCLUDE stores extra columns in the index purely for retrieval, so the query can be answered entirely from the index without visiting the table's heap",
        ["INCLUDE physically merges the index and the table into a single combined structure", "INCLUDE makes order_id and amount part of the sorted search key, alongside status", "INCLUDE only works when the included columns are also part of a WHERE clause"],
    ),
    (
        "Adding customer_name to the SELECT list, a column not included in idx_orders_status_covering, makes the plan no longer an Index Only Scan.\n\nWhy does asking for just one uncovered column break the covering index's benefit entirely?",
        "The moment a query asks for even one column the index doesn't store, the database has no choice but to fall back to a regular index scan with a heap fetch for every matching row — a covering index has to be designed around the specific columns a specific query actually needs, and any gap forces the fallback.",
        "medium", "analyze", "covering-indexes-and-index-only-scans",
        "Asking for even one column the index doesn't store forces a fallback to a regular index scan with heap fetches, since the covering index must be designed around exactly what a query needs",
        ["Nothing changes; the plan stays an Index Only Scan regardless of which columns are selected", "The query fails with an error, since covering indexes can't be combined with additional columns", "customer_name is automatically added to the index on the fly to keep the Index Only Scan"],
    ),
    (
        "INCLUDE columns come with two costs: the index grows larger, and every write to those included columns also has to update the index.\n\nWhen does the lesson say covering indexes are actually worth building, given these costs?",
        "For genuinely hot, frequently run queries where the read-speed benefit clearly outweighs the extra storage and write cost, not applied indiscriminately to every index in a schema — a deliberate, measured decision rather than a default habit.",
        "medium", "understand", "covering-indexes-and-index-only-scans",
        "For genuinely hot, frequently run queries where the read benefit clearly outweighs the extra storage and write cost, not as a default applied to every index",
        ["Covering indexes should always be built for every index, regardless of query frequency", "Covering indexes are only worth it on tables with fewer than 100 rows", "Covering indexes should never be built, since the costs always outweigh the benefits"],
    ),
    (
        "According to the \"Covering indexes at a glance\" table, what is an Index Only Scan specifically?",
        "The plan shown when every needed column is available directly from the index — no heap fetch required, since the index alone contains everything the query asks for, both in WHERE and in SELECT.",
        "medium", "remember", "covering-indexes-and-index-only-scans",
        "The plan shown when every column the query needs is available directly from the index, with no heap fetch required",
        ["A plan type that only occurs when a query has no WHERE clause at all", "A plan type used exclusively for INSERT and UPDATE statements, never SELECT", "A plan type that scans the index twice for extra accuracy"],
    ),
    (
        "Building idx_orders_status_covering with INCLUDE (order_id, amount) means those two columns are stored in the index but not part of its sorted search key.\n\nWhat does this imply about using order_id or amount in a WHERE clause against this index?",
        "INCLUDE columns are carried along purely as extra payload for retrieval; they are not part of the sorted key the index searches on, so filtering by order_id or amount doesn't get the same efficient lookup that filtering by status (the actual key column) does.",
        "hard", "analyze", "covering-indexes-and-index-only-scans",
        "INCLUDE columns are only stored for retrieval, not part of the sorted search key, so filtering on them doesn't get the efficient lookup that filtering on the actual key column (status) does",
        ["INCLUDE columns become fully searchable key columns, identical in behavior to status", "Filtering by an INCLUDE column is always faster than filtering by the actual key column", "INCLUDE columns cannot be referenced in a WHERE clause at all, or the query fails"],
    ),
]

WHEN_NOT_TO_INDEX = [
    (
        "Priya's team wants to add an index to every column of the orders table \"just in case,\" after seeing indexes fix several slow reports.\n\nWhy does the lesson say this instinct, taken too far, makes the system slower overall?",
        "Every index adds real, ongoing cost, extra storage and extra work on every write that touches an indexed column, and that cost is paid whether or not the index actually gets used often enough to be worth it — indexing everything means paying that cost repeatedly for little or no read benefit.",
        "easy", "understand", "when-not-to-index-the-cost-of-overindexing",
        "Every index adds ongoing storage and write cost, paid regardless of whether it's actually used often enough to justify that cost",
        ["Adding more indexes has no real downside; the lesson's concern is purely theoretical", "Indexes only cost money to create, with no cost after that point", "Too many indexes only slow down SELECT queries, never INSERT or UPDATE"],
    ),
    (
        "Inserting the same 5000 rows into orders_many_indexes (three extra indexes) takes measurably longer than into orders_few_indexes (only the primary key's automatic index), confirmed with EXPLAIN ANALYZE's Execution Time.\n\nWhy does more indexes on a table directly slow down inserts?",
        "Each insert has to update every index on the table, not just write the row itself, so a table with three extra indexes must additionally update three separate index structures for every single row, on top of writing the row.",
        "medium", "apply", "when-not-to-index-the-cost-of-overindexing",
        "Each insert must update every index on the table in addition to writing the row itself, so more indexes mean more work per insert",
        ["More indexes actually speed up inserts by helping the database find free space faster", "The slowdown only happens the first time a table is created, not on subsequent inserts", "EXPLAIN ANALYZE artificially slows down inserts regardless of how many indexes exist"],
    ),
    (
        "idx_many_name_amount already sorts by customer_name first, meaning it can serve most of what idx_many_name alone would serve.\n\nWhy does keeping both indexes mean \"paying the storage and write cost of two overlapping structures for a benefit neither one provides over the other\"?",
        "The query planner is free to choose either index to satisfy a customer_name filter, since both can serve it, but only one gets used per query — the other overlapping structure contributes nothing to that query while still being paid for on every write, making it redundant cost without redundant benefit.",
        "medium", "analyze", "when-not-to-index-the-cost-of-overindexing",
        "Only one of the two overlapping indexes actually gets used per query, so the unused one is pure write-cost overhead with no corresponding read benefit for that query",
        ["Both indexes are always used together for every query, doubling the read benefit", "Redundant indexes actually have no write cost at all, only storage cost", "The composite index idx_many_name_amount is always slower than the plain idx_many_name"],
    ),
    (
        "An index only pays for itself if queries actually use it often enough, through WHERE, JOIN conditions, or ORDER BY, to outweigh its ongoing write cost.\n\nWhat happens to a column that's essentially never filtered or sorted on, if it's indexed anyway?",
        "It gains nothing from being indexed, since no query ever uses that index to speed up a read, yet it still pays the full write-side cost on every insert or update, regardless — pure overhead with no corresponding benefit.",
        "medium", "understand", "when-not-to-index-the-cost-of-overindexing",
        "It gains no read benefit, since nothing ever queries it, but still pays the full write-side maintenance cost on every insert or update",
        ["It automatically gets dropped by PostgreSQL after a period of disuse", "It provides no cost at all, since unused indexes are free to maintain", "It actually speeds up writes, since the database can skip checking that column"],
    ),
    (
        "A column with very few distinct values, like a boolean flag or a status with only two or three values spread evenly across a huge table, \"often does not benefit much from a plain index.\"\n\nWhy does a low-cardinality column undermine an index's usual advantage?",
        "A lookup for one value would still match a large fraction of the table's rows, closer in cost to a sequential scan than to a precise, narrow index lookup — the whole benefit of an index comes from narrowing down to a small subset, which a low-cardinality column can't provide.",
        "medium", "analyze", "when-not-to-index-the-cost-of-overindexing",
        "A lookup on a low-cardinality column still matches a large fraction of the table, closer in cost to a sequential scan than a precise, narrow index lookup",
        ["Low-cardinality columns cannot technically have an index built on them at all", "Low-cardinality columns always benefit more from an index than high-cardinality ones", "This only matters for text columns, never for boolean or numeric flags"],
    ),
    (
        "The lesson suggests a partial index is often a better fit than a plain index for a low-cardinality column.\n\nWhy would a partial index solve the problem a plain index on the whole low-cardinality column has?",
        "A partial index can target just the specific, smaller subset of values a query actually cares about (like only \"active\" rows out of many statuses), rather than indexing the entire column including the common values that would still match a large fraction of the table.",
        "hard", "apply", "when-not-to-index-the-cost-of-overindexing",
        "A partial index can target just the specific, smaller subset of values actually queried, avoiding the problem of indexing common values that still match a large fraction of the table",
        ["A partial index removes the need for cardinality entirely, working equally well on any column", "A partial index only works on high-cardinality columns, not low-cardinality ones", "A partial index and a plain index perform identically on low-cardinality columns"],
    ),
    (
        "orders_many_indexes carries three extra indexes beyond the primary key, while orders_few_indexes carries only the primary key's automatic index.\n\nIf a report only ever queries orders_few_indexes-style tables by primary key, what does the lesson suggest about adding those same three extra indexes to it anyway?",
        "It would add write-side cost to every insert without any corresponding read benefit, since none of those extra indexes would ever actually be used by primary-key-only queries — exactly the overindexing pattern the lesson warns against, cost without benefit.",
        "medium", "apply", "when-not-to-index-the-cost-of-overindexing",
        "It would add write-side cost to every insert with no corresponding read benefit, since none of the extra indexes would ever be used by primary-key-only queries",
        ["It would make primary-key lookups faster, since more indexes always improve every kind of query", "It would have zero effect either way, since unused indexes carry no cost", "It would automatically get removed by the database once it detects the indexes are unused"],
    ),
]

SYNTHESIS = [
    (
        "The what-is-an-index lesson introduces the general trade-off (extra storage/write cost for faster reads). The B-tree lesson shows why B-trees stay fast at scale. The when-not-to-index lesson shows that trade-off can tip the wrong way.\n\nHow do these three lessons together explain why \"an index is always good\" is an oversimplification?",
        "An index's benefit (fast reads via a B-tree's efficient search) is real, but it's not free (storage and write cost from the first lesson), and that cost is paid regardless of whether the index is actually used enough to justify it (the overindexing lesson) — the B-tree's efficiency explains why indexes are usually worth it, but doesn't erase the underlying cost that makes an unused or redundant index a net loss.",
        "medium", "analyze", "when-not-to-index-the-cost-of-overindexing",
        "An index's read benefit is real and made efficient by the B-tree structure, but its storage/write cost is paid regardless of use, so an index that's rarely used or redundant becomes a net loss despite B-trees being efficient",
        ["B-trees eliminate all costs associated with indexing, making the trade-off from the first lesson obsolete", "The three lessons actually contradict each other, and only one can be correct", "Write cost only applies to hash indexes, not B-tree indexes, so this trade-off doesn't apply to the default index type"],
    ),
    (
        "The composite index lesson shows column order mattering (status, region) vs. (region, status) serve different queries differently. The overindexing lesson shows idx_many_name_amount making idx_many_name partially redundant.\n\nHow does understanding composite index column order help identify which indexes are truly redundant, versus which merely look similar?",
        "A composite index like (customer_name, amount) already serves as an effective index on customer_name alone (since it's the leading column), so a separate single-column index on customer_name is redundant; but it does NOT serve as an effective index on amount alone, so a separate index on amount would not be redundant with it, despite both indexes technically \"involving\" amount.",
        "hard", "analyze", "hash-composite-partial-and-expression-indexes",
        "A composite index effectively covers its leading column alone, making a separate index on just that leading column redundant, but it doesn't effectively cover trailing columns alone, so a separate index on a trailing column is not redundant",
        ["Any composite index makes every single-column index on its constituent columns fully redundant", "Composite indexes never create redundancy with single-column indexes, regardless of column order", "Redundancy only depends on how many total indexes exist, not on which columns they cover or in what order"],
    ),
    (
        "The covering index lesson shows INCLUDE eliminating a heap fetch by storing extra columns. The partial index lesson (from hash/composite/partial/expression) shows storing only a subset of rows to save space. Both add something to a plain B-tree index.\n\nWhat's the key difference between what a covering index (INCLUDE) adds versus what a partial index (WHERE) adds to a base index?",
        "A covering index adds more columns to every entry (making each entry wider, to eliminate heap fetches), while a partial index adds a row-filtering condition (making the index shorter, containing fewer entries) — one grows the index's width for read completeness, the other shrinks the index's length for storage efficiency, and the two techniques can even be combined.",
        "hard", "analyze", "covering-indexes-and-index-only-scans",
        "A covering index widens each entry (more columns per entry, eliminating heap fetches); a partial index shortens the index (fewer rows included, for storage efficiency) — they address different dimensions and can be combined",
        ["Covering indexes and partial indexes both do exactly the same thing: reduce the total index size", "A covering index removes rows from the index, while a partial index adds columns, the reverse of their actual effects", "The two techniques are mutually exclusive and can never be used together on the same index"],
    ),
    (
        "Across this chapter: a plain index helps equality lookups (lesson 1), a B-tree extends that to ranges and sorting (lesson 2), specialized variants target specific patterns like composite filters or computed values (lesson 3), a covering index eliminates the remaining heap-fetch cost (lesson 4), and the final lesson warns against applying all of this indiscriminately (lesson 5).\n\nWhat single discipline does this progression, taken as a whole, teach about how indexing should actually be approached in a real system?",
        "Indexing should be a deliberate decision matched to actual, observed query patterns, choosing the specific index shape (plain, composite, partial, expression, covering) that fits a real, frequently run query's real filtering and selection needs, rather than either avoiding indexes out of fear of the write cost or adding them reflexively to every column just because more capability sounds better.",
        "medium", "understand", "when-not-to-index-the-cost-of-overindexing",
        "Indexing should be a deliberate decision matched to actual query patterns, choosing the specific index shape that fits a real, frequently run query's needs, rather than either avoiding indexes entirely or adding them reflexively everywhere",
        ["The chapter's overall lesson is that every column should always be indexed with every available index type", "The chapter's overall lesson is that indexes should be avoided entirely in favor of always using sequential scans", "The chapter's overall lesson is that only B-tree indexes are ever worth using, and all specialized variants are unnecessary"],
    ),
    (
        "The what-is-an-index lesson shows ctid (from the storage chapter) being the pointer an index uses to reach back to the full row. The covering-index lesson shows INCLUDE storing extra columns to avoid needing that pointer's target at all.\n\nHow does this connect the storage chapter's physical addressing (ctid) to the indexing chapter's performance techniques?",
        "An ordinary index's core mechanism, a sorted key plus a ctid pointer, directly relies on the physical addressing scheme established in the storage chapter; a covering index is essentially a technique for making that ctid-based heap fetch unnecessary for a specific query, by carrying the answer to that jump directly inside the index itself instead of requiring the jump.",
        "hard", "analyze", "what-is-an-index",
        "An index's core mechanism (sorted key plus ctid pointer) relies directly on the storage chapter's physical addressing; a covering index makes that ctid-based heap fetch unnecessary by carrying the answer inside the index itself",
        ["ctid and covering indexes are entirely unrelated concepts that happen to appear in adjacent chapters", "A covering index actually replaces ctid with a completely different addressing mechanism", "ctid is only relevant to heap-organized tables, and indexes don't use ctid at all"],
    ),
]

SET1_SOURCES = [
    (WHAT_IS_AN_INDEX, 0),
    (BTREE_INDEXES, 0),
    (HASH_COMPOSITE_PARTIAL_EXPRESSION, 0),
    (COVERING_INDEXES, 0),
    (WHEN_NOT_TO_INDEX, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    WHAT_IS_AN_INDEX[1:]
    + BTREE_INDEXES[1:]
    + HASH_COMPOSITE_PARTIAL_EXPRESSION[1:]
    + COVERING_INDEXES[1:]
    + WHEN_NOT_TO_INDEX[1:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 7.2.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 7.2.2")
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
ws.title = "DBMS - MCQ - Unit 7.2"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 7 - Performance/7.2 - Indexes - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
