## Introduction

Raw requirements from many stakeholders rarely fit together neatly. Some conflict, some are unclear, some cannot be built within budget, and some quietly assume things that are not true. Analysis is the work of examining requirements for these problems, and negotiation is the work of reaching agreements that stakeholders will support. Neither is purely technical: both depend on evidence, listening, and clear communication.

**Definition:** Requirements analysis is the examination of gathered requirements for problems such as conflict, ambiguity, incompleteness, and infeasibility, and negotiation is the process by which stakeholders agree on resolutions and on the scope that will be built.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_requirements_analysis_and_negotiation.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three stakeholder figures around a table each holding a puzzle piece that does not quite fit, while an analyst in the middle slides a compromise piece into place.

ON-IMAGE TEXT: show a short bold title "Requirements Analysis and Negotiation" plus only these few labels, large and legible: Analyse, Conflict, Agree. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Analysis Looks For

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conflict</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two requirements cannot both be satisfied</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One group wants no login; another requires full identification</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ambiguity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A statement can be read in several ways</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Users can see their orders" (which users? what period?)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Incompleteness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needed information is missing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No behaviour defined when payment fails</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplication</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same need stated twice, possibly differently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two separate statements describing order cancellation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Infeasibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cannot be done within technology, budget, or time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Real-time results from data that arrives once a day</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gold plating</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Features nobody needs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An elaborate feature with no identified user</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden assumptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unstated beliefs that may be false</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assuming every user has constant internet access</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Untestability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No way to check if it is met</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"The system shall be intuitive"</td>
    </tr>
  </tbody>
</table>

## Techniques

- **Checklists** of common problems, applied to each requirement and to the whole set.
- **Modelling** the requirements, for example with use case, data, and process diagrams. Drawing often reveals gaps and contradictions that prose hides.
- **Prototyping** to test doubtful or high-risk requirements.
- **Feasibility analysis** covering technical, economic, legal, operational, and schedule feasibility.
- **Risk analysis** to identify requirements that threaten the project, such as new technology or a dependence on another team.
- **Interaction matrices** that compare requirements pairwise to find conflicts.

## Types of Conflict

Conflicts have different sources, and the approach depends on the source.

- **Conflicting information or facts:** resolved by finding out which is correct.
- **Conflicting goals:** stakeholders want different outcomes, so a decision on priorities is needed.
- **Conflicting interests:** one party gains while another loses, requiring negotiation.
- **Conflicting values or constraints:** based on rules or beliefs, which may require escalation to someone with authority.

## Principles of Negotiation

Requirements negotiation works best when it follows principles taken from the study of principled negotiation.

1. **Separate people from the problem.** Disagreement is about requirements, not personalities.
2. **Focus on interests, not positions.** A stated position ("we must have feature X") often hides an interest ("we need to meet audit deadlines") that other solutions could also meet.
3. **Generate options for mutual gain** before choosing.
4. **Use objective criteria**, such as cost estimates, user research, or regulation, to evaluate options.
5. **Be transparent** about costs and trade-offs so that stakeholders can make informed decisions.

## Managing Scope

Negotiation ends in an agreed **scope**: the set of requirements the project commits to deliver. Good practice makes scope explicit by listing what is included and also what is explicitly excluded. Items outside scope are recorded, not forgotten, so that they can be revisited later. Vague scope is a main cause of later disputes and overrun.

<!--
IMAGE PROMPT  ->  generate as images/02_position_vs_interest.png   (16:9 explanatory diagram, place here)

Three stakeholders each shown as an iceberg: the visible tip labelled Position (We must have feature X), and the much larger underwater part labelled Interest (the real need), with one shared option connecting the underwater parts.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Resolve the Conflict

The finance team requires that every order be approved by a manager before payment. The sales team requires that customers complete purchases with no delay.

1. State each team's likely underlying interest.
2. Suggest an option that serves both.

The finance team's interest is probably controlling fraud and large spending errors. The sales team's interest is not losing customers through friction. One option that serves both is to require approval only for orders above a threshold or for high-risk patterns, with other orders processed automatically, and with fast approval and notifications for those that need it.

## Conclusion

Requirements analysis is the examination of gathered requirements for problems such as conflict, ambiguity, incompleteness, and infeasibility, and negotiation is the process by which stakeholders agree on resolutions and on the scope that will be built. Looking beneath stated positions to underlying interests is the most reliable route to agreement.

Even an agreed set of requirements cannot all be built at once, or sometimes at all. The next chapter turns to ordering, recording, checking, and changing requirements, beginning with prioritisation.
