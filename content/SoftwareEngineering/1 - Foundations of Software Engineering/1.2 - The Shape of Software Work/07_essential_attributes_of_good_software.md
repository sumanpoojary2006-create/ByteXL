## Introduction

Software can do exactly what was asked and still be bad. A feature may be present and correct, yet too slow to use at busy times, too fragile to trust, too tangled to change, or too confusing to enjoy. Correctness is the entry ticket, not the whole game.

This topic names the qualities, beyond basic correctness, that determine whether software is good, and explains why they compete with each other so that choosing between them is a core engineering decision.

**Definition:** The essential attributes of good software are the qualities beyond basic correctness, chiefly maintainability, dependability and security, efficiency, and acceptability, that determine whether people can actually rely on it, afford to change it, and enjoy using it.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_essential_attributes_of_good_software.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A central rounded box labelled Good Software with four branches: Maintainability, Dependability and Security, Efficiency, Acceptability.

ON-IMAGE TEXT: show a short bold title "Essential Attributes of Good Software" plus only these few labels, large and legible: Fast, Reliable, Usable. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Four Essential Attributes

Ian Sommerville, whose textbook is used in many university courses, groups the qualities of good software into four essentials.

1. **Maintainability.** The software can be changed to meet evolving needs. Since business needs will change, the software must be built so that change is safe and affordable.
2. **Dependability and security.** The software can be trusted. It does not cause harm when it fails, and it resists misuse and attack.
3. **Efficiency.** The software does not waste resources such as processor time, memory, network capacity, and money.
4. **Acceptability.** The software is understandable, usable, and compatible with the systems its users already rely on, so that the intended people will accept it.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Attribute</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Plain-language meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example in a meal-ordering app</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy to understand and change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new developer can add a new kind of feedback without rewriting existing parts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Works when needed, fails safely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confirmed orders are never lost if a server restarts</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protects data and resists abuse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One user cannot act as another</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Efficiency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uses resources sensibly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Screens load quickly even at the lunch rush</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Acceptability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People find it usable and fitting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Controls are easy to tap on a small phone screen</td>
    </tr>
  </tbody>
</table>

## Dependability in More Detail

Dependability is a family of related ideas.

- **Reliability:** the probability that the system performs correctly over a given period.
- **Availability:** the proportion of time the system is up and responding. A system with 99.9% availability can still be down for nearly nine hours in a year.
- **Safety:** the system does not cause injury, loss of life, or environmental damage.
- **Security:** the system protects confidentiality, integrity, and availability against deliberate attack.

## International Quality Models

Standards bodies have formalised similar lists. The ISO/IEC 25010 quality model (2011 edition) names eight characteristics of product quality: functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, and portability. The names matter less than the message: quality has many dimensions, and each project must decide which matter most.

## Attributes Pull Against Each Other

Qualities compete. Stronger security often reduces convenience, because checks add steps. Squeezing out speed can make code harder to read and therefore harder to maintain. Very high reliability costs money for redundancy and testing.

A medical device places dependability far above efficiency. A game places efficiency and acceptability above exhaustive verification. Engineers do not maximise every attribute. They **choose the right balance for the system and justify it**.

## Unwritten Expectations Become Failures

A common pattern: a feature passes every functional check, then fails in real use because nobody wrote down how fast, how available, or how secure it had to be. What is not stated is not designed for and not tested. The next topic shows how to state these qualities precisely.

## Your Turn: Which Attribute Is at Risk?

Name the attribute in danger in each situation.

1. A developer copies the same block of logic into six places, so a fix must be repeated six times.
2. A payment service becomes unreachable and the application shows an unexplained blank page.
3. A login screen relies on a control so small that it cannot be used without zooming.
4. An attacker gains access because the system accepts very weak passwords.

Situation 1 threatens maintainability. Situation 2 threatens dependability, specifically availability and graceful failure. Situation 3 threatens acceptability, because the interface is hard to use. Situation 4 threatens security.

## Conclusion

The essential attributes of good software are the qualities beyond basic correctness, chiefly maintainability, dependability and security, efficiency, and acceptability, that determine whether people can actually rely on it, afford to change it, and enjoy using it. They compete with each other, so engineers choose the balance on purpose.

Qualities only guide a project if they are written down in a testable way. The next topic separates what a system does from how well it does it, and shows how to state both precisely.
