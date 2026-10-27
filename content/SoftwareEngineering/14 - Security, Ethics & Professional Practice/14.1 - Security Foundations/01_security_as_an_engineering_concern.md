## Introduction

Software holds money, health records, private messages, and the control systems of physical infrastructure. Anything of value that software handles can become the target of someone who is not meant to have it, or can be damaged by ordinary mistakes. Security is the property of a system that it protects its assets against harm from misuse, whether deliberate or accidental. It is not a feature added at the end, nor the responsibility of a separate team alone; it is a quality attribute, like performance or reliability, that arises from decisions made throughout design, construction, and operation.

This topic introduces the vocabulary of security, the three core properties of confidentiality, integrity, and availability, the nature of the threat landscape, the principles of secure design, and why security is everyone's responsibility in an engineering team.

**Definition:** Software security is the engineering of systems so that their assets, such as data, functions, and services, remain protected against unauthorised access, modification, and disruption, by preventing, detecting, and responding to attacks and errors throughout the life of the system.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_security_as_an_engineering_concern.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A central vault icon labelled Asset surrounded by three shields labelled Confidentiality, Integrity, Availability, with arrows from outside labelled Threats being deflected.

ON-IMAGE TEXT: show a short bold title "Security as an Engineering Concern" plus only these few labels, large and legible: Protect the Asset. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Basic Vocabulary

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Asset</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anything of value to protect: data, services, reputation, money, physical safety</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Threat</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A potential cause of harm, such as a criminal, a careless insider, or a natural event</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Threat actor (attacker)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A person or group that may act against the system</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vulnerability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A weakness in design, code, configuration, or process that a threat can exploit</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exploit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A method or tool that takes advantage of a vulnerability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attack</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An attempt to cause harm by exploiting a vulnerability</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The likelihood that a threat exploits a vulnerability, combined with the size of the harm</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control (countermeasure)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anything that reduces risk: a design choice, a technical mechanism, or a procedure</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attack surface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The sum of all the points where an attacker can try to enter or extract data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Incident / breach</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An event in which security is actually compromised</td>
    </tr>
  </tbody>
</table>

Security work is risk management, as in Unit 13: it is neither possible nor economical to remove all risk, so effort is directed at the most serious risks to the most valuable assets.

## The CIA Triad

Security properties are often grouped as three, abbreviated CIA.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Property</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Violation example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical controls</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confidentiality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Information is available only to those authorised to see it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer records read by a stranger</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Access control, encryption, careful data handling</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Information and systems are changed only in authorised ways and remain accurate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An order total altered in transit; tampered software update</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Validation, digital signatures, checksums, audit trails, access control</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Availability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system and its data are accessible when needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A service taken offline by a flood of requests; data destroyed by ransomware</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redundancy, backups, capacity planning, rate limiting</td>
    </tr>
  </tbody>
</table>

Further properties often added are **authenticity** (a party or message really is what it claims), **accountability** or **non-repudiation** (actions can be attributed and cannot be denied afterwards), and **privacy** (personal data is handled according to the rights of individuals, covered later in this unit).

The properties can conflict: tight confidentiality may reduce availability, and extreme availability may lead to broader access. Engineers therefore weigh them according to the purpose of the system. A hospital emphasises availability and integrity of records; a secrets vault emphasises confidentiality.

## The Threat Landscape

### Who Attacks

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Actor</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Motivation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Capability</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Opportunistic criminals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Money, through fraud, theft, or ransom</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated scanning of the entire internet for known weaknesses</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Organised crime</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Profit at scale: ransomware, payment fraud, selling stolen data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Skilled, well resourced</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Insiders</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grievance, profit, or simple carelessness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Legitimate access, knowledge of the system</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hacktivists</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Political or social aims</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Variable</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">State-sponsored actors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Espionage, sabotage, strategic advantage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very high, persistent</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Competitors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Industrial espionage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Variable</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Researchers and curious individuals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learning, recognition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Variable; usually benign if properly handled</td>
    </tr>
  </tbody>
</table>

### Common Kinds of Attack

- **Exploiting software flaws** such as injection, broken access control, and unpatched components.
- **Credential attacks:** guessing passwords, reusing leaked ones, and stealing sessions.
- **Social engineering and phishing:** deceiving people into revealing secrets or taking actions. Humans are often the weakest link.
- **Malware and ransomware:** malicious software that steals, destroys, or encrypts data.
- **Denial of service:** overwhelming a system so legitimate users cannot reach it.
- **Supply-chain attacks:** compromising a component, tool, or update that many systems trust.
- **Misconfiguration exploitation:** open storage, default passwords, and exposed management interfaces.
- **Physical attacks and theft of devices.**
- **Abuse of legitimate features:** using a system as designed, but for harmful ends.

### Why It Matters

Breaches have real consequences: harm to individuals whose data is exposed, financial loss, legal penalties, loss of customer trust, operational disruption, and in safety-related systems, physical harm. The cost of fixing a vulnerability grows sharply the later it is found, which echoes the cost-of-defects curve of Unit 10.

## Principles of Secure Design

In 1975 Jerome Saltzer and Michael Schroeder published design principles for protection mechanisms that are still taught today.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Least privilege</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every user and component gets only the access it needs, for only as long as needed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Economy of mechanism</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep designs simple; complexity hides flaws</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fail-safe defaults</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deny by default; access is granted explicitly, so mistakes err on the side of safety</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complete mediation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check every access to every resource, every time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Open design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security must not rely on the secrecy of the design; assume attackers know how the system works, and depend only on the secrecy of keys</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separation of privilege</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Require more than one condition for sensitive actions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Least common mechanism</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minimise shared components that could carry flaws between users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Psychological acceptability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security must be usable, or people will bypass it</td>
    </tr>
  </tbody>
</table>

Other widely taught principles are:

- **Defence in depth:** several independent layers of protection, so the failure of one does not expose everything.
- **Minimise the attack surface:** remove unneeded features, ports, and accounts.
- **Never trust input or other components:** validate at every trust boundary.
- **Zero trust:** do not grant trust merely because a request comes from inside the network; verify identity and authorisation for every request.
- **Secure by default and by design:** the safe configuration is the default, and security is considered from the start.
- **Assume breach:** design so that one compromised component or account cannot lead to total compromise, and so that attacks are detected quickly.
- **Fail securely:** when errors occur, the system must not open access or leak details.
- **Keep security independent of obscurity:** hiding something is not protecting it.
- **Make the secure path the easy path.**

## Security Is a Quality Attribute

Security shares the character of other non-functional qualities (Unit 1 and Unit 3): it is specified by requirements, shaped by architecture, built into code, verified by testing and review, and maintained in operation. It cannot be added by a final inspection.

- **Requirements:** who may do what, what must be protected, what laws apply.
- **Architecture:** boundaries, isolation, authentication, and data flow.
- **Construction:** secure coding practices and safe libraries.
- **Verification:** security testing and review.
- **Operation:** patching, monitoring, and incident response.

### Who Is Responsible?

Everyone. Specialists provide expertise, tools, and review, but the people who make the daily decisions on design and code are the engineers. Product managers decide what to collect and keep; testers look for abuse cases; operations staff manage configuration and patches. A **security champions** programme, in which a member of each team takes a special interest, is a common way to spread knowledge.

## Security and Other Qualities

- **Usability:** hard-to-use security gets bypassed. Good design makes the safe choice natural.
- **Performance:** encryption and checks have cost, usually small.
- **Cost and schedule:** security investment competes with features; risk-based argument is the best route to a fair balance.
- **Privacy and ethics:** collecting less data reduces both risk and harm.
- **Reliability:** many security failures also reduce reliability, and vice versa.

## Realistic Expectations

- **No system is perfectly secure.** The aim is to make attacks costly and failures contained.
- **Attackers need to find one weakness; defenders must cover all.** This asymmetry argues for depth and for detection.
- **Security is continuous.** New vulnerabilities in dependencies and new attack techniques appear every week.
- **Evidence beats confidence.** Claims of security should be supported by threat analysis, testing, and review.
- **Reporting should be safe.** Organisations that welcome reports from researchers and staff, often through a published disclosure policy, learn of problems sooner.

<!--
IMAGE PROMPT  ->  generate as images/01_cia_triad_and_defence_in_depth.png   (16:9 explanatory diagram, place here)

Left: a triangle with Confidentiality, Integrity, Availability at the corners and a data icon in the centre. Right: concentric rings around an asset labelled Network, Application, Data, People, Monitoring, with an attack arrow stopped at an outer ring and a second one stopped at an inner ring.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Classify the Harm

1. A competitor reads a company's unreleased product plans. Which property was violated?
2. An attacker changes the destination account in a payment request. Which property was violated?
3. A flood of requests makes a site unreachable. Which property was violated?
4. Why is hiding the design of a security mechanism an unreliable defence?

Case 1 is confidentiality. Case 2 is integrity. Case 3 is availability. For case 4, secrets about design tend to leak or be discovered, and the principle of open design says that protection should rest on keys and sound mechanisms, which can be changed if exposed, rather than on obscurity.

## Conclusion

Software security is the engineering of systems so that their assets, such as data, functions, and services, remain protected against unauthorised access, modification, and disruption, by preventing, detecting, and responding to attacks and errors throughout the life of the system. Understanding assets, threats, and vulnerabilities, and applying principles such as least privilege and defence in depth, give every engineer a basis for making sound decisions.

Security is more reliable when it is planned into every stage of development, not inspected at the end. The next topic describes the secure software development life cycle.
