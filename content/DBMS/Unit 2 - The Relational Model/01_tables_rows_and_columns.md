## Introduction

Devika's college has approved money for a real database, and before anyone touches a keyboard, she is asked to redraw her three spreadsheet files, `books.xlsx`, `members.xlsx`, and `loans.xlsx`, as something more disciplined. She starts with `books.xlsx`, and it turns out to already be halfway there: a grid of titles down the side and details across the top. Turning a spreadsheet grid into a proper relational table means tightening that grid until every position in it means exactly one thing, with no exceptions and no surprises.

## A Table Is a Grid With Rules

A **table** in the relational model is a named grid of data organized into rows and columns, where every row shares the exact same columns, and every column holds only one clearly defined kind of value. Devika's `books` table might have columns for `book_id`, `title`, `author`, and `shelf_location`. Every single book, without exception, is described using those same four columns; no book is allowed to sneak in an extra field of its own, and no book is allowed to leave one of them out.

This is stricter than a spreadsheet ever enforced. Nothing stopped Devika from typing a stray note into a random cell of `books.xlsx`, or leaving a shelf location blank for one particular row while filling it in for the rest. A table, once properly defined, does not allow that kind of drift.

## Rows: One Record, Fully Described

A **row**, sometimes called a record or a tuple, is a single complete entry in a table, one specific book, described by a value in every one of the table's columns. The row for "Wings of Fire" holds a specific `book_id`, its specific title, its specific author, and its specific shelf location, all four values belonging to that one book and no other.

Two different books are always two different rows, even if some of their column values happen to match. Two copies of the same title, sitting on different shelves, are two separate rows, because a row describes one physical thing, not one title.

## Columns: One Fact, Consistently Typed

A **column** is a named field that appears in every row of the table, and it holds the same kind of value everywhere it appears. The `shelf_location` column holds a shelf code for every single book row, never a phone number, never a borrower's name, never left to mean something different from one row to the next. This consistency is what makes a table queryable at all: asking "which books are on shelf A214" only makes sense because every row's `shelf_location` column means the exact same thing.

## Tables, Rows, and Columns at a Glance

| Term | What It Is | Library Example |
|---|---|---|
| Table | A named grid holding one kind of thing | `books`, one row per physical book |
| Row | One complete record inside a table | The specific row describing "Wings of Fire" |
| Column | A named field present in every row | `book_id`, `title`, `author`, `shelf_location` |

## Three Tables, Not One Giant Table

A natural question follows: why does Devika need three separate tables, `books`, `members`, and `loans`, rather than one enormous table with every possible column crammed into it?

Picture that single giant table for a moment. Every loan row would need to repeat the borrowing member's full name and phone number, and every book row that has never been borrowed would need to leave several loan-related columns sitting empty. This is exactly the redundancy problem from Unit 1, now visible directly inside the structure of a badly designed table. Separate tables, one for books, one for members, one for loans, each holding only the columns that genuinely belong to that one kind of thing, is the relational model's first line of defence against redundancy, well before keys or constraints even enter the picture.

## Sketching the Books Table

On paper, before any software is involved, Devika's `books` table might look like this:

| `book_id` | `title` | `author` | `shelf_location` |
|---|---|---|---|
| 1084 | Wings of Fire | A.P.J. Abdul Kalam | A214 |
| 1085 | The Discovery of India | Jawaharlal Nehru | A215 |
| 1086 | Wings of Fire | A.P.J. Abdul Kalam | B102 |

Notice rows 1 and 3: the same title and author, because the library owns two physical copies, but two distinct rows, because they are two distinct books sitting on two distinct shelves. This is exactly the "one row per real thing" discipline a table exists to enforce.

## Conclusion

A relational table is a named grid where every row shares the same columns and every column holds one consistently typed kind of value, a stricter and more trustworthy shape than any spreadsheet's free-form grid. Splitting related data into separate tables, one per kind of thing, is the model's first defence against the redundancy Unit 1 warned about. Sketching `books` this way is only the beginning: nothing yet says which column uniquely identifies a row, or what values `shelf_location` is actually allowed to hold. The next lesson gives every column a strict domain, so a column's freedom to hold "any text at all" narrows into a clear, enforceable rule.
