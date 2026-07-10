# Database Design & Modeling

**Database Management Systems**

Goal of this unit: Model real-world systems using ER diagrams, design well-structured relational schemas, and apply normalization principles to minimize redundancy and maintain data integrity.

## Chapters and Topics (teach in order)

### Entity-Relationship Modeling

| # | Topic | File |
|---|-------|------|
| 1 | Entities, Attributes, and Relationships: Modelling the Real World | [01_entities_attributes_and_relationships_modelling_th.md](Entity-Relationship%20Modeling/01_entities_attributes_and_relationships_modelling_th.md) |
| 2 | Types of Attributes: Simple, Composite, Derived, Multivalued | [02_types_of_attributes_simple_composite_derived_multi.md](Entity-Relationship%20Modeling/02_types_of_attributes_simple_composite_derived_multi.md) |
| 3 | Relationship Cardinality | [03_relationship_cardinality.md](Entity-Relationship%20Modeling/03_relationship_cardinality.md) |
| 4 | Participation Constraints | [04_participation_constraints.md](Entity-Relationship%20Modeling/04_participation_constraints.md) |
| 5 | Drawing an ER Diagram: Notation and Conventions | [05_drawing_an_er_diagram_notation_and_conventions.md](Entity-Relationship%20Modeling/05_drawing_an_er_diagram_notation_and_conventions.md) |
| 6 | Converting an ER Diagram into Relational Tables | [06_converting_an_er_diagram_into_relational_tables.md](Entity-Relationship%20Modeling/06_converting_an_er_diagram_into_relational_tables.md) |

### Normalization

| # | Topic | File |
|---|-------|------|
| 1 | Why Normalize? Update, Insert, and Delete Anomalies | [01_why_normalize_update_insert_and_delete_anomalies.md](Normalization/01_why_normalize_update_insert_and_delete_anomalies.md) |
| 2 | Functional Dependencies: The Engine Behind Normalization | [02_functional_dependencies_the_engine_behind_normaliz.md](Normalization/02_functional_dependencies_the_engine_behind_normaliz.md) |
| 3 | First Normal Form (1NF) | [03_first_normal_form.md](Normalization/03_first_normal_form.md) |
| 4 | Second Normal Form (2NF) | [04_second_normal_form.md](Normalization/04_second_normal_form.md) |
| 5 | Third Normal Form (3NF) | [05_third_normal_form.md](Normalization/05_third_normal_form.md) |
| 6 | Boyce-Codd Normal Form (BCNF) | [06_boycecodd_normal_form.md](Normalization/06_boycecodd_normal_form.md) |
| 7 | When to Denormalize: Trade-offs in Practice | [07_when_to_denormalize_tradeoffs_in_practice.md](Normalization/07_when_to_denormalize_tradeoffs_in_practice.md) |

### Practical Schema Design

| # | Topic | File |
|---|-------|------|
| 1 | Choosing the Right Data Type | [01_choosing_the_right_data_type.md](Practical%20Schema%20Design/01_choosing_the_right_data_type.md) |
| 2 | Primary Key Strategies: Integer IDs vs. UUIDs | [02_primary_key_strategies_integer_ids_vs_uuids.md](Practical%20Schema%20Design/02_primary_key_strategies_integer_ids_vs_uuids.md) |
| 3 | Naming Conventions | [03_naming_conventions.md](Practical%20Schema%20Design/03_naming_conventions.md) |
| 4 | Audit Columns and Soft Deletes | [04_audit_columns_and_soft_deletes.md](Practical%20Schema%20Design/04_audit_columns_and_soft_deletes.md) |
| 5 | Database Schemas and Namespaces | [05_database_schemas_and_namespaces.md](Practical%20Schema%20Design/05_database_schemas_and_namespaces.md) |
| 6 | Schema Design Review: Spotting Common Mistakes | [06_schema_design_review_spotting_common_mistakes.md](Practical%20Schema%20Design/06_schema_design_review_spotting_common_mistakes.md) |

Each lesson follows the house style: a standardized **Introduction** heading (no page-title H1), a story-led flow with real-world examples under natural headings, and a closing **Conclusion**. This unit precedes SQL Essentials, so schema and normalization ideas are illustrated with prose and Markdown tables of sample data rather than runnable SQL. No emojis, no em dashes, no forward or backward references to other units or chapters.

_Status: all 19 lessons authored and reviewed._
