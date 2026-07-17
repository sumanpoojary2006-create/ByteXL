import random
import openpyxl

random.seed(37)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

WHAT_IS_RELATIONAL_ALGEBRA = [
    (
        "Devika's manager explains that underneath every dashboard and report, a database performs a small, precise set of operations on its tables, each one taking a table in and handing back a table out.\n\nWhat is this formal toolkit called?",
        "This formal, mathematical toolkit beneath every question a relational database can answer is called relational algebra.",
        "easy", "remember", "what-is-relational-algebra",
        "Relational algebra",
        ["The system catalog", "The three-schema architecture", "A foreign key constraint"],
    ),
    (
        "In relational algebra, the formal name for a table, a set of rows sharing the same columns, is used constantly.\n\nWhat is that formal name?",
        "A relation is simply the formal name for a table in this context — a set of rows sharing the same columns.",
        "easy", "remember", "what-is-relational-algebra",
        "A relation",
        ["A domain", "A schema", "A transaction"],
    ),
    (
        "Every single relational algebra operation, no matter which one, obeys one rule without exception: feed a table in, and a table comes back out, with the same rows-and-columns shape as anything else the database stores.\n\nWhat is this property called, and why does it matter?",
        "This is closure. Because every operation's output is again a relation, the output of one operation can always become the input to another, letting a whole chain of simple steps answer a complicated question one step at a time, just like chaining arithmetic operations that always output a number.",
        "medium", "understand", "what-is-relational-algebra",
        "Closure — every operation's output is itself a relation, so operations can be chained together",
        ["Normalization — every operation removes duplicate rows automatically", "Indexing — every operation speeds up future queries automatically", "Serialization — every operation converts a relation into plain text"],
    ),
    (
        "Devika's manager says a database \"cannot afford to treat each differently worded question as a brand new puzzle.\" \"Mystery novels under 400 rupees\" and \"novels in the mystery genre priced below 400\" are different sentences.\n\nHow does relational algebra help the database handle both the same way?",
        "Relational algebra gives the database a fixed, well-understood vocabulary of operations that any request can be broken down into, so differently worded questions asking for the same thing express as the same underlying sequence of operations.",
        "medium", "analyze", "what-is-relational-algebra",
        "It expresses both differently worded requests as the same underlying sequence of formal operations",
        ["It translates both sentences into English before running either one", "It ignores the wording entirely and always returns every row in the table", "It requires the database to store both sentences as separate saved queries"],
    ),
    (
        "Relational algebra is described as \"not a programming language a person types directly, but the theoretical bedrock\" underneath something else.\n\nWhat does relational algebra provide the foundation for?",
        "It is the theoretical bedrock that lets query planning, and eventually SQL itself, exist on solid ground rather than guesswork — a fixed vocabulary the database can reason about and compare different ways of answering a query.",
        "hard", "analyze", "what-is-relational-algebra",
        "It provides the theoretical foundation for query planning and for SQL itself",
        ["It provides the physical storage format every database must use on disk", "It provides the network protocol used to send queries to a remote server", "It provides the exact color scheme used by database administration tools"],
    ),
    (
        "Devika's manager says a database \"cannot afford to treat each\" differently worded question \"as a brand new puzzle,\" since it answers thousands of them a day.\n\nHow does having a fixed vocabulary of operations help the database compare different ways of answering the same query?",
        "If every request can be expressed as a combination of the same small set of operations, the database can compare different ways of carrying out those operations and choose a faster one — exactly the planning step that happens invisibly every time a query is answered.",
        "medium", "analyze", "what-is-relational-algebra",
        "It lets the database express any request as combinations of the same operations, so different execution strategies can be compared and a faster one chosen",
        ["It lets the database skip validating any query it has seen worded similarly before", "It removes the need for a query processor, since the vocabulary answers queries directly", "It guarantees every query returns results in under one second"],
    ),
    (
        "\"Feed a table in, and a table comes back out, with the same rows-and-columns shape as anything else the database stores.\" The lesson compares this to ordinary arithmetic.\n\nWhat is that comparison, and why does it matter for relational algebra?",
        "Just as adding two numbers always gives back a number, letting additions be chained together, every relational algebra operation always gives back a relation, which is exactly what lets the output of one operation become the input to the next.",
        "medium", "understand", "what-is-relational-algebra",
        "Like arithmetic, where adding numbers always yields a number that can feed the next addition, every operation's output is a relation that can feed the next operation",
        ["Like arithmetic, relational algebra operations must always be performed in a fixed, unchangeable order", "Like arithmetic, every relational algebra operation must involve exactly two relations", "The comparison only holds for selection and projection, not for join or set operations"],
    ),
]

SELECTION_PROJECTION = [
    (
        "A librarian wants every book under 300 rupees; a volunteer wants only book titles and authors, no prices or genre codes, for every book.\n\nWhich operation does each request correspond to?",
        "The librarian's request, narrowing to rows that meet a price condition while keeping every column, is selection (sigma). The volunteer's request, keeping every row but only certain columns, is projection (pi).",
        "easy", "understand", "selection-and-projection",
        "The librarian's request is selection; the volunteer's request is projection",
        ["The librarian's request is projection; the volunteer's request is selection", "Both requests are examples of selection", "Both requests are examples of projection"],
    ),
    (
        "Selection is applied to the Books relation with the condition \"price less than 300.\" The original relation has five rows and five columns.\n\nWhat happens to the row count and column count in the result?",
        "Selection filters rows without ever touching columns — the column count stays exactly the same (still five columns), while the row count narrows to only the rows that satisfy the condition.",
        "medium", "apply", "selection-and-projection",
        "The row count shrinks to only matching rows; the column count stays exactly the same",
        ["The column count shrinks; the row count stays exactly the same", "Both the row count and column count shrink", "Neither the row count nor the column count changes"],
    ),
    (
        "Rohan projects the Books relation down to just the genre column. The raw values would be Mystery, Poetry, Mystery, Travel, Poetry, five values with genre repeated.\n\nWhat does the formal definition of projection do with those repeated values?",
        "Because a relation is meant to represent a set, relational algebra's projection removes duplicate rows from its result, leaving just the distinct values: Mystery, Poetry, and Travel.",
        "medium", "analyze", "selection-and-projection",
        "It removes the duplicates, leaving only the distinct genre values",
        ["It keeps all five values exactly as they appear, including duplicates", "It converts the duplicate values into a single combined text string", "It raises an error, since projection cannot be applied to a single column"],
    ),
    (
        "Rohan needs \"the titles of every mystery novel,\" which requires both filtering to mystery rows and keeping only the title column.\n\nWhat allows the output of the selection step to be fed directly into the projection step, with no special glue code in between?",
        "This is closure at work: because selection's output is itself a relation, and projection's input must be a relation, the two operations snap together cleanly, one feeding directly into the next.",
        "medium", "understand", "selection-and-projection",
        "Closure — selection's output is a relation, which is exactly the kind of input projection requires",
        ["A special conversion function that turns selection results into a format projection can read", "The two operations must always be run in a single combined statement", "Selection and projection cannot actually be chained together directly"],
    ),
    (
        "Compare selection and projection on two dimensions: what each one trims, and whether each removes duplicate rows from its result.\n\nWhich statement is correct?",
        "Selection trims rows (based on a condition) and does not remove duplicates. Projection trims columns (based on a list of column names) and does remove duplicate rows in its formal definition.",
        "hard", "analyze", "selection-and-projection",
        "Selection trims rows and keeps duplicates; projection trims columns and removes duplicates",
        ["Selection trims columns and removes duplicates; projection trims rows and keeps duplicates", "Both operations trim rows and both remove duplicates", "Both operations trim columns and neither removes duplicates"],
    ),
    (
        "Rohan needs \"every mystery novel priced above 400,\" which requires checking genre equals Mystery AND price is greater than 400 at the same time.\n\nIs this compound condition still a single selection operation, or does it require a new kind of operation?",
        "It is still selection (sigma), just with a compound condition combining two checks. Whether a condition is a single comparison or several joined together, the operation still works row by row and still leaves every column exactly as it was.",
        "medium", "apply", "selection-and-projection",
        "It is still a single selection operation, just with a compound condition",
        ["It requires two separate operations: one selection and one projection", "It becomes a join operation, since two conditions are being compared", "It becomes a set operation, since two conditions are combined with AND"],
    ),
    (
        "Does selection ever discard a column from its result, and does projection ever discard a row based on a condition?",
        "Selection never discards any column — it keeps every column of the rows that match. Projection never filters rows based on a condition — it keeps all rows, only restricted to the chosen columns.",
        "hard", "understand", "selection-and-projection",
        "No — selection never discards columns, and projection never filters rows based on a condition",
        ["Yes — selection discards non-matching columns, and projection discards non-matching rows", "Yes — selection discards columns, but projection never discards rows", "No — but only because both operations are actually identical to each other"],
    ),
]

SET_OPERATIONS = [
    (
        "Meera has two relations, Coding Club and Robotics Club, each with a single student_id column drawing from the same college's student ID numbering scheme.\n\nWhat property must two relations share before union, intersection, or difference can be meaningfully applied to them?",
        "The two relations must be union-compatible: they need the same number of columns, and each corresponding column must draw its values from the same domain.",
        "medium", "remember", "set-operations",
        "They must be union-compatible — matching in number of columns and in the domain each column draws from",
        ["They must have exactly the same number of rows", "They must share at least one identical row already", "They must both have a primary key defined"],
    ),
    (
        "Coding Club has student IDs {S101, S104, S107, S110} and Robotics Club has {S104, S107, S112}.\n\nWhat does the union of these two relations produce?",
        "Union keeps every row appearing in at least one relation, with duplicates collapsed to a single copy: S101, S104, S107, S110, S112 — five distinct IDs, even though the two relations together listed seven rows.",
        "medium", "apply", "set-operations",
        "{S101, S104, S107, S110, S112} — five distinct IDs, with S104 and S107 counted only once",
        ["{S104, S107} — only the IDs that appear in both relations", "{S101, S110} — only the IDs unique to Coding Club", "All seven rows from both relations, including S104 and S107 twice each"],
    ),
    (
        "Using the same two club relations, what does the intersection produce, and what real-world question does it answer?",
        "Intersection keeps only the rows appearing in both relations at once: {S104, S107}, answering \"who belongs to both clubs.\"",
        "easy", "understand", "set-operations",
        "{S104, S107} — answering who belongs to both clubs",
        ["{S101, S104, S107, S110, S112} — answering who belongs to either club", "{S101, S110} — answering who belongs only to Coding Club", "An empty result, since no student can join two clubs"],
    ),
    (
        "Applying \"Coding Club minus Robotics Club\" gives {S101, S110}. What would \"Robotics Club minus Coding Club\" give instead, and what does this reveal about the difference operation?",
        "\"Robotics Club minus Coding Club\" gives just {S112}, the one robotics member who never joined coding. This shows that, unlike union and intersection, difference is the one set operation where the order of the two relations changes the result.",
        "hard", "analyze", "set-operations",
        "{S112} — and it shows that difference, unlike union or intersection, changes result depending on the order of the two relations",
        ["{S101, S110} — the same result, since difference always ignores order", "{S104, S107} — the overlap between the two clubs", "An error, since difference can only be applied in one direction"],
    ),
    (
        "Meera tries to compare her Coding Club relation (a column of student IDs) against a relation of book titles from the library catalogue, asking \"which rows appear in both.\"\n\nWhy is this comparison meaningless?",
        "A student ID and a book title are not comparable values drawn from the same domain, so there is no sensible way to line up the columns to check for a match — the two relations are not union-compatible.",
        "medium", "analyze", "set-operations",
        "A student ID and a book title are not comparable values from the same domain, so the relations are not union-compatible",
        ["It isn't meaningless; any two relations can always be compared with set operations", "Book titles are always longer than student IDs, which breaks the comparison", "The library catalogue relation has too many rows for the comparison to run"],
    ),
    (
        "Two relations can have entirely different column names, such as \"student_id\" in one and \"member_no\" in another, and still be union-compatible.\n\nWhat actually determines union-compatibility, if not the column labels?",
        "What matters is the number of columns and the domain each one draws from, not the labels typed above them — two relations can be union-compatible even with completely different column names.",
        "medium", "understand", "set-operations",
        "The number of columns and the domain each column draws from, regardless of the labels used",
        ["The exact column names must match character-for-character", "The number of rows in each relation must be identical", "Union-compatibility does not actually exist as a real requirement"],
    ),
    (
        "Of Meera's three requests, everyone in either club (union), everyone in both clubs (intersection), and coding-only members (difference), which one requires knowing the order the two relations are written in to get a correct answer?",
        "Difference is the one set operation in this trio where order matters — Coding Club minus Robotics Club gives a different answer than Robotics Club minus Coding Club, unlike union or intersection, which give the same result regardless of order.",
        "medium", "analyze", "set-operations",
        "Difference — reversing the order of the two relations changes the result",
        ["Union — reversing the order changes which rows are kept", "Intersection — reversing the order changes which rows are kept", "None of the three; order never matters for any set operation"],
    ),
]

JOIN_OPERATOR = [
    (
        "A parent asks Farah, \"Which course is Kabir Singh actually taking?\" The Students relation only has student ID and name; the Enrollments relation only has student ID and course code.\n\nWhy can't either relation alone answer the parent's question?",
        "Neither table alone holds both a student's name and their course — Students knows the name, Enrollments knows the course, and the two facts only exist together once the two relations are combined based on their shared student ID.",
        "easy", "understand", "join-operator",
        "Each relation only holds half of the needed information; the name and the course exist in two separate tables",
        ["The Students relation is missing a primary key, so it cannot be queried at all", "Enrollments has no rows for any student, so nothing can be found", "Farah's question is ambiguous and has no single correct answer"],
    ),
    (
        "Pairing every row of Students with every row of Enrollments, with no filtering at all, produces every possible combination of one row from each, including nonsense pairings like Kabir Singh matched with Meenal Rao's enrollment.\n\nWhat is this unfiltered pairing called?",
        "This blunt, unfiltered pairing of every row with every row is the cartesian product, the starting point that join is built on top of.",
        "medium", "remember", "join-operator",
        "The cartesian product",
        ["The union", "The intersection", "A composite key"],
    ),
    (
        "The join operator takes the cartesian product of two relations and then does one more thing to it.\n\nWhat does join do to the cartesian product to produce a meaningful result?",
        "Join filters the cartesian product down to only the pairings where a chosen condition holds, typically that matching columns from each relation are actually equal, such as both student_id values genuinely matching.",
        "medium", "apply", "join-operator",
        "It filters the cartesian product to keep only pairings where a matching condition (usually equality on a shared column) holds",
        ["It sorts the cartesian product alphabetically by the first column", "It removes every column except the primary keys from both relations", "It duplicates every row in the cartesian product a second time"],
    ),
    (
        "In Farah's join of Students and Enrollments on student_id, Dev Sharma (student ST03) does not appear anywhere in the result.\n\nWhy not?",
        "No row in Enrollments has a matching student_id for Dev Sharma, meaning he simply has not enrolled in anything yet — with no matching pairing, his row is filtered out of the join's result entirely.",
        "medium", "analyze", "join-operator",
        "No row in Enrollments has a matching student_id for him, since he hasn't enrolled in any course yet",
        ["Dev Sharma was accidentally deleted from the Students relation", "The join operator only ever keeps the first two students alphabetically", "Enrollments does not allow more than two students to be joined at once"],
    ),
    (
        "Splitting Students and Enrollments into separate relations, rather than repeating a student's name on every enrollment row, keeps data organised. But this creates a tradeoff.\n\nWhat is that tradeoff, and how does join pay it back?",
        "The tradeoff is that any question spanning both ideas, like which course a named student is taking, cannot be answered by looking at one relation alone. Join pays that back by letting the database recombine the cleanly separated relations on demand, exactly when a cross-table question needs both.",
        "hard", "analyze", "join-operator",
        "Keeping relations separate means cross-table questions need both tables at once; join recombines them on demand when that's needed",
        ["The tradeoff is slower storage; join makes disk reads faster to compensate", "The tradeoff is duplicate data; join removes all duplicate rows automatically", "There is no real tradeoff; splitting relations has no downside at all"],
    ),
    (
        "Farah's Students relation has 3 rows and her Enrollments relation has 3 rows. The cartesian product pairs every row of one with every row of the other before any filtering.\n\nHow many total row-pairings does the cartesian product produce, and how many survive after the join's matching condition is applied?",
        "The cartesian product produces 3 x 3 = 9 total pairings. Join's matching condition, that both student_id values agree, filters that down to only 3 pairings where the condition is genuinely true.",
        "medium", "apply", "join-operator",
        "9 total pairings from the cartesian product, filtered down to 3 by the join's matching condition",
        ["6 total pairings, filtered down to 3", "9 total pairings, filtered down to 9 (nothing is removed)", "3 total pairings, filtered down to 1"],
    ),
    (
        "The introduction to join says it \"turns out to be built from two much simpler ideas Farah already half understands.\"\n\nWhat are those two ideas?",
        "Join is built from (1) pairing every row with every row (the cartesian product), and (2) throwing away the pairings that don't make sense (filtering by a matching condition).",
        "easy", "remember", "join-operator",
        "Pairing every row with every row, then throwing away the pairings that don't make sense",
        ["Sorting every row alphabetically, then removing duplicate rows", "Selecting certain rows, then projecting certain columns", "Merging two tables into one, then deleting the original two tables"],
    ),
]

SQL_TO_ALGEBRA = [
    (
        "Arjun's report needs to list restaurant names and zone names for restaurants in the \"Fast Food\" category, pulling data from both a Restaurants relation and a Zones relation.\n\nWhich clause of a structured query corresponds to relational algebra's selection (sigma)?",
        "The clause that narrows a query down using a condition, here \"category equals Fast Food,\" corresponds directly to selection, the sigma operation that keeps only the rows satisfying a test.",
        "easy", "remember", "sql-to-relational-algebra",
        "The clause that filters rows using a condition (a WHERE-style clause)",
        ["The clause that names which columns to return", "The clause that combines two relations on a shared value", "The clause that combines two similarly shaped relations"],
    ),
    (
        "Which clause of a structured query corresponds to relational algebra's projection (pi)?",
        "The clause that names which columns a query should return corresponds directly to projection, the operation that keeps certain columns and discards the rest.",
        "easy", "remember", "sql-to-relational-algebra",
        "The clause that specifies which columns to return (a SELECT-style clause)",
        ["The clause that filters rows using a condition", "The clause that pulls in a second relation via a shared value", "The clause that removes duplicate relations of the same shape"],
    ),
    (
        "Arjun's report needs zone_name, a column that lives in the Zones relation, not in Restaurants.\n\nWhich relational algebra operation corresponds to the clause that pulls Zones into the query based on a shared zone_id value?",
        "The clause pulling two relations together based on a shared value corresponds directly to the join operator, pairing rows from both relations and keeping only pairings where zone_id genuinely matches on both sides.",
        "medium", "apply", "sql-to-relational-algebra",
        "Join",
        ["Projection", "Selection", "Intersection"],
    ),
    (
        "Arjun's report is built in a specific order: first the Restaurants relation is filtered down to Fast Food rows, then those rows are joined with Zones, and only at the very end is the result trimmed to just name and zone_name.\n\nWhy does selection happen before the final projection, rather than the other way around?",
        "This mirrors how relational algebra expressions are built as a chain, one operation's result becoming the next operation's input. Filtering rows first (selection), then joining, then trimming columns last (projection) means each step works with only the data actually needed by the steps after it.",
        "hard", "analyze", "sql-to-relational-algebra",
        "Operations chain in sequence, each result feeding the next; filtering rows early keeps the following join and final trim working with only relevant data",
        ["Selection must always run last in every query, with no exceptions", "Projection can only be applied to a table that has never been joined", "The order of operations has no effect on the final result or the process"],
    ),
    (
        "Arjun learns to read any structured query as a small chain of operations before he even finishes typing it: find the columns being asked for, find the condition narrowing things down, find any second relation pulled in through a shared value, and find any combining of similarly shaped relations.\n\nWhich relational algebra concept does each of these four checks correspond to, respectively?",
        "Columns asked for → projection; a narrowing condition → selection; a second relation pulled in by a shared value → join; combining similarly shaped relations → set operations (union, intersection, difference).",
        "medium", "understand", "sql-to-relational-algebra",
        "Projection, selection, join, and set operations, respectively",
        ["Selection, projection, set operations, and join, respectively", "Join, set operations, projection, and selection, respectively", "All four checks correspond to the same operation: join"],
    ),
    (
        "Arjun's manager wants his report to stop looking like \"a black box that magically understands English sentences about mystery novels\" — the same phrase used earlier for Devika's reporting tool.\n\nWhat specifically lets Arjun see through any structured query before he even finishes typing it?",
        "Reading a query as a chain of the same handful of operations: the columns asked for are a projection, the narrowing condition is a selection, a second relation pulled in by a shared value is a join, and combining similarly shaped relations is a set operation.",
        "medium", "understand", "sql-to-relational-algebra",
        "Recognising the query's columns, condition, second relation, and combination as projection, selection, join, and set operations respectively",
        ["Memorising the exact SQL keywords without connecting them to any underlying operation", "Running the query first and reading the result before understanding what it does", "Asking the database administrator to explain each query individually"],
    ),
    (
        "The lesson claims relational algebra \"was worth learning before touching a real query language at all,\" describing it as not \"a separate, academic detour from the practical skill of writing queries.\"\n\nWhat does the lesson say relational algebra actually is, relative to writing queries?",
        "Relational algebra is the practical skill itself, described in its most precise and stripped-down form — once the underlying moves are familiar, learning a query language's exact wording becomes a matter of vocabulary, not relearning how to think about data.",
        "hard", "analyze", "sql-to-relational-algebra",
        "It is the practical skill of writing queries, in its most precise and stripped-down form, not a separate academic detour from it",
        ["It is a purely historical topic with no bearing on how queries are actually written today", "It is a stricter, slower alternative to writing real queries in production systems", "It is only useful for database administrators, not for anyone who writes queries"],
    ),
]

SYNTHESIS = [
    (
        "Devika's manager describes relational algebra as a toolkit where \"a table comes back out\" of every operation. Rohan later chains a selection (mystery books) into a projection (just the title column) with no extra glue code.\n\nWhich property of relational algebra makes that chaining possible?",
        "Closure: because every relational algebra operation always produces a relation as its output, and every operation accepts a relation as its input, the output of selection can be fed directly into projection as its next input.",
        "medium", "analyze", "what-is-relational-algebra",
        "Closure — every operation's output is itself a relation, so it can directly become another operation's input",
        ["Union-compatibility — every operation requires two relations of matching shape", "Normalization — every operation automatically removes redundant columns", "Indexing — every operation requires a pre-built index to run at all"],
    ),
    (
        "Meera's union of Coding Club and Robotics Club relies on union-compatibility, while Farah's join of Students and Enrollments relies on a shared student_id column, even though the two relations have entirely different columns otherwise.\n\nWhat is the key structural difference between when you'd use a set operation versus a join?",
        "Set operations (union, intersection, difference) compare relations that share the exact same shape and domain, column for column. Join instead combines relations with genuinely different columns, connecting them through a shared value rather than requiring identical shapes.",
        "hard", "analyze", "set-operations",
        "Set operations require the two relations to share the same shape and domain; join combines relations with different columns via a shared value",
        ["Set operations and join are two different names for exactly the same operation", "Set operations only work on a single relation; join always requires at least three relations", "Join requires union-compatible relations, while set operations do not"],
    ),
    (
        "In the join between Students and Enrollments, Meenal Rao appears twice in the final result, once for each course she is enrolled in.\n\nWhy does this happen, and is it a flaw in the join operation?",
        "This isn't a flaw — Meenal genuinely has two enrollment rows (PY101 and SQL201), so the cartesian-product-based join correctly produces one combined row per genuine pairing where the student_id values match, accurately reflecting that she really is taking two courses.",
        "medium", "apply", "join-operator",
        "It's not a flaw — Meenal genuinely has two enrollment rows, so join correctly produces one combined row for each real pairing",
        ["It is a flaw; join should always collapse a student down to exactly one row", "It happens only because the Students relation itself has a duplicate row for Meenal", "It happens because projection was applied before the join ran"],
    ),
    (
        "Arjun's report used selection (WHERE category = Fast Food) followed by a join (on zone_id) followed by a final projection (SELECT name, zone_name).\n\nIf Arjun instead needed \"every restaurant in either the Fast Food or the Healthy category, as one combined list,\" which relational algebra idea would that map to instead?",
        "\"Every restaurant in either category, as one combined list\" describes combining rows from two selections (or one relation filtered two ways) into a single list, which is exactly what a set operation, specifically union, is built for.",
        "medium", "apply", "sql-to-relational-algebra",
        "A set operation (union) combining the matching rows into one list",
        ["A join on the restaurant's category column", "A composite key built from category and zone_id", "A foreign key added to the Restaurants table"],
    ),
    (
        "Selection narrows rows, projection narrows columns, set operations compare relations of the same shape, and join combines relations of different shapes via a shared value.\n\nWhich single idea underlies all four of these being usable together in one query, one after another?",
        "Closure: because every one of these operations always takes a relation as input and always produces a relation as output, they can be freely combined and chained in any order a question requires, exactly as Arjun's report chained selection, then join, then projection.",
        "hard", "understand", "what-is-relational-algebra",
        "Closure — every operation's input and output are both relations, allowing any of them to be chained together",
        ["Union-compatibility — every operation requires the same column count as every other", "The system catalog — it silently rewrites every operation into SQL first", "The transaction manager — it decides which operation runs first in every query"],
    ),
]

SET1_SOURCES = [
    (WHAT_IS_RELATIONAL_ALGEBRA, 0),
    (SELECTION_PROJECTION, 0),
    (SET_OPERATIONS, 0),
    (JOIN_OPERATOR, 0),
    (SQL_TO_ALGEBRA, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    WHAT_IS_RELATIONAL_ALGEBRA[1:]
    + SELECTION_PROJECTION[1:]
    + SET_OPERATIONS[1:]
    + JOIN_OPERATOR[1:]
    + SQL_TO_ALGEBRA[1:]
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
            "topics": "database-foundations",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 1.4.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 1.4.2")
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
ws.title = "DBMS - MCQ - Unit 1.4"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 1 - Database Foundations/1.4 - Relational Algebra - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
