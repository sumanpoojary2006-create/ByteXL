## Introduction

The delivery startup runs a mentorship program for new riders: every experienced rider is paired with a couple of newer riders to show them the ropes, and that pairing is stored right inside the `riders` table itself, as a `mentor_id` column pointing to another rider's `rider_id`. Zoya's new task is to produce a list showing each rider's name next to their mentor's name. There is only one table involved, `riders`, but the report still needs two names sitting side by side on one line, which is exactly the shape a `join` produces. The twist is that both sides of this `join` come from the same table. That is a **self `join`**: a table joined to a copy of itself.

## Why One Table Needs to Act Like Two

The `riders` table stores every rider once, with a `mentor_id` column that is `NULL` for riders who have no assigned mentor.

```postgresql file=riders.sql
CREATE TABLE riders (
    rider_id INTEGER PRIMARY KEY,
    rider_name TEXT,
    mentor_id INTEGER REFERENCES riders(rider_id)
);

INSERT INTO riders (rider_id, rider_name, mentor_id) VALUES
(1, 'Suresh Pillai', NULL),
(2, 'Arjun Verma', NULL),
(3, 'Deepa Krishnan', 1),
(4, 'Farhan Iqbal', 1),
(5, 'Nikita Rao', 2),
(6, 'Om Prakash', 3);
```

```postgresql with=riders.sql
SELECT * FROM riders;
```

Reading this table row by row is already possible, since a human can trace `mentor_id = 1` back up to Suresh Pillai's row by eye. A query cannot do that kind of visual tracing; it needs the mentor's row and the mentee's row joined together as two separate table references, even though both rows live in the exact same table.

## Joining a Table to Itself Using Aliases

The trick to a self `join` is giving the same table two different names, or aliases, so the `join` condition can tell them apart.

```postgresql with=riders.sql
SELECT mentee.rider_name AS rider, mentor.rider_name AS mentor
FROM riders mentee
JOIN riders mentor ON mentee.mentor_id = mentor.rider_id;
```

`riders mentee` and `riders mentor` are the same table, `riders`, referenced twice with two different aliases:

- `mentee` stands in for "the rider currently being looked up."
- `mentor` stands in for "whoever that rider reports to."

The `join` condition, `mentee.mentor_id = mentor.rider_id`, matches each mentee's `mentor_id` against the mentor's own `rider_id`, exactly the same logic used to `join` two genuinely different tables in earlier lessons. The database has no trouble treating one physical table as two separate references, as long as the aliases keep them distinguishable in the query.

## Including Riders With No Mentor

An `INNER JOIN` self `join`, like the one above, drops Suresh and Arjun entirely, since their `mentor_id` is `NULL` and finds no match. If the report needs to show every rider, mentored or not, a `LEFT JOIN` self `join` solves it the same way it solved the unmatched-row problem for two different tables.

```postgresql with=riders.sql
SELECT mentee.rider_name AS rider, mentor.rider_name AS mentor
FROM riders mentee
LEFT JOIN riders mentor ON mentee.mentor_id = mentor.rider_id;
```

Now all 6 riders appear, and Suresh and Arjun show `NULL` in the `mentor` column, correctly reflecting that they are the senior riders at the top of the mentorship chain with no one assigned above them:

| rider | mentor |
|---|---|
| Suresh Pillai | `NULL` |
| Arjun Verma | `NULL` |
| Deepa Krishnan | Suresh Pillai |
| Farhan Iqbal | Suresh Pillai |
| Nikita Rao | Arjun Verma |
| Om Prakash | Deepa Krishnan |

## Finding Riders Who Are Mentors Themselves

A self `join` can also answer a different kind of question: which riders currently mentor someone, listed once per rider regardless of how many mentees they have?

```postgresql with=riders.sql
SELECT DISTINCT mentor.rider_name AS is_a_mentor
FROM riders mentee
JOIN riders mentor ON mentee.mentor_id = mentor.rider_id;
```

`DISTINCT` collapses duplicates here, since Suresh mentors two people, Deepa and Farhan, and without `DISTINCT` his name would appear twice. This returns Suresh, Arjun, and Deepa, since Deepa herself mentors Om Prakash even though she is also mentored by Suresh, showing that a rider can be both a mentee and a mentor at once.

## Self Joins at a Glance

| Concept | Detail |
|---|---|
| Table involved | Just one, referenced twice |
| Required | Two different aliases for the same table |
| `Join` condition | Usually links a row to another row in the same table, such as a manager or mentor column pointing back to the table's own key |
| `INNER JOIN` version | Drops rows with no self-reference, such as no mentor |
| `LEFT JOIN` version | Keeps every row, `NULL` where no self-reference exists |

## Your Turn

Zoya wants to know which riders share the same mentor as Farhan Iqbal, not including Farhan himself. Write a query against the `riders` table above that returns the names of Farhan's mentorship-siblings.

```postgresql with=riders.sql
-- Write your query below
```

If your query `joins` `riders` to itself on matching `mentor_id` values, filtering for rows where one side's name is 'Farhan Iqbal' and excluding that same name from the result, it returns Deepa Krishnan, since both she and Farhan are mentored by Suresh Pillai.

## Conclusion

A self `join` is not a different kind of `join` mechanically, it is the same `JOIN`, `LEFT JOIN`, or any other `join` type covered so far, applied to one table referenced twice under two different aliases, which is exactly what a hierarchy or a peer relationship stored in a single table needs. Zoya can now report mentor pairs, list unmentored seniors, and find mentorship-siblings, all from one `riders` table. Every `join` so far has combined exactly two table references at a time; the next lesson scales that up to three or more tables in a single query.
