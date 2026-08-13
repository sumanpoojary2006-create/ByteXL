## Introduction

Omkar is pulling together a report of Computer Science offerings for his advisor. His first attempt retrieves the entire course catalogue. The result includes Mathematics and Economics courses, so he has to scroll past rows that have nothing to do with what his advisor asked for.

What he actually needs is a way to tell the database "only hand me back the rows where this is true," and that instruction has a name: the **`WHERE` clause**.

![WHERE acting as a filter gate that keeps matching Computer Science rows and blocks other rows](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_where_filter_keeps_matching_rows.png)

**Definition:** The `WHERE` clause is what turns a table dump into an actual answer: it sits between `FROM` and `ORDER BY`, and it tests every row against a condition before deciding what makes it into the result.

## Filtering Rows Instead of Reading All of Them

A `SELECT` without a `WHERE` clause returns every row a table has. Add a `WHERE` clause and the database tests each row against a condition, keeping only the rows where that condition is true and discarding the rest before the result ever reaches Omkar's screen.

The `courses` table is the only dataset needed for this lesson. Before looking at the filtering query, inspect all five stored rows:

| course_id | title | department | credits |
| --------- | -------------------- | ---------------- | ------: |
| 101 | Database Systems | Computer Science | 4 |
| 102 | Data Structures | Computer Science | 4 |
| 103 | Linear Algebra | Mathematics | 3 |
| 104 | Discrete Mathematics | Mathematics | 3 |
| 105 | Microeconomics | Economics | 2 |

To create this dataset for practice, `CREATE TABLE` defines the four columns, and `INSERT INTO` adds the five displayed rows. Those statements belong in the setup file. They prepare the data but do not explain filtering, so the lesson first focuses on the `WHERE` query itself.

Omkar needs only the Computer Science courses. The query is `SELECT title, department, credits FROM courses WHERE department = 'Computer Science';`.

- `SELECT title, department, credits` chooses the columns that will appear.
- `FROM courses` identifies the source table.
- `WHERE department = 'Computer Science'` tests each row and keeps it only when its department matches the required value.

Expected output:

| title | department | credits |
| ---------------- | ---------------- | ------: |
| Database Systems | Computer Science | 4 |
| Data Structures | Computer Science | 4 |

Only `Database Systems` and `Data Structures` come back. The database evaluated the condition `department = 'Computer Science'` against every row in `courses`, kept the two rows where it held true, and dropped the mathematics and economics rows entirely. Omkar's advisor never even sees the rows that did not qualify.

## Hands-On Practice: Filter the Courses Table

First, `init.sql` prepares the dataset:

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
(105, 'Microeconomics', 'Economics', 2);
```

Then the active query file applies the filter:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakbxp" 
 width="100%"
></iframe>

Run the active query file. `init.sql` loads first, and the result contains the same two Computer Science courses shown above.

## Where WHERE Sits in a Query

The clause has a fixed position: it comes right after `FROM` and before `ORDER BY` or `LIMIT`. That ordering reflects the work the database performs: choose a source table, keep the matching rows, sort those survivors, and finally limit the result if required.

Suppose Omkar wants the Mathematics courses arranged alphabetically. The query is `SELECT title, department FROM courses WHERE department = 'Mathematics' ORDER BY title;`. `WHERE` first keeps the Mathematics rows, and `ORDER BY` then sorts only those matching rows by title.

Expected output:

| title | department |
| -------------------- | ----------- |
| Discrete Mathematics | Mathematics |
| Linear Algebra | Mathematics |

Both Mathematics courses survive the filter. `Discrete Mathematics` appears first because the surviving rows are then sorted alphabetically by `title`. Writing `ORDER BY` before `WHERE` is invalid because SQL requires the clauses in their defined order.

Try the explained query in the active file while keeping the same `init.sql` setup:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakc9g" 
 width="100%"
></iframe>

![SQL clause order showing WHERE filtering rows before ORDER BY sorts and LIMIT trims](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_where_clause_order.png)

## Clauses at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Clause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Runs relative to WHERE</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>SELECT</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Chooses which columns appear in the result</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decided last, on the surviving rows</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>FROM</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Names the table to read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Before WHERE</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>WHERE</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keeps only the rows matching a condition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The filtering step itself</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ORDER BY</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Arranges the surviving rows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">After WHERE</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>LIMIT</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Caps how many surviving rows are returned</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">After WHERE and ORDER BY</td>
    </tr>
  </tbody>
</table>

## Every Condition Is Just a True-or-False Test

`department = 'Computer Science'` and `department = 'Mathematics'` are equality checks, the simplest kind of condition `WHERE` can hold. But `WHERE` accepts far more than equality:

- Compare numbers and dates
- Combine several conditions together
- Match partial text patterns
- Handle missing values

Every one of those is really the same idea underneath, a test that a row either passes or fails, and what follows is simply a tour of the different kinds of tests you can write.

## Your Turn

Using the same `courses` table, write a query that returns the `title`, `department`, and `credits` of every Economics course. The condition to apply is `department = 'Economics'`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakckh" 
 width="100%"
></iframe>

Expected output:

| title | department | credits |
| -------------- | ---------- | ------: |
| Microeconomics | Economics | 2 |

The result contains only `Microeconomics` because it is the only row whose `department` value is `Economics`. If other courses appear, check that the `WHERE` clause is present and that the text value is enclosed in single quotes.

## Conclusion

The `WHERE` clause is what turns a table dump into an actual answer: it sits between `FROM` and `ORDER BY`, and it tests every row against a condition before deciding what makes it into the result.

Equality, the condition Omkar reached for first, is only the simplest member of a much larger toolkit for describing exactly which rows a query should return, from comparing numbers and dates to matching text and handling missing data, and that toolkit is what comes next.
