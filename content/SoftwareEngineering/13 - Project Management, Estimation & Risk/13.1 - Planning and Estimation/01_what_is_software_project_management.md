## Introduction

Software is rarely built by one person in an afternoon. Most of it is produced by teams, over weeks or years, with limited money, a deadline, and people who want different things from the result. Project management is the discipline of organising that effort so that the right thing is delivered, at an acceptable quality, within the limits of time and cost. It does not replace technical skill; it makes the technical skill effective by ensuring that people know what to build, in what order, with what resources, and what to do when plans meet reality.

This topic defines a project and project management, explains the classic constraints and how they trade against each other, outlines the activities and roles involved, and distinguishes plan-driven from adaptive approaches.

**Definition:** Software project management is the planning, organising, monitoring, and controlling of people, work, and resources so that a software product is delivered that meets its agreed goals within the constraints of scope, time, cost, and quality.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_what_is_software_project_management.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A triangle with Scope, Time, and Cost at the corners and Quality at its centre, a set of balance scales beside it, and a small timeline strip beneath showing Start and Finish markers.

ON-IMAGE TEXT: show a short bold title "What Is Software Project Management?" plus only these few labels, large and legible: Scope, Time, Cost. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Projects and Ongoing Work

A **project** is a temporary effort with a defined beginning and end, undertaken to create a unique product, service, or result. This distinguishes it from **operations**, which are continuing and repetitive, such as running and supporting a live system.

- A project has **goals,** a **limited duration,** a **budget,** and **people** assigned to it.
- It involves **uncertainty,** because something new is being created.
- It ends when the goals are met or when it is stopped.

Many software efforts blur this boundary. A product continues for years, receiving a stream of improvements. The final topic of this unit discusses how product thinking complements project thinking.

## The Constraints

Every project works within a set of constraints. The traditional model names three, drawn as the **project triangle** (also called the iron triangle or triple constraint), with quality at its centre.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Constraint</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical questions</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is to be delivered: features, behaviour, and boundaries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is included? What is explicitly excluded?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time (schedule)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When it must be delivered and when intermediate results are due</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is the deadline? Which dates are fixed?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost (budget and resources)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Money, people, equipment, and services available</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How many people? What is the budget?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How well the product meets needs: correctness, reliability, performance, security, usability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What standards must it meet?</td>
    </tr>
  </tbody>
</table>

The constraints are linked: changing one affects the others.

- **Adding scope** without adding time or cost reduces quality or causes delay.
- **Shortening the schedule** needs more people, which raises cost and, as a later topic explains, may not even help, or needs less scope.
- **Cutting cost** means less scope, more time, or lower quality.
- **Reducing quality** appears to save time and cost, but usually creates defects and technical debt that cost more later.

The common saying is "fast, cheap, good: choose two." The role of management is to make the trade-offs **explicit and deliberate,** with the people who own the decision, rather than allowing them to happen by accident.

### Fixed and Flexible

A useful discipline is to decide which constraint is **fixed,** which is **firm,** and which is **flexible.** Plan-driven projects often fix scope and let time and cost move. Many agile teams fix time and cost, using time-boxed iterations and a fixed team, and let scope vary, delivering the most valuable items first.

## What Project Management Involves

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Activity</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Covered in</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Initiation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Define why the project exists, its goals, its sponsor, and whether it is worth doing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">This topic</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scope definition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agree what is in and out, with requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unit 3</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Planning and scheduling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Break the work into tasks, order them, assign them</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Next topic</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predict the effort, time, and cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Topics 3 and 4</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anticipate and handle what could go wrong</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Topic 5</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Staffing and team organisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Obtain, organise, and develop people</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Topic 6</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monitoring and control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compare progress with the plan and correct course</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Topic 7</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Communication and stakeholder management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the right people informed and aligned</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Topic 8</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Procurement and vendor management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Buy or contract what is not built in-house</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Topic 9</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ensure the product meets its standards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Units 10 and 11</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evaluate and control changes to scope, plan, and product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Below</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Closure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deliver, hand over, learn from the project, and release the team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Capstone</td>
    </tr>
  </tbody>
</table>

## Managing Change

Requirements change. Business needs shift, users react to early versions, and technology moves. A project that treats every change as a failure of planning will fail; one that accepts all changes without evaluation will never finish. **Scope creep,** the gradual, uncontrolled growth of scope, is among the most common causes of project failure.

A change process answers four questions about each requested change: **what is the value, what is the cost, what is the effect on the schedule and quality, and who decides.** Plan-driven projects use a formal change control procedure with a decision-making body. Adaptive projects manage change through a **prioritised backlog** that the product owner reorders continuously, with new items replacing less valuable ones within the fixed capacity of the team.

## Roles in Project Management

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Responsibility</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sponsor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Funds the project, owns the business case, and removes organisational obstacles</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Project manager</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plans, coordinates, tracks, and reports; manages risk and communication; accountable for delivery</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product owner</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decides what is valuable and sets priorities (in agile settings)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scrum master or delivery lead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Helps the team follow its process and removes impediments</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical lead or architect</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Guides technical decisions and quality</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team members</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do the work and contribute estimates and knowledge</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stakeholders</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anyone affected by or influencing the project: users, customers, operations, legal, management</td>
    </tr>
  </tbody>
</table>

Small teams often combine roles, and in agile teams much of the traditional project manager role is shared among the team, the product owner, and the delivery lead. The responsibilities remain even where the job titles do not.

## Plan-Driven and Adaptive Approaches

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Plan-driven</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Adaptive (agile)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Planning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detailed up front for the whole project</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rolling: coarse for the future, detailed for the near term</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed early; changes controlled formally</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expected to evolve; managed through the backlog</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One major delivery at the end, or few large ones</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Frequent small increments</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feedback</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Late</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early and continuous</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Suits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stable requirements, regulated or contract-driven work, physical dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uncertain requirements, products that learn from users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concentrated late, when the product first runs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spread out and reduced by early delivery</td>
    </tr>
  </tbody>
</table>

Many organisations combine them: an overall budget, milestones, and governance from plan-driven practice, with adaptive methods inside the teams. The process models of Unit 2 give the background; this unit concentrates on the management skills that apply to both.

## Why Software Projects Are Hard to Manage

- **The product is invisible.** Progress cannot be seen as in building construction; "ninety per cent done" can persist for a long time.
- **Requirements are uncertain** and change.
- **Estimates are difficult,** because each project is partly new.
- **Productivity varies** widely between people and situations.
- **Dependencies are tangled:** parts of a system affect each other in unexpected ways.
- **People are the main resource,** and people are not interchangeable.
- **Success measures differ** between stakeholders.

Unit 1 listed the common reasons for failure; the topics in this unit are the management responses to them.

## What Success Means

A project can meet the plan and still fail if nobody uses the product, and a project can miss the plan and still be valuable. Good management defines success at several levels.

- **Delivery success:** on time, on budget, within scope.
- **Product success:** quality is good, and it works for users.
- **Business success:** it delivers the benefits that justified it.
- **Team success:** the people stay healthy and learn.

<!--
IMAGE PROMPT  ->  generate as images/01_the_project_triangle.png   (16:9 explanatory diagram, place here)

A triangle with corners Scope, Time, Cost and Quality in the centre. Three small panels show what happens when one corner is pushed: scope up (time and cost stretch, quality drops), time cut (scope shrinks or cost rises), cost cut (scope shrinks or time grows).

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Balance the Constraints

1. A customer asks for three extra features and insists the delivery date and budget stay the same. What are the choices?
2. A team is told to finish a month early with the same scope and the same people. What is likely to give?
3. Name two ways of managing change that suit adaptive projects.

For case 1, add time or people (which raises cost), remove other scope of equal size, or accept lower quality, ideally by explicit decision. For case 2, quality, because the team will cut testing and review, or overtime will harm the team. For case 3, a prioritised backlog and time-boxed iterations in which new items displace less valuable ones.

## Conclusion

Software project management is the planning, organising, monitoring, and controlling of people, work, and resources so that a software product is delivered that meets its agreed goals within the constraints of scope, time, cost, and quality. Its heart is making the trade-offs between those constraints visible and deliberate.

To manage a project, the work must first be broken into pieces that can be planned and tracked. The next topic describes work breakdown and scheduling.
