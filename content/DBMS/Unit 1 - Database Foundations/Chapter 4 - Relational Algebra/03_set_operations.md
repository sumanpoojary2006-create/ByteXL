## Introduction

Meera coordinates student clubs on campus, and this term she has been handed an awkward request from the events office: they want one clean list of every student who belongs to either the Coding Club or the Robotics Club, another list of students who belong to both, and a third list of coding-club students who have never set foot in robotics. Meera has two separate spreadsheets, one per club, each with a single column of student IDs, and no idea how to compare them without manually scrolling back and forth for an afternoon.

What Meera is really asking for are three classic comparisons between two relations that happen to hold the same kind of thing:

- Everyone in either group
- Everyone in both groups
- Everyone in one group but not the other

`Relational algebra` has a dedicated operation for each of these, borrowed directly from set theory, and together they are simply called **set operations**. Before any of the three can be applied, though, the two relations being compared have to satisfy one important condition, and that condition comes first.

## The Two Club Relations

Here are Meera's two relations, trimmed down to just the column that matters:

Coding Club:

| student_id |
|---|
| S101 |
| S104 |
| S107 |
| S110 |

Robotics Club:

| student_id |
|---|
| S104 |
| S107 |
| S112 |

Both relations have exactly one column, student_id, and both draw their values from the same underlying pool, valid student roll numbers at the same college. That similarity is not a coincidence, it is a requirement.

## Union-Compatible: Why the Shapes Must Match

Set operations only make sense when the two relations involved are what `relational algebra` calls **union-compatible**. Two relations are union-compatible when they have the same number of columns, and each corresponding column draws its values from the same domain, meaning the same kind of underlying data. Meera's two club relations qualify easily, both have one column, and both hold student IDs from the same college's numbering scheme.

It helps to see why this requirement exists by imagining what would go wrong without it. Suppose Meera tried to compare her Coding Club relation, a single column of student IDs, against a relation of book titles from the library catalogue. Asking "which rows appear in both" would be meaningless, a student ID and a book title are not comparable values, and there would be no sensible way to line up the columns to check for a match. Union-compatibility is what guarantees that comparing two relations row by row is actually a coherent thing to do. Two relations can have entirely different column names and still be union-compatible, what matters is the number of columns and the domain each one draws from, not the labels typed above them.

## Union: Everyone in Either Relation

The union of two union-compatible relations keeps every row that appears in at least one of them, with duplicates collapsed down to a single copy, exactly the way "or" works in ordinary set theory. Applied to Meera's two club relations, the union answers "who belongs to the Coding Club, the Robotics Club, or both":

| student_id |
|---|
| S101 |
| S104 |
| S107 |
| S110 |
| S112 |

Five distinct IDs, even though the two relations together listed seven rows, because S104 and S107 appeared in both and were only kept once. This single list is exactly what the events office wanted for its first request, one combined roster of everyone involved in either club.

## Intersection: Only the Rows in Both

The intersection of two union-compatible relations keeps only the rows that appear in both relations at once, exactly the way "and" works in ordinary set theory. Applied to the same two club relations, it answers "who belongs to both clubs":

| student_id |
|---|
| S104 |
| S107 |

Only S104 and S107 show up in both the Coding Club and Robotics Club relations, so only those two rows survive. This is the second list the events office asked for, students who might need to be counted once rather than twice when the office plans seating for a joint event.

## Difference: Rows in One But Not the Other

The difference between two union-compatible relations keeps the rows that appear in the first relation but not in the second, and order matters here in a way it did not for union or intersection. Applied as Coding Club minus Robotics Club, it answers "who is in coding but has never joined robotics":

| student_id |
|---|
| S101 |
| S110 |

S104 and S107 are removed because they also appear in the Robotics Club relation, leaving only the coding-only members. Notice that reversing the operation, Robotics Club minus Coding Club, would give a different answer entirely, just S112, the one robotics member who never joined coding. Difference is the one set operation in this trio where the order the relations are written in changes the result.

## Set Operations at a Glance

| Operation | Symbol idea | Keeps | Meera's example result |
|---|---|---|---|
| Union | Combine, remove duplicates | Rows in either relation | S101, S104, S107, S110, S112 |
| Intersection | Common rows only | Rows in both relations | S104, S107 |
| Difference | First relation minus second | Rows only in the first relation | S101, S110 |

## Conclusion

Union, intersection, and difference let a database compare two relations the way set theory compares two collections, but only once those relations are union-compatible, meaning they agree on the number of columns and the domain each column draws from. Union merges everyone from either side while dropping duplicates, intersection keeps only the overlap, and difference keeps what belongs to one side and not the other, with the order of the two relations mattering for that last one. Meera can now hand the events office exactly the three lists they asked for, a combined roster from union, the overlap from intersection, and the coding-only members from difference, without a single afternoon lost scrolling between two spreadsheets.

Every operation seen so far has worked on relations that already share the same columns, either narrowing a single relation or comparing two similarly shaped ones. The next operation breaks that pattern entirely, combining two genuinely different relations, each with its own columns, based on a value they happen to share.
