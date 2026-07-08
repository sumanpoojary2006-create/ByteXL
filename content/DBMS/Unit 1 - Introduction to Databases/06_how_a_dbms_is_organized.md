## Introduction

A student named Arjun walks up to the front desk and asks Devika, "how many books do I currently have out?" She types the question into the new system, and an answer appears in under a second: three. Somewhere between her keystrokes and that number appearing on screen, the DBMS did real work, and it is worth asking exactly what that work was, because "it just looked it up" hides three genuinely separate jobs happening in sequence, each one done by a different part of the DBMS.

## Storage: Where the Data Actually Sits

The **storage** layer is where the data physically lives, written to disk in a form the DBMS can read back reliably even after the power goes out. Arjun's three loan records are sitting there right now, alongside 40,000 book records and several thousand other loans, not as three separate files the way Devika's old spreadsheets were, but organized so that finding Arjun's specific three rows does not require reading through every loan the library has ever recorded.

Nobody, not Devika, not Arjun, ever touches this layer directly. It exists purely so every layer above it has something durable to read from and write to, crash or no crash.

## The Query Processor: Understanding and Answering a Question

The **query processor** is the part that receives a request such as "find every loan currently open for Arjun," works out the fastest correct way to actually fetch that answer from storage, and carries it out. This is the layer that turned Devika's typed question into the exact sequence of reads that produced "three" in under a second, and it is the layer this entire course spends the most time speaking to directly, through SQL, starting in Unit 3.

Notice what Devika never had to specify: she never said which order to check the loan records in, or how to skip past the tens of thousands of loans that belong to someone else. Deciding how to answer quickly and correctly is the query processor's job alone, a distinction the very next unit builds on directly, once "say what you want, not how to get it" becomes this course's central idea.

## The Catalog: The DBMS's Own Notes About Itself

The **catalog**, sometimes called the data dictionary, is the DBMS's internal record of its own structure: which tables exist, what columns each one has, what type of data each column may hold, and how tables relate to one another. Before the query processor can even attempt Arjun's question, it must first know, by consulting the catalog, that a `loans` table exists at all, that it has a column linking each loan back to a specific member, and that "currently open" means a loan whose return date is still blank.

Devika's spreadsheets had no equivalent of this whatsoever. Nothing enforced that `loans.xlsx` and `members.xlsx` used matching member identifiers; a person simply had to remember the convention and get it right by hand, the exact discipline that failed the day two assistants edited the same file. A DBMS's catalog makes that structure explicit, checked, and enforced automatically, every single time, not just when someone remembers to be careful.

## The Three Parts at a Glance

| Part | Job | What Happens for Arjun's Question |
|---|---|---|
| Storage | Physically holds the data, durably, on disk | Holds Arjun's three loan rows among thousands of others |
| Query processor | Understands a request and works out how to answer it | Decides how to find exactly Arjun's open loans, fast |
| Catalog | Keeps track of what tables, columns, and relationships exist | Confirms a `loans` table exists, linked to `members`, before any search begins |

## Watching the Three Parts Cooperate, in Order

Trace the full second between Devika's keystroke and the answer "three." First, the query processor receives "how many loans are currently open for member Arjun." Second, it consults the catalog, confirming that a `loans` table exists, that it is linked to `members` by a shared identifier, and that an open loan is one with no return date recorded. Third, armed with that structure, it goes to the storage layer, reads exactly Arjun's rows rather than all of them, counts three, and hands the number back.

Devika never saw any of these three steps happen. She asked one plain question and received one correct, fast answer, while three distinct parts of the DBMS quietly did their separate jobs in the background, in that exact order, every single time.

## Conclusion

A DBMS is not one monolithic block; it is storage holding data durably, a query processor deciding how to answer a request, and a catalog keeping track of the database's own structure so the query processor always knows what it is working with. These three parts cooperate in the same order every time a question is asked, invisibly, the same way Devika's old system once needed a person to play all three roles by hand, slowly and with far more room for error. The next lesson turns from this machinery to the people who actually rely on it day to day, starting with the very student who just asked Devika a question without any idea of the three steps his question triggered.
