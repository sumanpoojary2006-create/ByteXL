import random
import openpyxl

random.seed(31)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

THREE_SCHEMA = [
    (
        "Tara's college results portal shows her only her own name, roll number, and four subject scores, nothing about any other student and nothing about the raw files on the server.\n\nWhich level of the three-schema architecture is she interacting with?",
        "The external level hands each user or application a narrow, purpose-built slice of the data — exactly Tara's tailored result screen, shaped around what she specifically needs to see.",
        "easy", "understand", "three-schema-architecture",
        "The external level — a tailored slice of the data built for one user or application",
        ["The conceptual level — the registrar's overall structural design", "The internal level — how bytes are laid out on disk", "The system catalog — the database's metadata about itself"],
    ),
    (
        "The registrar's team designed a Students entity, a Courses entity, and a Marks entity, describing the overall structure of the entire database independent of any one screen. Neither Tara nor a professor ever looks at this design directly.\n\nWhich level of the three-schema architecture does this describe?",
        "This is the conceptual (or logical) schema — the registrar's shared structural picture that every external view is ultimately drawn out of, even though no end user sees it directly.",
        "medium", "understand", "three-schema-architecture",
        "The conceptual level",
        ["The external level", "The internal level", "The application level"],
    ),
    (
        "Tara has no idea, and no reason to care, whether her marks are stored in one large file or split cleverly across several files for speed.\n\nWhich level of the architecture is responsible for that storage detail, and who mainly works at that level?",
        "The internal (physical) level is concerned with how rows are actually stored on disk, which files hold which table's data, and what indexes exist. A database administrator tuning performance lives at this level far more than anyone else.",
        "medium", "apply", "three-schema-architecture",
        "The internal level, mainly the concern of a database administrator",
        ["The external level, mainly the concern of an end user like Tara", "The conceptual level, mainly the concern of a professor", "The system catalog, mainly the concern of a query processor"],
    ),
    (
        "A professor logging into the same underlying database as Tara sees a class list with average scores and no individual contact details, a completely different screen from Tara's own result view.\n\nWhat does this illustrate about the external level?",
        "The same database can support several different external views at once, each shaped around what one kind of user or application actually needs to see, all drawn from the same shared conceptual schema underneath.",
        "medium", "apply", "three-schema-architecture",
        "One database can support multiple different external views, each tailored to a different user or application",
        ["Every user of a database must always see the exact same screen", "A professor's view and a student's view must come from two entirely separate databases", "External views can only ever show numeric data, never names"],
    ),
    (
        "Why does splitting a database's description into external, conceptual, and internal layers, rather than fusing them into one tangled picture, matter in practice?",
        "The registrar's team can reason about students and marks without touching disk blocks, a DBA can reason about disk blocks without redesigning what a student sees, and whoever builds the results portal can design around the conceptual schema without needing storage details — each group works confidently at its own level.",
        "hard", "analyze", "three-schema-architecture",
        "It lets each group (end users, designers, and administrators) work confidently at their own level without needing to understand or disturb the others",
        ["It makes the database run faster by reducing the total number of tables", "It removes the need for a database to have a conceptual schema at all", "It ensures that every application automatically sees identical data"],
    ),
    (
        "Some of the earliest data-handling systems wired the screen a student stares at directly to the exact bytes on disk, with nothing in between.\n\nWhat specific risk did this create, the risk the three-schema architecture was built to avoid?",
        "The moment a screen depends directly on file layout, moving a file, adding an index, or reorganising storage for speed risks breaking the screen too — exactly the mess a proper database, with its layered schemas, was invented to avoid.",
        "medium", "analyze", "three-schema-architecture",
        "Moving a file or reorganising storage for speed would risk breaking the screen, since it depended directly on file layout",
        ["It made the database use significantly more disk space than necessary", "It prevented more than one student from using the portal at the same time", "It made every query run through the transaction manager twice"],
    ),
    (
        "A college's fee portal, built on the same underlying database as Tara's results portal, shows dues and payments rather than marks.\n\nWhich level of the three-schema architecture does the fee portal's screen belong to?",
        "The fee portal is another external view, a different application-specific slice drawn from the very same shared conceptual schema that also produces Tara's result screen and the professor's class list.",
        "medium", "apply", "three-schema-architecture",
        "The external level — it's a different application-specific view drawn from the same shared conceptual schema",
        ["The conceptual level, since it defines a completely new structural design", "The internal level, since it deals with how dues are stored on disk", "None of the three levels; billing screens exist outside the three-schema architecture"],
    ),
]

DATA_INDEPENDENCE = [
    (
        "Ravi's team swaps the company's ageing disks for solid-state drives and reorganises how order records are laid out on disk, with new file groupings and new indexes. The next morning, the checkout screen works exactly as before, and no application team even knows the disks changed.\n\nWhat is this an example of?",
        "Physical data independence means the internal, physical level, how data is actually stored on disk, can be changed without requiring any change to the conceptual schema or to applications built on top of it.",
        "easy", "understand", "data-independence",
        "Physical data independence",
        ["Logical data independence", "A foreign key constraint", "A composite key"],
    ),
    (
        "The product team asks Ravi to add a new column to the Orders table recording whether a customer tipped the delivery partner. After he adds it, dozens of existing screens and reports that never asked about tips keep working exactly as before, untouched.\n\nWhat allowed this to happen without a company-wide rewrite?",
        "Logical data independence means the conceptual schema can be extended without forcing every application that uses it to change too. Existing reports were never written to demand every column of the Orders table, so a new column arriving simply didn't concern them.",
        "medium", "apply", "data-independence",
        "Logical data independence — extending the schema with a new column didn't force unrelated applications to change",
        ["Physical data independence — the disks were upgraded at the same time", "A foreign key was added automatically to the new column", "The system catalog was disabled during the schema change"],
    ),
    (
        "Applications talk to Ravi's database in terms of \"an order with a customer, a restaurant, a list of items, and a total,\" never in terms of \"the fourth file on the second drive.\"\n\nWhy does this matter for physical data independence?",
        "Because applications rely on the logical definition of an order rather than the physical storage details, a storage reshuffle stays completely invisible above it — the checkout screen gets the same answer regardless of which drive or file layout holds the bytes underneath.",
        "medium", "analyze", "data-independence",
        "Because applications depend only on the logical definition of the data, changes to physical storage stay invisible to them",
        ["Because applications are required to know the exact file and drive holding each record", "Because physical storage never actually changes in a well-run database", "Because the query processor stores a copy of every file location for every application"],
    ),
    (
        "What would happen to a company's ability to improve its database if every application were wired directly to demand the exact, unchanging shape of a table, with no data independence at all?",
        "Without data independence, the database would calcify — too risky to improve, because improving it (whether storage or schema) would break everything built on top, and the company could never grow its data model without rewriting every screen that touches it.",
        "hard", "analyze", "data-independence",
        "The database would calcify — any improvement to storage or schema would risk breaking every application built on top of it",
        ["Nothing would change; applications would automatically adapt to any new table shape", "The database would become faster, since applications would be tightly optimized to it", "The company would only be affected if it used more than one DBMS at a time"],
    ),
    (
        "Physical data independence and logical data independence both protect applications from a kind of change.\n\nWhat is the key difference between what each one protects applications from?",
        "Physical independence protects applications from decisions about disk and storage layout; logical independence protects them from the schema itself growing or changing shape, such as new columns or relationships being added.",
        "medium", "understand", "data-independence",
        "Physical independence isolates apps from storage/disk changes; logical independence isolates them from changes to the schema's structure",
        ["Physical independence isolates apps from schema changes; logical independence isolates them from disk changes", "There is no real difference; both terms describe exactly the same protection", "Physical independence applies only to read operations; logical independence applies only to write operations"],
    ),
    (
        "During Ravi's hardware migration, the files holding order records moved to new drives, got reorganised, and gained new indexes. Separately, the definition of what an \"order\" is, how many columns it has, and how it relates to customers never changed.\n\nWhich of these two groups of facts belongs to the physical level, and which to the conceptual level?",
        "Moving files, reorganising layout, and adding indexes are all physical-level changes; the definition of an order's columns and relationships is the conceptual level, which stayed completely untouched by the migration.",
        "medium", "understand", "data-independence",
        "File moves, reorganisation, and indexes are physical-level; the order's definition and relationships are conceptual-level",
        ["File moves and indexes are conceptual-level; the order's definition is physical-level", "Both groups belong to the physical level, since both involve the Orders table", "Both groups belong to the conceptual level, since neither involves an end user directly"],
    ),
    (
        "When Ravi added the tip column, only the small handful of screens that actually needed to show or record a tip had to change, and the lesson describes that change as \"additive rather than disruptive.\"\n\nWhat does \"additive rather than disruptive\" mean here?",
        "The change only added something new for the applications that actually needed it, while every existing report, screen, and background job that never asked about tips kept working exactly as before, since they were never written to demand every column of the table.",
        "medium", "apply", "data-independence",
        "The new column only affected the few applications that needed it; everything else kept working exactly as before, untouched",
        ["Every application in the company had to be rewritten to account for the new column", "The new column silently deleted the old columns it was added next to", "The change was reversed automatically once every screen was updated"],
    ),
]

DBMS_COMPONENTS = [
    (
        "Meera's senior engineer sketches three boxes on a whiteboard: Query Processor, Storage Manager, and Transaction Manager, using the scene of thousands of people trying to book the same concert seat at once.\n\nWhich component interprets a request like \"find all available seats in the front section\" and decides on a sensible way to answer it?",
        "The query processor takes a query as written, checks it is grammatically valid, works out what it is actually asking for, and decides on a sensible plan of action, such as whether to scan every seat or jump to an index.",
        "easy", "remember", "dbms-components",
        "The query processor",
        ["The storage manager", "The transaction manager", "The system catalog"],
    ),
    (
        "Once the query processor has decided what needs fetching, some component has to actually read or write the seat records from wherever they physically live on disk.\n\nWhich component does this?",
        "The storage manager deals with the internal, physical reality of the database, the files, blocks, and indexes, handling every read and write that touches that layer, without the query processor needing to know exactly where a record sits.",
        "easy", "remember", "dbms-components",
        "The storage manager",
        ["The query processor", "The transaction manager", "The external schema"],
    ),
    (
        "Two people try to book the exact same concert seat, A12, within the same second. Left unmanaged, both bookings could read \"seat available,\" both proceed, and the venue would end up with one seat sold twice.\n\nWhich component prevents this, and how?",
        "The transaction manager treats each booking as a single, self-contained unit of work and ensures that even when many transactions run at the same moment, the result looks as if they happened one after another, so one booking succeeds cleanly and the other is correctly told the seat is taken.",
        "medium", "apply", "dbms-components",
        "The transaction manager — it ensures concurrent bookings are handled as if they occurred one after another, without corrupting the data",
        ["The query processor — it rejects the second request as grammatically invalid", "The storage manager — it physically locks the disk file containing all seats", "The system catalog — it records which user booked first for legal purposes"],
    ),
    (
        "The storage manager is described as what makes physical data independence possible in the first place.\n\nWhy is that connection true?",
        "The query processor never has to know whether a seat record lives in file three or file thirty; it simply asks the storage manager for \"the record for seat A12,\" and the storage manager works out where that record actually sits. If disks change, the storage manager keeps speaking the same language to everything above it.",
        "hard", "analyze", "dbms-components",
        "Because the storage manager hides physical storage details from the query processor, so storage changes never need to ripple upward",
        ["Because the storage manager and physical data independence are unrelated ideas that happen to share a name", "Because the storage manager is responsible for writing every application's user interface", "Because physical data independence only applies to the transaction manager, not the storage manager"],
    ),
    (
        "Why does a DBMS split query interpretation, physical storage, and concurrency control into three separate components rather than one component handling all three?",
        "None of the three could do a good job of another's work — a query processor also worrying about disk block layout would be tangled and slow to change, and a storage manager also refereeing simultaneous bookings would be reinventing the transaction manager badly. Giving each concern its own dedicated component keeps each one understandable, testable, and improvable on its own terms.",
        "medium", "understand", "dbms-components",
        "Each component can be understood, tested, and improved on its own terms, rather than being tangled together with unrelated responsibilities",
        ["Splitting them up makes the database use less disk space overall", "A DBMS is legally required to have exactly three internal components", "Combining them would make queries return results in a different order"],
    ),
    (
        "Before this week, Meera drew the entire database as one indivisible box in her own diagrams. After learning about the query processor, storage manager, and transaction manager, what changes for her, according to the lesson's conclusion?",
        "The next time a query runs slowly, or two bookings conflict unexpectedly, she now has a mental map of which component is actually responsible, rather than treating the whole database as one unexplainable mystery.",
        "medium", "understand", "dbms-components",
        "She gains a mental map of which component is responsible for a given problem, instead of treating the database as one unexplainable box",
        ["She learns to write a query processor herself from scratch", "She no longer needs to write any queries at all going forward", "She discovers the three components can be safely merged into one"],
    ),
    (
        "According to the components table, which DBMS component's main job touches \"the incoming query itself, before any data is read\"?",
        "The query processor's job is answering what a request is actually asking for and deciding on a plan, working with the incoming query itself before any data has been read.",
        "easy", "remember", "dbms-components",
        "The query processor",
        ["The storage manager", "The transaction manager", "The system catalog"],
    ),
]

SYSTEM_CATALOG = [
    (
        "Kabir types a query asking for a column called \"studentemail\" from the Students table. Before a single row comes back, the database stops him: no such column exists.\n\nHow did the database know this instantly, without scanning any student data?",
        "Somewhere inside every database sits the system catalog, a self-referential set of tables describing the database's own structure, including which columns each table actually has. The query is checked against the catalog before any real data is touched.",
        "easy", "understand", "system-catalog",
        "It checked the query against the system catalog, which records exactly which columns each table has",
        ["It scanned every row of the Students table looking for the column first", "It guessed based on similar column names used in other tables", "It asked the registrar's team directly before responding"],
    ),
    (
        "Which of the following is NOT something a typical system catalog keeps track of?",
        "The system catalog stores metadata about the database's own structure, table names, columns, keys, and permissions, not the business facts themselves, like a specific customer's actual order history.",
        "medium", "remember", "system-catalog",
        "The actual order history of a specific customer",
        ["Which column or columns act as the primary key for each table", "Which users or roles have permission to read or write each table", "What indexes exist, and which columns they are built on"],
    ),
    (
        "Kiran, a backend developer, says: \"The database does not just hold your data. It holds data about its own data too.\"\n\nWhat term describes this second kind of data, data describing data?",
        "This is metadata — information about the database's own structure, such as table names, column types, and constraints, rather than the actual business facts like student marks or customer orders.",
        "easy", "remember", "system-catalog",
        "Metadata",
        ["A transaction", "A relation", "A domain"],
    ),
    (
        "When Kiran tries to insert a new student record without a roll number, the database rejects the insert before it ever touches the stored rows.\n\nHow does the catalog make this rejection possible?",
        "The catalog records that roll number is a required column for the Students table, so the database can consult that recorded rule and reject the insert immediately, without needing to hand-code the check separately into every application.",
        "medium", "apply", "system-catalog",
        "The catalog records that roll number is a required column, letting the database check and reject the insert before touching stored data",
        ["The catalog stores a backup copy of every valid student record for comparison", "The database asks Kiran directly whether the insert should be allowed", "The catalog encrypts the insert request until a human approves it"],
    ),
    (
        "The lesson notes there is \"something almost playful\" about how a database treats its own catalog.\n\nWhat is that playful quality?",
        "The catalog stores its structural information using the very same mechanisms the database uses to store ordinary data, its tables have rows and columns, can be queried, and are protected by permissions, exactly like any other table in the system.",
        "hard", "analyze", "system-catalog",
        "The catalog is stored and queried using the exact same table-based mechanisms the database uses for ordinary business data",
        ["The catalog changes its own structure randomly every time the database restarts", "The catalog is the only part of the database that cannot be queried at all", "The catalog exists only in the query processor's temporary memory, never on disk"],
    ),
    (
        "Without a system catalog check, what would happen when Kabir's query asking for the nonexistent \"studentemail\" column was run instead?",
        "Instead of being refused immediately with a precise, useful error, the database might have to scan through thousands of rows only to fail later, or worse, silently return something wrong.",
        "hard", "analyze", "system-catalog",
        "The database might scan thousands of rows before failing later, or silently return an incorrect result, instead of refusing instantly",
        ["Nothing different would happen; the query would still be rejected just as fast", "The query would automatically create the missing column instead of failing", "The database would shut down entirely until an administrator intervened"],
    ),
    (
        "When Ravi added the new tip column to the Orders table, which part of the database was updated first, before any application could rely on the new column?",
        "The system catalog was updated first, to record that Orders now has one more column. Every other part of the database, and every application asking sensible questions of it, consults that same catalog to know what currently exists.",
        "medium", "apply", "system-catalog",
        "The system catalog, recording that Orders now has an additional column",
        ["The transaction manager, to lock every existing order row", "The external view shown to the checkout screen", "The storage manager's disk layout, before the catalog was told anything"],
    ),
]

QUERY_JOURNEY = [
    (
        "The moment Tara taps \"View Result,\" the portal sends a SQL request to the database. At this very first stage, has the database checked whether the request makes sense or gone anywhere near the stored marks yet?",
        "At the first stage, the query is nothing more than text, a precisely structured sentence. The database has simply received the request, like a receptionist receiving a visitor's name before deciding which office to send them to.",
        "easy", "remember", "sql-to-result-set",
        "No — the query has only just arrived as plain text; nothing has been checked or fetched yet",
        ["Yes — the database has already validated the query and fetched the marks", "Yes — the database has already chosen an execution plan at this stage", "No — the database has already rejected the query as invalid by this point"],
    ),
    (
        "Before Tara's query goes any further, it is checked for correct grammar and broken into its meaningful pieces, then compared against the database's own record of what tables and columns actually exist.\n\nWhich stage of the query's journey does this describe, and what would it catch?",
        "This is the parsing and catalog-check stage, the same stage that would catch a mistyped column name (like Kabir's earlier mistake) before the query ever touches real data.",
        "medium", "apply", "sql-to-result-set",
        "Parsing and catalog check — it would catch a misspelled column name or a table that doesn't exist",
        ["Execution — it would catch a conflict with another simultaneous transaction", "Result set return — it would catch a formatting error in the final output", "Planning — it would catch a slow-running query after it has already finished"],
    ),
    (
        "A validated query asking for Tara's marks could be answered by scanning every row of the Marks table, or by jumping straight to an index built on roll number.\n\nWhich stage of the query's journey decides between these options, and who notices this stage happening?",
        "This is the planning stage, choosing a sensible way to fetch the answer. It is entirely invisible to Tara — she only ever sees the final screen, never the decision-making that happened to produce it quickly.",
        "medium", "understand", "sql-to-result-set",
        "Planning — and it is invisible to the end user, who only sees the final result",
        ["Parsing — and it is visible to the end user as an error message", "Execution — and the database administrator must approve it manually each time", "Result set return — and it happens after the answer has already been shown"],
    ),
    (
        "If Tara checks her result at the exact moment an administrator is updating another student's marks nearby, what does the database still have to guarantee during the execution stage?",
        "The database has to guarantee that Tara's read is not corrupted or left half-finished by that unrelated, simultaneous activity elsewhere in the same tables — fetching the right bytes and keeping concurrent activity from interfering are two distinct jobs handled together during execution.",
        "hard", "analyze", "sql-to-result-set",
        "That Tara's read is not corrupted or left half-finished by the unrelated, simultaneous update happening elsewhere",
        ["That the administrator's update is cancelled until Tara finishes viewing her results", "That Tara's query is delayed until the next business day", "Nothing extra is guaranteed; simultaneous activity on unrelated rows has no effect on correctness"],
    ),
    (
        "Put these four stages of a query's journey in the correct order: (a) execution against stored data, (b) parsing and catalog check, (c) SQL arrives as plain text, (d) planning a fetch strategy.",
        "The journey runs: the SQL request arrives as plain text, it is parsed and checked against the catalog, a plan for fetching the answer is chosen, and only then is that plan executed against the actual stored data, after which the result set returns.",
        "medium", "understand", "sql-to-result-set",
        "(c) SQL arrives, (b) parsing and catalog check, (d) planning, (a) execution",
        ["(a) execution, (c) SQL arrives, (d) planning, (b) parsing and catalog check", "(b) parsing and catalog check, (a) execution, (c) SQL arrives, (d) planning", "(d) planning, (b) parsing and catalog check, (c) SQL arrives, (a) execution"],
    ),
    (
        "Before shadowing the on-call engineer, Aisha assumed a query is basically answered \"the moment it is typed, as if asking a question and getting an answer were a single, instant act.\"\n\nWhat did watching the logs actually reveal to her instead?",
        "It's really a short journey with distinct, ordered stops: the request is checked before it is trusted, a plan is chosen before anything is fetched, and only then does an answer come back.",
        "medium", "understand", "sql-to-result-set",
        "A query travels through a short journey of distinct, ordered stops — checked, planned, and only then fetched and returned",
        ["A query really is answered in one single, instant step, exactly as she originally assumed", "A query is answered only once a human administrator manually approves it", "A query's journey has no fixed order; steps happen in a random sequence each time"],
    ),
    (
        "\"Only once the request has been confirmed to make structural sense, a real table, real columns, a real relationship between Students and Marks, does the database consider it safe to proceed any further.\"\n\nWhich stage does this sentence describe, and what does passing it unlock?",
        "This describes the parsing and catalog-check stage; passing it is what allows the database to move on to choosing a plan and eventually executing it, rather than stopping the journey right there.",
        "medium", "apply", "sql-to-result-set",
        "The parsing and catalog check stage — passing it unlocks the planning and execution stages that follow",
        ["The result set stage — passing it unlocks a second, independent query", "The execution stage — passing it unlocks the original SQL text", "The planning stage — passing it unlocks the catalog check that follows it"],
    ),
]

SYNTHESIS = [
    (
        "A DBA reorganises how order records are stored on disk (new files, new indexes), and separately, a product team adds a new column to the same table.\n\nWhich two concepts from this chapter, each protecting applications from a different kind of change, are illustrated here?",
        "The disk reorganisation is protected by physical data independence, and the new column is protected by logical data independence — the two forms of independence that let the internal level and the conceptual level each evolve without forcing every application to change too.",
        "medium", "analyze", "data-independence",
        "Physical data independence (for the storage reorganisation) and logical data independence (for the new column)",
        ["Physical data independence for both changes, since both involve the same table", "Logical data independence for both changes, since both are made by the same team", "The system catalog for both changes, since neither involves the query processor"],
    ),
    (
        "Kabir's mistyped column name is rejected instantly at the parsing stage of the query journey, thanks to the system catalog. Meanwhile, a DBA reasons about disk blocks without knowing what a \"student\" means conceptually.\n\nHow does the system catalog relate to the three-schema architecture?",
        "The catalog records the conceptual schema's structure (tables, columns, keys) so that queries can be validated against it, while the internal level's physical storage details remain a separate concern the catalog doesn't need to expose to query validation.",
        "hard", "analyze", "system-catalog",
        "The catalog records the conceptual schema's structure, letting queries be validated against it independently of internal storage details",
        ["The system catalog is simply another name for the internal, physical schema", "The system catalog only exists at the external level, and has no connection to the conceptual schema", "The catalog and the three-schema architecture are entirely unrelated ideas covered coincidentally in the same chapter"],
    ),
    (
        "During the execution stage of a query's journey, which DBMS component actually fetches the bytes from disk, and which component ensures that fetch isn't corrupted by a simultaneous, unrelated update?",
        "The storage manager is responsible for physically locating and reading the record, while the transaction manager ensures that concurrent activity, such as an administrator's simultaneous update, does not corrupt or interfere with that read.",
        "medium", "apply", "dbms-components",
        "The storage manager fetches the bytes; the transaction manager guards against corruption from concurrent activity",
        ["The query processor fetches the bytes; the system catalog guards against corruption", "The transaction manager fetches the bytes; the storage manager guards against corruption", "The system catalog fetches the bytes; the query processor guards against corruption"],
    ),
    (
        "A student's results portal (external view), the registrar's Students/Courses/Marks design (conceptual schema), and the disk files holding that data (internal schema) are three separate descriptions of the same database.\n\nWhich DBMS component's main job is to interpret a request written against the conceptual schema and decide how to translate it into actual work?",
        "The query processor is the component that takes a request, works out what it's actually asking for in terms of the conceptual schema, and decides on a plan of action, before the storage manager gets involved in the internal level's details.",
        "medium", "understand", "dbms-components",
        "The query processor",
        ["The system catalog", "The storage manager alone, without the query processor's involvement", "The external schema itself, since it interprets its own requests"],
    ),
    (
        "If Ravi's storage migration had NOT been protected by physical data independence, what specifically would have gone wrong the morning after the migration?",
        "Without physical data independence, applications would be wired directly to disk file layout, so moving files or adding indexes would break every screen and query built on top, turning a routine storage upgrade into a company-wide outage.",
        "hard", "analyze", "data-independence",
        "Every application wired to the old file layout would break, turning a routine storage upgrade into a company-wide outage",
        ["Nothing different would happen, since physical data independence has no real effect on migrations", "Only the system catalog would need to be rewritten, with no effect on applications", "The transaction manager would automatically fix any broken queries within seconds"],
    ),
]

SET1_SOURCES = [
    (THREE_SCHEMA, 0),
    (DATA_INDEPENDENCE, 0),
    (DBMS_COMPONENTS, 0),
    (SYSTEM_CATALOG, 0),
    (QUERY_JOURNEY, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    THREE_SCHEMA[1:]
    + DATA_INDEPENDENCE[1:]
    + DBMS_COMPONENTS[1:]
    + SYSTEM_CATALOG[1:]
    + QUERY_JOURNEY[1:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 1.3.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 1.3.2")
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
ws.title = "DBMS - MCQ - Unit 1.3"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 1 - Database Foundations/1.3 - DBMS Architecture - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
