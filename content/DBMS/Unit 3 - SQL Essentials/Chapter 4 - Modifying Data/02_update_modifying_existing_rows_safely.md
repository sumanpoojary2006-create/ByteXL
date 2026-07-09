## Introduction

Rohit is going through this term's address updates. One student, Varun Nair, has moved from Chennai to Bengaluru for an internship and emailed the registrar's office asking for his city to be corrected on file. This is not a new row and not a row to be removed, it is one existing fact about one existing student that now needs to change. The tool for that job is **`UPDATE`**, the statement that modifies values already sitting in a table, and Rohit is about to learn that of everything he has typed so far, this is the one that deserves the most care before he presses enter.

```postgresql file=schema.sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    city TEXT,
    phone TEXT,
    joined_on DATE
);

INSERT INTO students (student_id, full_name, email, city, phone, joined_on) VALUES
(1, 'Omkar Rane', 'omkar.rane@campusmail.edu', 'Bengaluru', '9845011111', '2025-01-10'),
(2, 'Neha Sharma', 'neha.sharma@campusmail.edu', 'Mysuru', NULL, '2025-01-12'),
(3, 'Varun Nair', 'varun.nair@gmail.com', 'Chennai', '9845022222', '2025-01-15'),
(4, 'Siddharth Rao', 'siddharth.rao@campusmail.edu', 'Hyderabad', '9845033333', '2025-01-18'),
(5, 'Yusuf Khan', 'yusuf.khan@gmail.com', 'Pune', NULL, '2025-01-20'),
(6, 'Ishita Menon', 'ishita.menon@campusmail.edu', 'Bengaluru', '9845044444', '2025-01-22'),
(7, 'Rahul Verma', 'rahul.verma@gmail.com', 'Chennai', '9845055555', '2025-01-25'),
(8, 'Sanya Iyer', 'sanya.iyer@campusmail.edu', 'Mysuru', NULL, '2025-01-28');

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id),
    course_id INTEGER,
    enrolled_on DATE,
    grade TEXT
);

INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade) VALUES
(1, 1, 101, '2025-02-01', 'A'),
(2, 1, 103, '2025-02-01', 'B+'),
(3, 2, 101, '2025-02-02', NULL),
(4, 3, 102, '2025-02-03', 'A-'),
(5, 3, 105, '2025-02-03', NULL),
(6, 4, 104, '2025-02-04', 'B'),
(7, 5, 101, '2025-02-05', NULL),
(8, 6, 102, '2025-02-06', 'A'),
(9, 7, 103, '2025-02-07', 'C+'),
(10, 8, 105, '2025-02-08', 'B-');
```

## Checking Before Changing

Before Rohit touches anything, he runs a `SELECT` using the exact same condition he is about to update with. This is not an extra step, it is the actual safety check.

```postgresql with=schema.sql
SELECT student_id, full_name, city
FROM students
WHERE student_id = 3;
```

One row comes back: Varun Nair, city Chennai. Rohit now knows, with certainty, which row his `UPDATE` is about to touch, because he has already seen it with his own eyes before changing anything.

## The Shape of UPDATE

An `UPDATE` statement names the table, states which columns get new values with `SET`, and, almost always, narrows the target with `WHERE`.

```postgresql with=schema.sql
UPDATE students
SET city = 'Bengaluru'
WHERE student_id = 3;

SELECT student_id, full_name, city
FROM students
WHERE student_id = 3;
```

Varun's row, and only Varun's row, now shows Bengaluru. The `WHERE` clause here is doing the exact same job it did in the `SELECT` a moment ago: it identifies one row, `student_id = 3`, out of the whole table. `SET` is the new part, and it says which column changes and what it changes to. Everything else about the row, his name, his email, his join date, is left exactly as it was, because `UPDATE` only touches the columns named after `SET`.

## Why WHERE Is Not Optional

Here is the part of `UPDATE` that deserves real weight. `WHERE` is written as though it were optional syntax, and PostgreSQL will happily run an `UPDATE` with no `WHERE` clause at all, but the result is rarely what anyone intended.

```postgresql with=schema.sql
UPDATE students
SET city = 'Bengaluru';

SELECT student_id, full_name, city
FROM students
ORDER BY student_id;
```

Every single student now shows Bengaluru as their city, not just Varun. Rohit meant to fix one row and, without a `WHERE` clause, fixed and broke the entire table in the same instant, since `UPDATE` with no `WHERE` clause treats every row in the table as the target. Two things make this especially dangerous:

- There is no confirmation prompt, no warning about how many rows are about to change, and no undo button once the statement finishes.
- A `WHERE` clause that is too broad causes the exact same damage as no `WHERE` clause at all: writing `WHERE city = 'Chennai'` when the intent was `WHERE student_id = 3` would have updated every student living in Chennai, not the one student Rohit actually meant.

## Making the Safety Habit Concrete

The discipline that protects against this is simple and costs almost nothing: write the `WHERE` condition, run it first as a `SELECT`, look at exactly which rows come back, and only then turn that same condition into an `UPDATE`.

```postgresql with=schema.sql
SELECT student_id, full_name, city
FROM students
WHERE student_id = 6;

UPDATE students
SET city = 'Chennai'
WHERE student_id = 6;

SELECT student_id, full_name, city
FROM students
WHERE student_id = 6;
```

The first `SELECT` shows exactly one row, Ishita Menon in Bengaluru, before anything changes. The `UPDATE` then reuses that identical `WHERE student_id = 6` condition, so there is no gap between what Rohit checked and what he changed. The closing `SELECT` confirms Ishita now shows Chennai and nobody else's row moved. This check-then-update habit takes seconds and it is the single most reliable guard against an `UPDATE` going further than intended.

## Updating More Than One Column at Once

`SET` accepts more than one column, separated by commas, all applied together in a single statement.

```postgresql with=schema.sql
UPDATE students
SET city = 'Mumbai', phone = '9845099999'
WHERE student_id = 5;

SELECT student_id, full_name, city, phone
FROM students
WHERE student_id = 5;
```

Yusuf Khan's city and phone both update in one pass, and both changes are covered by the same single `WHERE` condition, so there is only one row to check rather than two separate statements to keep track of.

## UPDATE at a Glance

| Part | Purpose | What happens if skipped |
|---|---|---|
| `UPDATE table` | Names the table being changed | Not optional; a table must be named |
| `SET column = value` | Names which columns change and to what | Not optional; nothing changes without it |
| `WHERE condition` | Narrows the change to specific rows | Every row in the table gets updated instead of one |

## Your Turn

Siddharth Rao has moved from Hyderabad to Pune. Check which row this touches first, then update it, then confirm.

```postgresql with=schema.sql
SELECT student_id, full_name, city
FROM students
WHERE student_id = 4;

UPDATE students
SET city = 'Pune'
WHERE student_id = 4;

SELECT student_id, full_name, city
FROM students
WHERE student_id = 4;
```

The first `SELECT` shows Siddharth in Hyderabad, the `UPDATE` reuses that same `student_id = 4` condition, and the final `SELECT` confirms only his row now reads Pune while every other student's city is untouched.

## Conclusion

`UPDATE` looks like a small statement, a table name, a `SET`, sometimes a `WHERE`, but it is the first statement in this material that can silently damage far more than intended if that `WHERE` clause is missing or too loose. The habit that keeps it safe is not clever, it is simply checking with a `SELECT` under the same condition before the change and again right after, so that what was touched is always known rather than assumed. Rohit can now correct Varun Nair's city from Chennai to Bengaluru with total confidence that his `UPDATE` touched that one row and nothing else in the students table. Correcting a row that is wrong is only one kind of change a real system needs; sometimes a row needs to disappear entirely, and that calls for a statement with the very same discipline required around it.
