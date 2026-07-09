## Introduction

Omkar is pulling together a report of Computer Science offerings for his advisor. He starts the way anyone new to SQL does: `SELECT title, department, credits FROM courses;`. The result lists every course in the catalogue, mathematics and economics included, and he has to scroll past rows that have nothing to do with what his advisor asked for. What he actually needs is a way to tell the database "only hand me back the rows where this is true," and that instruction has a name: the **`WHERE` clause**.

## Filtering Rows Instead of Reading All of Them

A `SELECT` without a `WHERE` clause returns every row a table has. Add a `WHERE` clause and the database tests each row against a condition, keeping only the rows where that condition is true and discarding the rest before the result ever reaches Omkar's screen.

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

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT,
    department TEXT,
    credits INTEGER
);

INSERT INTO courses (course_id, title, department, credits) VALUES
(101, 'Database Systems', 'Computer Science', 4),
(102, 'Data Structures', 'Computer Science', 4),
(103, 'Linear Algebra', 'Mathematics', 3),
(104, 'Discrete Mathematics', 'Mathematics', 3),
(105, 'Microeconomics', 'Economics', 2);

CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY,
    full_name TEXT,
    department TEXT
);

INSERT INTO instructors (instructor_id, full_name, department) VALUES
(201, 'Ananya Bose', 'Computer Science'),
(202, 'Manoj Pillai', 'Mathematics'),
(203, 'Kavita Reddy', 'Economics');

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id),
    course_id INTEGER REFERENCES courses(course_id),
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

These four tables, students, courses, instructors, and enrollments, are the ones Omkar will keep coming back to. With them in place, his original problem has a one-line fix.

```postgresql with=schema.sql
SELECT title, department, credits
FROM courses
WHERE department = 'Computer Science';
```

Only `Database Systems` and `Data Structures` come back. The database evaluated the condition `department = 'Computer Science'` against every row in `courses`, kept the two rows where it held true, and dropped the mathematics and economics rows entirely. Omkar's advisor never even sees the rows that did not qualify.

## Where WHERE Sits in a Query

The clause has a fixed position: it comes right after `FROM` and before `ORDER BY` or `LIMIT`. That ordering reflects the order the database actually works in: first decide which table to read, then decide which of its rows survive, and only after that decide how to sort or trim what is left.

```postgresql with=schema.sql
SELECT full_name, city
FROM students
WHERE city = 'Chennai'
ORDER BY full_name;
```

This returns Rahul Verma and Varun Nair, the two students based in Chennai, sorted alphabetically by name. Filtering happens before sorting: the database first narrows the table down to Chennai residents, and only then arranges those survivors in order. Writing `ORDER BY` before `WHERE` in the query text is not valid; the clause order in SQL always matches the sequence in which these decisions get made.

## Clauses at a Glance

| Clause | Purpose | Runs relative to WHERE |
|---|---|---|
| `SELECT` | Chooses which columns appear in the result | Decided last, on the surviving rows |
| `FROM` | Names the table to read | Before WHERE |
| `WHERE` | Keeps only the rows matching a condition | The filtering step itself |
| `ORDER BY` | Arranges the surviving rows | After WHERE |
| `LIMIT` | Caps how many surviving rows are returned | After WHERE and ORDER BY |

## Every Condition Is Just a True-or-False Test

`department = 'Computer Science'` and `city = 'Chennai'` are both equality checks, the simplest kind of condition `WHERE` can hold. But `WHERE` accepts far more than equality:

- Compare numbers and dates
- Combine several conditions together
- Match partial text patterns
- Handle missing values

Every one of those is really the same idea underneath, a test that a row either passes or fails, and what follows is simply a tour of the different kinds of tests you can write.

## Your Turn

Using the same four tables, write a query that returns the `full_name` and `city` of every student based in Bengaluru.

```postgresql with=schema.sql
SELECT full_name, city
FROM students
WHERE city = 'Bengaluru';
```

Running this should return exactly two rows, Omkar Rane and Ishita Menon. If your result includes students from other cities, double check that the condition is written as `city = 'Bengaluru'` and not left out of the query entirely.

## Conclusion

The `WHERE` clause is what turns a table dump into an actual answer: it sits between `FROM` and `ORDER BY`, and it tests every row against a condition before deciding what makes it into the result. Equality, the condition Omkar reached for first, is only the simplest member of a much larger toolkit for describing exactly which rows a query should return, from comparing numbers and dates to matching text and handling missing data, and that toolkit is what comes next.
