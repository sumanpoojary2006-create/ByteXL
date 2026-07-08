## Introduction

The IT office asks Devika to sign off on her schema with one line: "Confirm the design satisfies entity and referential integrity." She has never heard either phrase before, but as she reads the definition, she realizes both rules were already sitting inside her design, unnamed, since the very first table was sketched: every row can always be told apart from every other, and every foreign key genuinely points at something real. These two promises are common enough across every relational database ever designed that they have earned formal names of their own: entity integrity and referential integrity.

## Entity Integrity: Every Row Must Be Identifiable

**Entity integrity** is the rule that every table must have a primary key, and that primary key's value must be both unique and never left blank, for every single row, with no exceptions. This is not a new idea; it is simply naming, precisely, the guarantee a primary key was always supposed to provide, back when Unit 2 first introduced the concept.

Consider what breaks if entity integrity is violated. A `members` row with no `member_id` at all cannot be reliably linked to from `loans`, since there is nothing stable to point at. Two rows sharing the same `member_id` are worse still: any question like "which member is this" now has two conflicting answers, and every foreign key pointing at that ID becomes ambiguous. Entity integrity is what keeps "one row, one identity" true everywhere in the database, not just in the table where a key was first defined.

## Referential Integrity: Every Pointer Must Point at Something Real

**Referential integrity** is the rule that every foreign key value must match an existing primary key value in the table it references, or be left blank if the design allows that. This is the formal name for the guarantee the foreign key lesson described directly: `loans.member_id` may not hold a value that does not correspond to a real row in `members`.

Referential integrity is what prevents the orphaned rows described earlier, loan records quietly pointing at a member who was never registered, or was since deleted without anyone updating the loans that referenced them. A properly enforced DBMS checks this rule the instant a row is inserted or a referenced row is removed, refusing the change outright if it would leave a foreign key pointing at nothing.

## The Two Rules at a Glance

| Rule | What It Guarantees | What Breaks Without It |
|---|---|---|
| Entity integrity | Every row has a unique, non-blank primary key | Rows cannot be reliably told apart or pointed at |
| Referential integrity | Every foreign key matches a real row elsewhere | Orphaned rows, pointing at data that does not exist |

## Watching Both Rules Protect a Single Loan

Trace one new loan through both rules at once. Devika's system is asked to insert a loan for `member_id = 12` and `book_id = 1084`. Entity integrity has already guaranteed, back when `members` and `books` were built, that at most one row exists for `member_id = 12` and at most one for `book_id = 1084`, so there is no ambiguity about which member or book is meant. Referential integrity then checks that a row with `member_id = 12` and a row with `book_id = 1084` genuinely exist before allowing the loan to be recorded at all. Only once both rules are satisfied does the new loan row become part of a trustworthy database.

## Why These Rules Are Named, Not Just Implied

A fair question: if these rules were already implied by keys and foreign keys, why give them separate names at all? Because naming them turns an implicit habit into an explicit, checkable standard. When two database designers discuss whether a schema is sound, "does it satisfy entity and referential integrity" is a precise, shared question, exactly the kind of shared vocabulary that let Devika's earlier, vaguer worry, "what if a loan points at nobody," become a rule any properly built DBMS enforces automatically, without her having to check it by hand the way she once had to check her spreadsheets.

## Conclusion

Entity integrity guarantees every row can always be uniquely and reliably identified; referential integrity guarantees every foreign key genuinely points at a row that exists. Together, they are the formal versions of guarantees this unit had already been building, one lesson at a time, since the very first table was sketched. A DBMS enforces both automatically once a schema states its keys and foreign keys correctly, exactly the coordination plain files in Unit 1 could never provide. The next lesson adds a handful of smaller, equally enforceable rules, NOT NULL, UNIQUE, DEFAULT, and CHECK, for the details that keys and foreign keys alone do not yet cover.
