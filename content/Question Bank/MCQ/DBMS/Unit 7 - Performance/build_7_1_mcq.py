import random
import openpyxl

random.seed(127)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

HOW_DATA_IS_STORED = [
    (
        "A database does not read or write one row at a time from disk; it reads and writes in fixed-size blocks called pages, typically 8 kilobytes each in PostgreSQL.\n\nWhat does this mean for a query that needs only one row?",
        "The database must still read the whole page that row lives on, dragging along every other row packed into that same page, because a row cannot be read in isolation from the page it lives in.",
        "easy", "understand", "how-data-is-stored",
        "It must read the entire page the row lives on, including every other row packed into that same page",
        ["It reads only the exact bytes belonging to that one row, ignoring the rest of the page", "It reads the entire table regardless of which row is needed", "It reads one row per page, since each page holds exactly one row"],
    ),
    (
        "PostgreSQL exposes a row's physical location through a hidden system column called ctid, showing values like (0,1).\n\nWhat does a ctid value actually represent?",
        "It identifies exactly which page and which position within that page a row currently occupies — (0,1) means page 0, position 1 within that page.",
        "easy", "remember", "how-data-is-stored",
        "The row's physical address: which page it's on, and its position within that page",
        ["The row's logical primary key value, duplicated for convenience", "A checksum used to verify the row hasn't been corrupted", "The timestamp when the row was originally inserted"],
    ),
    (
        "Rows with nearby order_id values, inserted around the same time, tend to land on the same or nearby pages, while a row inserted much later in the same batch sits on a later page.\n\nWhat does this reveal about what actually determines a row's ctid?",
        "A row's physical location is determined by insertion order and available space, not by its column values — order_id values don't need to be close together in value for rows to end up on nearby pages; what matters is when they were inserted.",
        "medium", "analyze", "how-data-is-stored",
        "Insertion order and available space determine physical location, not the row's own column values",
        ["The primary key value directly determines exactly which page a row is stored on", "Rows are always stored in alphabetical order by their first text column", "Physical location is randomized independently of insertion order or space"],
    ),
    (
        "Disks, even fast solid-state ones, are dramatically better at reading one large contiguous chunk than at making many small, scattered reads.\n\nHow does a database design around this hardware reality?",
        "It always reads a full page at once, even if a query only needs one row from it, exploiting the fact that reading one larger contiguous chunk is cheaper than many small scattered reads.",
        "medium", "understand", "how-data-is-stored",
        "It always reads a full page at once, taking advantage of disks being faster at large contiguous reads than many small scattered ones",
        ["It reads exactly the bytes needed for one row, since scattered reads are actually faster on modern disks", "It ignores page boundaries entirely and reads the whole table sequentially every time", "It caches every row individually in memory to avoid touching disk at all"],
    ),
    (
        "Grouping by page number using `(ctid::text::point)[0]` shows each page holding over a hundred rows.\n\nWhat does this make concrete about the cost of a lookup for a single row?",
        "A query that needs only one specific row still forces the database to read that row's entire page, dragging along every one of that row's hundred-plus neighbors, because the page is the smallest unit the disk deals in.",
        "medium", "apply", "how-data-is-stored",
        "Looking up one row still means reading its entire page, including all its neighboring rows, since the page is the smallest unit the disk operates on",
        ["It shows that each row lookup only ever touches exactly that one row's bytes", "It shows that pages shrink automatically to hold exactly one row when a query is selective", "It shows that the number of rows per page has no bearing on lookup cost"],
    ),
    (
        "According to the \"From table to disk, the full path\" summary, what is a table file, in relation to pages and rows?",
        "A table file is a sequence of pages on disk, making up the whole table — rows are the logical unit SQL operates on, pages are the fixed-size blocks holding many rows, and the table file is the full sequence of those pages.",
        "medium", "remember", "how-data-is-stored",
        "A sequence of pages on disk that together make up the whole table",
        ["A single page holding the entire table's worth of rows", "A separate index structure unrelated to how rows are stored", "A logical grouping of tables that share the same schema"],
    ),
    (
        "Checking the ctid values for order_id 100 and order_id 101, both inserted back to back in the same batch.\n\nWhat would you expect to see, and why?",
        "Both rows are very likely to show the same page number in their ctid, since they were inserted back to back in the same batch and packed onto the same page — physical proximity follows insertion order, not the order_id values themselves.",
        "medium", "apply", "how-data-is-stored",
        "Both would very likely show the same page number, since they were inserted consecutively in the same batch and packed onto the same page",
        ["They would definitely be on different pages, since consecutive order_id values are always split apart", "It's impossible to predict without running ANALYZE first", "They would show the same position within different pages, never the same page"],
    ),
    (
        "pg_relation_size reports how many bytes the orders table actually occupies on disk, and pg_size_pretty formats that into a readable size like \"48 kB.\"\n\nWhy is the table's total size described as \"not 500 individual files, one per row\"?",
        "A table is stored as a small number of 8 kilobyte pages, each holding dozens of rows packed together, rather than as separate individual files per row — the page, not the row, is the physical unit of storage on disk.",
        "medium", "understand", "how-data-is-stored",
        "Because rows are packed together into a small number of shared pages, not stored as separate individual files per row",
        ["Because PostgreSQL actually does create one file per row, but compresses them afterward", "Because the 500 rows were merged into a single row before being stored", "Because pg_relation_size only reports the size of the largest single row"],
    ),
    (
        "Why does the lesson describe understanding physical storage (pages, ctid) as what \"makes the rest of this unit, on indexes and query speed, make sense\"?",
        "Every performance concept covered later, indexes, scan costs, storage layout, all build directly on the physical fact that rows live inside pages and reading means fetching whole pages, so understanding this foundation first is what makes the later, more advanced concepts comprehensible rather than abstract rules to memorize.",
        "hard", "analyze", "how-data-is-stored",
        "Later concepts like indexes and scan costs are built directly on the physical reality of pages and row addresses, so understanding this foundation first makes those later ideas concrete rather than abstract",
        ["Physical storage details are actually unrelated to indexes and query speed, despite the lesson's claim", "Pages and ctid values are only relevant to database administrators, not to understanding query performance", "The connection is purely historical and has no bearing on how modern queries actually run"],
    ),
    (
        "SQL as a language is designed to let a person work with a table as \"an abstract grid of rows and columns,\" without ever thinking about disks or bytes.\n\nWhy does the lesson say understanding the physical layer underneath that abstraction still matters for someone writing queries?",
        "The abstraction is intentional and useful for writing correct SQL, but query speed depends directly on the physical reality beneath it (pages, row placement), so understanding that physical layer is what explains why some logically simple queries run instantly while others crawl, a gap the abstraction alone can't account for.",
        "hard", "analyze", "how-data-is-stored",
        "Query correctness only needs the logical abstraction, but query speed depends on the physical layer beneath it, which the abstraction alone can't explain",
        ["The physical layer is irrelevant once SQL's abstraction is properly understood", "SQL's abstraction actually requires understanding pages and ctid to write any correct query", "Physical storage only matters for database administrators, never for anyone writing SQL queries"],
    ),
    (
        "Priya notices some queries run instantly while others crawl, and the lesson traces this directly to how data is laid out on disk.\n\nBased on this lesson, what's the most direct physical explanation for why two logically similar queries could have very different speeds?",
        "The two queries likely differ in how many pages they force the database to read, which depends on physical row placement (page packing, insertion order) rather than on how the query is logically phrased or how many rows it conceptually asks for.",
        "medium", "apply", "how-data-is-stored",
        "The queries likely differ in how many pages they force the database to read, driven by physical row placement rather than how the query is logically written",
        ["Query speed is determined entirely by how many words appear in the SQL statement", "Two logically similar queries always run at exactly the same speed on the same table", "Query speed depends only on which columns are selected, never on which rows are filtered"],
    ),
]

FILE_ORGANIZATION = [
    (
        "Rows inserted with order_id values 5, 2, 8, then 1 still show ctid values that reflect insertion order, not sorted order_id order.\n\nWhat does this confirm about PostgreSQL's default table organization, the heap?",
        "A heap makes no attempt to keep rows physically sorted by any column at all — new rows are simply placed wherever there happens to be free space, with no guaranteed ordering.",
        "easy", "understand", "file-organization-heap-sorted-and-hashed-files",
        "A heap places new rows wherever there's free space, with no guaranteed ordering by any column",
        ["A heap always keeps rows sorted by their primary key automatically", "A heap sorts rows alphabetically by their first text column", "A heap groups rows by which page has the most free space remaining"],
    ),
    (
        "A query wanting \"every order with order_id between 1 and 4\" cannot assume those rows sit near each other on disk in a heap-organized table.\n\nWhat does finding them without help require?",
        "Checking every page, a full table scan, since a heap offers no guarantee that rows with nearby key values are physically located near each other.",
        "easy", "understand", "file-organization-heap-sorted-and-hashed-files",
        "Checking every page (a full table scan), since a heap gives no guarantee that nearby key values are physically close together",
        ["A single index lookup, since primary keys are always automatically sorted on disk", "Nothing extra; the heap already keeps this range contiguous by default", "A binary search directly on the heap's pages, without needing any structure"],
    ),
    (
        "CLUSTER physically reorders an existing table's rows to match an index's order, as a one-time operation. After running it, ctid values increase in the same order as order_id.\n\nWhy does this make a range query like \"every order between id 1 and 4\" dramatically cheaper afterward?",
        "The matching rows are now physically adjacent, reachable by reading a small, contiguous run of pages instead of scattering across the whole table — exactly the benefit sorted/clustered organization provides for range queries.",
        "medium", "analyze", "file-organization-heap-sorted-and-hashed-files",
        "The matching rows become physically adjacent after CLUSTER, so a small, contiguous run of pages can be read instead of scattering across the whole table",
        ["CLUSTER converts the table into a hash-organized structure automatically", "CLUSTER has no actual effect on physical row order, only on logical query results", "CLUSTER only helps exact-match lookups, never range queries"],
    ),
    (
        "CLUSTER is described as \"a one-time, explicit reorganization,\" after which \"new rows inserted afterward go back to landing wherever there is free space.\"\n\nWhat does this reveal about the ongoing cost of maintaining a clustered layout?",
        "The table gradually drifts back toward an unsorted heap after CLUSTER runs, since it isn't maintained automatically the way a heap's default insertion is — keeping a table clustered over time requires periodically re-running CLUSTER, an ongoing maintenance cost.",
        "medium", "apply", "file-organization-heap-sorted-and-hashed-files",
        "The table gradually drifts back toward an unsorted heap as new rows are added, requiring CLUSTER to be re-run periodically to stay sorted",
        ["CLUSTER permanently locks all future inserts into sorted position automatically", "New rows after CLUSTER are automatically inserted into their correct sorted position", "CLUSTER only needs to run once ever, with no ongoing maintenance required afterward"],
    ),
    (
        "With names listed alphabetically, `abs(hashtext(customer_name)) % 8 AS bucket` produces bucket numbers that jump around with no pattern at all, even for names that sit next to each other alphabetically.\n\nWhy is this scrambling described as \"not a flaw but the entire design\"?",
        "A hash function deliberately scatters values evenly so that no bucket gets overloaded, and the unavoidable price of that even distribution is that any notion of \"nearby\" or \"in between\" is destroyed on the way in — the scrambling is the intended trade-off, not a bug.",
        "medium", "understand", "file-organization-heap-sorted-and-hashed-files",
        "Hashing deliberately scatters values evenly to prevent overloaded buckets, and destroying any notion of \"nearby\" is the accepted trade-off for that even distribution",
        ["It's actually a bug in the hashtext function that PostgreSQL has not yet fixed", "The scrambling only happens because customer_name contains numbers mixed with letters", "Hash functions are supposed to preserve alphabetical order, and this shows a broken implementation"],
    ),
    (
        "A hash index built with `CREATE INDEX ... USING hash (customer_name)` serves an equality lookup for one specific value very well.\n\nWhat can it not help with, and why?",
        "It cannot help with \"find every customer whose name comes after Kavya alphabetically\" (a range-style query), because hashing scrambles order on purpose, destroying any notion of which values come before or after another.",
        "medium", "apply", "file-organization-heap-sorted-and-hashed-files",
        "Range-style queries like \"names after Kavya alphabetically,\" since hashing intentionally destroys ordering information",
        ["It cannot help with any query at all, including exact-match lookups", "It cannot help with queries filtering on customer_name specifically, only other columns", "It cannot help once the table grows past a few hundred rows"],
    ),
    (
        "According to the \"Choosing between the three, at a glance\" table, what is heap organization \"weak for,\" despite being the default?",
        "Any query that benefits from physical ordering — since a heap offers no guaranteed ordering at all, queries that rely on nearby values being physically close (like range scans) gain nothing from the default heap layout.",
        "medium", "remember", "file-organization-heap-sorted-and-hashed-files",
        "Any query that would benefit from physical ordering, since a heap provides no ordering guarantee at all",
        ["Fast writes, since a heap is actually the slowest organization for inserting new rows", "Exact-match lookups, since a heap cannot support equality searches at all", "Small tables, since a heap only works efficiently on very large tables"],
    ),
    (
        "New rows inserted into a table right after a CLUSTER operation are placed wherever free space is available, heap-style, not necessarily in sorted position.\n\nWhat would you expect the ctid values of those newly inserted rows to look like, relative to the already-clustered block?",
        "The new rows will likely appear after the already-clustered block rather than interleaved into perfectly sorted position, since CLUSTER only reorganizes the table at the moment it runs, and subsequent inserts revert to ordinary heap-style placement.",
        "medium", "apply", "file-organization-heap-sorted-and-hashed-files",
        "The new rows will likely land after the already-clustered block, not interleaved into sorted position, since CLUSTER doesn't run continuously",
        ["The new rows will always be inserted into their exact correct sorted position automatically", "The new rows will overwrite the existing clustered rows to maintain sort order", "The new rows will be rejected until CLUSTER is manually re-run"],
    ),
    (
        "PostgreSQL does not organize whole tables using a hashed strategy, but it does offer hash indexes that apply the same idea to speed up equality lookups specifically.\n\nWhy would applying hashing to an entire table's physical organization be a poor fit for most general-purpose querying, given what hashing does to order?",
        "Since hashing destroys any sense of order between values, organizing an entire table this way would make it impossible to efficiently answer range queries, sorting requests, or MIN/MAX lookups across the whole table, capabilities most general-purpose querying relies on at least occasionally, unlike the narrow equality-only use case a hash index targets.",
        "hard", "analyze", "file-organization-heap-sorted-and-hashed-files",
        "Hashing destroys ordering entirely, so organizing a whole table this way would sacrifice range queries, sorting, and MIN/MAX support across the board, not just for one narrow indexed column",
        ["Hashing would actually make every kind of query faster if applied to the whole table", "Hash organization is avoided only because PostgreSQL lacks the storage capacity to implement it", "Whole-table hashing would work identically to heap organization, making it redundant rather than harmful"],
    ),
    (
        "Comparing the three organizations, heap prioritizes fast writes with no reorganization overhead, sorted/clustered prioritizes range queries at the cost of ongoing maintenance, and hashed prioritizes exact-match lookups at the cost of range support entirely.\n\nWhat single principle explains why no one organization is simply \"the best\" for every table?",
        "Each organization makes a deliberate trade-off between write simplicity, maintenance cost, and which kind of read pattern it optimizes for, so the right choice depends entirely on how a specific table is actually queried, not on any organization being universally superior.",
        "hard", "understand", "file-organization-heap-sorted-and-hashed-files",
        "Each organization trades off write simplicity, maintenance cost, and a specific read pattern differently, so the right choice depends on how the table is actually queried",
        ["Heap is always the best choice, and the other two organizations exist only for legacy compatibility", "Sorted/clustered organization is strictly superior in every case, since it supports both equality and range queries", "The choice between organizations only matters for tables with fewer than 1000 rows"],
    ),
    (
        "A hash index is described as applying \"exactly this idea,\" the bucket-based hashing strategy, \"to speed up equality lookups specifically.\"\n\nWhat specific limitation does this inherit directly from how hashing scrambles alphabetical order?",
        "It cannot help with ORDER BY on the hashed column or with any range-style condition (greater than, less than, between), since the scrambling that makes equality lookups fast also destroys any notion of which values come before or after another.",
        "medium", "understand", "file-organization-heap-sorted-and-hashed-files",
        "It cannot support ORDER BY or range conditions on the hashed column, since the same scrambling that speeds up equality destroys ordering information",
        ["It cannot support equality lookups on more than one value at a time", "It cannot be created on text columns, only numeric ones", "It requires the table to be re-clustered before it can be used"],
    ),
]

WHY_STORAGE_LAYOUT_AFFECTS_SPEED = [
    (
        "`EXPLAIN SELECT * FROM orders WHERE customer_name = 'Customer 3000';` reports a \"Seq Scan.\"\n\nWhat does this mean the database intends to do, and why, given the heap organization from the previous lesson?",
        "It intends to read the table page by page, from the beginning, checking every row's customer_name against the target value until it reaches the end — the heap organization gives the database no shortcut, no way to know in advance which page holds that customer without checking.",
        "easy", "understand", "why-storage-layout-affects-query-speed",
        "It reads the table page by page from the beginning, checking every row, since the heap gives no shortcut to know which page holds the match in advance",
        ["It jumps directly to the page most likely to contain 'Customer 3000' based on alphabetical position", "It reads only the first page and assumes the match is there", "It builds a temporary sorted copy of the table before searching it"],
    ),
    (
        "Counting distinct pages with `(ctid::text::point)[0]` shows a sequential scan has to read every single page in the table, even for a single-row lookup.\n\nWhat does this confirm about how a sequential scan's cost scales?",
        "A sequential scan's cost scales with the size of the whole table, not with how many rows the query actually needs, whether that need is 1 row or 1000 — the entire table must be read regardless of how selective the query actually is.",
        "medium", "understand", "why-storage-layout-affects-query-speed",
        "Its cost scales with the total size of the table, regardless of how few or many rows the query actually needs",
        ["Its cost scales only with the number of rows the query actually returns", "Its cost is fixed and constant, regardless of table size", "Its cost scales with the number of columns selected, not the number of rows scanned"],
    ),
    (
        "Filtering on order_id (the primary key) instead of customer_name produces an \"Index Scan using orders_pkey\" instead of a sequential scan, even though the table's physical layout (the unordered heap) hasn't changed at all.\n\nWhat actually explains the different plan?",
        "PostgreSQL automatically builds a separate structure, an index, for every primary key in order to enforce uniqueness, and the planner uses that structure to jump straight to the right page — the only difference is that one column has a supporting structure and the other does not.",
        "medium", "analyze", "why-storage-layout-affects-query-speed",
        "PostgreSQL automatically builds a supporting index for the primary key to enforce uniqueness, and the planner uses it to skip most pages; customer_name has no such structure",
        ["Primary key columns are always physically sorted on disk, unlike other columns", "The table's heap layout actually changes to accommodate primary key searches specifically", "Index scans are always chosen over sequential scans, regardless of whether a supporting structure exists"],
    ),
    (
        "Doubling the row count in a heap table roughly doubles the reported table size, and a full scan against the larger table has roughly twice as many pages to check for the exact same single-row lookup.\n\nWhy does the lesson say this is precisely why \"it worked fine on my small test table\" is not evidence a query will stay fast?",
        "A full table scan's cost is a direct, predictable function of table size, so a query that felt fast on a small test table can become proportionally slower as real data volume grows, even though the logical query and the answer being searched for never changed.",
        "medium", "apply", "why-storage-layout-affects-query-speed",
        "A full scan's cost scales directly and predictably with table size, so a fast result on a small test table doesn't guarantee the same query stays fast as real data volume grows",
        ["Test tables and production tables are always structured completely differently", "Doubling the row count actually makes a full scan run faster due to caching effects", "Table size has no real effect on scan cost; only row content matters"],
    ),
    (
        "A full scan is described as \"often the most efficient plan the database could choose\" in certain situations, not always the wrong choice.\n\nWhen does the lesson say a full scan is genuinely the right call?",
        "When a query genuinely needs most or all of a table's rows, such as computing an aggregate across the entire table, reading every page is unavoidable regardless of any structure available, making a full scan often the most efficient plan.",
        "medium", "understand", "why-storage-layout-affects-query-speed",
        "When a query genuinely needs most or all of the table's rows, such as an aggregate over the whole table, where reading everything is unavoidable anyway",
        ["A full scan is never the right choice under any circumstances", "Only when the table has fewer than 100 rows total", "Only when no primary key has been defined on the table"],
    ),
    (
        "`EXPLAIN SELECT * FROM orders WHERE amount > 120000;` reports a sequential scan, even though amount tops out at 125000.00 and only a small fraction of rows would actually satisfy this condition.\n\nWhy is a sequential scan expected here, given how few rows qualify?",
        "amount has no supporting structure to help the database skip pages, meaning it must check every row's amount value against the condition regardless of how few rows actually qualify — a small result doesn't guarantee a cheap plan without a supporting index.",
        "medium", "apply", "why-storage-layout-affects-query-speed",
        "amount has no supporting index, so the database must check every row's value against the condition, regardless of how selective the result turns out to be",
        ["The condition amount > 120000 is actually not selective at all in this data", "A sequential scan is always chosen for numeric comparisons, regardless of any index", "The primary key index on order_id automatically covers filters on any other column too"],
    ),
    (
        "According to the \"Storage layout and query speed at a glance\" table, what does cost scale with when a query needs a few rows but the filtered column has no supporting structure?",
        "Table size, wastefully, since only a few rows were needed — the scan's cost is tied to how big the whole table is, not to how few rows actually matched, making it a wasteful situation precisely because the need was so narrow.",
        "medium", "remember", "why-storage-layout-affects-query-speed",
        "Table size, wastefully, since the query only needed a small number of rows but the scan cost scales with the entire table anyway",
        ["The number of rows actually returned, making it efficient regardless of table size", "The number of columns in the SELECT list, not the table's row count", "Nothing; this situation always produces a fixed, constant cost"],
    ),
    (
        "The primary key search in this lesson \"escaped this fate\" (the full table scan) specifically because PostgreSQL \"quietly built an index for it.\"\n\nWhat does the word \"quietly\" emphasize about why this escape happened?",
        "The index wasn't something the query writer explicitly created or requested for this purpose; it was an automatic side effect of declaring a PRIMARY KEY constraint, which exists to enforce uniqueness but happens to also give queries on that column a performance shortcut.",
        "hard", "analyze", "why-storage-layout-affects-query-speed",
        "The index was an automatic side effect of declaring PRIMARY KEY (for uniqueness enforcement), not something explicitly created for query speed, yet it still provided that speed benefit",
        ["\"Quietly\" means the index was created without PostgreSQL's knowledge, an unintentional bug", "\"Quietly\" means the index only partially works and sometimes fails silently", "\"Quietly\" means the index is hidden from EXPLAIN output and cannot be inspected"],
    ),
    (
        "Two physical facts from the previous lessons, data is read in whole pages, and a heap offers no guarantee about which rows land on which pages, combine directly in this lesson's explanation of a full table scan.\n\nHow do these two facts together explain why a full table scan must check every row, not just every page?",
        "Since the heap gives no guarantee about where a matching row might be, and pages must be read as whole units, the database cannot know in advance which pages to skip, so it must read every page in sequence and, once each page is loaded, check every row on it individually to find any matches.",
        "hard", "analyze", "why-storage-layout-affects-query-speed",
        "Since the heap offers no clue about which pages hold a match, every page must be read, and once loaded, every row on that page must be individually checked, combining both facts into the full-scan cost",
        ["A full table scan actually only reads pages, never checking individual rows within them", "The heap's lack of ordering only affects range queries, not the need to check every row", "Pages are read one row at a time, making the page/row distinction irrelevant to scan cost"],
    ),
    (
        "This lesson's conclusion says the primary key search \"escaped this fate only because PostgreSQL quietly built an index for it,\" setting up the next chapter's focus.\n\nWhat capability does the next chapter promise to extend, based on this lesson's closing line?",
        "The ability to get an index-based shortcut for any column a query filters on, not just the primary key — extending the same escape-from-full-scan benefit the primary key enjoyed automatically to any column a query actually needs to search efficiently.",
        "medium", "understand", "why-storage-layout-affects-query-speed",
        "The ability to build an index-based shortcut for any column a query filters on, not just the automatically-indexed primary key",
        ["The ability to eliminate full table scans entirely, for every possible query without exception", "The ability to convert every table into a hash-organized structure automatically", "The ability to avoid needing ANALYZE to keep statistics up to date"],
    ),
    (
        "The lesson states a full scan becomes a problem \"specifically when a query only needs a small fraction of a large table's rows.\"\n\nWhat's the precise reasoning behind why table size, not result size, drives the cost in this specific situation?",
        "Without a supporting structure, the database has no way to know in advance which rows or pages qualify, so it must inspect the entire table regardless of how few rows will ultimately match, making the wasted effort proportional to how much larger the table is than the actual result.",
        "hard", "analyze", "why-storage-layout-affects-query-speed",
        "Without a supporting structure, the database can't know in advance which rows qualify, so it inspects the whole table regardless of result size, making the waste proportional to the gap between table size and result size",
        ["Table size only matters when the result set is larger than the table itself", "The database always reads exactly the number of rows in the final result, regardless of table size", "This situation only occurs when the table has no primary key defined at all"],
    ),
]

SYNTHESIS = [
    (
        "The how-data-is-stored lesson establishes that reading a row means reading its whole page. The file-organization lesson shows a heap places rows with no guaranteed order. The why-storage-layout lesson shows a full table scan must check every page as a result.\n\nHow do these three facts chain together to explain why a heap-organized table with no supporting index is slow for a selective query?",
        "Because rows must be read as whole pages (fact one), and a heap gives no guarantee about which page holds a given value (fact two), the database has no way to skip any pages when searching for a specific value, forcing it to read and check every page in the table (fact three) — each fact is a necessary link in the chain that produces a full table scan's cost.",
        "medium", "analyze", "why-storage-layout-affects-query-speed",
        "Pages must be read as whole units, a heap gives no clue which page holds a match, so every page must be checked, chaining into a full table scan",
        ["The three facts are independent and don't actually combine to explain full scan cost", "Only the heap organization matters; page-based reading has no bearing on scan cost", "Full table scans occur regardless of these three facts, for unrelated reasons"],
    ),
    (
        "CLUSTER physically sorts a table to match an index's order, making range queries on the clustered column cheap. A hash index scrambles order entirely to make equality lookups cheap.\n\nWhy can't a single physical organization be simultaneously optimized for both fast range queries and fast equality lookups the way hashing achieves equality speed?",
        "Sorted/clustered organization achieves fast ranges precisely by keeping physically nearby values close together on disk, while hashing achieves fast equality precisely by deliberately scattering values evenly to avoid overloaded buckets — these two goals require opposite physical arrangements of the same data, so a single organization can't fully deliver both benefits simultaneously.",
        "hard", "analyze", "file-organization-heap-sorted-and-hashed-files",
        "Sorted organization requires keeping nearby values physically close (for ranges); hashing requires deliberately scattering values (for even equality lookups) — these are opposite physical arrangements",
        ["A single organization actually can achieve both goals equally well; the two lessons simply didn't demonstrate it", "Range queries and equality lookups are actually the same operation, so this tension doesn't really exist", "Hashing is strictly better than sorting for every kind of query, including ranges"],
    ),
    (
        "The primary key search escaped the full-scan fate because PostgreSQL automatically builds an index to enforce uniqueness. The customer_name search did not escape it, since no such automatic structure exists for that column.\n\nWhat does this contrast reveal about the relationship between a column's constraints (like PRIMARY KEY) and its query performance?",
        "A constraint's side effects (like the automatic index behind PRIMARY KEY) can incidentally provide performance benefits that have nothing to do with the constraint's actual purpose (enforcing uniqueness) — meaning query performance isn't solely a deliberate design choice, but can also be a byproduct of decisions made for entirely different reasons, like data integrity.",
        "hard", "understand", "why-storage-layout-affects-query-speed",
        "A constraint's side effects (like PRIMARY KEY's automatic index) can incidentally boost performance, showing that query speed can be a byproduct of integrity-focused decisions, not just deliberate performance tuning",
        ["Constraints and query performance are entirely unrelated, and PRIMARY KEY's speed benefit is a coincidence with no real explanation", "Every constraint automatically creates a performance-boosting index of some kind", "PRIMARY KEY only affects performance when the column is also filtered on in every query"],
    ),
    (
        "The how-data-is-stored lesson shows pg_relation_size reporting a table's total disk footprint. The file-organization lesson shows CLUSTER physically rewriting rows to a new order. The why-storage-layout lesson shows table size directly predicting full-scan cost.\n\nIf a table were clustered (sorted) rather than left as a heap, would pg_relation_size change, and would a full table scan's cost change?",
        "pg_relation_size would stay roughly the same, since CLUSTER only reorders existing rows rather than adding or removing data; but a full table scan's cost would also stay roughly the same, since a sequential scan reads every page regardless of the order those pages are in — clustering helps range queries and index-based lookups specifically, not a full scan that has to touch everything anyway.",
        "hard", "analyze", "file-organization-heap-sorted-and-hashed-files",
        "pg_relation_size would stay about the same (CLUSTER just reorders, doesn't add data), and a full scan's cost would also stay about the same, since it reads every page regardless of their order",
        ["pg_relation_size would shrink significantly, since CLUSTER removes redundant data during reordering", "A full table scan would become dramatically faster after clustering, since the rows are now sorted", "Both pg_relation_size and full-scan cost would double after clustering, due to the reorganization overhead"],
    ),
    (
        "Reading a page costs the same whether the query needs 1 row or 100 rows from that page (how-data-is-stored). A heap offers no ordering guarantee (file-organization). A full scan's cost scales with table size regardless of how few rows are needed (why-storage-layout).\n\nWhat single underlying idea connects all three of these observations?",
        "The cost of reading data from a heap-organized table, at every level, is driven by how much of the table's physical structure (pages) must be touched, not by how many rows the query logically needs — the gap between \"rows needed\" and \"pages touched\" is exactly what indexes exist to close, a theme this chapter builds toward.",
        "hard", "analyze", "how-data-is-stored",
        "Cost is driven by how much physical structure (pages) must be touched, not by how many rows are logically needed — the gap between the two is what indexes exist to close",
        ["The three observations are unrelated facts that happen to appear in the same chapter", "Cost is always directly proportional to the number of rows a query logically needs, with no gap to close", "Pages, heaps, and full scans are three separate performance concerns with no shared underlying cause"],
    ),
    (
        "The lesson on why storage layout affects speed shows a full scan being sometimes the RIGHT choice (aggregating the whole table) and sometimes the WRONG choice (a selective filter with no index). The file-organization lesson shows heap being the DEFAULT despite offering no ordering guarantee.\n\nWhy might PostgreSQL choose heap as the default organization, given that it's described as \"weak for\" queries needing physical ordering?",
        "A heap optimizes for fast, simple writes with no reorganization overhead, which suits the common case where a table's actual query patterns aren't known in advance; sorted or hashed organization would need to be deliberately chosen once real query patterns become clear, which is exactly why CREATE INDEX exists as an added-on structure rather than heap being replaced as the default.",
        "hard", "understand", "file-organization-heap-sorted-and-hashed-files",
        "Heap optimizes for simple, fast writes with no reorganization cost, which is a sensible default before actual query patterns are known; indexes can then be added deliberately once those patterns become clear",
        ["Heap is chosen as the default purely because it's the oldest organization strategy historically", "Heap is actually not the default; the lesson's framing of it as default is inaccurate", "PostgreSQL chooses heap as the default because it always outperforms sorted and hashed organization"],
    ),
    (
        "The lesson notes that doubling row count roughly doubles both table size and full-scan cost — a linear relationship. Meanwhile, a primary key search uses an index instead of a full scan.\n\nBased on everything in this chapter, what would you predict happens to an index-based lookup's cost as table size doubles, compared to a full scan's cost doubling?",
        "An index-based lookup would be expected to grow much more slowly than a full scan's cost, since the whole reason an index exists is to give the database a shortcut that avoids touching every page — though this chapter doesn't detail the index's own internal structure, it establishes that the index scan bypasses the full-scan cost-to-size relationship entirely.",
        "medium", "apply", "why-storage-layout-affects-query-speed",
        "An index-based lookup would grow much more slowly than a full scan, since the index gives a shortcut that avoids the linear, table-size-driven cost of scanning every page",
        ["An index-based lookup would double in cost too, exactly matching the full scan's linear growth", "An index-based lookup's cost would be completely unrelated to table size, staying at zero regardless of growth", "An index-based lookup would actually become slower than a full scan as the table grows larger"],
    ),
]

SET1_SOURCES = [
    (HOW_DATA_IS_STORED, 0),
    (FILE_ORGANIZATION, 0),
    (WHY_STORAGE_LAYOUT_AFFECTS_SPEED, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS[:7])

SET2 = (
    HOW_DATA_IS_STORED[1:]
    + FILE_ORGANIZATION[1:]
    + WHY_STORAGE_LAYOUT_AFFECTS_SPEED[1:]
    + SYNTHESIS[7:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 7.1.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 7.1.2")
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
ws.title = "DBMS - MCQ - Unit 7.1"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 7 - Performance/7.1 - Storage and File Organization - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
