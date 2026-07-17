import random
import openpyxl

random.seed(73)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

AGGREGATE_FUNCTIONS = [
    (
        "Priya needs to answer \"how many orders did we get this month?\" against the orders table.\n\nWhich query correctly answers this?",
        "`SELECT COUNT(*) AS total_orders FROM orders;` — COUNT(*) counts every row in the result set, regardless of what any column contains.",
        "easy", "remember", "aggregate-functions",
        "SELECT COUNT(*) AS total_orders FROM orders;",
        ["SELECT SUM(order_id) AS total_orders FROM orders;", "SELECT total_orders FROM orders;", "SELECT COUNT(order_id = NULL) AS total_orders FROM orders;"],
    ),
    (
        "What's the difference between COUNT(*) and COUNT(column_name)?",
        "COUNT(*) counts every row in the result set regardless of column contents, while COUNT(column_name) counts only the rows where that specific column is not NULL, a distinction that matters once a table has optional fields.",
        "medium", "understand", "aggregate-functions",
        "COUNT(*) counts every row regardless of contents; COUNT(column_name) counts only rows where that column is not NULL",
        ["COUNT(*) and COUNT(column_name) always return exactly the same number", "COUNT(*) counts non-NULL values; COUNT(column_name) counts every row regardless of content", "COUNT(*) only works on numeric columns; COUNT(column_name) works on any column"],
    ),
    (
        "`SELECT SUM(amount) AS total_revenue, AVG(amount) AS average_order_value FROM orders;` — what do SUM and AVG each compute, and how do they treat NULL values in the amount column?",
        "SUM adds up every value in the column across all matching rows; AVG divides that sum by the row count automatically. Both functions ignore NULL values in the column being summarized, rather than treating a NULL as zero.",
        "medium", "understand", "aggregate-functions",
        "SUM totals the column, AVG computes its average, and both ignore NULL values rather than treating them as zero",
        ["SUM and AVG both treat NULL as zero, including it in their calculations", "SUM ignores NULLs, but AVG treats them as zero, skewing the average downward", "SUM and AVG both raise an error if any row in the column is NULL"],
    ),
    (
        "Priya asks for the biggest single sale in the orders table.\n\nWhich query correctly answers this, and can MIN/MAX be used on non-numeric columns too?",
        "`SELECT MAX(amount) AS largest_order FROM orders;` — MAX returns the largest value found across all matching rows. MIN and MAX work on dates and text too, not just numbers, so MIN(order_date) would return the earliest date in the table.",
        "medium", "apply", "aggregate-functions",
        "SELECT MAX(amount) AS largest_order FROM orders; — and yes, MIN/MAX also work on dates and text, not just numbers",
        ["SELECT MAX(amount) AS largest_order FROM orders; — but MIN/MAX only work on numeric columns", "SELECT TOP(amount) AS largest_order FROM orders;", "SELECT amount FROM orders ORDER BY amount DESC;"],
    ),
    (
        "`SELECT COUNT(*) AS total_orders, SUM(amount) AS total_revenue, ROUND(AVG(amount), 2) AS average_order_value, MIN(amount) AS smallest_order, MAX(amount) AS largest_order FROM orders;` runs all five aggregates in one SELECT, with no GROUP BY.\n\nHow many rows does this query return?",
        "Exactly one summary row for the whole table — with no GROUP BY, every aggregate function summarizes the entire result set into a single row, the shape a founder-facing summary dashboard query usually takes.",
        "medium", "analyze", "aggregate-functions",
        "Exactly one row, since with no GROUP BY, all five aggregates summarize the entire table into a single row",
        ["Eight rows, one per order in the table", "Five rows, one per aggregate function used", "Zero rows, since combining five aggregates in one query is invalid"],
    ),
    (
        "The founders want the total number of orders and total revenue specifically from the \"Fiction\" category, aliased as fiction_orders and fiction_revenue.\n\nWhich query correctly does this, and what does it return?",
        "`SELECT COUNT(*) AS fiction_orders, SUM(amount) AS fiction_revenue FROM orders WHERE category = 'Fiction';` returns 3 orders and 1380.00 in revenue, since WHERE narrows the rows down first and the aggregate functions only ever see what survives that filter.",
        "medium", "apply", "aggregate-functions",
        "SELECT COUNT(*) AS fiction_orders, SUM(amount) AS fiction_revenue FROM orders WHERE category = 'Fiction';",
        ["SELECT COUNT(*) AS fiction_orders, SUM(amount) AS fiction_revenue FROM orders HAVING category = 'Fiction';", "SELECT COUNT(*) AS fiction_orders, SUM(amount) AS fiction_revenue FROM orders GROUP BY category = 'Fiction';", "SELECT COUNT(category) AS fiction_orders, SUM(amount) AS fiction_revenue FROM orders;"],
    ),
    (
        "COUNT, SUM, AVG, MIN, and MAX are all described as answering \"whole-business questions raw rows cannot answer on their own.\"\n\nWhat do all five aggregate functions have in common structurally?",
        "Each one collapses an entire result set (or a filtered subset of it) down to a single summary number, requiring a look at every matching row rather than any single row in isolation — the defining trait of aggregation.",
        "hard", "analyze", "aggregate-functions",
        "Each one collapses an entire result set down to a single summary number, requiring every matching row to be considered together",
        ["Each one only ever looks at exactly one row at a time, like WHERE does", "Each one modifies the underlying table's stored values permanently", "Each one requires a GROUP BY clause in order to function at all"],
    ),
    (
        "Priya's smallest order is Aman Gupta's 175.00 children's book purchase, and the largest is Sonal Deshpande's 1450.00 non-fiction order, found using MIN(amount) and MAX(amount).\n\nDo MIN and MAX require the orders table to already be sorted before they can find these extremes?",
        "No — MIN and MAX scan every matching row and keep only the extreme value found, regardless of what order the rows happen to be stored or retrieved in; no ORDER BY or prior sorting is required for them to work correctly.",
        "medium", "understand", "aggregate-functions",
        "No, they scan every row directly and identify the extreme value regardless of row order, with no sorting required",
        ["Yes, the table must be sorted by amount first using ORDER BY before MIN or MAX will work", "Yes, but only MAX requires sorting; MIN works on unsorted data", "No, but only because the orders table happens to already be in date order"],
    ),
]

GROUPING_DATA = [
    (
        "The founders ask \"which category earns us the most, Fiction, Non-Fiction, or Children's books?\" A single SUM(amount) across the whole orders table cannot answer this.\n\nWhich clause splits the table into separate buckets, one per category, before the aggregate functions run?",
        "GROUP BY — `SELECT category, SUM(amount) AS category_revenue FROM orders GROUP BY category;` tells the database to gather all rows sharing the same category value into one group before SUM runs, producing three totals instead of one grand total.",
        "easy", "remember", "grouping-data",
        "GROUP BY",
        ["PARTITION BY", "HAVING", "DISTINCT"],
    ),
    (
        "`SELECT category, customer_name, SUM(amount) AS category_revenue FROM orders GROUP BY category;` fails with an error.\n\nWhy does including customer_name in the SELECT list break this query?",
        "Once rows are collapsed into a category group, customer_name no longer refers to a single value within that group — the Fiction group alone contains orders from both Ishita Rao and Vivek Menon, so the database has no single customer_name to return for that row.",
        "medium", "understand", "grouping-data",
        "customer_name isn't grouped or aggregated, so within a category group it could refer to multiple different customers with no single value to return",
        ["customer_name is spelled incorrectly in the query", "GROUP BY can only be used with exactly one column in the SELECT list", "SUM cannot be combined with any other column in the same SELECT list"],
    ),
    (
        "What rule does every column in a SELECT list need to satisfy once GROUP BY is used?",
        "Every column in the SELECT list must either appear in GROUP BY, or be wrapped in an aggregate function like SUM, COUNT, MIN, or MAX — either way, the database always knows exactly one value to produce per group.",
        "easy", "remember", "grouping-data",
        "It must either appear in GROUP BY, or be wrapped in an aggregate function",
        ["It must always be wrapped in an aggregate function, with no exceptions", "It must always appear in GROUP BY, even if it's also aggregated", "It must be numeric, since GROUP BY cannot be used with text columns"],
    ),
    (
        "`SELECT customer_name, category, COUNT(*) AS orders_placed, SUM(amount) AS total_spent FROM orders GROUP BY customer_name, category;` groups by two columns at once.\n\nWhat does grouping by more than one column produce?",
        "It produces one group for every distinct combination of the grouped values, so Ishita Rao's Fiction orders are summarized separately from her Non-Fiction orders, even though both belong to the same customer.",
        "medium", "apply", "grouping-data",
        "One group for every distinct combination of the grouped column values",
        ["One group per customer only, with category ignored entirely", "One group per category only, with customer_name ignored entirely", "A single combined group covering every customer and category together"],
    ),
    (
        "`SELECT category, SUM(amount) AS category_revenue FROM orders GROUP BY category ORDER BY category_revenue DESC;`\n\nWhat does GROUP BY control versus what ORDER BY controls here?",
        "GROUP BY collapses rows into groups but does not control what order those groups appear in; ORDER BY category_revenue DESC sorts the three grouped rows by their computed total, largest first, turning a plain summary into a ranked list.",
        "medium", "understand", "grouping-data",
        "GROUP BY collapses rows into groups; ORDER BY separately controls the display order of the resulting groups",
        ["GROUP BY controls the display order; ORDER BY controls which rows get grouped together", "GROUP BY and ORDER BY do exactly the same thing and either one alone suffices", "ORDER BY must come before GROUP BY in every query, controlling which columns are grouped"],
    ),
    (
        "The founders want each customer's order count and total spend, ranked from highest spender down, aliased as order_count and total_spent.\n\nWhich query correctly does this?",
        "`SELECT customer_name, COUNT(*) AS order_count, SUM(amount) AS total_spent FROM orders GROUP BY customer_name ORDER BY total_spent DESC;` — Ishita Rao comes out on top with three orders totaling 1760.00.",
        "medium", "apply", "grouping-data",
        "SELECT customer_name, COUNT(*) AS order_count, SUM(amount) AS total_spent FROM orders GROUP BY customer_name ORDER BY total_spent DESC;",
        ["SELECT customer_name, COUNT(*) AS order_count, SUM(amount) AS total_spent FROM orders ORDER BY total_spent DESC;", "SELECT customer_name, COUNT(*) AS order_count, SUM(amount) AS total_spent FROM orders GROUP BY total_spent ORDER BY customer_name;", "SELECT customer_name, COUNT(*) AS order_count, SUM(amount) AS total_spent FROM orders GROUP BY customer_name, total_spent DESC;"],
    ),
    (
        "Comparing `SELECT category, SUM(amount) FROM orders GROUP BY category;` against `SELECT customer_name, category, SUM(amount) FROM orders GROUP BY customer_name, category;`\n\nWhat's the structural relationship between the number of columns grouped and the granularity of the resulting summary?",
        "The more columns included in GROUP BY, the finer-grained (more numerous, more specific) the resulting groups become, since each additional grouped column further subdivides the existing groups by another distinct combination of values, moving from a category-level summary to a customer-and-category-level summary.",
        "hard", "analyze", "grouping-data",
        "Adding more columns to GROUP BY produces finer-grained, more numerous groups, since each column further subdivides existing groups",
        ["Adding more columns to GROUP BY always reduces the number of resulting groups", "The number of columns grouped has no effect on how many result rows are produced", "GROUP BY can only ever use exactly one or exactly two columns, never more"],
    ),
    (
        "The lesson states plainly: \"Non-grouped, non-aggregated column in SELECT\" is \"Not allowed; the database would not know which value to show.\"\n\nWhat general principle does this rule protect?",
        "It protects the guarantee that every group in a GROUP BY result produces exactly one, unambiguous value per selected column — allowing an ungrouped, unaggregated column would mean a single output row could legitimately correspond to several different underlying values with no way to pick one.",
        "medium", "analyze", "grouping-data",
        "It guarantees every group produces exactly one unambiguous value per selected column, preventing an output row from having several possible values with no way to choose",
        ["It protects against typos in column names within the SELECT list", "It ensures GROUP BY queries always run faster than ungrouped queries", "It prevents a table from having more rows than columns"],
    ),
]

FILTERING_GROUPS = [
    (
        "Priya tries `SELECT customer_name, SUM(amount) FROM orders WHERE SUM(amount) > 1000 GROUP BY customer_name;` and it fails with an error about aggregate functions not being allowed there.\n\nWhy can't WHERE filter on SUM(amount)?",
        "WHERE runs before GROUP BY ever forms groups, back when the database is still looking at individual rows, and no single row has a SUM(amount) value to compare — WHERE can only see columns that already exist on a row, not a total that hasn't been computed yet.",
        "easy", "understand", "filtering-groups",
        "WHERE filters individual rows before grouping happens, so the aggregate total doesn't exist yet at that stage",
        ["WHERE can only compare against text columns, never numeric aggregates", "SUM(amount) is spelled incorrectly and should be SUM(amounts) instead", "WHERE and GROUP BY cannot be used together in the same query at all"],
    ),
    (
        "Which clause is built specifically to filter groups after they've already been summarized by an aggregate function?",
        "HAVING — it runs after GROUP BY has already collapsed rows into groups and the aggregate functions have already produced their results, so it can filter directly on those aggregate values.",
        "easy", "remember", "filtering-groups",
        "HAVING",
        ["WHERE", "FILTER", "QUALIFY"],
    ),
    (
        "`SELECT customer_name, SUM(amount) AS total_spent FROM orders GROUP BY customer_name HAVING SUM(amount) > 1000;` is run against four customers, three with totals over 1000 and Aman Gupta with a total of 385.00.\n\nWhat happens to Aman Gupta's group?",
        "It's dropped from the result entirely, group and all — HAVING discards any group whose aggregate total does not exceed 1000, unlike a row-level filter that would only remove individual rows.",
        "medium", "apply", "filtering-groups",
        "His entire group is dropped from the result, since his total (385.00) doesn't exceed the HAVING threshold",
        ["Only his individual orders below 1000 are removed, but his name still appears with a partial total", "His group is kept but marked with a warning flag in the result", "Nothing happens; HAVING only filters numeric columns that aren't aggregated"],
    ),
    (
        "`SELECT customer_name, SUM(amount) AS total_spent FROM orders WHERE category != 'Children' GROUP BY customer_name HAVING SUM(amount) > 500;` runs in three stages.\n\nWhat does each of the three stages do, in order?",
        "First, WHERE category != 'Children' removes Aman Gupta's children's-book orders before any grouping starts. Second, GROUP BY forms totals from what remains. Third, HAVING SUM(amount) > 500 discards any customer whose remaining total doesn't clear 500.",
        "medium", "understand", "filtering-groups",
        "WHERE removes non-matching rows first, then GROUP BY forms totals from what remains, then HAVING discards groups below the threshold",
        ["HAVING removes rows first, then WHERE forms totals, then GROUP BY filters the result", "GROUP BY runs first, then HAVING removes rows, then WHERE filters the final totals", "All three clauses run simultaneously in no particular order"],
    ),
    (
        "`SELECT customer_name, COUNT(*) AS orders_placed FROM orders GROUP BY customer_name HAVING COUNT(*) >= 3;` filters on COUNT instead of SUM.\n\nWhat does this query surface, and is HAVING limited to only SUM?",
        "It surfaces only the customers who placed 3 or more orders. HAVING works with any aggregate function, not just SUM — filtering on COUNT is often more useful than filtering on total spend for something like a loyalty program.",
        "medium", "apply", "filtering-groups",
        "Customers who placed 3 or more orders; HAVING can filter on any aggregate function, not just SUM",
        ["Customers whose total spend exceeds 3; HAVING can only filter on SUM", "The three highest-spending customers by rank; HAVING requires ORDER BY to work", "This query is invalid, since HAVING only accepts SUM as its aggregate"],
    ),
    (
        "The founders want product categories that generated less than 1000 in total revenue.\n\nWhich clause correctly expresses \"less than 1000 in total revenue,\" and where does it belong in the query?",
        "`GROUP BY category HAVING SUM(amount) < 1000` — since \"total revenue\" is an aggregate (a SUM computed per category group), the condition belongs in HAVING, which runs after grouping, not in WHERE, which would run too early to see the computed sum.",
        "medium", "apply", "filtering-groups",
        "HAVING SUM(amount) < 1000, placed after GROUP BY category",
        ["WHERE SUM(amount) < 1000, placed before GROUP BY category", "HAVING amount < 1000, placed before GROUP BY category", "WHERE amount < 1000, placed after GROUP BY category"],
    ),
    (
        "WHERE and HAVING are described as \"not interchangeable, but they work well together, since each one filters at a different stage.\"\n\nWhy might filtering some rows out with WHERE before grouping, rather than filtering everything with HAVING after grouping, be described as \"often cheaper\"?",
        "WHERE removes rows before any grouping work happens at all, so the database never has to bother computing aggregate totals for rows that were never going to matter anyway, unlike relying purely on HAVING, which would still group everything first and only discard unwanted groups afterward.",
        "hard", "analyze", "filtering-groups",
        "WHERE removes irrelevant rows before any grouping work happens, avoiding the cost of aggregating data that will just be discarded later",
        ["WHERE is always faster than HAVING regardless of what it filters on", "HAVING actually runs before WHERE, making WHERE the more expensive option", "There's no real performance difference; the phrase refers only to readability"],
    ),
    (
        "A report needs both \"only orders placed by returning customers\" (a row-level fact known before grouping) and \"only customer groups with total spend over 500\" (a fact only known after summing).\n\nWhich clause should express each condition, and why?",
        "The row-level condition (\"returning customer\") belongs in WHERE, since it can be checked directly on each individual order row before any grouping occurs. The aggregate condition (\"total spend over 500\") belongs in HAVING, since it depends on a SUM that only exists once rows have already been grouped.",
        "medium", "apply", "filtering-groups",
        "The row-level condition belongs in WHERE (checkable per-row, before grouping); the aggregate condition belongs in HAVING (depends on a sum computed after grouping)",
        ["Both conditions must go in WHERE, since HAVING cannot be combined with WHERE in one query", "Both conditions must go in HAVING, since WHERE cannot be used alongside GROUP BY", "The row-level condition belongs in HAVING; the aggregate condition belongs in WHERE"],
    ),
]

COMBINING_AGGREGATION = [
    (
        "The founders' request \"total revenue by region, for regions with at least two customers, sorted highest revenue first, counting only orders after the first week of April\" needs several pieces working together.\n\nWhy is a JOIN specifically needed here, when region isn't even a filtering condition mentioned directly?",
        "Region information lives on a separate customers table, not on orders itself; a JOIN is needed to bring in region data that isn't stored on the orders table at all, before it can be grouped on or reported by.",
        "easy", "understand", "combining-aggregation-sorting-filtering-joins",
        "Region data lives on a separate customers table, and a JOIN is needed to attach it to each order before grouping by it",
        ["A JOIN is needed because WHERE cannot filter on dates without one", "A JOIN is needed only because HAVING requires at least two tables to function", "No JOIN is actually needed; region can be computed directly from order_id"],
    ),
    (
        "`SELECT c.region, SUM(o.amount) AS region_revenue FROM orders o JOIN customers c ON o.customer_name = c.customer_name GROUP BY c.region;`\n\nWhat does the JOIN accomplish before GROUP BY runs?",
        "The JOIN attaches each order to its customer's region before grouping ever happens, so GROUP BY c.region can collapse rows by a column that was never on the orders table to begin with — the join widens each row with extra columns, and grouping then works with whichever of those columns it needs.",
        "medium", "understand", "combining-aggregation-sorting-filtering-joins",
        "It attaches each order to its customer's region, widening each row so GROUP BY can use a column that wasn't originally on orders",
        ["It removes any order rows that don't have a matching region", "It automatically sorts the orders by region before grouping", "It converts the region column into a numeric aggregate value"],
    ),
    (
        "`... WHERE o.order_date > '2025-04-07' GROUP BY c.region;` filters by date before grouping.\n\nWhy does filtering with WHERE before GROUP BY, rather than after, change which orders count toward each region's total?",
        "WHERE removes rows that don't satisfy the date condition before grouping ever forms totals, so only orders 5 through 8 survive and get grouped; the West region's total then reflects only the surviving orders (Sonal's and Vivek's later order), not Vivek's earlier April 3rd order that was already filtered out.",
        "medium", "analyze", "combining-aggregation-sorting-filtering-joins",
        "WHERE removes non-matching rows before grouping happens, so only surviving rows are included in each region's total",
        ["WHERE has no effect on group totals; it only affects which columns are displayed", "Filtering after grouping would remove different rows than filtering before grouping produces the same result either way", "WHERE only filters the JOIN's matching logic, not the actual row set being grouped"],
    ),
    (
        "`... GROUP BY c.region HAVING COUNT(DISTINCT o.customer_name) >= 2 ORDER BY region_revenue DESC;`\n\nWhy does the query use COUNT(DISTINCT o.customer_name) rather than plain COUNT(*) to check for \"at least two customers\"?",
        "COUNT(DISTINCT o.customer_name) counts unique customers per region rather than unique orders, which matters because one customer with many orders should not be mistaken for many customers — COUNT(*) would overcount a region with one prolific customer as having many customers.",
        "medium", "apply", "combining-aggregation-sorting-filtering-joins",
        "COUNT(DISTINCT ...) counts unique customers, avoiding overcounting a region where one customer placed many orders as if it had many customers",
        ["COUNT(DISTINCT ...) and COUNT(*) always return identical results in this query", "COUNT(DISTINCT ...) is required syntax whenever HAVING is used with COUNT", "COUNT(DISTINCT ...) counts unique regions, not unique customers"],
    ),
    (
        "The lesson lists the actual execution order a query runs in: FROM/JOIN, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, even though the clauses are written in the fixed syntax order SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY.\n\nWhy does WHERE run at step 2, before GROUP BY at step 3, according to this logical order?",
        "Individual rows need to be filtered before any grouping happens, since WHERE only has access to raw row-level columns; the aggregate values GROUP BY and HAVING work with don't exist until grouping has actually occurred, which is exactly why WHERE cannot reference an aggregate like SUM(amount).",
        "medium", "understand", "combining-aggregation-sorting-filtering-joins",
        "WHERE filters raw rows before any grouping occurs, since aggregate values don't exist until after grouping happens",
        ["WHERE runs at step 2 purely because it's written before GROUP BY in the query text", "WHERE actually runs after GROUP BY, despite being written before it", "The written order and the execution order are always identical for every clause"],
    ),
    (
        "Why can ORDER BY reference a column alias defined in the SELECT list, like `ORDER BY region_revenue DESC` referencing `SUM(o.amount) AS region_revenue`, even though SELECT is written before ORDER BY in a query?",
        "Sorting happens last in the actual execution order, step 6, after SELECT (step 5) has already computed the final columns and their aliases — by the time ORDER BY runs, the alias already exists and can be referenced directly.",
        "hard", "analyze", "combining-aggregation-sorting-filtering-joins",
        "ORDER BY runs last in execution order, after SELECT has already computed the aliases, so it can reference them directly",
        ["Aliases can never actually be referenced in ORDER BY; this is a misconception", "ORDER BY runs before SELECT, so it must define its own aliases separately", "This only works because region_revenue happens to be a numeric column"],
    ),
    (
        "The founders want total revenue and order count per category, but only for orders from the West and South regions, only categories with more than one order, sorted by revenue descending.\n\nWhich sequence of clauses, applied to the joined orders/customers data, correctly builds this report?",
        "JOIN orders to customers, filter with WHERE c.region IN ('West', 'South'), group by o.category, filter with HAVING COUNT(*) > 1, then order by the summed revenue descending — Non-Fiction comes out on top at 3339.00, ahead of Fiction at 1380.00.",
        "hard", "apply", "combining-aggregation-sorting-filtering-joins",
        "JOIN, then WHERE on region, then GROUP BY category, then HAVING COUNT(*) > 1, then ORDER BY revenue DESC",
        ["HAVING on region, then JOIN, then WHERE on category, then GROUP BY, then ORDER BY", "GROUP BY category first, then JOIN, then WHERE on region, then HAVING, then ORDER BY", "ORDER BY revenue first, then JOIN, then WHERE, then GROUP BY, then HAVING"],
    ),
    (
        "In the region-revenue example, `SUM(o.amount) AS region_revenue` uses the alias o for orders and c for customers, defined via `FROM orders o JOIN customers c ON o.customer_name = c.customer_name`.\n\nWhy are table aliases especially useful once a query joins two tables and aggregates across them?",
        "Once a query references columns from more than one table (o.amount, c.region), aliases keep each column reference short and make it immediately clear which table a column comes from, without repeatedly typing the full table names \"orders\" and \"customers\" throughout the WHERE, GROUP BY, HAVING, and SELECT clauses.",
        "medium", "understand", "combining-aggregation-sorting-filtering-joins",
        "Aliases keep column references short and clearly indicate which table each column comes from, especially valuable once multiple tables and clauses are involved",
        ["Aliases are required by SQL syntax whenever GROUP BY is used with a JOIN", "Aliases automatically improve query performance by skipping the JOIN condition", "Aliases are only useful for single-table queries with no JOIN involved"],
    ),
]

SYNTHESIS = [
    (
        "Priya's plain aggregate query (no GROUP BY) produces one summary row for the whole orders table. Her GROUP BY query produces one row per category. Her GROUP BY + HAVING query further discards some of those category rows.\n\nWhat does this progression reveal about the relationship between aggregation, grouping, and group filtering?",
        "Aggregation alone summarizes an entire result set into one row; GROUP BY subdivides that summarization into multiple rows, one per distinct value (or combination); and HAVING then selectively removes some of those already-summarized rows based on their aggregate values — each step builds on the output of the one before it.",
        "medium", "analyze", "grouping-data",
        "Aggregation summarizes everything into one row; GROUP BY subdivides that into multiple summarized rows; HAVING then filters which of those summarized rows survive",
        ["All three do exactly the same thing in a different order, with no real relationship", "HAVING must always run before GROUP BY, which must always run before aggregation", "GROUP BY and aggregation are unrelated; only HAVING actually summarizes data"],
    ),
    (
        "Priya's HAVING lesson establishes that WHERE cannot reference an aggregate because it runs before grouping. Her combining-clauses lesson lists the full logical execution order: FROM/JOIN, WHERE, GROUP BY, HAVING, SELECT, ORDER BY.\n\nHow does this full execution order explain, in one coherent story, why WHERE filters raw rows while HAVING filters aggregate results?",
        "WHERE sits at step 2, immediately after tables are combined but before any grouping (step 3) has happened, so it can only see row-level data. HAVING sits at step 4, after grouping has already produced aggregate values, so it's the first clause capable of testing those aggregates — the two clauses aren't arbitrarily different, they're simply positioned at different points in one fixed pipeline.",
        "hard", "analyze", "filtering-groups",
        "WHERE sits before grouping in the fixed execution pipeline (row-level data only); HAVING sits after grouping (aggregate values available)",
        ["WHERE and HAVING actually run at the exact same step in the pipeline", "HAVING runs before WHERE in the actual execution order, reversing the written order", "The execution order has no bearing on what each clause can reference"],
    ),
    (
        "The region-revenue report joins orders to customers, filters by date with WHERE, groups by region, filters by customer count with HAVING, and sorts with ORDER BY, all in one query.\n\nWhat does this single query demonstrate about how JOIN and the aggregation pipeline (WHERE, GROUP BY, HAVING, ORDER BY) relate to each other?",
        "A JOIN isn't a separate skill from aggregation; it simply happens first in the pipeline (step 1, before WHERE even runs), supplying extra columns from another table that the rest of the aggregation pipeline can then filter, group, and sort by, exactly as if those columns had always lived on the original table.",
        "hard", "understand", "combining-aggregation-sorting-filtering-joins",
        "JOIN runs first in the pipeline, supplying extra columns that the rest of the aggregation pipeline (WHERE, GROUP BY, HAVING, ORDER BY) can then use normally",
        ["JOIN and aggregation are mutually exclusive and can never appear in the same query", "Aggregation always runs before any JOIN can be applied to a query's results", "JOIN only works after GROUP BY has already collapsed the rows into groups"],
    ),
    (
        "Priya's aggregate functions lesson notes SUM and AVG both ignore NULL values rather than treating them as zero. Her later lessons never revisit this fact directly, but it stays true throughout GROUP BY, HAVING, and the combined multi-clause queries.\n\nWhy does this NULL-handling behavior matter specifically once GROUP BY enters the picture, compared to when aggregates were computed over the whole table?",
        "Once rows are split into groups, a group that happens to contain only NULL values in the aggregated column would show a NULL or zero-row-count result rather than a misleading zero, and a group with a mix of NULL and real values would still average or sum correctly using only the real values — the same NULL-skipping behavior that mattered for a single whole-table total now needs to hold correctly within every individual group.",
        "hard", "analyze", "aggregate-functions",
        "The same NULL-skipping behavior must now hold correctly within every individual group, not just once across the whole table, since each group computes its own independent aggregate",
        ["NULL-handling stops mattering once GROUP BY is introduced, since groups can never contain NULL values", "GROUP BY automatically converts every NULL value to zero before aggregating", "SUM and AVG only skip NULLs when no GROUP BY clause is present in the query"],
    ),
    (
        "The founders' final combined-clause request needs a JOIN (for region), a WHERE (for date), a GROUP BY (for category), a HAVING (for order count), and an ORDER BY (for revenue rank), all built from skills introduced separately across earlier lessons in this chapter.\n\nWhat does the lesson's conclusion say this progression reveals about joins, filters, grouping, group filters, and sorting?",
        "They are not separate skills but stages of one pipeline that runs in a fixed order regardless of how the query is written, and understanding that order explains every rule about what each clause is and is not allowed to reference — a single mental model that scales from a two-clause query to a five-clause one.",
        "medium", "understand", "combining-aggregation-sorting-filtering-joins",
        "They are stages of one fixed-order pipeline, and understanding that order explains every rule about what each clause can and cannot reference",
        ["They are entirely independent techniques that happen to be usable in the same query by coincidence", "Only JOIN and WHERE are related; GROUP BY, HAVING, and ORDER BY are unrelated to them", "The order clauses are written in the query text is the only order that matters, with no separate execution order"],
    ),
    (
        "COUNT(*) counts every row regardless of NULLs, while COUNT(DISTINCT o.customer_name), used in the region report, counts only unique, non-NULL values.\n\nWhat's the combined effect of adding both DISTINCT and a specific column to COUNT, compared to plain COUNT(*)?",
        "COUNT(DISTINCT column) narrows counting in two ways at once compared to COUNT(*): it ignores NULLs in that column, and it collapses repeated values down to one count each, giving a count of unique, present values rather than a raw row count.",
        "hard", "analyze", "aggregate-functions",
        "COUNT(DISTINCT column) both ignores NULLs and collapses repeated values, giving a count of unique, present values rather than a raw row count",
        ["COUNT(DISTINCT column) behaves identically to COUNT(*) in every situation", "COUNT(DISTINCT column) counts NULLs but ignores duplicate values", "COUNT(DISTINCT column) only works when combined with GROUP BY, unlike COUNT(*)"],
    ),
    (
        "Priya's category breakdown (GROUP BY category) and her customer-and-category breakdown (GROUP BY customer_name, category) both use SUM(amount), but produce different numbers of result rows from the same eight orders.\n\nWhy does the second query typically produce more rows than the first, even though both summarize the exact same underlying data?",
        "Grouping by two columns creates a group for every distinct combination of both values, which is generally a finer split than grouping by one column alone; a customer who ordered from two different categories now gets two separate group rows instead of being folded into just one category-level row alongside other customers.",
        "hard", "analyze", "grouping-data",
        "Grouping by two columns creates a group per distinct combination of both, generally producing more, finer-grained rows than grouping by one column alone",
        ["The second query produces fewer rows, since customer_name narrows the results down further", "Both queries always produce exactly the same number of rows regardless of grouping columns", "The second query fails to run, since GROUP BY cannot use two columns with SUM"],
    ),
    (
        "Priya's chapter moves from single-table aggregation (COUNT, SUM, AVG, MIN, MAX) to GROUP BY, to HAVING, and finally to combining all of that with JOIN, WHERE, and ORDER BY in one query.\n\nWhat does this overall progression suggest about how complex reporting queries are typically built up in practice?",
        "Complex reporting queries are usually built incrementally from a small set of well-understood pieces, aggregation, grouping, group filtering, joining in outside data, row filtering, and sorting, layered together one at a time rather than invented from scratch as one intricate query, since each piece keeps the same behavior it had on its own.",
        "medium", "understand", "combining-aggregation-sorting-filtering-joins",
        "Complex queries are built incrementally by layering a small set of well-understood pieces together, each keeping its own consistent behavior",
        ["Complex queries require an entirely different set of SQL keywords not covered by the simpler lessons", "Each new clause added replaces and overrides the behavior of the previous ones", "Complex reporting queries cannot actually be decomposed into simpler, individually understandable pieces"],
    ),
]

SET1_SOURCES = [
    (AGGREGATE_FUNCTIONS, 0),
    (GROUPING_DATA, 0),
    (FILTERING_GROUPS, 0),
    (COMBINING_AGGREGATION, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS[:6])

SET2 = (
    AGGREGATE_FUNCTIONS[1:]
    + GROUPING_DATA[1:]
    + FILTERING_GROUPS[1:]
    + COMBINING_AGGREGATION[1:]
    + SYNTHESIS[6:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 4.2.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 4.2.2")
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
ws.title = "DBMS - MCQ - Unit 4.2"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 4 - SQL for Data Retrieval and Analytics/4.2 - Aggregation - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
