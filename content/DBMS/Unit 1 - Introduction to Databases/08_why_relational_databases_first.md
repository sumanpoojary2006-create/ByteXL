## Introduction

Devika has now watched one library turn into a small case study of nearly everything this unit covers: data becoming information, files failing under shared use, a DBMS fixing what files could not, that same pattern repeating across a dinner order and a bank transfer, three different shapes a database can take, three parts cooperating to answer Arjun's question in under a second, and three different people relying on the result without needing the same knowledge. One question remains before any real database work begins. Of the three shapes named a few lessons ago, relational, key-value, document, why does this course, and most of the industry, start with the relational model specifically?

## Tables Match How People Already Think

A relational table looks like a structure almost everyone already understands without training: rows and columns, the same shape as a spreadsheet, a timetable, or Devika's original card catalogue, just enforced far more strictly. A `books` table with columns for title, author, and shelf location reads naturally to anyone, long before they know a single word of SQL, in a way a key-value store's locker-and-label shape, or a document database's flexible bundles, simply do not read as immediately. This familiarity is not an accident of teaching; it is a genuine reason the model spread as widely as it did in the first place.

## Relationships Are Made Explicit, Not Assumed

Real data is rarely one flat list; it is naturally connected. Arjun's loan connects one specific member to one specific book, and the relational model makes that connection explicit and enforced, through the keys and foreign keys the next unit introduces properly, rather than leaving it as an assumption a person has to remember correctly every time, the exact assumption that quietly broke down across Devika's separate spreadsheet files two lessons before any DBMS existed at all.

A key-value store, by contrast, has no built-in way to express "this loan belongs to that member and this book"; the login-session example from two lessons ago worked precisely because it needed no such relationship. Ask that same store to connect a session to a member's full loan history, and the connecting logic would have to live entirely in whatever application code sits on top, by convention, not by guarantee.

## SQL Is a Genuine Industry Standard

Structured Query Language, SQL, is the language nearly every relational database understands, with only small differences in dialect between MySQL, PostgreSQL, SQLite, and others. Learning it once means being able to work, with only minor adjustments, across an enormous share of the database systems actually running in production today, the exact systems this course names throughout Unit 1: the food delivery order history, the banking transfer log, the college portal's grade records. This is not true to nearly the same extent for key-value or document databases, where the query approach varies far more from one product to the next.

## Strong, Well-Understood Guarantees

Relational databases, and the DBMSs built around them, carry decades of engineering behind exactly the guarantees this unit cared about most: no lost updates, like the one that cost Devika a real loan record, no silent inconsistency, like Arjun's disagreeing phone number, and safe simultaneous access by many users at once. These guarantees are not a footnote; they are the actual reason a bank trusts a relational database with a five-thousand-rupee transfer, a guarantee this course studies directly in the unit on transactions.

## The Four Reasons at a Glance

| Reason | What It Means | The Moment From This Unit That Proves It |
|---|---|---|
| Familiar shape | Tables read like a spreadsheet or timetable | Devika's original card catalogue, only stricter |
| Explicit relationships | Keys and foreign keys state how data connects | Arjun's loan, linking one member to one book, never left to memory |
| SQL as a standard | One language, understood almost everywhere, with small variations | The same querying skill behind a library search and a banking transfer log |
| Strong guarantees | Decades of engineering against lost updates and inconsistency | The exact loan record two lessons ago that a real DBMS would never have lost |

## Not the Only Tool, but the Right Starting Point

None of this makes key-value and document databases lesser tools; the lesson on types of databases was explicit that each shape fits a different kind of problem, and the food delivery app from earlier in this unit likely uses all three at once, a document store for its varied restaurant listings, a key-value store for login sessions, a relational database for the order history and billing. It means relational databases are the strongest, most widely applicable starting point for learning how databases work at all, because their structure is the most explicit, their guarantees are the most thoroughly understood, and their language, SQL, is the one you are most likely to meet again and again across a real career.

## Conclusion

This course begins with the relational model because its tables match how people already think, its relationships are explicit rather than assumed, its query language is a genuine cross-industry standard, and its guarantees are exactly the ones this unit showed plain files could never provide. Every idea from this unit, data versus information, the cost of plain files, what a DBMS actually does, the shapes data can take, the machinery that answers a question, and the people who rely on it, was building toward this one starting point. The next unit stays entirely on paper a little longer, learning to see a real problem, Devika's library included, as tables, rows, and columns, before a single line of SQL is written in Unit 3.
