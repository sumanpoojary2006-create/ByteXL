## Introduction

A local repository is a private workshop. Teams work together by exchanging commits through a shared repository, usually hosted on a platform such as GitHub, GitLab, or Bitbucket. Understanding how local and remote repositories relate, and what each of the sharing operations really does, removes most of the confusion that beginners feel about collaboration, including the common message that a push was rejected.

**Definition:** A remote repository is a copy of a project hosted on another machine, typically a shared server, with which local repositories exchange commits by fetching new work from it and pushing local work to it, enabling a team to collaborate on the same history.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_remote_repositories_and_collaboration.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three developer laptops each with a full local repository, connected by arrows labelled clone, fetch, push to a central shared repository in the cloud labelled origin.

ON-IMAGE TEXT: show a short bold title "Remote Repositories and Collaboration" plus only these few labels, large and legible: Clone, Fetch, Push. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Local and Remote

Every developer has a complete **local repository**. A **remote** is a named reference to another repository, almost always a shared one. By convention, the remote from which a project was copied is called **origin**. A second remote, often called **upstream**, is used when working from a copy, called a fork, of someone else project to refer to the original.

## The Sharing Operations

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Operation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Changes your working files?</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clone</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copies a remote repository, with its whole history, to your machine and sets up the remote name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Creates them</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fetch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Downloads new commits and branch updates from the remote into your repository, without touching your own work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Merge or rebase</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrates fetched changes into your current branch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pull</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A shortcut that fetches and then integrates (by merging or rebasing)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Push</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uploads your local commits on a branch to the remote</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
    </tr>
  </tbody>
</table>

Understanding that **pull is fetch plus integrate** explains why fetching first, to look before integrating, is a safe habit.

## Tracking Branches

A local branch can be linked to a branch on the remote, so that Git knows what to compare and where to send changes. Git then reports whether your branch is **ahead** (you have commits the remote lacks), **behind** (the remote has commits you lack), or has **diverged** (both). It also keeps **remote-tracking references**, which are your local record of where the remote branches were at your last fetch, and they only change when you fetch.

## Why a Push Is Rejected

A push is refused when it would **discard other people work**. If a colleague pushed new commits to the branch after your last fetch, your history and the remote have diverged, and simply replacing the remote branch with yours would delete their commits. The remedy is not to force the push, but to **fetch, integrate their changes into your branch, resolve any conflicts, test, and push again**.

Using the **force** option overwrites the remote history and can destroy the work of teammates. If it must be used, for example after tidying a personal branch, the safer variant that checks that the remote has not changed unexpectedly should be preferred, and it should never be used on shared branches.

## Hosting Platforms

Services built around Git add features for collaboration.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Feature</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared repositories and access control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decide who can read and write</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pull or merge requests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Propose and review changes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Issue tracking and project boards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plan and track work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated pipelines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run builds, tests, and deployments on each change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Branch protection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevent direct changes to important branches and require checks and reviews</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code search, wikis, and releases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Navigation and communication</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Personal copies of a repository, used in open-source and cross-team work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Webhooks and integrations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Connect to other tools</td>
    </tr>
  </tbody>
</table>

The platform is separate from Git itself. A team can change platforms and keep its history, since every clone holds it all.

## Access and Authentication

Access to remote repositories needs proof of identity.

- **SSH keys:** a pair of cryptographic keys, with the public half registered on the platform and the private half kept secret on your machine.
- **Access tokens:** long random strings used instead of passwords, with limited permissions and an expiry.
- **Single sign-on and multi-factor authentication** for organisations.

**Never share private keys or tokens, and never commit them to a repository.** Permissions should follow the principle of least privilege.

## Collaboration Models

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Model</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared repository</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All team members have write access to one repository and work on branches in it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Teams within an organisation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fork and pull request</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contributors copy the repository, work in their own copy, and propose changes back</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Open-source projects, and external contributors</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainer with patches or email</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes are sent as patches for a maintainer to apply</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Some long-established projects, such as the Linux kernel</td>
    </tr>
  </tbody>
</table>

## Protecting Important Branches

A team normally **protects** the main branch so that:

- direct pushes are blocked, and changes arrive only through reviewed requests
- the automated checks must pass before merging
- a minimum number of approvals is required
- force pushes and deletion are prevented
- history stays linear or signed, if the team requires it

## Everyday Collaboration Habits

- **Fetch or pull before starting work,** and before pushing.
- **Push small, working commits regularly,** so work is backed up and visible.
- **Keep your branch up to date** with the main line.
- **Do not rewrite history that others may have used.**
- **Communicate** about large or risky changes before they land.
- **Check what you are about to push,** especially that no secrets or large files are included.
- **Use meaningful branch names** and delete old ones.

<!--
IMAGE PROMPT  ->  generate as images/02_push_rejected_and_fix.png   (16:9 explanatory diagram, place here)

Left: local main with commits A B C and remote main with A B D; a push arrow blocked by a red cross labelled Rejected: remote has work you lack. Right: the fix in three steps: Fetch, Integrate into a merged commit E, Push accepted with a green tick.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Fetch, Pull, or Push?

1. You want to see what colleagues have done without changing your own work.
2. You want your finished, committed work to be visible to the team.
3. Your push was rejected because the remote contains commits you do not have. What should you do?

Operation 1 is fetch. Operation 2 is push. For 3, fetch, integrate the remote changes into your branch, resolve any conflicts and test, and then push; do not force the push.

## Conclusion

A remote repository is a copy of a project hosted on another machine, typically a shared server, with which local repositories exchange commits by fetching new work from it and pushing local work to it, enabling a team to collaborate on the same history. Treating fetch, integrate, and push as separate steps, and protecting shared branches, keeps collaboration safe.

How a team organises its branches over time is a matter of agreed workflow. The next topic compares the main branching strategies.
