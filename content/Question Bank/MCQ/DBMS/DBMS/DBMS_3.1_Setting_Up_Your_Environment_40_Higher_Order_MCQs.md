# DBMS 3.1: Setting Up Your Environment — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** SQL Essentials
- **Chapter:** Setting Up Your Environment
- **Scope:** All four Topic 3.1 subtopics in the attached course blueprint (Choosing a Database System; Installing PostgreSQL; The psql CLI and pgAdmin; Creating Your First Database, Schema, and Table)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every scenario defines the database task, environment, and relevant objects before asking for a judgment. Evidence tables, terminal output, SQL fragments, and setup-state records are used whenever they make the reasoning visible.
- **Scope guard:** Questions use only concepts taught in Topic 3.1. Context establishes the environment but requires no outside operating-system or administration knowledge.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all four Topic 3.1 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. A database that travels inside the app

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Choosing a Database System  
**Is Curriculum Based:** No  
**Assessment type:** System-selection judgment

A meditation app has this storage profile:

| Requirement | Value |
|---|---|
| Storage location | On the phone |
| Network dependency | None |
| Users per database | One |
| Separate server process | Not wanted |

Approve the relational system whose deployment model matches all four requirements.

A. PostgreSQL, running as a service on every phone.  
B. MySQL, with each phone dialing a shared server.  
C. SQLite — an embedded, file-based engine, no server at all.  
D. A spreadsheet synced over email manually each and every week.

### 2. The defaults every tutorial assumes

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Installing PostgreSQL  
**Is Curriculum Based:** No  
**Assessment type:** Default-configuration recall

A new developer sees two empty fields after a standard PostgreSQL installation:

| Connection field | Required value |
|---|---|
| Administrative role | Default created by PostgreSQL |
| Port | Default PostgreSQL listening port |

Fill both connection fields with PostgreSQL's standard defaults.

A. Role `admin`, port 8080  
B. Role `postgres`, port 5432 — the defaults.  
C. Role `root`, port 3306  
D. Role `sa`, port 1433, a different system entirely.

### 3. One shell, no desktop

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The psql CLI and pgAdmin  
**Is Curriculum Based:** No  
**Assessment type:** Tool-selection judgment

An engineer's working environment is:

| Property | Available? |
|---|---|
| SSH text terminal | Yes |
| Graphical desktop | No |
| PostgreSQL connection | Yes |
| Task | Run one quick query |

Select the client that works within the shown environment.

A. pgAdmin, after installing a desktop environment on the server.  
B. Neither tool works without a mouse.  
C. Waiting until physically back at the office workstation tomorrow.  
D. psql — the command-line client runs in text-only sessions.

### 4. Write the table into existence

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** DDL-syntax selection

A cycling club needs a members table with an integer ID as primary key, a name, and a join date.

Approve the statement that creates every requested column with a suitable type.

A. `CREATE TABLE members (member_id INTEGER PRIMARY KEY, full_name TEXT, joined_on DATE);`  
B. `MAKE TABLE members WITH member_id, full_name, joined_on;`, using an English-style table declaration.  
C. `CREATE members (member_id, full_name, joined_on);`  
D. `TABLE NEW members: member_id INTEGER; full_name TEXT;`

### 5. Why the club system points at PostgreSQL

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Choosing a Database System  
**Is Curriculum Based:** No  
**Assessment type:** Evidence-based selection

A sports club documents its database needs:

| Need | Required |
|---|---|
| Concurrent staff connections | Yes |
| Strict integrity rules | Yes |
| Long-term feature growth | Yes |
| Licence fee | ₹0 |

Complete the recommendation using only evidence relevant to the requirements.

A. It is the only relational database capable of storing multilingual text and enforcing any membership rule.  
B. It requires no installation of any kind.  
C. It is the smallest download of the three options.  
D. It is a free, open-source, full-featured server built for many connections.

### 6. Seeing instead of typing

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The psql CLI and pgAdmin  
**Is Curriculum Based:** No  
**Assessment type:** Tool-strength identification

An analyst has never seen a teammate's database:

| Goal | Preference |
|---|---|
| Discover databases, schemas, tables, and columns | Browse visually |
| Memorize meta-commands first | No |
| Modify the underlying structure merely by browsing | No |

Choose the pgAdmin capability that directly satisfies the analyst's preference.

A. A faster network connection and lower server latency created by the graphical interface.  
B. Automatic documentation emailed as PDF.  
C. A visual browser tree of databases, schemas, tables, and columns.  
D. Nothing; pgAdmin is only for backups.

### 7. What the installer actually left behind

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Installing PostgreSQL  
**Is Curriculum Based:** No  
**Assessment type:** Install-outcome identification

A designer records the result of installation:

| Observation | Status |
|---|---|
| PostgreSQL files installed | Yes |
| Background process configured | Yes |
| Desktop window opened automatically | No |

Interpret the absence of a window and identify what was installed.

A. A background service listening on its port, plus role and tools.  
B. A game-like desktop application with a colorful animated start screen.  
C. Only documentation files.  
D. A browser extension.

### 8. Big box, middle box, small box

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** Hierarchy sequencing

A trekking company needs these nested objects:

| Object | Intended contents |
|---|---|
| Database | The project's independent storage area |
| Schema | Related booking tables |
| Tables | Booking rows and columns |

Arrange the creation sequence so every parent exists before its child.

A. Table first, then wrap a schema around it, then finally a database.  
B. Database first, then schema, then tables inside the schema.  
C. All three in one statement, in any order.  
D. Schema first; databases are optional.

### 9. Three cousins, one family

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Choosing a Database System  
**Is Curriculum Based:** No  
**Assessment type:** Comparison discrimination

A hiring exercise supplies these observations:

| System | Relational? | Deployment |
|---|---|---|
| PostgreSQL | Yes | Server |
| MySQL | Yes | Server |
| SQLite | Yes | Embedded file |

Retain the comparison that respects both their shared family and their differences.

A. Only PostgreSQL is relational; the other two are document stores.  
B. They share no relational ideas or SQL concepts, so learning one provides no transferable knowledge.  
C. SQLite is the most feature-rich server of the three.  
D. All three are relational and speak SQL, but deployment and feature emphasis differ.

### 10. The line under the rows

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The psql CLI and pgAdmin  
**Is Curriculum Based:** No  
**Assessment type:** Output reading

In psql, a query on a kayak-rental database prints:

```
 kayak_id | colour
----------+--------
        1 | red
        2 | yellow
        3 | red
(3 rows)
```

Interpret the footer without making a claim about the table's capacity.

A. The result set contains exactly three rows returned.  
B. The table has a permanent capacity of exactly three rows.  
C. Three queries have run this session.  
D. The connection will close in three seconds.

### 11. Two hundred clerks, one file?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Choosing a Database System  
**Is Curriculum Based:** No  
**Assessment type:** Limitation reasoning

A ticketing platform compares its prototype with production:

| Environment | Writers | Access pattern |
|---|---:|---|
| Prototype | 1 developer | Local file |
| Production | Hundreds | Simultaneous network bookings |

An engineer proposes keeping SQLite because the prototype succeeded.

Diagnose the workload mismatch exposed by the production profile.

A. SQLite cannot store dates.  
B. SQLite is not designed for hundreds of concurrent network writers.  
C. SQLite's SQL dialect has no SELECT statement.  
D. There is no mismatch because every relational system suits every workload equally.

### 12. Prove it works

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Installing PostgreSQL  
**Is Curriculum Based:** No  
**Assessment type:** Verification-step selection

A bootcamp learner has completed installation and opens a terminal:

| Check | Desired evidence |
|---|---|
| PostgreSQL client installed and discoverable | A version number printed by the command |

Choose the check that produces direct installation evidence.

A. Restart the computer and assume success.  
B. Confirm that the original installer file remains in the downloads folder.  
C. Run `psql --version` and confirm that a PostgreSQL version is printed.  
D. Reinstall a second time to be sure.

### 13. What typing into psql looks like

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The psql CLI and pgAdmin  
**Is Curriculum Based:** No  
**Assessment type:** Interaction-model identification

A bootcamp learner sees this interaction surface:

| Tool | Visible interface |
|---|---|
| psql | Text prompt awaiting typed input |

Complete the interaction description for the text prompt.

A. Queries are created only by dragging graphical blocks onto a canvas and clicking a Run button.  
B. psql records the screen and replays it later.  
C. Only administrators may type; others watch.  
D. You type SQL, end with a semicolon, press Enter, results print below.

### 14. A folder named for the faculty

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** DDL-syntax selection

A music academy wants a schema to group its tables, then a courses table inside it.

Approve the DDL pair that places the table inside the requested schema.

A. `CREATE SCHEMA academy;` then `CREATE TABLE academy.courses (course_id INTEGER PRIMARY KEY, title TEXT);`  
B. `CREATE FOLDER academy;` followed by `CREATE academy/courses WITH course_id INTEGER AND title TEXT;`, using filesystem-style nesting.  
C. `SCHEMA academy CREATE;` followed by `TABLE courses CREATE;`  
D. `CREATE TABLE courses IN SCHEMA academy WITHOUT COLUMNS;`

### 15. Why learning one teaches three

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Choosing a Database System  
**Is Curriculum Based:** No  
**Assessment type:** Transferability reasoning

A learner compares the course with a possible first job:

| Environment | Product | Core data model/language |
|---|---|---|
| Course | PostgreSQL | Relational tables and SQL |
| Possible job | MySQL or SQLite | Relational tables and SQL |

Select the shared foundation that makes much of the learning transferable.

A. All jobs use PostgreSQL exclusively.  
B. The three systems never appear in industry.  
C. All three belong to the relational family and speak SQL.  
D. SQL knowledge cannot transfer between different relational products.

### 16. Start now, install nothing

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Installing PostgreSQL  
**Is Curriculum Based:** No  
**Assessment type:** Alternative-path identification

A learner's environment has these constraints:

| Resource | Available? |
|---|---|
| Permission to install software | No |
| Web browser | Yes |
| Internet access | Yes |
| Goal | Run real SQL today |

Choose the route that satisfies every listed constraint today.

A. Writing SQL in a text file and imagining the results.  
B. A browser-based SQL environment running queries server-side.  
C. Borrowing a stranger's laptop.  
D. PostgreSQL must be installed locally before any SQL statement can run.

### 17. Two tasks, two doors

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The psql CLI and pgAdmin  
**Is Curriculum Based:** No  
**Assessment type:** Task-to-tool matching

Two tasks at a fisheries department:

| Task | Important requirement |
|---:|---|
| 1 | Replay a fixed weekly load unattended at 06:00 |
| 2 | Show an auditor the database hierarchy on a projector |

Assign one tool to each task.

A. pgAdmin for both because every scheduled task requires a graphical window.  
B. psql for both — text is always better.  
C. pgAdmin for task 1; psql for task 2.  
D. psql for task 1; pgAdmin's visual tree for task 2.

### 18. Why the database didn't create itself

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** Practice-rationale reasoning

A junior developer checks the setup state:

| Object | Present after installation? |
|---|---|
| PostgreSQL server and default administrative role | Yes |
| Project-specific database `bakery_db` | No |

Complete the setup diagnosis: the missing project database is ______.

A. The installer forgot; reinstalling fixes it.  
B. Databases appear when the first query runs.  
C. Creating a project database is a deliberate manual step.  
D. A project database can only be created by the PostgreSQL vendor.

### 19. One statement, one database

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** DDL-syntax selection

A pet-grooming startup needs a database named `groomly_db`.

Fill the one-statement setup step with valid PostgreSQL syntax.

A. `CREATE DATABASE groomly_db;`  
B. `NEW DATABASE groomly_db();` — invalid syntax entirely.  
C. `DATABASE ADD groomly_db;`  
D. `MAKE groomly_db AS DATABASE;`

### 20. Nothing is listening

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Installing PostgreSQL  
**Is Curriculum Based:** No  
**Assessment type:** Connection-failure diagnosis

A developer records a connection incident:

| Check | Result |
|---|---|
| Host | `localhost` |
| Port | `5432` |
| Previous-day test | Successful |
| After reboot | `connection refused` |

Choose the first component the developer should investigate.

A. The database was deleted by the reboot.  
B. The PostgreSQL server service is not running on this machine.  
C. Port 5432 ceases to exist after reboot and must be recreated manually before each connection.  
D. psql uninstalled itself.

### 21. What psql is, in one sentence

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The psql CLI and pgAdmin  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

A trainee separates the PostgreSQL components:

| Component | Role |
|---|---|
| PostgreSQL server | Stores data and answers requests |
| Unknown component | Text-based tool used to send SQL |

Choose the description that correctly fills the unknown component as psql.

A. The PostgreSQL server itself.  
B. A spreadsheet application bundled with PostgreSQL for editing database files without a server.  
C. A graphical dashboard for charts.  
D. PostgreSQL's command-line client, sending SQL and printing results.

### 22. Types for the first table

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** Column-type selection

A dance institute specifies four course fields:

| Field | Meaning |
|---|---|
| `course_id` | Whole-number primary key |
| `title` | Course name |
| `monthly_fee` | Exact rupees and paise |
| `starts_on` | Calendar date |

Complete all four definitions without dropping a requested field.

A. All four columns as `TEXT` for simplicity.  
B. `course_id TEXT PRIMARY KEY, title DATE, monthly_fee BOOLEAN, starts_on INTEGER`, treating all values as labels.  
C. `course_id INTEGER PRIMARY KEY, title TEXT, monthly_fee NUMERIC(8,2), starts_on DATE`.  
D. One combined column holding all four values with commas.

### 23. Where the little engine wins

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Choosing a Database System  
**Is Curriculum Based:** No  
**Assessment type:** Fit-inversion judgment

A team compares a failed production fit with a new candidate:

| Workload | Users/writers | Storage shape |
|---|---|---|
| Busy booking platform | Many concurrent | Shared server needed |
| Candidate desktop tracker | One user | One portable local file |

They conclude that SQLite is never appropriate merely because it failed the first workload.

Select the counterexample that fits SQLite's intended shape.

A. A stock exchange's matching engine with thousands of concurrent writers today.  
B. A single-user desktop tracker needing its database in one portable file.  
C. A bank's shared central ledger.  
D. A multi-region online game backend.

### 24. The first key to the building

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Installing PostgreSQL  
**Is Curriculum Based:** No  
**Assessment type:** Role-purpose identification

Immediately after installation, the connection record shows:

| Role | Created when | Initial privilege |
|---|---|---|
| `postgres` | During setup | Full server administration |

Classify the `postgres` role from the installation evidence.

A. The default administrative superuser created at install.  
B. A read-only guest login.  
C. A sample customer account with demo data preloaded already.  
D. A role that expires after 30 days.

### 25. One server, two windows

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The psql CLI and pgAdmin  
**Is Curriculum Based:** No  
**Assessment type:** Mental-model verification

A developer records two observations:

| Client | Observation |
|---|---|
| psql | `CREATE TABLE inventory.items (...)` succeeds |
| pgAdmin | `inventory.items` immediately appears in its tree |

Complete the developer's mental model of where the table actually lives.

A. pgAdmin copied the table from psql's memory.  
B. A lucky coincidence of names.  
C. The two tools duplicate every object through a shared configuration file.  
D. Both tools are clients of the same server, two doors, one database.

### 26. Boxes inside boxes

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** Hierarchy identification

A florist's object map is:

| Level | Name |
|---|---|
| Database | `bloom_db` |
| Schema | `shopfront` |
| Table | `bouquets` |

Read the object map from outer container to inner object.

A. The table contains `shopfront`, and that schema contains `bloom_db` as its innermost object.  
B. The database `bloom_db` contains schema `shopfront`, holding table `bouquets`.  
C. All three names refer to the same object.  
D. Schemas and databases are unrelated to tables.

### 27. What CREATE TABLE cannot do without

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** Requirement identification

A trainee's checklist contains:

| Required concept | Missing detail |
|---|---|
| Object identity | ? |
| Row structure | ? |

Fill both missing checklist details.

A. At least one index and one trigger must appear in the statement.  
B. The server's port number must be declared inside every table.  
C. A table name, and its columns each with a data type.  
D. The first ten rows of sample data.

### 28. Three errors, one statement

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** DDL debugging

A volunteer types this for an animal shelter and gets a syntax error:

```sql
CREATE TABLE adoptions (
    adoption_id INTEGER PRIMARY KEY
    animal_name TEXT,
    adopted_on
);
```

Select the smallest repair that addresses every shown syntax defect.

A. Add a comma after `PRIMARY KEY` and type `adopted_on` as `DATE`.  
B. Remove all commas; they are optional.  
C. Change CREATE TABLE to CREATE DATABASE.  
D. Wrap the complete statement in quotation marks before running it.

### 29. The semicolon that finishes the sentence

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The psql CLI and pgAdmin  
**Is Curriculum Based:** No  
**Assessment type:** Interaction-mechanics diagnosis

In psql, a learner types `SELECT * FROM boats` and presses Enter — nothing happens except the prompt changing slightly, as if psql is waiting.

Diagnose the changed prompt before altering the query.

A. The server has crashed.  
B. psql is waiting for the semicolon to finish the statement.  
C. The table is too large to display.  
D. psql waits because the `boats` table may be queried only after the current weekday ends.

### 30. The table that landed in the wrong folder

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** Qualification-consequence reasoning

A developer compares intention with outcome:

| Item | Value |
|---|---|
| Intended table | `stockroom.supplies` |
| Executed name | `supplies` |
| Result | Table exists, but `stockroom` does not contain it |

Record where PostgreSQL placed the unqualified table.

A. The statement failed silently, created no table, and discarded the entire `stockroom` schema.  
B. The table was created in every schema at once.  
C. The database renamed itself to stockroom.  
D. The unqualified name went to the default schema, not `stockroom`.

### 31. Match the systems to their one-liners

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Choosing a Database System  
**Is Curriculum Based:** No  
**Assessment type:** Description matching

Three one-line descriptions:

| Description | Characteristic |
|---:|---|
| 1 | Embedded engine; entire database in one local file |
| 2 | Popular open-source server; long a web-stack staple |
| 3 | Feature-deep, standards-strict open-source server used by this course |

Match all three descriptions to their systems.

A. 1: PostgreSQL, 2: SQLite, 3: MySQL  
B. 1: MySQL, 2: PostgreSQL, 3: SQLite  
C. 1: SQLite, 2: MySQL, 3: PostgreSQL  
D. All three describe MySQL

### 32. Knocking on the wrong door number

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Installing PostgreSQL  
**Is Curriculum Based:** No  
**Assessment type:** Configuration-mismatch diagnosis

A connection review shows:

| Item | Value |
|---|---:|
| PostgreSQL listening port | 5432 |
| Copied application configuration | 3306 |
| Server status | Running |

Trace the failed connection to the mismatched configuration value.

A. The app is knocking on 3306 while PostgreSQL listens on 5432.  
B. PostgreSQL accepts connections only from its own command-line client.  
C. The server must be reinstalled on port 3306.  
D. Ports are decorative and cannot cause failures.

### 33. Save the keystrokes, keep the power

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The psql CLI and pgAdmin  
**Is Curriculum Based:** No  
**Assessment type:** Capability reasoning

A data engineer's workflow is:

| Asset | Use |
|---|---|
| `weekly_load.sql` | Twelve statements saved in a fixed order |
| psql | Replays the file every Monday |

Identify the CLI property demonstrated by this weekly workflow.

A. psql converts every SQL script into a spreadsheet before execution and imports the resulting cells.  
B. Text commands are repeatable: typed once, saved, and replayed exactly.  
C. pgAdmin cannot open files of any kind.  
D. The file format is secret to psql.

### 34. The institute, in order

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** Script sequencing

A coaching institute needs this hierarchy:

| Parent | Child |
|---|---|
| PostgreSQL server | Database `institute_db` |
| `institute_db` | Schema `academy` |
| `academy` | Table `batches` |

Approve the sequence that creates each container in the correct connected context.

A. `CREATE TABLE academy.batches (...); CREATE SCHEMA academy; CREATE DATABASE institute_db;`  
B. `CREATE SCHEMA academy; CREATE DATABASE institute_db;` then connect and `CREATE TABLE batches (batch_id INTEGER PRIMARY KEY);`, leaving the schema in the previous database.  
C. All three statements merged into one line with AND.  
D. `CREATE DATABASE institute_db;` then `\c institute_db`, `CREATE SCHEMA academy;`, and `CREATE TABLE academy.batches (batch_id INTEGER PRIMARY KEY);`

### 35. What the schema contributes here

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** Purpose identification

A trekking database groups:

| Schema | Tables |
|---|---|
| `expeditions` | `bookings`, `guides`, `routes` |

Complete the design note describing the schema's contribution.

A. Faster disk writes for every table stored inside the schema.  
B. Automatic nightly backups.  
C. A named grouping of related tables under `expeditions.*`.  
D. Encryption of the guides' personal data.

### 36. Fair statements about the two doors

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** The psql CLI and pgAdmin  
**Is Curriculum Based:** No  
**Assessment type:** Comparison verification

A team records these two access paths to the same PostgreSQL server:

| Tool | Interface |
|---|---|
| psql | Typed terminal commands |
| pgAdmin | Graphical tree, editor, and result grid |

Select the comparison that remains accurate despite the different interfaces.

A. pgAdmin can display database objects and rows but cannot submit SQL or structural changes to the server.  
B. Both are full-powered clients of the same server, just different styles.  
C. psql can only run SELECT statements.  
D. Using both on one database corrupts it.

### 37. The moment after Enter

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** Outcome identification

A florist's setup log shows:

| Statement | Server response |
|---|---|
| `CREATE TABLE bouquets (bouquet_id INTEGER PRIMARY KEY, style TEXT, price NUMERIC(6,2));` | Success |
| `INSERT INTO bouquets ...` | Not run |

Record the database state immediately after the successful DDL.

A. An empty table: structure defined, ready for its first rows.  
B. A table pre-filled with sample bouquets.  
C. Nothing at all until the first INSERT eventually creates the table.  
D. A backup file on the desktop.

### 38. The toy that isn't a toy

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Choosing a Database System  
**Is Curriculum Based:** No  
**Assessment type:** Nuanced-judgment selection

A design review compares two claims:

| Engineer | Claim |
|---|---|
| 1 | “SQLite is merely a toy.” |
| 2 | “PostgreSQL is overkill for every small project.” |

Reject the caricatures and choose the workload-based assessment.

A. The first engineer is right; embedded databases are toys.  
B. PostgreSQL is unsuitable for every application with a small initial dataset.  
C. Both are right, so no database should be used.  
D. Both are caricatures: each system is professional-grade in its own shape.

### 39. "Server" without a screen

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Installing PostgreSQL  
**Is Curriculum Based:** No  
**Assessment type:** Concept clarification

A trainee observes:

| PostgreSQL behavior | Observation |
|---|---|
| Process | Runs in the background |
| Client connections | Accepted on a listening port |
| Required visible window | None |

Interpret “server” using the observed process behavior.

A. A dedicated monitor that must remain powered on beside the computer.  
B. A window that must stay open all day.  
C. A background service running with no window, listening on its port.  
D. The physical building where databases live.

### 40. The whole setup, start to finish

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** SQL Essentials  
**Subtopic:** Creating Your First Database, Schema, and Table  
**Is Curriculum Based:** No  
**Assessment type:** Integrated script selection

A robotics academy specifies:

| Level/field | Required value |
|---|---|
| Database | `academy_db` |
| Schema | `training` |
| Table | `workshops` |
| Columns | Integer primary key, text title, exact fee |

Approve the workflow that creates the full hierarchy and every required field.

A. `CREATE DATABASE academy_db;`, reconnect to it, create schema `training`, then create `training.workshops` with the required typed columns.  
B. `CREATE training.workshops IN academy_db WITH KEYS;`  
C. `CREATE SCHEMA academy_db; CREATE DATABASE training; CREATE workshops;`  
D. `CREATE TABLE workshops(title TEXT, fee NUMERIC);`, then create `training`, then create `academy_db`, leaving the table in the original database.

---

## Instructor Key

### 1. C

No server, no network, one local user: the embedded shape. SQLite lives as a file inside the application — installing a server on every phone (A) inverts the design.

### 2. B

PostgreSQL's install creates the administrative role `postgres` and listens on port 5432 by default. Options C and D belong to other database systems' defaults — a distinction that matters the first time a connection string fails.

### 3. D

psql is a text program that runs happily inside an SSH session. That portability — any terminal, anywhere — is exactly its advantage over a graphical tool in a no-desktop environment.

### 4. A

`CREATE TABLE` takes a name and a parenthesized, comma-separated list of typed columns. Option A includes all three requested fields, gives `joined_on` a real `DATE` type, and marks the integer identifier as the primary key.

### 5. D

The requirements line up with the server profile: concurrent staff (server architecture), strict constraints (enforcement depth), years of growth (feature richness), zero cost (open source). Each need maps to a reason; none of the other options states one.

### 6. C

pgAdmin's defining strength is visibility: the clickable tree presents databases, schemas, tables, and columns as structure to look at, replacing exploratory typing for someone learning a new database's layout.

### 7. A

A database install produces a service, not an application window: a background server on its port, an admin role to connect as, and client tools. "Nothing opened" is the correct experience.

### 8. B

Containers precede contents: the database exists first, the schema is created inside it, the tables inside the schema. Each CREATE presumes its parent already exists.

### 9. D

All three are SQL-speaking relational systems. Their shared model makes knowledge transferable, while their deployment shape, validation behavior, and feature emphasis still differ; SQLite is embedded, whereas PostgreSQL and MySQL are servers.

### 10. A

psql closes every result with a row count. `(3 rows)` is a statement about this result set — three rows came back — not about the table, the session, or the connection.

### 11. B

The prototype hid the mismatch: one developer and one local file. Production introduces hundreds of simultaneous network writers, a workload for which the chapter recommends a server database rather than SQLite's embedded design.

### 12. C

The reading's direct post-install check is `psql --version` (or `postgres --version`). A printed version confirms that the tool is installed and discoverable on the command path; a “command not found” response points to installation or path configuration.

### 13. D

psql is conversational text: statement in, semicolon to finish, result printed below. No canvas, no recording, no privileged typists.

### 14. A

`CREATE SCHEMA academy;` makes the group; the qualified name `academy.courses` then places the table inside it. The qualification in the CREATE TABLE is what connects the two statements.

### 15. C

The systems share the relational core the course actually teaches — tables, keys, constraints, SQL. Moving between them is a change of accent, not of language.

### 16. B

The chapter's zero-install route is the browser: an online PostgreSQL environment runs queries on someone else's server, making practice possible on any machine with a browser — locked-down laptops included.

### 17. D

Task 1 is unattended repetition, the natural territory of a saved psql script. Task 2 needs the database hierarchy to be visible to an audience, which matches pgAdmin's browsable tree. Option D assigns both tools.

### 18. C

The install delivers the machinery; populating it with databases is deliberate developer action. The gap between "server exists" and "my database exists" is crossed by an explicit CREATE DATABASE — by design, not by omission.

### 19. A

`CREATE DATABASE groomly_db;` is the complete PostgreSQL statement for this step: the command, the requested database name, and the terminating semicolon. The other options use invented syntax.

### 20. B

"Connection refused" with a correct address usually means no listener: the server service didn't start after the reboot. The data and the port are fine; the process that answers is simply not running.

### 21. D

psql is the client, not the server (A) — a text program that carries your SQL to the server and the server's answer back to your screen.

### 22. C

Each requested fact receives its matching type: integer identity, text title, exact `NUMERIC` money, and a `DATE` start. Option C is the only definition that includes and correctly types all four columns.

### 23. B

The team over-generalized from one mismatch. The desktop tracker is SQLite's native habitat: one user, one file, no server to administer. Fit runs in both directions.

### 24. A

`postgres` is the install's founding identity: the superuser through which the first databases, roles, and permissions are created. It is the key handed over at move-in.

### 25. D

Client-server architecture in one demonstration: the table lives on the server, and both tools are windows onto that one server. Neither tool holds data; both view the same truth.

### 26. B

The nesting reads database → schema → table, and the qualified name `shopfront.bouquets` spells the path. Option A inverts the containment.

### 27. C

The minimum is structure: a name, and columns with types. Indexes, triggers, and rows all come later; the port (B) belongs to connections, not tables.

### 28. A

Two defects: a missing comma between the first and second column definitions, and a column (`adopted_on`) with no data type. Column definitions are comma-separated and each requires a type — both rules must be satisfied.

### 29. B

An Enter without a semicolon continues the statement; psql's changed prompt is it saying "still listening." The semicolon is the full stop that sends the sentence to the server.

### 30. D

Unqualified names land in the default schema. The table exists, works, and is simply in the wrong folder — the qualified name is the addressing that puts it where intended.

### 31. C

The embedded single-file description maps to SQLite, the popular open-source web server maps to MySQL, and the feature-deep, standards-strict server selected by the course maps to PostgreSQL.

### 32. A

3306 is another system's default port; PostgreSQL's is 5432. The copied config aims the client at a door nobody is behind — a one-line fix once the mismatch is seen.

### 33. B

Scriptability is a natural CLI strength: typed statements can be saved in a file and replayed in the same order without re-entering twelve commands every Monday.

### 34. D

Each container is created before its contents: create the database, reconnect into it with `\c institute_db`, create the schema, and then create the qualified table. The reconnect is essential because schemas belong to the currently connected database.

### 35. C

The schema is the named folder: the trekking tables live together, addressable as `expeditions.*`, insulated from name collisions with other teams' work. Speed (A) and encryption (D) are not what folders do.

### 36. B

Both are clients with full access to the same server; the differences are ergonomics, not capability. Choosing between them is task-fit — portability and scripts versus visual structure.

### 37. A

DDL creates structure, not content: the table now exists with its columns, types, and key on record, holding zero rows. Option C reverses the roles of CREATE and INSERT.

### 38. D

The chapter's comparison is about deployment shape, not rank. Each engine is serious within its shape — embedded versus shared server — and the review's job is matching shape to need, not awarding prestige.

### 39. C

A server is a listening background process. No window is normal: the evidence of life is that clients can connect, not that anything appears on screen.

### 40. A

Option A performs the full workflow: create `academy_db`, reconnect into it, create `training`, and define `training.workshops` with the required integer key, title, and fee. Every other option breaks the nesting, order, or syntax.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| System-selection and fit judgment | 1, 5, 9, 11, 15, 23, 31, 38 |
| Install outcomes, defaults, and diagnosis | 2, 7, 12, 16, 20, 24, 32, 39 |
| Tool choice and interaction mechanics | 3, 6, 10, 13, 17, 21, 25, 29, 33, 36 |
| DDL syntax, sequencing, and debugging | 4, 8, 14, 19, 22, 26, 27, 28, 30, 34, 35, 37, 40 |
| Practice rationale | 18 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| Choosing a Database System | 1, 5, 9, 11, 15, 23, 31, 38 | 8 |
| Installing PostgreSQL | 2, 7, 12, 16, 20, 24, 32, 39 | 8 |
| The psql CLI and pgAdmin | 3, 6, 10, 13, 17, 21, 25, 29, 33, 36 | 10 |
| Creating Your First Database, Schema, and Table | 4, 8, 14, 18, 19, 22, 26, 27, 28, 30, 34, 35, 37, 40 | 14 |

Questions 1–10 collectively cover all four Topic 3.1 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 11 questions (2, 10, 12, 16, 19, 21, 23, 24, 26, 27, 35)
- Intermediate: 28 questions
- Advanced: 1 question (40)
- Correct option A: 10 questions (4, 7, 10, 14, 19, 24, 28, 32, 37, 40)
- Correct option B: 10 questions (2, 8, 11, 16, 20, 23, 26, 29, 33, 36)
- Correct option C: 10 questions (1, 6, 12, 15, 18, 22, 27, 31, 35, 39)
- Correct option D: 10 questions (3, 5, 9, 13, 17, 21, 25, 30, 34, 38)
- Longest consecutive run of one correct letter: below 3 throughout
