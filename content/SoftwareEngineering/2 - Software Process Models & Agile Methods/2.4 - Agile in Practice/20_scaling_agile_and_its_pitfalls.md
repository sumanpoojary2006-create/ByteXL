## Introduction

Agile methods were designed for small teams of a few people sitting together. Large products need many teams, sometimes hundreds of people, who must coordinate dependencies, share an architecture, and deliver a coherent product. Scaling frameworks try to preserve agility under these conditions, and the history of agile adoption also shows recurring ways in which organisations adopt the vocabulary but lose the benefits.

**Definition:** Scaling agile is the effort to coordinate many teams so that they can work with agile principles on one large product, and agile pitfalls are the recurring adoption mistakes in which practices are followed in form but not in intent.

<!--
IMAGE PROMPT  ->  generate as images/20_intro_scaling_agile_and_its_pitfalls.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Several small team circles connected by thin coordination lines into a larger network around a shared product, with a few warning signs marking broken links.

ON-IMAGE TEXT: show a short bold title "Scaling Agile and Its Pitfalls" plus only these few labels, large and legible: Teams, Coordination, Pitfalls. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Scaling Is Difficult

- **Dependencies.** Teams need output from one another, so waiting and handoffs reappear.
- **Shared architecture.** Several teams changing the same system must agree on structure and interfaces.
- **Alignment.** Many backlogs can pull in different directions unless there is a common vision and priority.
- **Communication.** The number of communication paths grows rapidly with the number of people, as the roles topic showed.
- **Integration.** Many streams of work must come together into one working product, frequently.

Conway's Law describes a related effect: the structure of a system tends to mirror the communication structure of the organisation that builds it. Organising teams around parts of the product, instead of around technical layers, reduces coordination.

## Common Approaches

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Approach</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Main idea</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scrum of Scrums</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Representatives of each team meet regularly to share progress and resolve cross-team issues</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large-Scale Scrum (LeSS)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One product backlog and one Product Owner for many teams, keeping Scrum principles with minimal added structure</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nexus</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An integration team coordinates three to nine Scrum teams working on one product backlog</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scaled Agile Framework (SAFe)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A comprehensive framework with levels such as team, programme, and portfolio, including planning events across many teams</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team topologies and platform teams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Organise teams by type, such as stream-aligned and platform teams, to reduce dependencies</td>
    </tr>
  </tbody>
</table>

Company-specific models, such as squads and tribes made popular by one well-known streaming company, are descriptions of how that organisation worked, and are not frameworks that guarantee success elsewhere.

## Principles That Scale

Regardless of framework, effective scaling tends to follow the same ideas.

- Keep **teams small and cross-functional**, with the skills to deliver without constant handoffs.
- Provide a single, clear **product vision and priority order**.
- **Reduce dependencies** by design: loose coupling in architecture, and ownership aligned to teams.
- **Integrate continuously** across teams, with shared automation.
- Align regularly through short, shared planning and review events.
- Invest in **platforms and shared tooling** so that teams do not each rebuild the basics.

## Common Pitfalls

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pitfall</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cargo cult agile</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ceremonies are performed without understanding their purpose, so nothing improves</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Return to the values and ask what each practice is for</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Water-Scrum-Fall</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agile development is sandwiched between a long up-front planning phase and a late, manual release phase</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extend agility to requirements and delivery</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Velocity as a target</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Points are inflated and measured as performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use velocity only for forecasting</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Skipped retrospectives</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improvement stops because the team is too busy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protect the time, and follow through on actions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Absent Product Owner</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Questions wait, priorities blur, and work is built on guesses</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Empower and make available a single decision maker</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Zombie Scrum</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Events happen but the team delivers nothing of value and nobody cares</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reconnect work to user feedback and real outcomes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No technical practices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speed increases defects, debt grows, and the team slows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invest in testing, integration, and design quality</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agile as an excuse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"We are agile" justifies having no plans, no documentation, and no discipline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remember that agility needs more discipline, not less</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_water_scrum_fall.png   (16:9 explanatory diagram, place here)

A horizontal bar split into three: a long grey block labelled Up-front planning, a thin agile loop block labelled Sprints, and a long grey block labelled Manual release phase. A warning label says Agile only in the middle.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Culture Over Process

Many pitfalls come from treating agile as a procedure to install. Organisations that gain from agile typically also change how they plan, fund, and manage: trusting teams, accepting honest information about progress, and being willing to hear bad news early. Process changes without this cultural change tend to produce the pitfalls above.

## Your Turn: Spot the Pitfall

1. A company reports that its teams are "agile," but each release still requires six months of analysis beforehand and three months of manual testing afterwards.
2. A manager sets a target that every team's velocity must rise 10% each quarter.
3. A team stops holding retrospectives because of a deadline, and the same problems recur every sprint.

Case 1 is Water-Scrum-Fall. Case 2 is velocity as a target, which will inflate the numbers without improving delivery. Case 3 is skipped retrospectives, which breaks the loop that produces improvement.

## Conclusion

Scaling agile is the effort to coordinate many teams so that they can work with agile principles on one large product, and agile pitfalls are the recurring adoption mistakes in which practices are followed in form but not in intent. The remedy for both is to keep returning to the values and to ask what each practice is meant to achieve.

Whatever the framework, teams succeed or fail on how well people communicate. The last topic of this unit looks at effective communication and collaboration.
