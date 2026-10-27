## Introduction

A goal such as "build the ordering system" is too large to plan, assign, or track. A plan becomes useful only when the work is divided into pieces small enough to estimate, give to a person, and recognise as finished, and when those pieces are arranged in time with their dependencies taken into account. Work breakdown is the first of these steps, and scheduling is the second.

This topic explains the work breakdown structure, the types of dependency, the critical path method that determines the shortest possible duration, schedule charts, and the practical ways of compressing a schedule and keeping it realistic.

**Definition:** A work breakdown structure (WBS) is a hierarchical decomposition of the total scope of a project into progressively smaller deliverables and work packages, and scheduling is the arrangement of those pieces in time, taking account of their dependencies, durations, and the resources available.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_work_breakdown_and_scheduling.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a tree diagram splitting one top box into branches and then into small leaf boxes. Right: a network of leaf tasks connected by arrows with one path highlighted in red, below which a horizontal bar chart shows the same tasks as bars across a calendar.

ON-IMAGE TEXT: show a short bold title "Work Breakdown and Scheduling" plus only these few labels, large and legible: Break Down, Then Order. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Work Breakdown Structure

The WBS divides the project into a tree. The top is the whole project; each level splits the one above into parts, and the lowest level holds **work packages** that can be estimated and assigned.

- **Deliverable-oriented:** the first levels name things to be delivered (such as "customer ordering" or "kitchen display"), not activities.
- **100 per cent rule:** the children of any item must together represent all of its work, nothing more and nothing less. This prevents gaps and overlap.
- **Mutually exclusive:** no work appears in two places.
- **Sensible granularity:** a common guide is that a work package takes from a day or two up to a couple of weeks; too small means excessive management, too large cannot be tracked.
- **Clear completion:** each package has a definition of done.
- **Includes all work:** not only coding, but design, testing, documentation, deployment, training, project management, and rework.

### Ways of Decomposing

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Basis</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example top-level branches</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">By deliverable or feature</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ordering, payments, menu management, reporting</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">By phase of the life cycle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements, design, construction, testing, deployment</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">By component or architecture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mobile app, web front end, back-end services, database</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">By team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Front-end team, platform team</td>
    </tr>
  </tbody>
</table>

Software projects frequently use features at the top and a short list of cross-cutting activities such as testing and deployment beside them. In agile practice, the same idea appears as **epics** divided into **user stories** divided into tasks.

## Dependencies

Tasks are rarely independent. A **dependency** is a relationship in which one task affects when another can start or finish.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finish-to-start (the common one)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">B cannot start until A finishes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing a screen cannot start until it is built</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start-to-start</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">B cannot start until A has started</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation begins once development begins</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finish-to-finish</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">B cannot finish until A finishes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing ends after development ends</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start-to-finish</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">B cannot finish until A starts (rare)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Old system stays on until the new one starts</td>
    </tr>
  </tbody>
</table>

Dependencies also differ by cause.

- **Mandatory (logical):** inherent in the work, such as a database must exist before data is stored in it.
- **Discretionary:** chosen by preference or best practice.
- **External:** on something outside the team, such as a vendor delivery, a legal approval, or another team's release.

**Lag** is a deliberate delay after a predecessor; **lead** is an overlap. External and cross-team dependencies are the most common cause of surprise delays and should be identified early and watched.

## The Network and the Critical Path

Drawing the tasks as a network, with arrows for dependencies, shows how the work flows. Each task has a **duration.** The **critical path method (CPM),** developed in the late 1950s for industrial scheduling, analyses the network as follows.

1. List all tasks, durations, and dependencies.
2. Moving forward from the start, compute the **earliest start** and **earliest finish** of every task.
3. Moving backward from the end, compute the **latest start** and **latest finish** that do not delay the project.
4. The **float** (slack) of a task is the amount it can slip without delaying the project: latest start minus earliest start.
5. The **critical path** is the longest chain of dependent tasks from start to finish. Its length is the **minimum project duration.** Tasks on it have **zero float:** any delay in them delays the whole project.

### What the Critical Path Tells You

- Where the schedule is **most sensitive:** the managers watch these tasks closely.
- Where **effort to shorten the project must be applied:** shortening a task off the critical path gains nothing.
- Where there is **slack,** which allows resources to be moved.
- That the critical path **can change** as tasks slip or are shortened; a near-critical path may become critical.

A related technique, **PERT** (program evaluation and review technique), uses three estimates per task (optimistic, most likely, pessimistic) to calculate an expected duration and its uncertainty, which acknowledges that durations are not exact.

## Schedule Representations

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Representation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Best for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gantt chart</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Horizontal bars for tasks along a calendar, with dependencies shown as links; named after Henry Gantt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Communicating the plan; showing overlaps and milestones</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Network diagram</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tasks as boxes connected by arrows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analysing dependencies and the critical path</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Milestone chart</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Key dates and the events they represent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reporting to executives</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Kanban or task board</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cards moving through workflow stages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Day-to-day flow of work</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Roadmap</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Themes or outcomes against broad time periods, without precise dates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Communicating direction in adaptive settings</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release plan and sprint plan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What will be delivered in which release or iteration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agile planning at different horizons</td>
    </tr>
  </tbody>
</table>

A **milestone** is a significant point with no duration, such as "first working version delivered to testers" or "security review passed." Good milestones are verifiable and meaningful, not simply "coding about halfway."

## Resources and Scheduling

A schedule drawn only from dependencies assumes unlimited people. In reality:

- **Resource constraints:** a specialist may be needed on several tasks at once. **Resource levelling** adjusts the schedule so that no one is overbooked, which may lengthen it.
- **Availability:** holidays, leave, meetings, and support work reduce the time available. A person is rarely productive on project tasks for the whole working week.
- **Skills:** assign by ability and learning needs.
- **Part-time and shared people** lose time switching between tasks.

## Shortening a Schedule

When the calculated duration is too long, the options act on the critical path.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cost or risk</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Crashing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add resources to critical tasks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Higher cost; communication overhead; may not help for tasks that cannot be divided (see Brooks's law, topic 6)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast tracking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do tasks in parallel that were planned in sequence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More rework and risk</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduce scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove or defer features</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less value delivered</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redesign the work or the architecture so teams can proceed independently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Takes design effort</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improve tools and automation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Faster builds, tests, and releases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Investment up front</td>
    </tr>
  </tbody>
</table>

## Building a Realistic Schedule

- **Include all the work,** including testing, reviews, integration, and deployment.
- **Add buffers** for uncertainty. The reasoning of Eliyahu Goldratt s **critical chain** method is that padding hidden inside every task is wasted; it is better to remove the padding and place a shared buffer at the end of a chain, and to watch how fast it is consumed.
- **Plan for the unknown:** reserve time for rework, defects, illness, and unplanned requests.
- **Schedule risky and uncertain work early,** so that problems appear while there is time to respond.
- **Integrate continuously** instead of leaving integration for the end.
- **Plan rolling horizons:** detailed plans for the next weeks, coarser for later. Detailed plans far ahead are mostly fiction.
- **Maintain the plan:** it is a living tool that is updated as facts arrive.
- **Beware of the planning fallacy,** the tendency, identified by Daniel Kahneman and Amos Tversky, to underestimate the time tasks will take even with experience of past overruns. Use historical data.
- **Parkinson's law** says work expands to fill the time available, and the **student syndrome** says people start late when a deadline is far away. Both argue for short feedback cycles.

<!--
IMAGE PROMPT  ->  generate as images/02_wbs_network_and_critical_path.png   (16:9 explanatory diagram, place here)

Left: a three-level WBS tree. Centre: a small task network with durations on boxes and the longest path highlighted in red with float values on the other paths in green. Right: the same tasks as a Gantt chart with the critical tasks in red and slack shown as light hatched bars.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Find the Critical Path

A small project has tasks A (3 days), B (2 days, after A), C (4 days, after A), D (2 days, after B and C).

1. What is the critical path, and how long is the project?
2. How much float does B have?
3. If task B is shortened by a day, does the project finish sooner?

For case 1, A, C, D takes 3 plus 4 plus 2 equals 9 days, which is longer than A, B, D (3 plus 2 plus 2 equals 7 days). For case 2, B takes 2 days but C takes 4, so B has 2 days of float. For case 3, no, because B is not on the critical path.

## Conclusion

A work breakdown structure is a hierarchical decomposition of the total scope of a project into progressively smaller deliverables and work packages, and scheduling is the arrangement of those pieces in time, taking account of their dependencies, durations, and the resources available. The critical path shows which tasks determine the finish date.

Both depend on knowing how long each piece of work will take, which is the hardest question in software. The next topic addresses software size and effort estimation.
