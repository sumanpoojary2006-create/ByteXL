## Introduction

Merge conflicts have an unjustified reputation as a disaster. They are a normal, expected part of collaborative work, and they occur for a simple reason: the tool cannot decide, on its own, between two different changes to the same place. Resolving one requires human judgement about what the code should say. With a clear method, a calm approach, and good habits that make conflicts rare and small, they become routine.

**Definition:** A merge conflict occurs when two lines of development have changed the same part of a file in different ways, or when one has changed what the other has removed, so that the version control system cannot combine them automatically and a person must decide the correct result.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_resolving_merge_conflicts.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Two arrows converging on one file region, each carrying a different version, with a person at a fork choosing, combining, or rewriting, and a clean resolved file emerging labelled Resolved and tested.

ON-IMAGE TEXT: show a short bold title "Resolving Merge Conflicts" plus only these few labels, large and legible: Two versions, One decision. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Conflicts Happen

Conflicts arise when the changes on the two sides **overlap**.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Both sides edit the same lines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two developers change the same line of a pricing rule to different values</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One side edits, the other deletes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One developer changes a function while another removes the whole file</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Both sides add at the same place</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two developers add different items at the same position in a list</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A file is moved or renamed on one side and edited on the other</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A refactoring moves a file while someone else changes its contents</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large automated changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reformatting a whole file overlaps with everyone else changes to it</td>
    </tr>
  </tbody>
</table>

Conflicts are more frequent when branches live long, when many people edit the same files, and when files are large and mix several responsibilities.

## How Git Reports a Conflict

When a merge cannot be completed automatically, Git stops, marks the files in conflict, and leaves the rest of the merge ready. In each conflicted file, it inserts **conflict markers**: a start marker, the version from your side, a separator, the version from the other side, and an end marker. Everything outside the marked areas has merged cleanly. The task is to edit each marked region into the correct final text and remove the markers.

## A Method for Resolving

1. **Stay calm and look at the situation.** See which files are in conflict. Nothing is lost: both versions are preserved.
2. **Understand both changes.** Read what each side intended. The commit messages and the people involved are the best sources. Do not simply choose one side.
3. **Decide what the result should be.** It may be one side, the other, a combination, or something new that satisfies both purposes.
4. **Edit the file** to that result and remove all markers.
5. **Build and run the tests.** A conflict-free file may still be wrong, and a resolved one needs verification.
6. **Mark it resolved** and complete the merge with a commit.
7. **Talk to the other author** when the intent is unclear. A short conversation is quicker than a wrong guess.

If the situation becomes confusing, the merge can be **aborted**, returning everything to how it was before, and attempted again after preparation.

## Tools

- **Editors and IDEs** show the two sides and the common ancestor in a three-pane view, with buttons to accept either side or edit manually.
- **Merge tools** are graphical programs that present the same information.
- **The three-way view is worth using:** seeing the **original** version as well as the two changed ones makes it much clearer what each side actually did.

## Preventing Conflicts

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Practice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it helps</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrate small changes frequently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Differences stay small</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep branches short-lived</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less time to diverge</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pull from the shared main line often</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Surprises appear early, when they are small</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Divide the code into focused modules and files</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fewer people edit the same place</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Communicate about who works where</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoids simultaneous large edits to one area</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Apply an automatic formatter consistently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevents formatting-only changes colliding with real ones</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make large renames or reformatting as separate, quickly merged changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gets the disruptive change out of the way</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid editing generated or lock files by hand</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduces collisions in files that change often</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use feature flags to merge unfinished work early</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allows integration without long branches</td>
    </tr>
  </tbody>
</table>

## Semantic Conflicts

The most dangerous conflicts are those that Git does not report. Two changes that merge cleanly but contradict each other, such as one side changing the meaning of a function while the other adds new uses of the old meaning, produce broken software with no warning. The protection is **automated testing and continuous integration** on the merged result, which the build chapter describes.

## Common Mistakes

- **Accepting one side without reading,** discarding someone else work.
- **Leaving markers in the code** by accident, which breaks the build.
- **Not testing after resolving.**
- **Resolving a conflict in an area you do not understand** without consulting the author.
- **Panicking and force-overwriting,** which can destroy work.
- **Letting conflicts pile up** by delaying integration.

## Conflicts as Information

A frequent conflict in one area is a design signal: too many people need to edit the same file, which suggests it has too many responsibilities, a smell discussed in Unit 8. Recurrent conflicts are worth discussing in a retrospective.

<!--
IMAGE PROMPT  ->  generate as images/02_three_way_merge_view.png   (16:9 explanatory diagram, place here)

A three-pane view: Original (common ancestor) in the middle top, Their change on the right, Your change on the left, and a Result pane below with the combined text. Conflict markers are drawn as coloured brackets around the contested lines, and a checklist beside it reads Understand, Decide, Edit, Test, Complete.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Resolve or Prevent?

1. Two developers changed the same line of a discount rule, one to ten percent and one to twelve percent. How should the conflict be resolved?
2. A merge completes with no conflicts, but the application no longer starts. What kind of problem is this?
3. A team suffers frequent conflicts in one large file edited by everyone. What is a good response?

In case 1, do not simply pick one: find out which value is intended, by talking to the authors or the requirement, then edit the line and test. Case 2 is a semantic conflict, found only by building and testing the merged result. In case 3, split the file into focused modules, and integrate more often.

## Conclusion

A merge conflict occurs when two lines of development have changed the same part of a file in different ways, or when one has changed what the other has removed, so that the version control system cannot combine them automatically and a person must decide the correct result. Understanding both changes, deciding deliberately, and testing the result make resolution routine, and frequent small merges make conflicts rare.

So far the work has been on a single machine. The next chapter turns to sharing work through remote repositories and collaborating with teammates.
