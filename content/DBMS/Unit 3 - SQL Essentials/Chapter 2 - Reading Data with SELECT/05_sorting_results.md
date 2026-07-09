## Introduction

Rhea is preparing a printed roster for orientation day, and she wants the students listed alphabetically by name so the volunteers checking people in can find a name quickly instead of scanning a jumbled list. She runs a plain `SELECT full_name, city FROM students;` and the rows come back in whatever order PostgreSQL happens to store or retrieve them in, which is not alphabetical, not by city, not by anything Rhea can rely on. A table's rows have no built-in order at all unless a query explicitly asks for one. The clause that asks for one is **`ORDER BY`**, and it is what turns an unpredictable pile of rows into a sequence a person can actually use.

## Sorting Ascending, the Default

Rhea's first fix is simple: add `ORDER BY` followed by the column she wants to sort on.

```postgresql file=students.sql
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

```postgresql with=students.sql
SELECT full_name, city
FROM students
ORDER BY full_name;
```

The result now starts with Aditya Kulkarni and ends with Sneha Gowda, running alphabetically A to Z the whole way through. This is ascending order, and it is what PostgreSQL uses whenever `ORDER BY` is given a column with no further instruction:

- For text, ascending means alphabetical.
- For numbers, it means smallest to largest.
- For dates, it means earliest to latest.

## Sorting Descending

Sometimes the useful order runs the other way. If Rhea instead wants the newest joiners at the top of a "welcome our latest students" notice, ascending order on the join date would put the oldest joiners first, exactly backwards from what she needs. Adding `DESC` after the column reverses the direction.

```postgresql with=students.sql
SELECT full_name, joined_on
FROM students
ORDER BY joined_on DESC;
```

Now Priya Subramaniam, who joined on 2025-01-28, appears first, and Ishaan Verma, who joined on 2025-01-10, appears last. Writing `ASC` explicitly is also allowed for ascending order, but since ascending is the default, most people leave it out and only write `DESC` when they actually need the reverse.

## Sorting by More Than One Column

A single sort key is not always enough. Suppose Rhea wants students grouped by city, and within each city, listed alphabetically by name, so a volunteer working the Bengaluru desk can find their group's names in order without scrolling past every other city first. `ORDER BY` accepts a list of columns, and it sorts by the first one, then uses the second one only to break ties within groups that share the same first value.

```postgresql with=students.sql
SELECT full_name, city
FROM students
ORDER BY city, full_name;
```

The result groups all of Bengaluru's students together, sorted alphabetically within that group, then moves to Chennai's students sorted alphabetically within that group, and so on through Hyderabad, Mysuru, and Pune. Arjun Bhat appears before Ishaan Verma within Bengaluru because the tie on city is broken by name. Each column in the list can carry its own direction too, so `ORDER BY city, full_name DESC` would keep cities grouped in ascending order while listing names within each city from Z to A.

## Sorting Results at a Glance

| Clause | Direction | Example |
|---|---|---|
| `ORDER BY full_name` | Ascending (default), A to Z | Aditya first, Sneha last |
| `ORDER BY joined_on DESC` | Descending, latest to earliest | Priya (2025-01-28) first |
| `ORDER BY city, full_name` | Groups by city, then name within each city | Bengaluru names together, sorted |

## Your Turn

The office also wants a version of the roster sorted so that students from the same city are still grouped together, but this time with the most recently joined student in each city appearing first. Write a query that returns `full_name`, `city`, and `joined_on`, grouped by city ascending and, within each city, newest join date first.

```postgresql with=students.sql
-- Write your query below
```

`SELECT full_name, city, joined_on FROM students ORDER BY city, joined_on DESC;` does exactly this: cities still run alphabetically overall, but inside each city's block the most recent joiner leads.

## Conclusion

`ORDER BY` replaces an unpredictable row order with one you actually chose, ascending by default or reversed with DESC, and it can chain several columns together so later ones only settle ties left by earlier ones. None of this changes how rows are stored, it only shapes the sequence a particular query hands back. Rhea's orientation roster can now print alphabetically by name, or grouped by city with each group internally sorted, so her volunteers can find any student in seconds instead of scanning an unpredictable list. Once a result can be put into a meaningful order, the natural next question is how to show only the first handful of rows from a large, sorted result, which is exactly the kind of trimming a dashboard preview needs.
