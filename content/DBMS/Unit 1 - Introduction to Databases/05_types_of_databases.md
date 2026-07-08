## Introduction

Devika mentions to her college's IT contact that she is finally comfortable with the word "database," and he replies with a sentence that unsettles her all over again: "Good, because the food delivery app from last night almost certainly isn't using the same kind of database your library will." She had assumed "database" meant one single kind of thing, the way "spreadsheet" means one kind of thing. It does not, and the reason is simpler than it sounds: different applications are storing genuinely different shapes of data, and each shape has a storage model built specifically for it.

## The Relational Model: Neat Rows and Columns

A relational database stores data in tables, rows, and columns, much like a very disciplined spreadsheet with strict rules about what each column may hold and how tables relate to each other. Devika's 40,000 book records fit this shape naturally: every single book has the same fields, a title, an author, a shelf location, no more and no fewer, and the tables connect to each other through shared identifiers rather than repeated details.

This is the model MySQL, PostgreSQL, and SQLite are all built around, and it is the model this entire course is built around, for reasons the final lesson of this unit lays out in full.

## Key-Value Stores: A Locker With a Number on It

A key-value database stores data as pairs: a key you already know, and a value it hands back instantly, with no relationships between different keys and no fixed set of columns at all. Picture a locker room where every locker has a number and holds whatever was placed inside it. Asking "what is in locker 42" is instant. Asking "which lockers contain a red bag" is not a question this shape was built to answer at all; someone would have to open every single locker to find out.

This fits the food delivery app's login session perfectly: the moment Devika opens the app, it needs one instant answer to "who is logged in right now, given this session key," and nothing about that answer needs to relate to any other shopper's session at all.

## Document Databases: Records That Are Allowed to Differ

A document database stores each record as a single, self-contained bundle, commonly in a format resembling JSON, where different records in the same collection are allowed to hold different fields entirely. One restaurant listing in that same food delivery app might include a delivery-time estimate and a minimum order value; another, sitting in the exact same collection, might skip both and instead list a "dine-in only" flag that the first restaurant never needed at all.

A relational table could not hold this comfortably, since every row in a relational table is expected to share the exact same columns. A document database embraces the variation instead of fighting it.

## Comparing the Three Shapes

| Model | Shape of the Data | Fits Best When | Real Example From Last Night |
|---|---|---|---|
| Relational | Tables, rows, and columns, with defined relationships | Data is structured and consistent, and relationships between records matter | Devika's library: books, members, and loans, all sharing fixed fields |
| Key-value | A key that instantly returns its value | Fast lookups by one known key, with no relationships needed | The food app remembering who is logged in, by session key |
| Document | Flexible, self-contained records that can vary in shape | Records legitimately differ from one another in structure | The food app's restaurant listings, each with its own mix of fields |

## Choosing Is About Fit, Not Rank

None of these three is simply "better" than the others; each is the better fit for a different shape of problem. Devika's library, with its strict, repeating structure and its clear relationships (a loan always connects exactly one member to exactly one book), is a textbook fit for the relational model. The same food delivery app that needed a document database for its varied restaurant listings almost certainly reaches for a key-value store for login sessions and a relational database for the actual order history and billing, three different shapes, inside one single app, each chosen for the job it fits.

A useful habit going forward: before reaching for any database technology, ask what shape the data naturally takes on its own, structured and interrelated, a simple key-driven lookup, or flexible and record-by-record, and let that answer, not familiarity, decide the tool.

## Conclusion

"Database" is a family of tools, not one single shape. Relational databases organize data into related tables built for structured, interconnected records; key-value stores trade relationships for extremely fast lookups by a known key; document databases embrace records that vary in shape from one to the next, inside the very same collection. Devika's library, and this entire course, live squarely in the relational world, because books, members, and loans are exactly the kind of structured, interrelated data that model was built to hold. The next lesson opens up the DBMS itself, to see what is actually happening inside it the instant it answers a request.
