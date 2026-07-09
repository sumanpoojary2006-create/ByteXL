## Introduction

Pooja has a server running, a client she knows how to open, and absolutely nothing stored inside either of them yet. Her task is to start building a small system for the training institute she interns at, one that keeps track of students, the courses they take, the instructors who teach those courses, and which student is enrolled in which course. Every tutorial she has skimmed so far has talked about databases, `schemas`, and tables as if she already knows how they nest inside one another, and she does not, not really, not in a way she could explain back.

So she asks the question plainly: if a PostgreSQL server can hold many things at once, what exactly holds what? The answer turns out to be a clean, three-level nesting:

1. A single running server can hold several **databases**, each one a fully separate world of data with its own tables.
2. Each database can in turn hold several **schemas**, named groupings that keep related tables together under one label, useful the moment more than one project or team shares a database.
3. Each `schema` holds the actual **tables**, the row-and-column structures where real data finally lives.

Server, then database, then `schema`, then table, each level nested inside the one before it. Today Pooja builds the bottom two levels of that nesting for real, for the first time.

## Why a Fresh Database Is Usually a Manual, Local Step

Creating a brand-new database is normally the very first move in any real project, done once, before anything else. It looks like this on a machine you control directly:

```text
-- Typed inside a psql session already connected to the server
CREATE DATABASE campus_training;

-- Then reconnect into the new database
\c campus_training
```

That single `CREATE DATABASE` statement asks the server to set up an entirely new, independent storage area named `campus_training`, separate from any other database already on the server. This is illustrated here rather than run live, because a shared online SQL environment already hands you one connected database to work inside for the session, and cannot spin up or switch between separate physical databases the way your own local install can. On your own machine, this is the very first command you would type. Here, and in every runnable example that follows, assume that database already exists and is where you are connected.

## Building the Schema and Tables for Pooja's Institute

Inside that one database, Pooja's next job is to organize her tables sensibly rather than dumping everything into one undifferentiated pile, and to actually define what a student record and a course record look like. She reaches for a `schema` named `campus` to hold everything belonging to this project, and then defines two tables inside it: `students`, one row per person enrolled at the institute, and `courses`, one row per course on offer. Every column gets a type that honestly matches the value it will hold, a habit she picked up from designing tables long before she ever touched live SQL.

```postgresql
CREATE SCHEMA IF NOT EXISTS campus;

CREATE TABLE campus.students (
    student_id  integer PRIMARY KEY,
    full_name   text NOT NULL,
    email       text NOT NULL,
    city        text,
    phone       text,
    joined_on   date NOT NULL
);

CREATE TABLE campus.courses (
    course_id   integer PRIMARY KEY,
    title       text NOT NULL,
    department  text NOT NULL,
    credits     integer NOT NULL
);

INSERT INTO campus.students (student_id, full_name, email, city, phone, joined_on) VALUES
    (1, 'Meera Nair', 'meera.nair@example.com', 'Kochi', '9876500001', '2026-01-12'),
    (2, 'Arjun Das', 'arjun.das@example.com', 'Bengaluru', NULL, '2026-01-15'),
    (3, 'Fatima Sheikh', 'fatima.sheikh@example.com', 'Hyderabad', '9876500003', '2026-02-01');

INSERT INTO campus.courses (course_id, title, department, credits) VALUES
    (101, 'Database Fundamentals', 'Computer Science', 4),
    (102, 'Business Communication', 'Management', 2),
    (103, 'Applied Statistics', 'Mathematics', 3);

SELECT * FROM campus.students;
SELECT * FROM campus.courses;
```

Reading through what each part does: `CREATE SCHEMA IF NOT EXISTS campus` sets up the named grouping first, since both tables need somewhere to live, and the `IF NOT EXISTS` guard means rerunning this statement will not fail with an error if the `schema` is already there. Each `CREATE TABLE` statement then lists its columns, one per line, together with a type, `integer` for whole-number identifiers and credit counts, `text` for names and free-form strings, `date` for the enrollment date, and `PRIMARY KEY` marking the column that uniquely identifies each row. Writing `campus.students` rather than just `students` everywhere is what actually places the table inside the `campus` `schema` instead of PostgreSQL's default, unlabelled location. The two `INSERT INTO` statements add a handful of realistic rows, and notice that Arjun's phone number is left as `NULL`, since that column was defined without a `NOT NULL` requirement and not every student has necessarily shared one. The final two `SELECT * FROM` statements ask PostgreSQL to hand back every column of every row in each table, which is exactly how Pooja confirms the tables were not just created but genuinely hold the data she just inserted.

## Reading What Came Back

Running that block, Pooja sees three rows appear under `students`, matching what she inserted, with Arjun's phone column showing as empty rather than an error, exactly as expected for a nullable column with no value supplied. The `courses` table likewise shows all three rows she added, each with its department and credit count intact. Nothing here required a leap of faith; the same statements that built the structure and inserted the rows are answered right back by a plain `SELECT`, which is the simplest possible proof that a table exists and is not empty.

This `campus` `schema`, and the `students` and `courses` tables sitting inside it, are not a one-off exercise. They form the running example this entire stretch of learning returns to again and again, alongside two more tables, one for instructors and one for enrollments linking a specific student to a specific course, that will be built out as the need for them arises. Every SQL idea from here forward gets demonstrated against this same small, familiar institute rather than a new invented scenario each time.

## Creating a Database, Schema, and Table at a Glance

| Level | Statement | What it holds |
|---|---|---|
| Database | `CREATE DATABASE campus_training;` | An entire independent storage area on the server |
| Schema | `CREATE SCHEMA campus;` | A named grouping of related tables inside one database |
| Table | `CREATE TABLE campus.students (...);` | Actual rows of structured data, one table at a time |
| Row | `INSERT INTO campus.students VALUES (...);` | One concrete record inside a table |

## Conclusion

The nesting Pooja set out to understand turned out to be exactly as tidy as it sounded: a server holds databases, a database holds `schemas`, and a `schema` holds the tables where rows of real data actually live. Working through that nesting for real, by creating a `schema`, defining two tables with sensibly chosen column types, inserting a handful of believable rows, and reading them straight back with a plain query, is the moment SQL stopped being something Pooja read about and became something she typed, ran, and watched work.

With a small, real institute database now sitting there, holding actual students and actual courses, the natural next step is learning how to ask richer questions of it, starting with the single statement responsible for pulling data back out in whatever shape you need.
