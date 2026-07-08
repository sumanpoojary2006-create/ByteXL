# Unit 2: The Relational Model

**Database Management Systems**

See all data as tables, and learn the rules that keep those tables trustworthy.

## Topics (teach in order)

| # | Topic | File |
|---|-------|------|
| 1 | Tables, Rows, and Columns: The Shape of Relational Data | [01_tables_rows_and_columns.md](01_tables_rows_and_columns.md) |
| 2 | Domains and Data Types: What a Column is Allowed to Hold | [02_domains_and_data_types.md](02_domains_and_data_types.md) |
| 3 | Keys: Candidate, Primary, and Composite | [03_keys_candidate_primary_and_composite.md](03_keys_candidate_primary_and_composite.md) |
| 4 | Foreign Keys: How Tables Point to Each Other | [04_foreign_keys.md](04_foreign_keys.md) |
| 5 | Relationships: One-to-One, One-to-Many, Many-to-Many | [05_relationships.md](05_relationships.md) |
| 6 | Integrity Rules: Entity Integrity and Referential Integrity | [06_integrity_rules.md](06_integrity_rules.md) |
| 7 | Constraints: NOT NULL, UNIQUE, DEFAULT, CHECK | [07_constraints.md](07_constraints.md) |
| 8 | Reading a Schema: From a Diagram to Real Tables | [08_reading_a_schema.md](08_reading_a_schema.md) |

## How each lesson is written

Each lesson follows the house style: a standardized **Introduction** heading (no page-title H1), a story-led flow with real-world examples and situation-based questions under natural headings, and a closing **Conclusion**. No emojis, no em dashes.

This unit is still entirely on paper. Constraint and key names (PRIMARY KEY, NOT NULL, and the rest) are introduced here as vocabulary and design rules, sketched as tables on paper, exactly the way Unit 1 of the Python course introduced pseudocode before any real syntax. No runnable SQL appears until Unit 3, where these same ideas get their first `CREATE TABLE` statement.

Lessons continue Devika's thread from Unit 1: her library's three spreadsheet files are redrawn as proper tables, each column is given a strict domain, each table is given a primary key, loans are linked back to books and members with foreign keys, the shape of those links is named precisely, two integrity rules are stated once and for all, a handful of constraints close the remaining loopholes, and the unit ends by reading one complete schema diagram end to end, the exact diagram Unit 3 will finally build for real.

_Status: lesson content authored for all 8 topics._
