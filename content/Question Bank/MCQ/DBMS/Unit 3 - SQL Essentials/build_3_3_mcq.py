import random
import openpyxl

random.seed(61)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

WHERE_CLAUSE = [
    (
        "Omkar runs `SELECT title, department, credits FROM courses;` and has to scroll past mathematics and economics rows to find the Computer Science courses his advisor asked about.\n\nWhich query correctly returns only the Computer Science courses?",
        "`SELECT title, department, credits FROM courses WHERE department = 'Computer Science';` tests the condition against every row, keeping only the two rows where it holds true and dropping the rest before the result reaches Omkar's screen.",
        "easy", "apply", "the-where-clause",
        "SELECT title, department, credits FROM courses WHERE department = 'Computer Science';",
        ["SELECT title, department, credits FROM courses IF department = 'Computer Science';", "SELECT title, department, credits FROM courses HAVING department = 'Computer Science';", "SELECT title, department, credits WHERE courses.department = 'Computer Science';"],
    ),
    (
        "A SELECT without a WHERE clause and the same SELECT with `WHERE department = 'Computer Science'` are run against the same courses table.\n\nWhat's the fundamental difference in what each one does?",
        "Without WHERE, every row a table has is returned. Add WHERE, and the database tests each row against the condition, keeping only the rows where it's true and discarding the rest before the result is ever produced.",
        "easy", "understand", "the-where-clause",
        "Without WHERE, every row is returned; with WHERE, only rows passing the condition are kept",
        ["Both return exactly the same rows; WHERE only changes column order", "WHERE deletes non-matching rows permanently from the table", "Without WHERE, the query fails with an error and returns nothing"],
    ),
    (
        "`SELECT full_name, city FROM students WHERE city = 'Chennai' ORDER BY full_name;` correctly returns Chennai students sorted alphabetically.\n\nWhy must WHERE appear before ORDER BY in the query text, rather than after?",
        "The clause order in SQL matches the sequence in which these decisions actually get made: first decide which table to read, then decide which rows survive (WHERE), and only after that decide how to sort or trim what's left (ORDER BY). Writing ORDER BY before WHERE is not valid SQL.",
        "medium", "understand", "the-where-clause",
        "SQL clause order reflects the actual decision sequence: filter rows first with WHERE, then sort what's left with ORDER BY",
        ["It's purely a stylistic convention with no effect on validity or correctness", "ORDER BY must always come first because sorting is more important than filtering", "WHERE and ORDER BY can be written in either order interchangeably"],
    ),
    (
        "The lesson lists SELECT, FROM, WHERE, ORDER BY, and LIMIT as clauses with a fixed relative order.\n\nWhich statement correctly places WHERE relative to the others?",
        "WHERE comes right after FROM and before ORDER BY or LIMIT: FROM names the table to read, WHERE is the filtering step itself, and ORDER BY and LIMIT act only on the rows WHERE has already let through.",
        "medium", "remember", "the-where-clause",
        "WHERE comes after FROM and before ORDER BY or LIMIT",
        ["WHERE comes after ORDER BY and before LIMIT", "WHERE comes before FROM, since it decides what to read first", "WHERE comes after LIMIT, since it filters the already-trimmed result"],
    ),
    (
        "`department = 'Computer Science'` and `city = 'Chennai'` are both described as \"equality checks, the simplest kind of condition WHERE can hold.\"\n\nWhat does the lesson say WHERE accepts beyond simple equality?",
        "WHERE can compare numbers and dates, combine several conditions together, match partial text patterns, and handle missing values — every one of these is really the same underlying idea: a test a row either passes or fails.",
        "medium", "understand", "the-where-clause",
        "Comparisons on numbers and dates, combined conditions, partial text pattern matching, and handling missing values",
        ["WHERE only ever accepts equality checks; nothing else is possible", "WHERE can only filter text columns, never numbers or dates", "WHERE can combine conditions but cannot match partial text at all"],
    ),
    (
        "Which query correctly returns the full_name and city of every student based in Bengaluru?",
        "`SELECT full_name, city FROM students WHERE city = 'Bengaluru';` tests the equality condition against every row and keeps only the ones where city genuinely equals 'Bengaluru'.",
        "easy", "apply", "the-where-clause",
        "SELECT full_name, city FROM students WHERE city = 'Bengaluru';",
        ["SELECT full_name, city FROM students WHERE city LIKE Bengaluru;", "SELECT full_name, city WHERE students.city = 'Bengaluru';", "SELECT full_name, city FROM students SET city = 'Bengaluru';"],
    ),
    (
        "Omkar's advisor never sees the mathematics and economics rows once WHERE department = 'Computer Science' is applied.\n\nAt what point are the non-matching rows actually removed from consideration?",
        "The database tests each row against the condition and drops the non-matching ones before the result ever reaches the screen — filtering happens as part of running the query itself, not as a separate manual step afterward.",
        "medium", "understand", "the-where-clause",
        "Before the result is ever returned, as part of the database evaluating the WHERE condition against each row",
        ["After the full result is displayed, by manually scrolling past them", "Only after the query is saved and re-run a second time", "The rows are never actually removed; they are just hidden visually"],
    ),
]

COMPARISON_OPERATORS = [
    (
        "Neha wants courses that cost more than the standard three-credit load, not exactly four credits.\n\nWhich query correctly returns Database Systems and Data Structures (both 4 credits), while excluding the two 3-credit Mathematics courses?",
        "`SELECT title, credits FROM courses WHERE credits > 3;` uses the greater-than operator, which excludes courses at exactly 3 credits, unlike `>= 3` which would include them.",
        "easy", "apply", "comparison-operators",
        "SELECT title, credits FROM courses WHERE credits > 3;",
        ["SELECT title, credits FROM courses WHERE credits >= 3;", "SELECT title, credits FROM courses WHERE credits = 4;", "SELECT title, credits FROM courses WHERE credits > 4;"],
    ),
    (
        "If Neha had written `WHERE credits >= 3` instead of `WHERE credits > 3`, what would change in the result against the courses table (two courses at 4 credits, two at 3 credits, one at 2 credits)?",
        "The two 3-credit Mathematics courses (Linear Algebra and Discrete Mathematics) would now qualify alongside the two 4-credit Computer Science courses, since >= 3 includes values exactly equal to 3, unlike the strict > 3 which excludes them.",
        "medium", "analyze", "comparison-operators",
        "The two 3-credit Mathematics courses would now be included alongside the two 4-credit courses",
        ["Nothing would change; > 3 and >= 3 always return identical results", "Only the 2-credit Economics course would be added to the result", "The result would become empty, since >= is invalid on integer columns"],
    ),
    (
        "The lesson notes that \"dates compare exactly the way numbers do: earlier dates are 'smaller' than later ones.\"\n\nWhich query correctly finds enrollments recorded before February 4th, 2025?",
        "`SELECT enrollment_id, student_id, course_id, enrolled_on FROM enrollments WHERE enrolled_on < '2025-02-04';` uses < the same way it would on numbers, since earlier dates sort as smaller values.",
        "medium", "apply", "comparison-operators",
        "SELECT enrollment_id, student_id, course_id, enrolled_on FROM enrollments WHERE enrolled_on < '2025-02-04';",
        ["SELECT enrollment_id, student_id, course_id, enrolled_on FROM enrollments WHERE enrolled_on > '2025-02-04';", "SELECT enrollment_id, student_id, course_id, enrolled_on FROM enrollments WHERE enrolled_on BEFORE '2025-02-04';", "SELECT enrollment_id, student_id, course_id, enrolled_on FROM enrollments WHERE enrolled_on = '< 2025-02-04';"],
    ),
    (
        "`SELECT title, department FROM courses WHERE department <> 'Mathematics';` is run against the five-course table.\n\nWhich courses come back, and which are excluded?",
        "Every course except Linear Algebra and Discrete Mathematics comes back, since those are the only two rows where the condition department <> 'Mathematics' (not equal to) is false.",
        "medium", "understand", "comparison-operators",
        "Every course except the two Mathematics courses (Linear Algebra and Discrete Mathematics) comes back",
        ["Only the two Mathematics courses come back", "No courses come back, since <> is invalid SQL syntax", "Every course comes back, since <> has no filtering effect"],
    ),
    (
        "`SELECT full_name FROM students WHERE full_name >= 'M' ORDER BY full_name;` is run, and Ishita Menon is left out of the result even though her name starts with a letter before the end of the alphabet.\n\nWhy is she excluded?",
        "Text comparison works character by character in alphabetical order, and 'Ishita Menon' sorts before 'M' alphabetically (I comes before M), so it fails the >= 'M' condition, unlike names starting with M through Z.",
        "hard", "analyze", "comparison-operators",
        "\"Ishita Menon\" sorts alphabetically before \"M\" (I comes before M), so it fails the >= 'M' condition",
        ["Ishita Menon's row was deleted from the table before the query ran", "The comparison operators only work on numbers, never on text columns", "\"Menon\" as a last name is being compared instead of the first name"],
    ),
    (
        "Which query returns only the course with the lowest credit value, using a comparison operator rather than sorting and limiting?",
        "`SELECT title, credits FROM courses WHERE credits <= 2;` returns only Microeconomics, the sole course carrying two credits, since no course in this table has fewer than two credits.",
        "medium", "apply", "comparison-operators",
        "SELECT title, credits FROM courses WHERE credits <= 2;",
        ["SELECT title, credits FROM courses ORDER BY credits LIMIT 1;", "SELECT title, credits FROM courses WHERE credits >= 2;", "SELECT MIN(title) FROM courses WHERE credits <= 2;"],
    ),
    (
        "The lesson lists six comparison operators in total: =, != (or <>), >, <, >=, and <=.\n\nWhat single idea does the lesson say every one of these six operators reduces to?",
        "Every comparison operator reduces to the same thing WHERE has always done: test a row, keep it if the test is true — greater than, less than, and their inclusive cousins are all just different shapes of that one underlying pass-or-fail test.",
        "easy", "remember", "comparison-operators",
        "Test a row against a condition, and keep it only if that test is true",
        ["Every operator sorts the result in a different direction", "Every operator only works on numeric columns, never text or dates", "Every operator requires a matching ORDER BY clause to function"],
    ),
]

LOGICAL_OPERATORS = [
    (
        "Varun writes `WHERE department = 'Computer Science' AND credits > 3 OR department = 'Economics';` intending \"Computer Science or Economics courses, but only if they carry more than three credits.\" The result incorrectly includes Microeconomics (2 credits).\n\nWhy does Microeconomics sneak in?",
        "SQL evaluates AND before OR when neither is grouped by parentheses, the same way multiplication is evaluated before addition. Varun's clause was actually read as `(department = 'Computer Science' AND credits > 3) OR department = 'Economics'`, so any Economics course qualifies regardless of its credit value.",
        "medium", "analyze", "logical-operators",
        "AND binds tighter than OR by default, so the clause is really read as (CS AND >3 credits) OR Economics, letting any Economics course through",
        ["Microeconomics actually has more than 3 credits in the table, so it correctly qualifies", "AND and OR are evaluated strictly left to right with no precedence rules at all", "The query contains a syntax error that PostgreSQL silently ignores"],
    ),
    (
        "Which corrected query fixes Varun's shortlist so that only Computer Science or Economics courses with more than three credits are returned (correctly excluding Microeconomics)?",
        "`SELECT title, department, credits FROM courses WHERE (department = 'Computer Science' OR department = 'Economics') AND credits > 3;` forces the OR to be settled first using parentheses, and only then does AND check the credit requirement against that combined result.",
        "medium", "apply", "logical-operators",
        "SELECT title, department, credits FROM courses WHERE (department = 'Computer Science' OR department = 'Economics') AND credits > 3;",
        ["SELECT title, department, credits FROM courses WHERE department = 'Computer Science' AND credits > 3 OR department = 'Economics';", "SELECT title, department, credits FROM courses WHERE department = 'Computer Science' OR credits > 3 AND department = 'Economics';", "SELECT title, department, credits FROM courses WHERE NOT department = 'Economics' AND credits > 3;"],
    ),
    (
        "What do AND and OR each require to keep a row, according to the lesson?",
        "AND keeps a row only when every joined condition is true. OR keeps a row when at least one joined condition is true — both let a single WHERE clause test more than one thing at a time, but with different requirements for a row to survive.",
        "easy", "remember", "logical-operators",
        "AND requires every condition to be true; OR requires at least one condition to be true",
        ["AND requires at least one condition to be true; OR requires every condition to be true", "AND and OR both require every condition to be true, with no difference between them", "AND requires exactly two conditions; OR requires exactly one condition"],
    ),
    (
        "`SELECT title, credits FROM courses WHERE NOT credits > 3;` returns Linear Algebra, Discrete Mathematics, and Microeconomics.\n\nWhat does NOT actually do to a condition?",
        "NOT flips a condition's truth value: rows that would have matched the original condition are excluded, and rows that would not have matched are included instead — here, rows where credits > 3 is true get excluded, leaving the ones where it's false.",
        "medium", "understand", "logical-operators",
        "It flips a condition's truth value, excluding rows that would have matched and including rows that wouldn't have",
        ["It deletes every row matching the condition from the table permanently", "It converts the condition into an OR condition automatically", "It has no effect unless combined with AND or OR in the same clause"],
    ),
    (
        "Which query correctly returns courses in Mathematics or Computer Science, restricted to those worth at least four credits, using parentheses so the grouping is unambiguous?",
        "`SELECT title, department, credits FROM courses WHERE (department = 'Mathematics' OR department = 'Computer Science') AND credits >= 4;` groups the department check first, then applies the credit requirement to that combined group, correctly excluding both 3-credit Mathematics courses.",
        "medium", "apply", "logical-operators",
        "SELECT title, department, credits FROM courses WHERE (department = 'Mathematics' OR department = 'Computer Science') AND credits >= 4;",
        ["SELECT title, department, credits FROM courses WHERE department = 'Mathematics' OR department = 'Computer Science' AND credits >= 4;", "SELECT title, department, credits FROM courses WHERE department = 'Mathematics' AND department = 'Computer Science' AND credits >= 4;", "SELECT title, department, credits FROM courses WHERE NOT (department = 'Mathematics' OR department = 'Computer Science') AND credits >= 4;"],
    ),
    (
        "Why does the lesson insist on using parentheses explicitly whenever AND and OR appear together in the same WHERE clause, rather than relying on SQL's default precedence?",
        "Relying on precedence to do the right thing by accident is risky, because AND silently binds tighter than OR whenever both appear ungrouped, turning a reasonable-looking query into a wrong answer. Parentheses remove the ambiguity by stating the grouping explicitly rather than leaving it to a rule the reader may not be thinking about.",
        "hard", "analyze", "logical-operators",
        "AND silently binds tighter than OR by default, so parentheses make the intended grouping explicit rather than relying on a rule the reader may forget",
        ["Parentheses are required by SQL syntax whenever more than one condition appears", "Parentheses make the query run measurably faster on large tables", "Without parentheses, AND and OR conditions cannot be combined at all"],
    ),
    (
        "`WHERE (department = 'Computer Science' OR department = 'Economics') AND credits > 3` and Varun's original unparenthesized version differ by only four characters, the added parentheses.\n\nWhat does the lesson say about the effect of that small change?",
        "The SQL text barely changed, four characters, but the meaning changed completely, which is exactly why relying on operator precedence to do the right thing by accident is worth avoiding whenever AND and OR appear in the same WHERE clause.",
        "medium", "analyze", "logical-operators",
        "A tiny textual change (adding parentheses) completely changed the query's meaning and correctness",
        ["The parentheses had no real effect; both versions return identical results", "The parentheses only affect how the result is displayed, not which rows are returned", "The parentheses converted the query from a SELECT into an UPDATE statement"],
    ),
]

PATTERN_MATCHING = [
    (
        "Siddharth needs everyone still using a college-issued email address, but the local part of every address is different; only the ending is shared.\n\nWhich query correctly finds every student whose email ends in \"campusmail.edu\"?",
        "`SELECT full_name, email FROM students WHERE email LIKE '%campusmail.edu';` uses % to mean \"anything at all can appear before this text,\" matching regardless of what the local part of the address looks like, as long as it ends with campusmail.edu.",
        "easy", "apply", "pattern-matching",
        "SELECT full_name, email FROM students WHERE email LIKE '%campusmail.edu';",
        ["SELECT full_name, email FROM students WHERE email = '%campusmail.edu';", "SELECT full_name, email FROM students WHERE email CONTAINS 'campusmail.edu';", "SELECT full_name, email FROM students WHERE email LIKE 'campusmail.edu';"],
    ),
    (
        "What do the two LIKE wildcard characters, % and _, each match?",
        "% stands in for any number of characters, including zero. _ stands in for exactly one character, no more and no fewer.",
        "easy", "remember", "pattern-matching",
        "% matches any number of characters (including zero); _ matches exactly one character",
        ["% matches exactly one character; _ matches any number of characters", "% and _ both match exactly one character each, with no real difference", "% matches letters only; _ matches digits only"],
    ),
    (
        "`SELECT full_name FROM students WHERE full_name LIKE 'S%';` returns Siddharth Rao and Sanya Iyer. If the query were instead written as `full_name LIKE 'S'` with no percent sign, what would happen?",
        "It would demand an exact, single-character match and return nothing at all, since LIKE never adds a wildcard on its own and no student's full name is just the letter S by itself.",
        "medium", "analyze", "pattern-matching",
        "It would return nothing, since \"S\" alone demands an exact single-character match and LIKE never adds wildcards automatically",
        ["It would return the exact same result as 'S%', since LIKE always adds a wildcard at the end", "It would return every student whose name contains the letter S anywhere", "It would raise a syntax error, since LIKE requires at least one wildcard character"],
    ),
    (
        "`SELECT full_name FROM students WHERE full_name LIKE '_a%';` returns Varun Nair, Rahul Verma, and Sanya Iyer.\n\nWhat does the pattern `_a%` actually require?",
        "It requires any single character, followed by the letter \"a\", followed by anything — matching names where \"a\" is specifically the second letter, which is different from `full_name LIKE 'a%'`, which would look for names starting with \"a\" itself.",
        "medium", "understand", "pattern-matching",
        "Any single character, followed by the letter \"a\", followed by anything — matching names with \"a\" as the second letter",
        ["Any name containing the letter \"a\" anywhere at all", "Any name that starts with the letter \"a\"", "Exactly two characters, the first of which must be \"a\""],
    ),
    (
        "`SELECT full_name, email FROM students WHERE email ILIKE '%GMAIL%';` correctly returns students with gmail.com addresses, even though the pattern is written in uppercase and the stored addresses are lowercase.\n\nWhat would happen if LIKE were used instead of ILIKE, with the exact same uppercase pattern?",
        "It would return nothing at all, since LIKE is case-sensitive by default and treats \"GMAIL\" and \"gmail\" as completely different text, unlike ILIKE, which is a PostgreSQL convenience that matches regardless of letter case.",
        "medium", "apply", "pattern-matching",
        "It would return nothing, since LIKE is case-sensitive and treats \"GMAIL\" and \"gmail\" as different text",
        ["It would return the exact same result, since LIKE and ILIKE are identical in PostgreSQL", "It would return every student regardless of their email provider", "It would raise a syntax error, since LIKE cannot accept uppercase patterns"],
    ),
    (
        "A query needs to find every student whose email address contains \"verma\" anywhere in it. Writing `email LIKE 'verma%'` instead of `email LIKE '%verma%'` returns an empty result.\n\nWhy does dropping the leading % change the outcome?",
        "`'verma%'` demands the address start with \"verma\", which none of the addresses do (verma appears mid-string, after the first name), while `'%verma%'` allows anything before and after, correctly finding \"verma\" wherever it appears in the address.",
        "hard", "analyze", "pattern-matching",
        "'verma%' demands the address start with \"verma\", while '%verma%' allows it to appear anywhere in the address",
        ["Both patterns are functionally identical; the empty result must be a database error", "'verma%' matches more addresses than '%verma%', not fewer", "The leading % is only required for uppercase letters, not lowercase ones"],
    ),
    (
        "The lesson describes ILIKE as \"specific to PostgreSQL,\" warning that \"other database systems handle case-insensitive matching differently.\"\n\nWhy does this distinction matter for someone writing SQL meant to run on more than one database system?",
        "Code relying on ILIKE would need to be rewritten or adapted for a database system that doesn't support it, since it's a PostgreSQL convenience rather than a universal SQL feature every relational database is guaranteed to implement the same way.",
        "medium", "analyze", "pattern-matching",
        "ILIKE is a PostgreSQL-specific convenience, not a universal SQL feature, so code using it may need adaptation on other database systems",
        ["It doesn't matter; ILIKE behaves identically on every relational database", "ILIKE is part of the official SQL standard and works everywhere unchanged", "Only LIKE is PostgreSQL-specific; ILIKE is universally supported"],
    ),
]

WORKING_WITH_NULL = [
    (
        "Yusuf writes `WHERE grade = NULL` to find every graded enrollment, and the query runs without error but returns zero rows, even though graded rows clearly exist in the table.\n\nWhy does this happen?",
        "= asks \"are these two values the same,\" and NULL is not a value at all, it's the absence of one. Comparing an unknown quantity against anything, even another unknown, doesn't produce true, it produces unknown, and WHERE only keeps rows where the condition comes out true.",
        "easy", "understand", "working-with-null",
        "NULL isn't a value that can be compared; = against NULL produces \"unknown,\" not true, so WHERE drops every row",
        ["It's a bug in PostgreSQL that only affects the grade column specifically", "NULL is silently treated as the number zero, and no grade equals zero", "The grade column doesn't actually contain any NULL values in this table"],
    ),
    (
        "Which query correctly finds the three enrollments that have not yet been assigned a grade?",
        "`SELECT enrollment_id, student_id, course_id, grade FROM enrollments WHERE grade IS NULL;` — IS NULL doesn't compare the column to anything; it asks the column directly whether it's holding a value at all, the only reliable way to find missing data.",
        "easy", "apply", "working-with-null",
        "SELECT enrollment_id, student_id, course_id, grade FROM enrollments WHERE grade IS NULL;",
        ["SELECT enrollment_id, student_id, course_id, grade FROM enrollments WHERE grade = NULL;", "SELECT enrollment_id, student_id, course_id, grade FROM enrollments WHERE grade = '';", "SELECT enrollment_id, student_id, course_id, grade FROM enrollments WHERE grade = 0;"],
    ),
    (
        "What does NULL actually represent, according to the lesson, and what three things does it explicitly NOT mean?",
        "NULL means \"unknown\" or missing. It does not mean zero, an empty string, or false — three easy things to confuse it with that all behave differently in comparisons.",
        "medium", "remember", "working-with-null",
        "NULL means unknown or missing; it is not zero, not an empty string, and not false",
        ["NULL means zero; it is not unknown, empty, or false", "NULL means an empty string; it is not unknown, zero, or false", "NULL and false mean the exact same thing in SQL comparisons"],
    ),
    (
        "The students table has a phone column left NULL for three students who never provided one.\n\nWhich condition is the only correct way to find those three students?",
        "`phone IS NULL` — the same IS NULL pattern that works for finding ungraded enrollments applies here, since = cannot reliably test for missing values anywhere in SQL, regardless of the column.",
        "medium", "apply", "working-with-null",
        "phone IS NULL",
        ["phone = NULL", "phone != NULL", "phone = ''"],
    ),
    (
        "Which query replaces a NULL grade with the more readable label \"In Progress\" for display purposes, without altering the underlying data?",
        "`SELECT enrollment_id, course_id, COALESCE(grade, 'In Progress') AS grade_display FROM enrollments ORDER BY enrollment_id;` — COALESCE takes a list of values and returns the first one that is not NULL, reaching for its fallback only when grade is NULL.",
        "medium", "understand", "working-with-null",
        "SELECT enrollment_id, course_id, COALESCE(grade, 'In Progress') AS grade_display FROM enrollments ORDER BY enrollment_id;",
        ["UPDATE enrollments SET grade = 'In Progress' WHERE grade IS NULL;", "SELECT enrollment_id, course_id, grade OR 'In Progress' AS grade_display FROM enrollments;", "SELECT enrollment_id, course_id, IFNULL(grade) AS grade_display FROM enrollments;"],
    ),
    (
        "Why does the lesson describe COALESCE(grade, 'In Progress') as different from actually fixing or filtering the underlying grade data?",
        "COALESCE only changes what's displayed in that one query's result; every row that already had a grade shows that grade unchanged, since COALESCE only reaches for its fallback when the first value is genuinely NULL. The actual stored grade column is never modified.",
        "hard", "analyze", "working-with-null",
        "COALESCE only affects the query's displayed output; it never modifies the actual stored grade value in the table",
        ["COALESCE permanently overwrites every NULL grade with 'In Progress' in the table", "COALESCE deletes rows where the grade is NULL from the underlying table", "COALESCE and UPDATE have exactly the same effect on the stored data"],
    ),
    (
        "Yusuf originally wrote `WHERE grade = NULL` intending to find graded enrollments, and it silently returned zero rows instead of raising an error.\n\nWhat makes this trap particularly dangerous compared to an outright error message?",
        "A silent, empty result gives no obvious signal that anything went wrong: the query runs successfully and looks like a valid answer (\"there are no graded enrollments\"), rather than clearly failing in a way that would prompt Yusuf to investigate immediately.",
        "hard", "analyze", "working-with-null",
        "It fails silently with a plausible-looking empty result, rather than an obvious error that would prompt immediate investigation",
        ["It isn't actually dangerous, since PostgreSQL always shows a warning for this exact mistake", "The query technically raises an error but the error message is hidden by default", "It's dangerous only because it deletes data instead of just reading it"],
    ),
]

SYNTHESIS = [
    (
        "Omkar's WHERE clause and Neha's comparison operators both narrow down rows using a single condition, while Varun's AND/OR/NOT lets several conditions combine.\n\nHow does the lesson describe the relationship between all of these, from equality up through combined logical conditions?",
        "Every one of these is really the same underlying idea: a test that a row either passes or fails. WHERE is the mechanism, equality is the simplest test, comparison operators extend it to ordering, and AND/OR/NOT let several such tests combine into one overall pass-or-fail decision per row.",
        "medium", "understand", "the-where-clause",
        "All of them are the same underlying idea: a pass-or-fail test per row, ranging from simple equality to combined multi-condition logic",
        ["They are unrelated features that happen to share the WHERE keyword by coincidence", "Comparison operators replace WHERE entirely once they're introduced", "AND, OR, and NOT can only be used without WHERE, never together with it"],
    ),
    (
        "Yusuf's NULL trap (`grade = NULL` returning nothing) and Varun's precedence trap (`AND`/`OR` without parentheses returning wrong rows) are both described as places where a \"reasonable-looking query\" quietly produces a wrong answer.\n\nWhat's the common lesson across both traps?",
        "SQL sometimes behaves in ways that don't match plain-English intuition, whether that's how NULL interacts with ordinary comparison operators or how AND silently binds tighter than OR; both require knowing the specific rule (use IS NULL, use parentheses) rather than trusting that the obvious-looking syntax does what it appears to say.",
        "hard", "analyze", "working-with-null",
        "SQL sometimes departs from plain-English intuition (NULL comparisons, AND/OR precedence), requiring the specific correct syntax rather than the obvious-looking one",
        ["Both traps are actually bugs in PostgreSQL that don't occur in other databases", "Both traps only occur when WHERE is combined with ORDER BY", "Neither trap is real; both queries actually work correctly as originally written"],
    ),
    (
        "Siddharth's LIKE pattern matching and Yusuf's IS NULL both exist because plain equality (=) falls short in certain situations.\n\nWhat does each one specifically solve that = cannot?",
        "LIKE solves matching a partial shape of text when there's no single fixed value to compare against (only a shared ending or fragment). IS NULL solves testing for a missing value, since = can never reliably compare against NULL, which represents the absence of a value rather than an actual value to match.",
        "medium", "analyze", "pattern-matching",
        "LIKE matches partial text patterns instead of one fixed value; IS NULL tests for missing values, which = can never reliably compare against",
        ["Both solve exactly the same problem: filtering numeric columns instead of text", "LIKE solves missing values; IS NULL solves partial text matching, the reverse pairing", "Neither actually solves anything that = cannot already do on its own"],
    ),
    (
        "Priyanka drops Rahul's Linear Algebra enrollment using the exact enrollment_id, while an earlier lesson used `student_id = 5 AND course_id = 101` to identify a single enrollment.\n\nWhy might combining two conditions with AND, as covered under logical operators, be necessary to safely target one specific row when no single unique ID is being used?",
        "A single condition like student_id = 5 alone might one day match more than one row if that student ever enrolls in something else; combining it with course_id = 101 using AND narrows the match down to exactly the one enrollment intended, the same discipline needed before any row-changing operation.",
        "hard", "apply", "logical-operators",
        "A single condition might match multiple rows over time; combining conditions with AND narrows the match down to exactly the intended row",
        ["AND is only useful for SELECT queries and has no bearing on identifying specific rows", "A single condition can never match more than one row, making AND unnecessary here", "Combining conditions with AND always requires using OR alongside it as well"],
    ),
    (
        "Across this chapter, WHERE always appears in the same fixed position (after FROM, before ORDER BY/LIMIT), regardless of whether the condition inside it uses equality, comparison operators, AND/OR/NOT, LIKE, or IS NULL.\n\nWhat does this consistent positioning reveal about how SQL treats all these different kinds of conditions?",
        "No matter how complex or simple the condition inside it becomes, WHERE always plays the exact same structural role: the single filtering step that runs after the table is chosen and before the surviving rows get sorted or trimmed — the condition's complexity changes, but WHERE's place in the query never does.",
        "medium", "understand", "the-where-clause",
        "WHERE always plays the same structural role (the filtering step after FROM, before ORDER BY/LIMIT), regardless of how complex the condition inside it is",
        ["WHERE's position changes depending on which kind of condition is used inside it", "LIKE and IS NULL require a completely different clause than WHERE to function", "Only equality conditions can use WHERE; the others require a separate clause"],
    ),
]

SET1_SOURCES = [
    (WHERE_CLAUSE, 0),
    (COMPARISON_OPERATORS, 0),
    (LOGICAL_OPERATORS, 0),
    (PATTERN_MATCHING, 0),
    (WORKING_WITH_NULL, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    WHERE_CLAUSE[1:]
    + COMPARISON_OPERATORS[1:]
    + LOGICAL_OPERATORS[1:]
    + PATTERN_MATCHING[1:]
    + WORKING_WITH_NULL[1:]
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
            "topics": "sql-essentials",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 3.3.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 3.3.2")
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
ws.title = "DBMS - MCQ - Unit 3.3"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 3 - SQL Essentials/3.3 - Filtering Data - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
