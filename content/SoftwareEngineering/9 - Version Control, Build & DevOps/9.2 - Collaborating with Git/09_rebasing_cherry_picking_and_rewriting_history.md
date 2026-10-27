## Introduction

Git makes it possible to change history, not just add to it: to tidy a messy series of commits, to move work onto a newer base, to copy a single fix to another branch, or to undo a mistake. These capabilities are powerful and, used on the right history, make a project record cleaner. Used on history that others rely on, they can cause confusion and lost work. The topic is therefore as much about **when not to** rewrite as about how.

**Definition:** Rewriting history is the practice of changing commits that already exist, by rebasing them onto a new base, combining or editing them, or copying individual commits elsewhere, to produce a cleaner or more suitable record, and it must be limited to history that has not yet been shared with others.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_rebasing_cherry_picking_and_rewriting_history.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a feature branch of three commits being lifted and replayed onto the tip of main as three new copies. Middle: one commit being copied across to another branch. Right: a safety net labelled reflog under a tightrope.

ON-IMAGE TEXT: show a short bold title "Rebasing, Cherry-Picking and Rewriting History" plus only these few labels, large and legible: Replay, Copy, Undo. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Golden Rule

**Never rewrite history that other people may already have.** Rewriting creates new commits with new identifiers to replace old ones. Anyone who based their work on the old commits finds that their history no longer matches the shared one, and repairing it is difficult and error-prone. Rewrite only commits that exist **solely in your own local repository** or on a personal branch that nobody else uses.

## Rebasing

**Rebase** takes the commits of a branch and **replays them, one by one, on top of a different starting point**, usually the latest commit of the main line. The result is that the branch looks as if it had been started from the newest state of main.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Merge</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rebase</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Action</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combines two lines with a merge commit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replays your commits onto the new base</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">History shape</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Branching history, true to what happened</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Straight line, as if work had been done in sequence</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Existing commits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unchanged</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replaced by new copies with new identifiers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conflicts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resolved once, at the merge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">May need resolving at each replayed commit</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safety</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safe for shared branches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only for unshared commits</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Traceability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shows when branches joined</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hides the fact that work happened in parallel</td>
    </tr>
  </tbody>
</table>

Rebasing is commonly used to **update a feature branch** with the latest main line before review, producing a clean, linear history.

## Interactive Rebase

An interactive rebase lets you edit a sequence of your own recent commits as a list, applying instructions to each.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Instruction</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effect</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pick</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the commit as it is</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reword</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the changes but edit the message</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Edit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pause to change the commit contents</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Squash (or fixup)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combine the commit with the previous one, joining their messages (or discarding the later message)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reorder</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change the order of the commits</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Drop</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove the commit entirely</td>
    </tr>
  </tbody>
</table>

A typical use: after working with many small, messy commits, such as "wip" and "oops, fix typo," a developer squashes them into a few clean logical commits before opening a pull request. This is the method behind the habit of committing frequently and tidying before sharing.

## Amending

The **amend** option replaces the most recent commit, adding forgotten changes or correcting its message. It is a small rewrite and subject to the same rule: not after the commit has been pushed and used by others.

## Cherry-Picking

**Cherry-pick** copies a **single commit**, or a few chosen ones, from one branch onto another, creating a new commit with the same changes. Typical uses are:

- **Back-porting a fix:** a bug fixed on the main line must also be applied to an older release branch.
- **Recovering one useful commit** from an abandoned branch.
- **Moving a commit made on the wrong branch** to the right one.

Cautions: the copy has a different identifier and is unrelated in the history, so the same change can later conflict or be applied twice when branches merge, and cherry-picking many commits becomes confusing. It is a precision tool, not a routine way to move work.

## Undoing Things: Reset, Revert, Restore

Several operations undo changes, with very different consequences.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Operation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rewrites history?</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Safe on shared branches?</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Revert</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Creates a **new commit** that reverses the changes of an earlier one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes: the standard way to undo a change that has been shared</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reset (soft)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moves the branch pointer back, keeping the changes staged</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reset (mixed)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moves the pointer back, keeping the changes in the working files but unstaged</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reset (hard)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moves the pointer back and discards the changes in the working files</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, and destroys uncommitted work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Restore or checkout of a file</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replaces a working file with an earlier version</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, but discards unsaved edits to that file</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stash</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Temporarily sets aside uncommitted changes, to be reapplied later</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
    </tr>
  </tbody>
</table>

**Revert** is the safe default for anything already published. **Hard reset** and similar operations should be used with care, since they discard uncommitted work for good.

## The Reflog: A Safety Net

Git keeps a private log, the **reflog**, of where your branch pointers and HEAD have been, for some time after each change. Even after a bad reset or rebase, the old commits usually still exist and can be found in the reflog and restored. Knowing it exists makes experimentation less frightening: **it is hard to lose committed work in Git, though uncommitted work is not protected.**

## Pushing After Rewriting

After rewriting commits that have been pushed to a personal branch, a normal push is refused because histories differ. A **force push** is then needed, and the safer variant, **force with lease**, refuses to proceed if the remote branch has received commits you have not seen. Force pushing to shared or protected branches should be prohibited by policy.

## Merge or Rebase: A Team Decision

Teams differ, and neither is right for everyone.

- **Prefer merge** where the true record of parallel work matters and where people are less experienced with rebasing.
- **Prefer rebase** (or squash) to keep a linear, readable main history, with a clear rule that rebasing is for unshared work.
- Whatever is chosen, **write it down** and apply it consistently.

<!--
IMAGE PROMPT  ->  generate as images/02_rebase_cherry_pick_revert.png   (16:9 explanatory diagram, place here)

Three panels. Rebase: a feature branch of commits X Y moved from an old base to the new tip, drawn with new copies X' Y'. Cherry-pick: one commit C copied from main to a release branch as C'. Revert: a new commit labelled Undo C appended to the history without removing C. A stop sign reads Do not rewrite shared history.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose the Operation

1. A developer has eight small messy commits on a personal branch and wants three clean ones before opening a pull request.
2. A fix on the main line must also be applied to the release branch for version 2.
3. A change that was merged into the shared main line yesterday turns out to be wrong and must be undone.

Case 1 uses interactive rebase to squash and reword. Case 2 uses cherry-pick. Case 3 uses revert, because the history is shared and must not be rewritten.

## Conclusion

Rewriting history is the practice of changing commits that already exist, by rebasing them onto a new base, combining or editing them, or copying individual commits elsewhere, to produce a cleaner or more suitable record, and it must be limited to history that has not yet been shared with others. Revert is the safe way to undo shared work, and the reflog is a safety net for mistakes.

The next chapter looks at how releases are marked and communicated, and at the tools around code for planning and for contributing to projects beyond your own team.
