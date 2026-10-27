## Introduction

Every project is a bet on an uncertain future. Key people may leave, a supplier may be late, a technology may not behave as hoped, requirements may change, or a security flaw may surface just before release. A risk is an uncertain event or condition that, if it occurs, has an effect on the objectives of the project. Risk management is the practice of thinking about these possibilities in advance, deciding which deserve attention, and preparing responses, so that problems become manageable events instead of crises.

This topic explains the nature of risk, the steps of the risk management process, how to assess and respond to risks, the typical risks of software projects, and how to keep risk management alive during the project.

**Definition:** A risk is an uncertain event or condition that, if it occurs, would affect project objectives (positively or negatively), and risk management is the systematic process of identifying, analysing, responding to, and monitoring risks throughout the life of a project.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_risk_management.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A cycle of four stages in a ring (Identify, Assess, Respond, Monitor) around a central risk register table; to the right a grid with Probability on one axis and Impact on the other, coloured green, orange, and red.

ON-IMAGE TEXT: show a short bold title "Risk Management" plus only these few labels, large and legible: Identify, Assess, Respond, Monitor. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Risks, Issues, and Assumptions

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Something that might happen</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The payment provider might change its interface during the project</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Issue</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A risk that has happened, or a problem that exists now</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The payment provider has changed its interface</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assumption</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A belief taken as true for planning; if wrong, it creates a risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The provider will remain stable</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Constraint</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A fixed limit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The launch date is set by a trade show</td>
    </tr>
  </tbody>
</table>

A risk has two measurable aspects: its **probability** (how likely) and its **impact** (how severe the consequences). Together they give its **exposure.** A frequent, minor event and a rare, catastrophic one may deserve different responses.

Risk is not always negative. An **opportunity** is a possible event with a beneficial effect, such as a reusable component becoming available, and can be managed in the same way: exploit it, share it, or enhance it.

## The Risk Management Process

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Step</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Output</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1. Plan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decide how risk will be managed: roles, scales, thresholds, and review frequency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk management approach</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2. Identify</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find and describe possible risks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk list</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3. Analyse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate probability and impact, and rank</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prioritised risk register</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4. Respond</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose and plan actions for the important risks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mitigation, contingency, and owners</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5. Monitor and review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Track risks, watch for triggers, and find new ones</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Updated register and reports</td>
    </tr>
  </tbody>
</table>

## Identifying Risks

Risks hide in optimistic plans, so deliberate technique is required.

- **Brainstorming** with the whole team, including those who do the work, since they see the dangers first.
- **Checklists** based on experience: lists of common risks by category help ensure nothing standard is forgotten.
- **Assumption analysis:** list the assumptions and ask what happens if each fails.
- **Pre-mortem:** imagine the project has failed completely a year from now, and each person writes down why. This overcomes the reluctance to say negative things in a planning meeting.
- **Review of past projects** and their retrospectives.
- **Interviews** with experts and stakeholders.
- **Analysis of the plan:** every dependency, estimate, and new technology is a source.
- **Threat modelling** for security risks, covered in Unit 14.

### Categories of Software Project Risk

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Category</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unclear or incomplete requirements; frequent changes; scope creep; conflicting stakeholders</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New or immature technology; performance targets uncertain; complex integration; poor architecture; insufficient test environments</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimation and schedule</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Optimistic estimates; unrealistic deadline; hidden work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Key person leaves or falls ill; lack of skills; low motivation; conflicts; high turnover; overwork</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Organisational</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changing priorities; funding cut; lack of sponsor support; reorganisation; competing projects</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">External</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Late vendors; third-party service changes; regulations; market change; economic conditions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Other teams late; shared platforms unstable</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality and security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects found late; security vulnerabilities; data loss; compliance failure</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deployment problems; capacity shortfalls; lack of monitoring or support readiness</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Skipping reviews and tests under pressure; poor communication; unclear ownership</td>
    </tr>
  </tbody>
</table>

Barry Boehm's well-known list of top software risks included personnel shortfalls, unrealistic schedules and budgets, wrong functions and user interfaces, gold plating, continuing requirements changes, shortfalls in externally supplied components, and shortfalls in real-time performance.

## Analysing Risks

### Qualitative Analysis

Each risk is rated for probability and impact on a simple scale (low, medium, high; or one to five), and placed on a **probability and impact matrix.** The product gives a priority.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Low impact</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Medium impact</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">High impact</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High probability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Medium</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Critical</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Medium probability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Medium</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low probability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Medium</td>
    </tr>
  </tbody>
</table>

Attention goes to the critical and high cells first. Other factors may also influence priority: **proximity** (how soon it might occur), **detectability** (whether warning signs are likely), and **how far the effect spreads.**

### Quantitative Analysis

Where more rigour is warranted, exposure is computed as probability times the cost of the impact, in money or days. Techniques include **expected monetary value, decision trees, sensitivity analysis,** and **Monte Carlo simulation,** which runs the schedule or cost model many thousands of times with random values drawn from the estimated ranges, to produce a distribution of outcomes: for example, a 50 per cent chance of finishing by one date and 90 per cent by a later date.

## Responding to Risks

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change the plan so that the risk cannot occur</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Drop an unproven technology and use a mature one</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mitigate (reduce)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lower the probability or the impact</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build a prototype early to test performance; cross-train team members</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transfer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pass the consequence to someone else</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Insurance; fixed-price contract; use a managed service</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accept</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do nothing in advance, consciously</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minor risks where the cost of action exceeds the benefit; with or without a contingency reserve</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Escalate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pass to someone with authority to decide</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A risk outside the project scope</td>
    </tr>
  </tbody>
</table>

Two kinds of planned response matter.

- **Mitigation actions** are taken **now** to reduce the risk. They cost effort and appear in the plan.
- **Contingency plans** are prepared **in advance** but triggered **only if** the risk occurs, for example a fallback vendor. Each has a **trigger,** the observable sign that tells you the risk is materialising, and an owner.

A **contingency reserve** of time or budget, sized from the risks, is a sensible part of the plan, and a **fallback** (plan B) for the most dangerous items is wise.

### Techniques Particularly Suited to Software

- **Spike or prototype** to answer a technical question early.
- **Tackle the riskiest work first,** so that unwelcome surprises appear while there is time and money. This is a key principle of iterative and agile development, and of the spiral model of Unit 2.
- **Incremental delivery** to learn from real users early.
- **Feature flags and gradual rollout** to limit the damage of a faulty release.
- **Automated testing and continuous integration** to reduce quality risk.
- **Pairing, documentation, and rotation** to reduce dependence on single individuals (the "bus factor": how many people would have to disappear before the project stalled).
- **Reuse of proven components** rather than building everything.
- **Clear agreements** with suppliers and defined interfaces.
- **Backups, disaster recovery plans,** and tested rollback.

## The Risk Register

The central tool is a simple table, updated regularly.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Field</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Content</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ID and title</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A short name</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Description</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The cause, the event, and the consequence</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Category</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Type of risk</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Probability and impact</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ratings and resulting priority</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Owner</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The person responsible for monitoring and responding</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Response</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strategy and specific actions with dates</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trigger</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The warning sign</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Status</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Open, mitigated, occurred, or closed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Last reviewed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Date of last review</td>
    </tr>
  </tbody>
</table>

A good description uses the form: **because of (cause), there is a risk that (event) will happen, resulting in (effect).** This avoids vague entries such as "bad requirements."

## Keeping Risk Management Alive

- **Review risks regularly,** for example at each planning meeting, retrospective, or milestone. A register made at the start and never opened is worthless.
- **Add new risks** and **retire** those that have passed.
- **Make it safe to raise risks.** Teams that punish bad news hear less of it, and then hear it too late.
- **Assign an owner** to each important risk; a risk with no owner is not managed.
- **Report the top risks** to stakeholders, with decisions needed.
- **Learn from outcomes:** compare what happened with what was predicted.
- **Keep it proportionate.** A small project needs a short list reviewed weekly, not a heavy process.

## Common Mistakes

- Treating risk as an activity done once at the start.
- Listing only technical risks and ignoring people and organisational ones.
- Rating everything medium, so nothing is prioritised.
- Writing risks that are really issues, or vague worries.
- Mitigation with no action, owner, or date.
- Optimism and wishful thinking, or blaming those who report problems.
- Confusing risk acceptance with risk ignorance.

<!--
IMAGE PROMPT  ->  generate as images/05_probability_impact_matrix_and_responses.png   (16:9 explanatory diagram, place here)

Left: a three-by-three heat grid, probability up, impact across, with a few labelled risk dots. Right: four response icons (Avoid, Mitigate, Transfer, Accept) each with a one-line label, and a timeline showing a trigger marker leading to a contingency plan.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Manage the Risk

1. Only one developer understands the payment module. Write the risk in the standard form and suggest a mitigation.
2. A team is unsure whether a new database will meet the performance target. What is a sensible early action?
3. What distinguishes a mitigation from a contingency plan?

For case 1, because knowledge is concentrated in one person, there is a risk that her or his absence will stop work on payments, resulting in delay; mitigate by pairing, documentation, and rotation. For case 2, a spike or prototype with realistic load, done early, with the result feeding the decision. For case 3, mitigation acts now to reduce the probability or the impact; a contingency plan waits for a trigger and acts only if the risk occurs.

## Conclusion

A risk is an uncertain event or condition that, if it occurs, would affect project objectives (positively or negatively), and risk management is the systematic process of identifying, analysing, responding to, and monitoring risks throughout the life of a project. Done regularly and openly, it turns surprises into planned responses.

Many of the largest risks are about people and how they are organised. The next topic examines team organisation and productivity.
