"""3.2 - Reading Data with SELECT - Coding Questions (26: SELECT basics,
aliases, DISTINCT, expressions, ORDER BY, LIMIT/OFFSET).

Dataset reuses the exact students/courses/enrollments rows from the lesson
markdown (content/DBMS/3 - SQL Essentials/3.2 - Reading Data with SELECT/),
so worked examples already confirm this environment's actual row order for
DISTINCT and plain SELECT without ORDER BY (verified against three separate
lesson-documented query outputs -- see comments below at each such question).

No local Postgres is available to execute solutions, so each question's
expected output is computed by a Python "oracle" run against the same
in-memory data used to generate preloadCode's INSERT statements (via
dbms_cqlib.sql_insert), rather than hand-typed.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

TOPIC = "sql-essentials"
SELECT_BASICS = "the-select-statement"
ALIASES = "column-aliases-and-table-aliases-with-as"
DISTINCT = "distinct-removing-duplicate-rows"
EXPRESSIONS = "expressions-and-calculated-columns"
SORTING = "sorting-results"
LIMITING = "limiting-results"

# ----------------------------- Dataset (matches lesson exactly) -----------------------------

STUDENT_COLUMNS = ["student_id", "full_name", "email", "city", "phone", "joined_on"]
STUDENTS = [
    dict(student_id=1, full_name="Ishaan Verma", email="ishaan.verma@example.com", city="Bengaluru", phone="9845011111", joined_on="2025-01-10"),
    dict(student_id=2, full_name="Meera Pillai", email="meera.pillai@example.com", city="Chennai", phone="9884022222", joined_on="2025-01-12"),
    dict(student_id=3, full_name="Arjun Bhat", email="arjun.bhat@example.com", city="Bengaluru", phone=None, joined_on="2025-01-15"),
    dict(student_id=4, full_name="Kavya Reddy", email="kavya.reddy@example.com", city="Pune", phone="9922033333", joined_on="2025-01-18"),
    dict(student_id=5, full_name="Rohan Joshi", email="rohan.joshi@example.com", city="Hyderabad", phone="9640044444", joined_on="2025-01-20"),
    dict(student_id=6, full_name="Sneha Gowda", email="sneha.gowda@example.com", city="Mysuru", phone=None, joined_on="2025-01-22"),
    dict(student_id=7, full_name="Aditya Kulkarni", email="aditya.kulkarni@example.com", city="Pune", phone="9822055555", joined_on="2025-01-25"),
    dict(student_id=8, full_name="Priya Subramaniam", email="priya.subramaniam@example.com", city="Chennai", phone="9884066666", joined_on="2025-01-28"),
]

COURSE_COLUMNS = ["course_id", "title", "department", "credits"]
COURSES = [
    dict(course_id=101, title="Database Systems", department="Computer Science", credits=4),
    dict(course_id=102, title="Data Structures", department="Computer Science", credits=4),
    dict(course_id=103, title="Linear Algebra", department="Mathematics", credits=3),
    dict(course_id=104, title="Discrete Mathematics", department="Mathematics", credits=3),
    dict(course_id=105, title="Microeconomics", department="Economics", credits=3),
]

ENROLLMENT_COLUMNS = ["enrollment_id", "student_id", "course_id", "enrolled_on", "grade"]
ENROLLMENTS = [
    dict(enrollment_id=1, student_id=1, course_id=101, enrolled_on="2025-02-01", grade="A"),
    dict(enrollment_id=2, student_id=1, course_id=103, enrolled_on="2025-02-01", grade="B"),
    dict(enrollment_id=3, student_id=2, course_id=105, enrolled_on="2025-02-03", grade="A"),
    dict(enrollment_id=4, student_id=3, course_id=101, enrolled_on="2025-02-05", grade=None),
    dict(enrollment_id=5, student_id=4, course_id=102, enrolled_on="2025-02-08", grade="B"),
    dict(enrollment_id=6, student_id=5, course_id=104, enrolled_on="2025-02-10", grade="A"),
    dict(enrollment_id=7, student_id=6, course_id=101, enrolled_on="2025-02-12", grade=None),
    dict(enrollment_id=8, student_id=7, course_id=105, enrolled_on="2025-02-15", grade="C"),
    dict(enrollment_id=9, student_id=8, course_id=103, enrolled_on="2025-02-18", grade="B"),
    dict(enrollment_id=10, student_id=2, course_id=102, enrolled_on="2025-02-20", grade=None),
]

STUDENTS_DDL = """
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    city TEXT,
    phone TEXT,
    joined_on DATE
);
"""

COURSES_DDL = """
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT,
    department TEXT,
    credits INTEGER
);
"""

ENROLLMENTS_DDL = """
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id),
    course_id INTEGER REFERENCES courses(course_id),
    enrolled_on DATE,
    grade TEXT
);
"""

STUDENTS_SQL = STUDENTS_DDL.strip("\n") + "\n\n" + sql_insert("students", STUDENT_COLUMNS, STUDENTS)
COURSES_SQL = COURSES_DDL.strip("\n") + "\n\n" + sql_insert("courses", COURSE_COLUMNS, COURSES)
ENROLLMENTS_SQL = (
    STUDENTS_DDL.strip("\n") + "\n\n" + sql_insert("students", STUDENT_COLUMNS, STUDENTS) + "\n\n"
    + COURSES_DDL.strip("\n") + "\n\n" + sql_insert("courses", COURSE_COLUMNS, COURSES) + "\n\n"
    + ENROLLMENTS_DDL.strip("\n") + "\n\n" + sql_insert("enrollments", ENROLLMENT_COLUMNS, ENROLLMENTS)
)

STUDENTS_SCHEMA_LINES = [
    "students(student_id INTEGER PK, full_name TEXT, email TEXT, city TEXT, phone TEXT, joined_on DATE) -- 8 rows, phone is NULL for two students",
]
COURSES_SCHEMA_LINES = [
    "courses(course_id INTEGER PK, title TEXT, department TEXT, credits INTEGER) -- 5 rows",
]
ENROLLMENTS_SCHEMA_LINES = [
    "students(student_id INTEGER PK, full_name TEXT, email TEXT, city TEXT, phone TEXT, joined_on DATE) -- 8 rows",
    "courses(course_id INTEGER PK, title TEXT, department TEXT, credits INTEGER) -- 5 rows",
    "enrollments(enrollment_id INTEGER PK, student_id INTEGER FK, course_id INTEGER FK, enrolled_on DATE, grade TEXT) -- 10 rows, grade is NULL for three enrollments",
]

Q = []

# ==================== the-select-statement ====================

Q.append(dict(
    title="Orientation Folder List", difficulty="Easy", topics=TOPIC, subTopics=SELECT_BASICS,
    bloomTaxonomy="remember",
    prose="Karthik has just been given read access to the college's student records database. "
          "The admissions coordinator wants the full students list, every column, every student, "
          "for the orientation folder.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=STUDENT_COLUMNS,
    solution_sql="SELECT * FROM students;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [tuple(s[c] for c in STUDENT_COLUMNS) for s in students],
    hints="SELECT * FROM a table returns every column in the order the table was created, and every row.",
))

Q.append(dict(
    title="Seating Arrangement Sheet", difficulty="Easy", topics=TOPIC, subTopics=SELECT_BASICS,
    bloomTaxonomy="apply",
    prose="A few minutes later the coordinator asks a narrower question: just names and cities, "
          "for the seating arrangement, nothing else from the students table.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "city"],
    solution_sql="SELECT full_name, city FROM students;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [(s["full_name"], s["city"]) for s in students],
    hints="Name only the columns you need, separated by commas, in the order you want them to appear.",
))

Q.append(dict(
    title="Course Catalog Preview", difficulty="Easy", topics=TOPIC, subTopics=SELECT_BASICS,
    bloomTaxonomy="apply",
    prose="The department office wants a course catalog preview: every course's title, department, "
          "and credit count, but not the internal course_id.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "department", "credits"],
    solution_sql="SELECT title, department, credits FROM courses;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [(c["title"], c["department"], c["credits"]) for c in courses],
    hints="List only the three columns asked for; course_id is not one of them.",
))

Q.append(dict(
    title="City First, Name Second", difficulty="Medium", topics=TOPIC, subTopics=SELECT_BASICS,
    bloomTaxonomy="analyze",
    prose="A volunteer wants the same student data as the seating sheet, but with city listed "
          "before the student's name in each row, since that is how their printed form is laid out.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["city", "full_name"],
    solution_sql="SELECT city, full_name FROM students;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [(s["city"], s["full_name"]) for s in students],
    hints="The order columns appear in the SELECT list is exactly the order they appear in the result, "
          "regardless of the order the table itself was created in.",
))

Q.append(dict(
    title="Enrollment Reference Numbers", difficulty="Medium", topics=TOPIC, subTopics=SELECT_BASICS,
    bloomTaxonomy="apply",
    prose="An auditor needs a plain list of which student enrolled in which course: just the "
          "enrollment_id, student_id, and course_id from the enrollments table, leaving out the "
          "enrollment date and grade.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id"],
    solution_sql="SELECT enrollment_id, student_id, course_id FROM enrollments;",
    data=dict(enrollments=ENROLLMENTS),
    oracle=lambda enrollments: [(e["enrollment_id"], e["student_id"], e["course_id"]) for e in enrollments],
    hints="Only three of the five enrollments columns are wanted here; name exactly those three.",
))

# ==================== column-aliases-and-table-aliases-with-as ====================

Q.append(dict(
    title="Dean's Office Summary", difficulty="Easy", topics=TOPIC, subTopics=ALIASES,
    bloomTaxonomy="apply",
    prose="Divya is preparing a one-page summary for the Dean's office and wants the raw "
          "full_name and city headers replaced with the friendlier labels student_name and location, "
          "without changing any of the underlying data.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_name", "location"],
    solution_sql="SELECT full_name AS student_name, city AS location FROM students;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [(s["full_name"], s["city"]) for s in students],
    hints='Put AS followed by the label you want directly after each column name: full_name AS student_name.',
))

Q.append(dict(
    title="Course List With Friendly Headers", difficulty="Easy", topics=TOPIC, subTopics=ALIASES,
    bloomTaxonomy="apply",
    prose="The catalog page needs course title and credits shown under the headers course_title "
          "and credit_count instead of the raw column names.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["course_title", "credit_count"],
    solution_sql="SELECT title AS course_title, credits AS credit_count FROM courses;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [(c["title"], c["credits"]) for c in courses],
    hints="AS renames a column in the output only; the courses table itself is untouched.",
))

Q.append(dict(
    title="Alias Without the AS Keyword", difficulty="Medium", topics=TOPIC, subTopics=ALIASES,
    bloomTaxonomy="understand",
    prose="Divya's colleague writes the same student_name / location summary she built earlier, "
          "but wants to see it written using the shorter form that drops the word AS entirely, "
          "just the alias placed right after the column name.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_name", "location"],
    solution_sql="SELECT full_name student_name, city location FROM students;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [(s["full_name"], s["city"]) for s in students],
    hints="AS is optional in PostgreSQL: writing full_name student_name works exactly like "
          "full_name AS student_name.",
))

Q.append(dict(
    title="Full Name and Email Address, Through a Table Alias", difficulty="Hard", topics=TOPIC, subTopics=ALIASES,
    bloomTaxonomy="apply",
    prose="The Dean's office wants a sheet with headers exactly 'Full Name' and 'Email Address' "
          "(capitalised, with a space), built from the students table given a short table alias s "
          "along the way.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["Full Name", "Email Address"],
    solution_sql='SELECT s.full_name AS "Full Name", s.email AS "Email Address" FROM students AS s;',
    data=dict(students=STUDENTS),
    oracle=lambda students: [(s["full_name"], s["email"]) for s in students],
    hints='An alias containing a space needs double quotes: AS "Full Name". students AS s gives the '
          "table the short handle s, usable as s.full_name.",
))

# ==================== distinct-removing-duplicate-rows ====================

# Row order below matches the lesson's own documented output exactly (first-occurrence
# order = table/insertion order for DISTINCT without ORDER BY, verified against three
# separate worked examples in 03_distinct_removing_duplicate_rows.md on this dataset).

Q.append(dict(
    title="Which Cities Do Students Come From", difficulty="Easy", topics=TOPIC, subTopics=DISTINCT,
    bloomTaxonomy="apply",
    prose="Simran wants to know which cities the students come from, listed once each, not one row "
          "per student.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["city"],
    solution_sql="SELECT DISTINCT city FROM students;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [(c,) for c in dict.fromkeys(s["city"] for s in students)],
    hints="DISTINCT collapses repeated values in the result down to one appearance each.",
))

Q.append(dict(
    title="Which Departments Offer Courses", difficulty="Easy", topics=TOPIC, subTopics=DISTINCT,
    bloomTaxonomy="apply",
    prose="The registrar wants to know which departments the college currently offers courses in, "
          "listed once each, with no repeats.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["department"],
    solution_sql="SELECT DISTINCT department FROM courses;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [(d,) for d in dict.fromkeys(c["department"] for c in courses)],
    hints="DISTINCT on a single column keeps only the unique values from that column.",
))

Q.append(dict(
    title="Unique Department and Credit-Load Combinations", difficulty="Medium", topics=TOPIC, subTopics=DISTINCT,
    bloomTaxonomy="analyze",
    prose="Simran now wants to know which department-and-credit-load combinations actually exist "
          "among the college's courses, not a row for every course.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["department", "credits"],
    solution_sql="SELECT DISTINCT department, credits FROM courses;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [pair for pair in dict.fromkeys((c["department"], c["credits"]) for c in courses)],
    hints="Given more than one column, DISTINCT keeps a row only if the whole combination of values "
          "is unique, not just one column by itself.",
))

Q.append(dict(
    title="Every Grade Value on Record, Including the Ungraded", difficulty="Hard", topics=TOPIC, subTopics=DISTINCT,
    bloomTaxonomy="analyze",
    prose="An advisor wants a list of every distinct grade value that appears anywhere in the "
          "enrollments table, in ascending order, with ungraded enrollments (a NULL grade) counted "
          "as a single value rather than listed once per ungraded enrollment.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["grade"],
    solution_sql="SELECT DISTINCT grade FROM enrollments ORDER BY grade;",
    data=dict(enrollments=ENROLLMENTS),
    oracle=lambda enrollments: [
        (g,) for g in sorted(dict.fromkeys(e["grade"] for e in enrollments), key=lambda v: (v is None, v))
    ],
    hints="DISTINCT treats every NULL grade as the same value, so all of them collapse into one row. "
          "PostgreSQL's default ascending sort puts NULL last.",
))

# ==================== expressions-and-calculated-columns ====================

Q.append(dict(
    title="Workload Score", difficulty="Easy", topics=TOPIC, subTopics=EXPRESSIONS,
    bloomTaxonomy="apply",
    prose="Nikhil's course catalog page needs a 'workload score' for each course: double the "
          "credit value, shown alongside the course's title and its real credits.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "credits", "double_credits"],
    solution_sql="SELECT title, credits, credits * 2 AS double_credits FROM courses;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [(c["title"], c["credits"], c["credits"] * 2) for c in courses],
    hints="Write the arithmetic directly in the SELECT list, exactly where a column name would go, "
          "and name it with AS.",
))

Q.append(dict(
    title="Course Label", difficulty="Easy", topics=TOPIC, subTopics=EXPRESSIONS,
    bloomTaxonomy="apply",
    prose="Nikhil also needs a combined label for each course, like 'Computer Science: Database "
          "Systems', built from the department and title joined by a colon and a space.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["course_label"],
    solution_sql="SELECT department || ': ' || title AS course_label FROM courses;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [(f'{c["department"]}: {c["title"]}',) for c in courses],
    hints="The || operator glues text together, left to right; ': ' is a fixed literal string, "
          "not a column.",
))

Q.append(dict(
    title="Contact Hours", difficulty="Medium", topics=TOPIC, subTopics=EXPRESSIONS,
    bloomTaxonomy="apply",
    prose="The catalog page needs a 'credit hours per week' figure, assuming each credit corresponds "
          "to roughly 15 contact hours across a term, shown alongside the course title.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "contact_hours"],
    solution_sql="SELECT title, credits * 15 AS contact_hours FROM courses;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [(c["title"], c["credits"] * 15) for c in courses],
    hints="contact_hours is credits multiplied by 15, computed fresh for every row.",
))

Q.append(dict(
    title="Full Catalog Row With Label and Workload", difficulty="Medium", topics=TOPIC, subTopics=EXPRESSIONS,
    bloomTaxonomy="analyze",
    prose="Nikhil wants everything on one line per course: course_id and title straight from the "
          "table, credits shown plainly, the doubled workload score, and the combined department-"
          "and-title label, all in a single query.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["course_id", "title", "credits", "double_credits", "course_label"],
    solution_sql="SELECT course_id, title, credits, credits * 2 AS double_credits, "
                 "department || ': ' || title AS course_label FROM courses;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["course_id"], c["title"], c["credits"], c["credits"] * 2, f'{c["department"]}: {c["title"]}')
        for c in courses
    ],
    hints="A single SELECT list can freely mix plain columns and expressions; nothing stops you from "
          "having several of each.",
))

Q.append(dict(
    title="Even or Odd Credit Load", difficulty="Hard", topics=TOPIC, subTopics=EXPRESSIONS,
    bloomTaxonomy="analyze",
    prose="A scheduling tool needs to know, for each course, the remainder when its credit value is "
          "divided by 2, so it can tell even-credit courses apart from odd-credit ones later.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "credits", "credits_mod_2"],
    solution_sql="SELECT title, credits, credits % 2 AS credits_mod_2 FROM courses;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [(c["title"], c["credits"], c["credits"] % 2) for c in courses],
    hints="% is the remainder operator; it works inside a SELECT list exactly like +, -, *, and /.",
))

# ==================== sorting-results ====================

Q.append(dict(
    title="Alphabetical Roster", difficulty="Easy", topics=TOPIC, subTopics=SORTING,
    bloomTaxonomy="apply",
    prose="Rhea wants the students listed alphabetically by name for a printed orientation roster, "
          "so volunteers can find a name quickly.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "city"],
    solution_sql="SELECT full_name, city FROM students ORDER BY full_name;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["city"]) for s in sorted(students, key=lambda s: s["full_name"])
    ],
    hints="ORDER BY with just a column name sorts ascending by default: A to Z for text.",
))

Q.append(dict(
    title="Most Recent Joiners First", difficulty="Easy", topics=TOPIC, subTopics=SORTING,
    bloomTaxonomy="apply",
    prose="Rhea wants a 'welcome our latest students' notice with the newest joiners at the top.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "joined_on"],
    solution_sql="SELECT full_name, joined_on FROM students ORDER BY joined_on DESC;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["joined_on"])
        for s in sorted(students, key=lambda s: s["joined_on"], reverse=True)
    ],
    hints="DESC after the column reverses the sort direction, so the most recent date comes first.",
))

Q.append(dict(
    title="Grouped by City, Alphabetical Within", difficulty="Medium", topics=TOPIC, subTopics=SORTING,
    bloomTaxonomy="analyze",
    prose="Rhea wants students grouped by city, and within each city listed alphabetically by name, "
          "so a volunteer working one city's desk can find their group without scrolling past others.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "city"],
    solution_sql="SELECT full_name, city FROM students ORDER BY city, full_name;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["city"])
        for s in sorted(students, key=lambda s: (s["city"], s["full_name"]))
    ],
    hints="ORDER BY sorts by the first column listed, then uses the second column only to break ties "
          "within groups that share the same first value.",
))

Q.append(dict(
    title="Newest Joiner First Within Each City", difficulty="Medium", topics=TOPIC, subTopics=SORTING,
    bloomTaxonomy="analyze",
    prose="The office wants students grouped by city as before, but this time with the most "
          "recently joined student in each city appearing first within that city's group.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "city", "joined_on"],
    solution_sql="SELECT full_name, city, joined_on FROM students ORDER BY city, joined_on DESC;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["city"], s["joined_on"])
        for s in sorted(
            sorted(students, key=lambda s: s["joined_on"], reverse=True),
            key=lambda s: s["city"],
        )
    ],
    hints="Each column in an ORDER BY list can carry its own direction: city stays ascending while "
          "joined_on is reversed with DESC.",
))

Q.append(dict(
    title="Courses Ranked by Workload, Then Name", difficulty="Hard", topics=TOPIC, subTopics=SORTING,
    bloomTaxonomy="analyze",
    prose="The department wants every course ranked by credit load from heaviest to lightest, and "
          "among courses tied on credits, ordered alphabetically by title.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "department", "credits"],
    solution_sql="SELECT title, department, credits FROM courses ORDER BY credits DESC, title;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["department"], c["credits"])
        for c in sorted(sorted(courses, key=lambda c: c["title"]), key=lambda c: c["credits"], reverse=True)
    ],
    hints="Sort by credits descending first; title, listed second with no DESC, breaks ties "
          "alphabetically.",
))

# ==================== limiting-results ====================

Q.append(dict(
    title="Recent Enrollments Widget", difficulty="Easy", topics=TOPIC, subTopics=LIMITING,
    bloomTaxonomy="apply",
    prose="Tanvi's dashboard widget only has room for five rows: the five most recently enrolled "
          "records, newest first.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["student_id", "course_id", "enrolled_on"],
    solution_sql="SELECT student_id, course_id, enrolled_on FROM enrollments "
                 "ORDER BY enrolled_on DESC, enrollment_id LIMIT 5;",
    data=dict(enrollments=ENROLLMENTS),
    oracle=lambda enrollments: [
        (e["student_id"], e["course_id"], e["enrolled_on"])
        for e in sorted(
            sorted(enrollments, key=lambda e: e["enrollment_id"]),
            key=lambda e: e["enrolled_on"], reverse=True,
        )[:5]
    ],
    hints="Sort newest first with ORDER BY ... DESC, then LIMIT 5 keeps only the first five rows of "
          "that already-sorted result.",
))

Q.append(dict(
    title="Page 2 of Enrollments", difficulty="Medium", topics=TOPIC, subTopics=LIMITING,
    bloomTaxonomy="apply",
    prose="An admin screen shows enrollments five at a time, newest first. Page 1 showed the five "
          "most recent; now show exactly what page 2 should display.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["student_id", "course_id", "enrolled_on"],
    solution_sql="SELECT student_id, course_id, enrolled_on FROM enrollments "
                 "ORDER BY enrolled_on DESC, enrollment_id LIMIT 5 OFFSET 5;",
    data=dict(enrollments=ENROLLMENTS),
    oracle=lambda enrollments: [
        (e["student_id"], e["course_id"], e["enrolled_on"])
        for e in sorted(
            sorted(enrollments, key=lambda e: e["enrollment_id"]),
            key=lambda e: e["enrolled_on"], reverse=True,
        )[5:10]
    ],
    hints="OFFSET 5 skips the five rows page 1 already showed, then LIMIT 5 collects the next five "
          "from the same sorted order.",
))

Q.append(dict(
    title="Top 3 Highest-Workload Courses", difficulty="Medium", topics=TOPIC, subTopics=LIMITING,
    bloomTaxonomy="apply",
    prose="The department office wants a 'highest workload' preview: the three courses with the "
          "most credits, and among courses tied on credits, the one whose title comes first "
          "alphabetically.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "credits"],
    solution_sql="SELECT title, credits FROM courses ORDER BY credits DESC, title LIMIT 3;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["credits"])
        for c in sorted(sorted(courses, key=lambda c: c["title"]), key=lambda c: c["credits"], reverse=True)[:3]
    ],
    hints="LIMIT only means something reliable once ORDER BY has decided what 'top' refers to; sort "
          "first, then trim to 3.",
))

Q.append(dict(
    title="Third Through Fifth Earliest Enrollments", difficulty="Hard", topics=TOPIC, subTopics=LIMITING,
    bloomTaxonomy="analyze",
    prose="An auditor reviewing early enrollment activity wants the third-, fourth-, and "
          "fifth-earliest enrollments by date, skipping the two earliest.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["student_id", "course_id", "enrolled_on"],
    solution_sql="SELECT student_id, course_id, enrolled_on FROM enrollments "
                 "ORDER BY enrolled_on, enrollment_id LIMIT 3 OFFSET 2;",
    data=dict(enrollments=ENROLLMENTS),
    oracle=lambda enrollments: [
        (e["student_id"], e["course_id"], e["enrolled_on"])
        for e in sorted(
            sorted(enrollments, key=lambda e: e["enrollment_id"]),
            key=lambda e: e["enrolled_on"],
        )[2:5]
    ],
    hints="Ascending ORDER BY (the default) puts the earliest date first; OFFSET 2 skips the two "
          "earliest, and LIMIT 3 then takes the next three.",
))

assert len(Q) == 27, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/3.2 - Reading Data with SELECT - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
