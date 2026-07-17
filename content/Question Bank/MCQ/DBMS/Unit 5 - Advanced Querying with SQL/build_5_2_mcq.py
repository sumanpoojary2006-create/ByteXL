import random
import openpyxl

random.seed(97)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

WHAT_IS_A_WINDOW_FUNCTION = [
    (
        "Leela wants to see every individual sale next to that salesperson's running total, but `SELECT salesperson, SUM(amount) FROM sales GROUP BY salesperson;` loses the individual sale rows.\n\nWhy does GROUP BY lose that detail?",
        "Grouping collapses many rows into one summary row per group, so the individual sale rows that made up each total are gone from the result — there's no way to see, in that same output, which specific sale contributed how much.",
        "easy", "understand", "what-is-a-window-function",
        "GROUP BY collapses many rows into one summary row per group, discarding the individual row-level detail",
        ["GROUP BY only works on numeric columns, and salesperson is text", "GROUP BY requires an ORDER BY clause before it can return any rows", "GROUP BY only shows the first row of each group, not a true summary"],
    ),
    (
        "`SELECT salesperson, sale_id, amount, SUM(amount) OVER (PARTITION BY salesperson) AS salesperson_total FROM sales;` returns all 6 original rows, each carrying an extra column.\n\nWhat does this demonstrate about how a window function differs from GROUP BY?",
        "A window function calculates something across a group of related rows, the way an aggregate does, but returns a value for every original row instead of collapsing them — every one of the 6 sale rows survives, each showing that salesperson's total repeated alongside it.",
        "easy", "understand", "what-is-a-window-function",
        "A window function computes an aggregate-style value but returns it on every original row instead of collapsing rows into one summary row",
        ["A window function only works when PARTITION BY is left out of the query entirely", "A window function behaves identically to GROUP BY in every respect", "A window function can only be used with the SUM function, unlike GROUP BY"],
    ),
    (
        "In `SUM(amount) OVER (PARTITION BY salesperson)`, what does PARTITION BY control, and how is that different from what GROUP BY controls?",
        "PARTITION BY only controls which rows are included in each calculation, leaving every original row in place; GROUP BY, by contrast, controls how many rows appear in the final result, collapsing each group into one row.",
        "medium", "analyze", "what-is-a-window-function",
        "PARTITION BY controls which rows are grouped together for the calculation, without reducing the row count; GROUP BY reduces the row count to one per group",
        ["PARTITION BY reduces the row count to one per group, exactly like GROUP BY does", "PARTITION BY and GROUP BY control exactly the same thing, with no functional difference", "PARTITION BY only works on date columns, unlike GROUP BY which works on any column"],
    ),
    (
        "`SELECT salesperson, sale_id, amount, SUM(amount) OVER () AS company_total FROM sales;` leaves the parentheses after OVER completely empty.\n\nWhat window does this define, and what does every row show?",
        "An empty OVER() means the window is the entire result set, with no partitioning at all, so every row shows the same company-wide total (61700.00) alongside its own individual sale amount — the simplest possible window, one big window covering everything.",
        "medium", "understand", "what-is-a-window-function",
        "The window is the entire result set with no partitioning, so every row shows the same overall company-wide total",
        ["The query fails, since OVER requires at least a PARTITION BY or ORDER BY inside it", "Each row shows its own individual amount only, with no aggregate calculation applied", "The window becomes just the current row, showing only that row's own amount as the total"],
    ),
    (
        "`SELECT salesperson, sale_id, amount, SUM(amount) OVER (PARTITION BY salesperson) AS salesperson_total FROM sales WHERE region != 'East';` filters out Tarun Bakshi's East-region row before the window function runs.\n\nWhat does this reveal about when a window function's calculation actually sees the data?",
        "The window calculation only ever sees the rows that survive filtering — Tarun's row is removed by WHERE before the window function ever runs, so it never factors into anyone's partitioned total and doesn't appear in the output at all.",
        "medium", "apply", "what-is-a-window-function",
        "The window function only computes over rows that have already survived the WHERE filter; filtered-out rows never factor into any partition's total",
        ["Window functions always compute over the entire table, ignoring any WHERE clause", "WHERE only removes rows from the display, but window totals still include filtered rows", "The window function runs before WHERE, so filtered rows are still counted once"],
    ),
    (
        "According to the \"Window functions vs. GROUP BY at a glance\" comparison, what happens to individual row detail and to the aggregate value's repetition, respectively, under a window function versus GROUP BY?",
        "Under a window function, individual row detail is preserved and the aggregate value is repeated across every row in that group; under GROUP BY, individual row detail is lost and there's only one aggregate value per group.",
        "medium", "remember", "what-is-a-window-function",
        "Window functions preserve individual row detail and repeat the aggregate on every row; GROUP BY loses row detail and produces one aggregate per group",
        ["Window functions lose row detail just like GROUP BY; only the aggregate calculation differs", "GROUP BY preserves row detail while window functions collapse rows, the reverse of the correct behavior", "Both approaches preserve row detail identically; only the column naming differs"],
    ),
]

OVER_PARTITION_ORDER_BY = [
    (
        "Leela wants each of Nikhil's sales next to his running total up to and including that sale, in date order.\n\n`SUM(amount) OVER (PARTITION BY salesperson ORDER BY sale_date)` — what does adding ORDER BY inside OVER change about the calculation?",
        "It changes the window's meaning entirely: instead of summing across all of a salesperson's rows equally, it now sums across only the rows up to and including the current one, in date order — an ordered, cumulative running total.",
        "easy", "understand", "over-partition-by-and-order-by",
        "It turns a flat per-partition total into a cumulative running total, summing only the rows up to and including the current one in date order",
        ["It has no real effect; ORDER BY inside OVER is purely cosmetic", "It reverses the partitioning, grouping by sale_date instead of salesperson", "It removes PARTITION BY's effect entirely, computing one company-wide total"],
    ),
    (
        "Nikhil's June 1 sale shows a running total of 12000.00 (its own amount), his June 5 sale shows 20500.00 (the first two combined), and his June 10 sale shows 29700.00 (all three combined).\n\nWhy does the June 1 row show exactly its own amount with nothing added?",
        "With ORDER BY inside OVER, the running total sums only the rows up to and including the current one; since June 1 is Nikhil's earliest sale, nothing came before it in the ordered partition, so the running total equals just that one sale's amount.",
        "medium", "apply", "over-partition-by-and-order-by",
        "As the earliest row in Nikhil's ordered partition, nothing precedes it, so the running total is just its own amount",
        ["It's a coincidence; the running total always starts at 12000.00 regardless of date", "June 1 is excluded from the partition, so the value shown is actually an error", "PARTITION BY resets to zero specifically on the first day of each month"],
    ),
    (
        "The query has both `ORDER BY sale_date` inside `OVER (...)` and a separate `ORDER BY salesperson, sale_date` at the very end of the query, outside OVER.\n\nWhat does each ORDER BY actually control, and what happens if the outer one is removed?",
        "The ORDER BY inside OVER controls how the running total is calculated; the separate outer ORDER BY controls the order rows appear in the final displayed result. Removing the outer ORDER BY would leave row display order effectively unspecified, even though every running total would still be computed correctly, since the two are entirely separate concerns.",
        "medium", "analyze", "over-partition-by-and-order-by",
        "The inner ORDER BY controls the calculation; the outer ORDER BY controls display order — removing the outer one leaves display order unspecified but the calculation stays correct",
        ["Both ORDER BY clauses do the exact same thing, making one of them redundant", "Removing the outer ORDER BY would break the running total calculation entirely", "The inner ORDER BY controls display order, and the outer one controls the calculation, the reverse of their actual roles"],
    ),
    (
        "`SUM(amount) OVER (PARTITION BY salesperson ORDER BY sale_date) AS running_total` and `SUM(amount) OVER (PARTITION BY salesperson) AS salesperson_total` are shown side by side in the same query.\n\nWhat's the key behavioral difference between the two, even though both partition by the same column?",
        "running_total grows row by row within each salesperson's partition (because of ORDER BY), while salesperson_total, with no ORDER BY, stays fixed at that salesperson's grand total on every one of their rows — the presence of ORDER BY is what changes what each row's window actually includes.",
        "medium", "apply", "over-partition-by-and-order-by",
        "running_total grows cumulatively row by row due to ORDER BY; salesperson_total stays fixed at the grand total on every row since it has no ORDER BY",
        ["The two produce identical values in every row, since both partition by salesperson", "salesperson_total grows cumulatively, while running_total stays fixed, the reverse of their actual behavior", "The difference only appears when PARTITION BY is removed from one of them"],
    ),
    (
        "`SUM(amount) OVER (ORDER BY sale_date) AS company_running_total` uses ORDER BY with no PARTITION BY at all.\n\nWhat does this produce, and what kind of report would need this shape?",
        "It tracks a single, company-wide running total across every sale regardless of salesperson, strictly in date order — exactly the shape a simple day-by-day revenue chart would need, where the whole company's cumulative total matters, not any one salesperson's.",
        "medium", "understand", "over-partition-by-and-order-by",
        "A single company-wide cumulative running total across all sales in date order, useful for something like a day-by-day revenue chart",
        ["It fails, since OVER requires PARTITION BY whenever ORDER BY is also present", "It produces one running total per salesperson, identical to using PARTITION BY", "It produces a flat, non-cumulative total identical to OVER() with nothing inside"],
    ),
    (
        "According to the \"OVER clause ingredients at a glance\" table, what does `OVER (PARTITION BY col1 ORDER BY col2)` produce?",
        "One window per distinct col1 value, cumulative in the order of col2 within each of those partitions — combining PARTITION BY's grouping with ORDER BY's cumulative sequencing inside each group.",
        "medium", "remember", "over-partition-by-and-order-by",
        "One window per distinct value of col1, with a cumulative calculation ordered by col2 within each of those windows",
        ["A single window covering the whole result set, ignoring both col1 and col2", "One window per distinct value of col2, cumulative in the order of col1", "The same as OVER() with nothing inside, since the two arguments cancel out"],
    ),
]

RANKING_FUNCTIONS = [
    (
        "The sales director wants a leaderboard ranking every salesperson by total sales, with ties handled sensibly.\n\nWhy can't a plain ORDER BY alone produce this leaderboard?",
        "ORDER BY can sort a result, but it cannot label each row with its rank, and it has no built-in way to decide what should happen to the rank numbers that follow a tie — a dedicated ranking function is needed for that.",
        "easy", "understand", "ranking-functions",
        "ORDER BY can sort rows but cannot assign rank numbers to them or decide how ties should be handled",
        ["ORDER BY can only sort text columns, not numeric ones like total sales", "ORDER BY requires GROUP BY to be present before it can run at all", "ORDER BY is deprecated in favor of ranking functions in modern SQL"],
    ),
    (
        "Sana Fatima and Tarun Bakshi both have 21000.00 in sales. `ROW_NUMBER() OVER (ORDER BY amount DESC)` still gives them different numbers (2 and 3).\n\nWhy does ROW_NUMBER do this despite the tie?",
        "ROW_NUMBER() assigns a strictly increasing integer to every row with no regard for ties at all, arbitrarily breaking a tie based on whatever order the database happens to process the rows in — useful for a strict, no-ties-allowed sequence, but not ideal for a leaderboard where a genuine tie should be reflected as one.",
        "medium", "understand", "ranking-functions",
        "ROW_NUMBER assigns a strictly increasing integer with no regard for ties, arbitrarily breaking them rather than reflecting them as equal",
        ["ROW_NUMBER actually gives tied rows the same number, and this describes RANK instead", "ROW_NUMBER only works correctly when there are no ties in the data at all", "The tie is broken based on alphabetical order of the salesperson's name"],
    ),
    (
        "With the same tied pair (Sana and Tarun at 21000.00), `RANK() OVER (ORDER BY amount DESC)` gives them both rank 2, and the next row, Priya Bose, gets rank 4, not rank 3.\n\nWhy does RANK skip rank 3 entirely?",
        "RANK gives tied rows the exact same rank number, then skips ahead by the number of tied rows before continuing — since two rows tied for rank 2, the next distinct rank counts them both and lands on 4, mirroring how a real sporting leaderboard usually works (two tied for second means the next person is fourth, not third).",
        "medium", "apply", "ranking-functions",
        "RANK counts both tied rows occupying rank 2, so the next distinct value skips ahead to 4, mirroring how sporting leaderboards handle ties",
        ["It's a bug; RANK should give Priya rank 3, and the lesson describes an error", "RANK skips numbers randomly, with no relationship to how many rows were tied", "RANK always skips exactly one number after any tie, regardless of how many rows tied"],
    ),
    (
        "With the same data, `DENSE_RANK() OVER (ORDER BY amount DESC)` gives Sana and Tarun both rank 2, but Priya Bose gets rank 3, not 4.\n\nWhat's the difference between RANK and DENSE_RANK's treatment of the rank sequence after a tie?",
        "DENSE_RANK also gives tied rows the same rank, but it does not skip any numbers afterward, keeping the rank sequence consecutive — it treats the tie as consuming only one rank position, not two, unlike RANK which leaves a gap.",
        "medium", "analyze", "ranking-functions",
        "DENSE_RANK keeps the rank sequence consecutive with no gaps after a tie, while RANK skips ahead by the number of tied rows",
        ["DENSE_RANK and RANK always produce identical results in every case", "DENSE_RANK skips numbers after a tie, while RANK stays consecutive, the reverse of their actual behavior", "DENSE_RANK ignores ties entirely, behaving exactly like ROW_NUMBER"],
    ),
    (
        "The lesson advises: use RANK if the count of people above someone genuinely matters, and use DENSE_RANK if only the relative tier matters.\n\nWhich scenario would favor RANK over DENSE_RANK?",
        "A scenario where the actual competitive standing matters, such as \"how many salespeople are strictly ahead of this person,\" since RANK's gaps correctly reflect that two people occupying rank 2 means the next person genuinely has two people ahead of them, information DENSE_RANK's consecutive numbering would obscure.",
        "hard", "apply", "ranking-functions",
        "A scenario where the exact count of people ranked above someone matters, since RANK's gaps preserve that count while DENSE_RANK's consecutive numbers don't",
        ["A scenario where ties should never occur in the data, since RANK requires unique values", "A scenario involving text data, since DENSE_RANK only works on numeric columns", "Both functions are always interchangeable, and the choice never actually matters"],
    ),
    (
        "The sales director wants a leaderboard using DENSE_RANK showing only salespeople ranked in the top 3 tiers, but writing `WHERE DENSE_RANK() OVER (...) <= 3` directly fails.\n\nWhy does this fail, and what's the correct approach?",
        "Window functions cannot be referenced directly in WHERE, the same restriction that applies to aggregate functions; the correct approach wraps the ranking in a CTE first, then filters the CTE's result with a plain WHERE clause on the now-ordinary rank column.",
        "medium", "understand", "ranking-functions",
        "Window functions can't be used directly in WHERE, the same restriction aggregate functions have; wrap the ranking in a CTE first, then filter that CTE's result",
        ["It fails because DENSE_RANK cannot be combined with a numeric comparison like <= 3", "It fails only because 3 should be written as '3' in quotes", "It fails because DENSE_RANK requires PARTITION BY to be present"],
    ),
]

OFFSET_LAG_LEAD = [
    (
        "`LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) AS previous_month` reaches back one row within each salesperson's partition, ordered by month.\n\nWhat does Nikhil's March row show for previous_month, and why?",
        "It shows NULL, since March is Nikhil's first row in the partition and there is no earlier row for LAG to reach — LAG returns the prior row's value, and a row with nothing before it has no prior value to return.",
        "easy", "understand", "offset-functions-lag-and-lead",
        "NULL, since there is no row before it in the partition for LAG to reach back to",
        ["0, since LAG defaults to zero when there's no prior row", "The current row's own value, repeated as a fallback", "The company-wide average, used as a default fallback value"],
    ),
    (
        "`total_amount - LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) AS change_from_last_month` computes Nikhil's April change as 3500.00 and May change as -4500.00.\n\nWhat would this same calculation have required before window functions existed?",
        "A self join matching each row to \"the row for the same salesperson, one month earlier,\" a noticeably more complex query for the same result — LAG lets the previous month's value sit directly on the same logical row, turning the calculation into a plain subtraction.",
        "medium", "analyze", "offset-functions-lag-and-lead",
        "A self join matching each row to the same salesperson's row from one month earlier, a more complex query for the same result",
        ["Nothing; this calculation was always impossible before window functions", "A recursive CTE walking back through every prior month one at a time", "A separate table specifically designed to store month-over-month differences"],
    ),
    (
        "LEAD is described as \"the mirror of LAG.\"\n\nWhat does `LEAD(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) AS next_month` show for Nikhil's March row and his final (June) row, respectively?",
        "March shows 25500.00 (April's total, reaching forward one row), while June, being his last row in the partition, shows NULL, since there's no later row for LEAD to reach forward into.",
        "medium", "apply", "offset-functions-lag-and-lead",
        "March shows April's total (25500.00), reaching forward; June shows NULL, since there's no later row to reach",
        ["March shows NULL, and June shows the earliest row's value, the reverse of LEAD's actual behavior", "Both March and June show NULL, since LEAD only works on rows in the middle of a partition", "March and June both show the same company-wide total, ignoring the partition"],
    ),
    (
        "Both LAG and LEAD accept two optional extra arguments beyond the column name.\n\nWhat does `LAG(total_amount, 2, 0)` specifically do?",
        "It reaches back two rows instead of the default one, and supplies 0 instead of NULL whenever there is no row that far back — the second argument sets the offset distance, and the third sets a fallback value for when no such row exists.",
        "medium", "understand", "offset-functions-lag-and-lead",
        "It reaches back two rows instead of one, and returns 0 (instead of NULL) whenever there's no row that far back",
        ["It reaches back zero rows and adds 2 to the current value", "It reaches back one row and multiplies the result by 2", "It reaches forward two rows, since LAG(n) always means \"n rows in the LEAD direction\""],
    ),
    (
        "Why is the fallback-value argument of LAG useful, according to the lesson, beyond simply avoiding a blank cell?",
        "It's useful when a downstream calculation needs a real number rather than a NULL to work with — a fallback like 0 lets arithmetic (like a change or growth calculation) proceed cleanly instead of the whole expression turning into NULL because one operand was missing.",
        "hard", "analyze", "offset-functions-lag-and-lead",
        "It gives downstream calculations a real number to work with instead of a NULL, which would otherwise make an arithmetic expression resolve to NULL entirely",
        ["It's useful purely for visual formatting, with no effect on any calculations", "It prevents the query from raising an error when no prior row exists", "It only matters for the very first row of the entire table, not any partition"],
    ),
    (
        "Leela wants to flag any month where a salesperson's total dropped compared to the previous month, using a \"trend\" column reading \"up\" or \"down.\"\n\nWhich expression correctly implements this using LAG and CASE?",
        "`CASE WHEN total_amount < LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) THEN 'down' ELSE 'up' END AS trend` — this correctly labels a drop as \"down\" and defaults every other case, including the first row of each partition (with nothing to compare against), to \"up\" through the ELSE branch.",
        "medium", "apply", "offset-functions-lag-and-lead",
        "CASE WHEN total_amount < LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) THEN 'down' ELSE 'up' END AS trend",
        ["CASE WHEN total_amount > LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) THEN 'down' ELSE 'up' END AS trend", "CASE WHEN LAG(total_amount) IS NULL THEN 'down' ELSE 'up' END AS trend", "CASE WHEN total_amount < LEAD(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) THEN 'down' ELSE 'up' END AS trend"],
    ),
]

RUNNING_TOTALS_WINDOW_FRAMES = [
    (
        "The earlier running-total pattern, `SUM(amount) OVER (PARTITION BY salesperson ORDER BY sale_date)`, quietly relied on a default frame Leela never had to name explicitly.\n\nWhat is that default frame, in plain terms?",
        "Everything from the very first row in the window up through and including the current row — written explicitly as RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW, this default is what makes a plain ORDER BY inside OVER produce a cumulative total in the first place.",
        "easy", "understand", "running-totals-moving-averages-and-window-frames",
        "From the very first row in the window through the current row, the default behind any cumulative running total",
        ["Only the current row by itself, with nothing before or after it included", "The entire partition regardless of row order, identical to no ORDER BY at all", "Exactly the three rows immediately surrounding the current one"],
    ),
    (
        "`SUM(total_amount) OVER (ORDER BY sale_month ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total` writes the frame explicitly instead of relying on the default.\n\nWhat does writing it out explicitly make possible that relying on the default does not?",
        "It produces an identical result to the shorthand version, but writing it explicitly is what makes it possible to change the frame to something other than the default, such as a fixed-size moving window instead of an ever-growing cumulative one.",
        "medium", "understand", "running-totals-moving-averages-and-window-frames",
        "It makes it possible to modify the frame to something other than the default, like a fixed-size moving window",
        ["It changes the result, since the explicit version produces a different total than the shorthand", "It allows the query to run without any ORDER BY clause at all", "It removes the need for PARTITION BY entirely, even in a partitioned query"],
    ),
    (
        "A 3-month moving average needs a frame of exactly the current row plus the two rows before it.\n\nWhich frame clause expresses this, and what does January's moving average show given it has no prior rows?",
        "`ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` — January's moving average is just its own value (18000.00), since only zero rows precede it; February's becomes the average of January and February (two rows); only from March onward does every row's average draw from exactly three months.",
        "medium", "apply", "running-totals-moving-averages-and-window-frames",
        "ROWS BETWEEN 2 PRECEDING AND CURRENT ROW; January shows just its own value, since no rows precede it yet",
        ["ROWS BETWEEN 3 PRECEDING AND CURRENT ROW; January shows NULL, since three rows don't yet exist", "ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING; January shows the average of January, February, and March", "ROWS BETWEEN UNBOUNDED PRECEDING AND 2 FOLLOWING; January shows the full 6-month average"],
    ),
    (
        "`ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING` is described as centering the frame on the current row.\n\nWhat does this frame include, and why might it be preferred over a backward-only frame for smoothing noisy data?",
        "It includes the current row, one row before it, and one row after it — a common way to smooth out noisy data symmetrically rather than only looking backward, since a backward-only average can lag behind sudden shifts that a centered average captures more evenly from both directions.",
        "medium", "analyze", "running-totals-moving-averages-and-window-frames",
        "It includes the current row plus one row on each side, smoothing data symmetrically rather than only looking backward",
        ["It includes only the current row, since PRECEDING and FOLLOWING cancel each other out", "It includes every row in the entire partition, identical to UNBOUNDED on both sides", "It includes the current row and the very first and very last rows of the partition only"],
    ),
    (
        "According to the \"Window frame options at a glance\" table, what does `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` mean?",
        "The entire partition, the same as no ORDER BY at all — this frame spans from the very first row to the very last row in the partition regardless of the current row's position, producing the same fixed total on every row, just like a plain PARTITION BY with no ORDER BY.",
        "medium", "remember", "running-totals-moving-averages-and-window-frames",
        "The entire partition, equivalent to having no ORDER BY at all inside OVER",
        ["Only the current row, with nothing before or after it", "From the first row to the current row, the default cumulative frame", "The current row plus exactly one row on either side"],
    ),
    (
        "Leela wants a 2-month moving total (current month plus the one before it) for Nikhil's sales.\n\nWhich frame clause correctly computes this, and what would it show for February given January is 18000.00 and February is 20000.00?",
        "`ROWS BETWEEN 1 PRECEDING AND CURRENT ROW` — February shows 38000.00, January plus February combined, since the frame includes exactly the current row and the one immediately before it.",
        "medium", "apply", "running-totals-moving-averages-and-window-frames",
        "ROWS BETWEEN 1 PRECEDING AND CURRENT ROW; February would show 38000.00 (January + February)",
        ["ROWS BETWEEN 2 PRECEDING AND CURRENT ROW; February would show 38000.00", "ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING; February would show 38000.00", "ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING; February would show 38000.00"],
    ),
]

TOPN_PER_GROUP = [
    (
        "The sales director's final request, \"show me the top 2 salespeople by revenue, within each region,\" needs both partitioned ranking and a way to filter to just the top-ranked rows.\n\nWhy can't ranking functions alone solve this, even with PARTITION BY?",
        "Ranking functions alone cannot filter, since window functions are not allowed inside WHERE, the same restriction noted when ranking functions were first introduced — the ranking has to be computed first and then filtered separately, which needs a CTE.",
        "easy", "understand", "topn-per-group",
        "Window functions like ranking functions can't be referenced directly in WHERE, so the rank has to be computed first and filtered afterward, needing a CTE",
        ["Ranking functions can't be combined with PARTITION BY at all", "Ranking functions only work when there is exactly one region in the data", "Ranking functions can filter directly, but only when used with RANK, not DENSE_RANK"],
    ),
    (
        "`RANK() OVER (PARTITION BY region ORDER BY total_amount DESC) AS region_rank` is applied across North, South, and East regions.\n\nWhat does PARTITION BY region specifically ensure about the ranking?",
        "It resets the ranking separately within each region — every region starts its own count from 1, so Nikhil Rao can rank 1st in North while Sana Fatima and Tarun Bakshi both rank 1st in South (tied), each independent of what's happening in other regions.",
        "easy", "understand", "topn-per-group",
        "The ranking restarts from 1 independently within each region, rather than ranking across the whole company at once",
        ["It ranks every salesperson across the whole company, ignoring region entirely", "It ensures every region has exactly the same number of ranked salespeople", "It sorts regions alphabetically before ranking salespeople within them"],
    ),
    (
        "Since `region_rank` can't be referenced directly in WHERE within the same query that defines it, the ranked result needs to be named with a CTE first.\n\n`WITH ranked_sales AS (SELECT ..., RANK() OVER (PARTITION BY region ORDER BY total_amount DESC) AS region_rank FROM sales) SELECT ... FROM ranked_sales WHERE region_rank <= 2;` — why does this two-step structure work when a single-step WHERE clause would not?",
        "The CTE computes the ranking exactly as before and gives it a name (ranked_sales); the outer query then treats region_rank as an ordinary column of that named result, which a plain WHERE can filter on normally, since by that point region_rank is no longer a window function call but just a regular column value.",
        "medium", "analyze", "topn-per-group",
        "The CTE turns region_rank into an ordinary column of a named result, which the outer WHERE can then filter normally, since it's no longer a live window function call",
        ["The CTE removes the need for PARTITION BY entirely, simplifying the WHERE clause", "WHERE inside a CTE behaves differently from WHERE in a normal query, allowing window functions", "The CTE runs the ranking calculation twice, once for each region, avoiding the restriction"],
    ),
    (
        "With North and South each having enough salespeople and East having only one (Kunal Verma), `WHERE region_rank <= 2` on the ranked_sales CTE returns 5 rows total, not 6.\n\nWhy does East only contribute one row to this top-2-per-region report?",
        "East only has one salesperson to begin with, so its entire \"top 2\" is just that single row — there's no second-place salesperson in East to rank and include, unlike North and South which each contribute their expected 2 rows.",
        "medium", "apply", "topn-per-group",
        "East only has one salesperson total, so there's no second row available to fill out a \"top 2\" for that region",
        ["East's data was accidentally excluded by a mistake in the WHERE clause", "region_rank <= 2 only applies to regions with more than one salesperson", "Kunal Verma's row is filtered out because he ties with someone in a different region"],
    ),
    (
        "In the South region, Sana Fatima and Tarun Bakshi are tied at rank 1 (both 21000.00), and Reema Ghosh, in third place by value, lands on rank 3 due to RANK's skip-ahead behavior after a tie.\n\nWhy is Reema correctly excluded by `WHERE region_rank <= 2`, and what would have happened if DENSE_RANK had been used instead?",
        "Reema's rank 3 (from RANK skipping ahead past the tied pair) correctly places her outside the top 2 filter. If DENSE_RANK had been used instead, the tie would only consume one rank position, and Reema would land on rank 2 instead of 3, incorrectly including her in a \"top 2\" that should really only hold the two tied leaders.",
        "hard", "analyze", "topn-per-group",
        "RANK's rank 3 for Reema correctly excludes her from the top 2; DENSE_RANK would have given her rank 2 instead, incorrectly including her alongside the tied leaders",
        ["RANK and DENSE_RANK would produce identical results here, since South only has three salespeople", "DENSE_RANK would exclude Reema even more strictly than RANK does", "The choice between RANK and DENSE_RANK has no effect on which rows survive the region_rank <= 2 filter"],
    ),
    (
        "To find the single lowest-selling salesperson in each region using RANK, the lesson flips ORDER BY total_amount DESC to `ORDER BY total_amount ASC` and filters with `WHERE region_rank = 1`.\n\nWhy does simply reversing the sort direction correctly find the lowest performer instead of the highest?",
        "Ranking always assigns rank 1 to whatever comes first in the ORDER BY sequence inside OVER; sorting ascending instead of descending means the smallest value now comes first, so rank 1 becomes the lowest seller instead of the highest, without needing any other change to the query's structure.",
        "medium", "understand", "topn-per-group",
        "Rank 1 always goes to whatever sorts first; switching to ascending order makes the smallest value sort first, so rank 1 becomes the lowest performer instead of the highest",
        ["It doesn't actually work; finding the lowest performer requires an entirely different function than RANK", "ASC forces RANK to count from the bottom up automatically, regardless of what ORDER BY value ranks 1", "Reversing to ASC changes region_rank = 1 into effectively meaning \"last place\" only by convention, not by calculation"],
    ),
]

SYNTHESIS = [
    (
        "The plain window function lesson (SUM OVER PARTITION BY) and the ranking functions lesson (RANK OVER ORDER BY) both use OVER, but one needs only PARTITION BY to answer its question while the other needs ORDER BY.\n\nWhy does a ranking function fundamentally require ORDER BY inside OVER, in a way that a flat per-group total (like a department total) does not?",
        "A rank is inherently a position within a sequence, first, second, third, so a ranking function needs to know the order to assign a position at all; a flat per-group total like SUM(amount) OVER (PARTITION BY salesperson) doesn't care about sequence, only about which rows belong together, so ORDER BY is optional for it but mandatory for meaningful ranking.",
        "medium", "analyze", "ranking-functions",
        "A rank is a position within a sequence, so ranking functions need ORDER BY to define that sequence; a flat total only needs to know which rows belong together, not their order",
        ["Both actually require ORDER BY equally; PARTITION BY alone is never sufficient for either", "Ranking functions use PARTITION BY instead of ORDER BY, the reverse of their actual requirement", "Neither function type actually requires ORDER BY under any circumstances"],
    ),
    (
        "LAG/LEAD (offset functions) and window frames (ROWS BETWEEN ... AND ...) both let a row's calculation reach beyond just itself, but they do so in structurally different ways.\n\nWhat's the key difference between what LAG/LEAD return and what a window frame's aggregate (like SUM or AVG) returns?",
        "LAG and LEAD return a single specific value from exactly one other row (a fixed number of rows back or forward), while a window frame's aggregate function computes over a whole range of rows at once (like the current row plus the two before it), collapsing that range into one summary value rather than pointing at a single neighboring row.",
        "hard", "analyze", "running-totals-moving-averages-and-window-frames",
        "LAG/LEAD return a single value from one specific neighboring row; a window frame's aggregate computes across a whole range of rows at once",
        ["LAG/LEAD and window frame aggregates both return exactly the same kind of result", "LAG/LEAD compute across a range of rows, while window frames return a single neighboring value, the reverse of their actual behavior", "Window frames can only be used with LAG and LEAD, never with SUM or AVG"],
    ),
    (
        "The top-N-per-group lesson combines PARTITION BY (from the second lesson), RANK's tie-handling (from the ranking lesson), and a CTE (needed because window functions can't sit inside WHERE, as established in the ranking lesson).\n\nWhat does this final lesson's combination reveal about how the individual pieces of this chapter build on each other?",
        "Each concept in the chapter (partitioning, ordering, ranking with specific tie behavior, and CTEs for filtering) is a reusable building block, and a genuinely useful business report, like top-N-per-group, is typically not answered by any single one of these tools alone but by combining several of them together in the right sequence.",
        "medium", "understand", "topn-per-group",
        "Each concept is a reusable building block, and real business reports typically require combining several of them together rather than relying on any single tool alone",
        ["Only the very last lesson's techniques actually matter; the earlier ones are optional background", "Top-N-per-group could be solved with RANK alone, without needing any of the earlier concepts", "The chapter's lessons are all independent and were never meant to be combined together"],
    ),
    (
        "GROUP BY collapses rows entirely (from the aggregation chapter), a window function preserves rows while adding an aggregate-style column, and a window frame further customizes exactly which neighboring rows that aggregate considers.\n\nHow does this progression, from GROUP BY, to a basic window function, to a windowed function with a custom frame, represent increasing levels of control over the same underlying idea (aggregating across related rows)?",
        "GROUP BY offers the least control, forcing one row per group with no detail preserved; a basic window function preserves every row and lets you choose which rows are related via PARTITION BY, still using a default frame; and an explicit window frame adds the finest level of control, letting you precisely define which subset of related rows, not just which whole partition, each row's calculation actually considers.",
        "hard", "analyze", "what-is-a-window-function",
        "GROUP BY offers the coarsest control (one row per group, no detail); window functions add row-preserving partition control; explicit window frames add the finest control over exactly which neighboring rows are considered",
        ["All three approaches offer exactly the same level of control, just with different syntax", "Window frames actually offer less control than plain GROUP BY, since they only work on ordered data", "GROUP BY offers the most granular control, while window functions and frames are coarser"],
    ),
]

SET1_SOURCES = [
    (WHAT_IS_A_WINDOW_FUNCTION, 0),
    (OVER_PARTITION_ORDER_BY, 0),
    (RANKING_FUNCTIONS, 0),
    (OFFSET_LAG_LEAD, 0),
    (RUNNING_TOTALS_WINDOW_FRAMES, 0),
    (TOPN_PER_GROUP, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    WHAT_IS_A_WINDOW_FUNCTION[1:]
    + OVER_PARTITION_ORDER_BY[1:]
    + RANKING_FUNCTIONS[1:]
    + OFFSET_LAG_LEAD[1:]
    + RUNNING_TOTALS_WINDOW_FRAMES[1:]
    + TOPN_PER_GROUP[1:]
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
            "topics": "advanced-querying-with-sql",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 5.2.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 5.2.2")
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
ws.title = "DBMS - MCQ - Unit 5.2"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 5 - Advanced Querying with SQL/5.2 - Window Functions - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
