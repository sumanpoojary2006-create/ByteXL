## Introduction

Devika's draft `books` table looks tidy on paper, until the same developer who called about Arjun's loan sends over a mock entry for testing: `book_id = 1087`, `title = "Panchatantra"`, `author = "Vishnu Sharma"`, `published_year = "a long time ago"`. Every field is filled in, and nothing on the page objects, because nothing yet says a publication year has to actually be a number. A column, so far, is just a name; it has no rule attached to it about what kind of value genuinely belongs there. That rule has a name of its own: a domain.

## A Domain Is the Set of Allowed Values

A **domain** is the complete set of values a column is permitted to hold. The domain of `shelf_location` is not "any text," it is something closer to "a shelf code following the library's own labelling pattern," and the domain of `published_year` is not "any value at all," it is something closer to "a whole number that could plausibly be a year." A column's domain is the honest answer to the question "what is this column actually allowed to contain," stated precisely enough that a wrong value can be caught before it is ever stored.

Without a stated domain, a column is only a suggestion. Devika's spreadsheets had exactly this problem: nothing stopped a stray note or a misplaced value from landing in the wrong cell, because no cell in a spreadsheet enforces what belongs in it.

## Data Types: A Practical Way to State a Domain

A **data type** is the everyday tool a database uses to enforce a domain: a named category of value, such as a whole number, a piece of text of a certain length, a date, or a true-or-false value, that a column is restricted to. Stating that `book_id` has an integer data type is a practical, enforceable way of saying its domain is whole numbers; stating that `title` has a text data type of a reasonable length says its domain is written text, not numbers or dates.

Every column in Devika's `books` table can now be given a type that captures its real domain far more tightly than "any value" ever did.

## Common Data Types, Named for the First Time

| Data Type | What It Holds | Example Column |
|---|---|---|
| Integer | Whole numbers, no decimal point | `book_id`, `published_year` |
| Text | Words, sentences, or short strings | `title`, `author`, `shelf_location` |
| Decimal | Numbers with a fractional part | `late_fee_amount` |
| Date | A calendar date | `date_borrowed`, `date_returned` |
| Boolean | Exactly one of two values, true or false | `is_available` |

This course names these types here in plain English on purpose. Unit 3 gives each one its exact SQL spelling and behaviour the moment real tables are actually created; for now, the goal is simply recognizing that every column deserves one of these categories, not "whatever happens to get typed in."

## Choosing a Type Is Choosing a Domain, Deliberately

Consider `published_year`. Should it be text or an integer? If it is stored as text, nothing stops someone from typing `"a long time ago"` into it, which technically fits "text" perfectly well but ruins any attempt to later ask "which books were published after 2010." Making it an integer immediately rules out that entire category of bad value, because an integer column simply has no way to hold the words "a long time ago" at all.

This is the real power a data type provides: it does not just describe a column, it actively narrows what can go wrong, before a single row is ever entered.

## Domains Beyond the Basic Types

Sometimes a domain is narrower than any basic type can express on its own. `is_available` is a boolean, true or false, but a library membership tier might realistically only ever be one of `"Student"`, `"Faculty"`, or `"Guest"`, a domain narrower than "any text." Basic data types are the first, most important layer of domain enforcement; later lessons in this unit, on constraints, add the finer-grained rules a plain data type cannot express by itself.

## Conclusion

A domain is the honest, complete set of values a column is allowed to hold, and a data type is the practical, enforceable way a database states that domain for every value entered. Choosing integer over text for `published_year`, or date over text for `date_borrowed`, is not a formality; it is what turns "please type something reasonable here" into a rule the system itself will not let anyone break. Every column drafted so far still lacks one more thing: some way to say which column, or combination of columns, uniquely picks out one single row. That is exactly what the next lesson, on keys, provides.
