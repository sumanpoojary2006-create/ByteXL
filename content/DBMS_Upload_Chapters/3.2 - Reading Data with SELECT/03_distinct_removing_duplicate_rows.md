## Introduction

Simran has been asked a question that sounds like it should have a short answer: "which cities do our students come from?" She writes what feels like the obvious query, selecting the city column from the students table, and runs it. Eight rows come back, one for every student, and Bengaluru shows up twice, Chennai shows up twice, Pune shows up twice.

She scrolls through the list herself, mentally crossing off repeats, to work out that there are really only five distinct cities represented. That is exactly the kind of tedious, error-prone work a database should be doing for her. The tool for it is **`DISTINCT`**, a keyword that tells PostgreSQL to collapse repeated values in a result down to one appearance each.

**Definition:** `DISTINCT` strips a result down to its genuinely unique rows, whether uniqueness is judged on a single column or on the combination of every column named in the `SELECT` list.

![Intro visual for distinct removing duplicate rows](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_intro_distinct_removing_duplicate_rows_actual3d_460189d4.png)

## The Repeated-Rows Problem

Before reaching for `DISTINCT`, it helps to see the problem it solves in plain output. The `students` table holds this data:

| student_id | full_name | email | city | phone | joined_on |
| ---------- | ----------------- | ------------------------------ | --------- | ---------- | ---------- |
| 1 | Ishaan Verma | ishaan.verma@example.com | Bengaluru | 9845011111 | 2025-01-10 |
| 2 | Meera Pillai | meera.pillai@example.com | Chennai | 9884022222 | 2025-01-12 |
| 3 | Arjun Bhat | arjun.bhat@example.com | Bengaluru | *NULL* | 2025-01-15 |
| 4 | Kavya Reddy | kavya.reddy@example.com | Pune | 9922033333 | 2025-01-18 |
| 5 | Rohan Joshi | rohan.joshi@example.com | Hyderabad | 9640044444 | 2025-01-20 |
| 6 | Sneha Gowda | sneha.gowda@example.com | Mysuru | *NULL* | 2025-01-22 |
| 7 | Aditya Kulkarni | aditya.kulkarni@example.com | Pune | 9822055555 | 2025-01-25 |
| 8 | Priya Subramaniam | priya.subramaniam@example.com | Chennai | 9884066666 | 2025-01-28 |

Simran asks for just the `city` column, one value per student, with no `DISTINCT` yet. The query is `SELECT city FROM students;`.

For hands-on practice, `init.sql` creates and populates the displayed `students` table:

```postgresql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    city TEXT,
    phone TEXT,
    joined_on DATE
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
```

The active query file contains the statement being practised:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagyw3" 
 width="100%"
></iframe>

Expected output:

| city |
| --------- |
| Bengaluru |
| Chennai |
| Bengaluru |
| Pune |
| Hyderabad |
| Mysuru |
| Pune |
| Chennai |

The result has eight rows, matching the eight students, and Bengaluru, Chennai, and Pune each appear twice because two students happen to live in each of those cities. Nothing is wrong with this query:

- It is faithfully reporting one city per student.
- It does not answer Simran's actual question, which is about the set of cities involved, not the list of students.

![Selecting city returns repeated city values because each student row contributes one value](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_repeated_values_before_distinct.png)

## Collapsing Repeats With DISTINCT

Adding the word `DISTINCT` right after `SELECT` changes the question from "what city does each student live in" to "what cities appear at all." The query is `SELECT DISTINCT city FROM students;`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagz6z" 
 width="100%"
></iframe>

Expected output:

| city |
| --------- |
| Bengaluru |
| Chennai |
| Pune |
| Hyderabad |
| Mysuru |

This time the result has exactly five rows: Bengaluru, Chennai, Pune, Hyderabad, and Mysuru, each listed once no matter how many students share it. PostgreSQL builds the full list first and then throws away any row whose value is an exact repeat of one already kept. Simran gets the answer to her real question directly, without counting anything by hand.

![DISTINCT filtering duplicate city cards into unique city values](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_distinct_unique_values.png)

## DISTINCT Across More Than One Column

- `DISTINCT` does not have to apply to a single column.
- Given more than one column in the list, it keeps a row only if the entire combination of values, taken together, is unique, not just one column in isolation.
- To see this clearly, it helps to look at a different table where a few rows genuinely repeat the same combination.

The `courses` table holds this data:

| course_id | title | department | credits |
| --------- | -------------------- | ---------------- | ------: |
| 101 | Database Systems | Computer Science | 4 |
| 102 | Data Structures | Computer Science | 4 |
| 103 | Linear Algebra | Mathematics | 3 |
| 104 | Discrete Mathematics | Mathematics | 3 |
| 105 | Microeconomics | Economics | 3 |

The query is `SELECT DISTINCT department, credits FROM courses;`, asking which department-and-credit-load combinations actually exist.

For hands-on practice, a second setup file, `init_002.sql`, creates and populates the displayed `courses` table:

```postgresql
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
(105, 'Microeconomics', 'Economics', 3);
```

The active query file contains the multi-column DISTINCT being practised:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagzfv" 
 width="100%"
></iframe>

Expected output:

| department | credits |
| ---------------- | ------: |
| Computer Science | 4 |
| Mathematics | 3 |
| Economics | 3 |

- The courses table has five rows, but this query returns only three: `Computer Science, 4`, `Mathematics, 3`, and `Economics, 3`.
- Both Computer Science courses are worth 4 credits, so that pair of values collapses into a single row, and the same happens for the two 3-credit Mathematics courses.
- Economics stays on its own since no other row shares its exact department-and-credits combination.
- `DISTINCT` here is answering "which department-and-credit-load combinations actually exist," a genuinely different question from listing every course.

## DISTINCT at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Query</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rows without DISTINCT</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rows with DISTINCT</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>SELECT city FROM students;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8, one per student</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5, one per unique city</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>SELECT department, credits FROM courses;</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5, one per course</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3, one per unique combination</td>
    </tr>
  </tbody>
</table>

## Your Turn

The registrar wants to know which departments the college currently offers courses in, listed once each, with no repeats. Write a query against the courses table above that returns just that.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagzrw" 
 width="100%"
></iframe>

`SELECT DISTINCT department FROM courses;` gets there in one line. Expected output:

| department |
| ---------------- |
| Computer Science |
| Mathematics |
| Economics |

Each department is returned exactly once, even though the underlying table has five course rows spread across those three departments.

## Conclusion

`DISTINCT` strips a result down to its genuinely unique rows, whether uniqueness is judged on a single column or on the combination of every column named in the `SELECT` list. It does not change the underlying table in any way, only the shape of the answer that comes back for that one query. Simran's original question, which cities the students come from, is now a single `SELECT DISTINCT city` away instead of a manual scroll-and-count through eight repeated rows. Knowing how to collapse repeated values is one half of getting a clean result; the other half is being able to compute new values that are not sitting in any column at all, which is exactly the kind of query that comes next.
