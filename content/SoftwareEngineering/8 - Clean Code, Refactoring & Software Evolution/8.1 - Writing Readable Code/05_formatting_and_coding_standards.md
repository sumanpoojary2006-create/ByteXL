## Introduction

When several people write code in the same project, small differences in style accumulate: one indents with tabs and another with spaces, one puts braces on a new line and another does not, names follow different conventions. Each difference is trivial, yet together they slow reading, create noise in version control, and provoke arguments in code review. Agreed formatting and coding standards remove this friction. They are most effective when they are decided once, written down, and enforced by tools, so that nobody has to argue or remember.

**Definition:** Coding standards are the agreed rules a team follows for the layout, naming, and structure of its code, and formatting is the visual arrangement of code, which together make code consistent and predictable to read regardless of who wrote it.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_formatting_and_coding_standards.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A team of four hands each writing in a different style on one shared page, then a tidy automatic formatter machine producing a single consistent page, with a style guide book beside it.

ON-IMAGE TEXT: show a short bold title "Formatting and Coding Standards" plus only these few labels, large and legible: Agree, Automate, Consistent. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Consistency Matters

- **Faster reading:** familiar layout lets the eye find structure instantly, and the reader spends attention on meaning.
- **Smaller changes in version control:** if everybody formats the same way, the differences between versions show only real changes.
- **Fewer arguments:** style disputes are settled once by the standard.
- **Easier onboarding:** new members learn one style.
- **Fewer defects:** some rules, such as always using braces around blocks, prevent classes of mistakes.
- **Professional impression and shared ownership.**

## What Standards Cover

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Area</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples of decisions</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Layout</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Indentation width and character, line length, blank lines, placement of braces, spacing around operators</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Naming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Case styles for variables, functions, classes, constants, files</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Structure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order of items in a file, grouping of imports, maximum function and file size</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Language usage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which language features to prefer or avoid, how to handle errors, use of types</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Comments and documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When required, in what form</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where tests live and how they are named</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commit and review conventions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Message format, size of changes, review expectations</td>
    </tr>
  </tbody>
</table>

## Vertical and Horizontal Formatting

Some widely followed ideas:

- **Vertical openness:** separate distinct concepts with blank lines, as paragraphs separate ideas in prose.
- **Vertical density:** keep closely related lines together.
- **The newspaper metaphor:** a file should read like an article, with the most important, high-level ideas first and details further down.
- **Related things close together:** a function should be near the functions it calls, and variables should be declared near their first use.
- **Line length:** keep lines short enough to read without scrolling sideways, commonly between 80 and 120 characters, according to the team's standard.
- **Consistent indentation** to show structure, since the eye relies on it.

## Published Style Guides

Teams rarely invent standards from nothing. Communities and companies publish guides that can be adopted or adapted, for example the PEP 8 guide for Python, and guides published by large technology companies for several languages. Adopting a well-known guide saves time and aligns the team with the wider community. Local additions cover matters specific to the project.

## Automation: Let Tools Enforce It

Human reviewers should not spend effort on layout. Tools can do it better.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Tool</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effect</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Formatter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rewrites code automatically into the standard layout</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Eliminates layout debate; one agreed output for any input</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Linter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analyses code for rule violations and likely mistakes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flags problems early, such as unused variables or suspicious constructs</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Editor configuration files</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Share settings such as indentation across editors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everyone edits with the same basic settings</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pre-commit checks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run formatters and linters before a change is recorded</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevents non-conforming code from entering</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous integration checks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run the same checks on every change on a shared server</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Final guarantee; failing checks block merging</td>
    </tr>
  </tbody>
</table>

An automatic formatter is the most effective single measure: the style is whatever the tool produces, and no discussion is needed. Teams that adopt one find that a great deal of review time is saved.

## Adopting and Changing Standards

- **Decide as a team,** and write the standard concisely, with the reasons for non-obvious rules.
- **Favour the existing convention of the language** unless there is a strong reason.
- **Do not waste effort on personal preference.** Which style is chosen matters less than that one is chosen. Endless debate over trivial choices is sometimes called bikeshedding.
- **Introduce a formatter at a clear moment,** reformatting the whole codebase in one separate change, so that later differences are meaningful.
- **Treat the standard as living:** revisit it when it causes friction, through the normal team process.
- **Apply the standard to new code at least,** and to old code when it is touched, if wholesale reformatting is impractical.

## Limits of Standards

Standards address surface features. They cannot make poorly designed code readable, and rigid rules that ignore context can reduce clarity. Good standards leave room for judgement and are enforced with common sense, with exceptions allowed where they improve understanding.

<!--
IMAGE PROMPT  ->  generate as images/02_standards_enforced_by_tools.png   (16:9 explanatory diagram, place here)

A left-to-right flow: Developer editor with shared settings, Formatter rewriting code, Pre-commit linter check, Continuous integration check, Merge. Each gate shows a green tick or a red block. A style guide book sits above as the source of rules.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose the Remedy

1. Reviewers spend time commenting on spacing and brace placement in every change.
2. Two developers each reformat files with their own settings, and every change shows hundreds of unrelated line differences.
3. A team cannot agree whether to indent with two or four spaces and has argued for weeks.

Problem 1 is solved by an automatic formatter, so reviews focus on substance. Problem 2 is solved by shared settings and a single enforced formatter, so every file takes the same layout. Problem 3 should be settled by adopting the convention of the language or a published guide, and moving on; the choice matters far less than having one.

## Conclusion

Coding standards are the agreed rules a team follows for the layout, naming, and structure of its code, and formatting is the visual arrangement of code, which together make code consistent and predictable to read regardless of who wrote it. They work best when decided once and enforced automatically.

Readable code makes the normal path clear. The next chapter turns to what happens off the normal path, beginning with how errors should be handled.
