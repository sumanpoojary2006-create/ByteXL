## Introduction

A repository history is a permanent record of why a system is the way it is. Read well, it answers questions that no document does: when did this behaviour begin, what was the reasoning, who understood this part? Read badly, it is a sequence of entries such as "fix", "update", and "more changes", from which nothing can be learned. The difference lies in how commits are made, and a little discipline in the moment produces large benefits for everyone who later searches the history.

**Definition:** A good commit is a small, self-contained, logically coherent change recorded with a clear message that explains what changed and, above all, why, so that the history of a project serves as a readable and searchable account of its evolution.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_commits_history_and_good_commit_messages.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Two commit logs side by side: left a messy log with entries fix, update, stuff, wip (red), right a tidy log with clear one-line summaries beside small icons (green). A magnifier searches the tidy log.

ON-IMAGE TEXT: show a short bold title "Commits, History and Good Commit Messages" plus only these few labels, large and legible: Atomic, Clear, Why. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Makes a Good Commit

- **Atomic:** one logical change, so it can be understood, reviewed, reverted, or moved on its own. A commit that mixes a bug fix, a rename, and a new feature is hard to review and impossible to revert cleanly.
- **Complete:** the code builds and the tests pass at each commit, so any point in history is a working state. This is essential for tools that search history for the source of a bug.
- **Focused:** no unrelated formatting changes or stray files.
- **Reviewable:** small enough for a person to understand in a few minutes.
- **Explained:** accompanied by a message that states its purpose.

A frequent habit is to **commit early and often** while working, then tidy the local history into clean logical commits before sharing, using the techniques of a later topic.

## Writing the Message

A widely followed convention, set out by Chris Beams and others, gives commit messages a simple structure.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Part</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Guideline</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Subject line</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A short summary, about 50 characters, in the imperative mood, as if giving an order: "Add coupon validation", not "Added" or "Adds"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Blank line</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separates the subject from the body</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Body (optional but valuable for non-trivial changes)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explains **what** changed and **why**, wrapped at a sensible line length. The code shows how</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Footer (optional)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">References to related issues, and notes such as breaking changes</td>
    </tr>
  </tbody>
</table>

A useful test: a subject line should complete the sentence "If applied, this commit will ..." The **why** is the most valuable part: the reason for a decision cannot be recovered from the code.

### Examples in Words

- A weak message says only "fix bug" or "updates".
- A good subject says "Reject orders with no items" and the body explains that empty orders previously caused a failure in the kitchen display, and refers to the related issue.

## Conventional Commits

Some teams adopt a more formal convention, **Conventional Commits**, in which the subject begins with a **type** and an optional scope, such as feat, fix, docs, refactor, test, or chore, followed by a short description. A note marking a **breaking change** is added where needed. Its benefits are that history is uniform and that tools can read it to generate changelogs and to decide the next version number automatically, in line with semantic versioning.

## What Not to Commit

- **Secrets:** passwords, keys, and tokens. Once committed, they remain in history and must be treated as compromised.
- **Generated files and build output,** which can be recreated.
- **Large binary files,** which bloat the repository.
- **Personal settings and temporary files.**
- **Half-finished or commented-out work** that breaks the build.

## Reading History

History is useful only if it can be explored. Common ways:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Need</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Approach</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">See recent changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">View the log, optionally condensed to one line per commit</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">See what a commit changed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show the commit and its differences</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find who last changed a line and why</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Annotate the file to show, for each line, the commit that last changed it (often called blame)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find when a behaviour began</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Search the history for changes involving a word or a line</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find which commit introduced a bug</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use bisection: mark a known good and a known bad commit, and Git guides a binary search between them, finding the culprit in a number of steps proportional to the logarithm of the number of commits</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compare two versions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show the differences between any two commits, branches, or tags</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Follow a file across renames</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">View the history of a file including moves</td>
    </tr>
  </tbody>
</table>

The usefulness of bisection and blame depends on the habits above: small, complete, well-explained commits.

## Signed Commits

For high-trust projects, commits can be **cryptographically signed**, so that others can verify that they come from the claimed author and were not altered. Hosting platforms show a verification mark for signed commits.

## Linking History to the Work

Including an **issue or ticket reference** in the message links the code change to the reason for it, and the platforms can show the connection in both directions. This supports traceability from requirement through to code, as Unit 3 described.

## Team Agreement

A team should agree on its conventions, record them in a short guide, and, where practical, support them with automation: a template for messages, checks in the pipeline that reject unclear ones, and tools that generate release notes from structured messages.

<!--
IMAGE PROMPT  ->  generate as images/02_commit_message_anatomy.png   (16:9 explanatory diagram, place here)

An annotated commit message card: Subject line (50 characters, imperative) at the top, blank line, Body explaining what and why, Footer with issue reference. Beside it a small branch of history with a bisect search narrowing from many commits to the faulty one.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Improve the Commit

1. A single commit changes the discount rules, renames twelve variables, and updates the formatting of three files. What is wrong?
2. A commit message reads: "stuff". What should it contain?
3. A developer committed a file containing a database password. What must happen?

The first mixes unrelated changes; it should be split into separate commits for the rule change, the renames, and the formatting. The second should have an imperative summary of what the change does and a body saying why. In the third case the password must be treated as compromised and changed, because removing it from the latest version does not remove it from history.

## Conclusion

A good commit is a small, self-contained, logically coherent change recorded with a clear message that explains what changed and, above all, why, so that the history of a project serves as a readable and searchable account of its evolution. A few minutes of care at commit time saves many hours later.

Commits make a history, and branches let several histories develop at once. The next topic describes branching and merging.
