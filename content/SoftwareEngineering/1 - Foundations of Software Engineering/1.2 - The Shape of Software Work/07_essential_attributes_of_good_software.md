## Introduction

The ratings feature went live on a Tuesday. By lunchtime on Wednesday it was failing. At exactly 1:00 p.m., when four thousand students opened the app within minutes of each other, the rating screen took forty seconds to load and sometimes showed nothing at all.

Ananya was baffled. "But it passed all my tests," she told Vikram. It had. Every rule in her acceptance list was satisfied: ratings were saved, duplicates were rejected, and averages were correct.

Vikram answered with a sentence she wrote on a sticky note: "Correct is the entry ticket, not the whole game." Software can do exactly what was asked and still be bad, because users and organisations care about far more than whether a feature technically exists.

**Definition:** The essential attributes of good software are the qualities beyond basic correctness, chiefly maintainability, dependability and security, efficiency, and acceptability, that determine whether people can actually rely on it, afford to change it, and enjoy using it.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_essential_attributes_of_good_software.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and engineering problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Ananya stares at a loading spinner on a student phone while a crowd of four thousand students waits outside the mess hall at lunchtime, and Vikram holds up a sticky note reading Correct is not enough.

ON-IMAGE TEXT: show a short bold title "Essential Attributes of Good Software" plus only these few labels, large and legible: Fast, Reliable, Usable. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Four Essential Attributes

Ian Sommerville, whose textbook is used in many university courses, groups the qualities of good software into four essentials.

1. **Maintainability.** The software can be changed to meet evolving needs. Since the business will change, the code must be written so that change is safe and affordable.
2. **Dependability and security.** The software can be trusted. It does not cause harm when it fails, and it resists misuse and attack.
3. **Efficiency.** The software does not waste resources such as processor time, memory, network, and money.
4. **Acceptability.** The software is understandable, usable, and compatible with the systems its users already rely on, so that the intended people will actually accept it.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Attribute</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Plain-language meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Ratings feature example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy to understand and change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new developer can add "rate the staff" without rewriting the feature</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Works when needed, fails safely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ratings are never lost if the server restarts</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protects data and resists abuse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A student cannot rate as someone else</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Efficiency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uses resources sensibly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The rating screen loads quickly even at the lunch rush</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Acceptability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People find it usable and fitting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stars are tappable on a small phone screen</td>
    </tr>
  </tbody>
</table>

## Dependability in More Detail

Dependability is not one thing but a family of related ideas.

- **Reliability:** the probability that the system performs correctly over a given period.
- **Availability:** the proportion of time the system is up and responding. A system with 99.9% availability can still be down for nearly nine hours in a year.
- **Safety:** the system does not cause injury, loss of life, or environmental damage.
- **Security:** the system protects confidentiality, integrity, and availability against deliberate attack.

<!--
IMAGE PROMPT  ->  generate as images/02_four_attributes_and_dependability_family.png   (16:9 explanatory diagram, place here)

A central rounded box labelled Good Software with four branches: Maintainability, Dependability and Security, Efficiency, Acceptability. The Dependability branch splits into four small boxes: Reliability, Availability, Safety, Security.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## International Quality Models

Standards bodies have formalised similar lists. The ISO/IEC 25010 quality model (2011 edition) names eight characteristics of product quality: functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, and portability. You do not need to memorise them. What matters is the message that quality has many dimensions, and each project must decide which matter most.

## Attributes Pull Against Each Other

Qualities compete. Making software more secure often makes it less convenient, because strong checks add steps. Making it faster may make the code harder to read and therefore harder to maintain. Making it extremely reliable costs money for redundancy and testing.

A heart monitor places dependability far above efficiency. A game places efficiency and acceptability above exhaustive formal verification. Engineers do not maximise every attribute. They **choose the right balance for the system and justify it**.

## Why the Lunch Rush Failed

Back to Wednesday. Ananya's ratings feature had functional correctness but no *efficiency* planning. It loaded every rating ever stored for a meal and averaged them in the app instead of asking the database for a total. With a few test ratings, this was instant. With thousands, it was not. Nobody had written down how fast the screen needed to be, so nobody had tested it.

## Your Turn: Which Attribute Is at Risk?

Name the attribute in danger in each situation.

1. A developer copies the same 40 lines of code into six places, so a bug fix must be repeated six times.
2. The payment service becomes unreachable and the app shows an unexplained blank page.
3. A login page asks users to press a tiny button that cannot be seen without zooming.
4. An attacker guesses a student's password because the system accepts "1234".

Situation 1 threatens maintainability. Situation 2 threatens dependability, specifically availability and graceful failure. Situation 3 threatens acceptability, because the interface is hard to use. Situation 4 threatens security.

## Conclusion

The essential attributes of good software are the qualities beyond basic correctness, chiefly maintainability, dependability and security, efficiency, and acceptability, that determine whether people can actually rely on it, afford to change it, and enjoy using it. They compete with each other, so engineers choose the balance on purpose.

Ananya's lunch-rush problem happened because nobody wrote the quality expectation down. The next lesson shows how to separate what a system does from how well it does it, and how to state both so precisely that they can be tested.
