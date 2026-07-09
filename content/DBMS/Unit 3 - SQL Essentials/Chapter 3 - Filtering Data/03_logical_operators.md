## Introduction

Varun wants a shortlist of courses worth registering for: something that is either Computer Science or Economics, but only if it carries more than three credits. He writes a single `WHERE` clause with both an `AND` and an `OR` in it, runs it, and gets a course back that clearly does not belong on the list. Nothing is wrong with his data. The problem is that SQL read his conditions in an order he did not intend, and fixing it means learning how the **logical operators**, `AND`, `OR`, and `NOT`, actually combine.

## Combining Conditions with AND and OR

- `AND` keeps a row only when every condition attached to it is true.
- `OR` keeps a row when at least one condition is true.

Both let a single `WHERE` clause test more than one thing at a time.

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

```postgresql with=schema.sql
SELECT full_name, city
FROM students
WHERE city = 'Bengaluru' AND phone IS NOT NULL;
```

Both Bengaluru students, Omkar Rane and Ishita Menon, have a phone number on file, so `AND` keeps both rows here. Now compare it with `OR` over a different pair of conditions on the courses table.

```postgresql with=schema.sql
SELECT title, department
FROM courses
WHERE department = 'Mathematics' OR department = 'Economics';
```

This returns three rows: `Linear Algebra`, `Discrete Mathematics`, and `Microeconomics`. `OR` only needs one side of the condition to be true, so every course in either department qualifies.

## Where Parentheses Actually Matter

Here is the query Varun originally wrote for his shortlist, exactly as he typed it.

```postgresql with=schema.sql
SELECT title, department, credits
FROM courses
WHERE department = 'Computer Science' AND credits > 3 OR department = 'Economics';
```

This returns three courses: `Database Systems`, `Data Structures`, and `Microeconomics`, even though `Microeconomics` carries only two credits, well below the "more than three" requirement Varun cares about. The reason is that SQL evaluates `AND` before `OR` when neither is grouped by parentheses, the same way multiplication is evaluated before addition in ordinary arithmetic. Varun's clause was actually read as `(department = 'Computer Science' AND credits > 3) OR department = 'Economics'`, so any Economics course sneaks in regardless of its credit value.

Adding parentheses around the department check fixes it, because it forces the `OR` to be settled first, and only then does `AND` check the credit requirement against that combined result.

```postgresql with=schema.sql
SELECT title, department, credits
FROM courses
WHERE (department = 'Computer Science' OR department = 'Economics') AND credits > 3;
```

Now only `Database Systems` and `Data Structures` come back. `Microeconomics` is correctly dropped, since it fails the `credits > 3` test once that test is applied to the right group of rows. The SQL text barely changed, four characters, but the meaning changed completely, which is exactly why relying on operator precedence to do the right thing by accident is worth avoiding whenever `AND` and `OR` appear in the same `WHERE` clause.

## NOT Reverses a Condition

`NOT` flips a condition's truth value: rows that would have matched are excluded, and rows that would not have matched are included instead.

```postgresql with=schema.sql
SELECT title, credits
FROM courses
WHERE NOT credits > 3;
```

This returns `Linear Algebra`, `Discrete Mathematics`, and `Microeconomics`, the three courses whose credit value is not greater than three. It reads naturally alongside `AND` and `OR`, and like both of them, it can be wrapped in parentheses to control exactly which condition it applies to when the clause grows more complex.

## Logical Operators at a Glance

| Operator | Keeps a row when | Precedence versus the others |
|---|---|---|
| `AND` | Every joined condition is true | Evaluated before OR |
| `OR` | At least one joined condition is true | Evaluated after AND unless grouped |
| `NOT` | The condition following it is false | Applies to whatever it is placed directly before |
| `( )` | N/A | Forces a group to be evaluated as one unit first |

## Your Turn

Write a query against `courses` for departments that are Mathematics or Computer Science, restricted to courses worth at least four credits, and use parentheses so the grouping is unambiguous.

```postgresql with=schema.sql
SELECT title, department, credits
FROM courses
WHERE (department = 'Mathematics' OR department = 'Computer Science') AND credits >= 4;
```

This should return exactly `Database Systems` and `Data Structures`. Both Mathematics courses carry only three credits, so they are correctly excluded once the parentheses force the department check to be grouped before the credit check applies to it.

## Conclusion

`AND`, `OR`, and `NOT` let a single `WHERE` clause weigh several conditions at once, but `AND` silently binds tighter than `OR` whenever both appear together ungrouped, which is precisely the kind of quiet behaviour that turns a reasonable-looking query into a wrong answer. Parentheses remove the ambiguity by stating the grouping explicitly rather than leaving it to a precedence rule the reader may not be thinking about. Varun's shortlist now correctly grouped, `(department = 'Computer Science' OR department = 'Economics') AND credits > 3`, returns only the two Computer Science courses he actually wanted, with Microeconomics no longer sneaking in under its two credits. With conditions on numbers, dates, and now combinations of several conditions all covered, the next gap is text that is not an exact match at all, finding rows by a partial pattern rather than a known value.
