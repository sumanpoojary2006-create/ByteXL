## Introduction

Sanjay has just joined a growing fintech company as its third backend hire, and his first week is spent doing something nobody warned him about in college: reading someone else's database instead of designing his own. Three inconsistencies greet him on his first read-through:

- The `schema` he inherits has a table called `Customer` and another called `transactions`, one written in the singular, the other in the plural, with no explanation for why.
- A column called `custId` sits beside another called `user_id`, both apparently referring to the same kind of person in different tables.
- A column simply called `type` shows up in three unrelated tables, and Sanjay has no way to tell, just by reading the name, whether it means a customer's account type, a transaction's type, or a support ticket's type.

By Thursday, Sanjay has spent more time asking teammates "wait, which table does this belong to?" than he has spent writing any actual code. His tech lead, mildly embarrassed, admits the `schema` grew for three years without anyone agreeing on a shared set of rules for naming tables and columns. What Sanjay is living through is the practical cost of ignoring **naming conventions**, the agreed-upon rules a team follows for how tables and columns are named, so that a name alone tells a reader what it holds and how it relates to everything else, without anyone needing to ask.

## Singular or Plural Table Names: Pick One and Never Look Back

The first inconsistency Sanjay flags is the mix of singular and plural table names. Some database designers name a table `Customer`, reasoning that each row is one customer. Others name it `Customers`, reasoning that the table as a whole is a collection of customers. Neither convention is objectively correct, and reasonable teams disagree on which one to pick. What is not defensible is doing both in the same `schema`, because a developer who has just learned that tables are plural will confidently write `Transactions` for a new table, and be wrong the moment it turns out this particular `schema` actually prefers the singular form for that one table, for reasons nobody remembers. The fix Sanjay proposes is unglamorous but effective: the team picks one convention, documents it in a single sentence at the top of their `schema` notes, and applies it to every table without exception going forward.

## snake_case or camelCase: The Same Rule Applies to Columns

The `custId` and `user_id` split is the column-level version of the same problem. One uses camelCase, capitalizing the first letter of each word after the first; the other uses snake_case, separating words with an underscore and keeping everything lowercase. Most relational database systems are, by default, case-insensitive about unquoted identifiers, which means mixing the two styles does not just look inconsistent, it can actively cause confusion about whether `custId` and `custid` are meant to be the same column or different ones. Sanjay's team settles on snake_case for every column, matching the convention most relational database tooling expects, and rewrites the plan for all new tables around it, leaving the legacy columns to be renamed gradually rather than all at once.

## Names That Collide With the Database's Own Vocabulary

Sanjay also spots a column simply named `order`, in a Payments table meant to store the sequence number of a payment attempt. The trouble is that "order" is a word many database systems already reserve for their own sorting instructions, and a column sharing a name with a word the database itself uses for something else invites exactly the kind of subtle, hard-to-diagnose error that eats an afternoon. The fix is simple: prefer a more specific column name, such as `attempt_number`, which is not only safer but also more informative on its own. As a general habit, any column name that reads like an everyday instruction rather than a piece of data, words like "order," "group," "user," or "date" used bare, deserves a second look before it goes into a `schema`.

## Foreign Key Names That Say What They Point To

The most confusing inconsistency Sanjay finds is inside the Transactions table, where a column is simply named `id`. Read in isolation, `id` looks like it should be the transaction's own primary key, but a closer look at the data shows it actually holds a reference to a row in the Customers table, meaning it is a `foreign key` masquerading as a primary key by name alone. A well-named `foreign key` states plainly what it points to: `customer_id` inside a Transactions table leaves no doubt that the value refers to a row in Customers, while a bare `id` forces every new developer to go digging through the data just to find out what the column actually means. Sanjay's rule of thumb going forward is that a `foreign key` column should always be named after the table it references, in the singular, followed by `_id`.

## Abbreviations That Only the Original Author Understood

The last habit Sanjay pushes back on is unexplained abbreviation. A column named `cst_addr_ln1` might have been perfectly clear to whoever wrote it three years ago, but it forces every new reader to reverse-engineer "customer address line 1" from a handful of truncated fragments. Abbreviating to save a few keystrokes almost never pays for itself once a `schema` is read by more people than wrote it, which is nearly always. Sanjay's rule is not "never abbreviate," since a handful of abbreviations, like `id` itself, are so universally understood they cause no confusion. The rule is narrower: abbreviate only when the shortened form would be instantly obvious to any new teammate on their first day, and spell the rest out in full.

| Naming problem Sanjay found | Fix the team agreed on |
|---|---|
| `Customer` and `transactions` mixed singular/plural | Pick one convention for every table, document it once |
| `custId` next to `user_id` | snake_case for every column, no exceptions |
| A column named `order` | Rename to something specific, like `attempt_number` |
| A foreign key simply named `id` | Name it after the table it points to: `customer_id` |
| `cst_addr_ln1` | Spell it out: `customer_address_line1`, unless the short form is universally obvious |

## Naming Conventions at a Glance

| Element | Convention to fix on | Why it matters |
|---|---|---|
| Table names | Singular or plural, chosen once | Prevents guesswork about which form a new table should take |
| Column names | snake_case, consistently | Matches typical database tooling, avoids case-sensitivity confusion |
| Reserved-sounding words | Avoid using bare as column names | Prevents collisions with the database's own vocabulary |
| Foreign keys | Named after the referenced table plus `_id` | Makes relationships readable without inspecting the data |
| Abbreviations | Only when instantly obvious to a newcomer | Keeps the `schema` self-explanatory years later |

## Conclusion

A naming convention is a small, almost invisible kind of documentation, one that lives inside the names themselves rather than in a separate document nobody reads. Consistent singular-or-plural table names, a single consistent casing style for columns, column names that avoid the database's own reserved vocabulary, `foreign keys` that plainly state what they reference, and abbreviations that never require a guess all add up to a `schema` a new developer can read cold, without pulling a teammate aside to translate it first.

Sanjay's team fixes their naming going forward, but naming alone does not tell a future reader when a row was created, when it last changed, or whether it was ever meant to disappear, questions that a different, equally quiet set of columns is built to answer.
