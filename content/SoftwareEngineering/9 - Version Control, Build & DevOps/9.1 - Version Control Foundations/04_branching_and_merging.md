## Introduction

Software teams rarely work on one thing at a time. A developer is fixing a defect, another is adding a feature that will take two weeks, a third is trying an experiment that may be abandoned. If all of them changed the same line of code, the main version would be unstable and progress would collide. Branching gives each line of work its own space, and merging brings the results back together. Because Git makes branches nearly free, the whole way teams work has been shaped around them.

**Definition:** Branching is creating an independent line of development from a point in history so that work can proceed in isolation, and merging is combining the changes of one line of development into another, integrating separate work into a single history.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_branching_and_merging.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A main line of commits with a feature line splitting off from it and later rejoining through a merge commit with two parent arrows, plus a second small branch that is abandoned and fades out.

ON-IMAGE TEXT: show a short bold title "Branching and Merging" plus only these few labels, large and legible: Diverge, Work, Combine. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Branch

- **Isolation:** unfinished work does not disturb the stable code or other people.
- **Parallel work:** several tasks proceed at once.
- **Safe experiments:** an idea can be tried and thrown away at no cost.
- **Review:** a branch gathers one body of work that can be examined as a unit before it is accepted.
- **Releases and fixes:** a version in production can be repaired without taking in unfinished features.

## Creating and Using Branches

A branch is created from a starting commit, normally the latest on the main line. Work then proceeds with commits on the new branch, and the main line is unaffected. At any time, a developer can switch between branches and the working files change to match.

Good practice for branches:

- **Use descriptive names,** often with a prefix showing the kind of work and a reference to the task, such as feature, fix, or experiment, followed by a short description.
- **Keep them short-lived,** days and not weeks, since the longer a branch lives, the further it drifts and the harder it is to merge.
- **Keep each to a single purpose.**
- **Update them regularly** with changes from the main line, to avoid surprises.
- **Delete them after merging,** since the history is preserved without the label.

## Merging

Merging takes the changes made on one branch and applies them to another. Git looks for the **merge base**, the most recent commit common to both branches, and combines the changes made on each side since then.

### Fast-Forward Merge

If the target branch has not changed since the branch was created, its label simply moves forward to the branch tip. The history stays a straight line, and no new commit is created.

### Three-Way Merge

If both branches have moved on, Git combines the two sets of changes, using the common ancestor as a reference, and creates a **merge commit** with two parents, recording the point where the lines of work came together. If the two sides changed the same lines differently, a **conflict** arises, which the next topic covers.

### Squash Merge

A **squash merge** combines all the commits of a branch into a single new commit on the target branch, giving a tidy linear main history at the cost of losing the detailed steps of the branch.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Style</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">History shape</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantage</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantage</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast-forward</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Straight line</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simplest, no extra commit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only possible when the target has not changed; loses visible branch structure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Merge commit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Branches visible, with merge points</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preserves the true history of how work developed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">History can become busy and hard to read</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Squash merge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One commit per branch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clean, readable main history; easy to revert a whole feature</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Loses detail of individual steps; authorship detail is compressed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rebase then fast-forward</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Straight line, with the individual commits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Linear and detailed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rewrites the branch commits; see the history rewriting topic</td>
    </tr>
  </tbody>
</table>

Teams choose a style and apply it consistently.

## What Merging Cannot Do

A merge combines changes **textually**, and a clean merge does not guarantee that the result works. Two developers may change different parts of the code in ways that are individually correct and jointly broken, for example one renames a function while the other adds a new call to the old name. This is called a **semantic conflict**, and it is caught only by building and testing the merged result, which is why automated tests on every change are essential.

## Keeping Integration Healthy

- **Integrate often.** Small, frequent merges are easier than large, rare ones.
- **Merge the main line into your branch regularly,** so differences stay small, or rebase on it.
- **Run the tests after a merge,** not just before.
- **Review before merging,** the topic of the pull request workflow.
- **Avoid long-lived branches** that diverge from the main line.

## Visualising

Graph views of history, offered by tools and by the log operation, show branches as lines that split and join. Learning to read them builds intuition: each commit points to its parent, and each branch is a label on one of the commits.

<!--
IMAGE PROMPT  ->  generate as images/02_fast_forward_merge_commit_squash.png   (16:9 explanatory diagram, place here)

Three small commit graphs. Fast-forward: the main label slides forward along a straight line. Merge commit: two lines joining at a commit with two parents. Squash: the feature commits collapse into one new commit on main. Each labelled with its history shape.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Merge?

1. The main line has not changed since a developer created a branch for a small fix.
2. Both the main line and a feature branch have received new commits since they diverged.
3. A team wants each feature to appear in main history as a single commit that is easy to revert.

Case 1 allows a fast-forward merge. Case 2 needs a three-way merge, producing a merge commit. Case 3 suits a squash merge.

## Conclusion

Branching is creating an independent line of development from a point in history so that work can proceed in isolation, and merging is combining the changes of one line of development into another, integrating separate work into a single history. Cheap branches and frequent, tested merges let teams work in parallel without chaos.

Merging is straightforward until two people have changed the same thing. The next topic describes how to resolve merge conflicts.
