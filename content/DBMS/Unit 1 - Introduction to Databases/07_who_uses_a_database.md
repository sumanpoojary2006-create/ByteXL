## Introduction

Arjun, the student from the last lesson, walks away satisfied with his answer of "three" and never once wonders about storage, query processors, or catalogs. Twenty minutes later, a developer the college hired calls Devika to ask exactly how "currently open" should be defined for a loan, because she is about to write the code behind a new search page. An hour after that, Devika herself spends ten minutes checking whether last night's backup actually completed. Same database, same single Tuesday morning, three completely different relationships to it.

## End Users: People Who Never See the Data Directly

An **end user** interacts with a database only through an application's screen, never through the database itself. Arjun typed nothing more than a spoken question at the front desk; a student using the library's own search kiosk types a title into a box and reads a list of results. Neither of them has any idea, and no need to have any idea, whether that search was answered by a relational database, a key-value store, or something else entirely, the three shapes named two lessons ago.

This describes nearly everyone from two lessons back: the food delivery customer waiting for a status update, the banking app user checking a balance, the student checking grades on the college portal. Their entire experience of a database is a screen that simply works, correctly and quickly, with all three cooperating parts from the last lesson staying completely out of sight.

## Developers: People Who Build the Bridge

A **developer** writes the code that sits between an end user's screen and the database itself, translating an action like typing a title and pressing "Search" into an actual request the query processor can answer, and translating the answer back into a readable list on screen. The library's new search kiosk did not build itself: a developer had to decide exactly what request to send the instant a student types a title, and precisely how "currently open" should be defined when a loan record is checked, the very question that developer called Devika about this morning.

This is precisely the audience this course is built for. From Unit 3 onward, you are learning to speak directly to the query processor yourself, the exact skill that developer needed the moment "how do we define an open loan" stopped being an abstract question and became a real line of code.

## Administrators: People Who Keep the Whole System Healthy

A **database administrator**, often shortened to DBA, is responsible for the database as a whole: who is allowed to access which data, whether backups are actually completing, whether the system holds up under real load, and what happens if a server fails outright. Devika, since her library moved off spreadsheets, has quietly become exactly this. She does not write the search kiosk's code, but she is the one who decided students may search the catalogue while only staff may view full loan histories, and she is the one who spent those ten minutes this morning confirming last night's backup genuinely finished, rather than discovering a gap only after something was already lost.

## The Three Roles at a Glance

| Role | What They Do | This Morning's Example |
|---|---|---|
| End user | Interacts with an application built on top of the database, never with the database directly | Arjun, asking "how many books do I have out" at the front desk |
| Developer | Builds the application that talks to the database on the end user's behalf | The developer defining exactly what "currently open" means in code |
| Administrator | Manages access, backups, and the health of the database itself | Devika, confirming last night's backup actually completed |

## One Person, More Than One Role, in the Same Hour

These roles are not always three different people. Devika spent her morning as an administrator, checking backups and access rules, but she was also, in effect, the end user who typed Arjun's question into the system in the first place, no different from how a student would use the search kiosk. In a much larger organization, these three roles are usually held by entirely separate specialists, sometimes whole teams for each one. What actually matters is not the headcount but recognizing, task by task, which relationship to the database a given moment requires, since each one expects genuinely different knowledge: Arjun needed none, the developer needed to speak SQL, and Devika needed to understand backups and access rules that neither of the other two ever had to think about.

## Conclusion

A database rarely serves just one kind of person in a single day, let alone across its whole lifetime. End users interact with it only through an application's surface, developers build that application by speaking to the database directly, and administrators keep the whole system healthy, secure, and running underneath both of them. This course is aimed squarely at the developer's relationship to a database, learning to ask it precise questions and trust the answers, the exact skill that turned "define an open loan" from a phone call into working code. The final lesson of this unit steps back to explain why, of every shape surveyed a few lessons ago, the relational model is where nearly every developer's journey actually begins.
