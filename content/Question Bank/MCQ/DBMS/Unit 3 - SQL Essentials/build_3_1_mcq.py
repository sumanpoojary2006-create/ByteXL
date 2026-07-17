import random
import openpyxl

random.seed(53)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

CHOOSING_DB_SYSTEM = [
    (
        "Ishaan's robotics club data, members, events, attendance records, and the relationships between them, is described as \"a textbook fit for the relational shape.\"\n\nWhy does it fit so naturally?",
        "It's structured, interrelated data: a member belongs to the club, attends events, and each attendance record links a specific member to a specific event on a specific date, exactly the kind of structured, interrelated data a relational system was designed to hold.",
        "easy", "understand", "choosing-a-database-system",
        "It's structured and interrelated, with attendance records linking specific members to specific events, exactly what relational systems are designed to hold",
        ["It has no relationships between different pieces of data at all", "It is loosely structured, closer to logs or a recommendation graph", "It only ever needs a single table with no keys at all"],
    ),
    (
        "Almost every database name Ishaan encountered belongs to one of two broad families.\n\nWhat are those two families?",
        "The relational family (PostgreSQL, MySQL, SQLite, Oracle, SQL Server, all organizing data into rows and columns with a shared query language) and the NoSQL family (documents, key-value pairs, or graphs, for data that doesn't fit the relational shape naturally).",
        "easy", "remember", "choosing-a-database-system",
        "The relational family and the NoSQL family",
        ["The open-source family and the commercial family", "The cloud family and the on-premises family", "The SQL family and the CLI family"],
    ),
    (
        "What does the lesson say makes PostgreSQL's learning \"transfer almost unchanged\" to most other relational systems a developer might meet later?",
        "PostgreSQL has spent decades closely following the official SQL standard rather than inventing its own shortcuts, so what's learned on it transfers cleanly because it behaves predictably and sticks to that shared standard.",
        "medium", "understand", "choosing-a-database-system",
        "It closely follows the official SQL standard rather than inventing its own shortcuts",
        ["It is the only relational database that supports SQL at all", "It automatically converts its own syntax into any other system's dialect", "It was the very first relational database system ever created"],
    ),
    (
        "How does the lesson describe the difference in emphasis between PostgreSQL and MySQL?",
        "PostgreSQL tends to support more advanced query features and stricter data validation out of the box, while MySQL has historically prioritized straightforward speed for common web workloads — neither is \"wrong\"; they simply optimized for slightly different priorities.",
        "medium", "understand", "choosing-a-database-system",
        "PostgreSQL emphasizes advanced features and stricter validation; MySQL emphasizes straightforward speed for web workloads",
        ["PostgreSQL is free while MySQL is a paid, commercial-only product", "MySQL supports SQL while PostgreSQL uses a completely different query language", "PostgreSQL cannot be used in production, only for learning"],
    ),
    (
        "SQLite is described as \"not a server you connect to at all.\"\n\nWhat is it instead, and what is its core limitation?",
        "SQLite is a library that stores an entire database inside a single file on disk, with no separate process to install or run. Its core limitation is that it's not built to have many people or programs writing to it at once over a network.",
        "medium", "apply", "choosing-a-database-system",
        "A library storing an entire database in one file, not built for many people writing to it at once over a network",
        ["A cloud-hosted server requiring a paid subscription to use at all", "A NoSQL document database with no relationship to SQL at all", "A full server process identical to PostgreSQL, just with a different name"],
    ),
    (
        "Why does SQLite's single-file simplicity ultimately not fit Ishaan's robotics club system, even though it's tempting for a first weekend of hacking?",
        "The system will be used by more than one officer at a time, and SQLite was never built for several people editing shared data at once, exactly the situation a shared club-membership system actually needs.",
        "medium", "apply", "choosing-a-database-system",
        "The club system needs several officers editing shared data at once, which SQLite wasn't built to support",
        ["SQLite cannot store text values, only numbers", "SQLite requires a paid license for any club or organization to use", "SQLite cannot store more than a handful of rows total"],
    ),
    (
        "What two specific needs of Ishaan's system push the decision toward a full server like PostgreSQL rather than SQLite?",
        "The system will be used by more than one officer at a time, and it needs to enforce that an attendance record cannot point to a member or event that does not exist — both needs that a shared, standards-compliant server handles and a single local file was never built for.",
        "hard", "analyze", "choosing-a-database-system",
        "Being used by more than one officer at once, and needing to enforce that attendance records reference real members and events",
        ["Needing the cheapest possible option, and needing the smallest possible file size", "Needing a NoSQL document structure, and needing graph-based relationships", "Needing to run entirely offline, and needing to avoid any installation at all"],
    ),
    (
        "What is the lesson's overall conclusion about how to choose a database system?",
        "Choosing a database system is not about finding one flawless option and discarding the rest — it is about matching a system's actual design to the shape of the problem in front of you.",
        "hard", "analyze", "choosing-a-database-system",
        "Match the system's actual design to the shape of the problem, rather than searching for one universally \"best\" option",
        ["Always choose whichever system is currently most popular on forums", "Always choose the newest database system released, regardless of the problem", "Always choose a NoSQL system, since relational systems are becoming obsolete"],
    ),
]

INSTALLING_POSTGRESQL = [
    (
        "Ananya wonders whether PostgreSQL is a program she opens each time, like a text editor, or something that runs in the background.\n\nWhat is the honest answer?",
        "PostgreSQL is a small, ongoing server process, a program that starts once, keeps running quietly in the background listening for connections, and stays available until stopped or the machine shuts down, rather than something opened and closed like a document.",
        "easy", "understand", "installing-postgresql",
        "It's an ongoing server process that starts once and keeps running in the background, unlike a document you open and close",
        ["It's a document-editing program you open fresh each time you need it", "It only runs for the duration of a single query and then shuts down", "It's a browser extension that requires no installation at all"],
    ),
    (
        "Regardless of operating system, what three things does a PostgreSQL install leave in place, according to the lesson?",
        "A running server process, a default administrative role, and a default network port the server listens on — the same handful of things underneath whatever wizard or command happened to drive the install.",
        "easy", "remember", "installing-postgresql",
        "A running server process, a default administrative role, and a default network port",
        ["A pre-built sample database, a licensing key, and a support contract", "A graphical editor, a web browser plugin, and a mobile app", "A backup schedule, a firewall rule, and a domain name"],
    ),
    (
        "What is the conventionally named default administrative role created by every fresh PostgreSQL install, and what capability does it have?",
        "The role is conventionally named \"postgres,\" and it has full administrative rights over the whole server — the account Ananya uses for her very first connection, the way a new laptop hands you one built-in administrator account before you create your own.",
        "medium", "remember", "installing-postgresql",
        "\"postgres,\" with full administrative rights over the whole server",
        ["\"admin,\" with read-only access to a single database", "\"root,\" with rights limited to the operating system, not the database", "\"guest,\" with no rights until manually upgraded"],
    ),
    (
        "What is PostgreSQL's conventional default network port, and what does a \"port\" actually mean in this context?",
        "Port 5432 is the convention. A port is simply the numbered \"door\" a program listens at for incoming connections, the same way a building might have several numbered entrances even though it is one structure.",
        "medium", "understand", "installing-postgresql",
        "Port 5432, the numbered \"door\" a program listens at for incoming connections",
        ["Port 80, the same port every web server uses by default", "Port 5432, which must be manually created by the administrator after install", "There is no default port; every install must choose a random one"],
    ),
    (
        "How does Ananya verify that her PostgreSQL install actually worked?",
        "By running psql --version or postgres --version from a terminal; seeing a version number printed back, rather than a \"command not found\" error, confirms the software is genuinely on the machine and the terminal knows where to find it.",
        "medium", "apply", "installing-postgresql",
        "Running psql --version or postgres --version and confirming a version number prints back",
        ["Restarting her computer and checking whether it boots faster", "Opening a random text file and checking whether it opens correctly", "Waiting 24 hours to see if the installer sends a confirmation email"],
    ),
    (
        "If the version-check command is not recognized after installing PostgreSQL, what does the lesson say is the usual culprit?",
        "The install's tools were most likely not added to the system's command search path during setup, a fixable configuration detail rather than a sign that anything is fundamentally broken.",
        "medium", "analyze", "installing-postgresql",
        "The install's tools weren't added to the system's command search path — a fixable configuration detail",
        ["The installer definitely failed and PostgreSQL was never actually installed", "The computer's hardware is incompatible with any database software", "PostgreSQL only supports being run from inside its own installer window"],
    ),
    (
        "What \"zero-install\" option does the lesson describe for someone who would rather not fight with installers on day one?",
        "A browser-based SQL environment, reachable through nothing more than a web page, gives an already-running database connection instantly, with no download, no password setup, and no port configuration to think about.",
        "medium", "apply", "installing-postgresql",
        "A browser-based SQL environment reachable through a web page, with no download or configuration needed",
        ["Asking a friend to run all queries on your behalf over a phone call", "Writing SQL commands on paper and mailing them to a data center", "There is no zero-install option; a local install is always required first"],
    ),
    (
        "What advice does the lesson give about treating a local PostgreSQL install as a \"prerequisite\" for getting started with SQL?",
        "It's worth doing eventually, but there's no need to treat it as a prerequisite — get comfortable typing queries and seeing real results first, in whichever environment is in front of you, and treat a local install as a milestone to reach once the basics no longer feel unfamiliar.",
        "hard", "analyze", "installing-postgresql",
        "It's not a prerequisite; get comfortable writing queries first and treat a local install as a milestone to reach later",
        ["A local install is mandatory before writing even a single query", "Local installs should be avoided entirely in favor of browser tools forever", "Installing PostgreSQL locally is only for professional database administrators"],
    ),
]

PSQL_PGADMIN = [
    (
        "Rehan watches one tutorial presenter type backslash commands into a terminal, and another click through a colourful tree of database and table icons.\n\nWhat are these two tools, and what do they fundamentally have in common?",
        "They are psql (a command-line client) and pgAdmin (a graphical client). Both are simply two different lenses for looking at and working with the same underlying PostgreSQL server; neither tool changes what the database actually stores.",
        "easy", "understand", "psql-and-pgadmin",
        "psql and pgAdmin — two different lenses onto the same underlying server, neither changing what's actually stored",
        ["Two entirely separate databases holding different data", "Two versions of PostgreSQL that are incompatible with each other", "A production tool and a testing-only tool that behave differently"],
    ),
    (
        "In a psql session, what do the meta-commands \\l and \\dt each do?",
        "\\l lists every database on the server. \\dt lists the tables inside whichever database is currently connected — two of psql's own shortcuts for common \"what exists here\" questions.",
        "easy", "remember", "psql-and-pgadmin",
        "\\l lists every database on the server; \\dt lists the tables in the currently connected database",
        ["\\l lists tables; \\dt lists databases — the reverse of the correct mapping", "\\l logs out of the session; \\dt deletes the current table", "\\l loads a saved query; \\dt displays the current date and time"],
    ),
    (
        "What does \\d students do in a psql session, and is it standard SQL?",
        "\\d students describes one specific table's columns and types. It is not SQL in the strict sense; it's one of psql's own meta-command shortcuts (starting with a backslash) for a question that would otherwise take a longer query to answer.",
        "medium", "understand", "psql-and-pgadmin",
        "It describes the students table's columns and types; it's a psql meta-command, not standard SQL",
        ["It deletes the students table; it is a standard SQL DROP command", "It duplicates the students table; it is standard SQL syntax", "It renames the students table; it works identically in every database system"],
    ),
    (
        "How does pgAdmin represent the same underlying structural information (which databases, schemas, and tables exist) that psql's meta-commands answer through typed commands?",
        "pgAdmin represents it as an expandable tree in a left-hand panel, much like a file browser's folder tree: clicking a database node reveals its schemas, clicking a schema reveals its tables, and clicking a table reveals its columns, without a single meta-command typed anywhere.",
        "medium", "apply", "psql-and-pgadmin",
        "As an expandable tree in a left-hand panel, similar to a file browser's folder structure",
        ["As a single flat list with no grouping of any kind", "By requiring the user to type the exact same backslash commands psql uses", "It doesn't represent this information at all; only psql can show table structure"],
    ),
    (
        "What trade-off does the lesson say a graphical tool like pgAdmin makes, compared to a command-line tool like psql?",
        "The trade is speed for visibility: where a psql user who already knows the shape of their database can type a short command in half a second, someone unfamiliar with what they're looking at often finds it faster to simply expand a tree and look.",
        "medium", "analyze", "psql-and-pgadmin",
        "Speed for visibility — pgAdmin trades typing speed for a clearer visual picture of unfamiliar structure",
        ["pgAdmin trades visibility for speed, being faster than psql in every situation", "There is no trade-off; both tools are identical in every respect", "pgAdmin trades reliability for convenience, often showing incorrect data"],
    ),
    (
        "After using both tools for a week, when does Rehan find psql the better choice?",
        "When he already knows exactly what he wants, a specific table's columns, a quick one-line query, whether a database exists, psql answers in the time it takes to type a short line — and that speed compounds further when writing scripts that run SQL commands unattended.",
        "medium", "apply", "psql-and-pgadmin",
        "When he already knows exactly what he wants, and especially for writing unattended scripts",
        ["Only when he is exploring a completely unfamiliar database for the first time", "Only when he needs a visual, point-and-click interface", "psql is never actually faster than pgAdmin for any task"],
    ),
    (
        "When does Rehan find pgAdmin the better choice?",
        "When exploring something unfamiliar, like a database a teammate built that he has never opened before, pgAdmin's tree lets him orient himself visually in a few clicks, seeing the whole shape of what exists before committing to typing anything specific.",
        "medium", "apply", "psql-and-pgadmin",
        "When exploring an unfamiliar database, letting him see the whole shape of what exists before typing anything",
        ["Only when running the exact same script repeatedly", "Only when working entirely offline with no network connection", "pgAdmin is never actually useful compared to psql"],
    ),
    (
        "Why does the lesson conclude that \"most people who work with databases regularly end up reaching for both\" tools, rather than settling on just one?",
        "psql rewards familiarity with speed for quick, repeated checks and automation, while pgAdmin rewards unfamiliarity with visibility for moments that call for a wider view — each tool suits a different kind of moment, not a different kind of person.",
        "hard", "analyze", "psql-and-pgadmin",
        "Each tool suits a different kind of moment (familiar/quick vs. unfamiliar/exploratory), not a different kind of person",
        ["Because using two tools is required by PostgreSQL's licensing terms", "Because psql and pgAdmin secretly connect to two different servers", "Because pgAdmin is strictly worse and psql is strictly better in every case"],
    ),
]

CREATING_DB_SCHEMA_TABLE = [
    (
        "Pooja asks: if a PostgreSQL server can hold many things at once, what exactly holds what?\n\nWhat is the clean, three-level nesting the lesson describes?",
        "A single running server can hold several databases; each database can hold several schemas; and each schema holds the actual tables where rows of real data finally live — server, then database, then schema, then table.",
        "easy", "remember", "creating-database-schema-table",
        "A server holds databases, each database holds schemas, and each schema holds tables",
        ["A table holds databases, each database holds schemas, and each schema holds a server", "A schema holds servers, each server holds databases, and each database holds tables", "A server holds tables directly, with no databases or schemas involved at all"],
    ),
    (
        "What does the statement CREATE DATABASE campus_training; actually do?",
        "It asks the server to set up an entirely new, independent storage area named campus_training, separate from any other database already on the server.",
        "easy", "understand", "creating-database-schema-table",
        "It creates an entirely new, independent storage area named campus_training on the server",
        ["It creates a new table named campus_training inside the current database", "It renames the current database to campus_training", "It deletes any database currently named campus_training"],
    ),
    (
        "Why is CREATE DATABASE illustrated in the lesson rather than run live inside a shared online SQL environment?",
        "A shared online SQL environment already hands you one connected database to work inside for the session, and cannot spin up or switch between separate physical databases the way your own local install can.",
        "medium", "understand", "creating-database-schema-table",
        "A shared online environment already provides one connected database and can't create or switch between separate physical databases",
        ["CREATE DATABASE is not valid SQL syntax in any environment", "Online environments do not support any SQL statements at all", "Creating a database is always instantaneous and needs no illustration"],
    ),
    (
        "In `CREATE TABLE campus.students (...)`, what does writing \"campus.students\" rather than just \"students\" actually accomplish?",
        "It places the table inside the campus schema instead of PostgreSQL's default, unlabelled location — the schema prefix is what actually nests the table where Pooja intends.",
        "medium", "apply", "creating-database-schema-table",
        "It places the table inside the campus schema instead of PostgreSQL's default location",
        ["It creates two separate tables, one named campus and one named students", "It has no effect; \"campus.students\" and \"students\" behave identically", "It marks the students table as the primary key of the campus schema"],
    ),
    (
        "What does `CREATE SCHEMA IF NOT EXISTS campus;` do, and specifically what does the \"IF NOT EXISTS\" guard prevent?",
        "It sets up the named grouping campus, giving both upcoming tables somewhere to live. The \"IF NOT EXISTS\" guard means rerunning this statement will not fail with an error if the schema is already there.",
        "medium", "apply", "creating-database-schema-table",
        "It creates the campus schema, and \"IF NOT EXISTS\" prevents an error if the schema already exists when rerun",
        ["It creates a table named \"IF NOT EXISTS\" inside the campus schema", "It deletes the campus schema if it already exists, then recreates it", "It has no functional effect and exists purely for documentation"],
    ),
    (
        "In Pooja's students table, Arjun Das's phone value is left as NULL.\n\nWhy is this valid, and what column property allows it?",
        "The phone column was defined without a NOT NULL requirement, so leaving it blank is valid, since not every student has necessarily shared a phone number.",
        "medium", "analyze", "creating-database-schema-table",
        "The phone column has no NOT NULL requirement, so leaving it blank is a valid, allowed state",
        ["It's invalid, and the INSERT statement should have failed with an error", "NULL is only allowed for the primary key column, never for any other column", "The phone column was declared as a boolean, which defaults to NULL"],
    ),
    (
        "What does the PRIMARY KEY marking on student_id in Pooja's CREATE TABLE statement actually guarantee?",
        "It marks the column that uniquely identifies each row, guaranteeing that no two rows will ever share the same value in that column.",
        "medium", "understand", "creating-database-schema-table",
        "It guarantees that no two rows in the table will ever share the same student_id value",
        ["It guarantees the column will always hold a positive number", "It guarantees the table can never have more than one row", "It guarantees the column's value will be visible to every other schema"],
    ),
    (
        "How does Pooja confirm that her tables were \"not just created but genuinely hold the data\" she inserted?",
        "By running SELECT * FROM campus.students; and SELECT * FROM campus.courses; and seeing the inserted rows come back correctly, exactly the same statements that built the structure now answered right back by a plain SELECT.",
        "medium", "apply", "creating-database-schema-table",
        "By running SELECT * on each table and confirming the inserted rows come back correctly",
        ["By reopening the installer and running its setup wizard a second time", "By checking the server's version number using psql --version", "By deleting and recreating both tables to confirm no errors occur"],
    ),
]

SYNTHESIS = [
    (
        "Ishaan chose PostgreSQL for his robotics club, Ananya installed it locally, Rehan learned both psql and pgAdmin, and Pooja built her first schema and tables.\n\nIn what order would a real project typically follow these four activities?",
        "Choose the right system for the problem (Ishaan) → get the server running, locally or via a browser environment (Ananya) → learn the client tools used to talk to it (Rehan) → create a database, schema, and tables to actually hold data (Pooja).",
        "medium", "analyze", "choosing-a-database-system",
        "Choose the system, then install/access it, then learn the client tools, then create the database, schema, and tables",
        ["Create the tables first, then choose a system, then install it, then learn the tools", "Learn the client tools first, then choose a system, then create tables, then install anything", "All four activities must happen simultaneously in a single step"],
    ),
    (
        "The default admin role (\"postgres\") and the default port (5432) both come from installing PostgreSQL.\n\nWhat shared underlying purpose do both of these serve?",
        "Both exist to get the background server process running reliably and to give a safe, well-known way to reach it — the role provides a way to manage the server, and the port provides the door client tools connect through.",
        "medium", "understand", "installing-postgresql",
        "Both support getting the ongoing server process running reliably and give a safe, well-known way to reach it",
        ["Both exist purely for billing and licensing purposes", "Both are optional settings with no real functional purpose", "Both are unrelated; the role manages users and the port manages disk space"],
    ),
    (
        "Rehan's \\dt meta-command in psql and Pooja's SELECT * FROM campus.students; both let someone check what's inside a database, but they answer genuinely different questions.\n\nWhat's the difference?",
        "\\dt lists which tables exist inside the currently connected database, a structural question. SELECT * FROM campus.students reads the actual row data stored inside one specific table, a content question.",
        "medium", "analyze", "psql-and-pgadmin",
        "\\dt answers a structural question (which tables exist); SELECT * answers a content question (what data is in one table)",
        ["Both commands answer exactly the same question in different syntax", "\\dt reads row data, while SELECT * lists which tables exist", "Neither command can be used to check what's inside a database"],
    ),
    (
        "Ishaan's club needing multiple officers connected at once is the exact scenario used to rule out SQLite. Which specific PostgreSQL install detail exists precisely to support multiple separate connections reaching the same running server?",
        "The default port (5432) is the numbered \"door\" that any client tool connects through — it's what lets multiple separate client connections, from different officers or different tools, all reach the same running server process concurrently.",
        "hard", "analyze", "installing-postgresql",
        "The default port (5432), the door that lets multiple separate client connections reach the same running server",
        ["The default administrative role, since only one person can ever use it at a time", "The CREATE DATABASE statement, since it must be re-run for every new connection", "The psql meta-commands, since only psql supports more than one connection"],
    ),
    (
        "If Pooja had created her students table simply as \"students\" instead of \"campus.students,\" what would be different, based on the schema-and-table nesting described in the lesson?",
        "The table would land in PostgreSQL's default, unlabelled location rather than inside the campus schema, breaking the intentional grouping Pooja was trying to build for her training institute project.",
        "medium", "apply", "creating-database-schema-table",
        "The table would end up in PostgreSQL's default location instead of inside the campus schema",
        ["Nothing would change; schema prefixes have no effect on where a table is created", "The CREATE TABLE statement would fail with an error and create nothing", "The table would automatically be created inside every schema on the server"],
    ),
    (
        "Ananya's zero-install browser-based SQL environment and Rehan's choice between psql and pgAdmin both ultimately point toward the same underlying resource.\n\nWhat is that resource?",
        "An actual running PostgreSQL server. Whether reached through a local install, a browser-based environment, or a graphical or command-line client, all roads lead to the same database server holding the same schemas and tables.",
        "medium", "understand", "psql-and-pgadmin",
        "An actual running PostgreSQL server, reachable through any of these different doors",
        ["Two completely separate and unrelated database products", "A single shared spreadsheet file that all tools edit directly", "A licensing server that must approve every query before it runs"],
    ),
    (
        "Why does the \"installing PostgreSQL\" lesson insist on verifying the install with a version check rather than simply assuming the installer wizard finished successfully?",
        "Confirming the install actually took hold, rather than silently assuming it worked, catches problems like tools missing from the command search path before they cause confusing failures later, when Pooja or Ananya actually try to connect and run real SQL.",
        "hard", "analyze", "installing-postgresql",
        "It catches configuration problems (like a missing command search path) early, before they cause confusing failures later",
        ["Version checks are purely a formality with no real diagnostic value", "The installer wizard is always unreliable and fails silently most of the time", "A version check is required by PostgreSQL's software license before first use"],
    ),
    (
        "PostgreSQL's identity as a full standards-compliant server (from choosing a database system) and its identity as an ongoing background server process (from installing PostgreSQL) are two separate facts about the same software.\n\nHow do these two facts together explain why Pooja's campus_training database stays available across separate sessions?",
        "Because PostgreSQL runs as a persistent background server process rather than something opened and closed like a document, any database created inside it, like campus_training, persists and remains reachable across separate client connections, exactly the durability expected of a real, standards-compliant server.",
        "hard", "analyze", "choosing-a-database-system",
        "Because PostgreSQL runs persistently in the background, databases created inside it remain available across separate client sessions",
        ["Because campus_training is automatically backed up to the cloud every second", "Because Pooja must manually restart the server before every connection", "Because standards-compliant servers delete all data at the end of each session"],
    ),
]

SET1_SOURCES = [
    (CHOOSING_DB_SYSTEM, 0),
    (INSTALLING_POSTGRESQL, 0),
    (PSQL_PGADMIN, 0),
    (CREATING_DB_SCHEMA_TABLE, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS[:6])

SET2 = (
    CHOOSING_DB_SYSTEM[1:]
    + INSTALLING_POSTGRESQL[1:]
    + PSQL_PGADMIN[1:]
    + CREATING_DB_SCHEMA_TABLE[1:]
    + SYNTHESIS[6:]
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
            "topics": "sql-essentials",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 3.1.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 3.1.2")
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
ws.title = "DBMS - MCQ - Unit 3.1"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 3 - SQL Essentials/3.1 - Setting Up Your Environment - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
