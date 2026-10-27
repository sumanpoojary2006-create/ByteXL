## Introduction

A software project succeeds or fails in the minds of the people who judge it. Those people, the stakeholders, include users, customers, sponsors, other teams, regulators, and the engineers themselves, and each holds expectations about what will be delivered, when, and at what cost. Technically excellent work can still be judged a failure if expectations were never aligned, and an imperfect delivery can be judged a success if people were informed and involved throughout. Managing stakeholders means identifying who matters, understanding what they need, communicating deliberately, and negotiating the inevitable conflicts.

This topic explains how to identify and analyse stakeholders, how to plan communication, how expectations form and are managed, how to negotiate, and how to say no constructively.

**Definition:** Stakeholder management is the practice of identifying the people and groups who affect or are affected by a project, understanding their needs and influence, and engaging and communicating with them so that their expectations are aligned with what the project can realistically deliver.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_managing_stakeholders_and_expectations.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A two-by-two grid with Influence vertical and Interest horizontal containing small person icons placed in the four quadrants, with a communication arrow from a central project box to each quadrant.

ON-IMAGE TEXT: show a short bold title "Managing Stakeholders and Expectations" plus only these few labels, large and legible: Who Matters, and How Much. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Who Are the Stakeholders?

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Group</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical concerns</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sponsors and executives</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those who fund and champion the project</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Return on investment, strategy, risk, schedule</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customers and buyers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those who pay for the product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Value, price, fit to need</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">End users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those who use the product daily</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability, reliability, support for their tasks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business owners and product managers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those who define what the product should do</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Features, priorities, market timing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivery team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers, testers, designers, analysts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear goals, sustainable pace, technical quality</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations and support</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those who run and support the product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stability, monitoring, documentation, handover</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security, legal, compliance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those who protect the organisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regulations, privacy, audits, risk</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Other teams and partners</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Teams that depend on or are depended on by this project</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interfaces, dates, impacts on their work</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vendors and suppliers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those who provide components or services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear requirements, payment</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regulators and the public</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Those affected by the product or its failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safety, privacy, fairness</td>
    </tr>
  </tbody>
</table>

Missing a stakeholder is a classic cause of late surprises: the security team that first sees the design a week before launch, or the support team that learns of a new product on release day.

## Analysing Stakeholders

Once identified, stakeholders are analysed to decide how to engage them.

### The Power and Interest Grid

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Low interest</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">High interest</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High power (influence)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep satisfied: brief them on major decisions, avoid unpleasant surprises</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manage closely: involve in decisions, communicate often</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low power (influence)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monitor: minimal effort, watch for change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep informed: regular updates, consult for feedback</td>
    </tr>
  </tbody>
</table>

Other useful questions are: what does each person **want** and **fear;** are they a supporter, neutral, or resistant; what do they **need to know** and **when;** and who **influences** them. Informal power matters, for the long-serving expert whose opinion shapes the decision of the executive, for example.

### Requirements and Conflict

Stakeholders want different, sometimes contradictory, things: sales wants features, operations wants stability, finance wants lower cost, users want simplicity, security wants restrictions. These are not mistakes to be removed but trade-offs to be made visible. The requirements engineering of Unit 3 provides the techniques for eliciting, prioritising, and negotiating needs; this topic concerns the continuing relationship.

## Communication Planning

A **communication plan** records who needs what information, in what form, how often, and from whom.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Audience</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sponsor; product owner; operations lead</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decision, awareness, feedback, or approval</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Content</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Progress, risks, budget, changes, demonstrations</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Format</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dashboard, written report, demonstration, meeting, chat channel</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Frequency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Daily, weekly, per iteration, at milestones, on exceptions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Owner</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who prepares and delivers it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feedback route</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How the audience can respond</td>
    </tr>
  </tbody>
</table>

### Principles of Good Communication

- **Know the audience.** Executives need outcomes, risks, and decisions; engineers need detail; users need what changes for them. Use their language, not internal jargon.
- **Lead with the message.** State the conclusion and what is wanted, then supply the support.
- **Be early and be honest.** Bad news does not improve with age. Stakeholders forgive problems reported promptly with a plan, and do not forgive hidden ones.
- **Prefer showing to telling.** A working demonstration builds more confidence than a status report.
- **Use the right channel.** Use written records for decisions and commitments, conversations for sensitive or complex matters, and shared channels for routine updates.
- **Be consistent** in rhythm and format, so that people know when and where to find information.
- **Listen.** Communication runs both ways; stakeholders' concerns often reveal requirements and risks.
- **Record decisions** with who made them, when, and why.
- **Avoid overload.** Too many messages are ignored.

### Agile Mechanisms

Agile practice builds stakeholder engagement into the process: a product owner who represents the business, end-of-iteration **reviews** where stakeholders see working software and give feedback, visible boards and roadmaps, and frequent releases. These give continuous, concrete conversation in place of a distant approval at the end.

## Expectations

An **expectation** is a belief about the future, and it forms early. The first number a stakeholder hears often becomes the number they remember; a casual remark ("it should be quick") may be taken as a promise.

### How Gaps Arise

- **Vague or unstated requirements,** where each side assumes the other understands.
- **Optimistic early estimates** given before the facts were known and treated as commitments.
- **Over-selling** to win approval or a contract.
- **Silence** during the project, so beliefs drift away from reality.
- **Changes not communicated:** scope, schedule, and trade-offs altered without telling those affected.
- **Demonstrations that hide shortcuts,** making unfinished work look finished.
- **Different meanings** of the same words: "done," "urgent," "simple," "supported."

### Managing Them

1. **Make the goals, scope, and exclusions explicit** and written down. What is **not** included is as important as what is.
2. **Share estimates as ranges** with assumptions, and refine them (see topic 3).
3. **Agree on the definition of done** and on acceptance criteria.
4. **Show progress early and often.**
5. **Report changes and their consequences promptly.**
6. **Under-promise and over-deliver,** or at least promise only what you can deliver with confidence.
7. **Agree on how disagreement is resolved** and who has the final say.
8. **Check understanding** by asking people to restate what they expect.

## Negotiation

Projects involve continual negotiation over scope, priority, schedule, and resources. Useful principles come from the Harvard Negotiation Project (Roger Fisher and William Ury, *Getting to Yes*).

- **Separate the people from the problem.** Be firm on the issue and kind to the person.
- **Focus on interests, not positions.** The position "we need the report by Friday" may rest on the interest "the board meets on Monday," which can be met in other ways.
- **Generate options** for mutual gain before deciding.
- **Use objective criteria,** such as data, standards, or independent estimates, rather than a contest of wills.
- **Know your alternative** if no agreement is reached.
- **Make trade-offs visible:** "we can add this feature if we defer that one, or move the date."

## Saying No

Engineers and managers must often decline or push back: on an extra feature, an impossible date, a risky shortcut, or a security compromise. A bare "no" damages relationships; agreeing to everything damages the project. A constructive refusal:

1. **Acknowledges the need** behind the request.
2. **States the constraint plainly and with evidence,** such as capacity, risk, or cost.
3. **Offers alternatives:** a smaller version, a later date, a different approach, or a trade-off ("yes, if we drop X").
4. **Leaves the decision with those who own it,** with the consequences clearly stated, rather than quietly absorbing the cost.
5. **Records the outcome.**

Phrases such as "Yes, and here is what it would take" or "We can do A or B, not both in this time" turn a refusal into a choice. Some matters, such as safety, legality, and ethics, are not negotiable, and the professional responsibility to refuse is covered in Unit 14.

## Difficult Situations

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Situation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Response</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Constant changes of mind</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make the cost of change visible; use a prioritised backlog; hold regular reviews so changes are made together</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stakeholder who is absent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Escalate need for a decision-maker; define who may decide in their place; document assumptions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conflicting stakeholders</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bring them together with data; seek the underlying interests; escalate to the sponsor for a ruling if needed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Executive pressure to hit an unrealistic date</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Present options with consequences (scope, resources, quality, risk); do not silently agree</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scope creep from "small requests"</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Route all requests through the same prioritisation; show what is displaced</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Surprise bad news</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Report it immediately with the facts, impact, options, and recommended action</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resistant users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Involve them early; understand fears; provide training and support</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Blame after failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Focus on facts and learning; use blameless review</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/08_stakeholder_grid_and_communication.png   (16:9 explanatory diagram, place here)

Left: power and interest grid with four labelled quadrants and example stakeholder icons. Right: a table-like strip showing audience, message, channel, and frequency as four columns with icons, and a gap between Expected and Delivered closing as communication arrows are added.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Align the Expectations

1. A senior executive has high influence and low day-to-day interest in a project. How should they be engaged?
2. A stakeholder asks for an additional feature two weeks before release. Give a constructive response.
3. Why is it useful to write down what is out of scope?

For case 1, keep satisfied: brief them on major decisions and risks without burdening them with detail, and avoid surprises. For case 2, acknowledge the value, explain the effect on date, risk, or other items, and offer options: defer to the next release, swap for something of equal size, or move the date. For case 3, because unstated exclusions are the source of mismatched assumptions, and a written list gives a reference when disputes arise.

## Conclusion

Stakeholder management is the practice of identifying the people and groups who affect or are affected by a project, understanding their needs and influence, and engaging and communicating with them so that their expectations are aligned with what the project can realistically deliver. Early and honest communication, explicit scope, visible trade-offs, and constructive negotiation keep trust intact when plans change.

Many projects also involve people outside the organisation. The next topic covers outsourcing, contracts, and vendor management.
