## Introduction

Users rarely ask how many defects a system contains. They ask whether it works when they need it, and how often it lets them down. Reliability and availability answer those questions. They are properties of the running system over time, not of the code at one moment, and they can be defined, measured, predicted, and designed for. Units 5 and 6 introduced them as quality attributes and architecture drivers. This topic gives the basic concepts and arithmetic that engineers use to reason about them.

**Definition:** Reliability is the probability that a system performs its required function without failure for a specified period under stated conditions, and availability is the proportion of time that the system is ready to perform that function, which depends on both how often it fails and how quickly it is restored.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_reliability_and_availability_basics.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A timeline showing alternating Up (green) and Down (red) periods, with labelled spans for time between failures and time to repair, and an availability percentage gauge. Beside it, two boxes in series and two in parallel with redundancy.

ON-IMAGE TEXT: show a short bold title "Reliability and Availability Basics" plus only these few labels, large and legible: Up, Down, Repair. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## From Fault to Failure

Three terms describe how things go wrong, refining the error-defect-failure chain of Unit 10.

- A **fault** is the cause, such as a defect in code or a failing component.
- An **error** is the incorrect internal state that results when the fault is activated.
- A **failure** is the visible deviation from correct service, when the error reaches the system's interface.

A fault may remain **dormant** for years until a particular input or condition activates it. Reliability engineering aims to prevent faults, to remove them, to tolerate them so that they do not become failures, and to forecast how many remain. These four approaches, **fault prevention, fault removal, fault tolerance, and fault forecasting,** were set out in the dependability research of Algirdas Avizienis, Jean-Claude Laprie, and colleagues.

## Dependability

Dependability is the umbrella property: the ability of a system to deliver service that can justifiably be trusted. It combines:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Attribute</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuity of correct service</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Availability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Readiness for correct service</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safety</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Absence of catastrophic consequences for users and environment</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Absence of improper alteration</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ability to undergo repairs and modifications</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confidentiality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Absence of unauthorised disclosure (sometimes grouped under security)</td>
    </tr>
  </tbody>
</table>

## Basic Measures

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failure rate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How often failures occur per unit of operating time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Often written as a rate per hour</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MTTF (mean time to failure)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Average operating time until the first failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">For items that are replaced, not repaired</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MTBF (mean time between failures)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Average time from one failure to the next, for repairable systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sum of the average operating time and the average repair time</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MTTR (mean time to repair or restore)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Average time to get the system working again</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Includes detection, diagnosis, and fix or workaround</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliability R(t)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The probability of operating without failure for time t</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Falls as t grows</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Availability A</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The fraction of time the system is up</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Steady-state: MTBF divided by MTBF plus MTTR</td>
    </tr>
  </tbody>
</table>

A simple, important formula (using uptime between failures as MTBF) is:

**Availability = MTBF / (MTBF + MTTR)**

### Worked Example

A service fails on average once every 1,000 hours of operation (MTBF = 1,000) and takes one hour to restore (MTTR = 1). Availability is 1,000 divided by 1,001, about 0.999, or **99.9 percent**.

The formula carries a vital lesson: availability depends on **both** how seldom the system fails **and** how quickly it recovers. If the same service could be restored in six minutes instead of an hour, availability would rise to about 99.99 percent without any fewer failures. This is why modern practice invests so heavily in monitoring, automation, and quick rollback, the topics of Unit 9: **reducing repair time is often cheaper than preventing every failure.**

## Combining Components

Real systems are made of parts. The availability of the whole depends on how they are arranged.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Arrangement</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rule</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Series (all must work)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Multiply the availabilities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two services each at 99.9 percent, both needed for a request: 0.999 times 0.999 is about 99.8 percent</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parallel (redundant, any one suffices)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One minus the product of the unavailabilities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two independent servers each at 99 percent: 1 minus (0.01 times 0.01) is 99.99 percent</td>
    </tr>
  </tbody>
</table>

Two consequences follow.

1. **Chains of dependencies reduce availability.** Ten services in series, each at 99.9 percent, give about 99.0 percent overall. Every additional required component makes the system less available, which is a quiet argument against needless dependencies and long synchronous call chains.
2. **Redundancy raises availability dramatically,** but only if the parts fail **independently.** Two servers in the same room, on the same power supply, or running the same faulty software, may fail together. Sources of **common-cause failure** must be considered.

## Reliability of Software: What Is Different

Hardware wears out, and its failure rate over its life follows a **bathtub curve**: high early failures, a long stable period, and rising failures with age. Software does not wear out, but its reliability behaves differently.

- Failures come from **design and coding faults** present from the start, not from deterioration.
- Reliability **improves as faults are found and removed,** a pattern modelled by **software reliability growth models** such as those developed by Jelinski and Moranda and by John Musa, which use the failure history during testing to estimate remaining faults and predict the time to reach a target.
- Reliability **depends on how the software is used.** A fault in a rarely used function rarely causes failure. Musa's **operational profile** describes the real mix of uses, and testing in proportion to it gives the most reliability improvement for the effort.
- **Change disturbs it:** each release can introduce new faults, so reliability can fall again.
- **The environment changes:** load, data, and dependencies drift.

## Designing for Reliability and Availability

### Prevent and Remove Faults

Good requirements, design, coding practices, reviews, static analysis, and testing, as described in this unit and the last, reduce the number of faults at the outset.

### Tolerate Faults

Fault tolerance techniques keep service going despite faults.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redundancy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplicate components, so that others carry on when one fails</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failover</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automatically switch to a standby when the active one fails</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replication</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep copies of data and services in several places</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retries with limits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Try again after a transient failure</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Timeouts and circuit breakers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stop waiting for failing dependencies, as Unit 6 described</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Graceful degradation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduce function, not stop, when part fails</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Checkpointing and recovery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Save state so work resumes from a recent point</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design diversity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Independent implementations of the same function, as in N-version programming, to avoid common faults; effective only where the versions really are independent, which research has shown is hard to guarantee</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recovery blocks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run an alternative if the first fails an acceptance check</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Watchdogs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A monitor that restarts a stalled component</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Load shedding</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refuse some work to protect the rest</td>
    </tr>
  </tbody>
</table>

### Recover Quickly

Monitoring and alerting to detect failure fast, runbooks and automation to restore, feature flags and rollback, and rehearsed recovery (Unit 9) all reduce MTTR.

### Forecast

Track failures in test and in production, estimate remaining faults and expected failure rate, and compare with targets set by service level objectives.

## Specifying and Measuring

Reliability requirements must be stated measurably, as Unit 3 insisted: for example, "no more than one failure per 1,000 hours of operation," "99.95 percent availability measured monthly," or "restore service within 15 minutes of failure." Measured from monitoring in production, they feed service level objectives and error budgets, as Unit 9 described.

<!--
IMAGE PROMPT  ->  generate as images/02_availability_formula_series_parallel.png   (16:9 explanatory diagram, place here)

Top: an up-down timeline with MTBF and MTTR spans and the formula Availability equals MTBF over MTBF plus MTTR with the worked 99.9 percent example. Bottom: a series chain of three boxes (availability falls) and a parallel pair of boxes (availability rises), with a warning about common-cause failure.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Calculate and Reason

1. A system has an MTBF of 500 hours and an MTTR of 0.5 hours. What is its availability?
2. A request needs two services in series, one at 99.5 percent and one at 99.8 percent. What is the combined availability, approximately?
3. Two servers at 99 percent each are placed in parallel but share a power supply. What is the weakness?

For case 1, availability is 500 divided by 500.5, about 99.9 percent. For case 2, multiply: 0.995 times 0.998 is about 0.993, or 99.3 percent. In case 3, the shared power supply is a common-cause failure: if it fails, both servers fail together, so the claimed redundancy is not real.

## Conclusion

Reliability is the probability that a system performs its required function without failure for a specified period under stated conditions, and availability is the proportion of time that the system is ready to perform that function, which depends on both how often it fails and how quickly it is restored. Engineers raise both by preventing faults, tolerating them, and recovering fast, and they reason about the whole system by combining the parts.

Testing can reduce the number of faults but cannot prove their absence. For the most critical software, a stronger kind of assurance is sometimes sought: mathematical proof. The next topic introduces formal specification and verification.
