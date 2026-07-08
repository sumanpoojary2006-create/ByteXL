## Introduction

Devika's `books` table now has well-typed columns, but a sharper question arrives from the same colleague: if two students are both named "Rina Shah," how does the system tell their loan records apart? Names alone will not do it. What Devika actually needs is some column, or combination of columns, guaranteed to be different for every single row, so that "this one specific row" can always be picked out without ambiguity. That guarantee is exactly what a key provides.

## Candidate Keys: Anything That Could Do the Job

A **candidate key** is any column, or minimal combination of columns, whose value is guaranteed to be unique across every row in the table, making it a genuine candidate for identifying a row on its own. In a `members` table, both `member_id` and, if the college guarantees no two students ever share one, `email_address` could each serve as a candidate key: either one, alone, is enough to tell every member apart from every other.

A table can have more than one candidate key at once. The word "candidate" is deliberate: each one is capable of doing the identifying job, even though, as the next section shows, only one of them actually gets chosen to do it.

## Primary Keys: The One Candidate That Gets the Job

A **primary key** is the one candidate key a table designer formally chooses as the official, permanent identifier for every row. Devika's `members` table might have both `member_id` and `email_address` as candidate keys, but she chooses `member_id` as the primary key, the single column every other part of the design will use whenever it needs to say "this exact member and no other."

Why prefer `member_id` over `email_address` here, when both are unique? A primary key should ideally never change over a row's lifetime, and an email address, unlike an assigned member number, is exactly the kind of value a real person might reasonably update. A good primary key is stable, not just unique, and this is precisely why Devika's college assigns a fixed `member_id` to every student rather than relying on an email address to identify them forever.

## Composite Keys: When One Column Is Not Enough

A **composite key** is a primary key made of more than one column together, needed when no single column, by itself, is guaranteed unique, but some specific combination is. Picture a `loan_items` table recording which specific copy of a book was included in which loan transaction: neither `loan_id` alone (many books can belong to the same loan) nor `book_copy_id` alone (the same physical copy is loaned out again and again over time) uniquely identifies one row on its own. The pair, `(loan_id, book_copy_id)` together, does: that exact copy appears at most once within that exact loan.

A composite key is not a workaround or a compromise; it is the correct, honest key whenever uniqueness is a property of a combination, not any single column.

## Keys at a Glance

| Kind of Key | What It Means | Library Example |
|---|---|---|
| Candidate key | Any column or minimal set of columns that is guaranteed unique | `member_id` and `email_address`, each unique on its own |
| Primary key | The one candidate key formally chosen to identify every row | `member_id`, chosen over `email_address` |
| Composite key | A primary key made of more than one column together | `(loan_id, book_copy_id)` in a table with no single unique column |

## What a Primary Key Actually Guarantees

Once `member_id` is declared the primary key of `members`, two guarantees follow automatically, enforced by the DBMS rather than left to a person's discipline. First, no two rows may ever share the same `member_id`. Second, no row may leave its `member_id` blank, since a missing identifier could never uniquely identify anything at all. These twin guarantees, uniqueness and presence, are given a formal name of their own two lessons from now, when this unit covers integrity rules directly.

## Conclusion

A candidate key is any column or combination guaranteed unique enough to identify a row; a primary key is the one candidate formally chosen for that job, ideally one that never changes; and a composite key is simply a primary key spread across more than one column, exactly when uniqueness genuinely depends on their combination. With every table now able to name one specific row precisely, the next lesson uses that same ability to let one table point at a row in a completely different table, the mechanism that will finally connect `loans` to both `books` and `members`.
