## Introduction

Tanvi is building a small dashboard widget titled "Recent Enrollments" for the department office's home screen, and the design only has room for five rows. The enrollments table behind it, though, holds every enrollment ever recorded, and that number only grows term after term. Pulling the whole table and cutting it down to five rows in whatever code renders the widget would work, but it means dragging far more data across the network than the screen will ever show. What Tanvi actually wants is to ask the database itself for just the first few rows of a result, and SQL has a clause built for exactly that request: **`LIMIT`**.

## Cutting a Result Down to N Rows

The enrollments table links students to the courses they have taken, along with the date they enrolled and, once available, a grade.

```postgresql file=schema.sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    city TEXT,
    phone TEXT,
    joined_on DATE
);

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT,
    department TEXT,
    credits INTEGER
);

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER REFERENCES students(student_id),
    course_id INTEGER REFERENCES courses(course_id),
    enrolled_on DATE,
    grade TEXT
);

INSERT INTO students (student_id, full_name, email, city, phone, joined_on) VALUES
(1, 'Ishaan Verma', 'ishaan.verma@example.com', 'Bengaluru', '9845011111', '2025-01-10'),
(2, 'Meera Pillai', 'meera.pillai@example.com', 'Chennai', '9884022222', '2025-01-12'),
(3, 'Arjun Bhat', 'arjun.bhat@example.com', 'Bengaluru', NULL, '2025-01-15'),
(4, 'Kavya Reddy', 'kavya.reddy@example.com', 'Pune', '9922033333', '2025-01-18'),
(5, 'Rohan Joshi', 'rohan.joshi@example.com', 'Hyderabad', '9640044444', '2025-01-20'),
(6, 'Sneha Gowda', 'sneha.gowda@example.com', 'Mysuru', NULL, '2025-01-22'),
(7, 'Aditya Kulkarni', 'aditya.kulkarni@example.com', 'Pune', '9822055555', '2025-01-25'),
(8, 'Priya Subramaniam', 'priya.subramaniam@example.com', 'Chennai', '9884066666', '2025-01-28');

INSERT INTO courses (course_id, title, department, credits) VALUES
(101, 'Database Systems', 'Computer Science', 4),
(102, 'Data Structures', 'Computer Science', 4),
(103, 'Linear Algebra', 'Mathematics', 3),
(104, 'Discrete Mathematics', 'Mathematics', 3),
(105, 'Microeconomics', 'Economics', 3);

INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade) VALUES
(1, 1, 101, '2025-02-01', 'A'),
(2, 1, 103, '2025-02-01', 'B'),
(3, 2, 105, '2025-02-03', 'A'),
(4, 3, 101, '2025-02-05', NULL),
(5, 4, 102, '2025-02-08', 'B'),
(6, 5, 104, '2025-02-10', 'A'),
(7, 6, 101, '2025-02-12', NULL),
(8, 7, 105, '2025-02-15', 'C'),
(9, 8, 103, '2025-02-18', 'B'),
(10, 2, 102, '2025-02-20', NULL);
```

```postgresql with=schema.sql
SELECT student_id, course_id, enrolled_on
FROM enrollments
ORDER BY enrolled_on DESC
LIMIT 5;
```

The enrollments table has ten rows in it, but this query returns exactly five: the five most recently enrolled records, newest first. Two clauses divide the work:

- `ORDER BY enrolled_on DESC` does the real work of deciding which rows count as "recent."
- `LIMIT 5`, placed after it, simply keeps the first five rows of that already-sorted result and drops the rest.

This is precisely Tanvi's dashboard widget, in one query, with the database doing the trimming instead of any application code downstream.

## Why LIMIT Needs ORDER BY to Mean Anything Useful

`LIMIT` on its own, with no `ORDER BY`, still runs and still returns some number of rows, but which rows it happens to return is not something a query should ever depend on. Without a sort, "the first five rows" is just whatever order the table happens to be stored or scanned in internally, which can change between runs, after an update, or after PostgreSQL chooses a different way to fetch the data. A "top 5" or "most recent 5" request only makes sense once the rows have been put into the order that "top" or "most recent" refers to, which is exactly why `LIMIT` is almost always paired with an `ORDER BY` that defines what that top actually means.

```postgresql with=schema.sql
SELECT student_id, course_id, enrolled_on
FROM enrollments
LIMIT 5;
```

This still returns five rows, but nothing in the query says they are the five most recent, the five earliest, or anything meaningful at all. Compare that to the sorted version above, and the difference in what the result actually promises becomes clear.

## Skipping Ahead With OFFSET

A dashboard widget usually only needs the very front of a result, but a paginated list, like a "page 2 of enrollments" view in an admin screen, needs to skip past rows already shown on page 1. `OFFSET`, placed after `LIMIT`, tells PostgreSQL how many rows to skip before it starts collecting the ones to return.

```postgresql with=schema.sql
SELECT student_id, course_id, enrolled_on
FROM enrollments
ORDER BY enrolled_on DESC
LIMIT 5 OFFSET 5;
```

This returns the next five most recent enrollments, the ones ranked sixth through tenth by enrollment date, since the first five were already shown on an earlier page and this query skips past them with `OFFSET 5`. A page 3 request, if the data were large enough, would simply change `OFFSET 5` to `OFFSET 10`, skipping the first ten rows before collecting the next batch of five.

## LIMIT and OFFSET at a Glance

| Clause | Purpose | Example |
|---|---|---|
| `LIMIT 5` | Keep only the first 5 rows of the (sorted) result | Dashboard preview, "top 5" widgets |
| `ORDER BY ... LIMIT 5` | Define what "top" or "recent" means, then trim to 5 | Most reliable, meaningful way to use LIMIT |
| `LIMIT 5 OFFSET 5` | Skip the first 5 rows, then return the next 5 | Page 2 of a paginated list |

## Your Turn

The department office wants a "highest workload" preview: the three courses with the most credits, and among courses tied on credits, the ones whose title comes first alphabetically. Write a query against the courses table above that returns `title` and `credits`, sorted appropriately, and limited to 3 rows.

```postgresql with=schema.sql
-- Write your query below
```

`SELECT title, credits FROM courses ORDER BY credits DESC, title LIMIT 3;` sorts by credits from highest to lowest, breaks any tie by title alphabetically, and keeps only the top three rows, giving Data Structures, Database Systems, and one of the 3-credit courses depending on alphabetical order among the remaining ties.

## Conclusion

`LIMIT` trims a result down to a manageable number of rows, and `OFFSET` lets a query skip past rows already handled, together making dashboard previews and paginated views practical without ever pulling more data than a screen can use. Neither clause means much on its own, since "the first few rows" only becomes a meaningful promise once `ORDER BY` has decided what order those rows are actually in. Tanvi's "Recent Enrollments" widget can now ask the database directly for just its five rows, sorted newest first, instead of dragging the entire growing enrollments table across the network to trim it down in code. With the ability to choose columns, rename them, deduplicate them, compute new ones, sort them, and trim them all in place, the remaining piece of everyday querying is deciding which rows even qualify for a result in the first place, which is where a precise condition on the data itself comes in.
