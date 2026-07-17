"""3.3 - Filtering Data - Coding Questions (29: WHERE, comparison operators,
logical operators, pattern matching (LIKE/ILIKE), NULL handling).

Dataset reuses the exact students/courses/instructors/enrollments rows from
the lesson markdown (content/DBMS/3 - SQL Essentials/3.3 - Filtering Data/).
Note this chapter's courses table differs slightly from 3.2's dataset
(Microeconomics is 2 credits here, not 3) -- values below match this
chapter's lesson text exactly, not 3.2's.

Every solution query includes an explicit ORDER BY (ORDER BY was already
taught in 3.2, so this is fair game here), which fully removes PostgreSQL's
unspecified-tie-order risk that chapter 3.2 had to reason around carefully.
Expected output is computed by a Python oracle run against the same in-memory
data used to generate preloadCode's INSERT statements (see dbms_cqlib.py).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

TOPIC = "sql-essentials"
WHERE_CLAUSE = "the-where-clause"
COMPARISON = "comparison-operators"
LOGICAL = "logical-operators"
PATTERN = "pattern-matching"
NULLS = "working-with-null"

# ----------------------------- Dataset (matches lesson exactly) -----------------------------

STUDENT_COLUMNS = ["student_id", "full_name", "email", "city", "phone", "joined_on"]
STUDENTS = [
    dict(student_id=1, full_name="Omkar Rane", email="omkar.rane@campusmail.edu", city="Bengaluru", phone="9845011111", joined_on="2025-01-10"),
    dict(student_id=2, full_name="Neha Sharma", email="neha.sharma@campusmail.edu", city="Mysuru", phone=None, joined_on="2025-01-12"),
    dict(student_id=3, full_name="Varun Nair", email="varun.nair@gmail.com", city="Chennai", phone="9845022222", joined_on="2025-01-15"),
    dict(student_id=4, full_name="Siddharth Rao", email="siddharth.rao@campusmail.edu", city="Hyderabad", phone="9845033333", joined_on="2025-01-18"),
    dict(student_id=5, full_name="Yusuf Khan", email="yusuf.khan@gmail.com", city="Pune", phone=None, joined_on="2025-01-20"),
    dict(student_id=6, full_name="Ishita Menon", email="ishita.menon@campusmail.edu", city="Bengaluru", phone="9845044444", joined_on="2025-01-22"),
    dict(student_id=7, full_name="Rahul Verma", email="rahul.verma@gmail.com", city="Chennai", phone="9845055555", joined_on="2025-01-25"),
    dict(student_id=8, full_name="Sanya Iyer", email="sanya.iyer@campusmail.edu", city="Mysuru", phone=None, joined_on="2025-01-28"),
]

COURSE_COLUMNS = ["course_id", "title", "department", "credits"]
COURSES = [
    dict(course_id=101, title="Database Systems", department="Computer Science", credits=4),
    dict(course_id=102, title="Data Structures", department="Computer Science", credits=4),
    dict(course_id=103, title="Linear Algebra", department="Mathematics", credits=3),
    dict(course_id=104, title="Discrete Mathematics", department="Mathematics", credits=3),
    dict(course_id=105, title="Microeconomics", department="Economics", credits=2),
]

ENROLLMENT_COLUMNS = ["enrollment_id", "student_id", "course_id", "enrolled_on", "grade"]
ENROLLMENTS = [
    dict(enrollment_id=1, student_id=1, course_id=101, enrolled_on="2025-02-01", grade="A"),
    dict(enrollment_id=2, student_id=1, course_id=103, enrolled_on="2025-02-01", grade="B+"),
    dict(enrollment_id=3, student_id=2, course_id=101, enrolled_on="2025-02-02", grade=None),
    dict(enrollment_id=4, student_id=3, course_id=102, enrolled_on="2025-02-03", grade="A-"),
    dict(enrollment_id=5, student_id=3, course_id=105, enrolled_on="2025-02-03", grade=None),
    dict(enrollment_id=6, student_id=4, course_id=104, enrolled_on="2025-02-04", grade="B"),
    dict(enrollment_id=7, student_id=5, course_id=101, enrolled_on="2025-02-05", grade=None),
    dict(enrollment_id=8, student_id=6, course_id=102, enrolled_on="2025-02-06", grade="A"),
    dict(enrollment_id=9, student_id=7, course_id=103, enrolled_on="2025-02-07", grade="C+"),
    dict(enrollment_id=10, student_id=8, course_id=105, enrolled_on="2025-02-08", grade="B-"),
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
    "students(student_id INTEGER PK, full_name TEXT, email TEXT, city TEXT, phone TEXT, joined_on DATE) -- 8 rows, phone is NULL for three students",
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

# ==================== the-where-clause ====================

Q.append(dict(
    title="Computer Science Offerings", difficulty="Easy", topics=TOPIC, subTopics=WHERE_CLAUSE,
    bloomTaxonomy="apply",
    prose="Omkar is pulling together a report of Computer Science offerings for his advisor and "
          "does not want to scroll past mathematics and economics courses to find them.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "department", "credits"],
    solution_sql="SELECT title, department, credits FROM courses "
                 "WHERE department = 'Computer Science' ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["department"], c["credits"])
        for c in sorted(courses, key=lambda c: c["course_id"])
        if c["department"] == "Computer Science"
    ],
    hints="WHERE tests every row against a condition and keeps only the rows where it is true.",
))

Q.append(dict(
    title="Students Based in Bengaluru", difficulty="Easy", topics=TOPIC, subTopics=WHERE_CLAUSE,
    bloomTaxonomy="apply",
    prose="Write a query that returns the full_name and city of every student based in Bengaluru.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "city"],
    solution_sql="SELECT full_name, city FROM students WHERE city = 'Bengaluru' ORDER BY student_id;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["city"])
        for s in sorted(students, key=lambda s: s["student_id"])
        if s["city"] == "Bengaluru"
    ],
    hints="An equality condition, city = 'Bengaluru', is the simplest kind of test WHERE can hold.",
))

Q.append(dict(
    title="Chennai Students, Alphabetically", difficulty="Medium", topics=TOPIC, subTopics=WHERE_CLAUSE,
    bloomTaxonomy="analyze",
    prose="Return the full_name and city of every student based in Chennai, sorted alphabetically "
          "by name.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "city"],
    solution_sql="SELECT full_name, city FROM students WHERE city = 'Chennai' ORDER BY full_name;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["city"])
        for s in sorted([s for s in students if s["city"] == "Chennai"], key=lambda s: s["full_name"])
    ],
    hints="Filtering happens before sorting: the database first narrows to Chennai residents, then "
          "arranges those survivors alphabetically.",
))

Q.append(dict(
    title="Mathematics Department Courses", difficulty="Medium", topics=TOPIC, subTopics=WHERE_CLAUSE,
    bloomTaxonomy="apply",
    prose="The Mathematics department wants a list of its own course titles and credit values only.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "credits"],
    solution_sql="SELECT title, credits FROM courses WHERE department = 'Mathematics' ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["credits"])
        for c in sorted(courses, key=lambda c: c["course_id"])
        if c["department"] == "Mathematics"
    ],
    hints="Filter on department, then select only the two columns actually asked for.",
))

Q.append(dict(
    title="Enrollments in Database Systems", difficulty="Hard", topics=TOPIC, subTopics=WHERE_CLAUSE,
    bloomTaxonomy="analyze",
    prose="The Database Systems instructor wants to see every enrollment recorded for their course "
          "(course_id 101): which student, and what grade so far.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["student_id", "course_id", "grade"],
    solution_sql="SELECT student_id, course_id, grade FROM enrollments WHERE course_id = 101 "
                 "ORDER BY enrollment_id;",
    data=dict(enrollments=ENROLLMENTS),
    oracle=lambda enrollments: [
        (e["student_id"], e["course_id"], e["grade"])
        for e in sorted(enrollments, key=lambda e: e["enrollment_id"])
        if e["course_id"] == 101
    ],
    hints="A WHERE condition can test a foreign-key-style column like course_id exactly the same "
          "way it tests any other column.",
))

# ==================== comparison-operators ====================

Q.append(dict(
    title="Courses Worth More Than Three Credits", difficulty="Easy", topics=TOPIC, subTopics=COMPARISON,
    bloomTaxonomy="apply",
    prose="Neha wants to see which courses cost more than the standard three-credit load.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "credits"],
    solution_sql="SELECT title, credits FROM courses WHERE credits > 3 ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["credits"]) for c in sorted(courses, key=lambda c: c["course_id"]) if c["credits"] > 3
    ],
    hints="> keeps only rows whose value is strictly greater than the number given.",
))

Q.append(dict(
    title="Courses Worth At Least Three Credits", difficulty="Easy", topics=TOPIC, subTopics=COMPARISON,
    bloomTaxonomy="apply",
    prose="This time Neha wants three-credit courses included too, not just anything above three.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "credits"],
    solution_sql="SELECT title, credits FROM courses WHERE credits >= 3 ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["credits"]) for c in sorted(courses, key=lambda c: c["course_id"]) if c["credits"] >= 3
    ],
    hints=">= includes the boundary value itself, unlike a plain >.",
))

Q.append(dict(
    title="Enrollments From the Opening Days of Registration", difficulty="Medium", topics=TOPIC, subTopics=COMPARISON,
    bloomTaxonomy="analyze",
    prose="Neha wants to see which enrollments were recorded before 2025-02-04, the opening days "
          "of registration, sorted from earliest to latest.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "enrolled_on"],
    solution_sql="SELECT enrollment_id, student_id, course_id, enrolled_on FROM enrollments "
                 "WHERE enrolled_on < '2025-02-04' ORDER BY enrolled_on, enrollment_id;",
    data=dict(enrollments=ENROLLMENTS),
    oracle=lambda enrollments: [
        (e["enrollment_id"], e["student_id"], e["course_id"], e["enrolled_on"])
        for e in sorted(
            [e for e in enrollments if e["enrolled_on"] < "2025-02-04"],
            key=lambda e: (e["enrolled_on"], e["enrollment_id"]),
        )
    ],
    hints="Dates compare exactly the way numbers do: earlier dates are 'smaller' than later ones.",
))

Q.append(dict(
    title="Every Course Except Mathematics", difficulty="Medium", topics=TOPIC, subTopics=COMPARISON,
    bloomTaxonomy="apply",
    prose="Return the title and department of every course that is not offered by the Mathematics "
          "department.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "department"],
    solution_sql="SELECT title, department FROM courses WHERE department <> 'Mathematics' ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["department"])
        for c in sorted(courses, key=lambda c: c["course_id"])
        if c["department"] != "Mathematics"
    ],
    hints="<> and != both mean not-equal-to; either spelling works in PostgreSQL.",
))

Q.append(dict(
    title="Students From M Onward, Alphabetically", difficulty="Hard", topics=TOPIC, subTopics=COMPARISON,
    bloomTaxonomy="analyze",
    prose="An examiner splitting the roster into two halves wants every student whose name sorts "
          "at 'M' or later in the alphabet.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name"],
    solution_sql="SELECT full_name FROM students WHERE full_name >= 'M' ORDER BY full_name;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"],) for s in sorted(students, key=lambda s: s["full_name"]) if s["full_name"] >= "M"
    ],
    hints="Text compares character by character in alphabetical order, so >= 'M' asks whether a "
          "name sorts at M or after.",
))

Q.append(dict(
    title="The Lowest-Credit Course", difficulty="Hard", topics=TOPIC, subTopics=COMPARISON,
    bloomTaxonomy="apply",
    prose="Find the course with the lowest credit value using a comparison operator rather than "
          "sorting and limiting.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "credits"],
    solution_sql="SELECT title, credits FROM courses WHERE credits <= 2 ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["credits"]) for c in sorted(courses, key=lambda c: c["course_id"]) if c["credits"] <= 2
    ],
    hints="Since the lowest credit value here is 2, credits <= 2 captures exactly the courses at "
          "that value.",
))

# ==================== logical-operators ====================

Q.append(dict(
    title="Four-Credit Computer Science Courses", difficulty="Easy", topics=TOPIC, subTopics=LOGICAL,
    bloomTaxonomy="apply",
    prose="Return every course that is both in the Computer Science department and worth exactly "
          "four credits.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "department", "credits"],
    solution_sql="SELECT title, department, credits FROM courses "
                 "WHERE department = 'Computer Science' AND credits = 4 ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["department"], c["credits"])
        for c in sorted(courses, key=lambda c: c["course_id"])
        if c["department"] == "Computer Science" and c["credits"] == 4
    ],
    hints="AND keeps a row only when every condition attached to it is true.",
))

Q.append(dict(
    title="Mathematics or Economics Courses", difficulty="Easy", topics=TOPIC, subTopics=LOGICAL,
    bloomTaxonomy="apply",
    prose="Return the title and department of every course that belongs to Mathematics or "
          "Economics.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "department"],
    solution_sql="SELECT title, department FROM courses "
                 "WHERE department = 'Mathematics' OR department = 'Economics' ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["department"])
        for c in sorted(courses, key=lambda c: c["course_id"])
        if c["department"] in ("Mathematics", "Economics")
    ],
    hints="OR keeps a row when at least one of the joined conditions is true.",
))

Q.append(dict(
    title="Varun's Shortlist, Written the Way He First Tried It", difficulty="Medium", topics=TOPIC, subTopics=LOGICAL,
    bloomTaxonomy="analyze",
    prose="Varun wants Computer Science courses worth more than three credits, or any Economics "
          "course, and writes his WHERE clause with AND and OR but no parentheses. Reproduce "
          "exactly what that ungrouped clause actually returns.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "department", "credits"],
    solution_sql="SELECT title, department, credits FROM courses "
                 "WHERE department = 'Computer Science' AND credits > 3 OR department = 'Economics' "
                 "ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["department"], c["credits"])
        for c in sorted(courses, key=lambda c: c["course_id"])
        if (c["department"] == "Computer Science" and c["credits"] > 3) or c["department"] == "Economics"
    ],
    hints="SQL evaluates AND before OR when neither is grouped by parentheses, the same way "
          "multiplication is evaluated before addition.",
))

Q.append(dict(
    title="Varun's Shortlist, Fixed With Parentheses", difficulty="Medium", topics=TOPIC, subTopics=LOGICAL,
    bloomTaxonomy="apply",
    prose="Fix Varun's shortlist so Microeconomics no longer sneaks in under its two credits: "
          "Computer Science or Economics courses, but only the ones worth more than three credits.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "department", "credits"],
    solution_sql="SELECT title, department, credits FROM courses "
                 "WHERE (department = 'Computer Science' OR department = 'Economics') AND credits > 3 "
                 "ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["department"], c["credits"])
        for c in sorted(courses, key=lambda c: c["course_id"])
        if (c["department"] in ("Computer Science", "Economics")) and c["credits"] > 3
    ],
    hints="Parentheses force the OR to be settled first, so AND then checks the credit requirement "
          "against that combined result.",
))

Q.append(dict(
    title="Courses at Three Credits or Fewer", difficulty="Hard", topics=TOPIC, subTopics=LOGICAL,
    bloomTaxonomy="analyze",
    prose="Return every course whose credit value is not greater than three, phrased using NOT "
          "rather than a <= comparison.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "credits"],
    solution_sql="SELECT title, credits FROM courses WHERE NOT credits > 3 ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["credits"]) for c in sorted(courses, key=lambda c: c["course_id"]) if not (c["credits"] > 3)
    ],
    hints="NOT flips a condition's truth value: rows that would have matched credits > 3 are "
          "excluded, and rows that would not have matched are included instead.",
))

Q.append(dict(
    title="Heavier Mathematics or Computer Science Courses", difficulty="Hard", topics=TOPIC, subTopics=LOGICAL,
    bloomTaxonomy="apply",
    prose="Return courses from departments that are Mathematics or Computer Science, restricted to "
          "courses worth at least four credits, using parentheses so the grouping is unambiguous.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["title", "department", "credits"],
    solution_sql="SELECT title, department, credits FROM courses "
                 "WHERE (department = 'Mathematics' OR department = 'Computer Science') AND credits >= 4 "
                 "ORDER BY course_id;",
    data=dict(courses=COURSES),
    oracle=lambda courses: [
        (c["title"], c["department"], c["credits"])
        for c in sorted(courses, key=lambda c: c["course_id"])
        if (c["department"] in ("Mathematics", "Computer Science")) and c["credits"] >= 4
    ],
    hints="Both Mathematics courses carry only three credits, so they should be excluded once the "
          "parentheses group the department check before the credit check applies to it.",
))

# ==================== pattern-matching ====================

Q.append(dict(
    title="College-Issued Email Addresses", difficulty="Easy", topics=TOPIC, subTopics=PATTERN,
    bloomTaxonomy="apply",
    prose="Siddharth needs everyone still using their college-issued email address, ahead of a "
          "migration to a new mail provider, regardless of what the local part of the address "
          "looks like.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "email"],
    solution_sql="SELECT full_name, email FROM students WHERE email LIKE '%campusmail.edu' "
                 "ORDER BY student_id;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["email"])
        for s in sorted(students, key=lambda s: s["student_id"])
        if s["email"].endswith("campusmail.edu")
    ],
    hints="% stands in for any number of characters, including zero; placing it before the fixed "
          "text anchors the match to the end of the string.",
))

Q.append(dict(
    title="Names Starting With S", difficulty="Easy", topics=TOPIC, subTopics=PATTERN,
    bloomTaxonomy="apply",
    prose="Return the full names of every student whose name begins with the letter S.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name"],
    solution_sql="SELECT full_name FROM students WHERE full_name LIKE 'S%' ORDER BY full_name;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"],)
        for s in sorted(students, key=lambda s: s["full_name"])
        if s["full_name"].startswith("S")
    ],
    hints="A trailing % after a fixed letter matches any amount of text following it.",
))

Q.append(dict(
    title="Second Letter Is 'a'", difficulty="Medium", topics=TOPIC, subTopics=PATTERN,
    bloomTaxonomy="analyze",
    prose="Return the full names of every student whose name has the letter 'a' as its second "
          "character.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name"],
    solution_sql="SELECT full_name FROM students WHERE full_name LIKE '_a%' ORDER BY full_name;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"],)
        for s in sorted(students, key=lambda s: s["full_name"])
        if len(s["full_name"]) >= 2 and s["full_name"][1] == "a"
    ],
    hints="_ stands for exactly one character, so '_a%' means: any single character, then the "
          "letter a, then anything.",
))

Q.append(dict(
    title="Gmail Addresses, Any Casing", difficulty="Medium", topics=TOPIC, subTopics=PATTERN,
    bloomTaxonomy="apply",
    prose="Find every student whose email address contains 'gmail', matching regardless of how "
          "the search text is capitalised.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "email"],
    solution_sql="SELECT full_name, email FROM students WHERE email ILIKE '%GMAIL%' ORDER BY student_id;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["email"])
        for s in sorted(students, key=lambda s: s["student_id"])
        if "gmail" in s["email"].lower()
    ],
    hints="ILIKE matches regardless of letter case, unlike LIKE which is case-sensitive by default.",
))

Q.append(dict(
    title="Email Contains 'verma'", difficulty="Hard", topics=TOPIC, subTopics=PATTERN,
    bloomTaxonomy="apply",
    prose="Find every student whose email address contains the text 'verma', regardless of where "
          "it appears in the address.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "email"],
    solution_sql="SELECT full_name, email FROM students WHERE email LIKE '%verma%' ORDER BY student_id;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["email"])
        for s in sorted(students, key=lambda s: s["student_id"])
        if "verma" in s["email"]
    ],
    hints="% on both sides of the search text means the pattern can appear anywhere in the string, "
          "not just at the start or end.",
))

Q.append(dict(
    title="Gmail Users Outside Chennai", difficulty="Hard", topics=TOPIC, subTopics=PATTERN,
    bloomTaxonomy="analyze",
    prose="Return the full name and email of every student using a gmail.com address who is not "
          "based in Chennai.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "email"],
    solution_sql="SELECT full_name, email FROM students "
                 "WHERE email LIKE '%gmail.com' AND city <> 'Chennai' ORDER BY full_name;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["email"])
        for s in sorted(students, key=lambda s: s["full_name"])
        if s["email"].endswith("gmail.com") and s["city"] != "Chennai"
    ],
    hints="Combine a LIKE pattern with a comparison using AND, exactly like combining any two "
          "WHERE conditions.",
))

# ==================== working-with-null ====================

Q.append(dict(
    title="Ungraded Enrollments", difficulty="Easy", topics=TOPIC, subTopics=NULLS,
    bloomTaxonomy="apply",
    prose="Yusuf wants to list every enrollment that has not been graded yet, because the course "
          "is still in progress.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="SELECT enrollment_id, student_id, course_id, grade FROM enrollments "
                 "WHERE grade IS NULL ORDER BY enrollment_id;",
    data=dict(enrollments=ENROLLMENTS),
    oracle=lambda enrollments: [
        (e["enrollment_id"], e["student_id"], e["course_id"], e["grade"])
        for e in sorted(enrollments, key=lambda e: e["enrollment_id"])
        if e["grade"] is None
    ],
    hints="= cannot test for NULL, since NULL is not a value to compare against. IS NULL asks the "
          "column directly whether it is holding a value at all.",
))

Q.append(dict(
    title="Graded Enrollments", difficulty="Easy", topics=TOPIC, subTopics=NULLS,
    bloomTaxonomy="apply",
    prose="Yusuf's original goal was to list every enrollment that has already been graded.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="SELECT enrollment_id, student_id, course_id, grade FROM enrollments "
                 "WHERE grade IS NOT NULL ORDER BY enrollment_id;",
    data=dict(enrollments=ENROLLMENTS),
    oracle=lambda enrollments: [
        (e["enrollment_id"], e["student_id"], e["course_id"], e["grade"])
        for e in sorted(enrollments, key=lambda e: e["enrollment_id"])
        if e["grade"] is not None
    ],
    hints="WHERE grade = NULL always returns zero rows, even when graded rows exist; "
          "IS NOT NULL is the correct way to ask this question.",
))

Q.append(dict(
    title="Students Without a Phone Number", difficulty="Medium", topics=TOPIC, subTopics=NULLS,
    bloomTaxonomy="apply",
    prose="List the full_name of every student who has not provided a phone number.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name"],
    solution_sql="SELECT full_name FROM students WHERE phone IS NULL ORDER BY student_id;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"],) for s in sorted(students, key=lambda s: s["student_id"]) if s["phone"] is None
    ],
    hints="The same IS NULL pattern that finds missing grades finds any missing column value, "
          "phone included.",
))

Q.append(dict(
    title="Enrollments With a Readable Grade Display", difficulty="Medium", topics=TOPIC, subTopics=NULLS,
    bloomTaxonomy="apply",
    prose="Build a report showing each enrollment's course and grade, but show 'In Progress' "
          "instead of a blank cell wherever a grade has not been recorded yet.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "course_id", "grade_display"],
    solution_sql="SELECT enrollment_id, course_id, COALESCE(grade, 'In Progress') AS grade_display "
                 "FROM enrollments ORDER BY enrollment_id;",
    data=dict(enrollments=ENROLLMENTS),
    oracle=lambda enrollments: [
        (e["enrollment_id"], e["course_id"], e["grade"] if e["grade"] is not None else "In Progress")
        for e in sorted(enrollments, key=lambda e: e["enrollment_id"])
    ],
    hints="COALESCE(grade, 'In Progress') returns grade itself whenever it is not NULL, and only "
          "reaches for the fallback text when it is.",
))

Q.append(dict(
    title="Students Who Provided a Phone Number", difficulty="Hard", topics=TOPIC, subTopics=NULLS,
    bloomTaxonomy="apply",
    prose="List the full_name and phone of every student who did provide a phone number, the "
          "opposite of the students-without-a-phone list.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "phone"],
    solution_sql="SELECT full_name, phone FROM students WHERE phone IS NOT NULL ORDER BY student_id;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["phone"])
        for s in sorted(students, key=lambda s: s["student_id"])
        if s["phone"] is not None
    ],
    hints="IS NOT NULL is the direct opposite check of IS NULL.",
))

Q.append(dict(
    title="Phoneless Students, Grouped by City", difficulty="Hard", topics=TOPIC, subTopics=NULLS,
    bloomTaxonomy="analyze",
    prose="List the full_name and city of every student with no phone on file, grouped by city, "
          "and alphabetically by name within each city.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["full_name", "city"],
    solution_sql="SELECT full_name, city FROM students WHERE phone IS NULL ORDER BY city, full_name;",
    data=dict(students=STUDENTS),
    oracle=lambda students: [
        (s["full_name"], s["city"])
        for s in sorted(
            [s for s in students if s["phone"] is None],
            key=lambda s: (s["city"], s["full_name"]),
        )
    ],
    hints="Combine the IS NULL filter from this lesson with the multi-column ORDER BY from the "
          "previous chapter: filter first, then sort by city, then by name.",
))

assert len(Q) == 29, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/3.3 - Filtering Data - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
