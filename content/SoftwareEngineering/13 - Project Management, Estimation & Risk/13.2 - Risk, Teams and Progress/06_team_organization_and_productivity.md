## Introduction

Software is made by people working together, and the way those people are organised has as great an effect on the result as the technology they choose. A team that is too large spends its time coordinating; one that is too fragmented cannot deliver anything whole; one in which knowledge sits with a single person is fragile. Observations made over fifty years, some of them stated as laws, describe how structure, size, communication, and productivity interact. Understanding them helps engineers and managers organise work so that it flows.

This topic explains the main team structures, Conway's law and its practical use, Brooks's law and the cost of communication, what affects productivity, and how to bring new people into a team.

**Definition:** Team organisation is the arrangement of people into groups with defined responsibilities, communication paths, and decision rights, intended to allow software work to be carried out effectively and sustainably.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_team_organization_and_productivity.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: three small teams drawn as clusters of dots with few internal lines; right: one large cluster where every dot is joined to every other with a dense tangle of lines, labelled communication paths; between them a ruler labelled Team size.

ON-IMAGE TEXT: show a short bold title "Team Organization and Productivity" plus only these few labels, large and legible: Size and Connections. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Team Structures

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Structure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Functional (by skill)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separate groups for analysts, designers, developers, testers, operations, each serving many projects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deep expertise; consistent standards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hand-offs and delay; no shared ownership of the outcome</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cross-functional product team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A small team containing all skills needed to deliver a part of the product from idea to operation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast flow; shared ownership; fewer hand-offs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specialists may feel isolated; needs enough people with each skill</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feature team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A cross-functional team that builds complete features across all layers of the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivers value end to end</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs shared code ownership and discipline</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Component team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A team that owns one component or layer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deep component knowledge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Features need several teams to coordinate</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Platform team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provides internal services and tools for other teams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reuse; efficiency; reduces cognitive load of others</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can become a bottleneck if it does not treat other teams as customers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Enabling team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specialists who help other teams adopt a capability for a time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spreads expertise</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs time-limited engagement</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Chief programmer team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A highly skilled lead supported by specialists (Harlan Mills, 1970s)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conceptual integrity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Depends on exceptional individuals</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Egoless team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Collective ownership, with decisions made by consensus (Gerald Weinberg)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared learning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow decisions; may lack direction</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Open-source style</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Distributed volunteers with maintainers, patches, and review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wide participation; transparent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs strong governance and communication practices</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Distributed or remote</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Members in different places and time zones</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wider talent pool; round-the-clock cover</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Communication friction; time zone delays</td>
    </tr>
  </tbody>
</table>

The book **Team Topologies** by Matthew Skelton and Manuel Pais names four fundamental types: stream-aligned teams (which own a flow of work), platform teams, enabling teams, and complicated-subsystem teams, and three interaction modes: collaboration, facilitation, and x-as-a-service. Its core idea is to design teams so that the **cognitive load** on each, the amount it must hold in its head, stays manageable.

## Team Size

Small teams work better. Agile practice commonly recommends from five to nine people, a size at which everyone can talk to everyone. Amazon is known for the "two-pizza" rule: a team should be small enough to be fed by two pizzas. Larger efforts are divided into several small teams with clear interfaces.

## Conway's Law

In 1968 Melvin Conway observed that **organisations which design systems are constrained to produce designs that copy the communication structures of those organisations.** If four teams build a compiler, it will have four stages.

The consequences are practical.

- **Architecture reflects organisation.** Boundaries between modules tend to appear where boundaries between teams lie. Where teams communicate poorly, interfaces between their parts are awkward.
- **Reorganising changes architecture,** whether or not intended.
- **The inverse Conway manoeuvre:** deliberately shape teams to produce the desired architecture. If the target is independent services, form independent teams that own them end to end.
- **Dependencies between teams slow delivery.** A design that needs five teams to agree for every change will deliver slowly, however good the technology.
- **Watch for mismatches,** such as a modular architecture owned by a single overloaded team, or a monolith divided among many teams who constantly collide.

## Brooks's Law and the Cost of Communication

In his 1975 book *The Mythical Man-Month,* Frederick Brooks, who managed the development of IBM's OS/360, argued that **adding people to a late software project makes it later.** Reasons:

1. **Ramp-up:** new people take time to learn, and the existing team spends time teaching them, so productivity first falls.
2. **Communication overhead:** with n people there are n times (n minus one) divided by two possible pairs. Five people have ten paths; ten people have forty-five; twenty have a hundred and ninety. Coordination effort grows faster than headcount.
3. **Indivisible tasks:** some work cannot be shared. As Brooks put it, bearing a child takes nine months no matter how many women are assigned.
4. **Partitioning needs design:** dividing work among more people requires interfaces and integration effort.

Brooks's point is that **effort and calendar time are not interchangeable,** so the "man-month" (person-month) is a misleading unit when tasks are sequential and need communication. It is not an absolute law: adding people early, to work that divides cleanly, or the right specialist at the right time, can help. Other observations in the same book include **the surgical team** (organising around a principal programmer), **conceptual integrity** (a system should reflect one coherent set of design ideas), and the **second-system effect** (the tendency to over-engineer a follow-up system).

## What Affects Productivity

Programmer productivity differs widely. Studies since the 1960s report differences of ten times or more between individuals, though the figures are debated. Factors include:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Factor</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effect</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Skill and experience</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large; but experience in the specific domain and system matters as well as general ability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clarity of requirements and goals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unclear goals cause rework and waiting</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interruptions and context switching</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moving between tasks costs time; flow states are fragile</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Meetings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Necessary ones help; excessive ones consume focus</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tools and automation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast builds, reliable tests, and good environments multiply output</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code quality and technical debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Messy code slows every change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team stability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Turnover loses knowledge and ramp-up time</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Psychological safety</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Willingness to admit mistakes and ask questions improves learning and quality</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Autonomy, mastery, and purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Motivation shapes effort and creativity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Working environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quiet, ergonomic space or good remote arrangements</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Overwork</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long hours raise errors and burnout, and lower output over weeks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependencies on other teams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Waiting for others is among the largest hidden losses</td>
    </tr>
  </tbody>
</table>

Tom DeMarco and Timothy Lister, in *Peopleware,* argued that the major problems of software projects are not technological but sociological, concerning people, teams, and the working environment. Google's research on its own teams (Project Aristotle) found that **psychological safety** was the strongest predictor of team effectiveness, ahead of the individual abilities of the members.

### Measuring Productivity

Measuring individual productivity by lines of code, commits, or hours is unreliable and harmful: it rewards volume, discourages collaboration, and invites gaming (Goodhart law: when a measure becomes a target, it ceases to be a good measure). Better frameworks look at team outcomes, such as the delivery metrics discussed in Unit 9 (deployment frequency, lead time, change failure rate, and recovery time) and the **SPACE framework,** which considers satisfaction, performance, activity, communication, and efficiency together. The next topic returns to metrics.

## Roles and Responsibility

- **Clear ownership:** every component, process, and decision has an owner.
- **Decision rights:** who decides what, so teams do not wait.
- **Collective code ownership,** with standards and review, avoids dependence on individuals.
- **Technical leadership** that guides without dictating.
- **Escalation paths** for conflicts.
- **Working agreements:** written agreements on how the team works, such as hours of overlap, communication channels, review rules, and definitions of done.

## Onboarding New Team Members

A new person is a cost before they are a benefit. Good onboarding shortens the time to productivity.

1. **Before day one:** accounts, hardware, access, and a welcome message.
2. **A guide or buddy** who answers questions and introduces people.
3. **Documentation** of the architecture, setup, conventions, and glossary, tested by new people, who fix what is wrong.
4. **A reproducible environment** that can be set up in hours, not days.
5. **A small first task** that reaches production in the first week; this teaches the whole path from change to release.
6. **Gradual widening** of responsibility and exposure to the system.
7. **Regular conversations** about progress and questions in the first months.
8. **Learning from the newcomer:** fresh eyes reveal confusing documentation and unspoken assumptions.

The time to the first production change is a useful measure of how healthy the engineering system is.

## Sustaining Teams

- **Keep teams stable** and avoid moving people between projects constantly.
- **Spread knowledge** through pairing, review, rotation, and documentation, to raise the bus factor.
- **Invest in growth:** learning time, mentoring, and career paths.
- **Protect focus time.**
- **Run retrospectives** and act on them.
- **Handle conflict early** and respectfully.
- **Watch for burnout:** sustained pace matters more than heroics.
- **Include and respect differences;** diverse teams consider more perspectives.

<!--
IMAGE PROMPT  ->  generate as images/06_communication_paths_and_conways_law.png   (16:9 explanatory diagram, place here)

Left: groups of 3, 5, 10 dots fully connected, labelled 3, 10, and 45 paths. Right: an organisation chart of three teams mirrored by a system diagram of three components with interface lines, showing that structures match.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Shape the Team

1. A project is late and the manager adds six developers to a team of six. What is likely to happen in the short term?
2. A company has separate front-end, back-end, and database teams, and every feature takes weeks of hand-offs. What organisational change might help?
3. How many communication paths exist in a team of eight?

For case 1, productivity drops as the team teaches the newcomers and communication paths multiply. For case 2, form cross-functional feature teams that own features end to end. For case 3, eight times seven divided by two is 28.

## Conclusion

Team organisation is the arrangement of people into groups with defined responsibilities, communication paths, and decision rights, intended to allow software work to be carried out effectively and sustainably. Conway's law, Brooks's law, and the evidence on productivity all point to small, stable, well-supported teams with clear ownership and few dependencies.

Once teams are in place and working, their progress must be observed and reported. The next topic covers tracking progress and project metrics.
