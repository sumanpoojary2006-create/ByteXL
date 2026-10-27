## Introduction

Software shapes who gets a loan, what news people see, whether an aircraft stays in the air, and how much of their private life is visible to others. Engineers make decisions that affect many people who will never meet them and who cannot inspect the system for themselves. Professions such as medicine and civil engineering have long recognised that such power carries responsibility, and have set out codes of conduct, standards of competence, and expectations about the public interest. Software engineering is a younger profession, but the same reasoning applies. Ethics is the part of professional practice that asks not only whether something can be built, or whether it is legal, but whether it should be built and how.

This topic explains why ethics matters in software, introduces the main codes of professional ethics, presents common ethical frameworks and a method for thinking through dilemmas, and discusses responsibilities such as honesty, competence, and the handling of concerns, including whistleblowing.

**Definition:** Professional ethics in software engineering is the set of moral principles and standards of conduct that guide engineers in their obligations to the public, clients and employers, colleagues, and the profession, especially where their work can affect the welfare, rights, and safety of others.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_professional_ethics_in_software_engineering.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Balance scales with a small software system icon on one pan and a group of people icons on the other, and a compass rose beneath labelled Public interest.

ON-IMAGE TEXT: show a short bold title "Professional Ethics in Software Engineering" plus only these few labels, large and legible: Public Good First. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Ethics Matters in Software

- **Scale:** one decision in code is applied to millions of people automatically, repeatedly, and invisibly.
- **Opacity:** users cannot inspect software; they rely on the engineers' integrity.
- **Power asymmetry:** organisations know far more about people than people know about the system.
- **Harm can be real:** loss of life (safety-critical systems, Unit 11), financial ruin, wrongful accusation, discrimination, loss of liberty, and erosion of trust in institutions.
- **Pressure:** deadlines, targets, and commercial interests can push towards cutting corners.
- **Diffused responsibility:** in large teams, everyone assumes someone else has considered the consequences.
- **Law lags technology:** much that is legal is still harmful, and engineers often face questions before regulation exists.

Ethical failures are rarely cartoon villainy. More often they result from small compromises, unexamined assumptions, narrow focus on one's own task, and silence.

## Codes of Ethics

### The ACM Code of Ethics and Professional Conduct

The Association for Computing Machinery first adopted a code in 1972 and revised it substantially in 2018. It begins with general ethical principles.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Summary</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1.1 Contribute to society and to human well-being</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Respect all people and acknowledge that computing should support the public good</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1.2 Avoid harm</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevent harm to users, the public, and the environment; report risks; weigh consequences</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1.3 Be honest and trustworthy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not make deceptive claims; be open about limitations</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1.4 Be fair and take action not to discriminate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Value diversity, inclusion, and equal treatment</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1.5 Respect the work required to produce new ideas, inventions, creative works, and computing artefacts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Give credit; respect licences and intellectual property</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1.6 Respect privacy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Collect and use personal data only as needed, with consent and transparency</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1.7 Honour confidentiality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Respect confidences, unless a greater obligation to the public intervenes</td>
    </tr>
  </tbody>
</table>

The code then lists professional responsibilities (strive for high quality, maintain competence, know and respect the law, accept and give professional review, give comprehensive evaluation of systems and their risks, and perform work only in areas of competence, among others), professional leadership principles, and obligations about compliance with the code itself.

### The Software Engineering Code of Ethics and Professional Practice

Jointly adopted by the ACM and the IEEE Computer Society in 1999, this code is specific to software engineers. Its eight principles describe obligations to eight parties.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concern</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1. Public</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Act consistently with the public interest</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2. Client and employer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Act in the best interests of client and employer, consistent with the public interest</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3. Product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ensure products and modifications meet the highest professional standards possible</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4. Judgment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintain integrity and independence in professional judgment</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5. Management</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Managers and leaders promote an ethical approach to development and maintenance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6. Profession</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Advance the integrity and reputation of the profession, consistent with the public interest</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">7. Colleagues</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Be fair to and supportive of colleagues</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8. Self</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Participate in lifelong learning and promote an ethical approach to the practice</td>
    </tr>
  </tbody>
</table>

The first principle is placed first deliberately: **when obligations conflict, the public interest takes precedence** over loyalty to an employer or client. Other bodies publish comparable codes, such as the British Computer Society's code of conduct, the Engineers Canada and national engineering councils' codes, and codes within employers and open-source communities.

### What Codes Do and Do Not Do

Codes state shared expectations, support individuals who refuse to do something wrong, and give a basis for professional discipline in bodies that license practitioners. They do not resolve every dilemma, they are not laws, and in software they are not enforced as strongly as in licensed professions. Their force comes from the practice of individuals and the culture of teams.

## Ethical Frameworks

Philosophy offers several ways of reasoning about right and wrong, each of which highlights something different.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Approach</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Core idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question asked</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strength</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limitation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consequentialism (utilitarianism)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Right actions produce the best overall outcomes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which option does the most good and least harm, for all affected?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Focuses on real effects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to predict and measure; may sacrifice minorities</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deontology (duty-based)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Some actions are right or wrong regardless of outcome; people have rights and duties</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What duties and rights are involved? Would I accept this as a universal rule?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protects rights and promises</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules can conflict; may be rigid</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Virtue ethics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Act as a person of good character would</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What would an honest, fair, courageous professional do?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Focuses on character and judgment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less specific guidance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Care ethics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attend to relationships, vulnerability, and responsibility to those dependent on us</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who is vulnerable here, and what do they need?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Brings in context and empathy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less systematic</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Justice and fairness (for instance Rawls)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Arrange things as you would if you did not know your own position in society</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Would this be fair if I were the person most affected?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Highlights distribution and equity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abstract</td>
    </tr>
  </tbody>
</table>

Using several lenses together gives a fuller view than any one.

## A Method for Ethical Decisions

1. **Recognise** that there is an ethical dimension. Warning signs: someone could be harmed, deceived, excluded, or have their rights weakened; you would be uncomfortable explaining it publicly.
2. **Gather the facts.** What exactly is being asked? What do we know and not know?
3. **Identify the stakeholders** (users, non-users, vulnerable groups, society, the environment, colleagues, the company) and what is at stake for each.
4. **Identify the obligations:** laws, codes, contracts, and values.
5. **Consider options,** including ones beyond the first two offered. Rarely is the choice only "do it" or "refuse".
6. **Evaluate options** with the frameworks above, and with tests such as:
   - the **publicity test:** would I be comfortable if this were reported openly?
   - the **reversal test:** how would I feel if I were on the receiving end?
   - the **universality test:** what if everyone did this?
   - the **mentor test:** what would a respected colleague say?
7. **Decide, act, and document.**
8. **Review** the outcome and learn.

## Common Areas of Responsibility

### Honesty and Integrity

- Do not overstate what software can do, in marketing or in estimates. Do not hide known defects or risks from those who need to decide.
- Do not falsify tests, results, metrics, or reports. Never write code whose purpose is to deceive users or regulators.
- Admit mistakes early. Avoid conflicts of interest or disclose them.

### Competence and Quality

- Accept work only within your competence; say so when you are out of your depth.
- Apply sound engineering practice (the rest of this course) and warn when schedule pressure threatens safety or security.
- Keep learning.

### Safety and Public Interest

- For systems with safety implications, accept a higher duty of care (Unit 11).
- Raise concerns about risks to the public clearly and in writing, escalating if ignored.

### Fairness and Inclusion

- Consider who might be excluded, disadvantaged, or harmed by a design, data set, or algorithm (the next topic and the accessibility topic).

### Respect for People's Data and Autonomy

- Collect and use data fairly (previous topic). Avoid manipulating people against their interests.

### Respect for Colleagues and the Profession

- Give credit; do not plagiarise. Provide fair review. Treat colleagues respectfully, welcome diversity, and do not tolerate harassment.

### Environmental Responsibility

- Consider the energy and resource use of systems (topic 14).

## Handling Pressure and Raising Concerns

Ethical problems seldom announce themselves. They appear as a request to "just ship it", to "adjust" a figure, to collect "a bit more" data, or to ignore a test failure. The following steps are an ordered path.

1. **Clarify:** ask questions; you may have misunderstood, or may have missing information.
2. **State the concern** to your colleague or manager, specifically, calmly, in terms of risk and consequences, not accusation. Propose alternatives.
3. **Document** what you saw, said, and the response, with dates; keep it factual.
4. **Escalate** through the organisation: senior management, an ethics or compliance officer, internal audit, a legal department, or a confidential reporting line.
5. **Refuse** to take part in what is clearly unethical or illegal. Seek support from peers.
6. **External reporting** (whistleblowing) as a last resort, where internal routes fail or are unavailable and there is serious harm to the public.

### Whistleblowing

**Whistleblowing** is the disclosure by a member of an organisation of wrongdoing or serious risk to those outside it, such as a regulator, the press, or the public. It is justified in many ethical analyses when there is serious and considerable harm, internal channels have been used and failed (unless that would be futile or dangerous), the person has good evidence, and there is reasonable chance of success. It carries personal risk: retaliation, damage to a career, and legal action. Many countries have laws that protect whistleblowers in defined circumstances, but protection varies and is often incomplete. Individuals should seek legal advice and support from professional bodies and recognised organisations before disclosing, and should not disclose beyond what is necessary or reveal confidential information unrelated to the wrong.

Employers can reduce the need for dramatic disclosure by building a culture in which concerns are welcomed, with safe channels, no retaliation, and visible action.

## Ethics in Everyday Engineering Decisions

Ethical choices appear in ordinary work as often as in scandal.

- What to log, and for how long.
- Whether a notification is designed to inform or to pressure.
- Whether a test data set represents the people who will use the product.
- How to describe a fault found in production to users.
- Whether to ship with a known security flaw.
- What defaults to set.
- Whether to build a feature that could be used for surveillance or abuse, and what safeguards to add.
- Whether to take a contract from a client whose aims you find objectionable.

Asking "who could be affected, and how?" as a routine design-review question is the most practical habit.

## Institutions Beyond the Individual

Ethical practice is not only individual courage. Organisations can support it through ethics review boards for sensitive projects, impact assessments for AI and data systems, diverse teams, clear escalation paths, training, incentives that do not reward cutting corners, and public commitments. Professional societies, regulation, standards, and education reinforce these. Engineers can also contribute by speaking up in design reviews, mentoring, and joining professional communities.

<!--
IMAGE PROMPT  ->  generate as images/10_ethical_decision_steps.png   (16:9 explanatory diagram, place here)

A staircase of eight steps from Recognise up to Review, each with a small icon, and a branching path at the top labelled Raise concern with rungs Colleague, Manager, Compliance, Regulator.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: What Would You Do?

1. A manager asks you to change the wording of a test report so that a failed safety check appears to pass, to meet a release date. What do you do?
2. A feature requested by the business would collect users' locations continuously to sell to advertisers, without telling them. Which principles from the codes are involved?
3. Under what conditions is external whistleblowing generally considered justified?

For case 1, refuse to falsify, state the concern in writing, propose alternatives such as a short delay or a limited release, escalate if necessary, and keep records. For case 2, honesty and trustworthiness, respect for privacy, avoiding harm, and the public interest; raise the concern, propose a consented, minimised design, and escalate. For case 3, when serious harm to the public is likely, internal channels have been tried or would be futile or unsafe, there is good evidence, and disclosure is limited to what is necessary, ideally with legal advice.

## Conclusion

Professional ethics in software engineering is the set of moral principles and standards of conduct that guide engineers in their obligations to the public, clients and employers, colleagues, and the profession, especially where their work can affect the welfare, rights, and safety of others. Codes, frameworks, and a habit of asking who might be harmed turn good intentions into dependable practice.

Principles are easiest to understand through real events. The next topic examines case studies in ethics and harm.
