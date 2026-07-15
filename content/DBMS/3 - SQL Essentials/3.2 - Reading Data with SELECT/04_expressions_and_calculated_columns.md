## Introduction

Nikhil is building a small course catalog page, and the design calls for two things the courses `table` does not actually store:

- A combined label like "Computer Science: Database Systems" for each `row`
- A "workload score" that doubles the credit value to weight it against another metric the page tracks

Neither of these exists as a `column`. Nothing needs to be added to the `table` to get them, though, because SQL can compute new values on the fly, right inside a `SELECT` list, using the `columns` that already exist.

A value built this way, out of `columns` and operators rather than read directly off disk, is called an **expression**, and when it is given a name in the output, it behaves exactly like a calculated `column`.

## Doing Arithmetic in a SELECT List

The courses `table` stores a `credits` `column` as a plain integer. Nikhil wants a doubled version of it for his workload score, and he gets it by writing the arithmetic directly where a `column` name would normally go.

```postgresql file=courses.sql
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

```postgresql with=courses.sql
SELECT title, credits, credits * 2 AS double_credits
FROM courses;
```

The result carries a third `column`, `double_credits`, holding 8, 8, 6, 6, and 6 for the five courses in that order, double whatever sat in `credits` for that `row`. PostgreSQL computes `credits * 2` fresh for every `row` as it builds the result; nothing about that math is stored anywhere, and running the same `query` again next year, after credit values might have changed, would simply recompute it from whatever `credits` holds then.

The usual arithmetic operators all work the same way inside a `SELECT` list: `+`, `-`, `*`, `/`, and `%` for remainder.

![An arithmetic expression turning credits into a calculated double_credits value](images/07_expression_arithmetic_calculated_column.png)

## Combining Text With Concatenation

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Numbers are not the only thing an expression can build. PostgreSQL lets you glue pieces of text together using the `</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">` operator, called concatenation, which is exactly what Nikhil needs for his combined label.</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
```postgresql with=courses.sql
SELECT department || ': ' || title AS course_label
FROM courses;
```

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Each row now returns a single text value: &quot;Computer Science: Database Systems&quot;, &quot;Computer Science: Data Structures&quot;, &quot;Mathematics: Linear Algebra&quot;, and so on. `</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"><code> takes whatever sits on its left and right, department and a literal string in this case, and joins them into one piece of text, left to right. A literal piece of text written directly in the query, like </code>&#x27;: &#x27;` here, is just a fixed value in single quotes; it is not read from any column, it is simply inserted as-is between the two real column values, giving the colon-and-space separator its shape.</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
![Text concatenation joining department, a separator, and title into one course label](images/08_expression_text_concatenation.png)

## Mixing Expressions With Ordinary Columns

An expression does not have to stand alone. It sits in the `SELECT` list exactly like any real `column`, so a single `query` can freely mix calculated values with `columns` pulled straight from the `table`.

```postgresql with=courses.sql
SELECT course_id, title, credits, credits * 2 AS double_credits, department || ': ' || title AS course_label
FROM courses;
```

This single `query` returns five `columns`: two untouched `columns` straight off the `table`, `course_id` and `title`, alongside `credits` shown plainly, then the doubled value, then the combined label, all computed in one pass over the same five `rows`. Nothing stops a `query` from having as many expressions as it needs sitting beside as many plain `columns` as it needs.

## Expressions at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Expression</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Result for Database Systems (CS, 4 credits)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Arithmetic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>credits * 2 AS double_credits</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>8</code></td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concatenation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>department \|\| &#x27;: &#x27; \|\| title AS course_label</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>Computer Science: Database Systems</code></td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mixed with plain columns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>title, credits, credits * 2 AS double_credits</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>Database Systems</code>, <code>4</code>, <code>8</code></td>
    </tr>
  </tbody>
</table>

## Your Turn

The catalog page also needs a "credit hours per week" figure, assuming each credit corresponds to roughly 15 contact hours across a term, shown alongside the course title. Write a `query` that returns `title` and a calculated `column` named `contact_hours`, equal to `credits * 15`.

```postgresql with=courses.sql
-- Write your query below
```

`SELECT title, credits * 15 AS contact_hours FROM courses;` produces exactly that, showing 60 contact hours for each 4-credit course and 45 for each 3-credit course, computed fresh from whatever `credits` currently holds.

## Conclusion

Expressions turn a `SELECT` list from a plain menu of stored `columns` into a small calculator that runs once per `row`: arithmetic operators combine numbers, `||` combines text, and `AS` gives the result a name worth keeping. None of this changes a single value sitting in the `table`, it only shapes what comes back for that one `query`.

Nikhil's course catalog page can now show its combined "Computer Science: Database Systems" label and doubled workload score straight from a `SELECT`, with no new `column` ever added to the courses `table` itself. With the ability to pick `columns`, rename them, deduplicate them, and compute new ones from them all in hand, the next natural need is controlling the order those `rows` arrive in, rather than accepting whatever order the `database` happens to hand them back.
