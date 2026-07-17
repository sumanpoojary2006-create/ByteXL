import random
import openpyxl

random.seed(83)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

UNION_UNION_ALL = [
    (
        "Tanvi needs one single mailing list combining names and emails from separate online_customers and store_customers tables, with no regard for which channel a customer originally came from.\n\nWhy is this not a job for JOIN?",
        "She isn't trying to match rows between the two tables and widen them with extra columns; she wants to stack the rows from both tables on top of each other into one combined list — that's a job for UNION, not JOIN.",
        "easy", "understand", "union-and-union-all",
        "She wants to stack rows from both tables vertically into one list, not match and widen rows with extra columns, which is what UNION does instead of JOIN",
        ["JOIN cannot be used with two tables that have the exact same column names", "JOIN would require the two tables to share a primary key, which they don't", "JOIN is actually the correct tool here, and UNION would be the wrong choice"],
    ),
    (
        "`SELECT customer_name, email FROM online_customers UNION SELECT customer_name, email FROM store_customers;` returns 5 rows even though Kavya Nair appears in both source tables.\n\nWhy does she appear only once in the combined result?",
        "UNION automatically removes exact duplicate rows across the two result sets, which is precisely the behavior Tanvi wants for a mailing list, since sending Kavya the same announcement twice would be an obvious mistake.",
        "easy", "understand", "union-and-union-all",
        "UNION automatically removes exact duplicate rows across the two combined result sets",
        ["Kavya's row was deleted from one of the source tables before the query ran", "UNION only returns rows from the first query listed, ignoring the second entirely", "The two tables were merged into one before the query, removing the duplicate at the source"],
    ),
    (
        "Tanvi wants to know exactly how many total customer records exist across both channels, including counting Kavya twice since she is genuinely a customer of both.\n\nWhich operator keeps every row from both queries with no deduplication, and how many rows would it return?",
        "UNION ALL keeps every row from both queries with no deduplication, returning 6 rows instead of 5, with Kavya Nair listed twice, once from each source table.",
        "easy", "apply", "union-and-union-all",
        "UNION ALL, returning 6 rows with Kavya Nair counted twice",
        ["UNION, returning 6 rows with Kavya Nair counted twice", "UNION ALL, returning 5 rows with Kavya Nair counted once", "INTERSECT ALL, returning 6 rows with Kavya Nair counted twice"],
    ),
    (
        "Beyond keeping duplicates, why is UNION ALL described as also being \"the more efficient\" choice when duplicates genuinely don't matter for the question being asked?",
        "UNION ALL is faster than plain UNION in most databases, since checking for and removing duplicates takes real work — skipping that duplicate check saves real work when deduplication isn't actually needed for the question at hand.",
        "medium", "understand", "union-and-union-all",
        "UNION ALL skips the duplicate-checking work that UNION must do, saving real computation when deduplication isn't needed",
        ["UNION ALL is faster only because it returns fewer rows than UNION", "UNION ALL and UNION always take exactly the same amount of time to run", "UNION ALL is faster because it doesn't require both queries to share the same columns"],
    ),
    (
        "`SELECT customer_name AS person, email AS contact_email, 'online' AS source FROM online_customers UNION ALL SELECT customer_name, email, 'store' FROM store_customers;` tags each row with its channel of origin.\n\nWhere do the final column headers \"person\" and \"contact_email\" come from, and does the second SELECT's column naming matter?",
        "The column names in the final result come from the first SELECT statement's aliases, regardless of what the second one calls them — the second SELECT's column names are ignored entirely for labeling purposes, though the values themselves still combine correctly, since only position and type matter, not name.",
        "medium", "analyze", "union-and-union-all",
        "The final headers come from the first SELECT's aliases; the second SELECT's column names don't matter for labeling, only their position and type",
        ["The final headers are a merge of both SELECT statements' column names", "The final headers come from the second SELECT's column names, not the first", "Both SELECT statements must use identical column aliases or the query fails"],
    ),
    (
        "Where can ORDER BY appear in a query combining two SELECT statements with UNION, and what does it sort?",
        "ORDER BY can only appear once, at the very end of the combined query, and it sorts the final stacked result rather than either query individually — placing it after both SELECT statements sorts the entire combined list.",
        "medium", "apply", "union-and-union-all",
        "Only once, at the very end of the combined query, sorting the final stacked result as a whole",
        ["Once per SELECT statement, sorting each query's rows independently before they're combined", "Anywhere in the query, since UNION ignores ORDER BY placement entirely", "Only immediately after the first SELECT statement, before UNION is applied"],
    ),
    (
        "Tanvi wants a single list of every unique email address across both channels, with no names, sorted alphabetically.\n\nWhich query correctly produces this?",
        "`SELECT email FROM online_customers UNION SELECT email FROM store_customers ORDER BY email;` returns 5 unique email addresses, with kavya.nair@example.com appearing only once despite being present in both source tables.",
        "medium", "apply", "union-and-union-all",
        "SELECT email FROM online_customers UNION SELECT email FROM store_customers ORDER BY email;",
        ["SELECT email FROM online_customers UNION ALL SELECT email FROM store_customers ORDER BY email;", "SELECT email FROM online_customers ORDER BY email UNION SELECT email FROM store_customers;", "SELECT DISTINCT email FROM online_customers, store_customers ORDER BY email;"],
    ),
    (
        "Both online_customers and store_customers share the same shape, a name and an email, which the lesson calls \"a requirement for combining them this way.\"\n\nWhat would happen if online_customers had a third column, say signup_date, that store_customers didn't have, and Tanvi tried to UNION both tables with SELECT * from each?",
        "The UNION would fail, since both SELECT statements combined with UNION must return the same number of columns, in compatible types, in the same order — a mismatched column count between the two sides is not allowed.",
        "medium", "analyze", "union-and-union-all",
        "The UNION would fail, since both queries must return the same number of columns for a UNION to be valid",
        ["The UNION would still succeed, simply leaving signup_date blank for store_customers rows", "The UNION would still succeed, and PostgreSQL would automatically add a matching column to store_customers", "The UNION would succeed, but only if signup_date were converted to text first"],
    ),
    (
        "If someone wanted a true total count of every customer record across both channels for billing purposes, but mistakenly used UNION instead of UNION ALL to count them.\n\nWhat would go wrong with their count?",
        "The count would undercount the true total, since UNION removes exact duplicate rows before the count happens, silently dropping Kavya Nair's second record even though she genuinely has two separate customer records, one per channel.",
        "medium", "apply", "union-and-union-all",
        "The count would undercount the true total, since UNION silently drops genuine duplicate records like Kavya's",
        ["The count would be identical either way, since UNION and UNION ALL always return the same row count", "The count would overcount the true total, since UNION adds extra rows to account for possible duplicates", "The query would fail with an error, since COUNT cannot be combined with UNION"],
    ),
    (
        "Does UNION or UNION ALL guarantee any particular row order in their combined result, if no ORDER BY is added?",
        "No — neither UNION nor UNION ALL guarantees any particular order on their own; ORDER BY must be added explicitly at the very end of the combined query to get a reliably ordered result, exactly the same rule that applies to a plain SELECT without ORDER BY.",
        "medium", "understand", "union-and-union-all",
        "No, neither guarantees any order; ORDER BY must be added explicitly at the end to get a reliable order",
        ["Yes, UNION always sorts alphabetically by the first column automatically", "Yes, UNION ALL always preserves insertion order, while UNION does not", "Yes, both operators automatically sort by whichever column has the most distinct values"],
    ),
    (
        "`SELECT customer_name AS person, email AS contact_email, 'online' AS source FROM online_customers UNION ALL SELECT customer_name, email, 'store' FROM store_customers;` adds a literal string as a third column to each query.\n\nWhat general pattern does adding a fixed literal value like 'online' or 'store' to each side of a UNION accomplish?",
        "It's a common pattern for tagging the origin of each row once separate sources get merged into one list, letting a later query still distinguish which original table a row came from, even after the two result sets have been combined into one.",
        "medium", "apply", "union-and-union-all",
        "It tags each row with its source, letting a later query distinguish which original table a merged row came from",
        ["It filters out rows that don't originally belong to the online_customers table", "It converts the query into an INTERSECT instead of a UNION", "It automatically deduplicates rows based on their source label"],
    ),
    (
        "If Tanvi tried `SELECT customer_name, email FROM online_customers UNION ALL SELECT customer_name, email, signup_channel FROM store_customers;` where the second query returns three columns instead of two.\n\nWhat would happen?",
        "The query would fail, since both SELECT statements combined with UNION ALL must return the same number of columns — a three-column second query cannot be combined with a two-column first query no matter how compatible the individual column types might be.",
        "medium", "analyze", "union-and-union-all",
        "The query would fail, since both sides of a UNION ALL must return the same number of columns",
        ["The extra column would simply be dropped silently, and the query would succeed with two columns", "The first query would automatically gain a third, empty column to match", "UNION ALL ignores column count mismatches, unlike plain UNION"],
    ),
]

INTERSECT_EXCEPT = [
    (
        "Tanvi needs to know exactly which customers shop both online and in-store, for a cross-channel loyalty reward.\n\nWhich set operation returns only the rows common to both queries?",
        "INTERSECT — it compares two result sets and keeps only the rows that appear in both, matching on every selected column at once.",
        "easy", "remember", "intersect-and-except",
        "INTERSECT",
        ["UNION", "EXCEPT", "UNION ALL"],
    ),
    (
        "`SELECT customer_name, email FROM online_customers INTERSECT SELECT customer_name, email FROM store_customers;` returns only Kavya Nair.\n\nWhat exactly must match for a row to survive an INTERSECT, and why does only Kavya qualify?",
        "A row must have the exact same customer_name and email in both online_customers and store_customers to survive, matching on every selected column at once — Kavya is the one customer whose full row appears identically in both tables.",
        "medium", "understand", "intersect-and-except",
        "The row must match on every selected column at once (both customer_name and email); Kavya is the only customer whose full row appears identically in both tables",
        ["Only the customer_name needs to match; email is ignored by INTERSECT", "Any customer appearing in either table qualifies, regardless of exact match", "INTERSECT requires the two tables to have identical row counts, which only Kavya's presence satisfies"],
    ),
    (
        "Tanvi needs online customers who have never once shopped in a physical store.\n\nWhich query correctly returns this, and what does it return?",
        "`SELECT customer_name, email FROM online_customers EXCEPT SELECT customer_name, email FROM store_customers;` returns Aditi Kulkarni and Rohan Das, the two online customers who don't appear anywhere in store_customers.",
        "medium", "apply", "intersect-and-except",
        "SELECT customer_name, email FROM online_customers EXCEPT SELECT customer_name, email FROM store_customers; — returns Aditi Kulkarni and Rohan Das",
        ["SELECT customer_name, email FROM store_customers EXCEPT SELECT customer_name, email FROM online_customers; — returns Aditi Kulkarni and Rohan Das", "SELECT customer_name, email FROM online_customers INTERSECT SELECT customer_name, email FROM store_customers; — returns Aditi Kulkarni and Rohan Das", "SELECT customer_name, email FROM online_customers UNION SELECT customer_name, email FROM store_customers; — returns Aditi Kulkarni and Rohan Das"],
    ),
    (
        "Reversing the two queries in `store_customers EXCEPT online_customers` instead of `online_customers EXCEPT store_customers` returns a completely different result: Imran Sheikh and Neha Bhatt instead of Aditi Kulkarni and Rohan Das.\n\nWhy does EXCEPT behave this way, unlike UNION and INTERSECT?",
        "Unlike UNION and INTERSECT, where the order of the two queries doesn't change the final set of rows returned, EXCEPT is directional, much like regular subtraction: 5 minus 2 is not the same as 2 minus 5.",
        "medium", "analyze", "intersect-and-except",
        "EXCEPT is directional like subtraction, unlike UNION and INTERSECT which are order-independent",
        ["EXCEPT is actually a bug in most databases and should never change based on order", "EXCEPT only appears to change because the two tables have different numbers of rows", "UNION and INTERSECT are also directional; this is not actually unique to EXCEPT"],
    ),
    (
        "`SELECT customer_name FROM online_customers INTERSECT SELECT customer_name FROM store_customers;` drops down to just the customer_name column, compared to the earlier two-column version.\n\nWhat risk does this narrower query introduce that the two-column version avoided?",
        "If two different customers happened to share the exact same name across the two tables but had different emails, this narrower query would treat them as the same person, while the earlier two-column version would correctly keep them apart — choosing which columns to include in a set operation is choosing exactly how strict the matching should be.",
        "hard", "analyze", "intersect-and-except",
        "Two genuinely different customers sharing the same name (but different emails) would be incorrectly treated as the same person",
        ["There is no real risk; the narrower query always produces identical results to the two-column version", "The narrower query would fail to run, since INTERSECT requires at least two columns", "The narrower query would return more rows than the two-column version, not fewer"],
    ),
    (
        "Tanvi wants to confirm the loyalty reward list using INTERSECT but starting from store_customers instead of online_customers this time.\n\nWhat does `SELECT customer_name, email FROM store_customers INTERSECT SELECT customer_name, email FROM online_customers;` return, and what does this confirm about INTERSECT's order-sensitivity compared to EXCEPT?",
        "It still returns just Kavya Nair, confirming that unlike EXCEPT, swapping the order of the two queries in an INTERSECT does not change which rows come back.",
        "medium", "apply", "intersect-and-except",
        "Still just Kavya Nair, confirming that swapping query order doesn't change INTERSECT's result, unlike EXCEPT",
        ["An empty result, since swapping the order of an INTERSECT always returns nothing", "Both Kavya Nair and Aditi Kulkarni, since order affects INTERSECT the same way it affects EXCEPT", "An error, since INTERSECT requires the first query to always be the smaller table"],
    ),
    (
        "If Tanvi ran INTERSECT between online_customers and a hypothetical third table with completely different customers, no names or emails overlapping at all.\n\nWhat would the query return, and would it raise an error?",
        "It would return an empty result set with no error at all — INTERSECT simply finds zero rows common to both queries when there's no overlap, which is a perfectly valid, if unexciting, outcome rather than a failure.",
        "medium", "apply", "intersect-and-except",
        "An empty result set, with no error — finding zero common rows is a valid outcome, not a failure",
        ["An error, since INTERSECT requires at least one matching row to run successfully", "The full contents of online_customers, since INTERSECT defaults to the first table when nothing matches", "NULL values in place of every row, rather than an empty result"],
    ),
    (
        "EXCEPT is called MINUS in some databases like Oracle, though PostgreSQL and MySQL both use EXCEPT.\n\nWhat does this naming difference reveal about SQL and database portability?",
        "The underlying set operation (subtracting one result set from another) is a standard, shared concept across relational databases, but the specific keyword used to invoke it can vary by vendor — a query using EXCEPT would need to be rewritten to use MINUS to run unchanged on a database that only recognizes the other name.",
        "hard", "analyze", "intersect-and-except",
        "The underlying operation is a shared, standard concept, but the specific keyword naming it can vary by database vendor, requiring rewrites when porting queries",
        ["EXCEPT and MINUS are actually completely different operations with unrelated behavior", "This naming difference means EXCEPT cannot be used in PostgreSQL at all", "MINUS is a deprecated feature that no modern database vendor still supports"],
    ),
    (
        "Must the two queries combined with INTERSECT or EXCEPT have exactly identical data types for each column, or is there more flexibility than that?",
        "The columns must be in compatible types, not strictly identical ones — the same relaxed requirement covered for UNION, since the underlying comparison can often reconcile closely related types (like different numeric types) as long as they're meaningfully comparable.",
        "medium", "understand", "intersect-and-except",
        "Compatible types are sufficient; the columns don't need to be strictly identical data types",
        ["The types must be strictly identical; even compatible numeric types like integer and numeric would fail", "Data types are ignored entirely by INTERSECT and EXCEPT, unlike UNION", "Only text columns can ever be compared with INTERSECT or EXCEPT"],
    ),
    (
        "INTERSECT is described as comparing \"on every selected column at once,\" the same rule EXCEPT follows.\n\nIf Tanvi ran EXCEPT using only the customer_name column (dropping email), would the result be identical to the two-column version, larger, or smaller?",
        "It could return fewer rows kept (a smaller or equal result), since dropping email means two different customers who happen to share a name would now be treated as a match and excluded, whereas the two-column version would have correctly told them apart and kept at least one of them.",
        "hard", "analyze", "intersect-and-except",
        "It could return a smaller (or equal) result, since matching on fewer columns makes it easier for rows to be treated as matching and get excluded",
        ["It would always return exactly the same result regardless of how many columns are compared", "It would always return more rows, since fewer columns means a broader match", "The query would fail to run with fewer columns specified"],
    ),
]

SET_OPS_VS_JOINS = [
    (
        "Tanvi notices an INTERSECT query and a NOT EXISTS-based anti join both seem to answer similar \"does this row also appear elsewhere\" questions.\n\nWhat's the short version of the structural difference between joins and set operations, according to the lesson?",
        "Joins combine columns from two tables side by side (widening a row), while set operations combine entire rows from two queries stacked vertically (never adding columns) — that structural difference decides which tool actually fits a given question.",
        "easy", "understand", "set-operations-vs-joins",
        "Joins widen rows sideways with columns from two tables; set operations stack or compare whole rows vertically, never adding columns",
        ["Joins and set operations are simply two different names for the exact same operation", "Joins stack rows vertically; set operations widen rows sideways, the reverse of the correct pairing", "Set operations can only be used on a single table, while joins require exactly two"],
    ),
    (
        "`SELECT o.customer_name, o.email, s.customer_name AS store_side_name FROM online_customers o JOIN store_customers s ON o.email = s.email;` and the earlier INTERSECT version can both answer \"who shops in both channels.\"\n\nWhat can the JOIN version do that the INTERSECT version structurally cannot?",
        "Only the join naturally supports pulling in extra, non-matching columns from either side, such as a loyalty tier stored only on the store side — the INTERSECT version returns exactly the matching people but as a single set of columns, not a widened row that could carry additional unmatched columns.",
        "medium", "analyze", "set-operations-vs-joins",
        "The join can pull in extra, non-matching columns from either side (like a loyalty tier), which INTERSECT's row-stacking approach cannot naturally do",
        ["The join always runs faster than the equivalent INTERSECT query", "The INTERSECT version can pull in extra columns, but the join cannot", "There's no real difference; both versions can equally pull in unrelated columns"],
    ),
    (
        "A NOT EXISTS-based anti join and an EXCEPT-based query can produce identical results for a single-table, single-condition case.\n\nHow does the lesson say the two read differently, guiding which to reach for?",
        "The NOT EXISTS version reads naturally as \"keep this row if no match exists,\" and generalizes easily to conditions beyond a simple whole-row comparison. The EXCEPT version reads naturally as \"everything in the first list, minus everything in the second,\" often the more direct choice when the comparison genuinely is a whole-row match between two similarly shaped queries.",
        "medium", "understand", "set-operations-vs-joins",
        "NOT EXISTS reads as \"keep if no match exists\" and generalizes to complex conditions; EXCEPT reads as \"first list minus second,\" fitting whole-row comparisons between similarly shaped queries",
        ["NOT EXISTS and EXCEPT always produce different results, so there's no real choice to make", "EXCEPT generalizes to complex conditions better; NOT EXISTS fits whole-row comparisons better, the reverse pairing", "The two are functionally identical in every respect, including how they read"],
    ),
    (
        "According to the lesson, when should a JOIN specifically be the right choice, especially compared to a set operation?",
        "Reach for a join whenever the result needs columns from both tables sitting together in one row, especially when one side can legitimately match more than one row on the other side — an order joined to its customer and restaurant is a clear join situation, since a customer can have many orders.",
        "medium", "apply", "set-operations-vs-joins",
        "When the result needs columns from both tables together in one row, especially when one side can match many rows on the other",
        ["Whenever both queries return the exact same shape of row with the same columns", "Only when checking whether a row exists at all, with no interest in its columns", "Only when the two tables involved have no primary keys defined"],
    ),
    (
        "According to the lesson, when should EXISTS or NOT EXISTS specifically be the right choice, rather than a plain set operation?",
        "Reach for EXISTS or NOT EXISTS when the existence check involves a condition more complex than matching every column, or when a second table is being checked against without any interest in its columns at all, such as \"does this customer have at least one order over 1000\" — a check a plain set operation between differently shaped tables cannot express.",
        "medium", "apply", "set-operations-vs-joins",
        "When the existence check involves a condition more complex than a full-row match, or checks a second table with no interest in its columns at all",
        ["Only when the two tables being compared have identical column names", "Only when the result needs to be sorted with ORDER BY afterward", "Whenever a join would return more than one row per match"],
    ),
    (
        "Tanvi needs every customer name that appears in exactly one of the two tables, not both, the customers who shop through only one channel.\n\nWhich approach correctly builds this from EXCEPT and UNION ALL?",
        "`(SELECT customer_name FROM online_customers EXCEPT SELECT customer_name FROM store_customers) UNION ALL (SELECT customer_name FROM store_customers EXCEPT SELECT customer_name FROM online_customers);` returns Aditi Kulkarni, Rohan Das, Imran Sheikh, and Neha Bhatt, everyone who shops through exactly one channel.",
        "hard", "apply", "set-operations-vs-joins",
        "Run EXCEPT once in each direction (online minus store, and store minus online), then combine both results with UNION ALL",
        ["Run INTERSECT once, then subtract the result from UNION using EXCEPT", "Run EXCEPT only once, from online_customers to store_customers, with no need for UNION ALL", "Run UNION ALL first on both tables, then apply EXCEPT to remove duplicates"],
    ),
    (
        "The lesson's final table lists \"Checking existence against NULL-containing columns\" as best fit for EXISTS/NOT EXISTS over IN/NOT IN.\n\nWhy does this guidance connect back to a risk covered in the joins chapter?",
        "NOT IN silently returns zero rows for every row if even one NULL appears in its subquery's results, a well-known trap that NOT EXISTS does not share, since NOT EXISTS tests for the presence of a matching row directly rather than comparing against a list of values that could include a NULL.",
        "hard", "analyze", "set-operations-vs-joins",
        "NOT IN silently breaks (returns zero rows for everything) if its subquery contains even one NULL, a trap NOT EXISTS avoids by testing for a matching row directly",
        ["EXISTS and NOT EXISTS cannot be used with NULL-containing columns at all, unlike IN and NOT IN", "IN and NOT IN both handle NULL values perfectly safely, unlike EXISTS and NOT EXISTS", "This guidance is unrelated to anything covered in the earlier joins chapter"],
    ),
    (
        "A JOIN naturally allows a customer to appear multiple times if they match multiple rows on the other side, and it can pull in extra unmatched columns from either table.\n\nCould a plain INTERSECT between two same-shaped queries ever produce this same duplicated-row, extra-column behavior?",
        "No — INTERSECT enforces that both queries return exactly the same shape (same columns) and removes duplicates from its result by definition, so it can never produce either the row-multiplying behavior or the extra-column widening that a JOIN naturally supports.",
        "hard", "analyze", "set-operations-vs-joins",
        "No, INTERSECT enforces identical row shape and removes duplicates, so it can never multiply rows or widen them with extra columns the way a JOIN can",
        ["Yes, INTERSECT can be configured to preserve duplicates and pull in extra columns, just like a JOIN", "Yes, but only when the two queries involved have more than 100 rows each", "INTERSECT and JOIN always produce mathematically identical results for any input"],
    ),
    (
        "\"Does this customer have at least one order over 1000\" is given as an example question that \"a plain set operation between differently shaped tables cannot express.\"\n\nWhy can't a set operation like INTERSECT directly answer this, when customers and orders are two different tables?",
        "Set operations require both queries to return the same shape of row to compare or stack them meaningfully, but a customers table and an orders table (filtered by amount) don't naturally produce comparably-shaped rows for this kind of existence check — EXISTS, which doesn't require matching row shapes at all, fits this situation instead.",
        "hard", "analyze", "set-operations-vs-joins",
        "Set operations require both queries to already share the same row shape, which customers and a filtered orders table don't naturally have for this kind of check",
        ["Set operations can express this perfectly well; EXISTS is never actually needed for it", "It's because customers and orders don't share a foreign key relationship at all", "It's because INTERSECT can only ever be used on a single table, never two different tables"],
    ),
    (
        "Tanvi's \"customers who shop through only one channel\" report was built using EXCEPT run twice, combined with UNION ALL.\n\nCould this same report instead be built using two NOT EXISTS checks combined with UNION ALL, based on the lesson's earlier point that NOT EXISTS and EXCEPT can produce identical results for single-table comparisons?",
        "Yes — since NOT EXISTS and EXCEPT are shown to produce identical results for this kind of whole-row, single-condition comparison, each EXCEPT could be replaced with an equivalent NOT EXISTS check (customers with no match in the other table), still combined with UNION ALL to merge both one-directional results into one report.",
        "medium", "apply", "set-operations-vs-joins",
        "Yes, each EXCEPT could be replaced with an equivalent NOT EXISTS check, since the two approaches produce identical results for this kind of comparison",
        ["No, NOT EXISTS can only ever check one table at a time and cannot be combined with UNION ALL", "No, EXCEPT and NOT EXISTS always produce different results and cannot be substituted for each other", "Yes, but only if the customers who shop through both channels are removed first with INTERSECT"],
    ),
    (
        "The lesson's decision table lists four situations: needing columns from both tables in one row, one side matching many rows on the other, two same-shaped queries comparing whole rows, and an existence check with a condition beyond a simple column match.\n\nWhich tool does each of these four situations map to, respectively?",
        "Join, join, set operation (UNION/INTERSECT/EXCEPT), and EXISTS/NOT EXISTS, respectively — each situation in the table maps directly to the tool built specifically for that shape of question.",
        "medium", "remember", "set-operations-vs-joins",
        "Join, join, a set operation, and EXISTS/NOT EXISTS, in that order",
        ["Set operation, EXISTS, join, join, the reverse of the correct mapping", "All four situations map to the same tool: JOIN, regardless of the specifics", "EXISTS, EXISTS, join, set operation, in that order"],
    ),
]

SYNTHESIS = [
    (
        "Tanvi's UNION removes exact duplicate rows automatically, while her later INTERSECT keeps only rows common to both queries, and EXCEPT keeps only rows unique to the first query.\n\nHow do these three operators relate to each other as a family, in terms of what portion of two result sets each one keeps?",
        "UNION keeps everything from either result set (the combined total, deduplicated), INTERSECT keeps only the overlap between them, and EXCEPT keeps only what's in the first set but missing from the second — three different slices of the same underlying comparison between two similarly shaped result sets.",
        "medium", "analyze", "intersect-and-except",
        "UNION keeps everything from either set; INTERSECT keeps only the overlap; EXCEPT keeps only what's in the first set but absent from the second",
        ["All three operators return exactly the same rows, just in a different order", "UNION keeps only the overlap; INTERSECT keeps everything; EXCEPT is identical to UNION ALL", "EXCEPT keeps everything from both sets; UNION and INTERSECT both keep only the overlap"],
    ),
    (
        "Both UNION/UNION ALL and INTERSECT/EXCEPT require the two combined queries to return the same number of columns, in compatible types, in the same order.\n\nWhy does this shared column-shape requirement make sense given what set operations fundamentally do, as distinguished from what a JOIN does?",
        "Since set operations stack or compare whole rows rather than widening them with new columns from a second table, every row being compared or stacked must already share the same shape for the comparison to mean anything — a join has no such requirement because it explicitly attaches differently-shaped tables together rather than comparing rows of identical shape.",
        "hard", "analyze", "union-and-union-all",
        "Since set operations compare or stack whole rows without adding new columns, the rows being compared must already share the same shape for the operation to make sense",
        ["The requirement exists purely as an arbitrary SQL syntax rule with no functional reason", "JOIN has the exact same column-shape requirement as set operations, for the same reason", "The requirement only applies to UNION, not to INTERSECT or EXCEPT"],
    ),
    (
        "Tanvi's UNION ALL row-count question (\"how many total customer records exist across both channels\") and her JOIN-vs-set-operation comparison both hinge on whether duplicates or matches should be collapsed or preserved.\n\nWhat's the common thread between choosing UNION vs. UNION ALL, and choosing a JOIN vs. a set operation for a \"who's in both\" question?",
        "Both decisions come down to whether the question genuinely needs deduplicated, one-row-per-entity output (UNION, or a set operation like INTERSECT) or needs every individual occurrence and its full row context preserved (UNION ALL, or a JOIN pulling in extra columns) — the right tool always follows from exactly what the underlying business question is actually asking for.",
        "hard", "analyze", "set-operations-vs-joins",
        "Both decisions hinge on whether the question needs deduplicated, single-row output or needs every occurrence and its full context preserved",
        ["Both decisions are actually unrelated and depend on completely different technical factors", "UNION ALL and JOIN always produce identical results, just with different syntax", "The choice depends solely on which table has more rows, not on the underlying question"],
    ),
    (
        "The chapter ends noting that Tanvi's cross-channel shopper list, mailing list, and channel-exclusive lists are all \"set membership\" questions, contrasted with an order needing its customer's and restaurant's names attached, which is a \"join\" question.\n\nWhat single question would a developer ask themselves to decide between these two categories of tool for a new reporting requirement?",
        "Does the answer require columns from two different kinds of things sitting together in one row (a join, like an order needing its customer's name attached), or does it require determining which rows belong to one group, another group, both, or neither, when both queries already return the same shape of row (a set operation, like customers shopping in one channel versus another)?",
        "medium", "understand", "set-operations-vs-joins",
        "Whether the answer needs columns from two different kinds of things combined in one row (join), or needs to determine group membership across similarly shaped rows (set operation)",
        ["Whether the query involves more than one table at all, regardless of what's being asked", "Whether the tables involved have primary keys defined, regardless of the question being asked", "Whether the report needs to be sorted, since only joins support ORDER BY"],
    ),
    (
        "UNION removes duplicate rows by default, and INTERSECT also removes duplicates from its result by definition (it only ever keeps one copy of each row common to both queries).\n\nWhat does this shared default reveal about deduplication across the whole family of set operations, compared to a plain JOIN?",
        "Deduplication is the default behavior across the set-operation family (UNION, INTERSECT, and EXCEPT all implicitly deduplicate, with UNION ALL as the explicit exception that preserves duplicates), while a JOIN has no equivalent default at all — it naturally preserves however many matching rows exist on each side, duplicating a row once per match rather than collapsing repeats.",
        "hard", "analyze", "union-and-union-all",
        "Deduplication is the shared default across UNION, INTERSECT, and EXCEPT (with UNION ALL as the explicit exception); JOIN has no such default and naturally preserves one row per match, including repeats",
        ["JOIN also deduplicates by default, exactly like UNION and INTERSECT", "None of the set operations deduplicate by default; only UNION ALL does", "Deduplication only applies to UNION; INTERSECT and EXCEPT always preserve duplicates"],
    ),
    (
        "Across the whole unit, 4.1 transforms individual values, 4.2 summarizes groups of rows into aggregate numbers, 4.3 attaches related columns from other tables, and 4.4 covers set operations.\n\nWhat capability does 4.4 uniquely add to the toolkit that the other three chapters don't provide?",
        "The ability to compare or combine entire result sets based on row membership, everything in either set, only what's common to both, or only what's in one but not the other, rather than transforming individual values, summarizing rows into group totals, or attaching columns from a related table.",
        "medium", "understand", "set-operations-vs-joins",
        "The ability to compare or combine whole result sets by row membership (union, overlap, or difference), distinct from value transformation, group summarization, or attaching related columns",
        ["4.4 is really just a repeat of the JOIN chapter using different keywords", "4.4 uniquely adds the ability to change a column's data type mid-query", "4.4 is the only chapter that introduces the WHERE clause for the first time"],
    ),
    (
        "UNION's automatic deduplication and DISTINCT (from the SELECT chapter) both remove exact duplicate values, but they operate on different things: DISTINCT collapses repeats within a single query's result, while UNION collapses repeats across two combined queries' results.\n\nWhat would `SELECT customer_name, email FROM online_customers UNION ALL SELECT customer_name, email FROM online_customers;` (unioning a table with itself) reveal about the relationship between DISTINCT and UNION?",
        "It would return every row from online_customers twice, since UNION ALL performs no deduplication at all; running `SELECT DISTINCT customer_name, email FROM (that UNION ALL query)` would then be needed to remove the duplication, showing that DISTINCT and UNION (without ALL) both ultimately rely on the same underlying deduplication logic, just applied to different starting result sets.",
        "hard", "analyze", "union-and-union-all",
        "It would return every row twice (since UNION ALL never deduplicates), showing that DISTINCT and plain UNION both rely on the same deduplication logic, just applied to different result sets",
        ["It would return each row only once automatically, since UNION ALL always deduplicates identical tables", "It would raise an error, since a table cannot be unioned with itself", "DISTINCT and UNION are entirely unrelated operations with no shared logic"],
    ),
]

SET1_SOURCES = [
    (UNION_UNION_ALL, 0),
    (INTERSECT_EXCEPT, 0),
    (SET_OPS_VS_JOINS, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS[:7])

SET2 = (
    UNION_UNION_ALL[1:]
    + INTERSECT_EXCEPT[1:]
    + SET_OPS_VS_JOINS[1:]
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
            "topics": "sql-for-data-retrieval-and-analytics",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 4.4.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 4.4.2")
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
ws.title = "DBMS - MCQ - Unit 4.4"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 4 - SQL for Data Retrieval and Analytics/4.4 - Set Operations and Combining Queries - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
