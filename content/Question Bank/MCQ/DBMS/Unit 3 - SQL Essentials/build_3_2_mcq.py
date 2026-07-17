import random
import openpyxl

random.seed(59)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

SELECT_STATEMENT = [
    (
        "The admissions coordinator asks Karthik to \"pull up the students list, all of it, for the orientation folder.\" The students table has columns for id, name, email, city, phone, and joined date.\n\nWhich query correctly returns every column and every row?",
        "`SELECT * FROM students;` names the table to read from with FROM, and `*` is shorthand meaning \"every column,\" returning all rows and all columns exactly as stored.",
        "easy", "remember", "the-select-statement",
        "SELECT * FROM students;",
        ["SELECT ALL FROM students;", "SELECT students.*;", "GET * FROM students;"],
    ),
    (
        "The coordinator later asks a narrower question: \"I just need names and cities, for the seating arrangement.\"\n\nWhich query correctly returns exactly those two columns, for every student?",
        "`SELECT full_name, city FROM students;` names exactly the columns wanted, separated by commas, and the result has exactly those two columns for all rows.",
        "easy", "apply", "the-select-statement",
        "SELECT full_name, city FROM students;",
        ["SELECT * FROM students WHERE full_name, city;", "SELECT students(full_name, city);", "SELECT full_name AND city FROM students;"],
    ),
    (
        "In a column list like `SELECT full_name, email, city FROM students;`, what determines the order columns appear in the result?",
        "The column list can hold as many or as few columns as the task needs, in any order, and that order is exactly how they appear in the result, regardless of how the table itself was created.",
        "medium", "understand", "the-select-statement",
        "The order the columns are listed in the SELECT statement itself",
        ["The order the columns were originally defined when the table was created", "Alphabetical order, regardless of how they're listed in the query", "The order in which the columns were most recently updated"],
    ),
    (
        "The students table has six columns, but the lesson warns that real production tables often have twenty or thirty, including audit timestamps and internal flags nobody looks at.\n\nWhy do experienced SQL users reach for `SELECT *` sparingly once a table grows large?",
        "Asking for every column when a report only needs two wastes bandwidth pulling data nobody will read and makes the output harder to scan, and there's a subtler risk: a query using * silently changes its own output if someone later adds a column or reorders the table.",
        "medium", "analyze", "the-select-statement",
        "It wastes bandwidth on unneeded columns and silently changes its output if the table's columns are later added to or reordered",
        ["SELECT * is always slower to type than naming columns explicitly", "SELECT * only works correctly on tables with fewer than ten columns", "Naming columns explicitly is required by SQL syntax rules for large tables"],
    ),
    (
        "What's the rule of thumb the lesson gives for when SELECT * is fine versus when naming columns explicitly is the safer habit?",
        "For a one-off look at a small table, * is fine. For anything Karthik plans to reuse, save, or hand to someone else, naming the columns explicitly is the safer habit to build early.",
        "medium", "apply", "the-select-statement",
        "SELECT * is fine for a quick one-off look; name columns explicitly for anything reused, saved, or shared",
        ["SELECT * should never be used under any circumstances, ever", "Named columns should only be used for tables with a single row", "There is no meaningful difference; both approaches are always equivalent"],
    ),
    (
        "Karthik writes a query and later notices Arjun Bhat and Sneha Gowda show up with an empty phone value.\n\nWhat does this empty value represent, and why does the lesson say \"that gap will matter a great deal once filtering enters the picture\"?",
        "The empty value represents a missing phone number that was never recorded for those students (a NULL). It matters for filtering because ordinary comparisons behave unexpectedly against a missing value, a topic covered once WHERE and NULL handling are introduced.",
        "hard", "analyze", "the-select-statement",
        "It represents a missing (NULL) phone number, which behaves unexpectedly under ordinary filtering conditions later in the course",
        ["It represents a phone number of exactly zero digits, treated as a normal value", "It represents a duplicate row that needs to be removed with DISTINCT", "It represents a syntax error in the original INSERT statement"],
    ),
]

COLUMN_TABLE_ALIASES = [
    (
        "Divya's query `SELECT full_name, city FROM students;` returns correct data, but the column headers read \"full_name\" and \"city,\" underscores and all. She wants the headers to read \"Student Name\" and \"Location\" instead, without touching the table itself.\n\nWhich SQL feature does this?",
        "A column alias, written with the AS keyword, renames a column in the output only, for the duration of one query, without ever touching anything inside the actual table.",
        "easy", "understand", "column-and-table-aliases",
        "A column alias, using the AS keyword",
        ["A table alias, using the AS keyword", "A view, created with CREATE VIEW", "A constraint, added with ALTER TABLE"],
    ),
    (
        "Divya writes `SELECT full_name AS student_name, city AS location FROM students;` and then separately runs `SELECT * FROM students;`.\n\nWhat does the second query show for the column header that was aliased?",
        "It still shows \"full_name,\" untouched — the label only exists for the one result of the aliased query; it never renames anything inside the actual table.",
        "medium", "apply", "column-and-table-aliases",
        "It still shows \"full_name,\" since the alias never changes the actual table's column name",
        ["It shows \"student_name,\" since the alias permanently renamed the column", "It shows an error, since the column no longer exists under its original name", "It shows both \"full_name\" and \"student_name\" as two separate columns"],
    ),
    (
        "SQL allows dropping the word AS entirely: `SELECT full_name student_name, city location FROM students;` produces the exact same result as using AS.\n\nWhy does the lesson still recommend keeping AS even though it's optional?",
        "Without AS, a reader scanning the query has to pause and work out whether \"student_name\" is a second column being selected or a rename of the one before it. With AS sitting in between, the intent is unambiguous at a glance: this word is a label, not another column.",
        "medium", "analyze", "column-and-table-aliases",
        "AS removes ambiguity about whether the next word is a rename or a separate column, making the query's intent clear at a glance",
        ["AS is actually required by SQL syntax and the short form is invalid", "Without AS, the query runs slower because PostgreSQL must guess the intent", "AS is only optional for table aliases, never for column aliases"],
    ),
    (
        "Divya writes `SELECT s.full_name AS student_name, s.city AS location FROM students AS s;`.\n\nWhat does \"students AS s\" accomplish, and what does \"s.full_name\" then mean?",
        "\"students AS s\" tells PostgreSQL that s now stands for the students table for the rest of the query, so \"s.full_name\" means \"the full_name column, from the table aliased as s.\"",
        "medium", "understand", "column-and-table-aliases",
        "It gives the students table the short alias s, and s.full_name refers to the full_name column through that alias",
        ["It creates a new table named s that copies all of students' data", "It renames the students table permanently to s", "It filters the students table down to only rows where the alias matches"],
    ),
    (
        "The lesson notes that a table alias \"looks unnecessary on a query this small,\" but says the habit pays off later.\n\nWhen does a table alias become genuinely useful, according to the lesson?",
        "The habit pays off the moment a query starts pulling from more than one table, exactly where the students, courses, and enrollments tables are eventually headed together, since a short alias makes it clear which table each column reference comes from.",
        "medium", "apply", "column-and-table-aliases",
        "Once a query starts pulling from more than one table at once",
        ["Only when a table has more than one hundred columns", "Only when the query includes an ORDER BY clause", "Table aliases are never actually useful in practice"],
    ),
    (
        "Divya's next request needs headers \"Full Name\" and \"Email Address,\" which contain spaces.\n\nA working answer is `SELECT s.full_name AS \"Full Name\", s.email AS \"Email Address\" FROM students AS s;` — why are double quotes needed around these particular aliases?",
        "PostgreSQL treats an unquoted alias as a single word and would otherwise misread \"Full Name\" as two separate tokens; double quotes are needed around any alias containing a space to keep it as one label.",
        "hard", "analyze", "column-and-table-aliases",
        "PostgreSQL treats an unquoted alias as a single word, so an alias containing a space needs double quotes to stay one label",
        ["Double quotes are required around every alias in PostgreSQL, with no exceptions", "Double quotes convert the alias into a numeric data type automatically", "Double quotes are only needed for table aliases, never for column aliases"],
    ),
]

DISTINCT_DUPLICATES = [
    (
        "Simran runs `SELECT city FROM students;` against eight student rows and gets eight rows back, with Bengaluru, Chennai, and Pune each appearing twice.\n\nIs this query wrong?",
        "Nothing is wrong with the query — it's faithfully reporting one city per student. It just doesn't answer Simran's actual question, which is about the set of cities involved, not the list of students.",
        "easy", "understand", "distinct-removing-duplicates",
        "No, it correctly reports one city per student; it just answers a different question than the one Simran actually wants",
        ["Yes, it's a syntax error since city appears in multiple rows", "Yes, the table itself must be broken if a value repeats", "No, but only because the table has too many rows total"],
    ),
    (
        "Which query correctly answers \"what cities appear at all,\" collapsing repeats down to one appearance each?",
        "`SELECT DISTINCT city FROM students;` changes the question from \"what city does each student live in\" to \"what cities appear at all,\" building the full list first and discarding any row whose value is an exact repeat of one already kept.",
        "easy", "apply", "distinct-removing-duplicates",
        "SELECT DISTINCT city FROM students;",
        ["SELECT UNIQUE city FROM students;", "SELECT city FROM students GROUP;", "SELECT city FROM students WHERE DISTINCT;"],
    ),
    (
        "`SELECT DISTINCT department, credits FROM courses;` is run against a table with five course rows, two of which share \"Computer Science, 4\" and two of which share \"Mathematics, 3.\"\n\nHow does DISTINCT decide which rows count as duplicates when more than one column is listed?",
        "DISTINCT keeps a row only if the entire combination of values, taken together across all listed columns, is unique, not just one column in isolation — so both Computer Science/4 rows collapse into one, and both Mathematics/3 rows collapse into one.",
        "medium", "understand", "distinct-removing-duplicates",
        "It keeps a row only if the full combination of all listed column values together is unique, not any single column alone",
        ["It only checks the first column listed and ignores the rest", "It removes a row if ANY one of the listed columns matches another row", "It requires every column in the table to be listed, not just some"],
    ),
    (
        "The courses table has five rows: two Computer Science courses (4 credits each), two Mathematics courses (3 credits each), and one Economics course (3 credits).\n\nHow many rows does `SELECT DISTINCT department, credits FROM courses;` return?",
        "Three rows: Computer Science/4, Mathematics/3, and Economics/3. Economics stays on its own since no other row shares its exact department-and-credits combination, even though it shares its credit value with Mathematics.",
        "medium", "apply", "distinct-removing-duplicates",
        "Three rows, since Economics doesn't share its exact department-and-credits combination with any other row",
        ["Five rows, since DISTINCT has no effect when more than one column is listed", "One row, since all courses eventually collapse into a single combination", "Two rows, matching only the two departments with repeated credit values"],
    ),
    (
        "Does DISTINCT change anything about the underlying courses table itself?",
        "No — DISTINCT does not change the underlying table in any way, only the shape of the answer that comes back for that one query.",
        "medium", "understand", "distinct-removing-duplicates",
        "No, it only changes the shape of the result for that one query, leaving the table itself untouched",
        ["Yes, it permanently deletes the duplicate rows from the table", "Yes, it merges duplicate rows into a single row inside the table", "Yes, it adds a new column to the table marking which rows were duplicates"],
    ),
    (
        "The registrar wants departments with courses offered, listed once each. `SELECT DISTINCT department FROM courses;` returns Computer Science, Mathematics, and Economics, even though the underlying table has five course rows.\n\nWhat does this illustrate about DISTINCT applied to a single column versus a multi-column list?",
        "Applied to a single column, DISTINCT collapses every row down to the unique values of that one column alone, regardless of what differs in the other columns (like course titles) — a more aggressive collapse than the multi-column case, which only merges rows matching on every listed column together.",
        "hard", "analyze", "distinct-removing-duplicates",
        "Single-column DISTINCT collapses based on that one column alone, ignoring differences elsewhere; multi-column DISTINCT requires every listed column to match",
        ["Single-column and multi-column DISTINCT always produce the exact same row count", "Single-column DISTINCT is invalid syntax; only multi-column lists are allowed", "Multi-column DISTINCT ignores all but the first column listed, same as single-column"],
    ),
]

EXPRESSIONS_CALCULATED_COLUMNS = [
    (
        "Nikhil wants a \"workload score\" that doubles the credit value of each course, without adding a new column to the table.\n\nWhich query computes this on the fly?",
        "`SELECT title, credits, credits * 2 AS double_credits FROM courses;` computes the arithmetic directly in the SELECT list, aliasing the result as double_credits, with nothing stored anywhere in the table.",
        "easy", "apply", "expressions-and-calculated-columns",
        "SELECT title, credits, credits * 2 AS double_credits FROM courses;",
        ["SELECT title, credits SET double_credits = credits * 2 FROM courses;", "UPDATE courses SET double_credits = credits * 2;", "SELECT title, credits WHERE double_credits = credits * 2 FROM courses;"],
    ),
    (
        "PostgreSQL computes `credits * 2` fresh for every row when the query runs.\n\nWhat happens if the underlying credits value changes and the exact same query is run again later?",
        "Nothing about the math is stored anywhere; running the same query again would simply recompute double_credits from whatever credits holds at that later time, reflecting the new value automatically.",
        "medium", "understand", "expressions-and-calculated-columns",
        "The query recomputes the doubled value fresh from the new credits value, since nothing was ever stored",
        ["The query returns the old, stale doubled value from the first time it ran", "The query fails with an error, since double_credits was never a real column", "The credits column itself is automatically doubled in the table"],
    ),
    (
        "Nikhil needs a combined label like \"Computer Science: Database Systems\" built from the department and title columns.\n\nWhich operator does PostgreSQL use to glue text values together, and what does the lesson call this operation?",
        "The || operator, called concatenation, takes whatever sits on its left and right and joins them into one piece of text, left to right, as in `department || ': ' || title AS course_label`.",
        "easy", "remember", "expressions-and-calculated-columns",
        "The || operator, called concatenation",
        ["The + operator, called addition", "The & operator, called string joining", "The CONCAT keyword, called text merging"],
    ),
    (
        "In `department || ': ' || title AS course_label`, what is `': '` specifically, and where does it come from?",
        "It's a literal piece of text written directly in the query, a fixed value in single quotes that is not read from any column, simply inserted as-is between the two real column values to give the separator its shape.",
        "medium", "apply", "expressions-and-calculated-columns",
        "A literal text value written directly in the query, not read from any column",
        ["A third column in the courses table holding punctuation marks", "A system variable PostgreSQL fills in automatically for every query", "An alias referring to a separate table storing separator characters"],
    ),
    (
        "Nikhil's query `SELECT course_id, title, credits, credits * 2 AS double_credits, department || ': ' || title AS course_label FROM courses;` returns five columns.\n\nWhat does this demonstrate about mixing expressions with ordinary columns?",
        "An expression doesn't have to stand alone; it sits in the SELECT list exactly like any real column, so a single query can freely mix calculated values with columns pulled straight from the table, with as many expressions as needed beside as many plain columns as needed.",
        "medium", "understand", "expressions-and-calculated-columns",
        "A single query can freely mix any number of calculated expressions with plain, unmodified columns in the same SELECT list",
        ["Expressions and plain columns cannot appear together in the same query", "Only one expression is allowed per query, alongside unlimited plain columns", "Mixing expressions with plain columns requires a separate JOIN clause"],
    ),
    (
        "The catalog page needs a \"credit hours per week\" figure, assuming 15 contact hours per credit, shown alongside the course title.\n\nWhich query correctly computes this, and what would it show for a 4-credit course?",
        "`SELECT title, credits * 15 AS contact_hours FROM courses;` shows 60 contact hours for each 4-credit course (4 * 15 = 60) and 45 for each 3-credit course, computed fresh from whatever credits currently holds.",
        "medium", "apply", "expressions-and-calculated-columns",
        "SELECT title, credits * 15 AS contact_hours FROM courses; — showing 60 for a 4-credit course",
        ["SELECT title, credits + 15 AS contact_hours FROM courses; — showing 19 for a 4-credit course", "SELECT title, 15 / credits AS contact_hours FROM courses; — showing 3.75 for a 4-credit course", "SELECT title, credits AS contact_hours * 15 FROM courses; — showing 60 for a 4-credit course"],
    ),
]

SORTING_RESULTS = [
    (
        "Rhea runs `SELECT full_name, city FROM students;` and the rows come back in an order that is not alphabetical, not by city, not anything she can rely on.\n\nWhat does the lesson say about a table's row order by default?",
        "A table's rows have no built-in order at all unless a query explicitly asks for one — whatever order PostgreSQL happens to store or retrieve rows in is not something a query should ever depend on without ORDER BY.",
        "easy", "understand", "sorting-results",
        "A table's rows have no built-in order at all unless a query explicitly requests one with ORDER BY",
        ["Tables are always stored in the exact order rows were inserted", "Tables are always sorted alphabetically by their primary key", "Tables are always sorted by whichever column comes first in the CREATE TABLE statement"],
    ),
    (
        "Which query lists students alphabetically by name, from Aditya Kulkarni to Sneha Gowda?",
        "`SELECT full_name, city FROM students ORDER BY full_name;` sorts in ascending order, PostgreSQL's default when no direction is specified, which for text means alphabetical A to Z.",
        "easy", "apply", "sorting-results",
        "SELECT full_name, city FROM students ORDER BY full_name;",
        ["SELECT full_name, city FROM students SORT BY full_name;", "SELECT full_name, city FROM students ORDER full_name;", "SELECT full_name, city FROM students WHERE full_name ASC;"],
    ),
    (
        "Rhea wants the newest joiners at the top of a \"welcome our latest students\" notice.\n\nWhich query achieves this, and why does she need to add anything beyond a plain ORDER BY joined_on?",
        "`SELECT full_name, joined_on FROM students ORDER BY joined_on DESC;` — plain ascending order on join date would put the oldest joiners first, exactly backwards from what she needs, so DESC reverses the direction to put the newest first.",
        "medium", "apply", "sorting-results",
        "SELECT full_name, joined_on FROM students ORDER BY joined_on DESC; — DESC reverses the default ascending order",
        ["SELECT full_name, joined_on FROM students ORDER BY joined_on; — ascending order already puts newest first for dates", "SELECT full_name, joined_on FROM students ORDER BY joined_on ASC; — ASC always means newest first for dates", "SELECT full_name, joined_on FROM students REVERSE ORDER BY joined_on;"],
    ),
    (
        "Rhea wants students grouped by city, and within each city, listed alphabetically by name. She writes `ORDER BY city, full_name`.\n\nHow does ORDER BY handle a list of more than one column?",
        "It sorts by the first column listed, then uses the second column only to break ties within groups that share the same first value — so all of Bengaluru's students group together, sorted alphabetically within that group, then Chennai's students, and so on.",
        "medium", "understand", "sorting-results",
        "It sorts by the first column, then uses later columns only to break ties among rows sharing the same earlier value",
        ["It sorts by whichever column has the most distinct values first", "It sorts each column completely independently, ignoring the others", "It only actually sorts by the last column listed, ignoring earlier ones"],
    ),
    (
        "In `ORDER BY city, full_name`, Arjun Bhat appears before Ishaan Verma even though both are Bengaluru students.\n\nWhy?",
        "Both share the same city, so the tie on city is broken by the second sort key, full_name, and \"Arjun Bhat\" sorts alphabetically before \"Ishaan Verma.\"",
        "medium", "apply", "sorting-results",
        "Their tie on city is broken by the second sort column, full_name, and \"Arjun\" comes before \"Ishaan\" alphabetically",
        ["Arjun Bhat was inserted into the table before Ishaan Verma", "ORDER BY city, full_name actually only sorts by full_name, ignoring city", "The database always lists shorter names before longer ones"],
    ),
    (
        "Each column in an ORDER BY list can carry its own direction. What would `ORDER BY city, full_name DESC` produce?",
        "Cities would stay grouped in ascending (alphabetical) order, but within each city's group, names would be listed from Z to A instead of A to Z, since DESC applies specifically to full_name here, not to city.",
        "hard", "analyze", "sorting-results",
        "Cities grouped in ascending order, but names within each city listed from Z to A",
        ["Both cities and names would be sorted in descending order together", "This is invalid syntax; DESC can only apply to the first column in the list", "Cities would be sorted in descending order, and names would stay ascending"],
    ),
]

LIMITING_RESULTS = [
    (
        "Tanvi's dashboard widget only has room for five rows, but the enrollments table holds every enrollment ever recorded and keeps growing.\n\nWhich clause lets her ask the database itself for just the first few rows, rather than pulling everything and trimming it in application code?",
        "LIMIT — a clause built exactly for this request, keeping only a specified number of rows of a result and dropping the rest, with the database doing the trimming instead of any downstream application code.",
        "easy", "remember", "limiting-results",
        "LIMIT",
        ["TOP", "FIRST", "ROWCOUNT"],
    ),
    (
        "`SELECT student_id, course_id, enrolled_on FROM enrollments ORDER BY enrolled_on DESC LIMIT 5;` is run against a ten-row enrollments table.\n\nWhat do the two clauses ORDER BY and LIMIT each contribute?",
        "ORDER BY enrolled_on DESC does the real work of deciding which rows count as \"recent\" (newest first); LIMIT 5, placed after it, simply keeps the first five rows of that already-sorted result and drops the rest.",
        "medium", "understand", "limiting-results",
        "ORDER BY decides which rows count as \"recent\"; LIMIT keeps only the first five of that sorted result",
        ["LIMIT decides the sort order; ORDER BY trims the result to five rows", "Both clauses do the exact same thing and either one alone would suffice", "ORDER BY only works after LIMIT has already trimmed the rows"],
    ),
    (
        "`SELECT student_id, course_id, enrolled_on FROM enrollments LIMIT 5;` is run with no ORDER BY at all.\n\nWhy does the lesson say this query is risky, even though it runs without error and returns five rows?",
        "Without a sort, \"the first five rows\" is just whatever order the table happens to be stored or scanned in internally, which can change between runs, after an update, or after PostgreSQL chooses a different way to fetch the data — nothing in the query says these five rows are the most recent or most meaningful.",
        "medium", "analyze", "limiting-results",
        "Without ORDER BY, \"the first five rows\" depends on internal storage order, which can change and carries no guaranteed meaning",
        ["It's risky only because LIMIT 5 is too large a number to request safely", "It's risky because LIMIT without ORDER BY is actually invalid SQL syntax", "It's risky because it always returns fewer than five rows in practice"],
    ),
    (
        "A \"page 2 of enrollments\" admin screen needs to skip past rows already shown on page 1.\n\nWhich clause, placed after LIMIT, tells PostgreSQL how many rows to skip before it starts collecting the ones to return?",
        "OFFSET — `LIMIT 5 OFFSET 5` returns the next five most recent enrollments (ranked sixth through tenth), since the first five were already shown on an earlier page and OFFSET 5 skips past them.",
        "easy", "remember", "limiting-results",
        "OFFSET",
        ["SKIP", "PAGE", "AFTER"],
    ),
    (
        "For a hypothetical \"page 3\" request on a larger dataset, what would need to change in `LIMIT 5 OFFSET 5`?",
        "OFFSET 5 would become OFFSET 10, skipping the first ten rows (pages 1 and 2's worth) before collecting the next batch of five for page 3 — LIMIT stays the same since each page still shows five rows.",
        "medium", "apply", "limiting-results",
        "OFFSET 5 would change to OFFSET 10, skipping the first ten rows before collecting the next five",
        ["LIMIT 5 would change to LIMIT 10, while OFFSET stays at 5", "Both LIMIT and OFFSET would need to become 10", "Nothing changes; the same query works for every page automatically"],
    ),
    (
        "The department office wants the three courses with the most credits, and among ties, the alphabetically first title.\n\nWhich query correctly returns this?",
        "`SELECT title, credits FROM courses ORDER BY credits DESC, title LIMIT 3;` sorts by credits from highest to lowest, breaks any tie by title alphabetically, and keeps only the top three rows.",
        "hard", "apply", "limiting-results",
        "SELECT title, credits FROM courses ORDER BY credits DESC, title LIMIT 3;",
        ["SELECT title, credits FROM courses LIMIT 3 ORDER BY credits DESC, title;", "SELECT title, credits FROM courses ORDER BY credits, title DESC LIMIT 3;", "SELECT title, credits FROM courses WHERE credits = MAX(credits) LIMIT 3;"],
    ),
]

SYNTHESIS = [
    (
        "Karthik's earlier lesson warns that a query using SELECT * silently changes its output if the table's columns change. Divya's lesson shows that a column alias like `full_name AS student_name` only affects the output, never the table.\n\nWhat do both of these facts together reveal about the relationship between a SELECT query's output and the underlying table's actual structure?",
        "A query's output (column selection, aliases, computed values) is a separate, temporary view built fresh each time the query runs; it can be shaped, renamed, or limited freely without ever altering the table's real, stored structure or column names.",
        "medium", "analyze", "column-and-table-aliases",
        "A query's output is a temporary, freshly-built view; it can be shaped or renamed without ever changing the table's real stored structure",
        ["A query's output always permanently modifies the underlying table's column names", "SELECT * and column aliases both permanently change the table's structure identically", "There is no real relationship between a query's output and the table underneath it"],
    ),
    (
        "Nikhil's expressions lesson shows credits * 2 AS double_credits recomputed fresh every time the query runs. Rhea's sorting lesson shows ORDER BY choosing a row order fresh every time too, with no permanent effect on storage.\n\nWhat common principle links expressions and ORDER BY?",
        "Both are computed or applied at query time, based on the SELECT statement itself, rather than being stored properties of the table — the table's actual stored data and row order remain completely unaffected by either one.",
        "medium", "analyze", "expressions-and-calculated-columns",
        "Both are computed fresh at query time from the SELECT statement, leaving the table's actual stored data and order unaffected",
        ["Expressions are stored permanently, while ORDER BY is only temporary", "ORDER BY is stored permanently, while expressions are only temporary", "Both permanently reorder and modify the table's stored rows"],
    ),
    (
        "Simran's DISTINCT lesson removes duplicate rows from a result. Tanvi's LIMIT lesson trims a result down to a fixed number of rows. Both change how many rows come back, but for different reasons.\n\nWhat's the key difference between what DISTINCT filters out and what LIMIT filters out?",
        "DISTINCT removes rows based on their content, dropping exact repeats of values already seen. LIMIT removes rows based on position, keeping only a fixed count of whatever rows are first in the (possibly sorted) result, regardless of whether their content repeats.",
        "hard", "analyze", "distinct-removing-duplicates",
        "DISTINCT filters by content, removing exact duplicate values; LIMIT filters by position, keeping a fixed count regardless of content",
        ["DISTINCT and LIMIT both filter by exactly the same criterion: row position", "DISTINCT and LIMIT both filter by exactly the same criterion: row content", "DISTINCT only works with LIMIT and cannot be used on its own"],
    ),
    (
        "Karthik's lesson introduces SELECT and column choice. Divya's introduces aliases. Simran's introduces DISTINCT. Nikhil's introduces expressions. Rhea's introduces ORDER BY. Tanvi's introduces LIMIT/OFFSET.\n\nIf a single query needed to use all six ideas together, roughly what order would the clauses need to appear in, matching how the lessons describe them being layered on?",
        "SELECT (with column choice, aliases, DISTINCT, and expressions all inside the SELECT list) comes first, naming what to retrieve; FROM names the table; ORDER BY comes after to arrange the surviving rows; and LIMIT (with OFFSET) comes last to trim the final, sorted result.",
        "hard", "understand", "sorting-results",
        "SELECT list (columns, aliases, DISTINCT, expressions), then FROM, then ORDER BY, then LIMIT/OFFSET last",
        ["LIMIT first, then ORDER BY, then FROM, then the SELECT list last", "FROM first, then LIMIT, then the SELECT list, then ORDER BY last", "The order of clauses never matters and can be written in any sequence"],
    ),
]

SET1_SOURCES = [
    (SELECT_STATEMENT, 0),
    (COLUMN_TABLE_ALIASES, 0),
    (DISTINCT_DUPLICATES, 0),
    (EXPRESSIONS_CALCULATED_COLUMNS, 0),
    (SORTING_RESULTS, 0),
    (LIMITING_RESULTS, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    SELECT_STATEMENT[1:]
    + COLUMN_TABLE_ALIASES[1:]
    + DISTINCT_DUPLICATES[1:]
    + EXPRESSIONS_CALCULATED_COLUMNS[1:]
    + SORTING_RESULTS[1:]
    + LIMITING_RESULTS[1:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 3.2.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 3.2.2")
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
ws.title = "DBMS - MCQ - Unit 3.2"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 3 - SQL Essentials/3.2 - Reading Data with SELECT - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
