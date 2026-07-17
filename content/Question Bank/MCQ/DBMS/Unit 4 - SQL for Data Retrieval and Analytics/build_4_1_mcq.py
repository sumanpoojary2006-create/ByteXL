import random
import openpyxl

random.seed(71)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

STRING_FUNCTIONS = [
    (
        "Meera's restaurants table stores branch_name and locality in separate columns, but the delivery app needs one combined display like \"Spice Route - Koramangala\".\n\nWhich query correctly builds this combined label?",
        "`SELECT CONCAT(branch_name, ' - ', locality) AS display_name FROM restaurants;` — CONCAT glues its arguments together into one string, and the literal ' - ' inserts a separator between the two column values.",
        "easy", "apply", "string-functions",
        "SELECT CONCAT(branch_name, ' - ', locality) AS display_name FROM restaurants;",
        ["SELECT branch_name + ' - ' + locality AS display_name FROM restaurants;", "SELECT MERGE(branch_name, locality) AS display_name FROM restaurants;", "SELECT branch_name, locality AS display_name FROM restaurants;"],
    ),
    (
        "\"Spice Route\" and \"SPICE ROUTE\" are meant to be the same restaurant branch, but a case-sensitive comparison would treat them as different values.\n\nWhy does applying LOWER(branch_name) before grouping or comparing solve this?",
        "LOWER forces text into one consistent case, so comparisons and grouping stop caring about how someone originally typed it — applying LOWER(branch_name) to every row means \"Spice Route\" and \"SPICE ROUTE\" collapse into a single group instead of two.",
        "medium", "understand", "string-functions",
        "LOWER forces every value into consistent case, so differently-cased versions of the same text collapse into one group",
        ["LOWER deletes any row with uppercase letters from the result", "LOWER only works on the first character of a string, not the whole value", "LOWER permanently rewrites the stored branch_name column to lowercase"],
    ),
    (
        "A space at the end of a stored email address makes `WHERE manager_email = 'ravi.kumar@spiceroute.com'` fail to match, even though the value looks identical on screen.\n\nWhich two functions does Meera use together to both fix and verify this problem?",
        "TRIM removes whitespace from both ends of a string, and LENGTH counts characters, which is how Meera confirmed the raw column had extra characters an eyeball check could not catch, by comparing raw_length against clean_length for each row.",
        "medium", "apply", "string-functions",
        "TRIM to remove the stray whitespace, and LENGTH to compare character counts before and after",
        ["UPPER to normalize the case, and CONCAT to rebuild the email from scratch", "SUBSTRING to cut off the last character, and ROUND to fix the value", "COALESCE to replace the email with a default, and ABS to measure the length"],
    ),
    (
        "Meera needs just the domain of each manager's email to check which restaurants still use the old curryleaf.com address.\n\n`SELECT manager_email, SUBSTRING(TRIM(manager_email) FROM POSITION('@' IN TRIM(manager_email)) + 1) AS domain FROM restaurants;` — what does POSITION('@' IN ...) find, and why is the result used with + 1?",
        "POSITION finds where the @ sits in the cleaned email; SUBSTRING then starts pulling characters one position after that (+1), giving back everything from the domain onward rather than including the @ symbol itself.",
        "medium", "understand", "string-functions",
        "POSITION finds where @ sits in the string; +1 tells SUBSTRING to start extracting right after the @ symbol",
        ["POSITION finds the total string length; +1 adds one extra character to the result", "POSITION counts how many @ symbols exist; +1 doubles that count", "POSITION finds the first letter of the domain; +1 has no real effect on the result"],
    ),
    (
        "Why does the lesson wrap the email argument in TRIM before applying SUBSTRING and POSITION to find the domain?",
        "A stray trailing space would otherwise show up glued onto the extracted domain, since SUBSTRING pulls everything from the @ position to the end of the string, whitespace included, unless it's trimmed first.",
        "hard", "analyze", "string-functions",
        "Without trimming first, a stray trailing space would end up glued onto the extracted domain result",
        ["TRIM is required by SQL syntax before SUBSTRING can be used at all", "TRIM converts the email to lowercase before POSITION can search it", "TRIM has no real effect here; it's included purely as a stylistic habit"],
    ),
    (
        "Head office wants a cleaned-up directory column with the trimmed, lowercase email for every restaurant, aliased as contact_email.\n\nWhich query correctly produces this?",
        "`SELECT LOWER(TRIM(manager_email)) AS contact_email FROM restaurants;` — TRIM removes stray whitespace first, and LOWER then normalizes the case, so every address reads the same clean way regardless of how it was originally typed.",
        "medium", "apply", "string-functions",
        "SELECT LOWER(TRIM(manager_email)) AS contact_email FROM restaurants;",
        ["SELECT TRIM(LOWER(manager_email)) AS contact_email FROM restaurants; -- functionally different from the correct order", "SELECT UPPER(manager_email) AS contact_email FROM restaurants;", "SELECT manager_email AS contact_email FROM restaurants WHERE manager_email = TRIM(manager_email);"],
    ),
    (
        "Meera's report joins CONCAT, UPPER/LOWER, TRIM, LENGTH, and SUBSTRING, all applied to the same five rows of raw restaurant data, without ever editing the stored table.\n\nWhat does this demonstrate about how string functions work in a SELECT list?",
        "String functions let a query reshape text as it leaves the table, joining columns together, normalizing case, stripping whitespace, and pulling out substrings, all computed fresh at query time, with the underlying stored data never modified.",
        "medium", "understand", "string-functions",
        "They reshape text at query time without ever modifying the underlying stored data in the table",
        ["They permanently rewrite the table's stored values to match their output", "Only one string function can be applied per query at a time", "String functions require a separate UPDATE statement to take effect"],
    ),
]

NUMERIC_FUNCTIONS = [
    (
        "A price of 599.995 needs to round to a clean value before it reaches a customer's price tag.\n\nWhich query correctly rounds selling_price to the nearest whole number?",
        "`SELECT product_name, selling_price, ROUND(selling_price, 0) AS rounded_price FROM products;` — the second argument to ROUND controls how many decimal places survive, so 0 rounds to the nearest whole number.",
        "easy", "apply", "numeric-functions",
        "SELECT product_name, selling_price, ROUND(selling_price, 0) AS rounded_price FROM products;",
        ["SELECT product_name, selling_price, ROUND(selling_price) AS rounded_price FROM products WHERE selling_price = 0;", "SELECT product_name, TRUNCATE(selling_price) AS rounded_price FROM products;", "SELECT product_name, selling_price / 1 AS rounded_price FROM products;"],
    ),
    (
        "Arjun is calculating how many boxes are needed to ship a fractional number of kilograms; rounding down would leave stock behind, so he needs to always round up.\n\nWhich function guarantees that even a small fraction like 0.145 kg rounds up to 1, ensuring enough capacity?",
        "CEIL (short for ceiling) always rounds up to the next whole number, so 0.145 becomes 1 — the opposite of FLOOR, which always rounds down and would leave a partial kilogram uncounted.",
        "easy", "understand", "numeric-functions",
        "CEIL",
        ["FLOOR", "ROUND", "ABS"],
    ),
    (
        "Arjun wants to know which product IDs would divide evenly into groups of 6 (a remainder of 0) versus which would not, using `product_id % 6 AS remainder_when_packed_in_sixes`.\n\nWhat does the % operator return here?",
        "The % operator, also written as MOD(a, b) in some databases, returns the remainder of a division — here showing which product IDs pack evenly into groups of 6 (remainder 0) versus which don't (any other remainder).",
        "medium", "understand", "numeric-functions",
        "The remainder left over after dividing product_id by 6",
        ["The number of times 6 divides evenly into product_id", "The result of product_id divided by 6, rounded to the nearest whole number", "A boolean flag indicating whether product_id is a multiple of 6"],
    ),
    (
        "The webcam row has a selling_price of -1249.0000, a data-entry mistake. Arjun wants to see how far off each negative price is from zero.\n\nWhich function and query correctly computes this?",
        "`SELECT product_name, selling_price, ABS(selling_price) AS positive_price FROM products WHERE selling_price < 0;` — ABS strips the sign off a number, turning -1249.0000 into 1249.0000, its distance from zero regardless of sign.",
        "medium", "apply", "numeric-functions",
        "SELECT product_name, selling_price, ABS(selling_price) AS positive_price FROM products WHERE selling_price < 0;",
        ["SELECT product_name, selling_price, ROUND(selling_price) AS positive_price FROM products WHERE selling_price < 0;", "SELECT product_name, selling_price, -selling_price AS positive_price FROM products WHERE selling_price > 0;", "SELECT product_name, CEIL(selling_price) AS positive_price FROM products WHERE selling_price < 0;"],
    ),
    (
        "What does ROUND(599.995, 2) evaluate to, and what does the second argument specifically control?",
        "It evaluates to 600.00; the second argument controls how many decimal places survive the rounding, so a currency needing two decimal places (cents) uses 2 rather than 0.",
        "medium", "apply", "numeric-functions",
        "600.00, where the 2 specifies how many decimal places to keep",
        ["599.99, where the 2 specifies how many digits to truncate", "600, where the 2 specifies how many times to round", "599.995, since ROUND with a second argument has no effect on this value"],
    ),
    (
        "Arjun needs a margin report showing product_name and the profit margin (selling_price - cost_price) rounded to two decimal places, aliased as margin.\n\nWhich query correctly does this?",
        "`SELECT product_name, ROUND(selling_price - cost_price, 2) AS margin FROM products;` — the arithmetic runs first, and ROUND then cleans the result to two decimal places; the webcam row would show a large negative margin, confirming its price needs a manual fix.",
        "medium", "apply", "numeric-functions",
        "SELECT product_name, ROUND(selling_price - cost_price, 2) AS margin FROM products;",
        ["SELECT product_name, ROUND(selling_price, 2) - ROUND(cost_price, 2) AS margin FROM products; -- not the pattern shown in the lesson", "SELECT product_name, selling_price - ROUND(cost_price, 2) AS margin FROM products;", "SELECT product_name, ABS(selling_price - cost_price) AS margin FROM products;"],
    ),
    (
        "CEIL(0.145) returns 1, and FLOOR(1.3) returns 1, even though the two functions do opposite things.\n\nWhy do both calls produce the same result of 1 here, despite CEIL rounding up and FLOOR rounding down?",
        "CEIL(0.145) rounds up from a value between 0 and 1, landing on 1, while FLOOR(1.3) rounds down from a value between 1 and 2, also landing on 1 — it's coincidental that both source values happen to round toward the same whole number from opposite directions.",
        "hard", "analyze", "numeric-functions",
        "CEIL rounds 0.145 up to 1, while FLOOR rounds 1.3 down to 1 — the two source values happen to round toward the same result from opposite directions",
        ["CEIL and FLOOR are actually the same function under different names", "Both functions always return exactly 1 regardless of their input", "The results only match because both inputs were originally negative numbers"],
    ),
]

DATE_TIME_FUNCTIONS = [
    (
        "Every date calculation Divya needs eventually requires knowing what \"now\" is.\n\nWhat's the difference between NOW() and CURRENT_DATE?",
        "NOW() returns the exact current timestamp the database sees at query time, down to the second, while CURRENT_DATE returns just today's date with no time component at all.",
        "easy", "remember", "date-and-time-functions",
        "NOW() returns the full current timestamp including time; CURRENT_DATE returns just today's date with no time",
        ["NOW() returns just the date; CURRENT_DATE returns the full timestamp including time", "NOW() and CURRENT_DATE are identical and interchangeable in every case", "NOW() only works on TIMESTAMP columns; CURRENT_DATE only works on DATE columns"],
    ),
    (
        "`SELECT patient_name, visit_time, AGE(NOW(), visit_time) AS time_since_visit, visit_time + INTERVAL '7 days' AS suggested_followup FROM appointments;`\n\nWhat do AGE and the INTERVAL addition each produce?",
        "AGE(later, earlier) returns a readable span, like \"11 months 2 days,\" friendlier for a doctor to scan than raw seconds. Adding an INTERVAL directly to a timestamp produces a new timestamp shifted forward by exactly that span, generating a suggested follow-up date.",
        "medium", "understand", "date-and-time-functions",
        "AGE produces a readable time span between two timestamps; adding INTERVAL shifts a timestamp forward by a fixed amount",
        ["AGE produces a timestamp shifted forward; INTERVAL produces a readable span between two dates", "Both AGE and INTERVAL addition return the exact same kind of value", "AGE only works on dates, never timestamps, unlike INTERVAL addition"],
    ),
    (
        "Divya wants to know which weekday and which hour patients tend to book, without caring about the specific date at all.\n\nWhich function pulls a single component like the hour or day-of-week out of a full timestamp?",
        "EXTRACT(field FROM timestamp) pulls a single component out of a date or timestamp — EXTRACT(DOW FROM visit_time) returns the day of week (0 for Sunday through 6 for Saturday), and EXTRACT(HOUR FROM visit_time) returns the hour in 24-hour format.",
        "easy", "remember", "date-and-time-functions",
        "EXTRACT(field FROM timestamp)",
        ["SPLIT(timestamp, field)", "PART(field, timestamp)", "SLICE(timestamp FOR field)"],
    ),
    (
        "`SELECT patient_name, visit_time, CURRENT_DATE - visit_time::DATE AS days_since_visit FROM appointments ORDER BY days_since_visit;`\n\nWhy does the query cast visit_time to ::DATE before subtracting, rather than subtracting the full timestamp directly?",
        "visit_time::DATE converts the timestamp to a plain date first, dropping the time-of-day portion, so the subtraction returns a clean whole number of days rather than a mixed interval that includes hours and minutes.",
        "medium", "analyze", "date-and-time-functions",
        "Casting to ::DATE drops the time-of-day portion, so the subtraction returns a clean whole number of days",
        ["The cast is required syntax and has no effect on the result's shape", "Casting to ::DATE converts the value into a readable AGE-style span instead of a number", "Without the cast, the subtraction would raise an error and fail to run at all"],
    ),
    (
        "According to the EXTRACT fields table, what would `EXTRACT(DOW FROM visit_time)` return for a timestamp of 2025-03-18 10:00:00, and what does DOW stand for?",
        "DOW stands for day of week, returning 0 for Sunday through 6 for Saturday; for 2025-03-18 (a Tuesday), it returns 2.",
        "medium", "apply", "date-and-time-functions",
        "2, since DOW means day of week (0=Sunday through 6=Saturday) and March 18, 2025 is a Tuesday",
        ["18, since DOW returns the day of the month", "3, since DOW returns the month number", "10, since DOW returns the hour of the timestamp"],
    ),
    (
        "The clinic wants a recall list: patient name and visit date for every appointment more than 60 days old, counting from today, ordered with the oldest visit first.\n\nWhich query correctly produces this?",
        "`SELECT patient_name, visit_time FROM appointments WHERE CURRENT_DATE - visit_time::DATE > 60 ORDER BY visit_time;` — the WHERE clause filters to appointments more than 60 days old, and ordering by visit_time ascending puts the earliest (oldest) visits first.",
        "medium", "apply", "date-and-time-functions",
        "SELECT patient_name, visit_time FROM appointments WHERE CURRENT_DATE - visit_time::DATE > 60 ORDER BY visit_time;",
        ["SELECT patient_name, visit_time FROM appointments WHERE CURRENT_DATE - visit_time::DATE > 60 ORDER BY visit_time DESC;", "SELECT patient_name, visit_time FROM appointments WHERE visit_time > CURRENT_DATE - 60 ORDER BY visit_time DESC;", "SELECT patient_name, visit_time FROM appointments HAVING CURRENT_DATE - visit_time::DATE > 60;"],
    ),
    (
        "Divya answers four different scheduling questions, current moment, arithmetic, extraction, and comparison, all from one column of raw timestamps stored in the appointments table.\n\nWhat does this demonstrate about how a single stored timestamp value can be used?",
        "A single stored value can be pulled apart, compared, or measured against \"right now\" in many different ways at query time, since date and time functions compute all of this fresh from the one raw column rather than requiring separate stored fields for each derived fact.",
        "hard", "analyze", "date-and-time-functions",
        "A single stored timestamp can be reshaped into many different derived answers at query time, without needing separate stored columns for each",
        ["Each different question actually requires its own separate stored column in the table", "Timestamps can only answer one kind of question per table, requiring multiple tables", "NOW() must be stored in the table before any date function can be applied"],
    ),
]

NULL_HANDLING_FUNCTIONS = [
    (
        "Vikram wants the directory to show a phone number for every employee: fall back to the primary number if secondary is missing, and fall back to a placeholder if both are missing.\n\nWhich function and query correctly implements this fallback chain?",
        "`SELECT full_name, COALESCE(secondary_phone, primary_phone, 'Not on file') AS contact_number FROM employees;` — COALESCE scans its arguments left to right and returns the first one that is not NULL.",
        "easy", "apply", "null-handling-functions",
        "SELECT full_name, COALESCE(secondary_phone, primary_phone, 'Not on file') AS contact_number FROM employees;",
        ["SELECT full_name, NULLIF(secondary_phone, primary_phone) AS contact_number FROM employees;", "SELECT full_name, secondary_phone OR primary_phone OR 'Not on file' AS contact_number FROM employees;", "SELECT full_name, IFNULL(secondary_phone) AS contact_number FROM employees;"],
    ),
    (
        "For Ayesha Khan, both secondary_phone and primary_phone are NULL.\n\nWhat does COALESCE(secondary_phone, primary_phone, 'Not on file') return for her row?",
        "It returns 'Not on file' — COALESCE falls all the way through to the third argument since both of the first two are NULL, exactly the standard pattern for showing a sensible default instead of a blank space.",
        "medium", "apply", "null-handling-functions",
        "'Not on file'",
        ["NULL, since COALESCE cannot resolve when all arguments are missing", "An empty string, not the literal text 'Not on file'", "0, since COALESCE defaults to zero when every argument is NULL"],
    ),
    (
        "Manoj's row has an odd duplication: his primary_phone and secondary_phone are identical, because someone copied the primary number into the secondary field by mistake.\n\nWhich function treats a secondary number that exactly matches the primary as if it were not really provided at all?",
        "NULLIF(a, b) compares its two arguments, and if they are equal, it returns NULL; otherwise it returns a unchanged — for Manoj, since secondary_phone equals primary_phone, the result is NULL instead of a duplicate number.",
        "medium", "understand", "null-handling-functions",
        "NULLIF(secondary_phone, primary_phone)",
        ["COALESCE(secondary_phone, primary_phone)", "CASE secondary_phone WHEN primary_phone THEN NULL END -- valid logic but not the function used", "ABS(secondary_phone - primary_phone)"],
    ),
    (
        "`SELECT full_name, COALESCE(NULLIF(secondary_phone, primary_phone), primary_phone, 'Not on file') AS best_contact_number FROM employees;`\n\nReading from the inside out, what happens for Manoj's row specifically?",
        "NULLIF first turns Manoj's duplicated secondary number into NULL (since it equals primary_phone), then COALESCE steps in and falls back to his primary_phone, since the secondary is now effectively missing.",
        "medium", "analyze", "null-handling-functions",
        "NULLIF turns his duplicated secondary phone into NULL, then COALESCE falls back to his primary_phone",
        ["COALESCE runs first and returns his secondary_phone unchanged, ignoring NULLIF entirely", "NULLIF deletes his row from the result entirely, since the two values match", "Both functions cancel out, and the result is always his employee_id instead"],
    ),
    (
        "For every employee other than Manoj, whose secondary_phone and primary_phone genuinely differ, how does `COALESCE(NULLIF(secondary_phone, primary_phone), primary_phone, 'Not on file')` resolve?",
        "It resolves the same way it did before combining the two functions, since NULLIF only changes behavior when the two compared values are identical — for everyone else, NULLIF passes secondary_phone through unchanged, and COALESCE uses that as its first non-NULL value.",
        "medium", "understand", "null-handling-functions",
        "The same as before combining them, since NULLIF only changes behavior when the two compared values are identical",
        ["It always falls through to the literal 'Not on file' regardless of the actual values", "It always falls back to primary_phone, ignoring secondary_phone entirely", "It raises an error, since NULLIF requires the two values to be identical"],
    ),
    (
        "The company org chart needs a \"reports to\" column: show employee_id as the reporting line if manager_id is missing, otherwise show manager_id, aliased as reports_to.\n\nWhich query correctly does this, and what would it show for Neha (who has no manager)?",
        "`SELECT full_name, COALESCE(manager_id, employee_id) AS reports_to FROM employees;` — for Neha, manager_id is NULL, so COALESCE falls back to her own employee_id, correctly marking her as the top of the chart with nobody above her.",
        "medium", "apply", "null-handling-functions",
        "SELECT full_name, COALESCE(manager_id, employee_id) AS reports_to FROM employees; — shows Neha's own employee_id",
        ["SELECT full_name, NULLIF(manager_id, employee_id) AS reports_to FROM employees; — shows NULL for Neha", "SELECT full_name, COALESCE(employee_id, manager_id) AS reports_to FROM employees; — shows Neha's own employee_id", "SELECT full_name, manager_id AS reports_to FROM employees WHERE manager_id IS NOT NULL; — omits Neha's row entirely"],
    ),
    (
        "Why does the lesson describe COALESCE and NULLIF as solving \"a large, recurring problem\" with real data, rather than a narrow, one-off issue?",
        "Real data has gaps everywhere, and a query that ignores those gaps produces blank cells, broken math, or misleading duplicates; COALESCE fills a missing value with a fallback, and NULLIF turns an unwanted match into a NULL that COALESCE can then catch, a combination that generalizes to any table with optional or accidentally-duplicated fields.",
        "hard", "analyze", "null-handling-functions",
        "Real data commonly has gaps and accidental duplicates everywhere, and this pair of functions generalizes to handling both problems in any table",
        ["The problem is narrow and only ever applies to phone number columns specifically", "COALESCE and NULLIF only work correctly on the employees table used in this lesson", "Real data never actually contains NULL values; this is a purely theoretical concern"],
    ),
]

CONDITIONAL_LOGIC = [
    (
        "The front desk wants members labeled \"Highly Active,\" \"Active,\" or \"At Risk\" based on visits_this_month, a label that doesn't exist in the table.\n\n`CASE WHEN visits_this_month >= 12 THEN 'Highly Active' WHEN visits_this_month >= 4 THEN 'Active' ELSE 'At Risk' END` — how does CASE decide which branch to use for a given row?",
        "CASE checks each WHEN condition in order, top to bottom, and returns the value after the first THEN whose condition is true; if none match, it falls back to whatever follows ELSE.",
        "easy", "understand", "conditional-logic",
        "It checks WHEN conditions top to bottom and returns the value for the first one that's true, falling back to ELSE if none match",
        ["It checks all WHEN conditions and returns the value for the last one that's true", "It randomly selects one matching WHEN condition among all that are true", "It evaluates every WHEN condition and combines all matching results into one value"],
    ),
    (
        "Karan has 18 visits. Using `CASE WHEN visits_this_month >= 12 THEN 'Highly Active' WHEN visits_this_month >= 4 THEN 'Active' ELSE 'At Risk' END`, what label does he get, and why?",
        "\"Highly Active\" — his 18 visits satisfy the first condition (>= 12), and since CASE stops at the first true condition, it never even checks the second WHEN.",
        "easy", "apply", "conditional-logic",
        "\"Highly Active\", since 18 satisfies the first WHEN condition (>= 12) and CASE stops there",
        ["\"Active\", since 18 is also >= 4, and CASE always picks the more general match", "\"At Risk\", since 18 doesn't exactly equal either threshold", "Both \"Highly Active\" and \"Active\", since CASE returns every matching branch"],
    ),
    (
        "If the conditions are reordered to `CASE WHEN visits_this_month >= 4 THEN 'Active' WHEN visits_this_month >= 12 THEN 'Highly Active' ELSE 'At Risk' END`, what label does Karan (18 visits) get now, and why does this happen?",
        "\"Active\" instead of \"Highly Active\" — visits_this_month >= 4 is checked first and is already true at 18 visits, so CASE stops right there and never reaches the \"Highly Active\" condition, exactly why the most specific or restrictive condition must come first.",
        "medium", "analyze", "conditional-logic",
        "\"Active\", because the looser >= 4 condition is checked first and matches before CASE ever reaches the stricter >= 12 condition",
        ["\"Highly Active\", since CASE always finds the most accurate matching condition regardless of order", "An error, since CASE requires conditions to be written from loosest to strictest", "\"At Risk\", since reordering the conditions breaks the ELSE branch"],
    ),
    (
        "`CASE membership_type WHEN 'premium' THEN 'Full access, all branches' WHEN 'standard' THEN ... ELSE 'Unknown plan' END` uses a shorter form than `CASE WHEN condition THEN ...`.\n\nWhen is this shorter form appropriate to use?",
        "Use the shorter form when every branch is a simple equality check against the same column, comparing membership_type directly against each listed value; fall back to the full CASE WHEN condition THEN form whenever a condition is more than a plain equality.",
        "medium", "understand", "conditional-logic",
        "When every branch is a simple equality check against the same column",
        ["Only when there are exactly three WHEN branches in the expression", "Only when the column being checked is numeric, never text", "The two forms are functionally identical and interchangeable in every situation, with no distinction"],
    ),
    (
        "`SELECT full_name, visits_this_month * CASE membership_type WHEN 'premium' THEN 10 WHEN 'standard' THEN 5 ELSE 2 END AS loyalty_points FROM members;`\n\nWhat does this demonstrate about where a CASE expression can be used?",
        "CASE expressions can be used anywhere a normal value is allowed, including inside arithmetic — here it resolves to a plain number (10, 5, or 2) for each row, which is then multiplied directly by visits_this_month, producing loyalty points in a single pass with no second query needed.",
        "medium", "apply", "conditional-logic",
        "CASE can be used inside arithmetic expressions, resolving to a plain value that participates directly in the calculation",
        ["CASE can only be used as a standalone column, never combined with arithmetic", "CASE must always be wrapped in a separate subquery before it can be multiplied", "This query is invalid, since CASE cannot appear inside a multiplication"],
    ),
    (
        "The gym wants a discount eligibility flag: members with fewer than 5 visits get \"Send Offer,\" everyone else gets \"No Offer Needed,\" aliased as offer_status.\n\nWhich query correctly implements this?",
        "`CASE WHEN visits_this_month < 5 THEN 'Send Offer' ELSE 'No Offer Needed' END AS offer_status` — only Nisha (4 visits) and Ritu (0 visits) would be flagged for an offer, matching their visit counts below the threshold.",
        "medium", "apply", "conditional-logic",
        "SELECT full_name, CASE WHEN visits_this_month < 5 THEN 'Send Offer' ELSE 'No Offer Needed' END AS offer_status FROM members;",
        ["SELECT full_name, CASE WHEN visits_this_month >= 5 THEN 'Send Offer' ELSE 'No Offer Needed' END AS offer_status FROM members;", "SELECT full_name, CASE visits_this_month WHEN < 5 THEN 'Send Offer' END AS offer_status FROM members;", "SELECT full_name, IF(visits_this_month < 5, 'Send Offer') AS offer_status FROM members;"],
    ),
    (
        "Farah uses CASE to label activity levels, describe membership plans in plain language, and calculate loyalty points, all from just two columns of raw data (visits_this_month and membership_type).\n\nWhat does this reveal about what CASE fundamentally provides to a query?",
        "CASE turns a raw column value into whatever label, category, or calculated result a business question actually needs, checking conditions in order and returning the first match, with ELSE as a safety net — letting several different business rules be expressed from the same small set of stored columns.",
        "hard", "analyze", "conditional-logic",
        "It lets several different business rules be expressed from the same stored columns, without needing extra columns or separate queries",
        ["It requires a new column to be added to the table for every new label needed", "It can only be used once per query, requiring separate queries for each label", "CASE only works on numeric columns, never on text columns like membership_type"],
    ),
]

SYNTHESIS = [
    (
        "Meera's string functions and Vikram's NULL-handling functions both reshape a column's displayed value without altering the underlying stored data.\n\nWhat's the key difference in what problem each category of function actually solves?",
        "String functions (CONCAT, TRIM, UPPER/LOWER, SUBSTRING) reshape the format or structure of a text value that's already present. NULL-handling functions (COALESCE, NULLIF) address the case where a value might be entirely absent, substituting a fallback or converting an unwanted duplicate into a genuine absence.",
        "medium", "analyze", "null-handling-functions",
        "String functions reshape text that already exists; NULL-handling functions address values that might be entirely absent",
        ["Both categories solve exactly the same problem: converting text to numbers", "String functions handle missing values; NULL-handling functions reshape text formatting", "There's no real difference; both categories are simply different names for the same functions"],
    ),
    (
        "Arjun's `ABS(selling_price)` and Divya's `visit_time::DATE` both transform a raw stored value into a cleaner form for a specific purpose (flagging a bad price, computing whole days).\n\nWhat do both of these transformations have in common with the CASE expression used for gym activity labels?",
        "All three take a raw column value and derive a new, more useful representation from it purely at query time, whether that's a magnitude, a simplified date, or a business-rule label, without requiring any change to how the value is actually stored in the table.",
        "medium", "analyze", "conditional-logic",
        "All three derive a new, more useful representation from a raw column purely at query time, with no change to stored data",
        ["All three permanently rewrite the underlying table's stored values", "Only CASE computes a new value; ABS and the date cast simply display the stored value unchanged", "ABS, the date cast, and CASE all require a separate UPDATE statement to take effect"],
    ),
    (
        "The margin report (`ROUND(selling_price - cost_price, 2)`) combines arithmetic with a numeric function, and the loyalty points calculation (`visits_this_month * CASE ... END`) combines arithmetic with a conditional expression.\n\nWhat does this pairing across two different lessons reveal about how SQL functions and expressions compose?",
        "Functions like ROUND and expressions like CASE aren't limited to standing alone in a SELECT list; they can be embedded directly inside arithmetic, letting a single column value pass through a calculation and a transformation together in one expression, without a second query or temporary table.",
        "hard", "analyze", "numeric-functions",
        "Functions and expressions like CASE can be embedded directly inside arithmetic, combining calculation and transformation in a single expression",
        ["ROUND and CASE can never be combined with arithmetic operators in the same query", "Combining a function with arithmetic always requires a separate temporary table first", "ROUND only works on the result of a CASE expression, never on raw arithmetic"],
    ),
    (
        "Meera's SUBSTRING/POSITION domain extraction and Divya's EXTRACT(HOUR FROM visit_time) both pull out a smaller, specific piece from a larger stored value (an email string, a timestamp).\n\nWhat's the key structural difference between how each one locates the piece it extracts?",
        "SUBSTRING with POSITION requires manually finding a marker character (the @ symbol) within a general-purpose text string before extracting relative to it. EXTRACT works directly on a structured date/time type, pulling out a named, pre-defined component (like HOUR or DOW) without needing to search for any marker at all.",
        "hard", "analyze", "date-and-time-functions",
        "SUBSTRING with POSITION searches for a marker character in unstructured text; EXTRACT pulls a named component directly from a structured date/time type",
        ["Both functions work identically, searching for a marker character before extracting", "EXTRACT requires POSITION internally, while SUBSTRING does not", "SUBSTRING only works on numbers, while EXTRACT only works on text"],
    ),
    (
        "Head office's cleaned contact_email query nests TRIM inside LOWER, and Vikram's best_contact_number query nests NULLIF inside COALESCE.\n\nWhat common pattern do both of these nested function calls illustrate?",
        "Both illustrate that SQL functions can be composed, with the result of an inner function feeding directly into an outer function as its argument, letting two separate cleanup or fallback steps run in sequence within a single expression, read from the inside out.",
        "medium", "understand", "string-functions",
        "Functions can be composed, with an inner function's result feeding directly into an outer function, read from the inside out",
        ["Nesting functions is invalid SQL syntax and both examples actually use separate statements", "Only NULLIF and TRIM can ever be nested; other function pairs cannot be combined", "Nesting always reverses the order functions are meant to be read in"],
    ),
]

SET1_SOURCES = [
    (STRING_FUNCTIONS, 0),
    (NUMERIC_FUNCTIONS, 0),
    (DATE_TIME_FUNCTIONS, 0),
    (NULL_HANDLING_FUNCTIONS, 0),
    (CONDITIONAL_LOGIC, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    STRING_FUNCTIONS[1:]
    + NUMERIC_FUNCTIONS[1:]
    + DATE_TIME_FUNCTIONS[1:]
    + NULL_HANDLING_FUNCTIONS[1:]
    + CONDITIONAL_LOGIC[1:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 4.1.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 4.1.2")
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
ws.title = "DBMS - MCQ - Unit 4.1"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 4 - SQL for Data Retrieval and Analytics/4.1 - Transforming Data - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
