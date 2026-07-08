## Introduction

Devika's library outgrew index cards years ago. The whole catalogue now lives in three spreadsheet files: `books.xlsx`, `members.xlsx`, and `loans.xlsx`, each maintained by whoever is on the front desk that day. It works, mostly, until the day two assistants both update `loans.xlsx` at the same time, on their own laptops, and email their versions back to Devika. She now has two spreadsheets, each missing the other's changes, and no clean way to tell which loan records actually happened.

This is not a story about spreadsheets being a bad tool. It is a story about a genuine limit that appears the moment shared data is kept in ordinary files, no matter how carefully those files are maintained. That limit has a name, and it has three well-known symptoms: redundancy, inconsistency, and lost updates.

## Redundancy: Saying the Same Thing More Than Once

Redundancy means the same fact is stored in more than one place. Devika's member details, name, phone number, department, are typed once into `members.xlsx`, but they are also retyped into `loans.xlsx` every time that member borrows a book, because the loans file needs to show who borrowed what without anyone having to open a second file to check.

A member who borrows ten books in a term now has their phone number sitting in eleven different places: once in `members.xlsx`, and once inside each of the ten rows in `loans.xlsx`. Nothing is wrong yet. The redundancy simply exists, quietly, waiting for its consequence to show up in the next lesson's problem.

## Inconsistency: When the Copies Disagree

A student, Arjun, changes his phone number and tells the front desk. Whoever is on duty updates `members.xlsx`. But Arjun has three loan records already sitting in `loans.xlsx`, each with his old number copied in, and nobody thinks to open that file and fix all three. Now `members.xlsx` says one phone number, and `loans.xlsx` says another, older one, in three separate places.

This is **inconsistency**: the same fact, stored redundantly, now disagreeing with itself because only some of its copies were updated. Ask Devika for Arjun's phone number and the honest answer becomes "it depends which file you check," which is not an answer any library, or any real system, can actually work with.

## Lost Updates: When Two Changes Collide

The opening story is the sharpest version of this problem. Two assistants open `loans.xlsx` at 2 PM. One records that Arjun returned a book; the other records a brand-new loan for a different student. Both save their own copy over email. Whichever file Devika saves last simply overwrites the other, and one of those two genuine, correct updates vanishes without a trace, with no error message and no warning that anything was lost.

This is a **lost update**: two separate, valid changes happen at roughly the same time, and a plain file, with no mechanism for coordinating simultaneous edits, can only keep one of them.

## The Three Symptoms at a Glance

| Symptom | What Happens | Library Example |
|---|---|---|
| Redundancy | The same fact is stored in multiple places | A phone number typed into both `members.xlsx` and every loan row in `loans.xlsx` |
| Inconsistency | Redundant copies of a fact disagree with each other | Arjun's phone number differs between the two files after only one was updated |
| Lost updates | Two simultaneous changes overwrite each other | Two assistants' edits to `loans.xlsx`; only one survives the save |

## Why Careful People Cannot Simply Avoid This

A reasonable question follows: could Devika's team just be more careful? Could they agree on a rule, always update every file, always take turns editing?

For three people and three small spreadsheets, discipline can paper over the problem for a while. But it does not scale, and it does not survive a single tired evening shift or a new part-time assistant who was never told the rule. The moment more than one person needs to read or write the same shared data, at any real volume, the three symptoms above stop being occasional accidents and become a routine, predictable cost of doing business with plain files. The problem is not the people. It is the tool: files were never designed to coordinate simultaneous, shared access to the same data, or to enforce that every copy of a fact stays in sync with every other copy.

## Conclusion

Plain files invite redundancy, because the same fact often has to be retyped wherever it is needed; redundancy invites inconsistency, because updating one copy does not update the others; and simultaneous edits invite lost updates, because a file has no way to merge two people's changes safely. None of this is a failure of Devika's team. It is what happens, reliably, once shared data outgrows a single person maintaining a single file alone. The next lesson names the tool built specifically to solve all three problems at once, and draws the line between that tool and the software that manages it.
