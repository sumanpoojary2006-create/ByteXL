## Introduction

Siddharth has been asked to pull together a list of everyone still using their college-issued email address, ahead of a migration to a new mail provider. He does not have a fixed value to compare against; he cannot write `email = 'something'` because the local part of every address is different, it is only the ending that is shared. What he needs is a way to match a partial shape of text rather than an exact value, and that is what **pattern matching** with `LIKE` is for.

## Matching Part of a String with LIKE

`LIKE` compares a text column against a pattern instead of a fixed value. The pattern can include two special wildcard characters:

- `%` stands in for any number of characters, including zero.
- `_` stands in for exactly one character.

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
SELECT full_name, email
FROM students
WHERE email LIKE '%campusmail.edu';
```

Five students come back: Omkar Rane, Neha Sharma, Siddharth Rao, Ishita Menon, and Sanya Iyer. The `%` before `campusmail.edu` means "anything at all can appear before this text," so the pattern matches regardless of what the local part of the address looks like, as long as the address ends with `campusmail.edu`. Varun Nair, Yusuf Khan, and Rahul Verma are left out, since their addresses end with `gmail.com` instead.

## Anchoring a Pattern to the Start or Middle

`%` is not limited to the end of a pattern. Placing it at the start checks a suffix, placing it in the middle checks that two fragments both appear in order, and leaving it off one side anchors the match to that side.

```postgresql with=schema.sql
SELECT full_name
FROM students
WHERE full_name LIKE 'S%';
```

This returns Siddharth Rao and Sanya Iyer, the two students whose name begins with the letter S. The trailing `%` in `'S%'` is doing the real work here: it is what allows any amount of text to follow the S, matching a name of any length as long as it starts with that letter. `LIKE` never adds a wildcard on its own, so dropping that `%` and writing `full_name LIKE 'S'` would demand an exact, single-character match and return nothing at all, since no student's full name is just the letter S by itself.

## Matching Exactly One Character with _

`_` is stricter than `%`. It stands for exactly one character, no more and no fewer, which makes it useful when you know the shape of the text but not one specific letter in it.

```postgresql with=schema.sql
SELECT full_name
FROM students
WHERE full_name LIKE '_a%';
```

Three names come back: Varun Nair, Rahul Verma, and Sanya Iyer. The pattern says "any single character, followed by the letter a, followed by anything," and all three names happen to have `a` as their second letter. Compare this with `full_name LIKE 'a%'`, which would look for names starting with `a` itself, a completely different and, in this data, empty result.

## Case-Insensitive Matching with ILIKE

`LIKE` is case-sensitive by default, so a pattern written in uppercase will not match lowercase text. PostgreSQL offers `ILIKE` as a convenience that matches regardless of letter case, which is handy when you are not sure how something was typed in.

```postgresql with=schema.sql
SELECT full_name, email
FROM students
WHERE email ILIKE '%GMAIL%';
```

This still returns Varun Nair, Yusuf Khan, and Rahul Verma, even though the pattern is written in uppercase and the stored addresses are all lowercase. Swapping `ILIKE` for `LIKE` here with the same uppercase pattern would return nothing at all, since `LIKE` treats `GMAIL` and `gmail` as different text entirely. `ILIKE` is specific to PostgreSQL; other database systems handle case-insensitive matching differently, so it is worth knowing it is a PostgreSQL convenience rather than a universal SQL feature.

## Pattern Matching at a Glance

| Symbol or keyword | Matches | Example | Matches values like |
|---|---|---|---|
| `%` | Any number of characters, including none | `'%edu'` | `omkar.rane@campusmail.edu` |
| `_` | Exactly one character | `'_a%'` | `Sanya`, `Varun`, `Rahul` |
| `LIKE` | Case-sensitive pattern match | `'S%'` | `Siddharth`, `Sanya` |
| `ILIKE` | Case-insensitive pattern match (PostgreSQL) | `'%GMAIL%'` | any casing of "gmail" |

## Your Turn

Write a query that finds every student whose email address contains the text "verma", regardless of where it appears in the address.

```postgresql with=schema.sql
SELECT full_name, email
FROM students
WHERE email LIKE '%verma%';
```

This should return exactly one row, Rahul Verma, since his email address is the only one containing that fragment anywhere in it. Try replacing `%verma%` with just `verma%` and notice the result becomes empty, since that pattern demands the address start with "verma" rather than merely contain it.

## Conclusion

`LIKE` turns `WHERE` from a tool that only recognises exact values into one that can recognise a shape of text, using `%` for a stretch of any length and `_` for a single fixed position, with `ILIKE` available whenever letter case should not matter. Siddharth can now pull his full list of college-issued addresses ahead of the mail migration with a single `WHERE email LIKE '%campusmail.edu'`, without ever needing a fixed value to match against. Text is not the only place an exact match falls short, though. Some columns do not hold a value at all, and comparing against nothing behaves in a way that trips up almost everyone the first time they meet it.
