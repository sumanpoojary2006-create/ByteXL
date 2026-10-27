## Introduction

Ethical principles become concrete when applied to what actually happened. Cases in which software contributed to harm show how ordinary decisions, such as a design shortcut, a data set that was not examined, a target that rewarded the wrong behaviour, or a concern that was not escalated, led to serious consequences. Studying them is not an exercise in blame. It trains the habit of recognising early the conditions that precede harm, and of asking what could have been done differently at each point.

This topic presents four categories of case: algorithmic bias, deliberate deception in software (the Volkswagen emissions scandal), the safety failure of the Boeing 737 MAX flight-control system, and manipulative design known as dark patterns, followed by shorter cases and a method of analysis. The accounts summarise widely reported public information and findings of investigations; details should be checked against the original reports.

**Definition:** A case study in ethics is a structured examination of a real event in which technical, organisational, and human factors led to harm or to a significant ethical failure, undertaken to identify causes, responsibilities, and lessons that can improve future professional practice.

<!--
IMAGE PROMPT  ->  generate as images/11_intro_case_studies_in_ethics_and_harm.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Four panels in a two-by-two grid with icons: a scale with unbalanced figures (bias), an exhaust pipe with a hidden switch (deception), an aircraft with a sensor warning (safety), and a button with a hidden decline option (dark pattern).

ON-IMAGE TEXT: show a short bold title "Case Studies in Ethics and Harm" plus only these few labels, large and legible: Four Ways Things Go Wrong. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## How to Analyse a Case

For each case, ask:

1. **What happened?** Establish the facts and timeline.
2. **Who was affected,** and how seriously, including indirectly?
3. **What decisions** led to it, at which levels: engineer, team, management, company, regulator?
4. **What were the technical causes,** and what were the organisational and cultural causes?
5. **What warnings** existed, and what became of them?
6. **Which ethical principles** (public interest, honesty, competence, fairness, privacy) were involved?
7. **What could have been done differently,** and by whom, at what point?
8. **What lessons** apply to your own work?

## Case 1: Algorithmic Bias

Algorithms that learn from historical data, or that are built on assumptions about who the users are, can reproduce and amplify unfairness at scale while appearing objective.

### Examples

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What was reported</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Lesson</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recruiting tool</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A company built an experimental system to rank job applicants from patterns in past hiring decisions. It was reported in 2018 to have learned to penalise applications associated with women, because the historical data reflected a male-dominated industry. The company abandoned it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Historical data encodes past bias. Removing an explicit attribute does not remove it, because other signals act as proxies</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Facial analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A 2018 study by Joy Buolamwini and Timnit Gebru (Gender Shades) found commercial systems had far higher error rates for darker-skinned women than for lighter-skinned men. Vendors subsequently improved their products, and several limited police use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test data sets must represent everyone affected; report performance by group, not only averages</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Criminal risk scores</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A 2016 investigation by ProPublica of the COMPAS tool used in some US courts alleged that Black defendants were more often wrongly labelled high risk than white defendants. The developer and other researchers disputed the analysis. The debate showed that several reasonable definitions of fairness cannot all be satisfied at once when groups differ in base rates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Fair" has multiple, sometimes incompatible, definitions. Decisions about liberty need transparency and human accountability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Credit and welfare decisions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated systems used to score applicants or detect fraud have in several countries wrongly denied benefits or credit, with affected people unable to understand or challenge the decision</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High-stakes automation needs explanation, appeal, and monitoring</td>
    </tr>
  </tbody>
</table>

### Sources of Bias

- **Data:** unrepresentative samples, historical discrimination, labels made by biased humans, missing groups.
- **Problem framing:** the choice of what to predict (for instance, arrests as a stand-in for crime).
- **Features and proxies:** postcode, language, or purchase patterns that correlate with protected traits.
- **Model and metric choices:** optimising average accuracy hides poor performance for minorities.
- **Deployment context:** using a system on populations or for purposes it was not designed for.
- **Feedback loops:** predictions shape what data is later collected, reinforcing patterns (for example, more policing in areas flagged, producing more recorded incidents there).
- **Automation bias:** human reviewers defer to the machine.

### Responses

- Examine data for coverage and bias; document data sets and models (datasheets and model cards).
- Define fairness metrics suited to the context and measure them by group.
- Include affected people and domain experts in design and testing.
- Provide transparency, explanation, human review, and a way to contest decisions.
- Monitor after release for drift and disparate impact.
- Decide, sometimes, not to automate a decision at all.
- Observe the law: anti-discrimination rules and data-protection rules on automated decisions apply (previous topic). Later topics treat machine learning engineering further.

## Case 2: Volkswagen Emissions (2015)

In September 2015, the US Environmental Protection Agency announced that Volkswagen had installed software in about half a million diesel cars in the United States (and later millions worldwide) that detected when a vehicle was undergoing an official emissions test and changed the engine's behaviour to meet the limits on nitrogen oxides. On the road, the cars emitted many times the permitted levels. The software was a "defeat device".

### What Happened

- Engine software recognised test conditions from signals such as steering input, speed pattern, and duration, and switched to a low-emission mode only in those conditions.
- The practice continued for years. The discovery followed independent testing of vehicles on real roads by a university team in the United States.
- The company admitted wrongdoing, paid settlements and fines amounting to tens of billions of dollars, recalled vehicles, and saw senior executives and engineers face criminal and civil proceedings. Individuals were convicted and sentenced in the United States and Germany.

### Ethical Analysis

- **Deliberate deception:** this was not an accident. Software engineers wrote and maintained code whose purpose was to mislead regulators.
- **Organisational pressure:** reports of the investigations described pressure to meet demanding technical targets that the available technology could not meet within cost limits, and a culture in which problems were hidden.
- **Individual responsibility:** engineers carried out instructions to implement deception; "I was told to" is not a defence in the ethical codes (the honesty and public-interest principles), and several faced personal consequences.
- **Harm:** pollution contributing to health damage, along with loss of public trust in the industry.
- **Lessons:** refuse to write code designed to deceive; the duty of honesty applies to software behaviour, not only to statements; escalate pressure that makes compliance impossible; regulators and auditors should test in real conditions; and organisations must make it safe to say that a target cannot be met honestly.

## Case 3: Boeing 737 MAX (2018 and 2019)

Two accidents involving the Boeing 737 MAX, Lion Air Flight 610 in October 2018 and Ethiopian Airlines Flight 302 in March 2019, killed all 346 people on board the two aircraft. The type was grounded worldwide for about twenty months.

### Technical Background

To fit larger, more efficient engines, the MAX's engines were mounted further forward and higher, changing the aircraft's handling at high angles of attack. A flight-control function called MCAS (Manoeuvring Characteristics Augmentation System) was added to push the nose down automatically in certain conditions, so that the aircraft would feel like earlier 737 models to pilots.

Investigations by the accident authorities and by US government and congressional bodies identified, among other things:

- MCAS originally relied on data from a **single** angle-of-attack sensor, so a faulty sensor could trigger it wrongly.
- The system could act repeatedly and with more authority than was assumed in the original safety assessment.
- Pilots were not told of MCAS in manuals or training, and the alerts and procedures for dealing with its misbehaviour were not adequate; a warning light that some customers believed was standard was an optional extra.
- Safety assessments and certification had relied heavily on the manufacturer's own delegated work, with limited independent scrutiny of the changes, and commercial and schedule pressure to avoid costly new pilot training influenced decisions.

### Ethical Analysis

- **Single point of failure in a safety-critical function** contradicts basic safety engineering (Unit 11): redundancy, fail-safe design, and hazard analysis.
- **Changed assumptions not re-examined:** the behaviour of the system was modified during development, but the safety analysis was not fully updated to reflect it.
- **Transparency:** those who operated the aircraft were not given complete information.
- **Pressure and incentives:** business goals, competition, and schedule shaped technical decisions; reports described internal messages in which employees expressed concerns.
- **Regulatory capture and oversight:** over-reliance on the regulated party to certify its own work.
- **Lessons:** safety cases must be kept current with design changes; safety concerns must reach decision-makers; disclose system behaviour to the people who depend on it; resist treating schedule and cost as reasons to reduce safety margins; and understand that software that alters the behaviour of physical machines carries obligations of the highest order.

## Case 4: Dark Patterns

A **dark pattern,** a term coined by designer Harry Brignull in 2010, is an interface design that tricks or pressures users into actions they did not intend and that benefit the operator.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pattern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confirmshaming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Declining is phrased to make the user feel foolish or guilty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"No thanks, I prefer to pay more"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden costs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fees appear only at the last step</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A low price that grows at checkout</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forced continuity and roach motel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy to subscribe, hard to cancel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sign up in one click, cancel only by phone</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Disguised ads</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Advertisements look like content or navigation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A download button that is an ad</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pre-selected options and sneaking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extra items or consents are added by default</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pre-ticked marketing consent</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">False urgency and scarcity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invented countdowns or "only one left" messages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A timer that resets</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nagging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeated interruptions until the user gives in</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Constant prompts to enable tracking</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Misdirection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Visual emphasis steers away from the privacy-friendly choice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bright "Accept all" and a faint, hidden "Reject"</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Privacy zuckering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tricking users into sharing more than intended</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confusing settings</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Obstruction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Making an action deliberately difficult</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Burying account deletion</td>
    </tr>
  </tbody>
</table>

### Ethical and Legal View

Dark patterns undermine autonomy and informed consent, exploit psychological biases, and disproportionately harm the less technical, the young, and the vulnerable. They conflict with honesty, respect for users, and the public interest in the codes. Regulators have acted: European data-protection and consumer authorities have found that deceptive consent designs invalidate consent, consumer-protection agencies in several jurisdictions have taken action over subscription traps and fake urgency, and new laws and guidance address manipulative design. They also damage long-term trust and attract complaints and churn.

### Alternatives

Design for clarity: equal prominence for choices; plain language; cancellation as easy as sign-up; honest pricing; defaults that favour the user; consent that is genuine. A practical test: could you explain the design, openly, to the user it affects, without embarrassment?

## Other Cases Worth Studying

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Case</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Summary</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Main lessons</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Therac-25 (1985 to 1987)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A radiation therapy machine whose software contained concurrency faults and which removed hardware safety interlocks overdosed several patients, some fatally</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safety-critical software needs independent hardware safeguards, thorough testing, and a culture that takes incident reports seriously (Unit 11)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">UK Post Office Horizon scandal (1999 onward)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An accounting system with bugs showed false shortfalls at post office branches. Hundreds of sub-postmasters were prosecuted or held liable; many convictions were later quashed, and a public inquiry followed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software defects have human victims; organisations must not assume the system is right; evidence from software needs scrutiny; those with knowledge of faults must speak up</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cambridge Analytica and Facebook (2018)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Personal data of tens of millions of users was harvested through a quiz application and used for political profiling beyond what users understood</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data sharing through platforms, consent, purpose limitation, and the responsibility of platform owners</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Equifax breach (2017)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Personal data of about 147 million people exposed after a known, unpatched flaw in a web framework</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patch management, asset inventory, and the duty to protect data entrusted to you (previous topics)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knight Capital (2012)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A faulty deployment left old code active on one of eight servers and lost around 440 million dollars in about 45 minutes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release discipline, deployment automation, and kill switches (Unit 9)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ariane 5 flight 501 (1996)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reused software failed on a faster rocket because of an unhandled numeric conversion error; the rocket was destroyed 37 seconds after launch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reuse requires revalidation; handle exceptional conditions (Unit 11)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uber self-driving fatality (2018)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A pedestrian was killed by an autonomous test vehicle; investigators cited the failure of the system to classify her correctly, disabled emergency braking, and inadequate safety culture and operator monitoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing on public roads is an ethical decision; safety culture; human supervisors cannot be expected to remain vigilant</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Therac and Horizon-style over-trust</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operators and organisations trusted software over reports from people</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evidence from people who report problems deserves a serious hearing</td>
    </tr>
  </tbody>
</table>

## Patterns Across the Cases

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pattern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Appears in</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pressure from schedule, cost, or targets overriding caution</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Volkswagen, 737 MAX, Knight Capital</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concerns raised but not acted upon</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">737 MAX, Horizon, Therac-25</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assumptions not revisited after change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">737 MAX, Ariane 5</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lack of transparency to those affected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">737 MAX, dark patterns, Cambridge Analytica, bias cases</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unrepresentative testing or data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Facial analysis, recruiting tool, Uber</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-trust in automation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Credit/welfare systems, Horizon, Uber</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak oversight</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">737 MAX, risk scores, Volkswagen</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Individual engineers following instructions without questioning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Volkswagen</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failure to maintain and patch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Equifax</td>
    </tr>
  </tbody>
</table>

## Lessons for Practice

1. **Make harm part of the design review.** Ask "who could be hurt, and how?" for every significant feature.
2. **Treat warnings as data.** Make it safe and easy to report concerns, and ensure someone is responsible for answering them.
3. **Keep safety and fairness analyses current** when designs change.
4. **Prefer transparency** to those who depend on the system.
5. **Test with the real population** and in the real environment.
6. **Include humans meaningfully,** with authority, information, and time to override automation.
7. **Know your own limits** and the point at which you will refuse.
8. **Remember that you are accountable** as an individual professional, whatever the instruction.

<!--
IMAGE PROMPT  ->  generate as images/11_common_patterns_in_ethical_failures.png   (16:9 explanatory diagram, place here)

A central swiss-cheese style stack of five slices labelled Pressure, Unheard warnings, Stale assumptions, Weak oversight, Opaque design with a red arrow passing through aligned holes to a box labelled Harm, and green hands inserting a slice labelled Speak up to block it.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Analyse a Case

1. In a design review for a loan-approval model, you notice that approval rates are much lower for one neighbourhood. What do you do?
2. A product manager suggests a countdown timer on the checkout page that restarts when it expires, to "encourage decisions". Which ethical principle is at stake, and what would you propose?
3. Identify two common patterns in the 737 MAX and Knight Capital cases.

For case 1, treat it as a signal: investigate whether proxies for protected traits are involved, measure outcomes by group, raise it to the team and responsible owners, and do not release until understood. For case 2, honesty and respect for user autonomy; the timer is deceptive false urgency, so propose honest messaging, such as real stock levels or real deadlines. For case 3, pressure on cost and schedule, and weaknesses in change control (a design changed without full re-assessment; a deployment process not verified).

## Conclusion

A case study in ethics is a structured examination of a real event in which technical, organisational, and human factors led to harm or to a significant ethical failure, undertaken to identify causes, responsibilities, and lessons that can improve future professional practice. The same patterns of pressure, unheeded warnings, stale assumptions, and opacity recur, and recognising them early is the practical skill that these cases teach.

Ethics also governs the use of other people's work. The next topic covers intellectual property and software licensing.
