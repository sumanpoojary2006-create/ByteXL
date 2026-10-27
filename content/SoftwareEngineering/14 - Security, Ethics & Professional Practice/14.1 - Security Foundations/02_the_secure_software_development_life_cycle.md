## Introduction

Security problems are cheapest to prevent at the earliest stages of development and most expensive to correct after release. A flaw in a requirement or an architecture may require redesign; a flaw in code is a defect to be fixed and redeployed; a flaw found by an attacker may already have caused a breach. A secure software development life cycle (secure SDLC) integrates security activities into every stage of the process described in Units 1 and 2, so that security is built in progressively instead of being inspected in at the end.

This topic describes the security activities appropriate to each stage, the idea of shifting security left, well-known frameworks, and how security fits into agile and DevOps practice.

**Definition:** A secure software development life cycle is a development process in which security activities, such as security requirements, threat analysis, secure design and coding, security testing, and secure operation, are built into every phase of the life cycle so that vulnerabilities are prevented early and detected and corrected promptly.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_the_secure_software_development_life_cycle.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A horizontal life-cycle ribbon with stages Requirements, Design, Build, Test, Release, Operate, each with a small padlock activity icon beneath, and an arrow at the left pointing leftward labelled Shift left.

ON-IMAGE TEXT: show a short bold title "The Secure Software Development Life Cycle" plus only these few labels, large and legible: Security in Every Stage. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Earlier Is Better

Studies of defect cost, beginning with work by Barry Boehm in the 1970s and 1980s, find that the effort to fix a defect increases steeply with the time between introduction and discovery. Security defects follow the same pattern with an added factor: after release, the cost includes incident response, notification of affected people, legal consequences, and loss of trust.

**Shift left** is the practice of moving security activities earlier in the timeline (leftward on a diagram of the life cycle) so that problems are found when they are small. It does not mean that later activities are dropped; it means that checks are added early as well.

## Security Activities by Phase

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Phase</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Security activities</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Output</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Planning and requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Identify assets and sensitive data; define security and privacy requirements; identify legal, regulatory, and contractual obligations; classify data; decide the acceptable risk; write abuse cases alongside use cases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security requirements; data classification; compliance list</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Architecture and design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Threat modelling; design of trust boundaries, authentication, authorisation, encryption, logging, and isolation; selection of secure components; security design review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Threat model; security architecture; design decisions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Implementation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secure coding standards; safe libraries and frameworks; input handling; secret management; peer review with a security lens; static analysis in the editor and in the pipeline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reviewed code that meets standards</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security-focused tests; static and dynamic analysis; dependency scanning; fuzzing; penetration testing; review of results against requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test results; vulnerability reports</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release and deployment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hardened configuration; secrets management; integrity checks and signing of builds; release review; incident response readiness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verified release package</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operation and maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monitoring and logging; patching; vulnerability management; incident response; periodic reassessment; handling of reports from outside</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operating evidence; updates</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retirement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secure disposal of data, keys, and accounts; revoking access; planned decommissioning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safe end of life</td>
    </tr>
  </tbody>
</table>

### Abuse Cases and Misuse Cases

A use case describes how a legitimate user achieves a goal (Unit 3). A **misuse or abuse case** describes how an adversary might exploit or subvert the same functionality: how someone could guess another customer's order number, how a script could create thousands of accounts. Writing them beside the use cases turns vague worries into testable requirements.

### Security Requirements

Requirements should be specific and verifiable.

- Weak: "The system shall be secure."
- Better: "Only the customer who placed an order and authorised staff shall be able to view its details."
- Better: "Sensitive personal data shall be encrypted at rest and in transit."
- Better: "Failed sign-in attempts shall be limited, and repeated failures shall be logged and alerted."

Sources include laws and regulations (privacy, finance, health), contracts, industry standards, organisational policy, and the threat model.

## Frameworks and Standards

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Framework</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Source</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Microsoft Security Development Lifecycle (SDL)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Microsoft, from about 2004</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A set of practices applied across the phases, from training to incident response</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">OWASP SAMM (Software Assurance Maturity Model)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">OWASP</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A measurable model with business functions (governance, design, implementation, verification, operations) and maturity levels</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">BSIMM (Building Security In Maturity Model)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Synopsys, based on observation of real organisations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A descriptive survey of the practices of many firms to benchmark against</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">NIST Secure Software Development Framework (SSDF)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">US National Institute of Standards and Technology</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A set of high-level practices, used also in government procurement</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Touchpoints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gary McGraw</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Seven practices such as code review, risk analysis, and penetration testing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ISO/IEC 27001 and 27034</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">International standards bodies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Management of information security and application security</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">OWASP ASVS (Application Security Verification Standard)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">OWASP</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A checklist of verifiable requirements at three levels of rigour</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Common Criteria</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">International</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Formal evaluation of security products</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Industry rules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PCI DSS for payment cards; HIPAA for US health data; sector regulators</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compulsory requirements in their domains</td>
    </tr>
  </tbody>
</table>

Organisations rarely adopt a framework wholesale. They use one as a map, choose the practices that fit their risk, and improve gradually.

## Security in Agile and DevOps

Short iterations and continuous delivery do not suit a heavy gate at the end, so security is woven into the flow.

- **Security stories and acceptance criteria** in the backlog, and security items in the definition of done (Unit 2).
- **Lightweight threat modelling** for each significant feature or change.
- **Automated checks in the pipeline** (Unit 9): static analysis, secret scanning, dependency scanning, container image scanning, and automated tests of security behaviour, all failing the build on serious findings.
- **Infrastructure as code** reviewed and scanned like application code.
- **Peer review** with attention to security.
- **Short feedback loops:** findings reach the developer within minutes, not months.
- **Security champions** in each team to carry knowledge and advocate.
- **Regular training** on common weaknesses and secure practices.

The name **DevSecOps** expresses the aim: development, security, and operations share responsibility, with automation making the secure path routine.

## Managing Security Debt

Like technical debt (Unit 8), unaddressed vulnerabilities accumulate. A vulnerability backlog should be triaged by severity and exposure, with agreed deadlines for fixing, for example critical issues in days. Severity is commonly rated using the **Common Vulnerability Scoring System (CVSS)**, which produces a score from 0 to 10 based on how easily an attack can be launched and how severe the effects are, and published weaknesses are catalogued in the **CVE** list (Common Vulnerabilities and Exposures) and the **CWE** list (Common Weakness Enumeration). Context matters: a high-scoring flaw in a component that is not reachable by attackers may matter less than a moderate one on a public interface.

## Release Gates and Evidence

Before release, a team should be able to show:

- the threat model has been reviewed and its significant threats addressed;
- required security tests passed and open findings are accepted by named owners;
- dependencies have no unaddressed critical vulnerabilities;
- secrets are not in the code or the build output;
- monitoring and incident response are in place;
- compliance obligations are met.

Gates should be proportionate: strict for high-risk changes, light for low-risk ones, so that they support speed rather than obstruct it.

## Measuring Progress

Useful indicators are the number and age of open vulnerabilities by severity; time to fix; proportion of code covered by automated security checks; proportion of services with up-to-date threat models; dependency freshness; training completion; and time to detect and respond to incidents. Avoid measures that reward hiding findings.

## Common Failure Patterns

- **Security as a final inspection:** problems found a week before release are either ignored or cause delay.
- **Tools without people:** scanners produce noise that nobody triages.
- **Checklist compliance without understanding:** meeting the letter of a standard while real risks go untouched.
- **Blame culture:** staff hide mistakes instead of reporting them.
- **Treating developers as the enemy** instead of equipping them with easy-to-use secure defaults.

<!--
IMAGE PROMPT  ->  generate as images/02_secure_sdlc_activities.png   (16:9 explanatory diagram, place here)

A left-to-right life-cycle timeline with six stages; beneath each, a lane of security activity icons (requirements, threat model, secure coding, scanning, penetration test, monitoring). A curve above shows cost of fixing a defect rising to the right, with a green arrow showing the shift left.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Place the Activity

1. At which phase should the question "what would an attacker try to do with this feature?" first be asked?
2. A build pipeline passes all functional tests but a scan reports a critical flaw in a library. What should happen?
3. Why is "the system shall be secure" a poor requirement?

For case 1, as early as requirements and design, through abuse cases and threat modelling. For case 2, the build should fail or be blocked until the library is updated or the risk is explicitly assessed and accepted. For case 3, it is not specific or verifiable; requirements should say what is protected, from whom, and how this will be checked.

## Conclusion

A secure software development life cycle is a development process in which security activities, such as security requirements, threat analysis, secure design and coding, security testing, and secure operation, are built into every phase of the life cycle so that vulnerabilities are prevented early and detected and corrected promptly. Automating checks and sharing responsibility make it practical even in fast-moving teams.

One of the central activities of secure design is the systematic analysis of how a system could be attacked. The next topic covers threat modelling.
