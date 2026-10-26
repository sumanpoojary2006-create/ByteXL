## Introduction

Git has a reputation for being difficult, and much of the difficulty comes from learning commands without understanding the model underneath. Git is built on a small number of simple ideas. A person who understands them can reason about almost any situation, while a person who memorises commands is lost when something unexpected happens. This topic explains the model: what Git stores, where changes live, and what a branch really is.

**Definition:** Git is a distributed version control system that stores the history of a project as a connected set of snapshots called commits, held in a local repository on every user machine, with changes moving between a working directory, a staging area, and the repository.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_git_fundamentals.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three boxes in a row labelled Working directory, Staging area, Repository, with arrows labelled add and commit between them, and a chain of commit circles inside the repository box with a label pointing to the latest one named branch.

ON-IMAGE TEXT: show a short bold title "Git Fundamentals" plus only these few labels, large and legible: Working, Staged, Committed. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Snapshots and Commits

Git thinks of history as a series of **snapshots**. Each time a commit is made, Git records the state of all tracked files at that moment, and efficiently reuses the parts that did not change. A **commit** is a snapshot together with:

- a unique identifier, a long hexadecimal **hash** computed from its content
- the **author** and time
- a **message** describing the change
- a link to its **parent** commit (or parents, for a merge)

Because each commit points to its parent, commits form a chain, or more generally a **graph**. The hash depends on the content and the parent, so changing anything in history changes every later identifier. This makes history **tamper-evident**, and it is why rewriting shared history has consequences, covered later in the unit.

## Objects Under the Hood

Git stores everything as four kinds of object, each identified by the hash of its content.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Object</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Contains</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Blob</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The content of a file</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tree</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A directory: a list of names pointing to blobs and other trees</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A pointer to a tree (the snapshot), the parent commits, and the metadata</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tag</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A named, possibly annotated, pointer to a commit</td>
    </tr>
  </tbody>
</table>

A beginner does not need to manipulate these, but knowing that they exist explains why Git is fast, why identical files are stored once, and why history is so reliable.

## The Three Areas

A central idea is that changes flow through three places.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Area</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens here</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Working directory</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The files you see and edit on disk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">You change files</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Staging area (index)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A preparation area for the next commit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">You choose exactly which changes will go into it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repository (the .git history)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The permanent record of commits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commits are stored and never silently altered</td>
    </tr>
  </tbody>
</table>

The staging area lets you build a commit deliberately: a developer who has made two unrelated changes can stage and commit them separately, producing two clean logical commits.

A file can be in these **states**: **untracked** (Git does not know it), **modified** (changed since the last commit), **staged** (marked for the next commit), and **committed** (safely stored).

## Branches and HEAD

A **branch** in Git is simply a **movable label pointing to a commit**. When a new commit is made on a branch, the label moves forward to it. Because a branch is just a small pointer, creating one is instantaneous and cheap, which is why branching is routine in Git.

**HEAD** is a special pointer that says **where you are now**, normally pointing to the current branch. Committing moves the current branch, and so HEAD with it. Switching branches changes HEAD and updates the working directory to match.

## The Local and the Remote

Every clone of a repository contains the **entire history**, so most operations, committing, viewing history, branching, comparing, are local, fast, and work offline. Sharing happens by exchanging commits with another repository, normally a shared one hosted on a service, called a **remote**. The next chapter describes this in detail.

## The Basic Vocabulary

Git is operated by commands. The following table lists the names of the most common ones, as a reference to the operations described in this unit.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Operation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Command name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Create a repository</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">init</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start tracking a project</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copy a repository</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">clone</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Obtain a full copy of a remote repository</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">See what changed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">status, diff</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show modified files and the differences</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stage changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">add</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Select changes for the next commit</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Record a commit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">commit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Save the staged snapshot with a message</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">View history</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">log</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">List past commits</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Create or list branches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">branch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make a new line of work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Switch branch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">switch, checkout</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move to another branch</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combine branches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">merge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bring changes from one branch into another</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Download from remote</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">fetch, pull</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Get new commits from a remote</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Upload to remote</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">push</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Send local commits to a remote</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Undo safely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">revert</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Create a new commit reversing an earlier one</td>
    </tr>
  </tbody>
</table>

## A Typical Cycle

1. Update your local copy with the latest from the shared repository.
2. Create a branch for your task.
3. Edit files, and check what has changed.
4. Stage the related changes and commit them with a clear message. Repeat as work proceeds.
5. Publish the branch to the shared repository.
6. Have it reviewed and merged, and remove the branch.

## Ignoring Files

Not everything in a project folder belongs in the repository: compiled output, downloaded libraries, logs, editor settings, and secrets. A file named **gitignore** lists patterns that Git should not track. Keeping generated files and secrets out of the repository keeps history small, clean, and safe.

## Common Misunderstandings

- **"Git stores differences."** Conceptually it stores snapshots, even though it compresses efficiently.
- **"A branch is a copy of the code."** It is only a pointer.
- **"Git and GitHub are the same."** Git is the tool; GitHub, GitLab, and Bitbucket are services that host Git repositories and add collaboration features.
- **"Committing sends my work to others."** A commit is local until it is pushed.

<!--
IMAGE PROMPT  ->  generate as images/02_commit_graph_branch_pointers_head.png   (16:9 explanatory diagram, place here)

A commit graph: a chain of circles A, B, C on main, with a branch feature splitting from B to D and E. Labels main, feature, and HEAD as small flags pointing to specific commits. A note says A branch is just a label pointing to a commit.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Where Is the Change?

1. You edit a file but have not run any Git operation yet.
2. You mark the edit for inclusion in the next commit.
3. You record the commit.

After step 1, the change is in the working directory (modified). After step 2, it is staged. After step 3, it is committed in your local repository, and is still not visible to anyone else until pushed.

## Conclusion

Git is a distributed version control system that stores the history of a project as a connected set of snapshots called commits, held in a local repository on every user machine, with changes moving between a working directory, a staging area, and the repository. Understanding snapshots, the three areas, and branches as pointers makes the individual commands logical.

The quality of history depends on how commits are made. The next topic describes commits, history, and good commit messages.
