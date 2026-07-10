# Performance

**Database Management Systems**

Goal of this unit: Improve database performance through indexing and query optimization techniques.

## Chapters and Topics (teach in order)

### Storage and File Organization

| # | Topic | File |
|---|-------|------|
| 1 | How Data Is Stored? | [01_how_data_is_stored.md](7.1%20-%20Storage%20and%20File%20Organization/01_how_data_is_stored.md) |
| 2 | File Organization: Heap, Sorted, and Hashed Files | [02_file_organization_heap_sorted_and_hashed_files.md](7.1%20-%20Storage%20and%20File%20Organization/02_file_organization_heap_sorted_and_hashed_files.md) |
| 3 | Why Storage Layout Affects Query Speed | [03_why_storage_layout_affects_query_speed.md](7.1%20-%20Storage%20and%20File%20Organization/03_why_storage_layout_affects_query_speed.md) |

### Indexes

| # | Topic | File |
|---|-------|------|
| 1 | What is an Index? | [01_what_is_an_index.md](7.2%20-%20Indexes/01_what_is_an_index.md) |
| 2 | B-Tree Indexes | [02_btree_indexes.md](7.2%20-%20Indexes/02_btree_indexes.md) |
| 3 | Hash, Composite, Partial, and Expression Indexes | [03_hash_composite_partial_and_expression_indexes.md](7.2%20-%20Indexes/03_hash_composite_partial_and_expression_indexes.md) |
| 4 | Covering Indexes and Index-Only Scans | [04_covering_indexes_and_indexonly_scans.md](7.2%20-%20Indexes/04_covering_indexes_and_indexonly_scans.md) |
| 5 | When Not to Index: The Cost of Over-Indexing | [05_when_not_to_index_the_cost_of_overindexing.md](7.2%20-%20Indexes/05_when_not_to_index_the_cost_of_overindexing.md) |

### Query Optimization

| # | Topic | File |
|---|-------|------|
| 1 | Inside the Query Optimizer | [01_inside_the_query_optimizer.md](7.3%20-%20Query%20Optimization/01_inside_the_query_optimizer.md) |
| 2 | Reading EXPLAIN | [02_reading_explain.md](7.3%20-%20Query%20Optimization/02_reading_explain.md) |
| 3 | Reading EXPLAIN ANALYZE | [03_reading_explain_analyze.md](7.3%20-%20Query%20Optimization/03_reading_explain_analyze.md) |
| 4 | Join Algorithms | [04_join_algorithms.md](7.3%20-%20Query%20Optimization/04_join_algorithms.md) |
| 5 | Common Bottlenecks: Missing Indexes, N+1 Queries, Large Scans | [05_common_bottlenecks_missing_indexes_n1_queries_larg.md](7.3%20-%20Query%20Optimization/05_common_bottlenecks_missing_indexes_n1_queries_larg.md) |
| 6 | Iterative Performance Tuning: Measure, Change, Re-measure | [06_iterative_performance_tuning_measure_change_remeas.md](7.3%20-%20Query%20Optimization/06_iterative_performance_tuning_measure_change_remeas.md) |

Each lesson follows the house style: a standardized **Introduction** heading (no page-title H1), a story-led flow with real-world examples under natural headings, runnable SQL examples embedded via OneCompiler, and a closing **Conclusion**. No emojis, no em dashes, no forward or backward references to other units or chapters.

_Status: all 14 lessons authored and reviewed._
