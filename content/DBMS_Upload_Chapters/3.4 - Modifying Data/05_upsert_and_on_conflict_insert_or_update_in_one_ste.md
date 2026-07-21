## Introduction

Aditya is processing a batch of enrollment submissions that arrived from a paper form, and the batch has a problem: some of these student-course pairings are brand new and simply need to be inserted, while others already exist in the table from an earlier submission and just need their grade corrected.

Worse, he cannot tell which is which until he checks, and checking first with a `SELECT` and then deciding whether to `INSERT` or `UPDATE` is not just clumsy to write, it can go wrong if two people are processing the same batch at the same time and both check before either one writes.

What Aditya needs is a single statement that inserts a row if it is new and updates it if it already exists, and PostgreSQL provides exactly that with **`ON CONFLICT`**, the clause behind what is commonly called an upsert.

**Definition:** An **upsert** is a single operation that inserts a new row when no matching row exists or updates the existing row when a uniqueness conflict occurs; PostgreSQL implements it with `INSERT ... ON CONFLICT`.

![Intro visual for upsert and on conflict insert or update in](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44sjn9mdv/05_intro_upsert_and_on_conflict_insert_or_update_in_one_s.png)

## Setting Up a Uniqueness Rule to Conflict Against

The `students`, `courses`, and `enrollments` tables hold this data:

| student_id | full_name | city |
| ---------- | ----------- | --------- |
| 1 | Omkar Rane | Bengaluru |
| 2 | Neha Sharma | Mysuru |
| 3 | Varun Nair | Chennai |

| course_id | title | department | credits |
| --------- | ---------------- | ---------------- | ------: |
| 101 | Database Systems | Computer Science | 4 |
| 102 | Data Structures | Computer Science | 4 |
| 103 | Linear Algebra | Mathematics | 3 |

| enrollment_id | student_id | course_id | enrolled_on | grade |
| ------------- | ---------- | --------- | ---------- | ------ |
| 1 | 1 | 101 | 2025-02-01 | A |
| 2 | 2 | 101 | 2025-02-02 | *NULL* |
| 3 | 3 | 103 | 2025-02-03 | B+ |

A setup file builds this starting point with `CREATE TABLE` and `INSERT INTO`. An upsert only makes sense once the database has a rule to check a new row against, so the `enrollments` table is created with a `UNIQUE (student_id, course_id)` constraint, which states plainly that the same student cannot be enrolled in the same course twice. That constraint line is what gives `ON CONFLICT` something concrete to react to; without it, PostgreSQL would have no rule saying two rows with the same student_id and course_id are a problem, and there would be nothing for an upsert to "conflict" against at all.

![A UNIQUE student_id plus course_id rule detecting a duplicate enrollment conflict](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_upsert_unique_conflict_rule.png)

### Hands-On Practice: Prepare the Tables

The OneCompiler exercise uses two files. `init.sql` creates and populates the starting tables, including the `UNIQUE` constraint. The active query file contains only the statement being practised. Because each run reloads `init.sql`, the dataset is always fresh.

First, `init.sql` prepares the source tables:

```postgresql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    full_name TEXT,
    city TEXT
);

INSERT INTO students (student_id, full_name, city) VALUES
(1, 'Omkar Rane', 'Bengaluru'),
(2, 'Neha Sharma', 'Mysuru'),
(3, 'Varun Nair', 'Chennai');

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
    grade TEXT,
    UNIQUE (student_id, course_id)
);

INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade) VALUES
(1, 1, 101, '2025-02-01', 'A'),
(2, 2, 101, '2025-02-02', NULL),
(3, 3, 103, '2025-02-03', 'B+');
```

The active query files below all run against this same prepared dataset.

## INSERT ... ON CONFLICT DO UPDATE

Aditya's first case: Neha Sharma's Database Systems enrollment already exists with no grade recorded, and the new submission carries her final grade, B+. He writes this as a single statement: `INSERT INTO enrollments (...) VALUES (4, 2, 101, '2025-02-02', 'B+') ON CONFLICT (student_id, course_id) DO UPDATE SET grade = EXCLUDED.grade RETURNING ...;`.

Expected output, directly from the `RETURNING` clause:

| enrollment_id | student_id | course_id | grade |
| ------------- | ---------- | --------- | ----- |
| 2 | 2 | 101 | B+ |

PostgreSQL processed this in three steps:

1. It tried the `INSERT` exactly as written.

2. It detected that student_id 2 and course_id 101 already matched the `UNIQUE` constraint.

3. Instead of raising an error, it ran the `DO UPDATE SET` instead, targeting the row that was already there.

- The result shows enrollment_id 2, the row that already existed, now carrying grade B+, not a new row with enrollment_id 4.
- `EXCLUDED.grade` refers to the grade value from the row that was proposed for insertion, the B+ that never actually got inserted, letting the `UPDATE` branch reuse it without retyping it.

### Hands-On Practice: Upsert That Updates

Keep the same `init.sql` file and change only the active query file:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafh5v" 
 width="100%"
></iframe>

## The Same Statement, Genuinely Inserting

Aditya's second case: Varun Nair has newly registered for Data Structures, course_id 102, a pairing that has never been submitted before. The same upsert shape, `INSERT INTO enrollments (...) VALUES (5, 3, 102, '2025-02-10', NULL) ON CONFLICT (student_id, course_id) DO UPDATE SET grade = EXCLUDED.grade RETURNING ...;`, handles it.

Expected output, directly from the `RETURNING` clause:

| enrollment_id | student_id | course_id | grade |
| ------------- | ---------- | --------- | ------ |
| 5 | 3 | 102 | *NULL* |

This time enrollment_id 5 appears in the result, a genuinely new row, because student_id 3 and course_id 102 had never been paired before and there was no conflict to react to.

The exact same statement Aditya used a moment ago to update an existing row here performs a plain insert instead, because `ON CONFLICT` only changes behavior when a conflict is actually detected; otherwise the `INSERT` proceeds exactly as it would have without the clause at all.

![ON CONFLICT branching to INSERT when there is no conflict and UPDATE when there is one](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_upsert_insert_or_update_branch.png)

### Hands-On Practice: Upsert That Inserts

Keep the same `init.sql` file and change only the active query file:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafhev" 
 width="100%"
></iframe>

## ON CONFLICT DO NOTHING for the Simpler Case

Sometimes there is no update to make at all, only a wish to insert a row if it is not already there and quietly skip it otherwise. `DO NOTHING` covers exactly that: `INSERT INTO enrollments (...) VALUES (6, 1, 101, '2025-02-01', 'A') ON CONFLICT (student_id, course_id) DO NOTHING RETURNING ...;`.

Expected output:

*(no rows returned)*

Nothing comes back from `RETURNING` at all, because student_id 1 and course_id 101 already exist as enrollment 1, and `DO NOTHING` means precisely that: the conflicting row is left exactly as it was, no error is raised, and no update happens either. This is the right choice whenever re-submitting an already-known pairing should simply be a harmless no-op rather than a correction.

### Hands-On Practice: Upsert That Does Nothing

Keep the same `init.sql` file and change only the active query file:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafhrf" 
 width="100%"
></iframe>

## Why Not Just Check First, Then Decide

- Aditya's original instinct, a `SELECT` to check for the row followed by an `INSERT` or an `UPDATE` depending on the answer, takes two or three separate statements and a decision made in between them by whatever program is driving the process.
- If two submissions for the same student-course pairing are being processed at nearly the same moment, both could run their `SELECT`, both could see no existing row yet, and both could then attempt an `INSERT`, one of which fails or, worse, both of which succeed and violate the very constraint meant to prevent duplicates.
- `ON CONFLICT` avoids this entirely because the check and the action happen as one atomic statement handled by the database itself, with no gap in between for another process to interfere.

## UPSERT at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Clause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Behavior on conflict</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Behavior with no conflict</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ON CONFLICT (cols) DO UPDATE SET ...</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Updates the existing row using EXCLUDED values</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performs a plain INSERT</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ON CONFLICT (cols) DO NOTHING</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Leaves the existing row untouched, no error</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performs a plain INSERT</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No ON CONFLICT clause</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Raises a uniqueness violation error</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performs a plain INSERT</td>
    </tr>
  </tbody>
</table>

## Your Turn

Omkar Rane's Linear Algebra grade needs to be recorded for the first time as A-, using an upsert in case it was already partially submitted.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafj8f" 
 width="100%"
></iframe>

A working answer is `INSERT INTO enrollments (enrollment_id, student_id, course_id, enrolled_on, grade) VALUES (7, 1, 103, '2025-02-11', 'A-') ON CONFLICT (student_id, course_id) DO UPDATE SET grade = EXCLUDED.grade RETURNING enrollment_id, student_id, course_id, grade;`. Expected output, directly from the `RETURNING` clause:

| enrollment_id | student_id | course_id | grade |
| ------------- | ---------- | --------- | ----- |
| 7 | 1 | 103 | A- |

Since Omkar had never registered for course 103 before, this returns enrollment_id 7 as a genuinely new row with grade A-, showing the same statement handles a fresh pairing just as correctly as a repeated one.

## Conclusion

`ON CONFLICT` turns a two-step, race-prone guess into a single statement that always does the right thing, updating a row that is already there or inserting one that is not, decided by the database itself rather than by a program hoping nothing changes in between its own check and its own write:

`DO UPDATE SET` is for when a repeat submission should correct something. `DO NOTHING` is for when a repeat submission should simply be ignored.

Aditya can now run his whole batch of enrollment submissions through a single `ON CONFLICT` statement without first sorting new pairings from corrections by hand, trusting the database to insert or update each row correctly even if two clerks process overlapping paper forms at the same time.

Between naming columns carefully on `INSERT`, guarding `UPDATE` and `DELETE` with a `WHERE` clause checked in advance, and now resolving conflicts atomically, the common thread running through all of it is the same: changing data well is less about memorizing syntax and more about knowing, before a statement runs, exactly what it is about to do.
