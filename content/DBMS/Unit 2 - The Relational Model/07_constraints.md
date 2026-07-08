## Introduction

Devika runs one more mock batch of test data past the developer before sign-off, and three small gaps surface that neither entity nor referential integrity was ever built to catch. A test book gets inserted with `title` left completely blank. Two test members are registered with the exact same `email_address`, even though their `member_id` values are correctly unique. A newly added book has no value at all in `is_available`, leaving it blank instead of sensibly marked as available. Keys and foreign keys, the last two lessons showed, say nothing about any of these three. Closing them needs a smaller, well-known set of rules: constraints.

## NOT NULL: This Value Cannot Be Missing

A **NOT NULL** constraint states that a column may never be left blank; every row must supply a real value for it. Devika's `books.title` is an obvious candidate: a book with no title recorded at all is barely a usable record. Declaring `title` as NOT NULL means the database itself refuses any row that tries to leave it empty, rather than quietly accepting an incomplete book and letting the gap surface later as confusion.

Not every column needs this constraint. A book's `subtitle` might genuinely be blank for many titles that never had one; forcing it to NOT NULL would only invite people to type in a meaningless placeholder just to satisfy the rule.

## UNIQUE: No Two Rows May Share This Value

A **UNIQUE** constraint states that no two rows may hold the same value in a given column, even though that column is not the primary key. `members.email_address` is a strong candidate: `member_id` is already the primary key, but the college also wants a guarantee that no two members ever register with the same email, since email is how overdue notices get sent. A UNIQUE constraint provides exactly that second guarantee, entirely independent of the primary key.

This is a genuinely different job from a primary key. A table may have several UNIQUE columns; it may only ever have one primary key.

## DEFAULT: A Sensible Value When None Is Given

A **DEFAULT** constraint supplies an automatic value for a column when a new row does not specify one. Devika's `books.is_available` column makes sense to default to `true`: a newly added book has, almost always, never been borrowed yet, so assuming it is available unless a loan says otherwise saves every future insert from having to state the obvious. A default is a convenience with real value: it removes an entire category of small, repetitive mistakes where someone simply forgets to set a column that almost always holds the same starting value anyway.

## CHECK: A Rule the Value Must Satisfy

A **CHECK** constraint states a condition a column's value must satisfy for a row to be accepted at all. A `late_fee_amount` column should probably never hold a negative number, since a negative fee makes no real-world sense; a CHECK constraint stating that the value must be zero or greater enforces exactly that, refusing any row that tries to violate it. This is the most flexible constraint of the four, since the condition itself can be almost any rule the data genuinely needs to satisfy.

## The Four Constraints at a Glance

| Constraint | What It Enforces | Library Example |
|---|---|---|
| NOT NULL | This column can never be left blank | `books.title` must always be supplied |
| UNIQUE | No two rows may share this value | `members.email_address` must differ across all members |
| DEFAULT | An automatic value fills in if none is given | `books.is_available` defaults to true |
| CHECK | The value must satisfy a stated condition | `late_fee_amount` must be zero or greater |

## Constraints Are Small, But They Close Real Gaps

None of these four constraints is as structurally central as a primary key or a foreign key, but each one closes a specific, realistic gap that keys alone leave open. A primary key guarantees `member_id` is unique and present; it says nothing about whether `email_address` is unique, whether `title` was actually filled in, or whether a fee is a sensible non-negative number. Constraints are how a table designer states every rule the real data needs to obey, not just the rules that happen to follow automatically from choosing a primary key.

## Conclusion

NOT NULL refuses a missing value, UNIQUE refuses a duplicate in a non-key column, DEFAULT quietly fills in a sensible starting value, and CHECK refuses any value that fails a stated condition. Together with the keys, foreign keys, and integrity rules from earlier in this unit, these constraints are what turn a plausible-looking table on paper into a schema that actively defends its own data, exactly the discipline Devika's original spreadsheets never had. The final lesson of this unit steps back to read one complete schema, diagram and all, tying every idea from this unit together before Unit 3 finally builds it in real SQL.
