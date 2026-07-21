## Introduction

Varun wants a shortlist of courses worth registering for: something that is either Computer Science or Economics, but only if it carries more than three credits. He writes a single `WHERE` clause with both an `AND` and an `OR` in it, runs it, and gets a course back that clearly does not belong on the list. Nothing is wrong with his data.

The problem is that SQL read his conditions in an order he did not intend, and fixing it means learning how the **logical operators**, `AND`, `OR`, and `NOT`, actually combine.

![AND and OR shown as gates where AND needs all checks true and OR needs at least one](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_and_or_logical_gates.png)

**Definition:** `AND`, `OR`, and `NOT` let a single `WHERE` clause weigh several conditions at once.

## Combining Conditions with AND and OR

- `AND` keeps a `row` only when every condition attached to it is true.
- `OR` keeps a `row` when at least one condition is true.

Both let a single `WHERE` clause test more than one thing at a time.

The lesson uses one `courses` table throughout:

| course_id | title | department | credits |
| --------- | -------------------- | ---------------- | ------: |
| 101 | Database Systems | Computer Science | 4 |
| 102 | Data Structures | Computer Science | 4 |
| 103 | Linear Algebra | Mathematics | 3 |
| 104 | Discrete Mathematics | Mathematics | 3 |
| 105 | Microeconomics | Economics | 2 |

To find Computer Science courses that also carry four credits, use `SELECT title, department, credits FROM courses WHERE department = 'Computer Science' AND credits = 4;`. The `department` check and the `credits` check must both be true for a row to survive.

Expected output:

| title | department | credits |
| ---------------- | ---------------- | ------: |
| Database Systems | Computer Science | 4 |
| Data Structures | Computer Science | 4 |

Both rows satisfy both conditions. The Mathematics courses fail the department test, and Microeconomics fails both tests.

For hands-on practice, `init.sql` creates and populates only the displayed table:

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

The active query file contains the logical condition:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakcw5" 
 width="100%"
></iframe>

Now compare `AND` with `OR`. The query `SELECT title, department FROM courses WHERE department = 'Mathematics' OR department = 'Economics';` keeps a row when either department check is true.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakd92" 
 width="100%"
></iframe>

Expected output:

| title | department |
| -------------------- | ---------- |
| Linear Algebra | Mathematics |
| Discrete Mathematics | Mathematics |
| Microeconomics | Economics |

This returns three `rows`: `Linear Algebra`, `Discrete Mathematics`, and `Microeconomics`. `OR` only needs one side of the condition to be true, so every course in either department qualifies.

## Where Parentheses Actually Matter

Here is the `query` Varun originally wrote for his shortlist, exactly as he typed it.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakdnp" 
 width="100%"
></iframe>

Expected output:

| title | department | credits |
| ---------------- | ---------------- | ------: |
| Database Systems | Computer Science | 4 |
| Data Structures | Computer Science | 4 |
| Microeconomics | Economics | 2 |

- This returns three courses: `Database Systems`, `Data Structures`, and `Microeconomics`, even though `Microeconomics` carries only two credits, well below the "more than three" requirement Varun cares about.
- The reason is that SQL evaluates `AND` before `OR` when neither is grouped by parentheses, the same way multiplication is evaluated before addition in ordinary arithmetic.
- Varun's clause was actually read as `(department = 'Computer Science' AND credits > 3) OR department = 'Economics'`, so any Economics course sneaks in regardless of its credit value.

Adding parentheses around the department check fixes it, because it forces the `OR` to be settled first, and only then does `AND` check the credit requirement against that combined result.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakdy3" 
 width="100%"
></iframe>

Expected output:

| title | department | credits |
| ---------------- | ---------------- | ------: |
| Database Systems | Computer Science | 4 |
| Data Structures | Computer Science | 4 |

- Now only `Database Systems` and `Data Structures` come back.
- `Microeconomics` is correctly dropped, since it fails the `credits > 3` test once that test is applied to the right group of `rows`.
- The SQL text barely changed, four characters, but the meaning changed completely, which is exactly why relying on operator precedence to do the right thing by accident is worth avoiding whenever `AND` and `OR` appear in the same `WHERE` clause.

![Parentheses grouping department choices before applying the credits greater than 3 condition](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_parentheses_group_conditions.png)

## NOT Reverses a Condition

`NOT` flips a condition's truth value: `rows` that would have matched are excluded, and `rows` that would not have matched are included instead.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkake9e" 
 width="100%"
></iframe>

Expected output:

| title | credits |
| -------------------- | ------: |
| Linear Algebra | 3 |
| Discrete Mathematics | 3 |
| Microeconomics | 2 |

This returns `Linear Algebra`, `Discrete Mathematics`, and `Microeconomics`, the three courses whose credit value is not greater than three. It reads naturally alongside `AND` and `OR`, and like both of them, it can be wrapped in parentheses to control exactly which condition it applies to when the clause grows more complex.

## Logical Operators at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Operator</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Keeps a row when</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Precedence versus the others</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>AND</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every joined condition is true</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evaluated before OR</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>OR</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">At least one joined condition is true</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evaluated after AND unless grouped</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NOT</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The condition following it is false</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Applies to whatever it is placed directly before</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>( )</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">N/A</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forces a group to be evaluated as one unit first</td>
    </tr>
  </tbody>
</table>

## Your Turn

Write a `query` against `courses` for departments that are Mathematics or Computer Science, restricted to courses worth at least four credits, and use parentheses so the grouping is unambiguous.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkakem4" 
 width="100%"
></iframe>

Expected output:

| title | department | credits |
| ---------------- | ---------------- | ------: |
| Database Systems | Computer Science | 4 |
| Data Structures | Computer Science | 4 |

This should return exactly `Database Systems` and `Data Structures`. Both Mathematics courses carry only three credits, so they are correctly excluded once the parentheses force the department check to be grouped before the credit check applies to it.

## Conclusion

`AND`, `OR`, and `NOT` let a single `WHERE` clause weigh several conditions at once. Because `AND` binds more tightly than `OR`, parentheses matter whenever the intended grouping is not obvious. Varun's correctly grouped condition, `(department = 'Computer Science' OR department = 'Economics') AND credits > 3`, now returns only the two qualifying Computer Science courses instead of allowing Microeconomics to slip through.

With numeric, date, and combined conditions covered, the next gap is text that is not an exact match at all. Pattern matching provides the tools for finding `rows` from only part of a stored value.
