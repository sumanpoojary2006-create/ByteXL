## Introduction

Code answers what the system does, version control records how it changed, and something else must record what remains to be done and why. Without a shared list of work, tasks live in memory, chat messages, and private notes, and are lost or duplicated. An issue tracker provides that list, and project boards show its state. Linked to the repository, they connect the plan to the code, so that for any change one can answer: why was this done, who decided, and what happened to it.

**Definition:** An issue tracker is a system that records units of work, such as bugs, feature requests, and tasks, each with a description, owner, and status, and a project board is a visual arrangement of those items by stage, together giving a team a shared, traceable view of what is planned, in progress, and finished.

<!--
IMAGE PROMPT  ->  generate as images/11_intro_issue_tracking_and_project_boards.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A board with columns Backlog, To Do, In Progress, Review, Done, containing cards with small labels and avatars, a card being dragged from left to right, and thin lines linking one card to a pull request icon and a commit icon.

ON-IMAGE TEXT: show a short bold title "Issue Tracking and Project Boards" plus only these few labels, large and legible: Issue, Stage, Link. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What an Issue Is

An **issue** (also called a ticket or work item) is a record of one piece of work or one problem. Typical kinds:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bug</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A defect to be fixed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Orders with no items crash the kitchen display</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feature or user story</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new capability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allow customers to save a favourite order</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Task</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A piece of work that is not a feature or bug</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Upgrade the database library</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Epic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A large body of work, divided into stories</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redesign the checkout</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spike</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A time-boxed investigation to reduce uncertainty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test whether a new payment provider meets performance needs</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improvement or technical debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Internal quality work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split the pricing module</td>
    </tr>
  </tbody>
</table>

## Anatomy of a Good Issue

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Field</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Title</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A short, specific summary: "Reject orders with no items," not "Order problem"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Description</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The context, what is wanted or wrong, and why it matters</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Acceptance criteria</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How anyone will know it is done</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">For a bug: steps to reproduce, expected and actual behaviour, environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allows the problem to be seen and fixed; Unit 10 covers bug reports in detail</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Type and labels</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Classification, such as bug, enhancement, security, area of the system</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Priority and severity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How important and how harmful it is</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assignee</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The person responsible</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Milestone or sprint</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The release or time period it belongs to</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Links</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Related issues, requirements, designs, pull requests, and commits</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A rough size, if the team uses them</td>
    </tr>
  </tbody>
</table>

Good issues are **specific, self-contained, and actionable**. A vague issue wastes time for everyone who reads it.

## The Workflow of an Issue

Issues move through states that reflect the team process. A simple flow is: **Open** (reported), **Triaged** (reviewed, prioritised, and accepted), **In progress**, **In review**, **Done**, and **Closed**. Some end differently: **Won't fix**, **Duplicate**, **Cannot reproduce**, or **Deferred**. Making the states and their rules explicit avoids ambiguity about what "done" means, and ties to the Definition of Done in Unit 2.

## Triage

**Triage** is the regular review of new issues to decide what happens to each: is it valid, a duplicate, clear enough, and how urgent? A team that triages routinely keeps its list useful. A team that does not accumulates a long, stale list that nobody trusts.

## Project Boards

A **board** shows issues as cards in columns that represent stages of work. It is the same idea as the Kanban boards of Unit 2: the columns are **the stages that work actually passes through**, and cards move from left to right.

- Typical columns: Backlog, To Do, In Progress, In Review, Done.
- A **work-in-progress limit** on a column discourages starting too much at once.
- **Swimlanes** can group cards by team, person, or kind.
- **Filters and views** show the work for a person, a release, or a label.
- **Automation** moves cards when events occur, such as when a pull request is opened or merged.
- Boards support planning sessions, daily stand-ups, and reviews.

Tools offer related views: **lists** for backlog management, **timelines or roadmaps** for planning across weeks and months, and **charts** such as burndown, cumulative flow, and cycle time.

## Linking Issues and Code

The value of integrated tools lies in the connections.

- **Branches and commits reference issue numbers,** so history shows the reason for each change.
- **Pull requests link to issues,** and **closing keywords** in descriptions can close the issue automatically when the request is merged.
- **Releases list the issues resolved,** so release notes can be assembled from them.
- **Traceability** from requirement to issue to commit to release becomes automatic, useful for audit and for impact analysis.

## Good Practice

1. **One source of truth.** Keep the plan in the tracker, not scattered across messages and documents.
2. **Write for a reader who lacks your context.**
3. **Keep issues small,** so they can be completed within a short time.
4. **Use consistent labels and templates,** so information is uniform.
5. **Groom the backlog,** closing what is stale or obsolete, and ordering the rest.
6. **Update status promptly,** so the board is accurate. An out-of-date board is worse than none.
7. **Do not use the tracker to avoid conversation.** A quick discussion often resolves what ten comments cannot.
8. **Measure flow,** using cycle time and throughput, as Unit 2 described, not to punish people but to find bottlenecks.

## Common Problems

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Huge backlog nobody reads</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No triage or pruning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regular grooming; close stale issues with a note</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vague issues</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No template or standard</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provide templates; reject unclear reports politely with a request for detail</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Board out of date</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Status updates seen as extra work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automate transitions; discuss the board in stand-ups</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplicate issues</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No search before reporting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Search first; merge duplicates</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too many fields and states</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-engineered process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simplify to what the team actually uses</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Priority inflation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything marked urgent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear criteria; a limit on top-priority items</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using the tracker for status reporting only</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Management focus</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use it first as a tool for the people doing the work</td>
    </tr>
  </tbody>
</table>

## Tools

Popular tools include the issue and project features of the code hosting platforms, and dedicated products such as Jira, Linear, Trello, and ClickUp. The best choice is the one the team will actually keep up to date, and that integrates with its repository and pipelines.

<!--
IMAGE PROMPT  ->  generate as images/02_issue_board_with_links.png   (16:9 explanatory diagram, place here)

A project board with columns Backlog, To Do, In Progress (limit 3), In Review, Done. One expanded issue card shows title, labels, assignee, acceptance criteria, and linked pull request and commit icons. Arrows show the card moving left to right and an automation bolt closing it on merge. No code imagery.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Improve the Issue

1. A bug issue reads: App does not work. Please fix.
2. A board shows twelve cards in In Progress with a limit of three. What does this indicate?
3. A pull request is merged, and the related issue still shows as open weeks later.

Issue 1 lacks steps to reproduce, expected and actual behaviour, and environment; a request for detail should be made. Case 2 shows that the limit is ignored and the team is starting more than it finishes, so work should be finished before more is started. Case 3 shows missing linkage or automation: the pull request should reference the issue, with a closing keyword, so the issue closes when the change merges.

## Conclusion

An issue tracker is a system that records units of work, such as bugs, feature requests, and tasks, each with a description, owner, and status, and a project board is a visual arrangement of those items by stage, together giving a team a shared, traceable view of what is planned, in progress, and finished. Their value depends on clear issues, honest status, and links to the code.

Most of the tools and practices in this unit began in the world of open-source projects. The last topic of the chapter describes how to take part in open-source collaboration.
