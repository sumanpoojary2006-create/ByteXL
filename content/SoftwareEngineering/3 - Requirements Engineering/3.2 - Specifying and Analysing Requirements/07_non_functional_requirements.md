## Introduction

A system can do everything specified and still be unacceptable, because it is too slow, too insecure, too hard to use, or too fragile. Non-functional requirements capture these qualities. They are often neglected because they are harder to state and because stakeholders assume them, yet they frequently decide whether a system succeeds and they strongly influence its architecture and cost.

**Definition:** Non-functional requirements describe the qualities a system must have, such as performance, security, reliability, and usability, and the constraints within which it must operate, and to be useful they must be stated in measurable terms with a defined way of checking them.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_non_functional_requirements.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A set of gauges around a central system block labelled Performance, Security, Reliability, Usability, Scalability, Maintainability, each with a numeric target on its dial.

ON-IMAGE TEXT: show a short bold title "Non-Functional Requirements" plus only these few labels, large and legible: Quality, Measure, Target. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why They Matter

- They often have **more impact on architecture** than individual features. A system that must serve millions of users, or must never lose data, is built differently from one that does not.
- They are **costly to add later.** Retrofitting security or performance into a finished design is far harder than planning for it.
- They are **where users feel quality**: slow, unreliable, or confusing systems are rejected even when their functions are complete.

## Main Categories

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Category</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concerns</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example of a measurable requirement</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Response time, throughput, resource use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">95 percent of searches return within 1 second with 1,000 concurrent users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scalability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handling growth in users or data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system shall support 10 times the current number of users by adding servers, with no redesign</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliability and availability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failure rate, uptime, recovery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Available 99.9 percent of the time per month; service restored within 30 minutes of failure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confidentiality, integrity, access control, auditing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All personal data encrypted in storage; an account locks after 5 failed logins</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Privacy and compliance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Legal and regulatory obligations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Personal data is deleted within 30 days of an account closure request</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability and accessibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ease of learning and use, access for all</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new user completes the main task unaided within 3 minutes; the interface meets WCAG 2.1 level AA</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ease of change and diagnosis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A typical defect fix can be released within one working day</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Portability and compatibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Running on different platforms and with other systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Works on the latest two versions of major web browsers and on phones with 4-inch screens</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monitoring, deployment, support</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deployments require no downtime; every error is logged with a traceable identifier</td>
    </tr>
  </tbody>
</table>

## Making Them Measurable

A useful pattern for a quality requirement has four parts: the **scenario** (what is happening), the **stimulus** (what triggers it), the **response** (what the system must do), and the **measure** (how well). For example: during the lunch-hour peak (scenario), when 2,000 users request the menu at once (stimulus), the system returns each menu page (response) within 2 seconds for 95 percent of requests (measure).

Testing a non-functional requirement requires a method as well as a number: a load test, a security review, a usability session, or monitoring in production. If nobody can say how a requirement will be checked, it is not yet a requirement.

## Constraints

Some non-functional requirements are **constraints**: fixed conditions imposed on the solution, not qualities to be traded. Examples are mandatory technology, compliance with a law, a fixed budget or deadline, and compatibility with an existing system. Constraints are discovered early by asking what is non-negotiable, and they shape every later decision.

## Trade-offs Between Qualities

Qualities conflict. High security can reduce convenience. Fast response may cost more infrastructure. Portability may limit the use of platform-specific features. Because of this, requirements should be **prioritised** and the trade-offs agreed with stakeholders instead of leaving them to be decided by developers during design.

<!--
IMAGE PROMPT  ->  generate as images/02_quality_scenario_pattern.png   (16:9 explanatory diagram, place here)

A four-box flow: Scenario (lunch rush), Stimulus (2,000 users request menu), Response (menu page returned), Measure (within 2 seconds for 95 percent of requests), with a Test method label beneath: Load test.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Make It Measurable

1. "The system shall be secure."
2. "The system shall be available."
3. "The app shall be easy to learn."

Statement 1 can be refined into several requirements, for example: passwords are stored only as salted hashes, all network traffic is encrypted, and an independent security review finds no high-severity issues before release. Statement 2 could be: the system shall be available at least 99.9 percent of the time each month, excluding announced maintenance windows of up to 2 hours. Statement 3 could be: in a usability test with 10 first-time users, at least 9 shall complete a purchase within 3 minutes without help.

## Conclusion

Non-functional requirements describe the qualities a system must have, such as performance, security, reliability, and usability, and the constraints within which it must operate, and to be useful they must be stated in measurable terms with a defined way of checking them. They deserve the same care as features, because they shape both cost and architecture.

With requirements gathered and written, conflicts and doubts will remain. The next topic covers how analysts examine requirements and negotiate agreements among stakeholders.
