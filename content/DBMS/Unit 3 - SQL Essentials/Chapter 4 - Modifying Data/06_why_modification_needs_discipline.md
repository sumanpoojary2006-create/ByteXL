## Introduction

Naveen has just been handed write access to the college's live enrollment system, the same tables Alia, Rohit, Priyanka, Zara, and Aditya have all been working with, and he notices something about how each of them actually types their statements. None of them writes an `UPDATE` or a `DELETE` the moment they think of it. Each one pauses, checks, and only then commits to the change. Naveen realizes that everything he has learned about `INSERT`, `UPDATE`, `DELETE`, `RETURNING`, and `ON CONFLICT` was never really a set of separate ideas about separate keywords. It was one continuous idea, that changing data is a fundamentally different act from reading it, and it calls for **discipline**, a habit of checking before acting that a `SELECT` never demanded in the first place.

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
(4, 'Siddharth Rao', 'siddharth.rao@campusmail.edu', 'Hyderabad', '9845033333', '2025-01-18');

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT,
    department TEXT,
    credits INTEGER
);

INSERT INTO courses (course_id, title, department, credits) VALUES
(101, 'Database Systems', 'Computer Science', 4),
(102, 'Data Structures', 'Computer Science', 4),
(103, 'Linear Algebra', 'Mathematics', 3);

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id),
    course_id INTEGER REFERENCES courses(course_id),
    enrolled_on DATE,
    grade TEXT
);

INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade) VALUES
(1, 1, 101, '2025-02-01', 'A'),
(2, 2, 101, '2025-02-02', NULL),
(3, 3, 103, '2025-02-03', 'B+'),
(4, 4, 102, '2025-02-04', NULL);
```

## Why a SELECT Mistake and a Modification Mistake Are Not the Same

A `SELECT` with a wrong `WHERE` clause returns the wrong rows on screen, and Naveen can simply notice, fix the condition, and run it again with nothing lost. An `UPDATE` or a `DELETE` with a wrong or missing `WHERE` clause changes or removes rows permanently, and by the time the mistake is noticed, the correct data may no longer exist anywhere to compare against. This asymmetry, that reading forgives mistakes and writing does not, is the entire reason a modification statement deserves a slower hand than a query typed to satisfy curiosity.

## Knowing Exactly Which Rows Before Touching Any of Them

Every genuinely safe modification Naveen has seen so far starts the same way: know exactly which rows a `WHERE` clause will match, before running anything that changes them.

```postgresql with=schema.sql
SELECT enrollment_id, student_id, course_id, grade
FROM enrollments
WHERE student_id = 2 AND course_id = 101;

UPDATE enrollments
SET grade = 'B'
WHERE student_id = 2 AND course_id = 101
RETURNING enrollment_id, student_id, course_id, grade;
```

The `SELECT` confirms exactly one row before anything changes: Neha Sharma's ungraded Database Systems enrollment. The `UPDATE` reuses that identical condition rather than a rewritten or loosened version of it, and `RETURNING` confirms, in the same statement, that grade B landed on that one row and nothing else. Three separate habits are stacked in these two statements:

1. Checking first.
2. Matching the condition exactly.
3. Confirming immediately.

None of them is difficult, they simply have to be done on purpose rather than skipped because a `SELECT` never seemed to need them.

## Treating a Modification as a Decision, Not a Reflex

A `SELECT` can be typed as fast as a thought, because getting it wrong costs nothing more than glancing at an unexpected result and trying again. An `INSERT`, `UPDATE`, or `DELETE` against real data should never be typed at that same speed. The habit worth carrying forward is a short pause built into the process itself: what table, what condition, how many rows should this match, and does the statement in front of me actually say that. Naveen has started reading his own `WHERE` clause out loud before running anything that changes a row, a small ritual that catches a surprising number of mistakes before they become permanent.

## What RETURNING Adds to That Discipline

`RETURNING` is not just a convenience for skipping a second query, it is a built-in confirmation step that happens whether or not anyone remembers to ask for it separately.

```postgresql with=schema.sql
DELETE FROM enrollments
WHERE student_id = 4 AND course_id = 102
RETURNING enrollment_id, student_id, course_id;
```

The result shows exactly one row leaving the table, Siddharth Rao's Data Structures enrollment, and that visible confirmation, arriving in the same breath as the `DELETE` itself, is what turns "I think that worked" into "I can see that it worked."

## Discipline Habits at a Glance

| Habit | What it catches |
|---|---|
| SELECT with the same WHERE, run first | Confirms exactly which rows a modification is about to touch |
| Matching the modification's WHERE to the checked SELECT exactly | Prevents drift between what was checked and what actually ran |
| RETURNING on the modification itself | Confirms the result immediately, without a separate query |
| Treating INSERT, UPDATE, DELETE as deliberate, not reflexive | Catches mistakes before they become permanent |
| ON CONFLICT for insert-or-update situations | Removes the gap between checking and writing that two separate statements leave open |

## Your Turn

Confirm exactly which enrollment belongs to Varun Nair in Linear Algebra, then correct his grade to A, using `RETURNING` to see the result immediately.

```postgresql with=schema.sql
SELECT enrollment_id, student_id, course_id, grade
FROM enrollments
WHERE student_id = 3 AND course_id = 103;

UPDATE enrollments
SET grade = 'A'
WHERE student_id = 3 AND course_id = 103
RETURNING enrollment_id, student_id, course_id, grade;
```

The `SELECT` isolates exactly one row before the change, the `UPDATE` reuses that same condition, and `RETURNING` confirms grade A landed on enrollment 3 and nowhere else.

## Conclusion

Everything Naveen has walked through, from Alia's first `INSERT` to Aditya's `ON CONFLICT`, comes down to one underlying discipline: know what a statement will touch before it runs, confirm what it touched once it has, and never let the speed of typing a change outpace the care that change deserves. Real systems tend to go further still, offering ways to group several changes together so that if something goes wrong partway through, every part of that group can be undone at once rather than leaving the data half-changed, an idea worth carrying forward the moment more than one modification needs to succeed or fail as a single unit.
