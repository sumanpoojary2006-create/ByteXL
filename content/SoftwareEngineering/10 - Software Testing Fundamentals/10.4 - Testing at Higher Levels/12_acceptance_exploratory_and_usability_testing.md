## Introduction

Automated tests confirm that software does what its authors expected. They cannot tell whether those expectations were right, whether the software suits the people who must use it, or what unexpected problems lurk in situations nobody thought of. Those questions need human beings. Three kinds of testing address them: acceptance testing, which decides whether the software meets the needs of its customers; exploratory testing, in which skilled testers investigate the software freely; and usability testing, which watches real users attempt real tasks.

**Definition:** Acceptance testing determines whether a system satisfies the needs and criteria of its users and customers so that it can be accepted, exploratory testing is the simultaneous learning, test design, and execution by a skilled tester investigating the software, and usability testing observes representative users attempting realistic tasks to find where the design hinders them.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_acceptance_exploratory_and_usability_testing.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three panels: a customer signing off a checklist, a tester with a map and magnifying glass exploring a software landscape, and a user at a laptop being observed by a researcher with notes.

ON-IMAGE TEXT: show a short bold title "Acceptance, Exploratory and Usability Testing" plus only these few labels, large and legible: Accept, Explore, Observe. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Acceptance Testing

Acceptance testing is the final check by or for the customer that the product is fit for purpose. It answers: **have we built the right thing?** It is validation, in the sense of Unit 2.

### Forms of Acceptance Testing

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Form</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Who and what</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User acceptance testing (UAT)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Representative users perform realistic tasks in a test environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confirm the software supports real work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business acceptance testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business owners check that business processes and rules are met</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confirm the business case</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operational acceptance testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations staff check backup, recovery, monitoring, installation, security procedures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confirm the system can be run and supported</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contract and regulatory acceptance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Checks against terms in a contract or against legal and industry standards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confirm obligations are met</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Alpha testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Internal users test the near-final product within the developing organisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early real-use feedback</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Beta testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Selected external users try the product in real conditions before general release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wider feedback, real environments</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dogfooding</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The organisation uses its own product for its real work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Frequent, honest feedback</td>
    </tr>
  </tbody>
</table>

### Acceptance Criteria and Automation

In agile projects, acceptance starts with the **acceptance criteria** written for each story, as Unit 3 described, and with the Given-When-Then examples of behaviour-driven development. Many of these are automated, so that acceptance of each story is checked continuously. Human acceptance remains important for judging whether the whole works for real tasks. The Product Owner usually decides acceptance of each story at the sprint review, as Unit 2 described.

### Planning UAT

- **Define entry and exit criteria:** what must be true to begin, and what counts as success.
- **Involve real users,** with real tasks and realistic data.
- **Prepare scenarios** from business processes, not from the technical design.
- **Provide a safe environment** and support.
- **Collect and prioritise findings,** and decide which are blockers.
- **Record the decision** to accept, accept with conditions, or reject.

## Exploratory Testing

### The Idea

Exploratory testing, a term used by Cem Kaner from the 1980s and developed by James Bach and others, is defined as **simultaneous learning, test design, and test execution.** The tester is not following a prewritten script. They use what they learn from the software, and from its behaviour so far, to decide what to try next. It is structured investigation, not random clicking.

### Why It Matters

- Scripts only check what someone thought of in advance. Exploration finds **unexpected** problems.
- It adapts at once to what is discovered.
- It makes use of the tester's **skill, experience, and curiosity.**
- It is quick to start, needing no preparation, and suits new or changing features.
- It finds **usability problems and oddities** that scripts miss.

### Session-Based Testing

To make exploration accountable, Jonathan and James Bach developed **session-based test management.**

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Charter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A short mission for the session: "Explore order cancellation with different payment methods to discover problems with refunds"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time box</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An uninterrupted session, typically 60 to 120 minutes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Notes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The tester records what was tested, the questions raised, and the defects found, as they go</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Debrief</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A short conversation afterwards with a lead or colleague, reviewing findings and deciding what to explore next</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Metrics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of time on testing, investigation, and setup, and the numbers of defects and open questions</td>
    </tr>
  </tbody>
</table>

### Heuristics and Tours

Testers use prompts to guide exploration.

- **Tours:** a guided pass through the software with a theme, such as a feature tour, a data tour that exercises different data, or a back-alley tour that visits rarely used features.
- **Variation heuristics:** try different data, orders of steps, speeds, and interruptions; change the environment; go back and repeat steps.
- **Boundary and invalid input:** push limits, enter strange values.
- **Goldilocks:** too big, too small, just right.
- **Consistency heuristics:** compare with the specification, with similar products, with the documentation, and with the tester's own expectations.
- **Interruptions:** lose the network, switch applications, rotate the device.

### Strengths and Limits

Exploratory testing finds high-value defects quickly, but it is less repeatable, depends on the tester's skill, and does not provide an automatic regression suite. It **complements** automated checks and scripted tests; it does not replace them.

## Usability Testing

Usability testing asks whether people can use the software **effectively, efficiently, and with satisfaction.** Jakob Nielsen's heuristics from Unit 5 are used to inspect a design, and usability testing observes real users.

### How a Test Is Run

1. **Define goals** and the tasks to test, such as "find and order a vegetarian lunch and pay."
2. **Recruit participants** who represent real users. A handful, around five per round, typically reveals a large share of the main problems, and repeated small rounds work better than one large one.
3. **Observe them attempting the tasks** with little help, in person or remotely.
4. **Ask them to think aloud,** saying what they are looking for and what they expect.
5. **Record** where they hesitate, make errors, or fail, and what they say.
6. **Analyse and prioritise** the problems by severity and frequency.
7. **Fix and retest.**

### Measures

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Task success rate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of participants who complete each task</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time on task</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How long the task takes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wrong turns and mistakes made</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Satisfaction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Opinion, often with a standard questionnaire such as the System Usability Scale</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Qualitative observations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quotes, confusion, and unexpected behaviour</td>
    </tr>
  </tbody>
</table>

### Related Methods

- **A/B testing** compares two versions on live traffic to see which produces better behaviour, such as more completed orders.
- **Accessibility testing** checks use with assistive technology and against standards such as WCAG, as Unit 5 described.
- **Beta programmes and analytics** reveal how people really use the product.
- **Surveys and feedback tools** collect opinions at scale.

## Putting the Three Together

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Method</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it meet the agreed criteria for each story?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated acceptance tests and Product Owner acceptance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is the whole product fit for the customer needs?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User and business acceptance testing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What unexpected problems exist?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exploratory testing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can ordinary people use it easily?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability testing</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_session_charter_and_usability_session.png   (16:9 explanatory diagram, place here)

Left: an exploratory session card with Charter, Time box 90 minutes, Notes, Debrief arrows. Right: a usability test setup with a participant at a laptop thinking aloud, an observer taking notes, and a small results panel showing task success and time on task.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Method?

1. A team wants real customers to try the nearly finished product in their own conditions before general release.
2. A tester wants to investigate how the refund feature behaves in unusual circumstances, without a script.
3. A team wants to know where first-time users get confused in the ordering flow.

Case 1 is beta testing, a form of acceptance testing. Case 2 is exploratory testing, ideally structured in a chartered session. Case 3 is usability testing, with observation of representative users attempting tasks.

## Conclusion

Acceptance testing determines whether a system satisfies the needs and criteria of its users and customers so that it can be accepted, exploratory testing is the simultaneous learning, test design, and execution by a skilled tester investigating the software, and usability testing observes representative users attempting realistic tasks to find where the design hinders them. These human-centred methods find what automation cannot.

So far the focus has been on whether the software does the right things. The next topic turns to how well it does them: non-functional testing.
