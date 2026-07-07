# SKILL.md — The ByteXL Curriculum Authoring Skill

> Operating manual for any future AI model asked to write, extend, or repair
> content in the ByteXL workspace at `/Users/suman/Desktop/ByteXL/`.
>
> Read this file **before** touching a single `.md` under `content/`, before
> generating or editing a question workbook, and before designing an image
> prompt. The workspace already contains dozens of hand-refined,
> final-standard lessons and assessment sets; your job is to match that bar
> exactly, not to invent a new voice.
>
> **Revision note (2026-07-08).** Replaces the §3.4 "create the file in the
> same block first" rule with the `file=`/`with=` multi-file editor
> convention (see §5.9). Snippets that read, glob, or parse a file must now
> get that file from the OneCompiler EXPLORER panel via a real `file=` block,
> never by fabricating it with throwaway `open(...,"w")`/`Path.write_text()`
> setup code baked into the runnable block.
>
> **Revision note (2026-07-07).** This version incorporates the assessment
> standards agreed in the Suman/Smaran 1-1: MCQ scenario-first descriptions,
> MCQ set structure and `Python - MCQ - U.S.Q` naming, `Python - ` title
> prefixes on all questions, the confirmed 2-open/5-hidden testcase standard,
> and the new DBMS course (TOC drafted, reading materials upcoming).

---

## 1. Purpose Of This Skill

### 1.1 What this skill produces

This skill guides the creation of three families of deliverables:

1. **Reading-material lessons** (Markdown) — the per-topic `NN_slug.md` files
   inside `content/Semester 1/Unit N - .../` and `content/Semester 2/Unit N - .../`.
   These are the primary deliverable and the primary source of quality signal.
2. **Assessment items** — coding questions (Excel workbooks generated from
   Python builder scripts in `content/Question Bank/Coding Questions/_generator/`)
   and MCQs (multi-sheet Excel workbooks under `content/Question Bank/MCQ/`,
   organised into sets of 10).
3. **New courses following the Python template.** The Database Management
   Systems (DBMS) course is the first: its Table of Contents lives at
   `content/Curriculum/DBMS Curriculum - Table of Contents.md` and its
   reading materials will be authored in the same house style once the TOC
   is finalized. Any future course repeats this pattern: TOC first (mirroring
   the Python unit/topic structure), then scaffolded unit folders, then
   lessons.

Supporting artefacts the skill must respect (but rarely rewrite):

- Curriculum workbooks (`content/Curriculum/*.xlsx`) and the DBMS TOC — the
  source of truth for unit order, topic order, and topic count.
- Image prompts embedded as HTML comments in lesson files, and rendered PNGs
  under each unit's `images/` folder.
- Uploader tooling under `tools/` (Vercel apps, image converter, batch upload
  scripts) — you only touch this when explicitly asked; content authoring does
  not require it.

### 1.2 What problems this skill solves

- **Consistency at scale.** ~200 lessons across two semesters (plus the
  upcoming DBMS course) must feel written by one confident, patient teacher —
  same shape, same voice, same rhythm.
- **First-principles pedagogy for beginners.** Every lesson has to earn the
  concept with a real-world scene before it earns the syntax. Every MCQ has
  to earn the code with a one-line scenario before the question.
- **No AI-tell.** The finished lessons must not read like generic LLM output:
  no emojis, no em dashes, no "in this article we will explore", no bulleted
  summaries pretending to be prose.
- **Assessment that is provably correct and unambiguously identifiable.**
  Coding questions ship with a reference solution executed at build time to
  compute expected outputs. Every question title carries a `Python - ` prefix
  and (for MCQs) a `U.S.Q` number so the item stays identifiable even if
  platform-side tags are deleted.

### 1.3 The quality bar future outputs must clear

A new lesson is only finished when it could be dropped, unedited, next to
`content/Semester 1/Unit 1 - Introduction to Programming/01_what_is_programming.md`
and a reader could not tell which one was written first. A new question set is
only finished when it matches the current shipped workbooks (e.g.
`Unit 5 - Strings - MCQ.xlsx`), not the `.bak` versions beside them.

---

## 2. Directory Understanding

The workspace is organised into four peers plus a top-level README:

```
ByteXL/
├── README.md                    # Workspace overview (short, authoritative)
├── SKILL.md                     # This file
├── content/                     # The deliverables — every future task centres here
│   ├── Curriculum/              # Master workbooks + DBMS TOC (source of truth)
│   │   ├── Python Curriculum - Semester 1 (Fundamentals).xlsx
│   │   ├── Python Curriculum - Semester 2 (Advanced).xlsx
│   │   └── DBMS Curriculum - Table of Contents.md   # Draft awaiting finalization
│   ├── Semester 1/              # 13 units of Python Fundamentals
│   │   ├── README.md            # Semester index (unit table, style line)
│   │   └── Unit N - Title/
│   │       ├── README.md        # Unit index (topic table, character thread, status)
│   │       ├── NN_slug.md       # Per-topic lesson (the primary artefact)
│   │       └── images/          # Per-lesson PNGs, named NN_scene_slug.png
│   ├── Semester 2/              # 14 units of Advanced Python (same structure)
│   └── Question Bank/
│       ├── Coding Questions/
│       │   ├── _generator/      # Python builders (cqlib.py + unitNN_topic.py)
│       │   └── Unit N - Title/  # Shipped .xlsx (+ .xlsx.bak pre-revision backups)
│       ├── MCQ/                 # Per-unit multi-sheet MCQ .xlsx (+ .bak backups)
│       ├── Template/            # questions-mcq-template.xlsx (canonical column layout)
│       └── Review/              # Editorial review artefacts (docx + json)
├── tools/                       # Authoring, upload, and converter apps (leave alone unless asked)
│   ├── scripts/                 # scaffold_reading.py, add_image_prompts.py,
│   │                            # upload_images.py, batch_upload.py, etc.
│   ├── image-converter/         # Flask/Vercel image-to-URL app
│   ├── image-converter-extension/
│   ├── vercel-coding-question-uploader/
│   └── vercel-onecompiler-builder/
├── docs/                        # Human-facing docs (uploader walkthrough, automation notes)
└── archive/                     # Backups + regenerable build artefacts (do not edit)
```

### 2.1 Role of each file/folder

| Path | Role | Treat as |
|---|---|---|
| `README.md` (workspace) | Human orientation | Reference only; update if you materially change the shape of `content/` or `tools/`. |
| `content/Curriculum/Python Curriculum - *.xlsx` | Master Python syllabus | **Source of truth** for unit order, unit names, topic order, topic count. Never override on your own. |
| `content/Curriculum/DBMS Curriculum - Table of Contents.md` | DBMS syllabus draft | The unit/topic plan for the DBMS course, structured exactly like the Python workbooks (13 units, one-line goal per unit, topics in teaching order). Once finalized it becomes the source of truth for DBMS scaffolding and lessons. |
| `content/Semester N/README.md` | Semester index | Auto-generatable index; keep the table row-count matching the unit folders. |
| `content/Semester N/Unit K - .../README.md` | Unit charter | Sets the unit's **goal**, the **character thread** (Sem 2) or "no single host" note (some Sem 1 units), the **topic table with filenames**, and the **style reminder**. Read this before every lesson you write. |
| `content/Semester N/Unit K - .../NN_slug.md` | Final lesson | **Final output**. This is what "good" looks like. |
| `content/Semester N/Unit K - .../images/NN_*.png` | Rendered scene art | Bound to the lesson by filename prefix; you author the *prompt*, not the pixels. |
| `content/Question Bank/Coding Questions/_generator/cqlib.py` | Assessment engine | Shared library. Executes reference solutions to compute expected outputs. Do not fork the schema. **Known gap:** it does not yet add the `Python - ` title prefix (see §5.6). |
| `content/Question Bank/Coding Questions/_generator/unitNN_topic.py` | Per-unit question script | Author new questions here. One list of dicts per unit. |
| `content/Question Bank/Coding Questions/_generator/validate_all.py` | Cross-unit validator | Run before shipping a batch. |
| `content/Question Bank/Coding Questions/Unit K - .../*.xlsx` | Shipped coding sets | 30 questions, titles prefixed `Python - `. The **current standard**. |
| `content/Question Bank/MCQ/Unit K - .../*.xlsx` | Shipped MCQ sets | Multi-sheet workbook: one sheet per set of 10 (`Python - MCQ - U.S`). The **current standard**. |
| `content/Question Bank/**/*.xlsx.bak` | Pre-revision backups | The state before the 2026-07-07 naming/scenario revision. Never use as a reference; never edit; never regenerate from. |
| `content/Question Bank/Template/questions-mcq-template.xlsx` | Column layout | Canonical MCQ column order. |
| `content/Question Bank/Review/` (`mcq_review_data.json`, `MCQ Review - ... .docx`, `build_mcq_review_doc.js`) | Pre-revision editorial snapshot | **Old standard.** The JSON holds Unit 1-3 MCQs from before the 2026-07-07 revision: bare titles ("Definition of programming"), no scenario-first descriptions, placeholder taxonomy (`sample-subtopic`). Useful only to understand what the review changed. Never use as a content or format reference. |
| `content/Question Bank/Coding Questions/backup-before-taxonomy-fix/` | Historical backup | Do not use as a reference; taxonomy has moved on. |
| `tools/scripts/scaffold_reading.py` | Bootstrap | Regenerates Semester and Unit `README.md` skeletons from the curriculum xlsx. Rerun if unit order changes. Never manually resync. |
| `tools/scripts/add_image_prompts.py` | Image-prompt injector | Canonical **style prompt** + per-unit **character prompt** + per-lesson **scene**. Read this file to learn the image-prompt formula (see §5.5). |
| `tools/scripts/upload_images.py`, `batch_upload.py` | Publisher | Sends locally-authored PNGs into ByteXL and rewrites the markdown image URLs. Do not run without explicit instruction. |
| `tools/vercel-coding-question-uploader/` | Uploader app | Separate deliverable; content authoring does not touch it. |
| `docs/CODING_QUESTION_UPLOAD_AUTOMATION.md` | Ops doc | Reference only. |
| `archive/` | Backups | Read-only. Never author here. |

### 2.2 What is a "final" file vs a draft?

If it lives under `content/`, and its unit `README.md` marks it as `Status: all N lessons authored and verified.` (Semester 2 convention) or it simply exists in the current tree (Semester 1 convention), treat it as **final** and match its bar.

If two files disagree, prefer:
1. The plain `.xlsx` over its `.xlsx.bak` sibling — the `.bak` is always the older standard.
2. The lesson with rendered images referenced in the markdown (`![...](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/...)`), because it has been through the upload pipeline.
3. The shipped workbook over the generator script, where the two diverge on titles (see §5.6).
4. Never trust anything in `archive/` or `backup-before-taxonomy-fix/`.

---

## 3. Output Standards

### 3.1 Voice, tone, and register

- **Professional, warm, beginner-friendly.** The reader is an Indian
  undergraduate. Assume intelligence, not prior programming knowledge.
- **Storyteller, not textbook.** Every concept enters through a specific
  character in a specific scene doing a specific thing. Names, places, and
  props are concrete (Asha's low-battery banner, Tara's merch stall CSV,
  Kiran's twelve API endpoints).
- **British-leaning Indian English is fine.** "colour", "organise",
  "programme" are acceptable; do not switch mid-lesson.
- **Second person, present tense for instructions**; third person for
  narrative scenes.
- **Confident but never smug.** Explain the misconception, then the truth.
  Never sneer at beginners.

### 3.2 Hard formatting rules (non-negotiable)

- **No emojis. Anywhere.** Not in headings, not in prose, not in code
  comments, not in Question Bank titles.
- **No em dashes (`—`).** Use a comma, a full stop, or the word "and". This
  is the single most common AI-tell we strip out.
- **No en dashes in ranges either.** Use "3 to 10" or "3-10" (hyphen) not "3–10".
- **No H1 (`#`) at the top of a lesson.** Lessons open with `## Introduction`
  as their very first line. The unit `README.md` is the only file inside a
  unit that uses `#`.
- **`## Introduction` and `## Conclusion` are literal.** These exact headings
  bracket every lesson. Do not rename them ("Overview", "Wrap-up", "Summary"
  are all wrong).
- **No horizontal rules (`---`) inside lessons.** Section headings do the job.
- **No collapsible sections, no `<details>`, no HTML except image-prompt
  comment blocks.**
- **No trailing "further reading" section, no external links** except the S3
  image URLs that the upload pipeline writes for you.

### 3.3 The lesson skeleton (reading-material)

Every `NN_slug.md` follows this order, though internal headings vary by lesson:

```
## Introduction
(2-4 short paragraphs. Open on a named character/scene. Land on the concept
in bold: "...is the whole idea behind **programming**." or similar.)

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/...)   ← hero image, S1 style
  or
![Descriptive alt text describing the scene](images/NN_slug.png) ← S2 style, before upload

## Some Natural Heading That Names The Idea
(Prose + optionally a small code block or a 2-4 row table.)

## Another Natural Heading
(...)

## The <Concept> At A Glance
(A compact table summarising the mechanics. Very common. Not always literally
called "At A Glance" — variations: "The if Statement at a Glance", "CSV Tools
at a Glance", "Writing a Simple Decorator at a Glance".)

## Your Turn: <Concrete Micro-Task>
(A short runnable snippet or a challenge. Optional but frequent, especially
in Sem 1 lessons that introduce syntax and in all Sem 2 lessons.)

## Conclusion
(1-2 tight paragraphs. Recap in one sentence, then hand off to the next
lesson by name/topic: "...which the next unit on data types builds on
directly." Never a bulleted takeaway list.)
```

Typical size: **5,000-8,500 characters** of Markdown (roughly 800-1,400 words).
Longer than 9,000 characters is a smell; shorter than 4,500 usually means the
scene is missing.

DBMS reading materials, once the TOC is finalized, follow this identical
skeleton — SQL snippets replace Python snippets, and the "runnable as-is"
rule applies to SQL (state the assumed schema or create the table inside the
snippet).

### 3.4 Code style inside lessons

- Python 3.10+. Use `match/case` where natural (see Sem 1 Unit 3).
- Snippets should be **runnable as-is**. If a snippet reads, globs, or parses
  a file, that file must exist as a real file in the OneCompiler EXPLORER
  panel, never be fabricated with throwaway `open(...,"w")`/
  `Path.write_text()` setup code inside the runnable block itself. Use the
  `file=`/`with=` fence-info convention (see §5.9) to give a runnable block a
  real file. The only exception is when writing/creating the file *is* the
  concept the block is teaching (e.g. a `csv.writer` or `json.dump` lesson) —
  in that case the write call stays, because it is the point.
- Every non-trivial snippet is followed by an explanatory paragraph that
  names *what* line does *what* using the identifier ("`newline=""` prevents
  the `csv` module from writing extra blank lines...").
- Show output inline as a fenced block or as trailing `# comments` on
  `print(...)` lines. Both are used; pick whichever is more readable for the
  snippet.
- Keep example variable names culturally consistent (Asha, Kabir, Meera,
  Tara, Kiran, Ravi, Aisha) rather than `foo`/`bar`.

### 3.5 Table conventions

- Small (2-5 rows), tight columns, sentence-case headers.
- Use tables for **compare-and-contrast**, **at-a-glance mechanics**, and
  **common mistakes**. Do not use tables to list steps of a procedure;
  numbered lists are better for that.
- Column count is usually 2 or 3; four is the maximum before readability
  drops on ByteXL's mobile view.

### 3.6 Image conventions

- One hero image is standard, placed **immediately after the Introduction**,
  before the first non-Introduction heading.
- A lesson may have 1-3 additional inline images, each tied to a specific
  micro-concept, placed right after the paragraph that motivates them.
- **Alt text policy differs by pipeline stage**:
  - Pre-upload (local authoring in Sem 2): descriptive alt text, `![The @
    syntax shown as sugar over fn = decorator(fn)](images/03_writing_a_simple_decorator.png)`.
  - Post-upload (final Sem 1): empty alt text with S3 URL, `![](https://s3...)`.
- Every image the lesson references must have (a) a rendered PNG in the
  local `images/` folder with the same numeric prefix as the lesson, and
  (b) an image-prompt block (see §5.5) authored per the formula.

### 3.7 Naming conventions

**Files and folders**

- Lesson files: `NN_snake_case_slug.md` where `NN` is a 2-digit index
  matching the topic table in the unit `README.md`.
- Image files: `NN_short_scene_slug.png`; the `NN` matches the lesson prefix.
- Unit folders: `Unit N - Title In Title Case` (with the literal " - " and no
  colon). Matches the master workbook and the semester `README.md`.
- Coding-question workbooks: `Unit N - Title - Coding Questions.xlsx`.
- MCQ workbooks: `Unit N - Title - MCQ.xlsx`.
- Backups made before a bulk revision: append `.bak` to the workbook name and
  leave it beside the original.

**Question and sheet naming (the 2026-07-07 standard)**

- **Every question title starts with `Python - `** (with spaces around the
  hyphen), for both MCQ and coding questions. This is deliberate redundancy:
  if platform-side tags are ever deleted, the title alone still identifies
  the course. A future DBMS question bank would use `DBMS - `.
- **MCQ titles**: `Python - MCQ - U.S.Q` where `U` = unit number, `S` = set
  number, `Q` = question number within the set. Example: `Python - MCQ - 5.1.10`
  is Unit 5, Set 1, Question 10.
- **MCQ sheet (tab) names**: `Python - MCQ - U.S`, one sheet per set.
  Example workbook: `Unit 5 - Strings - MCQ.xlsx` contains sheets
  `Python - MCQ - 5.1` through `Python - MCQ - 5.4`.
- **MCQ sets contain exactly 10 questions each.** Set 1 must on its own give
  reasonable coverage of the unit's subtopics (it is the set most students
  will see first); do not front-load Set 1 with only the first subtopic.
- **Coding-question titles**: `Python - <Evocative Title>` (e.g.
  `Python - Rocket Countdown`, `Python - Canteen Bill Calculator`). The
  themed "Canteen" questions follow the same rule: `Python - Canteen ...`.

---

## 4. Workflow Instructions

Follow this order every time you author or extend curriculum content. Never
jump straight to writing prose.

### 4.1 New lesson under an existing unit

1. **Read the unit `README.md`.** It tells you:
   - The unit goal (one sentence).
   - The character thread (name, palette, setting) if this is a Sem 2 unit
     or an image-carrying Sem 1 unit.
   - The topic table with filenames — this pins the exact filename and
     topic-index for the lesson you are about to write.
2. **Read the neighbouring lessons.** At minimum: the lesson before and
   after in the same unit.
3. **Read Semester 1 / Unit 1 / lesson 01 or 09** if you are unsure about
   voice. Those two files are the workshop-quality reference.
4. **Plan the shape.** Write down (in a scratch note, not on disk):
   - Opening scene (character + situation + the one specific object).
   - The concept-landing sentence.
   - 3-6 internal section headings you will use.
   - One "At A Glance" table if applicable.
   - The "Your Turn" micro-task if applicable.
   - The hand-off sentence for the Conclusion.
5. **Draft the lesson** end to end. Do not stop mid-way.
6. **Author the image prompt** using the formula in §5.5.
7. **Self-review with the §6 checklist.**
8. **Save the file** at `content/Semester X/Unit N - .../NN_slug.md`.
9. **Do not run upload scripts** unless the user asked for it.

### 4.2 New unit (or filling in a scaffolded unit)

1. Confirm the unit exists in the curriculum workbook (Python) or the
   finalized TOC (DBMS) and in the semester `README.md` table.
2. If the unit folder is missing or its `README.md` is a stale scaffold,
   check whether `tools/scripts/scaffold_reading.py` was rerun. Do not
   hand-edit unit `README.md`s to invent topics.
3. Decide the character thread for the unit (see §5.4) and record it in the
   unit `README.md`.
4. Author lesson 01 first. It sets the scene the rest of the unit reuses.
5. Author lessons in order, referring back to earlier lessons by name.
6. Update the unit `README.md` status line to
   `_Status: all N lessons authored and verified._` only when every lesson
   passes the checklist.

### 4.3 New coding question set (per unit)

1. Read `content/Question Bank/Coding Questions/_generator/cqlib.py` end
   to end. It defines the column schema, testcase count, difficulty labels,
   and the ByteXL upload contract. Do not deviate.
2. Read the two closest existing scripts (e.g. `unit04_looping.py`,
   `unit05_strings.py`) to match tone, and open one **shipped** `.xlsx` to
   confirm the title-prefix standard.
3. Author a new `unitNN_topic.py` beside them:
   - Import `main` from `cqlib`.
   - Build a list `Q` of question dicts.
   - **10 Easy / 10 Medium / 10 Hard** unless the user specifies otherwise.
   - Medium questions should include multi-branch conditional logic where
     the unit allows it (e.g. checking both membership status and age), per
     the 2026-07-07 review standard.
   - Each question dict has: `title`, `difficulty`, `topics`, `subTopics`,
     `prose`, `input_lines`, `inputs` (list of exactly 7 stdin strings),
     `solution` (Python source as a triple-quoted string).
   - **Testcase standard: 7 total = 2 open + 5 hidden.** The open/hidden
     split is enforced by the uploader's "public testcases (first N)"
     setting, so order your `inputs` with the two simplest, most
     illustrative cases first.
   - Never author expected outputs by hand. `cqlib.run_solution` executes
     the reference solution against each input; broken solutions raise, and
     you fix the solution, not the expected output. Output normalization is
     built in (trailing whitespace stripped per line, trailing blank lines
     dropped) to match ByteXL's trailing-newline-insensitive compare, so do
     not add your own padding or strip logic.
4. **Apply the `Python - ` title prefix.** As of this revision, `cqlib.py`
   does not add it automatically and the `unitNN_*.py` scripts still carry
   bare titles, while every shipped workbook has prefixed titles. Until the
   generator is updated, either (a) write titles in the script already
   prefixed, or (b) update `cqlib.py` once to prepend the prefix centrally —
   prefer (b) if you are asked to touch the generator anyway. Never ship a
   workbook whose titles lack the prefix, and never regenerate an existing
   workbook in a way that strips it.
5. Before overwriting a shipped `.xlsx`, copy it to `<name>.xlsx.bak`.
6. Run the script from the `_generator/` directory to produce the `.xlsx`,
   then run `validate_all.py`.

### 4.4 New or revised MCQ set

The MCQ standard changed on 2026-07-07. The shipped workbooks (not the
`.bak` files, not the old Template alone) define the current format.

1. Open a current shipped workbook (e.g.
   `content/Question Bank/MCQ/Unit 5 - Strings/Unit 5 - Strings - MCQ.xlsx`)
   and the Template for the column order: `title`, `description`,
   `explanation`, `score`, `status`, `difficulty`, `bloomTaxonomy`, `tags`,
   `subjects`, `topics`, `subTopics`, `companies`, `option1`..`option4`,
   `answer`.
2. **Structure the workbook as sets.** One sheet per set of 10 questions,
   sheet named `Python - MCQ - U.S`. Four sets (40 questions) per unit is
   the current norm.
3. **Balance Set 1.** Reorder questions so the first set covers the unit's
   distinct subtopics (e.g. for Sets and Dictionaries, Set 1 must include
   set-method questions, not just definitions). Later sets deepen coverage.
4. **Title every question** `Python - MCQ - U.S.Q`, numbering within the
   sheet from 1 to 10.
5. **Open every description with a one-line scenario** that grounds the
   question in a real situation before any code appears:
   > A chat app needs to store a user's typed message exactly as entered,
   > character by character in order. What is a string in Python?
   For code-reading questions, the scenario line may be replaced by the code
   block itself only when the code *is* the scenario; prefer scenario + code.
   Never open with a bare "What is the output of the following?".
6. Match `topics`/`subTopics` vocabulary with the sibling coding-question
   workbook for the same unit so platform filters stay aligned.
7. Before overwriting a shipped workbook, copy it to `<name>.xlsx.bak`.

### 4.5 Image prompts (any lesson)

You author the prompt, not the pixels. The formula lives in
`tools/scripts/add_image_prompts.py`. See §5.5 for how to reuse it.

### 4.6 New course (the DBMS pattern)

1. **TOC first.** Draft a Table of Contents that mirrors the Python
   curriculum structure exactly: `Unit N: Title` + one-line goal + topics in
   teaching order, ~8-10 topics per unit, ~13 units per semester-length
   course, concepts-first opening units, a practical closing unit. The
   worked example is `content/Curriculum/DBMS Curriculum - Table of Contents.md`.
2. **Submit for finalization.** Do not scaffold folders or author lessons
   against a draft TOC.
3. **After sign-off:** scaffold unit folders and READMEs (adapt
   `scaffold_reading.py`), then author reading materials unit by unit under
   §4.1/§4.2 rules, in the same house style, as a single comprehensive
   ground truth.
4. Question banks for the new course adopt the same naming standard with the
   course prefix swapped (`DBMS - MCQ - U.S.Q`, `DBMS - <Title>`).

---

## 5. Reusable Patterns

### 5.1 The "situation-first" opening

Every lesson opens with a specific person doing a specific thing in a specific
place, and the concept name **only** enters after the reader has felt the
problem the concept solves.

> "It is the first day of college admissions. A single clerk sits at a desk
> while a queue of 5,000 students stretches around the building..."
> — `01_what_is_programming.md`

> "Kiran is building the library management system's API. She has twelve
> endpoint handlers, and every one needs to log its execution time."
> — `01_firstclass_functions_and_closures.md`

**Pattern to reuse.** Name a person → name the object they are looking at →
name the exact micro-frustration → in a sentence or two, name the concept in
**bold**.

The same instinct now applies to MCQs at miniature scale: the one-line
scenario is the MCQ's Introduction (see §5.8).

### 5.2 The "computer is a literal helper" primitive

Any lesson about correctness, syntax, or debugging can reach back to Sem 1
Unit 1's literal-helper metaphor without re-introducing it. Reuse this
callback rather than inventing a new metaphor.

### 5.3 The "at a glance" summary table

Between the last conceptual heading and "Your Turn" (or between "Your Turn"
and the Conclusion), most lessons drop a 3-6 row summary table titled
`## <Concept> At A Glance` or `## <Concept> Tools At A Glance`. Two-column
form is `Part | Purpose` or `Tool | Reads or Writes` or `Step | Code`.

### 5.4 The Semester 2 character-per-unit pattern

Each Sem 2 unit is anchored by a single named developer with a single
concrete backend problem (Unit 5: Kiran, 12 API endpoints needing
timing/auth/logging). The unit `README.md` states the character thread once;
every lesson refers back to that character by first name and their specific
project. When you add a new unit, pick one character and one anchoring
problem and hold both across all lessons. Do not swap mid-unit.

### 5.5 Image-prompt formula (canonical)

The prompt formula, extracted from `tools/scripts/add_image_prompts.py`, has
four fixed slots plus one per-lesson slot:

1. **Format line.** `16:9 cinematic hero image, place here, right after the
   Introduction`.
2. **CHARACTER & THEME block.** For Sem 2 and image-carrying Sem 1 units:
   a locked description of the recurring character (age, hair, outfit,
   palette, prop). Repeat verbatim in every lesson of the unit. For units
   without a recurring host, say so explicitly and describe a distinct
   ordinary Indian person per lesson.
3. **STYLE block (never modify).** Verbatim from `add_image_prompts.py`:
   > STYLE: world-class high-end 3D RENDER, cinematic and vibrant, the
   > quality of a top animation studio or an award-winning CGI key visual.
   > Glossy, soft 3D forms with physically based materials, global
   > illumination, soft contact shadows, gentle ambient occlusion, subtle
   > reflections, rim light and bloom, and a shallow depth of field.
   > Dynamic three-quarter hero camera angle with real depth, scale, and a
   > sense of motion. Premium, playful, and polished. Explicitly NOT a flat
   > vector diagram and NOT a textbook illustration. Use a vivid green
   > accent for positive or yes outcomes and a vivid red accent for
   > negative or no outcomes, on a soft studio-gradient backdrop with a
   > glowing focal element. Ultra-detailed, 4k, crisp.
4. **SCENE block.** One or two sentences describing the specific micro-moment
   the image should render. Must map 1:1 to a scene actually present in the
   lesson.
5. **ON-IMAGE TEXT block.** A short bold title + at most three or four
   legible labels. No sentences on the image.

### 5.6 Coding-question anatomy

From `cqlib.py` and the shipped workbooks:

- Fixed schema of 34 columns (17 metadata columns, 14 testcase
  input/output columns, then `preloadCode_python`, `solution_python`,
  `hints`); do not add or remove. The exact order is the `HEADERS` list in
  `cqlib.py`.
- `NUM_TESTCASES = 7`: **2 open + 5 hidden** (the confirmed platform
  standard; the split is applied by the uploader's "public testcases"
  setting, so the two most illustrative inputs go first).
- Difficulty is exactly one of `Easy`, `Medium`, `Hard`; batches are
  10/10/10.
- Titles are `Python - <Evocative Title>` (2-4 words after the prefix,
  Title Case): `Python - Rocket Countdown`, `Python - Canteen Bill Calculator`.
  **Divergence alert:** the `_generator/unitNN_*.py` scripts predate the
  prefix and still contain bare titles; the shipped `.xlsx` files are the
  standard. Reconcile toward the prefix whenever you touch either side.
- Description is auto-assembled from `prose`, `input_lines`, sample output,
  and `DEFAULT_CONSTRAINTS`: prose paragraph → `### Input Format` bullets →
  `### Output Format` fenced block → `### Constraints` bullets.
- Reference `solution` is minimal, idiomatic Python using only the language
  features already taught by that unit's position in the syllabus (the
  `unit04_looping.py` docstring's "scope lock" is the model).
- Medium questions should exercise multiple conditional branches when the
  unit's scope allows.
- Taxonomy fields (`topics`, `subTopics`) must match the MCQ workbook and
  the reading-material unit README.

### 5.7 Question prose style

- Every problem opens with a real-world framing (`"A fitness app adds up a
  running total from day 1 to day N."`), not abstract math.
- The task sentence starts with a concrete verb: "Read N and print..."
- `input_lines` are 1-2 bullet-like strings describing each input line by
  purpose, not by variable name.
- Evocative not academic titles: `Rocket Countdown`, `Cash Register Total`,
  `Factorial Machine` (all now carrying the `Python - ` prefix).

### 5.8 MCQ anatomy (the 2026-07-07 standard)

- **Workbook:** `Unit N - Title - MCQ.xlsx`, one sheet per set.
- **Sheet names:** `Python - MCQ - U.S` (e.g. `Python - MCQ - 5.3`).
- **10 questions per sheet**, titled `Python - MCQ - U.S.Q` in order.
- **Set 1 is the coverage set:** its 10 questions must span the unit's
  subtopics, not just the first lessons.
- **Description = scenario + question (+ code).** The first line is a
  one-sentence real-world scenario that explains why anyone would care about
  the code's logic; then the code block (fenced, ` ```python `), then the
  question sentence ("What is printed?"). Scenario style matches the
  reading-material openers in miniature: an app, a person, a concrete need.
- **Four options** (`option1`..`option4`), one `answer`, an `explanation`
  that teaches (why the right one is right *and* why the tempting wrong one
  is wrong), and `difficulty`/`bloomTaxonomy`/`topics`/`subTopics` filled in.
- Blank `bloomTaxonomy` is treated as `apply` by the uploader and flagged as
  a warning; fill it explicitly.

### 5.9 Multi-file editor embeddings (`file=`/`with=`)

When a lesson's runnable snippet needs to read, glob, or parse a file that
was not just written earlier in the same block, give the OneCompiler embed a
real second file instead of fabricating one with `open(...,"w")` or
`Path.write_text()` inline. Two fence-info attributes drive this, parsed by
`tools/vercel-onecompiler-builder/app.js`:

- **`file=<name>`** on a fenced code block marks it as a *file definition*,
  not a runnable snippet. `<name>` may include a subfolder
  (`reports/day1_sales.txt`). The converter never turns this block into its
  own iframe; it renders as a plain fenced code block in the output markdown
  so the reader still sees the file's contents inline, and its content is
  registered for `with=` blocks to pull in.
- **`with=<name1>,<name2>`** on a normal runnable fence pulls one or more
  previously-defined `file=` blocks into that embed's EXPLORER as extra
  files, alongside the main runnable script. The main script always stays
  file 0 (the active tab); the `with=` files load beside it.

A `file=` definition can be referenced by any `with=` block anywhere later
in the same lesson file, so a fixture used by five different examples (e.g.
`attendees.txt` across several blocks in one lesson) is defined once and
reused, not re-fabricated per block. A `with=` name with no matching `file=`
definition earlier in the file is dropped from that embed and reported as a
build-time warning in `onecompiler-report.md`, so a typo fails loudly instead
of shipping a half-populated editor.

Example, replacing the old fabricate-then-import pattern:

````
```python file=billing.py
def split_cost(total, people, service_charge=0):
    return (total + service_charge) / people
```

```python with=billing.py
import billing

mess_share = billing.split_cost(1200, 4)
print("Each person owes:", mess_share)
```
````

Use this any time a snippet's whole point is consuming a file (reading,
`glob`-ing, `csv.reader`/`DictReader`, `json.load`) rather than creating one.
Leave file-creation code alone when writing *is* the lesson.

---

## 6. Quality Control Checklist

Before declaring any output complete, tick every box. Do not paraphrase this
list; work through it literally.

### 6.1 Every reading-material lesson

- [ ] File is named `NN_snake_case.md`, `NN` matches the unit README topic table.
- [ ] First line of the file is `## Introduction`. No H1. No frontmatter.
- [ ] Opens with a specific character + specific scene + specific object.
- [ ] The concept name lands in **bold** by the end of the Introduction.
- [ ] Hero image is placed immediately after the Introduction; filename
      prefix matches the lesson.
- [ ] No emojis anywhere in the file.
- [ ] No em dashes (`—`). Grep the file to be sure.
- [ ] No horizontal rules (`---`) inside the lesson body.
- [ ] Section headings are natural English phrases, not textbook labels.
- [ ] Every code block is runnable as-is, or the prose explicitly warns
      it is a snippet.
- [ ] If a table appears, it is 2-4 columns, sentence-case headers, 2-6 rows.
- [ ] "At a Glance" summary table is present when the lesson introduces
      multiple named mechanics.
- [ ] "Your Turn" is present when the lesson introduces syntax or a new
      construct.
- [ ] Ends with `## Conclusion` (exact heading), one or two prose paragraphs,
      final sentence names the *next* lesson's topic to hand off.
- [ ] No bulleted "key takeaways" list in the Conclusion.
- [ ] Character names, palettes, and settings are consistent with the unit's
      character thread.
- [ ] File size roughly 5-8.5 KB of Markdown, i.e. 800-1,400 words.
- [ ] Image prompt follows the 5-slot formula in §5.5, STYLE block verbatim.

### 6.2 Every coding question

- [ ] Uses `cqlib.main`; does not hand-roll the xlsx schema.
- [ ] Exactly 7 testcases, ordered so the first 2 are the open ones (simple,
      illustrative), the remaining 5 the hidden ones (edge cases, scale).
- [ ] Reference `solution` uses only language features taught by that unit
      or earlier in the syllabus.
- [ ] Reference `solution` runs cleanly under `run_solution` (the build
      script did not raise).
- [ ] Difficulty is one of `Easy`, `Medium`, `Hard`; batch is 10/10/10.
- [ ] Medium questions include multi-branch conditional logic where the
      unit's scope allows.
- [ ] **Title starts with `Python - `** and the rest is 2-4 evocative
      Title-Case words. Canteen-themed questions read `Python - Canteen ...`.
- [ ] `topics` and `subTopics` match the taxonomy already in use for that unit.
- [ ] `prose` opens with a real-world framing sentence.
- [ ] `input_lines` describe each input line by purpose.
- [ ] Shipped workbook was backed up to `.xlsx.bak` before overwrite.
- [ ] `validate_all.py` passes after the batch is written.

### 6.3 Every MCQ set

- [ ] Workbook named `Unit N - Title - MCQ.xlsx`; one sheet per set.
- [ ] Sheet names are exactly `Python - MCQ - U.S`.
- [ ] Each sheet has exactly 10 questions, titled `Python - MCQ - U.S.Q`
      with `Q` running 1-10 in row order.
- [ ] Set 1 covers the unit's distinct subtopics (spot-check: do set
      methods / the unit's later lessons appear in Set 1?).
- [ ] Every description opens with a one-line real-world scenario before
      the code and the question.
- [ ] Code in descriptions is fenced with ` ```python `.
- [ ] Four options, one answer, and an explanation that addresses the most
      tempting distractor.
- [ ] `bloomTaxonomy` is filled (never left blank).
- [ ] `topics`/`subTopics` align with the sibling coding-question workbook.
- [ ] Column order matches `Template/questions-mcq-template.xlsx`.
- [ ] Previous shipped workbook preserved as `.xlsx.bak`.

### 6.4 Every unit README

- [ ] `# Unit N: Title` on line 1.
- [ ] `**Semester N: Semester Name**` on line 3.
- [ ] One-line unit goal.
- [ ] Character thread paragraph (Sem 2) or omitted (Sem 1 units that use
      per-lesson characters).
- [ ] Topic table with exact filenames as clickable links.
- [ ] Final line either the style reminder (Sem 1) or the
      `_Status: all N lessons authored and verified._` marker (Sem 2), not
      both.

### 6.5 Every course TOC (DBMS pattern)

- [ ] `Unit N: Title` + one-line goal + numbered topics in teaching order.
- [ ] ~8-10 topics per unit; unit count and total topic count in the same
      band as Python Semester 1 (13 units, ~100 topics).
- [ ] Concepts-first opening units before any syntax; practical closing unit.
- [ ] Summary table with per-unit topic counts at the end.
- [ ] Notes-for-finalization section flagging judgment calls.
- [ ] Marked as draft until explicitly finalized; no scaffolding before
      sign-off.

---

## 7. Do's and Don'ts

### 7.1 Always do

- Open every lesson with a person, a place, and a specific object.
- Open every MCQ description with a one-line scenario.
- Write `## Introduction` and `## Conclusion` as literal, exact headings.
- Bold the concept name the first time it is defined.
- Prefix every question title with the course name: `Python - ` (later
  `DBMS - `).
- Number MCQs `U.S.Q` and name MCQ sheets `Python - MCQ - U.S`.
- Keep 10 questions per MCQ set, with Set 1 spanning the unit's subtopics.
- Use 7 testcases per coding question, the first 2 being the open ones.
- Back up a shipped workbook to `.xlsx.bak` before overwriting it.
- Use small tables for compare-and-contrast and at-a-glance mechanics.
- Include a runnable "Your Turn" whenever a lesson introduces syntax.
- Hand off in the Conclusion by naming the next lesson's topic.
- For coding questions, let `cqlib` compute expected outputs by executing
  your reference solution.
- Read the unit README and both neighbouring lessons before writing.
- Reuse the exact character, palette, and setting the unit locks in.

### 7.2 Never do

- **Never** use emojis anywhere in `content/`.
- **Never** use em dashes; use commas or "and" or full stops.
- **Never** start a lesson with `# Title` or with frontmatter.
- **Never** rename `## Introduction` or `## Conclusion`.
- **Never** end a lesson with a bulleted "key takeaways" list.
- **Never** open an MCQ with a bare "What is the output of the following?".
- **Never** ship a question whose title lacks the `Python - ` prefix, and
  never regenerate a workbook in a way that strips existing prefixes.
- **Never** hand-author expected outputs for coding questions.
- **Never** use a `.bak` workbook or `backup-before-taxonomy-fix/` as a
  style reference; they encode superseded standards.
- **Never** invent a new unit, topic, or ordering not present in the
  curriculum workbook or finalized TOC.
- **Never** scaffold or author lessons for a course whose TOC is still a
  draft awaiting finalization.
- **Never** edit files in `archive/`.
- **Never** run `tools/scripts/upload_*.py` or the Vercel apps' deploy
  commands unless the user explicitly asks.
- **Never** paste JWT tokens, API keys, or the `bytexl_config.json` contents
  into a lesson, workbook, or PR body.
- **Never** introduce a new voice, palette, or character mid-unit.
- **Never** produce a lesson under 4,500 characters — it will be shallow by
  construction.

---

## 8. Examples And References

Use these files as canonical patterns. Read them, do not copy them.

### 8.1 The workshop-quality reference lessons

- `content/Semester 1/Unit 1 - Introduction to Programming/01_what_is_programming.md`
  — The gold-standard opening: fee-receipt scene, literal-helper metaphor,
  "using vs writing software" table, six-line Conclusion pattern.
- `content/Semester 1/Unit 1 - Introduction to Programming/09_setting_up_python_first_program.md`
  — Introducing code without losing the story: two-doors metaphor, first
  program, "little mistakes" table.
- `content/Semester 1/Unit 3 - Control Flow/02_the_if_statement.md`
  — A syntax lesson: Asha's low-battery banner, "at a glance" table,
  "Your Turn" micro-task.
- `content/Semester 1/Unit 11 - File Handling/07_reading_and_writing_csv_files.md`
  — A heavier-code Sem 1 lesson: self-contained runnable examples,
  reader/writer/DictReader/DictWriter progression.
- `content/Semester 2/Unit 5 - Decorators/01_firstclass_functions_and_closures.md`
  and `03_writing_a_simple_decorator.md`
  — Sem 2 opening and mechanics lessons: Kiran's twelve endpoints,
  descriptive alt text, step-code "at a glance" table.

### 8.2 The assessment references

- `content/Question Bank/Coding Questions/_generator/cqlib.py` — the schema
  and the run-solution contract. Non-negotiable (but see the title-prefix
  divergence note in §5.6).
- `content/Question Bank/Coding Questions/_generator/unit04_looping.py` —
  the 10/10/10 structure, scope-lock docstring, and question-prose style.
- `content/Question Bank/Coding Questions/Unit 4 - Looping/Unit 4 - Looping - Coding Questions.xlsx`
  — a shipped coding set with the current `Python - ` titles.
- `content/Question Bank/MCQ/Unit 5 - Strings/Unit 5 - Strings - MCQ.xlsx`
  — the canonical current MCQ workbook: four `Python - MCQ - 5.S` sheets,
  10 scenario-first questions each, `Python - MCQ - 5.S.Q` titles.
- `content/Question Bank/Template/questions-mcq-template.xlsx` — MCQ column
  order.

### 8.3 The curriculum/TOC references

- `content/Curriculum/Python Curriculum - Semester 1 (Fundamentals).xlsx`,
  sheet "Curriculum (Unit-Topic)" — the unit/topic layout every course TOC
  mirrors.
- `content/Curriculum/DBMS Curriculum - Table of Contents.md` — the worked
  example of a new-course TOC in that layout (draft; awaiting finalization).

### 8.4 The tooling references

- `tools/scripts/add_image_prompts.py` — the STYLE block (verbatim), the
  per-unit CHARACTER blocks, and the SCENE + ON-IMAGE TEXT data structure.
- `tools/scripts/scaffold_reading.py` — the unit `README.md` skeleton wording
  and the semester index table format.

---

## 9. Operating Notes For Future Models

- **Default working directory:** treat `/Users/suman/Desktop/ByteXL/` as the
  workspace root. All `CONTENT_ROOT`s in the scripts resolve to
  `<root>/content/`.
- **Read before you write.** For any lesson task, the minimum read set is:
  the unit `README.md`, the two neighbouring lessons, and Sem 1 / Unit 1 /
  lesson 01. For any question task, the minimum read set is `cqlib.py` (or
  the MCQ Template) plus one **currently shipped** workbook — never a `.bak`.
- **Never delegate voice.** If you spawn a subagent to draft prose, review
  every sentence yourself against §3.1 and §7 before saving. Subagents
  routinely produce emojis and em dashes when unattended.
- **Stop conditions.** A lesson is done only when §6.1 is fully ticked. A
  coding set is done only when §6.2 is ticked and `validate_all.py` passes.
  An MCQ set is done only when §6.3 is ticked.
- **Never touch the pipeline on your own.** The uploader scripts talk to
  ByteXL production and image hosting. Do not run `upload_images.py`,
  `batch_upload.py`, `upload_onecompiler_embeds.py`, or the Vercel deploy
  commands without an explicit instruction naming the exact script.
- **Known divergences to reconcile when touched:**
  - Generator scripts (`unitNN_*.py`) carry bare titles; shipped workbooks
    carry `Python - ` prefixes. The prefix wins.
  - `Semester 2/` contains both `Unit 14 - Packaging and Distribution` and
    `Unit 14 - Packaging, Project Structure, and Distribution`. The semester
    README's unit table points to `Unit 14 - Packaging and Distribution`
    (6 topics), so that folder is the live one; treat the
    `Packaging, Project Structure, and Distribution` folder (4 lessons, no
    images) as a superseded draft until it is explicitly reconciled.
- **When something disagrees with this file.** If a shipped artefact in
  `content/` clearly contradicts this document but is otherwise final and
  polished, treat the artefact as the newer truth, update this SKILL.md to
  match, and note the change in the top-level `README.md`. If a scaffold,
  `.bak`, or archive file disagrees, ignore the disagreement.
