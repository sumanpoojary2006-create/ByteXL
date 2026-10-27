## Introduction

Engineers in most fields learn from failures. Bridge designers study the collapses of the past, aviation investigators publish accident reports for the whole industry, and surgeons review cases in which things went wrong. Software has the same need. Each major failure is an expensive experiment already paid for, and its lessons are available to anyone who takes the trouble to study it. Unit 1 introduced several classic cases. This topic offers a method for studying failures and examines further cases, drawing out the themes that recur.

**Definition:** Learning from failures is the practice of studying incidents and accidents systematically, reconstructing what happened and why, identifying the technical and organisational factors involved, and turning the findings into changes in practice, so that others do not repeat the same mistakes.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_learning_from_failures.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A library shelf of case-file folders labelled with years and short titles, an investigator reading one, and a shield-shaped lesson card pulled out with arrows pointing to Design, Process, Culture.

ON-IMAGE TEXT: show a short bold title "Learning from Failures" plus only these few labels, large and legible: Study, Extract, Apply. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## A Method for Studying a Case

1. **Reconstruct the facts** as a timeline: what happened, in order, according to reliable sources, such as official investigation reports.
2. **Identify the technical cause:** the defect or design decision that triggered the failure.
3. **Look for contributing factors:** requirements, testing gaps, process shortcuts, communication failures, organisational pressure, human factors, and regulatory weaknesses.
4. **Ask which defences failed or were missing:** reviews, tests, monitoring, safety mechanisms, using the Swiss cheese model.
5. **Separate hindsight from foresight.** It is easy to see after the event what was invisible before. Ask what information was available to the people at the time.
6. **Avoid blame.** Individuals acted within a system, and the system is what can be changed.
7. **Draw lessons and tie them to practice:** what would have prevented or reduced the harm?

## Cases Beyond Those in Unit 1

Unit 1 examined Ariane 5, the Mars Climate Orbiter, Knight Capital, and Therac-25. Further cases follow, summarised from public investigations and reporting.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Case</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happened</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technical cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Contributing factors and lessons</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patriot missile failure, Dhahran, 1991</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">On 25 February 1991 an air defence system failed to intercept a missile that struck a barracks, killing 28 US soldiers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system kept time as a count of tenths of a second held with limited precision, so a small rounding error grew with running time; after about 100 hours of continuous operation the error was large enough to put the tracking window in the wrong place</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system had been designed for short operation but was used continuously; a fix was in progress when the accident happened. Lessons: long-running behaviour, numeric precision, and operating conditions must be tested against how the system is actually used</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">North American blackout, 2003</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">On 14 August 2003 a cascading power failure left about 50 million people in the United States and Canada without electricity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A race condition in the alarm software of a control room stalled the alarm system, so operators were not alerted to failing power lines and were unaware of the growing problem</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operators trusted a system that had silently failed; inadequate monitoring of the monitoring. Lessons: concurrency defects in critical software, alarm design, and detection of the failure of monitoring tools themselves</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Heartbleed, 2014</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A flaw in a widely used encryption library allowed attackers to read portions of the memory of servers, exposing secrets such as keys and passwords</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A missing check on the length of a request in a heartbeat feature allowed reading beyond the intended data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A critical open-source component maintained by very few, underfunded people; code review and testing did not catch the flaw. Lessons: memory-unsafe languages, fuzzing, support for critical shared infrastructure, and rapid patching</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Boeing 737 MAX, 2018 and 2019</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two aircraft crashed within five months, one operated by Lion Air in October 2018 and one by Ethiopian Airlines in March 2019, killing 346 people; the fleet was grounded worldwide</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A flight control function (MCAS) could repeatedly push the nose down, based on the reading of a single angle-of-attack sensor, which could be faulty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliance on one sensor; pilots not adequately informed or trained about the function; schedule and commercial pressure; weaknesses in the certification oversight. Lessons: redundancy for safety-critical inputs, system-level hazard analysis, human factors, honest communication, and independent regulation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Post Office Horizon scandal, UK, 1999 to 2015 and after</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An accounting system used by branch operators showed false shortfalls; hundreds of subpostmasters were prosecuted, many were convicted, and many lost livelihoods, health, and reputations; convictions were later overturned and a public inquiry held</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software defects produced incorrect balances, and remote access to branch accounts was possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The organisation and the courts assumed the computer evidence was reliable and disbelieved the people; faults were denied; there was no independent scrutiny of the software. Lessons: software evidence can be wrong, systems must be auditable, defects must be acknowledged, and ethical responsibility for harm to users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CrowdStrike outage, 19 July 2024</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A faulty update to security software crashed millions of Windows computers (Microsoft estimated about 8.5 million) worldwide, disrupting airlines, hospitals, banks, and broadcasters</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A configuration update defined more input fields than the code supplied, leading to an out-of-bounds memory read in software running with high privilege, which crashed the machines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The update was released to all systems at once, not gradually; validation of the content was insufficient; the component ran at a level where a fault stops the whole machine. Lessons: staged rollouts and canaries, validation of configuration like code, limiting the blast radius of privileged components, and rapid recovery plans</td>
    </tr>
  </tbody>
</table>

## Recurring Themes

Reading across these and the earlier cases, the same patterns recur.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Theme</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Single points of failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One sensor (737 MAX); one alarm system (blackout); one release to all machines (CrowdStrike); one eager deployment step (Knight Capital)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assumptions that stopped being true</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reused software on a new rocket (Ariane 5); a system designed for short runs used for days (Patriot); units assumed to match (Mars Climate Orbiter)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inadequate testing of unusual conditions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long running time, rare timing, malformed input (Patriot, blackout, Heartbleed, Therac-25)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complexity and concurrency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Race conditions in the blackout and Therac-25</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Silent failure of monitoring and alarms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The blackout alarm; operators unaware of the real state</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Insufficient independent review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing hazard review (737 MAX), unreviewed code (Heartbleed), unexamined evidence (Horizon)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-trust in automation and in software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Therac-25 interlocks removed; Horizon evidence believed over people; pilots unprepared for automation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Schedule and commercial pressure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">737 MAX; Knight Capital; many others</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak operational practice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manual deployment (Knight Capital); no staged rollout (CrowdStrike)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Organisational culture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Denial and defensiveness (Horizon); normalisation of deviance</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lack of resources for critical infrastructure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Heartbleed</td>
    </tr>
  </tbody>
</table>

Almost none of these failures arose from a single programmer's slip. Each was a **chain**: a defect, plus untested conditions, plus missing safeguards, plus pressure, plus an organisation that did not listen.

## Practices That Help

- **Defence in depth,** as in the Swiss cheese model.
- **Staged rollouts, feature flags, and fast rollback,** to limit the blast radius (Unit 9).
- **Redundancy and independence** for critical inputs and safeguards.
- **Testing under realistic and extreme conditions,** including long running and failure of dependencies.
- **Independent review and hazard analysis,** and diversity of viewpoint.
- **Observability,** including monitoring of the monitors.
- **Pre-mortems:** before launch, imagine that the project has failed badly and ask why, a technique described by Gary Klein that surfaces risks people hesitate to voice.
- **Blameless postmortems** and learning from near misses, as in Unit 9.
- **Open reporting systems,** such as those used in aviation, where incidents can be reported without penalty and the lessons shared.
- **Honest communication** with users, regulators, and the public.
- **Ethical responsibility:** the codes of ethics of professional bodies place the safety and welfare of the public first, and Unit 14 returns to the subject.

## Using Cases in Your Own Work

Studying failures is not only history. For each case, ask of your own system: **Could this happen here?** Is there a single sensor, a single deploy path, an untested assumption, a monitoring tool that could fail silently, a critical dependency that nobody maintains? The most valuable use of a case study is to find the same weakness at home before it becomes an incident.

<!--
IMAGE PROMPT  ->  generate as images/02_failure_cases_timeline_and_themes.png   (16:9 explanatory diagram, place here)

A horizontal timeline with six case markers (1991 Patriot, 2003 Blackout, 2014 Heartbleed, 2018-19 737 MAX, 1999-2015 Horizon bar, 2024 CrowdStrike). Below, a row of theme icons connected to cases: Single point of failure, Broken assumption, Silent monitoring failure, Pressure, Culture. A Swiss cheese stack with aligned holes on the right.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Find the Pattern

1. A system has a single sensor feeding a safety decision. Which case does this recall, and what defence is missing?
2. A company releases a configuration update to every customer machine at the same moment. What could limit the damage?
3. Operators rely on an alarm that failed silently. What practice would help?

The first recalls the 737 MAX; the missing defence is redundancy and cross-checking of the critical input. The second recalls CrowdStrike and Knight Capital; staged or canary rollout and quick rollback would limit the damage. The third recalls the 2003 blackout; monitoring of the monitoring system, so that a failed alarm is itself detected, would help.

## Conclusion

Learning from failures is the practice of studying incidents and accidents systematically, reconstructing what happened and why, identifying the technical and organisational factors involved, and turning the findings into changes in practice, so that others do not repeat the same mistakes. Failures are rarely the work of one careless person: they are chains in which several defences failed, and the lessons lie in strengthening the chain.

This completes Unit 11. You can now explain what quality means and how quality models describe it, distinguish quality assurance from quality control, conduct reviews and inspections, use static analysis, apply metrics sensibly, manage defects and find root causes, reason about reliability and availability, recognise the role of formal methods, understand the demands of safety-critical software, and learn from real failures. Unit 12 moves from assuring the software to designing the interfaces and data on which modern systems rely: APIs, data, and persistence.
