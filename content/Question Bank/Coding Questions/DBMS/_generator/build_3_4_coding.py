"""3.4 - Modifying Data - Coding Questions (32: INSERT, UPDATE, DELETE,
RETURNING, ON CONFLICT / upsert, and the discipline habits that tie them
together).

Design note: every solution is a SINGLE SQL statement using RETURNING, never
a modification followed by a separate verification SELECT. The lesson
markdown itself demonstrates the two-statement style (modify, then SELECT to
check), but this bank standardizes on RETURNING throughout because there is
no confirmed spec for how ByteXL's grader would capture output from a
multi-statement solution (a "last statement only" vs. "every statement's
output" ambiguity), whereas a single RETURNING statement has one unambiguous
output. This also means no "reproduce the missing-WHERE mistake" questions
exist here -- a coding question's target answer should always be correct
SQL, so the WHERE-discipline lessons are tested through precise, well-scoped
correct statements rather than by asking a student to write intentionally
broken SQL.

Two datasets are used:
- The standard students/courses/enrollments dataset (matches 3.3's exactly,
  including Microeconomics at 2 credits) for INSERT/UPDATE/DELETE/RETURNING/
  discipline questions.
- A separate, smaller dataset with a UNIQUE(student_id, course_id) constraint
  on enrollments (matching lesson 5's own setup) for the upsert questions,
  since ON CONFLICT has nothing to react to without that constraint.

Expected output is computed by a Python oracle modeling the mutation against
the same in-memory data used to generate preloadCode's INSERT statements.
"""
import copy
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

TOPIC = "sql-essentials"
INSERT_TOPIC = "insert-adding-new-rows"
UPDATE_TOPIC = "update-modifying-existing-rows-safely"
DELETE_TOPIC = "delete-removing-rows-without-accidents"
RETURNING_TOPIC = "returning-getting-back-what-you-just-changed"
UPSERT_TOPIC = "upsert-and-on-conflict-insert-or-update-in-one-step"
DISCIPLINE_TOPIC = "why-modification-needs-discipline"

# ----------------------------- Standard dataset (matches 3.3 exactly) -----------------------------

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
STUDENTS_AND_COURSES_SQL = (
    STUDENTS_DDL.strip("\n") + "\n\n" + sql_insert("students", STUDENT_COLUMNS, STUDENTS) + "\n\n"
    + COURSES_DDL.strip("\n") + "\n\n" + sql_insert("courses", COURSE_COLUMNS, COURSES)
)

STUDENTS_SCHEMA_LINES = [
    "students(student_id INTEGER PK, full_name TEXT, email TEXT, city TEXT, phone TEXT, joined_on DATE) -- 8 rows",
]
COURSES_SCHEMA_LINES = [
    "courses(course_id INTEGER PK, title TEXT, department TEXT, credits INTEGER) -- 5 rows",
]
STUDENTS_AND_COURSES_SCHEMA_LINES = STUDENTS_SCHEMA_LINES + COURSES_SCHEMA_LINES
ENROLLMENTS_SCHEMA_LINES = STUDENTS_SCHEMA_LINES + COURSES_SCHEMA_LINES + [
    "enrollments(enrollment_id INTEGER PK, student_id INTEGER FK, course_id INTEGER FK, enrolled_on DATE, grade TEXT) -- 10 rows, grade is NULL for three enrollments",
]

# ----------------------------- Upsert dataset (matches lesson 5, with UNIQUE constraint) -----------------------------

U_STUDENT_COLUMNS = ["student_id", "full_name", "city"]
U_STUDENTS = [
    dict(student_id=1, full_name="Omkar Rane", city="Bengaluru"),
    dict(student_id=2, full_name="Neha Sharma", city="Mysuru"),
    dict(student_id=3, full_name="Varun Nair", city="Chennai"),
]

U_COURSE_COLUMNS = ["course_id", "title", "department", "credits"]
U_COURSES = [
    dict(course_id=101, title="Database Systems", department="Computer Science", credits=4),
    dict(course_id=102, title="Data Structures", department="Computer Science", credits=4),
    dict(course_id=103, title="Linear Algebra", department="Mathematics", credits=3),
]

U_ENROLLMENT_COLUMNS = ["enrollment_id", "student_id", "course_id", "enrolled_on", "grade"]
U_ENROLLMENTS = [
    dict(enrollment_id=1, student_id=1, course_id=101, enrolled_on="2025-02-01", grade="A"),
    dict(enrollment_id=2, student_id=2, course_id=101, enrolled_on="2025-02-02", grade=None),
    dict(enrollment_id=3, student_id=3, course_id=103, enrolled_on="2025-02-03", grade="B+"),
]

U_STUDENTS_DDL = """
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    full_name TEXT,
    city TEXT
);
"""

U_COURSES_DDL = COURSES_DDL

U_ENROLLMENTS_DDL = """
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id),
    course_id INTEGER REFERENCES courses(course_id),
    enrolled_on DATE,
    grade TEXT,
    UNIQUE (student_id, course_id)
);
"""

UPSERT_SQL = (
    U_STUDENTS_DDL.strip("\n") + "\n\n" + sql_insert("students", U_STUDENT_COLUMNS, U_STUDENTS) + "\n\n"
    + U_COURSES_DDL.strip("\n") + "\n\n" + sql_insert("courses", U_COURSE_COLUMNS, U_COURSES) + "\n\n"
    + U_ENROLLMENTS_DDL.strip("\n") + "\n\n" + sql_insert("enrollments", U_ENROLLMENT_COLUMNS, U_ENROLLMENTS)
)
UPSERT_SCHEMA_LINES = [
    "students(student_id INTEGER PK, full_name TEXT, city TEXT) -- 3 rows",
    "courses(course_id INTEGER PK, title TEXT, department TEXT, credits INTEGER) -- 3 rows",
    "enrollments(enrollment_id INTEGER PK, student_id INTEGER FK, course_id INTEGER FK, enrolled_on DATE, grade TEXT, UNIQUE(student_id, course_id)) -- 3 rows",
]

Q = []

# ==================== insert-adding-new-rows ====================

Q.append(dict(
    title="Enroll a Newly Paid Student", difficulty="Easy", topics=TOPIC, subTopics=INSERT_TOPIC,
    bloomTaxonomy="apply",
    prose="A new student, Diya Kulkarni, has just finished paying fees and needs to appear in the "
          "system. Add her with student_id 9, email diya.kulkarni@campusmail.edu, city Pune, phone "
          "9845066666, joined_on 2025-02-14, and confirm the row in the same statement.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_id", "full_name", "city", "phone"],
    solution_sql="INSERT INTO students (student_id, full_name, email, city, phone, joined_on)\n"
                 "VALUES (9, 'Diya Kulkarni', 'diya.kulkarni@campusmail.edu', 'Pune', '9845066666', '2025-02-14')\n"
                 "RETURNING student_id, full_name, city, phone;",
    data=dict(),
    oracle=lambda: [(9, "Diya Kulkarni", "Pune", "9845066666")],
    hints="Name the columns you are filling in, then supply the values in the same order, and add "
          "RETURNING to confirm the row in the same statement.",
))

Q.append(dict(
    title="Register Farhan Ali", difficulty="Easy", topics=TOPIC, subTopics=INSERT_TOPIC,
    bloomTaxonomy="apply",
    prose="Farhan Ali has just registered from Hyderabad with no phone number on file yet. Add him "
          "with student_id 12, email farhan.ali@campusmail.edu, joined_on 2025-02-16, and confirm "
          "the row landed correctly.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_id", "full_name", "city", "phone"],
    solution_sql="INSERT INTO students (student_id, full_name, email, city, phone, joined_on)\n"
                 "VALUES (12, 'Farhan Ali', 'farhan.ali@campusmail.edu', 'Hyderabad', NULL, '2025-02-16')\n"
                 "RETURNING student_id, full_name, city, phone;",
    data=dict(),
    oracle=lambda: [(12, "Farhan Ali", "Hyderabad", None)],
    hints="A value that genuinely has not been provided yet is written as NULL, not left out of the "
          "VALUES list.",
))

Q.append(dict(
    title="Register Two Students in One Statement", difficulty="Medium", topics=TOPIC, subTopics=INSERT_TOPIC,
    bloomTaxonomy="apply",
    prose="Registration week rarely brings in one student at a time. Add Kabir Sethi (student_id "
          "10, kabir.sethi@campusmail.edu, Chennai, phone 9845077777, joined 2025-02-15) and Meera "
          "Das (student_id 11, meera.das@gmail.com, city not yet recorded, phone 9845088888, "
          "joined 2025-02-15) in a single INSERT statement.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_id", "full_name", "city"],
    solution_sql="INSERT INTO students (student_id, full_name, email, city, phone, joined_on) VALUES\n"
                 "(10, 'Kabir Sethi', 'kabir.sethi@campusmail.edu', 'Chennai', '9845077777', '2025-02-15'),\n"
                 "(11, 'Meera Das', 'meera.das@gmail.com', NULL, '9845088888', '2025-02-15')\n"
                 "RETURNING student_id, full_name, city;",
    data=dict(),
    oracle=lambda: [(10, "Kabir Sethi", "Chennai"), (11, "Meera Das", None)],
    hints="INSERT accepts more than one row in a single statement: each row is a parenthesized "
          "group separated by a comma.",
))

Q.append(dict(
    title="Add a Course by Column Position", difficulty="Medium", topics=TOPIC, subTopics=INSERT_TOPIC,
    bloomTaxonomy="apply",
    prose="Add a new course, Operating Systems, course_id 106, Computer Science, 4 credits, using "
          "the table's column order directly rather than naming the columns.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["course_id", "title", "department", "credits"],
    solution_sql="INSERT INTO courses VALUES (106, 'Operating Systems', 'Computer Science', 4)\n"
                 "RETURNING course_id, title, department, credits;",
    data=dict(),
    oracle=lambda: [(106, "Operating Systems", "Computer Science", 4)],
    hints="Leaving out the column list matches your VALUES to the table's columns purely by "
          "position, in the exact order courses was created: course_id, title, department, credits.",
))

Q.append(dict(
    title="Enroll Varun Nair in Discrete Mathematics", difficulty="Hard", topics=TOPIC, subTopics=INSERT_TOPIC,
    bloomTaxonomy="apply",
    prose="Varun Nair (student_id 3) has just registered for Discrete Mathematics (course_id 104). "
          "Add his enrollment with enrollment_id 11, enrolled_on 2025-02-20, no grade yet, and "
          "confirm it in the same statement.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade)\n"
                 "VALUES (11, 3, 104, '2025-02-20', NULL)\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(11, 3, 104, None)],
    hints="An enrollments row referencing an existing student and course is inserted exactly like "
          "any other row: name the columns, supply matching values.",
))

# ==================== update-modifying-existing-rows-safely ====================

Q.append(dict(
    title="Correct Varun Nair's City", difficulty="Easy", topics=TOPIC, subTopics=UPDATE_TOPIC,
    bloomTaxonomy="apply",
    prose="Varun Nair (student_id 3) has moved from Chennai to Bengaluru for an internship. Update "
          "his city on file and confirm the change.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_id", "full_name", "city"],
    solution_sql="UPDATE students SET city = 'Bengaluru' WHERE student_id = 3\n"
                 "RETURNING student_id, full_name, city;",
    data=dict(),
    oracle=lambda: [(3, "Varun Nair", "Bengaluru")],
    hints="UPDATE names the table, SET says which column changes and to what, and WHERE narrows "
          "the change to exactly the one row intended.",
))

Q.append(dict(
    title="Correct Siddharth Rao's City", difficulty="Easy", topics=TOPIC, subTopics=UPDATE_TOPIC,
    bloomTaxonomy="apply",
    prose="Siddharth Rao (student_id 4) has moved from Hyderabad to Pune. Update his city and "
          "confirm only his row changed.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_id", "full_name", "city"],
    solution_sql="UPDATE students SET city = 'Pune' WHERE student_id = 4\n"
                 "RETURNING student_id, full_name, city;",
    data=dict(),
    oracle=lambda: [(4, "Siddharth Rao", "Pune")],
    hints="Target the update with WHERE student_id = 4 so only Siddharth's row is affected.",
))

Q.append(dict(
    title="Correct Ishita Menon's City", difficulty="Medium", topics=TOPIC, subTopics=UPDATE_TOPIC,
    bloomTaxonomy="apply",
    prose="Ishita Menon (student_id 6) has moved from Bengaluru to Chennai. Update her city and "
          "confirm the change in the same statement.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_id", "full_name", "city"],
    solution_sql="UPDATE students SET city = 'Chennai' WHERE student_id = 6\n"
                 "RETURNING student_id, full_name, city;",
    data=dict(),
    oracle=lambda: [(6, "Ishita Menon", "Chennai")],
    hints="The same single-row WHERE pattern applies regardless of which student is being "
          "corrected.",
))

Q.append(dict(
    title="Update Yusuf Khan's City and Phone Together", difficulty="Medium", topics=TOPIC, subTopics=UPDATE_TOPIC,
    bloomTaxonomy="apply",
    prose="Yusuf Khan (student_id 5) has moved to Mumbai and finally provided a phone number, "
          "9845099999. Update both columns in a single statement and confirm the result.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_id", "full_name", "city", "phone"],
    solution_sql="UPDATE students SET city = 'Mumbai', phone = '9845099999' WHERE student_id = 5\n"
                 "RETURNING student_id, full_name, city, phone;",
    data=dict(),
    oracle=lambda: [(5, "Yusuf Khan", "Mumbai", "9845099999")],
    hints="SET accepts more than one column, separated by commas, all applied together under the "
          "same WHERE condition.",
))

Q.append(dict(
    title="Record Yusuf Khan's Database Systems Grade", difficulty="Hard", topics=TOPIC, subTopics=UPDATE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Yusuf Khan's (student_id 5) Database Systems (course_id 101) enrollment has not been "
          "graded yet. Record his grade as B, targeting exactly that one enrollment.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="UPDATE enrollments SET grade = 'B' WHERE student_id = 5 AND course_id = 101\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(7, 5, 101, "B")],
    hints="student_id alone might one day match more than one enrollment; combining it with "
          "course_id using AND makes the target specific enough to trust.",
))

# ==================== delete-removing-rows-without-accidents ====================
# All targets are enrollments rows: students and courses have rows referenced by
# enrollments' foreign keys, so deleting from either would violate a FK constraint.

Q.append(dict(
    title="Remove Rahul Verma's Dropped Enrollment", difficulty="Easy", topics=TOPIC, subTopics=DELETE_TOPIC,
    bloomTaxonomy="apply",
    prose="Rahul Verma registered for Linear Algebra and then dropped it within the deadline. "
          "Remove his enrollment (enrollment_id 9) entirely and confirm what was removed.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id"],
    solution_sql="DELETE FROM enrollments WHERE enrollment_id = 9\n"
                 "RETURNING enrollment_id, student_id, course_id;",
    data=dict(),
    oracle=lambda: [(9, 7, 103)],
    hints="DELETE FROM names the table, WHERE narrows which rows are removed, and RETURNING shows "
          "exactly what disappeared.",
))

Q.append(dict(
    title="Remove Neha Sharma's Dropped Enrollment", difficulty="Easy", topics=TOPIC, subTopics=DELETE_TOPIC,
    bloomTaxonomy="apply",
    prose="Neha Sharma (student_id 2) has dropped Database Systems (course_id 101). Remove exactly "
          "that enrollment and confirm what was removed.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id"],
    solution_sql="DELETE FROM enrollments WHERE student_id = 2 AND course_id = 101\n"
                 "RETURNING enrollment_id, student_id, course_id;",
    data=dict(),
    oracle=lambda: [(3, 2, 101)],
    hints="Combine student_id and course_id with AND to pin down exactly one enrollment row.",
))

Q.append(dict(
    title="Remove Siddharth Rao's Dropped Enrollment", difficulty="Medium", topics=TOPIC, subTopics=DELETE_TOPIC,
    bloomTaxonomy="apply",
    prose="Siddharth Rao (student_id 4) has dropped Discrete Mathematics (course_id 104). Remove "
          "his enrollment and confirm its full details as they looked right before removal.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="DELETE FROM enrollments WHERE student_id = 4 AND course_id = 104\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(6, 4, 104, "B")],
    hints="RETURNING on a DELETE hands back the row exactly as it looked the instant before it was "
          "removed, grade included.",
))

Q.append(dict(
    title="Remove Sanya Iyer's Dropped Enrollment", difficulty="Medium", topics=TOPIC, subTopics=DELETE_TOPIC,
    bloomTaxonomy="apply",
    prose="Sanya Iyer (student_id 8) has dropped Microeconomics (course_id 105). Remove her "
          "enrollment and confirm exactly what was removed.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="DELETE FROM enrollments WHERE student_id = 8 AND course_id = 105\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(10, 8, 105, "B-")],
    hints="Even a graded enrollment is removed the same way; RETURNING shows the grade it carried "
          "right up until removal.",
))

Q.append(dict(
    title="Remove the Ungraded Microeconomics Enrollment", difficulty="Hard", topics=TOPIC, subTopics=DELETE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Among the Microeconomics (course_id 105) enrollments, remove specifically the one that "
          "has not been graded yet, without referencing which student it belongs to directly.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="DELETE FROM enrollments WHERE course_id = 105 AND grade IS NULL\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(5, 3, 105, None)],
    hints="Combine a comparison on course_id with grade IS NULL from the previous chapter to "
          "identify the one ungraded Microeconomics enrollment.",
))

# ==================== returning-getting-back-what-you-just-changed ====================

Q.append(dict(
    title="Enroll Siddharth Rao, Confirmed Immediately", difficulty="Easy", topics=TOPIC, subTopics=RETURNING_TOPIC,
    bloomTaxonomy="apply",
    prose="Siddharth Rao (student_id 4) has newly registered for Database Systems (course_id 101). "
          "Insert his enrollment (enrollment_id 11, enrolled 2025-02-09, no grade yet) and learn "
          "back exactly what was recorded, with no separate SELECT afterward.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "enrolled_on"],
    solution_sql="INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade)\n"
                 "VALUES (11, 4, 101, '2025-02-09', NULL)\n"
                 "RETURNING enrollment_id, student_id, course_id, enrolled_on;",
    data=dict(),
    oracle=lambda: [(11, 4, 101, "2025-02-09")],
    hints="RETURNING hands back the row exactly as it was written, in the same result set the "
          "INSERT itself produces.",
))

Q.append(dict(
    title="Update Neha Sharma's City, Confirmed Immediately", difficulty="Easy", topics=TOPIC, subTopics=RETURNING_TOPIC,
    bloomTaxonomy="apply",
    prose="Neha Sharma (student_id 2) has moved to Chennai. Update her city and learn back the row "
          "as it looks after the change, all in one statement.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_id", "full_name", "city"],
    solution_sql="UPDATE students SET city = 'Chennai' WHERE student_id = 2\n"
                 "RETURNING student_id, full_name, city;",
    data=dict(),
    oracle=lambda: [(2, "Neha Sharma", "Chennai")],
    hints="RETURNING on an UPDATE hands back the row as it looks after the change has been "
          "applied, not before.",
))

Q.append(dict(
    title="Remove an Enrollment, Confirmed Immediately", difficulty="Medium", topics=TOPIC, subTopics=RETURNING_TOPIC,
    bloomTaxonomy="apply",
    prose="Remove the enrollment with enrollment_id 5 and confirm, in the same statement, exactly "
          "which row was removed.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="DELETE FROM enrollments WHERE enrollment_id = 5\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(5, 3, 105, None)],
    hints="RETURNING on a DELETE gives the last view anyone gets of that row before it is gone for "
          "good.",
))

Q.append(dict(
    title="Register Kabir Sethi, Confirmed Immediately", difficulty="Medium", topics=TOPIC, subTopics=RETURNING_TOPIC,
    bloomTaxonomy="apply",
    prose="Insert a new student, Kabir Sethi (student_id 9, kabir.sethi@campusmail.edu, Chennai, "
          "phone 9845077777, joined 2025-02-16), and confirm the row using RETURNING, with no "
          "separate SELECT afterward.",
    schema_sql=STUDENTS_SQL, schema_lines=STUDENTS_SCHEMA_LINES,
    header=["student_id", "full_name", "city"],
    solution_sql="INSERT INTO students (student_id, full_name, email, city, phone, joined_on)\n"
                 "VALUES (9, 'Kabir Sethi', 'kabir.sethi@campusmail.edu', 'Chennai', '9845077777', '2025-02-16')\n"
                 "RETURNING student_id, full_name, city;",
    data=dict(),
    oracle=lambda: [(9, "Kabir Sethi", "Chennai")],
    hints="RETURNING at the end of the INSERT is what removes the need for a follow-up SELECT.",
))

Q.append(dict(
    title="Attempted Update for a Nonexistent Enrollment", difficulty="Hard", topics=TOPIC, subTopics=RETURNING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Someone tries to record a grade for enrollment_id 999, which does not exist in the "
          "table. Write the UPDATE with RETURNING exactly as they would, and show what genuinely "
          "comes back.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="UPDATE enrollments SET grade = 'A' WHERE enrollment_id = 999\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [],
    allow_empty_result=True,
    hints="If the WHERE condition matches no rows at all, RETURNING comes back empty, which is "
          "itself a useful signal that nothing was touched.",
))

Q.append(dict(
    title="Remove Ishita Menon's Enrollment, Confirmed Immediately", difficulty="Hard", topics=TOPIC, subTopics=RETURNING_TOPIC,
    bloomTaxonomy="apply",
    prose="Ishita Menon (student_id 6) has dropped Data Structures (course_id 102). Remove her "
          "enrollment and confirm exactly what was removed, in the same statement.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="DELETE FROM enrollments WHERE student_id = 6 AND course_id = 102\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(8, 6, 102, "A")],
    hints="Combine student_id and course_id with AND, then RETURNING confirms the exact row that "
          "left the table.",
))

# ==================== upsert-and-on-conflict-insert-or-update-in-one-step ====================

Q.append(dict(
    title="Correct Neha Sharma's Existing Grade via Upsert", difficulty="Easy", topics=TOPIC, subTopics=UPSERT_TOPIC,
    bloomTaxonomy="apply",
    prose="Neha Sharma's Database Systems enrollment already exists with no grade recorded. A new "
          "submission carries her final grade, B+. Write a single statement that inserts if new "
          "and updates the grade if the pairing already exists.",
    schema_sql=UPSERT_SQL, schema_lines=UPSERT_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade)\n"
                 "VALUES (4, 2, 101, '2025-02-02', 'B+')\n"
                 "ON CONFLICT (student_id, course_id)\n"
                 "DO UPDATE SET grade = EXCLUDED.grade\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(2, 2, 101, "B+")],
    hints="The result shows enrollment_id 2, the row that already existed, not a new row with "
          "enrollment_id 4, since student_id 2 and course_id 101 already matched the UNIQUE "
          "constraint.",
))

Q.append(dict(
    title="Register Varun Nair for Data Structures via Upsert", difficulty="Easy", topics=TOPIC, subTopics=UPSERT_TOPIC,
    bloomTaxonomy="apply",
    prose="Varun Nair has newly registered for Data Structures (course_id 102), a pairing that has "
          "never been submitted before. Use the same insert-or-update statement shape as always.",
    schema_sql=UPSERT_SQL, schema_lines=UPSERT_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade)\n"
                 "VALUES (5, 3, 102, '2025-02-10', NULL)\n"
                 "ON CONFLICT (student_id, course_id)\n"
                 "DO UPDATE SET grade = EXCLUDED.grade\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(5, 3, 102, None)],
    hints="ON CONFLICT only changes behavior when a conflict is actually detected; since student_id "
          "3 and course_id 102 have never been paired, this proceeds as a plain insert.",
))

Q.append(dict(
    title="Resubmit an Already-Recorded Enrollment", difficulty="Medium", topics=TOPIC, subTopics=UPSERT_TOPIC,
    bloomTaxonomy="apply",
    prose="A duplicate submission arrives for Omkar Rane's Database Systems enrollment, which "
          "already exists. There is nothing to correct here, so a repeat submission of an "
          "already-known pairing should simply be a harmless no-op.",
    schema_sql=UPSERT_SQL, schema_lines=UPSERT_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade)\n"
                 "VALUES (6, 1, 101, '2025-02-01', 'A')\n"
                 "ON CONFLICT (student_id, course_id)\n"
                 "DO NOTHING\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [],
    allow_empty_result=True,
    hints="DO NOTHING means precisely that: the conflicting row is left exactly as it was, no "
          "error is raised, and RETURNING comes back empty since nothing was inserted or updated.",
))

Q.append(dict(
    title="Register Omkar Rane for Linear Algebra, No Conflict", difficulty="Medium", topics=TOPIC, subTopics=UPSERT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Omkar Rane has newly registered for Linear Algebra (course_id 103), a pairing that has "
          "never been submitted before. Use DO NOTHING in case it turns out to be a duplicate.",
    schema_sql=UPSERT_SQL, schema_lines=UPSERT_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade)\n"
                 "VALUES (6, 1, 103, '2025-02-05', NULL)\n"
                 "ON CONFLICT (student_id, course_id)\n"
                 "DO NOTHING\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(6, 1, 103, None)],
    hints="DO NOTHING only suppresses the insert when a real conflict exists; with no conflict "
          "here, the row is inserted normally and RETURNING shows it.",
))

Q.append(dict(
    title="Register Varun Nair for Database Systems via Upsert", difficulty="Hard", topics=TOPIC, subTopics=UPSERT_TOPIC,
    bloomTaxonomy="apply",
    prose="Varun Nair has newly registered for Database Systems (course_id 101) with a grade of B "
          "already available. Use a single insert-or-update statement to handle it correctly "
          "whether or not the pairing already exists.",
    schema_sql=UPSERT_SQL, schema_lines=UPSERT_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade)\n"
                 "VALUES (7, 3, 101, '2025-02-11', 'B')\n"
                 "ON CONFLICT (student_id, course_id)\n"
                 "DO UPDATE SET grade = EXCLUDED.grade\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(7, 3, 101, "B")],
    hints="student_id 3 and course_id 101 have never been paired before, so this is a genuine "
          "insert, landing as enrollment_id 7 with grade B already set.",
))

Q.append(dict(
    title="Correct Varun Nair's Grade Without Disturbing His Enrollment Date", difficulty="Hard", topics=TOPIC, subTopics=UPSERT_TOPIC,
    bloomTaxonomy="analyze",
    prose="A resubmission for Varun Nair's Linear Algebra enrollment carries a new grade, A, and "
          "(incorrectly) a different enrolled_on date, 2025-03-01. Since only the grade should "
          "ever be corrected by this upsert, the enrolled_on date on file must stay exactly what "
          "it already was.",
    schema_sql=UPSERT_SQL, schema_lines=UPSERT_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "enrolled_on", "grade"],
    solution_sql="INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade)\n"
                 "VALUES (8, 3, 103, '2025-03-01', 'A')\n"
                 "ON CONFLICT (student_id, course_id)\n"
                 "DO UPDATE SET grade = EXCLUDED.grade\n"
                 "RETURNING enrollment_id, student_id, course_id, enrolled_on, grade;",
    data=dict(),
    oracle=lambda: [(3, 3, 103, "2025-02-03", "A")],
    hints="DO UPDATE SET grade = EXCLUDED.grade only ever changes the grade column; enrolled_on is "
          "not named in SET, so the original value, 2025-02-03, stays exactly as it was.",
))

# ==================== why-modification-needs-discipline ====================

Q.append(dict(
    title="Correct Neha Sharma's Grade, Precisely Targeted", difficulty="Easy", topics=TOPIC, subTopics=DISCIPLINE_TOPIC,
    bloomTaxonomy="apply",
    prose="Neha Sharma's (student_id 2) Database Systems (course_id 101) enrollment needs its "
          "grade recorded as B. Use a WHERE condition specific enough to touch only that one row, "
          "and confirm the result immediately.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="UPDATE enrollments SET grade = 'B' WHERE student_id = 2 AND course_id = 101\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(3, 2, 101, "B")],
    hints="Knowing exactly which row a WHERE clause will match, and matching the modification's "
          "condition to it precisely, is the core habit this lesson is built around.",
))

Q.append(dict(
    title="Correct Varun Nair's Microeconomics Grade", difficulty="Easy", topics=TOPIC, subTopics=DISCIPLINE_TOPIC,
    bloomTaxonomy="apply",
    prose="Varun Nair's (student_id 3) Microeconomics (course_id 105) enrollment needs its grade "
          "recorded as B+. Target exactly that enrollment and confirm the result in the same "
          "statement.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="UPDATE enrollments SET grade = 'B+' WHERE student_id = 3 AND course_id = 105\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(5, 3, 105, "B+")],
    hints="A precise, compound WHERE condition is what makes a modification trustworthy, "
          "confirmed immediately by RETURNING.",
))

Q.append(dict(
    title="Remove Omkar Rane's Database Systems Enrollment, Confirmed", difficulty="Medium", topics=TOPIC, subTopics=DISCIPLINE_TOPIC,
    bloomTaxonomy="apply",
    prose="Omkar Rane (student_id 1) has dropped Database Systems (course_id 101). Remove exactly "
          "that enrollment and confirm, in the same statement, precisely what left the table.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "grade"],
    solution_sql="DELETE FROM enrollments WHERE student_id = 1 AND course_id = 101\n"
                 "RETURNING enrollment_id, student_id, course_id, grade;",
    data=dict(),
    oracle=lambda: [(1, 1, 101, "A")],
    hints="RETURNING on the modification itself is what turns 'I think that worked' into 'I can "
          "see that it worked.'",
))

Q.append(dict(
    title="Enroll Ishita Menon in Discrete Mathematics, Deliberately", difficulty="Medium", topics=TOPIC, subTopics=DISCIPLINE_TOPIC,
    bloomTaxonomy="apply",
    prose="Ishita Menon (student_id 6) is newly enrolling in Discrete Mathematics (course_id 104). "
          "Insert her enrollment (enrollment_id 11, enrolled 2025-02-20, no grade yet) and confirm "
          "the full row, treating the statement as a deliberate action rather than a reflex.",
    schema_sql=ENROLLMENTS_SQL, schema_lines=ENROLLMENTS_SCHEMA_LINES,
    header=["enrollment_id", "student_id", "course_id", "enrolled_on", "grade"],
    solution_sql="INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade)\n"
                 "VALUES (11, 6, 104, '2025-02-20', NULL)\n"
                 "RETURNING enrollment_id, student_id, course_id, enrolled_on, grade;",
    data=dict(),
    oracle=lambda: [(11, 6, 104, "2025-02-20", None)],
    hints="Even an INSERT benefits from the same discipline as UPDATE and DELETE: know exactly "
          "what a statement will create before running it, and confirm what it created afterward.",
))

Q.append(dict(
    title="Correct a Clerical Error in a Course's Credit Value", difficulty="Hard", topics=TOPIC, subTopics=DISCIPLINE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Microeconomics (course_id 105) was recorded as 2 credits but should be 3. Apply the "
          "same precise, confirmed-immediately discipline to a courses table correction, touching "
          "only that one course.",
    schema_sql=COURSES_SQL, schema_lines=COURSES_SCHEMA_LINES,
    header=["course_id", "title", "credits"],
    solution_sql="UPDATE courses SET credits = 3 WHERE course_id = 105\n"
                 "RETURNING course_id, title, credits;",
    data=dict(),
    oracle=lambda: [(105, "Microeconomics", 3)],
    hints="The discipline habits from this lesson, know the target, match the condition exactly, "
          "confirm immediately, apply to any table, not just students and enrollments.",
))

assert len(Q) == 32, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/3.4 - Modifying Data - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
