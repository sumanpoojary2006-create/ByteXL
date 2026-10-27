## Introduction

Every system of any size fails sometimes: a deployment goes wrong, a dependency stops responding, a disk fills, a certificate expires, a traffic spike arrives. What distinguishes strong engineering organisations is not that they avoid failure altogether, which is impossible, but how they respond: calmly, in an organised way, restoring service quickly, and then learning so that the same failure does not recur. Incident response is the first part, and the blameless postmortem is the second.

**Definition:** An incident is an unplanned event that disrupts or degrades a service, incident response is the organised process of detecting, coordinating, mitigating, and resolving it, and a postmortem is a structured, blameless review afterwards that records what happened, why, and what will be changed to prevent or reduce recurrence.

<!--
IMAGE PROMPT  ->  generate as images/22_intro_incident_response_and_postmortems.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A control room scene: a timeline of an incident from Detect through Triage, Mitigate, Resolve with a clock, a role board with Incident commander, Communications, Operations, and a document labelled Postmortem with a lightbulb.

ON-IMAGE TEXT: show a short bold title "Incident Response and Postmortems" plus only these few labels, large and legible: Respond, Restore, Learn. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Counts as an Incident

An incident is any event that affects users or the business significantly enough to need a coordinated response: an outage, serious slowness, data loss, a security breach, or a failing release. Teams classify incidents by **severity** so that the response matches the impact.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Severity</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical response</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Severity 1 (critical)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Major outage or data loss affecting many users or core functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Immediate response, around the clock, senior involvement, executive notification</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Severity 2 (high)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Significant degradation or partial outage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Urgent response during working hours or on call</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Severity 3 (medium)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limited impact or a workaround exists</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handle within normal work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Severity 4 (low)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minor issue</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ticket and schedule</td>
    </tr>
  </tbody>
</table>

The scales differ by organisation, but clear definitions avoid argument during a crisis.

## Preparation

Good response depends on what is done beforehand.

- **On-call rotations:** named people reachable at all times, with a fair schedule, handover, and support. On-call must be sustainable.
- **Monitoring and alerting** that detect problems quickly, as the previous topic described.
- **Runbooks:** documented procedures for known failure modes, with steps, commands, and decision points, so a tired person at three in the morning can act correctly.
- **Defined roles and a process,** practised in advance.
- **Access and tools** ready: dashboards, logs, deployment and rollback abilities, communication channels.
- **Contact lists and escalation paths.**
- **Game days:** rehearsals in which teams practise responding to simulated failures, and **chaos engineering**, the deliberate injection of faults, pioneered by Netflix with its Chaos Monkey tool, to find weaknesses before they cause real incidents.

## Roles in an Incident

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Responsibility</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Incident commander</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Leads the response, makes decisions, keeps the team focused and organised; does not usually perform the technical work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations (technical) lead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Directs the investigation and the technical fix</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Communications lead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keeps stakeholders, support staff, and users informed, using a regular update rhythm</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scribe</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Records the timeline, actions, and decisions as they happen</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Subject-matter experts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Brought in as needed for particular systems</td>
    </tr>
  </tbody>
</table>

In a small incident one person may combine roles, but **separating coordination from technical work** is the most important discipline in a large one.

## The Phases of a Response

1. **Detect.** An alert, a customer report, or an observation reveals the problem. Faster detection is the biggest lever on impact.
2. **Triage.** Assess the scope and severity, assign an incident commander, and open a communication channel.
3. **Mitigate.** **Stop the harm first.** Restore service as quickly as possible by whatever safe means: roll back a release, switch off a feature flag, fail over to a backup, add capacity, block bad traffic. Do not search for the root cause while users are still suffering, unless that is the fastest route to mitigation.
4. **Resolve.** Apply a proper fix, verify that the service is healthy, and monitor for recurrence.
5. **Communicate** throughout: acknowledge the incident, say what is known and unknown, give the next update time, and announce resolution. Status pages and honest, regular messages keep trust.
6. **Review.** Hold the postmortem.

## Good Practices During an Incident

- **Stay calm and structured.** Panic and parallel, uncoordinated changes make things worse.
- **Make one change at a time** and observe the effect, recording each.
- **Keep a written timeline.**
- **Prefer reversible actions.**
- **Ask for help early,** and rotate people on long incidents, since tired people make mistakes.
- **Separate the channels:** one for the technical team, one for stakeholder updates.
- **Do not hide or minimise.** Accurate information beats comfortable information.

## Measuring Response

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time to detect (MTTD)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How long from the start of the problem until it was noticed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time to acknowledge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How long until a person took ownership</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time to mitigate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How long until user impact was reduced</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time to restore (MTTR)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How long until service was restored; "MTTR" is used with several slightly different meanings, so teams should define it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Incident frequency and severity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How often and how serious</td>
    </tr>
  </tbody>
</table>

The averages hide the worst cases, and they are best used to look at trends and to improve, not as targets.

## The Blameless Postmortem

After the incident, the team writes and discusses a **postmortem** (also called an incident review). The practice, described in the influential 2012 article on blameless postmortems by John Allspaw at Etsy and widely adopted since, rests on a conviction: **people make reasonable decisions with the information they have, and failures are caused by weaknesses in systems and processes, not by individual carelessness.** Blaming individuals teaches people to hide mistakes, and so the organisation loses the information it needs to improve.

### Contents of a Postmortem

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Section</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Content</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Summary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What happened, in a few sentences</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Impact</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who and what was affected, for how long, with measures such as users, orders, or revenue</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Timeline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A factual, time-stamped sequence of events, from the first sign to resolution</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detection and response</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How it was noticed, how the team responded, what helped and what delayed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Root causes and contributing factors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The conditions that allowed the incident, usually several, including technical, process, and organisational ones</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What went well, what went poorly, where we got lucky</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Balanced reflection; luck is a warning of a gap</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Action items</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specific, owned, time-bound changes to prevent or reduce recurrence and to improve detection and response</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lessons learned</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What others in the organisation should know</td>
    </tr>
  </tbody>
</table>

### Finding Causes

Failures rarely have a single root cause. The "five whys" technique, asking why repeatedly, can help, but it can oversimplify by following one chain. Better reviews look for **multiple contributing factors**, such as the missing test, the unclear alert, the risky deployment process, and the pressure to release, in the spirit of the Swiss cheese model of Unit 1: several defences failed at once.

### Making It Work

- **Hold the review soon,** while memory is fresh, and **for all significant incidents,** including near misses.
- **Focus on how and why,** not who.
- **Write it down and share it widely,** so others learn.
- **Follow through on actions.** A postmortem without completed actions is theatre. Track them like other work.
- **Review trends** across incidents to find systemic issues.
- **Celebrate learning,** and thank those who surface problems.

<!--
IMAGE PROMPT  ->  generate as images/02_incident_lifecycle_and_postmortem_loop.png   (16:9 explanatory diagram, place here)

A timeline from Problem starts through Detect, Triage, Mitigate, Resolve, with MTTD and MTTR spans marked, and a loop at the end through Postmortem to Action items to Prevention back into the system. A side card lists roles Commander, Operations, Communications, Scribe.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: What Comes First?

1. A release has caused a spike in errors, and a rollback is available.
2. During an incident, a manager asks who is responsible for the faulty change.
3. After resolution, the team writes up the timeline and the contributing factors.

In case 1, mitigate first: roll back to restore service, then investigate the cause. In case 2, the incident is not the time for blame; focus on restoring service, and later examine the conditions that allowed the change to cause harm, in a blameless review. Case 3 is the postmortem, the learning step.

## Conclusion

An incident is an unplanned event that disrupts or degrades a service, incident response is the organised process of detecting, coordinating, mitigating, and resolving it, and a postmortem is a structured, blameless review afterwards that records what happened, why, and what will be changed to prevent or reduce recurrence. Mitigating first, communicating honestly, and learning without blame turn failures into improvement.

The practices of this unit, from version control to postmortems, share a common spirit about how development and operations work together. The final topic describes it: the DevOps culture.
