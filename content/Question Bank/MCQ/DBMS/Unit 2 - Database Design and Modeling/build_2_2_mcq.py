import random
import openpyxl

random.seed(43)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

WHY_NORMALIZE = [
    (
        "Ilyas Bakery Supplies' address is written four different ways across four different rows in Sunrise Traders' Orders table, because his shop placed four orders and the address was only corrected on the most recent one, leaving the invoice sent to his old address.\n\nWhat is this problem called?",
        "This is an update anomaly: changing a single real-world fact (the address) requires updating it in every row where it happens to be repeated, and missing even one row leaves the table telling two different stories about the same customer.",
        "easy", "understand", "why-normalize",
        "An update anomaly — the same fact is repeated across rows and not all copies got updated",
        ["An insert anomaly — a new fact could not be recorded", "A delete anomaly — deleting a row destroyed unrelated data", "A domain violation — the address doesn't match its column's legal values"],
    ),
    (
        "A warehouse manager wants to add a new product, a box of highlighters, to the catalog before launch, but Priya has no way to do it in the Orders table, since every row represents an order requiring a customer and quantity.\n\nWhat is this problem called?",
        "This is an insert anomaly: a table structured around one kind of event (an order) cannot hold a fact about something else (a product) until that something else becomes involved in an event, so the highlighters can't officially exist until someone buys them.",
        "easy", "understand", "why-normalize",
        "An insert anomaly — a new product fact cannot be recorded without inventing a fake order",
        ["An update anomaly — the highlighters' price keeps changing across rows", "A delete anomaly — the highlighters were accidentally removed from the catalog", "A partial dependency — the product depends on only part of a composite key"],
    ),
    (
        "Meenal Stationers placed exactly one order, and when that order (row O503) is deleted after the shop closes, the shop's address and phone number, which existed only in that one row, disappear along with it.\n\nWhat is this problem called?",
        "This is a delete anomaly: removing a row for one reason (cancelling an order) accidentally destroys an unrelated fact (a customer's contact details), simply because the two facts were never separated in the first place.",
        "easy", "understand", "why-normalize",
        "A delete anomaly — deleting an order row also destroyed the customer's only stored contact record",
        ["An update anomaly — Meenal's address was never correctly entered", "An insert anomaly — a new customer could not be added to the system", "A transitive dependency — CustomerCity depends on CustomerID indirectly"],
    ),
    (
        "All three anomalies Priya finds, update, insert, and delete, share one root cause according to the lesson.\n\nWhat is that shared root cause?",
        "The Orders table is asking a single row to answer three unrelated questions at once (who is this customer, what is this product, what happened in this order); whenever one row is forced to carry facts about more than one real-world thing, those facts inevitably get repeated across other rows, and repetition is where every anomaly breeds.",
        "medium", "analyze", "why-normalize",
        "A single row is forced to carry facts about more than one real-world thing at once, causing repetition",
        ["The table simply has too many columns, regardless of what they describe", "The table was never given a primary key of any kind", "The table stores text values instead of numeric ones wherever possible"],
    ),
    (
        "What is the fix Priya eventually reaches for to resolve all three anomalies, according to the lesson's conclusion?",
        "Not a clever trick or a stricter data-entry policy, but a disciplined way of reorganizing the table, normalization, so that each fact is stored exactly once, attached to the one real-world thing it actually describes.",
        "medium", "understand", "why-normalize",
        "Normalization — splitting the table so each fact is stored exactly once, attached to the thing it describes",
        ["Adding stricter validation rules to the existing single table, without splitting it", "Training staff to double-check every row manually before saving", "Storing every fact as plain text so it's easier for humans to compare visually"],
    ),
]

FUNCTIONAL_DEPENDENCIES = [
    (
        "Meera notices that every row with CustomerID C12 in Sunrise Traders' data says \"Ilyas Bakery Supplies,\" with no exceptions anywhere in the table.\n\nHow would she write this relationship using functional dependency notation?",
        "This is written CustomerID -> CustomerName: for any two rows sharing the same CustomerID, they must also share the same CustomerName, with certainty, every single row, no exceptions.",
        "easy", "remember", "functional-dependencies",
        "CustomerID -> CustomerName",
        ["CustomerName -> CustomerID", "CustomerID -> OrderID", "CustomerName -> CustomerAddress"],
    ),
    (
        "In a college roll number table, \"Naina Fernandes\" appears twice, attached to two different roll numbers (21CS045 and 21CS047). Does this break the functional dependency RollNumber -> StudentName?",
        "No — a functional dependency only requires that the same X (RollNumber) always produces the same Y (StudentName); it says nothing about whether the same Y can come from more than one X. Every occurrence of a given roll number brings the same name with it, so the dependency holds perfectly.",
        "medium", "analyze", "functional-dependencies",
        "No — the dependency only requires that a given RollNumber always maps to the same name, not that names are unique",
        ["Yes — a functional dependency requires that every value on the right side be unique", "Yes — two students can never share the same name in a valid functional dependency", "No — but only because this is a coincidence and the dependency should be rewritten"],
    ),
    (
        "In Meera's dependency table, OrderID -> OrderDate and OrderID -> CustomerID are listed.\n\nWhat is the column on the left side of a functional dependency called?",
        "The column on the left, the one doing the determining, is called the determinant. Here, OrderID is the determinant, and OrderDate and CustomerID are the dependent columns.",
        "easy", "remember", "functional-dependencies",
        "The determinant",
        ["The candidate key", "The foreign key", "The surrogate key"],
    ),
    (
        "In an OrderItems table keyed by the pair (OrderID, ProductID), Meera notices that ProductName doesn't actually need OrderID at all — it's fully explained by ProductID alone.\n\nWhat is this pattern called?",
        "A dependency where a column depends on only part of a composite key, rather than the whole key, is called a partial dependency — a warning sign that a fact is stored in a table keyed by more information than that fact actually needs.",
        "medium", "understand", "functional-dependencies",
        "A partial dependency",
        ["A transitive dependency", "A full functional dependency", "A candidate key violation"],
    ),
    (
        "In a simplified Orders table storing OrderID, CustomerID, and CustomerCity, OrderID determines CustomerID, and CustomerID determines CustomerCity — but OrderID only reaches CustomerCity by first passing through CustomerID.\n\nWhat is this two-hop chain called?",
        "This is a transitive dependency: a column depends on the key only indirectly, through another non-key column, rather than depending on the key directly — a pattern Meera flags as probably not sitting in the right table.",
        "medium", "understand", "functional-dependencies",
        "A transitive dependency",
        ["A partial dependency", "A composite key", "A referential integrity constraint"],
    ),
]

FIRST_NORMAL_FORM = [
    (
        "Tara finds Ilyas Bakery Supplies' PhoneNumbers cell holding \"9845012233, 9900112244\" as a single comma-separated value.\n\nWhat rule does this cell violate, and what does that rule require?",
        "It violates First Normal Form (1NF), the rule that every column in every row must hold one atomic, indivisible value — never a repeating group or a comma-separated bundle disguised as a single entry.",
        "easy", "understand", "first-normal-form",
        "First Normal Form (1NF) — every column must hold exactly one atomic, indivisible value",
        ["Second Normal Form (2NF) — every non-key column must depend on the whole key", "Third Normal Form (3NF) — no column may depend transitively on the key", "Referential integrity — every foreign key value must reference a real row"],
    ),
    (
        "Tara tries to answer \"find every customer whose phone number is 9900112244\" against the PhoneNumbers column as it stands, and either has to scan for a substring or misses Ilyas Bakery Supplies entirely.\n\nWhy does this simple search become clumsy?",
        "Because the column isn't atomic — it holds two phone numbers squeezed into one cell, so a direct, exact match on a single value isn't possible; the search has to awkwardly hunt for a substring inside a longer piece of text instead.",
        "medium", "apply", "first-normal-form",
        "The column isn't atomic, so a direct exact match isn't possible; the search must hunt for a substring instead",
        ["The column is missing a primary key, which is unrelated to atomicity", "The column's data type is text instead of a number", "The database has no index on the PhoneNumbers column"],
    ),
    (
        "Tara's fix splits the Customers table into a leaner Customers table and a new CustomerPhones table, with one row per individual phone number, linked back by CustomerID.\n\nAfter this split, how many rows does Ilyas Bakery Supplies (with two phone numbers) occupy in CustomerPhones?",
        "Two rows — Ilyas Bakery Supplies having two phone numbers is no longer a formatting trick inside one crowded cell, it's simply two ordinary rows in CustomerPhones, both pointing back to the same CustomerID.",
        "medium", "apply", "first-normal-form",
        "Two rows, one per phone number, both referencing the same CustomerID",
        ["One row, with both phone numbers still combined in a single cell", "Zero rows, since phone numbers are removed entirely once 1NF is applied", "Four rows, one for each digit group in the phone numbers"],
    ),
    (
        "A design using separate columns Phone1, Phone2, Phone3 instead of a comma-separated cell is described as having \"the identical problem wearing a different disguise.\"\n\nWhat's wrong with the Phone1/Phone2/Phone3 approach?",
        "It still assumes every customer has the same number of phone numbers, wastes space for customers with fewer, and simply breaks for a customer who eventually needs a fourth — 1NF is a rule about refusing to let one column secretly represent more than one fact, not just about commas specifically.",
        "hard", "analyze", "first-normal-form",
        "It assumes a fixed number of phone numbers per customer, wasting space for some and breaking entirely for anyone needing more",
        ["Nothing is wrong with it; Phone1/Phone2/Phone3 fully satisfies 1NF", "It's wrong only because column names shouldn't include numbers", "It's wrong because it uses more storage than a single PhoneNumbers column"],
    ),
    (
        "What does reaching 1NF guarantee about a table, and what does it explicitly NOT yet guarantee?",
        "1NF guarantees only that every cell is honest about holding a single value. It says nothing about whether every column in a table actually belongs with the rest of that table's key — later checks like 2NF and 3NF are needed for that.",
        "medium", "understand", "first-normal-form",
        "It guarantees every cell holds a single atomic value, but says nothing about whether every column truly belongs with the table's key",
        ["It guarantees every column belongs with the table's key, but not that values are atomic", "It guarantees the table has no redundant data of any kind", "It guarantees every table has a properly chosen primary key"],
    ),
]

SECOND_NORMAL_FORM = [
    (
        "Arjun's OrderItems table is keyed by the composite pair (OrderID, ProductID). Quantity depends on both OrderID and ProductID together, but ProductName and ProductPrice only depend on ProductID alone.\n\nWhich normal form is designed to catch this exact mismatch?",
        "Second Normal Form (2NF) exists to catch and correct exactly this: columns that lean on only part of a composite key rather than the whole thing.",
        "easy", "remember", "second-normal-form",
        "Second Normal Form (2NF)",
        ["First Normal Form (1NF)", "Third Normal Form (3NF)", "Boyce-Codd Normal Form (BCNF)"],
    ),
    (
        "2NF has a prerequisite before it's even a meaningful question to ask about a table.\n\nWhat is that prerequisite?",
        "A table must already be in 1NF before 2NF is meaningful, since 2NF is entirely about how non-key columns relate to the key, and that relationship is only worth examining once every column is confirmed to hold a single atomic value.",
        "medium", "understand", "second-normal-form",
        "The table must already satisfy 1NF",
        ["The table must already have at least one foreign key defined", "The table must already satisfy 3NF", "The table must have fewer than five columns total"],
    ),
    (
        "A table with a single-column primary key (not composite) automatically satisfies 2NF.\n\nWhy is that true?",
        "2NF is about whether a non-key column depends on only part of the primary key. With a single-column key, there is no \"part\" of it to partially depend on — the question only becomes interesting once a table's key is composite, built from two or more columns.",
        "medium", "analyze", "second-normal-form",
        "There is no \"part\" of a single-column key to partially depend on, so partial dependency can't occur",
        ["Single-column keys are always automatically unique, which is unrelated to 2NF", "2NF only applies to tables with more than five columns", "Single-column primary keys are never allowed to have non-key columns at all"],
    ),
    (
        "Rows O501 and O503 both order \"A4 Notebook,\" and both repeat \"A4 Notebook\" and its price \"45\" all over again in Arjun's OrderItems table.\n\nWhat anomaly does this partial dependency drag back in, the same one Priya first encountered?",
        "This is an update anomaly: if Sunrise Traders ever changes the price of an A4 Notebook, every single order line that ever ordered one needs to be found and updated — exactly the same problem Priya ran into with customer addresses, now resurfacing for products.",
        "medium", "apply", "second-normal-form",
        "An update anomaly — changing the notebook's price requires updating every order line that ordered one",
        ["An insert anomaly — new notebooks cannot be added to the catalog", "A delete anomaly — deleting an order would remove the notebook from existence", "A domain violation — the price value falls outside its allowed range"],
    ),
    (
        "If OrderItems had used a single manufactured OrderItemID as its primary key instead of the composite (OrderID, ProductID) pair, the textbook definition of 2NF would already be technically satisfied.\n\nWhy does the lesson still treat this as a problem worth fixing?",
        "The underlying redundancy, ProductName and ProductPrice repeating across every line mentioning the same product, would still be sitting right there in the data, just less visible under the formal rule. The goal was never to pass the rule technically, it was to stop retyping the same product details over and over.",
        "hard", "analyze", "second-normal-form",
        "The same redundancy would still exist in the data, just hidden from the formal rule by renaming the key — the actual goal is eliminating redundancy, not passing a checkbox",
        ["It isn't actually a problem; a manufactured key fully resolves all redundancy automatically", "It's a problem only because manufactured keys are always slower to query", "It's a problem because manufactured keys cannot be used as primary keys in a relational database"],
    ),
]

THIRD_NORMAL_FORM = [
    (
        "Naina's Orders table has a single-column primary key (OrderID), no composite key at all, yet CustomerCity is repeated three times for every order CustomerID C12 places.\n\nSince there's no composite key, which check is this table failing?",
        "This table is failing 3NF, not 2NF — the problem is a transitive dependency (OrderID -> CustomerID -> CustomerCity), a different, sneakier pattern that doesn't require a composite key to occur at all.",
        "easy", "understand", "third-normal-form",
        "Third Normal Form (3NF), due to a transitive dependency",
        ["Second Normal Form (2NF), due to a partial dependency", "First Normal Form (1NF), due to a non-atomic value", "BCNF, due to a determinant that isn't a candidate key"],
    ),
    (
        "Naina traces how CustomerCity connects to OrderID: OrderID determines CustomerID, and CustomerID determines CustomerCity.\n\nHow is this two-step chain written, and what is it called?",
        "It's written OrderID -> CustomerID -> CustomerCity, and this two-step chain, where a non-key column depends on the primary key only indirectly through another non-key column, is called a transitive dependency.",
        "medium", "apply", "third-normal-form",
        "OrderID -> CustomerID -> CustomerCity, a transitive dependency",
        ["CustomerCity -> CustomerID -> OrderID, a partial dependency", "OrderID -> CustomerCity, a full functional dependency with no issue", "CustomerID -> OrderID -> CustomerCity, a candidate key violation"],
    ),
    (
        "3NF assumes a table already satisfies 2NF and adds one further requirement on top of it.\n\nWhat is that additional requirement?",
        "No non-key column may depend transitively on the primary key through another non-key column — a table can pass 2NF perfectly (no composite key to be partial against) and still fail 3NF because of a transitive chain.",
        "medium", "remember", "third-normal-form",
        "No non-key column may depend transitively on the primary key through another non-key column",
        ["Every column must hold a single atomic value", "Every non-key column must depend on the entire composite key", "Every determinant must be a candidate key"],
    ),
    (
        "After Naina's fix, CustomerCity moves into a new Customers table keyed by CustomerID, while Orders keeps only OrderID, CustomerID, and OrderDate.\n\nWhat happens now when Ilyas Bakery Supplies relocates to a new city?",
        "Naina updates the city in a single row of Customers, and every order referencing CustomerID C12 stays correctly, automatically associated with the right city, because the city is looked up through the relationship rather than copied onto every order.",
        "medium", "apply", "third-normal-form",
        "A single row in Customers is updated, and every related order automatically reflects the correct city",
        ["Every order row for that customer still needs to be manually updated one at a time", "Nothing changes; the city fact is lost once it's moved into a separate table", "A new OrderID must be generated for every one of that customer's past orders"],
    ),
    (
        "Comparing partial dependency (2NF) and transitive dependency (3NF): where does each show up, and what's the key structural difference between the two patterns?",
        "Partial dependency shows up only in tables with a composite key, where a column depends on only part of that key. Transitive dependency shows up in tables with any kind of key, even a single column, where a column depends on the key only indirectly, through another non-key column.",
        "hard", "analyze", "third-normal-form",
        "Partial dependency needs a composite key and a column depending on only part of it; transitive dependency can occur with any key shape via an indirect chain through a non-key column",
        ["They are the same pattern, just given two different names by different textbooks", "Partial dependency occurs with any key shape; transitive dependency requires a composite key", "Transitive dependency only occurs in tables with no primary key at all"],
    ),
]

BCNF = [
    (
        "Dev's OrderInspection-style table, keyed by (OrderID, ProductCategory), passes 1NF, 2NF, and 3NF cleanly. Yet \"Rakesh\" and \"Paper Goods\" appear together twice, on two different orders.\n\nWhat functional dependency is causing this redundancy, and why did 3NF miss it?",
        "Inspector -> ProductCategory is the culprit: each inspector specializes in exactly one category. 3NF missed it because 3NF only restricts dependencies landing on non-prime attributes, and ProductCategory happens to be part of the primary key (prime), so the transitive-style dependency slips past 3NF's check entirely.",
        "medium", "analyze", "bcnf",
        "Inspector -> ProductCategory; 3NF missed it because ProductCategory is a prime attribute (part of the key), and 3NF only restricts non-prime attributes",
        ["OrderID -> Inspector; 3NF missed it because OrderID is never checked by 3NF", "ProductCategory -> OrderID; 3NF missed it because OrderID is a foreign key", "There is no real dependency causing this; it's simply coincidence in a small sample"],
    ),
    (
        "What does BCNF demand for every functional dependency X -> Y in a table, and how is that different from what 3NF checks?",
        "BCNF requires that X (the determinant) must be a candidate key for every functional dependency in the table. Unlike 3NF, it doesn't matter whether Y is prime or not — BCNF cares only about whether the determinant is powerful enough to identify a whole row by itself.",
        "medium", "remember", "bcnf",
        "For every dependency X -> Y, X must be a candidate key — regardless of whether Y is a prime or non-prime attribute",
        ["For every dependency X -> Y, Y must be a candidate key, exactly like 3NF requires", "BCNF only requires that every table have at least one composite key", "BCNF requires that no table have more than two columns per candidate key"],
    ),
    (
        "Dev checks whether Inspector, alone, is a candidate key of the OrderInspection-style table.\n\nWhat does he find, and why does that make Inspector -> ProductCategory a BCNF violation?",
        "Inspector alone cannot uniquely identify a row, since the same inspector appears in multiple rows tied to different orders — OrderID is still needed to pin a row down. Since Inspector determines ProductCategory but Inspector is not a candidate key, this is a BCNF violation, even though the table already satisfied every earlier rule.",
        "medium", "apply", "bcnf",
        "Inspector alone cannot identify a row (OrderID is still needed), so Inspector -> ProductCategory violates BCNF's requirement that the determinant be a candidate key",
        ["Inspector alone can identify a row perfectly, so there is no BCNF violation at all", "Inspector is a candidate key, but ProductCategory is not, which is what triggers the violation", "The violation exists only because OrderID is missing from the table entirely"],
    ),
    (
        "Dev fixes the BCNF violation by splitting into two tables: OrderInspection (OrderID, Inspector) and InspectorSpecialty (Inspector, ProductCategory).\n\nWhy does Inspector -> ProductCategory no longer violate any rule inside InspectorSpecialty?",
        "In InspectorSpecialty, Inspector is now the whole primary key, so Inspector -> ProductCategory no longer breaks any rule — the determinant is finally a candidate key of the table it lives in.",
        "medium", "apply", "bcnf",
        "Inspector is now the entire primary key of InspectorSpecialty, so the determinant genuinely is a candidate key there",
        ["ProductCategory is now the primary key instead, resolving the issue", "The dependency was removed entirely rather than fixed by splitting", "OrderID was added back into InspectorSpecialty to resolve the violation"],
    ),
    (
        "The term \"prime attribute\" is used to explain why 3NF missed the Inspector -> ProductCategory dependency.\n\nWhat does \"prime attribute\" mean, and how does it relate to that gap?",
        "A prime attribute is a column that belongs to a candidate key. 3NF's transitive-dependency check only restricts dependencies landing on non-prime attributes, so a dependency landing on a prime attribute (like ProductCategory here) slips past 3NF entirely, even while producing the exact same redundancy 3NF exists to prevent.",
        "hard", "analyze", "bcnf",
        "A prime attribute is a column that's part of a candidate key; 3NF only restricts non-prime attributes, so dependencies landing on prime attributes slip past its check",
        ["A prime attribute is any column with a numeric data type, unrelated to keys", "A prime attribute is a column that can never be part of a functional dependency", "A prime attribute is simply another name for a foreign key column"],
    ),
]

DENORMALIZE = [
    (
        "Vivek's monthly revenue-per-city report requires pulling data from five separate tables, and it now takes noticeably longer to run than it did against the old, messy, single Orders table.\n\nWhat is Vivek experiencing, according to the lesson?",
        "He isn't seeing a bug — he's running into the honest cost of normalization itself: safe, anomaly-free writes traded for slower reads, since combining several small, precise tables back together takes real computing work.",
        "easy", "understand", "denormalize",
        "The honest cost of normalization — safe writes traded for slower reads that must combine several tables",
        ["A bug introduced by the normalization process that needs to be fixed", "Evidence that his team applied BCNF incorrectly somewhere", "A sign that the tables need to be merged back into one immediately"],
    ),
    (
        "What does the old, single combined Orders table protect well, and what does it cost, compared to the fully normalized, split schema?",
        "The old wide table gives fast reads (everything sits together already) but costs redundant data with update and delete anomalies. The fully normalized schema is the mirror image: safe, anomaly-free writes, but reports must combine several tables, which takes real computing work.",
        "medium", "understand", "denormalize",
        "The wide table gives fast reads but risks anomalies; the normalized schema gives safe writes but slower, more complex reads",
        ["The wide table gives safe writes but slow reads; the normalized schema gives fast reads but risky writes", "Both designs give identical performance; the only difference is disk space used", "The wide table has no real drawback compared to the normalized schema"],
    ),
    (
        "Vivek's fix is not to undo the normalized schema Sunrise Traders depends on for everyday order-taking.\n\nWhat does he build instead, and what is this practice called?",
        "He builds a separate summary structure specifically for reporting, storing CustomerCity and ProductCategory directly alongside sales totals, refreshed on a schedule rather than recalculated from scratch. This deliberate reintroduction of redundancy for speed is called denormalization.",
        "medium", "apply", "denormalize",
        "A separate, deliberately redundant reporting summary, refreshed periodically — this practice is called denormalization",
        ["A rollback of all the normalization work, restoring the original single table", "A new index added to each of the five normalized tables, with no redundancy involved", "A caching layer that stores query results but no actual data redundancy"],
    ),
    (
        "The lesson lists several habits that \"keep the trade-off honest\" when denormalizing. Which habit addresses the risk that a denormalized copy eventually tells a lie, the same kind of lie the original combined table told about Ilyas Bakery Supplies' address?",
        "Putting a plan in place for keeping the redundant copy refreshed, whether nightly recalculation or updating whenever the source data changes, because a denormalized copy that nobody refreshes eventually goes stale and untrustworthy.",
        "medium", "apply", "denormalize",
        "Putting a plan in place for keeping the redundant copy refreshed on a schedule",
        ["Normalizing the denormalized copy a second time to remove its redundancy", "Deleting the denormalized copy immediately after each report is generated", "Granting every employee write access to the denormalized copy directly"],
    ),
    (
        "The lesson insists denormalization should happen \"only after a genuine, measured slowdown shows up, not because combining tables sounds slow in theory.\"\n\nWhy does this ordering matter?",
        "Normalizing first is the right default because most everyday work against a database (placing orders, updating addresses) is writes, and writes are exactly where anomalies do their damage. Denormalizing without a measured, genuine slowdown risks reintroducing anomaly-prone redundancy for a performance problem that doesn't actually exist yet.",
        "hard", "analyze", "denormalize",
        "Denormalizing without a real, measured need risks reintroducing anomaly-prone redundancy to solve a performance problem that doesn't actually exist",
        ["The ordering doesn't actually matter; denormalizing early always saves time later", "It matters only because measuring slowdowns is required by database vendor licenses", "It matters only for very large companies, not for small startups like Sunrise Traders"],
    ),
]

SYNTHESIS = [
    (
        "Priya's original combined Orders table had all three anomalies (update, insert, delete) at once, all tracing back to one root cause: a single row answering questions about a customer, a product, and an order simultaneously.\n\nWhich technique, built from functional dependencies, is the disciplined fix for this root cause?",
        "Normalization, guided by functional dependencies (which column determines which), is the disciplined, step-by-step process that splits a table so each fact lives in exactly one place, attached to the one real-world thing it actually describes.",
        "medium", "understand", "why-normalize",
        "Normalization, guided by identifying functional dependencies between columns",
        ["Denormalization, which deliberately reintroduces redundancy for speed", "Adding more indexes to the existing single table, without splitting it", "Renaming the table's columns to be more descriptive"],
    ),
    (
        "Sunrise Traders' schema goes through 1NF (atomic phone numbers), 2NF (splitting ProductName/ProductPrice out of OrderItems), and 3NF (splitting CustomerCity out of Orders).\n\nPut these three fixes in the correct order of the normal form each one addresses.",
        "1NF first (Tara's atomic PhoneNumbers fix), then 2NF (Arjun's partial dependency fix splitting Products out of OrderItems), then 3NF (Naina's transitive dependency fix splitting Customers out of Orders) — each form builds on the one before it.",
        "medium", "analyze", "second-normal-form",
        "1NF (atomic phone numbers), then 2NF (splitting Products out of OrderItems), then 3NF (splitting Customers out of Orders)",
        ["3NF first, then 2NF, then 1NF, since higher-numbered forms must be checked first", "2NF first, then 1NF, then 3NF, since composite keys must be resolved before atomicity", "All three can be checked in any order with no dependency between them"],
    ),
    (
        "Dev's Inspector -> ProductCategory dependency passed 1NF, 2NF, and 3NF but failed BCNF, because ProductCategory happened to be a prime attribute (part of the composite key).\n\nWhat general lesson does this teach about the relationship between 3NF and BCNF?",
        "A table can satisfy every rule up to and including 3NF and still contain redundancy if a dependency's determinant is not a candidate key and the dependent column happens to be prime — BCNF closes this specific gap that 3NF's prime-attribute exception leaves open.",
        "hard", "analyze", "bcnf",
        "A table can pass 3NF fully and still hide redundancy if a determinant isn't a candidate key and the dependent column is prime — exactly the gap BCNF closes",
        ["3NF and BCNF always produce identical results for every possible table", "BCNF is a weaker, less strict version of 3NF used only for legacy systems", "Passing 3NF automatically guarantees a table also passes BCNF"],
    ),
    (
        "Sunrise Traders keeps its order-taking tables (Customers, Products, Orders, OrderItems, InspectorSpecialty) fully normalized, while Vivek's separate reporting summary deliberately stores CustomerCity and ProductCategory redundantly.\n\nWhy does the lesson consider this a disciplined choice rather than backsliding into the original problem?",
        "The redundancy is chosen deliberately, for one specific, measured bottleneck (a slow report), kept clearly separate from the tables handling everyday writes, and refreshed on a schedule — unlike the original combined table, which backed into redundancy by accident with no plan to keep copies in sync.",
        "hard", "analyze", "denormalize",
        "The redundancy is deliberate, measured, kept separate from the write-critical tables, and refreshed on a schedule — unlike the original table's accidental, unmanaged redundancy",
        ["It isn't actually different; both are equally risky forms of redundancy", "It's disciplined only because the reporting summary uses a different database server", "It's disciplined only because Vivek personally reviews every report by hand"],
    ),
    (
        "Meera identifies CustomerID -> CustomerAddress as a functional dependency in Sunrise Traders' original combined table. That same dependency is exactly what caused Ilyas Bakery Supplies' address to appear inconsistently across his orders.\n\nHow does identifying functional dependencies connect to fixing the update anomaly Priya first found?",
        "Functional dependencies are the precise map of which facts belong to which real-world thing; once Meera confirms CustomerID -> CustomerAddress holds, that dependency tells the team exactly where CustomerAddress truly belongs (a Customers table keyed by CustomerID), which is the split that eliminates the repeated, drifting copies causing the update anomaly.",
        "medium", "analyze", "functional-dependencies",
        "The dependency shows CustomerAddress truly belongs in a Customers table keyed by CustomerID, and moving it there eliminates the repeated copies causing the update anomaly",
        ["Functional dependencies are unrelated to anomalies; anomalies are fixed only by adding constraints", "The dependency proves CustomerAddress should stay duplicated in every order row for performance", "Identifying the dependency deletes the anomaly automatically without any table changes"],
    ),
]

SET1_SOURCES = [
    (WHY_NORMALIZE, 0),
    (FUNCTIONAL_DEPENDENCIES, 0),
    (FIRST_NORMAL_FORM, 0),
    (SECOND_NORMAL_FORM, 0),
    (THIRD_NORMAL_FORM, 0),
    (BCNF, 0),
    (DENORMALIZE, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS[:3])

SET2 = (
    WHY_NORMALIZE[1:]
    + FUNCTIONAL_DEPENDENCIES[1:]
    + FIRST_NORMAL_FORM[1:]
    + SECOND_NORMAL_FORM[1:]
    + THIRD_NORMAL_FORM[1:]
    + BCNF[1:]
    + DENORMALIZE[1:]
    + SYNTHESIS[3:]
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


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 2.2.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 2.2.2")
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
ws.title = "DBMS - MCQ - Unit 2.2"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 2 - Database Design and Modeling/2.2 - Normalization - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
