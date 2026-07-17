import random
import openpyxl

random.seed(47)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

CHOOSING_DATA_TYPES = [
    (
        "Arjun's first instinct for the Products table's price column is a floating-point type, but his manager stops him before he writes it down.\n\nWhy is a floating-point type dangerous for a money column?",
        "Floating-point types store numbers as an approximation in binary. Adding 0.10 and 0.20 enough times can drift the running total away from the exact 0.30 it should be, a small error on any single row that compounds into disagreement with an accountant's totals across thousands of transactions.",
        "easy", "understand", "choosing-data-types",
        "It stores numbers as a binary approximation, and rounding errors compound across many transactions until totals drift from the exact amount",
        ["It uses too much disk space compared to a whole-number type", "It cannot store negative prices, such as refunds", "It requires a separate column for currency symbols"],
    ),
    (
        "What type should the price column actually use, and what guarantee does it provide that a floating-point type doesn't?",
        "A fixed-precision decimal type, which stores a fixed number of digits before and after the decimal point rather than an approximation. A price of 499.50 stored this way is exactly 499.50, forever, no matter how many times it's added, subtracted, or summed across a million rows.",
        "medium", "apply", "choosing-data-types",
        "A fixed-precision decimal type, which stores an exact value with no rounding drift, however many times it's summed",
        ["A variable-length text type, which stores the price exactly as typed by a human", "A whole-number type, since prices should always be rounded to the nearest rupee", "A boolean type, since price only needs to indicate whether an item is paid or free"],
    ),
    (
        "Every SKU code at Kadam Retail is exactly eight characters long by company policy.\n\nWhat data type fits this column, and why?",
        "A fixed-length text type, since every value occupies the same amount of space and the database never has to guess how much room a row will need — a natural fit whenever every value truly is the same length by policy.",
        "easy", "understand", "choosing-data-types",
        "Fixed-length text, since every SKU is guaranteed to be exactly the same length",
        ["Variable-length text, since SKU codes might occasionally need to grow longer", "A whole-number type, since SKU codes only ever contain digits", "A boolean type, since a SKU code only needs to indicate whether a product is active"],
    ),
    (
        "Product names range from \"Pen\" to forty or fifty characters describing a bundle or variant.\n\nWhat type fits this column, and what habit should always accompany it?",
        "A variable-length text type, which only stores as many characters as the value actually contains. Arjun's manager adds the habit of always attaching a maximum length, even though the type technically allows unlimited length, to protect against data-entry mistakes and hint at what a \"normal\" value should look like.",
        "medium", "apply", "choosing-data-types",
        "Variable-length text, always capped with a sensible maximum length even if the type allows more",
        ["Fixed-length text, since all product names should be padded to the same length", "Variable-length text, with no maximum length set, since names should never be restricted", "A whole-number type referencing a separate lookup table of allowed names"],
    ),
    (
        "Availability (whether a product is currently for sale) is declared as a dedicated boolean type, rather than a whole number (1/0) or free text (\"Yes\"/\"No\").\n\nWhy does the boolean type win here?",
        "A boolean type says directly that this is a strict two-state question with nothing in between. A whole number or free text column invites mistakes like \"yess\" that a genuine boolean type simply cannot produce.",
        "medium", "understand", "choosing-data-types",
        "It directly enforces a strict two-state value, preventing typos like \"yess\" that text or numeric alternatives can't rule out",
        ["It uses less storage than any other data type available", "It's the only type that can be indexed for fast searching", "It automatically converts to a percentage when displayed on screen"],
    ),
    (
        "An earlier version of Kadam Retail's inventory system stored stock quantity in a type too narrow for large numbers. Two years later a bulk supplier deal pushed one product's stock past that ceiling, and the column silently overflowed into a nonsensical negative number.\n\nWhat lesson does this teach about choosing a type too narrow?",
        "Choosing a type too narrow for where data is actually headed does not fail today, it fails later, quietly, at the worst possible moment, once real growth outpaces the assumption baked into the original type choice.",
        "hard", "analyze", "choosing-data-types",
        "A too-narrow type doesn't fail immediately; it fails later and silently, once real growth exceeds the original assumption",
        ["Choosing a type too narrow always fails immediately and loudly with a clear error", "Stock quantity should never be stored as a number under any circumstances", "The overflow was actually caused by using a floating-point type instead of an integer"],
    ),
]

PRIMARY_KEY_STRATEGIES = [
    (
        "Vaanam Logistics has always identified shipments with a simple auto-incrementing number from one central database. The company is now opening a second data center that can also create shipment records.\n\nWhy does this break the auto-incrementing approach?",
        "Both data centers cannot be allowed to hand out the same shipment number, like \"shipment 4501,\" at the same moment for two completely different shipments — auto-increment fundamentally depends on a single, central counter, and now there are two places doing the counting.",
        "easy", "understand", "primary-key-strategies",
        "Two independent data centers could generate the exact same shipment number for two different shipments at once",
        ["Auto-incrementing numbers can never exceed a few thousand values total", "The second data center cannot physically store numeric columns", "Shipment numbers would need to become text instead of numbers"],
    ),
    (
        "What property of a UUID lets Vaanam's two data centers each safely mint new shipment IDs, independently, without any risk of collision?",
        "A UUID is generated largely from randomness, engineered so the odds of two different systems generating the same UUID by coincidence are astronomically small, and generating one requires no coordination with any central authority.",
        "medium", "understand", "primary-key-strategies",
        "UUIDs are generated independently with no central coordination needed, and collisions are astronomically unlikely",
        ["UUIDs are assigned by a single master server that both data centers must contact first", "UUIDs are simply auto-incrementing numbers with letters mixed in for readability", "UUIDs guarantee uniqueness only within a single data center, not across two"],
    ),
    (
        "Compared to auto-incrementing integers, what real costs come with switching to UUIDs?",
        "A UUID takes up noticeably more storage (several times the size of a small integer), is unordered by nature (making certain bulk indexing slightly less efficient), and is simply harder for a human to work with or read aloud.",
        "medium", "apply", "primary-key-strategies",
        "More storage per row, less efficient ordering for indexing, and much harder for a human to read or say aloud",
        ["UUIDs are actually smaller and faster to index than integers in every case", "UUIDs cannot be used as primary keys in a relational database at all", "UUIDs require a separate database server dedicated only to generating them"],
    ),
    (
        "An auto-incrementing integer used as a public-facing order number is described as revealing \"more about the business than Vaanam might want to expose.\"\n\nWhat exactly does it reveal?",
        "Anyone who sees \"order 8000\" knows the company has processed roughly 8,000 orders total, and anyone handed two order IDs on different days can guess roughly how many orders landed in between — information that isn't a problem internally but can leak business details publicly.",
        "medium", "analyze", "primary-key-strategies",
        "Roughly how many total orders the company has processed, and roughly how many orders occurred between any two visible IDs",
        ["The exact identity of every customer who placed an order", "The physical location of the warehouse that shipped each order", "The exact profit margin earned on each individual order"],
    ),
    (
        "Devika's tech lead frames the primary key decision as a question about where and how rows get created, not which option is \"objectively better.\"\n\nWhat's the sensible choice for a single, centrally controlled database serving a purely internal admin tool?",
        "An auto-incrementing integer remains the simplest, fastest, most space-efficient choice, since there's no coordination problem to solve — reaching for a UUID there would just be paying a cost for a problem that doesn't exist.",
        "medium", "apply", "primary-key-strategies",
        "An auto-incrementing integer, since a single internal database has no distributed coordination problem to solve",
        ["A UUID, since UUIDs are always the objectively superior choice", "Neither; internal tools should never have a primary key at all", "A composite key made from every column in the table"],
    ),
    (
        "Even inside a single database with no distribution problem at all, a team might still choose a UUID for a customer-facing order ID shown in a URL.\n\nWhy would they make that choice?",
        "So a curious or malicious visitor cannot increment a number in the address bar and quietly browse through every other customer's order by simply changing \"order/4501\" to \"order/4502\" — an unguessable identifier protects against this even without any distribution problem.",
        "hard", "analyze", "primary-key-strategies",
        "To prevent a visitor from guessing and browsing neighbouring customers' orders by incrementing a visible number in the URL",
        ["Because UUIDs make the URL load noticeably faster for the customer", "Because auto-incrementing integers cannot be displayed in a web browser", "Because the database requires a UUID for any column shown in a URL"],
    ),
]

NAMING_CONVENTIONS = [
    (
        "Sanjay finds a table called Customer and another called transactions in the same schema, one singular, one plural, with no explanation for the difference.\n\nWhat's the actual problem here, and what's the fix his team agrees on?",
        "Neither convention is objectively wrong on its own, but doing both in the same schema is indefensible, since a developer following one pattern will confidently guess wrong for a table that quietly uses the other. The fix is to pick one convention, document it once, and apply it to every table without exception.",
        "easy", "understand", "naming-conventions",
        "Mixing both styles in one schema forces guesswork; the fix is picking one convention and documenting it once for every table",
        ["Plural table names are always correct, and singular names must be renamed immediately", "The problem is only cosmetic and has no real effect on developers", "Singular table names are always correct, and plural names must be renamed immediately"],
    ),
    (
        "A column called custId sits beside another called user_id in different tables, both referring to the same kind of person.\n\nWhat problem does this illustrate, and what convention does Sanjay's team settle on?",
        "This is a mix of camelCase and snake_case styles. Most relational database systems are case-insensitive about unquoted identifiers by default, so mixing styles can actively cause confusion about whether names are meant to be the same or different. The team settles on snake_case for every column.",
        "medium", "apply", "naming-conventions",
        "Mixed casing styles (camelCase vs. snake_case); the team settles on snake_case for every column, consistently",
        ["Mixed casing styles; the team settles on camelCase for every column, consistently", "Duplicate column names; the team removes one of the two columns entirely", "A missing foreign key; the team adds a constraint linking the two columns"],
    ),
    (
        "A column named order sits in a Payments table, meant to store a sequence number for a payment attempt.\n\nWhy is this name risky, and what's the fix?",
        "\"Order\" is a word many database systems reserve for their own sorting instructions, and a column sharing that name invites exactly the kind of subtle, hard-to-diagnose error that eats an afternoon. The fix is a more specific name, such as attempt_number.",
        "medium", "analyze", "naming-conventions",
        "\"Order\" collides with a word many database systems reserve internally; the fix is a more specific name like attempt_number",
        ["\"Order\" is too short a name to be valid in most database systems", "The column should be renamed to \"sequence\" instead, which has no reserved meaning anywhere", "There's no real risk; reserved words only matter for table names, not column names"],
    ),
    (
        "A column in the Transactions table is simply named id, but a closer look at the data shows it actually holds a reference to a row in the Customers table.\n\nWhat's wrong with this name, and what rule does Sanjay propose going forward?",
        "The bare name \"id\" looks like it should be the transaction's own primary key, but it's really a foreign key masquerading as a primary key by name alone. Sanjay's rule going forward is that a foreign key column should be named after the table it references, in the singular, followed by _id — here, customer_id.",
        "medium", "apply", "naming-conventions",
        "\"id\" misleadingly looks like the table's own primary key; foreign keys should be named after the referenced table plus _id, e.g. customer_id",
        ["\"id\" is fine as a foreign key name as long as the column type is an integer", "The column should be renamed \"reference\" instead, which is more general-purpose", "There's no problem; every column in every table should simply be named \"id\""],
    ),
    (
        "A column named cst_addr_ln1 forces every new reader to reverse-engineer \"customer address line 1\" from truncated fragments.\n\nWhat is Sanjay's rule about when abbreviation is acceptable?",
        "Abbreviate only when the shortened form would be instantly obvious to any new teammate on their first day, like \"id\" itself, which is universally understood. Everything else should be spelled out in full, since abbreviating to save a few keystrokes almost never pays for itself once a schema is read by more people than wrote it.",
        "medium", "understand", "naming-conventions",
        "Abbreviate only when the shortened form is instantly obvious to any newcomer; otherwise spell names out in full",
        ["Never abbreviate under any circumstances, including universally understood terms like \"id\"", "Always abbreviate every column name to save storage space", "Abbreviate only column names, never table names, regardless of clarity"],
    ),
    (
        "Why does the lesson describe a naming convention as \"a small, almost invisible kind of documentation\"?",
        "A naming convention lives inside the names themselves rather than in a separate document nobody reads — consistent table names, consistent casing, self-explanatory foreign keys, and disciplined abbreviations together let a new developer read a schema cold, without pulling a teammate aside to translate it.",
        "hard", "analyze", "naming-conventions",
        "Good names carry documentation inside themselves, letting a schema be read cold instead of requiring a separate document or a teammate's explanation",
        ["It's called that because naming conventions are always written as code comments", "It's called that because naming conventions require no written documentation ever, by any team", "It's called that because database systems automatically generate documentation from column names"],
    ),
]

AUDIT_COLUMNS_SOFT_DELETES = [
    (
        "Rekha Menon's account row is completely gone after a weekend cleanup script runs, not marked inactive, just gone. Engineering tells Farah the row cannot be recovered.\n\nWhat should have been in place from the start to prevent this outcome?",
        "Audit columns and soft deletes — the table was never designed to remember that a row had ever existed once it was deleted, and a soft-delete mechanism would have kept the row recoverable instead of erasing it outright.",
        "easy", "understand", "audit-columns-and-soft-deletes",
        "Audit columns and a soft-delete mechanism, so the row would remain recoverable instead of being erased entirely",
        ["A stronger password policy for the engineering team", "A larger server with more available disk space", "A faster network connection between the cleanup script and the database"],
    ),
    (
        "What are the two most common audit columns, and who or what actually sets their values?",
        "created_at, a timestamp recorded automatically the moment a row is first inserted, and updated_at, a timestamp that refreshes automatically every time any part of the row changes afterward. Neither is typed in by a user; the database or application layer sets them silently in the background.",
        "easy", "remember", "audit-columns-and-soft-deletes",
        "created_at and updated_at, set automatically by the database or application layer, never typed in by a user",
        ["deleted_at and restored_at, typed in manually by a support agent", "start_date and end_date, entered by the customer during signup", "row_id and table_id, generated once when the table itself is created"],
    ),
    (
        "What is a soft delete, and how does it differ from removing a row from a table entirely?",
        "A soft delete marks a row as deleted, typically with a boolean flag or a nullable deleted_at timestamp, rather than physically removing it. The row stays fully present in the table and recoverable, simply becoming invisible to the parts of the application that only want to see active rows.",
        "medium", "understand", "audit-columns-and-soft-deletes",
        "It marks a row as deleted (e.g. via a deleted_at timestamp) while keeping it fully present and recoverable, rather than physically erasing it",
        ["It's identical to a normal delete, just performed on a schedule instead of immediately", "It moves the row to a separate database on a different server", "It converts the row's data into an encrypted, unreadable format"],
    ),
    (
        "If Rekha's row had used a deleted_at column, how could Farah have resolved the entire phone call in minutes, according to the lesson?",
        "By finding the row, confirming it matched Rekha's account, and simply clearing the deleted_at timestamp back to empty — the order history, preferences, and loyalty progress would never have been at risk, because none of it was ever actually gone.",
        "medium", "apply", "audit-columns-and-soft-deletes",
        "By finding the row and clearing its deleted_at timestamp back to empty, since the data was never actually erased",
        ["By restoring the entire database from a backup taken the previous week", "By manually re-typing two years of Rekha's order history from memory", "By asking Rekha to create a brand new account with the same email address"],
    ),
    (
        "What is the first tradeoff of soft deletes the tech lead is careful to walk through with Farah?",
        "Every future query against that table that only wants \"real,\" active rows now has to remember to filter out the soft-deleted ones, every single time, in every application, report, and script — forget that filter once, and a supposedly deleted customer reappears somewhere embarrassing, like a marketing email.",
        "medium", "analyze", "audit-columns-and-soft-deletes",
        "Every query wanting only active rows must remember to filter out soft-deleted ones, or a deleted record can reappear unexpectedly",
        ["Soft deletes make every query run permanently slower with no possible fix", "Soft deletes require every column in the table to become nullable", "Soft deletes can only be applied to tables with fewer than ten columns"],
    ),
    (
        "What is the second tradeoff of soft deletes, related to how a table grows over time?",
        "A table using soft deletes never actually shrinks from deletions, since nothing is truly removed through normal application use. Over years it can accumulate a large number of soft-deleted rows sitting alongside active ones, which can slow queries and inflate storage unless someone revisits old soft-deleted data for a genuine, permanent cleanup on a separate, deliberate schedule.",
        "hard", "analyze", "audit-columns-and-soft-deletes",
        "The table never shrinks from normal deletions, so soft-deleted rows accumulate over time, potentially slowing queries and inflating storage",
        ["The table automatically shrinks every night to remove all soft-deleted rows", "Soft-deleted rows are compressed automatically to use zero extra storage", "The table's primary key eventually runs out of available values"],
    ),
]

SCHEMAS_AND_NAMESPACES = [
    (
        "The sales team creates an Orders table. Weeks later, unaware, the inventory team creates its own Orders table meaning purchase orders sent to suppliers, a completely different concept sharing the exact same name.\n\nWhat happens, and what organizational tool does Kiran introduce to fix it?",
        "The two Orders tables collide, and nobody notices until a report quietly pulls the wrong one. Kiran's fix is a schema (or namespace), a named grouping that lets related tables live together under one label while staying cleanly separated from tables owned by a different team.",
        "easy", "understand", "schemas-and-namespaces",
        "The two tables collide silently; Kiran's fix is a schema (namespace) grouping each team's tables under its own label",
        ["The two tables merge automatically into one combined table", "The database refuses to let the inventory team create any table at all", "Nothing happens; database systems automatically rename duplicate table names"],
    ),
    (
        "The word \"schema\" is used two different ways in database work.\n\nWhat's the difference between the two meanings, and which one is being introduced in this lesson?",
        "One meaning refers to the structure of a single table, its columns, types, and keys. The meaning at stake here is different: a schema as a named container that groups a set of related tables together inside one database, much like a folder groups related files on a hard drive.",
        "medium", "understand", "schemas-and-namespaces",
        "One meaning is a single table's structure (columns/types/keys); this lesson's meaning is a named container grouping related tables, like a folder",
        ["Both meanings refer to exactly the same thing, just used in different contexts", "One meaning refers to a database server; the other refers to a single row", "One meaning refers to a query language; the other refers to a data type"],
    ),
    (
        "After Kiran introduces sales, inventory, and reporting schemas, sales.Orders and inventory.Orders can coexist safely.\n\nWhat is a table's \"true identity\" really made of, once schemas are in place?",
        "A table's true identity is really the pair of its schema name and its table name together, sales.Orders and inventory.Orders, not the table name alone — which is exactly why the naming collision that started the whole mess can no longer happen.",
        "medium", "apply", "schemas-and-namespaces",
        "The pair of its schema name and table name together, not the table name by itself",
        ["The table's row count at the moment it was created", "The order in which the table was created relative to other tables", "The physical disk drive the table's data happens to be stored on"],
    ),
    (
        "Beyond preventing name collisions, what organizational benefit does browsing tables \"by schema\" give Kiran's reporting team when exploring what exists to build a new dashboard?",
        "It lets them see, at a glance, which tables belong to sales, which belong to inventory, and which are reporting's own intermediate tables, rather than scrolling through one enormous undifferentiated list of every table the company has ever created.",
        "medium", "analyze", "schemas-and-namespaces",
        "It lets them see at a glance which team owns which tables, instead of scrolling through one flat, undifferentiated list",
        ["It automatically generates a dashboard for them with no further work needed", "It prevents the reporting team from ever needing to write a query", "It merges all three teams' tables into a single unified table automatically"],
    ),
    (
        "Kiran grants the reporting team read-only access to the sales and inventory schemas as a whole, rather than listing permissions table by table.\n\nWhat does granting access at the schema level save her from doing?",
        "It saves her from maintaining a table-by-table permissions list by hand — granting access at the schema level sets one rule instead, and most systems can be configured so any new table created inside that schema inherits the same policy automatically going forward.",
        "medium", "apply", "schemas-and-namespaces",
        "Maintaining a table-by-table permissions list by hand; one schema-level rule can cover every table, including future ones",
        ["Nothing; schema-level access provides no real savings over table-level access", "Writing any queries at all for the reporting team", "Backing up the sales and inventory schemas separately"],
    ),
    (
        "Why does the sales team get full read-and-write access only to its own sales schema, with no access at all to inventory?",
        "Sales has no legitimate reason to modify warehouse stock counts directly — the same instinct behind giving each team its own labeled drawer rather than one shared drawer everyone digs through, making a team far less likely to accidentally break something belonging to someone else.",
        "hard", "analyze", "schemas-and-namespaces",
        "Sales has no legitimate reason to modify inventory data directly, and restricting access reduces the risk of accidentally breaking another team's data",
        ["Sales is technically incapable of writing to any schema other than its own", "Inventory data is stored on a completely different physical server", "Restricting access has no real benefit; it's purely a symbolic gesture"],
    ),
]

SCHEMA_DESIGN_REVIEW = [
    (
        "Meenal's colleague's draft booking table has no primary key at all, no column or combination guaranteed unique for every row.\n\nWhat's the risk, and what's the fix?",
        "Nothing stops two rows from ending up completely identical, and nothing gives any other part of the system a reliable way to say \"this specific booking, and no other.\" The fix is adding a dedicated booking_id that the database generates automatically for every new row.",
        "easy", "understand", "schema-design-review",
        "Rows can't be reliably told apart; the fix is a dedicated, auto-generated booking_id column",
        ["There is no real risk, since bookings are always naturally unique", "The fix is to rename the table, which resolves the missing key issue", "The fix is to delete duplicate rows manually once a week"],
    ),
    (
        "StudentName and StudentEmail use one capitalization style, eventTitle and ticketPrice use another, and event_date uses a third, all inside the same table.\n\nWhat is the fix Meenal recommends?",
        "A consistent style, snake_case throughout, chosen once and applied everywhere, removes the guesswork about which style applies where, table by table and column by column.",
        "easy", "apply", "schema-design-review",
        "Apply one consistent casing style, snake_case, to every column in the table",
        ["Keep three different styles, since variety helps distinguish column types visually", "Rename every column to a single word with no separators at all", "Switch every column to uppercase letters only, for maximum visibility"],
    ),
    (
        "ticketPrice is declared as a floating-point number in the draft.\n\nWhy does Meenal flag this as the most urgent problem, and what's the fix?",
        "It's the kind of mistake that looks completely fine in testing and only reveals itself once thousands of real transactions have run through it, as tiny rounding errors compound into totals that don't match a receipt or an accountant's ledger. The fix is a fixed-precision decimal type instead.",
        "medium", "analyze", "schema-design-review",
        "Floating-point rounding errors silently compound over many transactions; the fix is a fixed-precision decimal type",
        ["It's urgent only because floating-point numbers take up more storage than text", "It's urgent because floating-point types cannot store prices above 1000", "It's urgent because floating-point columns cannot be indexed at all"],
    ),
    (
        "The draft table has no created_at or updated_at columns.\n\nWhat real scenario, six months in the future, does Meenal imagine that makes this a genuine problem rather than a nitpick?",
        "A student disputes a booking, claiming they never made it, and support has no way to check when the row was created or whether it was recently changed by anyone, including by mistake — two quiet audit columns would answer that in seconds.",
        "medium", "apply", "schema-design-review",
        "A student disputes a booking months later, and support has no way to check when it was created or last changed",
        ["A student wants to change their seat assignment the same day they booked it", "The event itself gets cancelled and every booking needs to be refunded at once", "The system needs to calculate how many seats remain available for an event"],
    ),
    (
        "StudentName and StudentEmail are copied directly into every booking row a student makes across multiple events.\n\nWhat is this problem called, and what's the structural fix?",
        "This is redundant, unnormalized data — the same student's name and email get retyped, verbatim, once for every event they book. The fix is to split the table in two: a Students table holding each student's details exactly once, and a Bookings table that refers back to a student by a stable identifier.",
        "medium", "analyze", "schema-design-review",
        "Redundant, unnormalized data; the fix is splitting into separate Students and Bookings tables linked by a stable reference",
        ["A missing index; the fix is adding an index on StudentName", "A data type mismatch; the fix is converting StudentEmail to a numeric type", "An access-control problem; the fix is restricting who can read the table"],
    ),
    (
        "Meenal flags booking_id as risky if it's a simple auto-incrementing integer, since booking confirmations get shared with students through a public link.\n\nWhat's the risk, and what's the fix?",
        "A student could edit that link and quietly browse other students' bookings just by changing one digit. Because this identifier is meant to be public-facing, an unguessable identifier, generated independently rather than counted upward from a shared starting point, is the safer choice.",
        "hard", "analyze", "schema-design-review",
        "A predictable integer lets someone guess neighbouring bookings by editing a digit in the link; the fix is an unguessable public identifier",
        ["The risk is that integers take up too much storage for a public link", "The risk applies only to internal tables, never to public-facing ones", "The fix is to remove booking_id from the table entirely and rely on event_title instead"],
    ),
]

SYNTHESIS = [
    (
        "Arjun's Products table uses a fixed-precision decimal for price, and Meenal's booking review flags ticketPrice as a floating-point mistake in an unrelated schema.\n\nWhat common principle do both examples teach about columns holding money?",
        "Money should always use a fixed-precision decimal type, never an approximate floating-point type, because floating-point rounding errors compound over many transactions into totals that silently disagree with real receipts and ledgers.",
        "medium", "analyze", "choosing-data-types",
        "Money columns should always use fixed-precision decimal types, never floating-point, to avoid compounding rounding errors",
        ["Money columns should always be stored as plain text to avoid rounding entirely", "The two examples actually teach opposite lessons about which type to use for money", "Floating-point types are fine for money as long as the amount stays under 1000"],
    ),
    (
        "Devika's UUID decision for Vaanam's shipments and Meenal's booking_id fix both involve choosing between an auto-incrementing integer and an unguessable identifier.\n\nWhat's the shared decision rule across both cases?",
        "The right choice depends on where and how rows get created and whether the identifier is ever exposed publicly — an auto-incrementing integer is fine for internal, single-database use, but a public-facing or multi-system identifier needs an unguessable, independently generatable ID like a UUID.",
        "hard", "analyze", "primary-key-strategies",
        "The choice depends on whether rows are created by multiple independent systems and whether the ID is public-facing; both favor an unguessable identifier",
        ["Auto-incrementing integers should always be used, regardless of the situation", "UUIDs should always be used, regardless of the situation", "The two cases are unrelated and share no common decision rule"],
    ),
    (
        "Meenal's redundant StudentName/StudentEmail problem and Sunrise Traders' repeated CustomerAddress problem (from normalization) describe the same underlying issue in two different lessons.\n\nWhat is that shared issue, and what's the shared structural fix?",
        "Both are the same fact stored redundantly in every row that mentions it, causing update anomalies when the fact changes. The shared fix is splitting the table so the fact lives exactly once in a table of its own, referenced from other tables by a stable identifier.",
        "hard", "analyze", "schema-design-review",
        "Both are redundant data causing update anomalies; the shared fix is splitting the fact into its own table, referenced by a stable identifier",
        ["The two problems are unrelated; one is about naming and the other is about data types", "The shared fix is adding a floating-point column to track how often the fact changes", "The shared fix is deleting the redundant rows rather than restructuring the table"],
    ),
    (
        "Kiran's schema-level access control and Meenal's audit-column recommendation are both described as habits that pay off later rather than immediately.\n\nWhich future problem does each practice specifically prevent?",
        "Schema-level access control prevents accidental cross-team writes and table-name collisions as a company scales to multiple teams sharing one database. Audit columns prevent an unanswerable \"when did this happen\" question when a dispute or investigation arises months after a row was created or changed.",
        "medium", "analyze", "schemas-and-namespaces",
        "Schema access prevents accidental cross-team collisions and writes; audit columns prevent an unanswerable \"when did this happen\" question later",
        ["Both practices prevent exactly the same problem: slow query performance", "Schema access prevents rounding errors; audit columns prevent naming collisions", "Neither practice actually prevents any specific future problem"],
    ),
]

SET1_SOURCES = [
    (CHOOSING_DATA_TYPES, 0),
    (PRIMARY_KEY_STRATEGIES, 0),
    (NAMING_CONVENTIONS, 0),
    (AUDIT_COLUMNS_SOFT_DELETES, 0),
    (SCHEMAS_AND_NAMESPACES, 0),
    (SCHEMA_DESIGN_REVIEW, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    CHOOSING_DATA_TYPES[1:]
    + PRIMARY_KEY_STRATEGIES[1:]
    + NAMING_CONVENTIONS[1:]
    + AUDIT_COLUMNS_SOFT_DELETES[1:]
    + SCHEMAS_AND_NAMESPACES[1:]
    + SCHEMA_DESIGN_REVIEW[1:]
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
            "topics": "database-design-and-modeling",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 2.3.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 2.3.2")
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
ws.title = "DBMS - MCQ - Unit 2.3"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 2 - Database Design and Modeling/2.3 - Practical Schema Design - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
