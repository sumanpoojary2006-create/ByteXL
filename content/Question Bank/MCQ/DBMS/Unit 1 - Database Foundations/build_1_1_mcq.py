import random
import openpyxl

random.seed(23)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

# --- data-vs-information (5) ---
DATA_VS_INFO = [
    (
        "A campus ID system stores the value `21` against a student's record, with no label attached anywhere nearby.\n\nOn its own, is `21` data or information?",
        "A bare value with no label or context, is it someone's age, a room number, a count, is ambiguous. It stays data until it is tied to a name, a purpose, or a scale.",
        "easy", "understand", "data-vs-information",
        "Data — the value has no context attached, so its meaning is ambiguous",
        ["Information — any value stored in a system counts as information", "Information — numbers are always information, unlike text", "Data — but only because it is a small number"],
    ),
    (
        "Priya's college result system responds to a roll number with: \"Ananya Rao, B.Sc. Computer Science, Semester 3: Physics 85, overall percentage 80.25%, result PASS.\"\n\nWhy does this count as information rather than plain data?",
        "The raw number 85 has been tied to a name, a subject, a scale, and a verdict, exactly the structure and purpose that turns raw data into usable information.",
        "medium", "understand", "data-vs-information",
        "The raw marks are organised and connected to a name, subject, and verdict, giving them meaning someone can act on",
        ["It counts as information simply because it appears on a screen instead of paper", "It counts as information because percentages are always more meaningful than integers", "It is still data, since a database can only ever store raw facts"],
    ),
    (
        "Before a database existed, Priya's office kept a stack of paper forms with roll numbers, names, and marks written on them. Finding \"What did Ananya score in Physics?\" meant a clerk digging through the stack by hand.\n\nWhy does an organised database make this faster than the paper forms, even though both technically \"store the same facts\"?",
        "The database keeps roll number, name, subject, and marks tied together as structured data, so answering a precise question becomes a direct lookup instead of a manual reconstruction the clerk has to redo every time.",
        "medium", "apply", "data-vs-information",
        "The database keeps related facts structured and connected, so producing an answer is a fast, repeatable lookup rather than manual searching",
        ["The database is faster only because computers process numbers quicker than humans read paper", "Paper forms cannot legally store the same facts a database can", "There is no real difference — both approaches take the same effort once organised"],
    ),
    (
        "Compare two records about the same fact:\n\n1. `\"O positive\"`\n2. \"Patient ID 1042, blood group O positive, last donation 2026-03-14\"\n\nWhich one is information, and why?",
        "Record 2 ties the blood group to a patient identity and a date, giving it context and purpose. Record 1 is the same fact floating free, with no label to say whose blood group it is.",
        "medium", "apply", "data-vs-information",
        "Record 2 — it connects the value to a patient ID and a date, giving it context a person can act on",
        ["Record 1 — shorter records are always clearer", "Both are equally information, since both mention a blood group", "Neither is information, since blood group alone is never useful"],
    ),
    (
        "A `database`'s core purpose, as distinct from a plain pile of files, is described in terms of turning data into information.\n\nWhich statement best captures that purpose?",
        "The distinction is not academic: a database exists specifically so that producing information from stored data is fast, reliable, and repeatable, instead of something a person reconstructs by hand every time.",
        "hard", "analyze", "data-vs-information",
        "To store data in a structured way so that turning it into information later is fast, reliable, and repeatable",
        ["To make sure every value stored is already information rather than raw data", "To replace paper entirely, regardless of how the data is structured", "To guarantee that data can never be ambiguous once it is typed in"],
    ),
]

# --- problems-with-files (5) ---
PROBLEMS_WITH_FILES = [
    (
        "Kabir's office keeps applicant details in `applicants.xlsx`, `documents.xlsx`, and `interviews.xlsx`. Rohan's phone number is typed separately into all three files so each can be read on its own.\n\nWhich problem does this illustrate?",
        "The same fact, Rohan's phone number, is stored in more than one place. That repetition is redundancy, and by itself it doesn't break anything yet, it just creates copies waiting to drift apart.",
        "easy", "remember", "problems-with-files",
        "Redundancy — the same fact is stored in more than one file",
        ["Inconsistency — the copies already disagree with each other", "A lost update — one coordinator's edit has been overwritten", "None of these; storing a phone number three times is normal practice"],
    ),
    (
        "Rohan's category certificate is corrected. Kabir updates `applicants.xlsx` to show \"General merit,\" but nobody opens `interviews.xlsx`, which still shows him under the SC panel three weeks later.\n\nWhich problem does this illustrate?",
        "Two redundant copies of the same fact, Rohan's category, now disagree because only one was updated. That disagreement between copies is exactly what inconsistency means.",
        "medium", "understand", "problems-with-files",
        "Inconsistency — two copies of the same fact now disagree because only one was updated",
        ["Redundancy — the fact was typed in two places, which is the entire problem here", "A lost update — an edit was silently overwritten by a second save", "Data vs. information confusion — the category was never real information"],
    ),
    (
        "Two coordinators open `interviews.xlsx` at nearly the same moment. One adds a new interview slot, the other confirms three candidates. Both save within a minute of each other, and whichever file lands last on the server simply overwrites the other.\n\nWhich problem does this illustrate?",
        "Both coordinators made genuine, valid changes to the same shared file, but the file format has no way to merge them. Whichever save happens last wins, and the other person's honest work vanishes without any error — a lost update.",
        "medium", "apply", "problems-with-files",
        "A lost update — two valid simultaneous changes collide, and only one survives",
        ["Redundancy — the same interview slot was typed into two files", "Inconsistency — the two coordinators disagreed about who should be interviewed", "A database constraint violation — the file rejected one of the two saves"],
    ),
    (
        "Someone suggests fixing Kabir's office problems with a simple rule: always update every file the moment anything changes, and never let two people open the same file at once.\n\nWhy does relying on discipline alone fail to solve this at real scale?",
        "The rule might survive a small, quiet week, but a busy interview season with dozens of near-simultaneous edits, a new volunteer who was never told the rule, and the ordinary habit of only updating the file already open all make the rule break down in practice.",
        "hard", "analyze", "problems-with-files",
        "It only works for a handful of careful people; real scale brings simultaneous edits, untrained newcomers, and habits that no rule can fully police",
        ["Discipline always works; the office's real mistake was using Excel instead of Word", "It fails because spreadsheets are incapable of holding more than a few hundred rows", "It fails because plain files cannot be backed up, unlike a database"],
    ),
    (
        "Redundancy, inconsistency, and lost updates are described as \"three distinct, well-known faces\" of the same underlying failure.\n\nWhat is that underlying failure?",
        "Plain files were never built to coordinate shared, growing data safely across multiple people reading and writing at once — that single gap in capability produces all three symptoms.",
        "medium", "understand", "problems-with-files",
        "Plain files were never built to coordinate shared, growing data safely among multiple simultaneous users",
        ["The office staff were careless and did not proofread their spreadsheets", "Spreadsheet software has a hard row limit that admissions data exceeds", "Excel files cannot store text and numbers in the same file"],
    ),
]

# --- database-vs-dbms (5) ---
DB_VS_DBMS = [
    (
        "Meera applies a test: if every computer in the office lost power for a week, would the admissions database still exist?\n\nWhat does the answer to this test reveal?",
        "The answer is yes, the data would still sit untouched on disk, just like a locked drawer of paper files surviving a power cut. That confirms a database is content, not machinery, distinct from the software that manages it.",
        "medium", "understand", "database-vs-dbms",
        "Yes — a database is the organised data itself, which persists independently of any running software",
        ["No — a database only exists while a DBMS program is actively running", "Yes, but only if the DBMS is PostgreSQL specifically", "No — databases are erased whenever power is lost, which is why backups exist"],
    ),
    (
        "A vendor proposal states: \"PostgreSQL is the DBMS that will manage your admissions database.\"\n\nWhat is PostgreSQL, according to this sentence?",
        "PostgreSQL is named as the DBMS, the software responsible for creating, storing, retrieving, updating, and protecting the data, not the admissions records themselves.",
        "easy", "remember", "database-vs-dbms",
        "The software that manages the admissions data, not the data itself",
        ["The admissions database itself, containing every applicant record", "A file format used to save spreadsheets", "A synonym for \"database\" with no real distinction"],
    ),
    (
        "Meera asks the vendor: if the college later switches from PostgreSQL to a different product, does the office lose any applicant records, certificates, or interview history?\n\nWhat is the honest answer, and why?",
        "No — the applicant names, categories, and interview outcomes are one fixed body of facts (the database). Only the software reading and writing them (the DBMS) would change.",
        "medium", "apply", "database-vs-dbms",
        "No — the data is a fixed body of facts separate from the DBMS; only the managing software would change",
        ["Yes — every DBMS stores data in a proprietary format tied permanently to that vendor", "No — but only because PostgreSQL and every other DBMS are actually the same underlying program", "Yes — switching DBMS always requires re-entering all applicant data by hand"],
    ),
    (
        "Which statement correctly distinguishes \"safe to edit directly by hand\" for a database versus a DBMS?",
        "Editing the raw data directly by hand risks the same redundancy and lost-update problems seen with plain files. A DBMS exists specifically to make safe, coordinated editing possible instead.",
        "medium", "analyze", "database-vs-dbms",
        "The database is not safe to edit by hand directly; the DBMS layer exists to make safe, coordinated editing possible",
        ["Both the database and the DBMS are equally safe to edit directly by hand", "The DBMS is not safe to edit by hand, but the raw database files are", "Neither the database nor the DBMS can ever be edited safely, even through an application"],
    ),
    (
        "A vendor blurs \"database\" and \"DBMS\" together throughout a proposal, treating them as interchangeable words.\n\nWhy does the lesson describe this as \"quietly steering Meera toward worrying about the wrong thing\"?",
        "If the two words are treated as one, Meera might focus on which brand of software is fashionable this year instead of the real question: whether her actual data survives untouched no matter which DBMS manages it later.",
        "hard", "analyze", "database-vs-dbms",
        "It shifts her attention toward which software brand is used, instead of whether her actual data would survive a future change untouched",
        ["It has no real effect, since the two words mean exactly the same thing", "It makes her worry about backups, which the lesson says are unnecessary", "It causes her to overpay for extra applicant records she does not need"],
    ),
]

# --- databases-in-everyday-apps (5) ---
DBS_EVERYDAY = [
    (
        "A food delivery app has exactly one plate of biryani left. Two customers tap \"confirm order\" within the same few seconds.\n\nWhat is a properly coordinated database expected to prevent here?",
        "A database is what stops both customers from being told \"confirmed\" for a dish only one plate of which actually exists, the same kind of collision that caused Kabir's office to lose an interview slot.",
        "easy", "apply", "databases-in-everyday-apps",
        "Both customers being told their order for the same last dish is confirmed",
        ["The restaurant from ever running out of any dish", "The delivery rider from taking a wrong turn", "The customer from being charged twice for one order"],
    ),
    (
        "A bank transfer must decrease one account and increase another by the exact same amount, as a single coordinated action. If the connection dropped between those two steps and only the decrease was saved, what would happen to the money?",
        "The money would not sit in either account, it would simply cease to exist anywhere, undiscoverable by rechecking a balance. This is exactly why a database's coordination is not a nicety for banking, it's the entire basis of trust.",
        "medium", "analyze", "databases-in-everyday-apps",
        "It would effectively vanish, present in neither account and undiscoverable by checking either balance",
        ["It would automatically be refunded to the sender's account within a day", "It would sit safely in a temporary holding account until the connection resumes", "Nothing would change, since balances are always rechecked before a transfer completes"],
    ),
    (
        "A professor uploads marks for two hundred students at 6 PM. Five minutes later, a student's portal already reflects the update, with no manual syncing between separate files.\n\nWhy does this happen without drift or delay?",
        "Both the professor's upload and the student's portal read from and write to the same underlying database, so there is no second copy that could fall out of step, unlike Kabir's three separate spreadsheets.",
        "medium", "apply", "databases-in-everyday-apps",
        "Both the upload and the student portal are reading from and writing to the same underlying database",
        ["The college portal automatically emails every student a copy of their marks", "Marks are cached in the student's browser the moment they log in for the first time", "The professor's upload and the student portal use two files that are synced manually every night"],
    ),
    (
        "Food delivery, banking, and college portal examples are all described as \"the same coordination problem, solved at the scale of millions of users.\"\n\nWhat is the shared pattern across all three apps?",
        "Each app quietly relies on a database behind the screen to read and write shared, changing facts correctly, whether or not the end user ever notices that a database is involved at all.",
        "medium", "understand", "databases-in-everyday-apps",
        "Each app relies on a database behind the scenes to coordinate reads and writes correctly, invisibly to the end user",
        ["Each app stores its data in a single shared spreadsheet file for simplicity", "Each app avoids using a database entirely by keeping data only on the user's phone", "Each app requires the end user to manually refresh the page to see correct data"],
    ),
    (
        "A step counter drifting by a few hundred steps is called \"a minor annoyance,\" while a hospital's record of a patient's allergies drifting even slightly is treated very differently.\n\nWhy does the same kind of database correctness matter more in one case than the other?",
        "The consequence of incorrect data scales with what's at stake: a wrong step count is harmless, but a wrong allergy record or an incorrect money transfer can cause real, serious harm, so those systems demand stronger correctness guarantees.",
        "hard", "analyze", "databases-in-everyday-apps",
        "Because the real-world consequence of wrong data differs — a wrong step count is harmless, but a wrong allergy record or transfer amount can cause serious harm",
        ["Because hospitals are legally required to use a different type of computer than fitness apps", "Because step counters do not use databases at all, unlike hospital systems", "There is no real difference; both examples are treated identically by the lesson"],
    ),
]

# --- types-of-databases (5) ---
TYPES_OF_DBS = [
    (
        "A delivery app's order history needs an order ID, a customer, a total, and a status, with every order sharing the exact same fields and tables linked through shared identifiers.\n\nWhich database model fits this data naturally?",
        "Data that is structured and consistent, with the same fields on every record and meaningful relationships between tables, is exactly what the relational model, tables, rows, and columns, is built for.",
        "easy", "understand", "types-of-databases",
        "The relational model — tables, rows, and columns with fixed fields and relationships",
        ["A key-value store — fast lookups with no relationships needed", "A document database — records that vary in shape from one another", "None of these; order history cannot be modelled by any database"],
    ),
    (
        "An app needs to instantly answer \"who is logged in right now, given this session key,\" with no need to relate one user's session to another's.\n\nWhich database model fits this need best?",
        "A key-value store returns a value instantly for an already-known key, with no relationships between different keys required, exactly the shape of a login-session lookup.",
        "medium", "apply", "types-of-databases",
        "A key-value store — an already-known key returns its value instantly, with no relationships needed",
        ["The relational model — because login data must always live in fixed rows and columns", "A document database — because sessions vary too much to use any other model", "None of these; session data cannot be stored in a database at all"],
    ),
    (
        "One restaurant listing includes a delivery-time estimate and a minimum order value. Another restaurant in the same list skips both and instead carries a \"dine-in only\" flag that the first restaurant never needed.\n\nWhich database model is built to embrace this kind of variation?",
        "A document database stores each record as a self-contained bundle, and different records in the same collection are allowed to hold entirely different fields, exactly the flexibility this restaurant data needs.",
        "medium", "apply", "types-of-databases",
        "A document database — records in the same collection can hold different fields",
        ["The relational model — every row in a relational table is expected to share the same columns", "A key-value store — because restaurant listings are looked up by name only", "None of these; varying fields must always be split into three separate tables"],
    ),
    (
        "Why would a relational table resist storing the varying restaurant listings described above, where one restaurant has fields another restaurant doesn't need at all?",
        "Every row in a relational table is expected to share the same set of columns, so fields that only some restaurants need would either force empty columns everywhere or force restructuring the table awkwardly.",
        "hard", "analyze", "types-of-databases",
        "Because every row in a relational table is expected to share the same fixed set of columns",
        ["Because relational tables cannot store text values, only numbers", "Because relational databases do not allow more than one table per application", "Because relational tables can only hold a maximum of four columns"],
    ),
    (
        "Kiran's mentor shows her three different database systems already running behind apps she uses daily, and none of the three \"outranks\" the others.\n\nWhat should actually decide which database model to use for a given piece of data?",
        "The lesson's guiding habit is to ask what shape the data naturally takes, structured and interconnected, a simple key-driven lookup, or flexible and record-by-record, and let that shape decide the tool, not familiarity or habit.",
        "medium", "understand", "types-of-databases",
        "The natural shape the data takes on its own, not familiarity with any one particular technology",
        ["Whichever database model the development team already knows best, regardless of the data", "Whichever database is the newest and most recently released", "The one that requires the least amount of storage space, regardless of structure"],
    ),
]

# --- why-relational-databases-first (5) ---
WHY_RELATIONAL = [
    (
        "Farhan's manager asks: \"Which proposal could literally any developer at this company sit down and query correctly on their very first day, without asking you a single question?\"\n\nWhat is this question really testing?",
        "The question is about the relational model's payoff: tables and SQL are already familiar and standardized, so a new developer can be productive immediately, unlike a system with a syntax invented specifically for one company.",
        "medium", "understand", "why-relational-databases-first",
        "Whether the design relies on shapes and a query language that are already familiar and standardized industry-wide",
        ["Whether the proposal uses the newest available database technology", "Whether the shipment data includes every possible field a customer might need", "Whether the database can be hosted without an internet connection"],
    ),
    (
        "Farhan's manager doesn't have to reconstruct the shape of the shipments table in her head when she reviews it.\n\nWhy do relational tables carry this kind of built-in familiarity?",
        "A relational table is a grid of rows and columns, the same shape as a spreadsheet, attendance register, or printed timetable, so most people already have the right mental model before writing a single line of code.",
        "easy", "understand", "why-relational-databases-first",
        "Rows and columns are the same shape as a spreadsheet or attendance register that most people already understand",
        ["Relational tables always display a helpful tutorial explaining their structure", "Relational tables are simpler because they can only hold a single column", "Familiarity comes from relational databases being invented very recently"],
    ),
    (
        "SQL is described as an \"industry standard.\" What concrete, checkable benefit does that label actually point to?",
        "Being an industry standard means decades of accumulated tooling, documentation, hiring pools, and battle-tested behavior, so a query written for one relational database mostly transfers to another, and most backend developers already know it.",
        "medium", "apply", "why-relational-databases-first",
        "A query written for one relational database mostly transfers to another, backed by decades of tooling and a large hiring pool",
        ["It means SQL queries always run faster than any other query language", "It means every company is legally required to use SQL for its data", "It means SQL was invented by an international standards committee last year"],
    ),
    (
        "Farhan's manager imagines needing to hire three more backend developers next quarter. If the shipments system used a query syntax invented specifically for one company instead of SQL, what would that cost?",
        "Every new hire would need weeks of ramp-up just to learn that one-off storage layer before being trusted to write a single feature, unlike SQL knowledge, which usually transfers in from a developer's previous job.",
        "hard", "analyze", "why-relational-databases-first",
        "Every new hire would need weeks of ramp-up learning the one-off syntax before becoming productive",
        ["Nothing — proprietary query languages are always faster to learn than SQL", "The company would be unable to hire any developers at all", "It would only affect developers hired from outside the country"],
    ),
    (
        "Does choosing tables and SQL as the default starting point mean that no other kind of database ever makes sense?",
        "The lesson is explicit that this is a starting point, not a verdict: some data genuinely fits a flexible, bundle-of-fields shape better, and many successful systems combine a relational core with a different store for a specific need.",
        "medium", "analyze", "why-relational-databases-first",
        "No — it's a sensible starting point, and many systems combine a relational database with other stores for specific needs",
        ["Yes — every serious production system must use only relational databases forever", "Yes — key-value and document databases were only ever proof-of-concept ideas", "No — but only small companies are ever allowed to use non-relational databases"],
    ),
]

# --- database-users-and-roles (4) ---
USERS_ROLES = [
    (
        "Ravi types a professor's name into his college portal's search box and gets office hours and a contact email back, without ever wondering how the search works.\n\nWhich role does Ravi represent?",
        "Ravi interacts with the database only through the application's screen, with no need to know whether it runs on a relational database or anything else, exactly the description of an end user.",
        "easy", "remember", "database-users-and-roles",
        "End user — he interacts with the database only through the application's screen",
        ["Developer — he is deciding what counts as a matching search", "Database administrator — he is confirming backups completed", "None of these; searching a portal requires no relationship to a database at all"],
    ),
    (
        "Kiran spends an hour deciding exactly what request the search box should send when a name is typed, including whether a partial spelling should count as a match.\n\nWhich role does Kiran represent, and why?",
        "Kiran writes the code that translates a user's action into an actual request the query processor can answer, and translates the result back into something readable, exactly the developer's job of building the bridge.",
        "medium", "understand", "database-users-and-roles",
        "Developer — she builds the code that translates a user's action into a request the database can answer",
        ["End user — she is simply testing the search box like any other user", "Database administrator — she is responsible for who can access which data", "None of these; deciding on matching logic has nothing to do with a database"],
    ),
    (
        "Aisha spends twenty minutes confirming that last night's backup of the entire portal actually completed without errors, and she also decided that only staff may view a student's full academic history.\n\nWhich role does Aisha represent?",
        "Managing backups, access rules, and overall system health, rather than writing search logic or using the app as an end user, is exactly the responsibility of a database administrator (DBA).",
        "medium", "apply", "database-users-and-roles",
        "Database administrator (DBA) — she manages backups, access rules, and system health",
        ["End user — she is just checking her own academic history", "Developer — she wrote the portal's search-matching logic", "A fourth, unrelated role not described in the lesson"],
    ),
    (
        "The lesson notes that \"nobody thanks Aisha\" when a search returns fast results or a semester passes without a lost record.\n\nWhy is a DBA's success typically invisible?",
        "A DBA's success looks exactly like nothing going wrong, backups quietly completing, servers staying up, so the work only becomes visible during a rare bad week, like a crash or a failed backup, rather than through positive recognition.",
        "hard", "analyze", "database-users-and-roles",
        "Because success looks like nothing going wrong; the job only becomes visible when something rare goes badly",
        ["Because DBAs are not allowed to discuss their work with other staff", "Because DBA responsibilities are entirely automated and require no real effort", "Because end users are responsible for backups instead of the DBA"],
    ),
]

# --- data-lifecycle (4) ---
DATA_LIFECYCLE = [
    (
        "The instant Asha taps \"confirm order,\" a new record is created holding her order ID, restaurant, items, total, address, and a status field starting as `placed`.\n\nWhich stage of the data lifecycle does this represent?",
        "A brand-new fact entering the database for the very first time, exactly once, is the creation stage, the simplest and earliest point in the lifecycle.",
        "easy", "remember", "data-lifecycle",
        "Creation — a new record enters the database for the first time",
        ["Query — the record is being read for the first time", "Update — an existing record's fields are being changed", "Deletion — the record is being removed from the database"],
    ),
    (
        "Between the order being placed and delivered, the kitchen screen, the delivery app, the rider's app, and Asha herself all read the same order record repeatedly, far more often than it is ever changed.\n\nWhich lifecycle stage does this describe, and how common is it?",
        "This is the query stage: the ordinary, everyday shape of most data in most systems is created once, then read repeatedly by many different people and programs for different reasons.",
        "medium", "understand", "data-lifecycle",
        "Query — and it is the most frequent stage, since most data is read far more often than it is changed",
        ["Update — because the status field changes every time someone checks it", "Creation — because each read effectively creates a new copy of the order", "Deletion — because reading old data eventually causes it to be archived"],
    ),
    (
        "Asha's order status moves from `placed` to `preparing` to `picked up` to `delivered`. Each change updates the same row rather than creating a new one.\n\nWhy does the lesson emphasize that this happens \"in place\" on the same row?",
        "Updating the same row in place is precisely why Asha's tracker shows one order moving through stages instead of a growing list of separate, disconnected orders, each representing a different snapshot.",
        "medium", "apply", "data-lifecycle",
        "Because updating the same row is what lets the tracker show one order progressing through stages, instead of a pile of disconnected records",
        ["Because databases are physically unable to create more than one row per customer", "Because creating a new row for every status change would be faster for the kitchen to read", "It has no real effect; a new row per status change would behave identically"],
    ),
    (
        "A bank keeps transaction records for years, while a temporary discount code might be deleted the day it expires.\n\nWhat determines whether data is deleted outright or archived rather than deleted immediately?",
        "The choice depends on whether the data might still matter later: legal and trust requirements keep bank transactions around for years, while a discount code that nothing will ever need again can be deleted right away.",
        "hard", "analyze", "data-lifecycle",
        "Whether the data might still matter later — for legal, trust, or business reasons — rather than a fixed rule applied to all data",
        ["The file size of the record — larger records are always deleted sooner", "The order in which the data was originally created", "Whether the data belongs to a paying customer or a free-tier user"],
    ),
]

SET1_SOURCES = [
    (DATA_VS_INFO, 0),
    (PROBLEMS_WITH_FILES, 0),
    (DB_VS_DBMS, 0),
    (DBS_EVERYDAY, 0),
    (TYPES_OF_DBS, 0),
    (WHY_RELATIONAL, 0),
    (USERS_ROLES, 0),
    (DATA_LIFECYCLE, 0),
]

SYNTHESIS = [
    (
        "Four ideas from this chapter: (1) data becomes information once it has context, (2) a database is distinct from the DBMS that manages it, (3) redundant copies of a fact can go inconsistent, (4) a database's job includes preventing lost updates.\n\nWhich pair below correctly matches a concept to its admissions-office example?",
        "Rohan's category showing \"General\" in one file and \"SC\" in another is two redundant copies of the same fact disagreeing, exactly what inconsistency means.",
        "medium", "analyze", "problems-with-files",
        "Inconsistency — Rohan's category shows \"General\" in `applicants.xlsx` but \"SC\" in `interviews.xlsx`",
        ["Data vs. information — PostgreSQL is the software managing the admissions data", "Lost update — Ravi searches for a professor's name and gets office hours back", "Database vs. DBMS — two coordinators' saves to the same file collide within a minute"],
    ),
    (
        "A retail company is deciding how to store three very different kinds of data: (a) structured order records with customer, total, and status, (b) session tokens looked up by a single key, (c) product listings where different products carry very different sets of attributes.\n\nWhich pairing of data shape to database model is correct?",
        "This mirrors Kiran's food delivery app: structured, interrelated records fit the relational model, single-key lookups fit key-value stores, and records that vary in shape fit document databases.",
        "hard", "apply", "types-of-databases",
        "(a) relational, (b) key-value, (c) document",
        ["(a) document, (b) relational, (c) key-value", "(a) key-value, (b) document, (c) relational", "All three should use the same single database model for consistency"],
    ),
]

SET1 = []
for src, idx in SET1_SOURCES:
    SET1.append(src[idx])
SET1.extend(SYNTHESIS)

SET2 = (
    DATA_VS_INFO[1:]
    + PROBLEMS_WITH_FILES[1:]
    + DB_VS_DBMS[1:]
    + DBS_EVERYDAY[1:]
    + TYPES_OF_DBS[1:]
    + WHY_RELATIONAL[1:]
    + USERS_ROLES[1:]
    + DATA_LIFECYCLE[1:]
)

assert len(SET1) == 10, len(SET1)
assert len(SET2) == 30, len(SET2)


def build_rows(items, set_label, title_prefix):
    positions = [(i % 4) + 1 for i in range(len(items))]
    random.shuffle(positions)

    rows = []
    for idx, (desc, expl, diff, bloom, subtopic, correct, distractors) in enumerate(items, start=1):
        pos = positions[idx - 1]
        options = distractors[:]
        options.insert(pos - 1, correct)
        rows.append({
            "title": f"{title_prefix}.{idx}",
            "description": desc,
            "explanation": expl,
            "score": 1,
            "status": "published",
            "difficulty": diff,
            "bloomTaxonomy": bloom,
            "tags": f"dbms - {set_label}",
            "subjects": "dbms",
            "topics": "database-foundations",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 1.1.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 1.1.2")
all_rows = rows1 + rows2


def summarize(name, rs):
    diff, bloom, sub, ans = {}, {}, {}, {1: 0, 2: 0, 3: 0, 4: 0}
    for r in rs:
        diff[r["difficulty"]] = diff.get(r["difficulty"], 0) + 1
        bloom[r["bloomTaxonomy"]] = bloom.get(r["bloomTaxonomy"], 0) + 1
        sub[r["subTopics"]] = sub.get(r["subTopics"], 0) + 1
        ans[r["answer"]] += 1
    print(name, "diff:", diff)
    print(name, "bloom:", bloom)
    print(name, "subtopics:", sub)
    print(name, "answers:", ans)


summarize("SET1", rows1)
summarize("SET2", rows2)

descs = [r["description"] for r in all_rows]
assert len(descs) == len(set(descs)), "duplicate description found"
for r in all_rows:
    opts = [r["option1"], r["option2"], r["option3"], r["option4"]]
    assert len(set(opts)) == 4, f"duplicate option in {r['title']}: {opts}"

headers = ["title", "description", "explanation", "score", "status", "difficulty", "bloomTaxonomy",
           "tags", "subjects", "topics", "subTopics", "companies",
           "option1", "option2", "option3", "option4", "answer"]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "DBMS - MCQ - Unit 1.1"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 1 - Database Foundations/1.1 - What is a Database - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
