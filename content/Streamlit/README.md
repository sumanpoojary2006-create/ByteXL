# Streamlit

**Building Web Apps From Python Scripts**

A standalone add-on course teaching Streamlit as a way to turn an existing Python script into a small, shareable web tool, no separate frontend language required. Assumes comfort with core Python (functions, dictionaries, lists, `csv`/`io`) at the level covered in the Semester 1 course, but does not depend on it directly.

## Topics (teach in order)

| # | Topic | File |
|---|-------|------|
| 1 | What is Streamlit? From Script to Web App | [01_what_is_streamlit_from_script_to_web_app.md](01_what_is_streamlit_from_script_to_web_app.md) |
| 2 | Displaying Content: Text, Markdown, and Layout Basics | [02_displaying_content_text_markdown_and_layout_basics.md](02_displaying_content_text_markdown_and_layout_basics.md) |
| 3 | Input Widgets: Capturing User Input | [03_input_widgets_capturing_user_input.md](03_input_widgets_capturing_user_input.md) |
| 4 | Session State: Making Streamlit Remember | [04_session_state_making_streamlit_remember.md](04_session_state_making_streamlit_remember.md) |
| 5 | Organizing the Page: Sidebar, Columns, and Tabs | [05_organizing_the_page_sidebar_columns_and_tabs.md](05_organizing_the_page_sidebar_columns_and_tabs.md) |
| 6 | Displaying Data: Tables, DataFrames, and Charts | [06_displaying_data_tables_dataframes_and_charts.md](06_displaying_data_tables_dataframes_and_charts.md) |
| 7 | File Uploads and Downloads | [07_file_uploads_and_downloads.md](07_file_uploads_and_downloads.md) |
| 8 | Putting It Together: A Complete Multi-Section App | [08_putting_it_together_a_complete_multisection_app.md](08_putting_it_together_a_complete_multisection_app.md) |

## How each lesson is written

Each lesson follows the house style: a standardized **Introduction** heading (no page-title H1), a story-led flow with a real-world example under natural headings, and a closing **Conclusion**. No emojis, no em dashes, no forward or backward references to other units or chapters.

**Code blocks are split into two kinds**, because Streamlit apps run via `streamlit run app.py` and render in a browser rather than printing to a terminal, which means `st.*` calls cannot be executed standalone the way the rest of this platform's Python lessons are:

- ` ```python ` blocks contain plain, runnable Python that isolates the underlying logic (filtering, aggregating, parsing CSV text, simulating what a widget's return value or a session-state dictionary would hold across reruns). Every one of these runs standalone and prints visible output, verified by executing each block in isolation.
- ` ```text ` blocks contain reference-only Streamlit code (`st.title`, `st.slider`, `st.session_state`, and so on) showing how that same logic is wired into an actual app, along with prose describing what would render on the page. These are not meant to be executed directly; `text` is a hard-coded skip language in the OneCompiler embed pipeline, so they render as plain code, not interactive editors.

Lessons follow a single recurring scenario: Kavya, a student volunteering with her college's Placement Cell, converts a plain shortlist script into a tool the (non-coding) placement coordinator can run herself, cutoff sliders and branch filters instead of edited source code, a running approved shortlist that survives every click, a sidebar and tabbed layout, a sortable results table and a branch-wise chart, and finally her own CSV upload and a downloadable shortlist. Topic 8 assembles every prior topic's pieces into that one finished app and traces a full sequence of the coordinator's clicks by hand.

MCQs and a project statement for this course are tracked separately and not yet part of this folder.

_Status: all 8 lessons authored; every runnable Python block executed and its output verified to match what's documented._
