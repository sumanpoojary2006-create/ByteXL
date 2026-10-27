## Introduction

Much of the data that software holds is about people: who they are, where they go, what they buy, whom they talk to, and what they are worried about. Protecting such data from attackers is security; deciding what to collect, why, for how long, and what individuals may control is privacy. A system can be perfectly secure and still invade privacy, for instance by gathering far more than it needs and using it for purposes nobody agreed to. Privacy by design is the approach of building respect for personal data into the structure of a system from the start, instead of adding warnings and controls afterwards.

This topic defines personal data, presents the principles of privacy by design and the data-protection principles found in the European General Data Protection Regulation (GDPR) and similar laws, explains lawful bases and individual rights, and describes how engineers translate these into design decisions.

**Definition:** Privacy by design is the practice of embedding the protection of personal data into the design and operation of systems from the earliest stage, by collecting only what is necessary, using it only for stated purposes, giving people transparency and control, and protecting it throughout its life.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_privacy_by_design.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A person silhouette on the left handing a small data card across a boundary to a system box; a funnel labelled Only what is needed narrows the flow; sliders on the person side labelled Consent and Control.

ON-IMAGE TEXT: show a short bold title "Privacy by Design" plus only these few labels, large and legible: Minimise, Explain, Control. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Privacy and Security Compared

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Security</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Privacy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Core question</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is the data protected from unauthorised parties?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Should this data be collected and used at all, and are individuals in control?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concerned with</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attackers, errors, availability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Appropriate and fair use, including by the organisation itself</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failure example</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A breach exposes records</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data legitimately held is used for an unrelated purpose or kept forever</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relationship</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security is a necessary means of protecting privacy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Privacy goes beyond security</td>
    </tr>
  </tbody>
</table>

## What Is Personal Data?

**Personal data** is any information relating to an identified or identifiable person. It is broader than names and addresses.

- **Direct identifiers:** name, identity numbers, email address, phone number, photograph.
- **Indirect or technical identifiers:** device identifiers, internet addresses, cookie identifiers, location history, account numbers.
- **Combinations:** a postcode, birth date, and sex together can often identify a single person even though none does alone.
- **Behavioural data:** purchases, browsing history, usage patterns.
- **Derived and inferred data:** scores, profiles, and predictions made about a person.

**Special categories** (called sensitive data) receive stronger protection: racial or ethnic origin, political opinions, religious beliefs, trade-union membership, genetic and biometric data used for identification, health, and sex life or orientation. Children's data is also given extra care.

**Anonymised** data, from which individuals can no longer be identified by any reasonable means, falls outside most privacy laws, but true anonymisation is difficult: many supposedly anonymous data sets have been re-identified by linking them with other data. **Pseudonymised** data replaces identifiers with codes but can be traced back using additional information, so it remains personal data, though it lowers risk.

## The Seven Principles of Privacy by Design

Ann Cavoukian, then Information and Privacy Commissioner of Ontario, set out seven foundational principles in the 1990s, later adopted widely.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1. Proactive, not reactive; preventative, not remedial</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anticipate and prevent privacy problems before they occur</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2. Privacy as the default setting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The most privacy-protective choice applies automatically, without the user having to ask</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3. Privacy embedded into design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It is an essential part of the system, not an add-on</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4. Full functionality: positive-sum, not zero-sum</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Seek solutions that achieve both privacy and the business aim, rather than trade one for the other</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5. End-to-end security: full life-cycle protection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protect data from collection to deletion</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6. Visibility and transparency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operate openly, in a way that can be verified</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">7. Respect for user privacy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the interests of the individual at the centre: strong defaults, clear notice, easy choices</td>
    </tr>
  </tbody>
</table>

## Data-Protection Principles in Law

The GDPR, which took effect across the European Union in May 2018, has influenced laws around the world. Article 25 requires **data protection by design and by default.** Article 5 lists principles for processing personal data.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What engineers do</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lawfulness, fairness, and transparency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">There is a valid legal basis; people are not misled; they are told what happens to their data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear privacy notices; no hidden use; no manipulative interfaces</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purpose limitation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data is collected for specified, explicit, legitimate purposes and not used in incompatible ways</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Record the purpose of each data item; block reuse for unrelated ends</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data minimisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only data adequate, relevant, and necessary for the purpose is collected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Challenge every field: do we need this? Prefer less precise data (age band, not birth date; city, not exact location)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accuracy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data is correct and kept up to date</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ways to view and correct data; validation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Storage limitation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data is kept no longer than necessary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retention periods; automatic deletion and archiving</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrity and confidentiality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data is protected from loss, damage, and unauthorised access</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security measures of the previous topics</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accountability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The organisation can demonstrate compliance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation, records of processing, impact assessments, audits</td>
    </tr>
  </tbody>
</table>

### Lawful Bases

Personal data may be processed only if one of a limited set of bases applies: **consent;** necessity for a **contract** with the person; a **legal obligation;** protecting **vital interests;** a **public task;** or the organisation's **legitimate interests,** balanced against the rights of the person. Each purpose needs its own basis; consent is only one option and must be freely given, specific, informed, unambiguous, and as easy to withdraw as to give. Pre-ticked boxes and bundled consent do not count.

### Rights of Individuals

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Right</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Implication for systems</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Information</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To know what is collected and why</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear notices</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Access</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To obtain a copy of their data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ability to find and export all data about a person</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rectification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To have inaccurate data corrected</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Edit paths, propagated to copies</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Erasure ("right to be forgotten")</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To have data deleted in certain cases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deletion across databases, caches, logs, backups and processors, with defined limits</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Restriction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To pause processing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flags that stop use</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Portability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To receive data in a usable format and move it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Export in structured, common formats (Unit 12)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Objection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To object to certain processing, such as direct marketing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Opt-out mechanisms honoured everywhere</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rights concerning automated decisions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To human review of significant decisions made by algorithms and to explanation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Human-in-the-loop designs; explainability</td>
    </tr>
  </tbody>
</table>

These rights must be designed in. A system that scatters personal data across dozens of unconnected stores cannot answer an access request or complete an erasure; architecture decisions decide whether compliance is possible.

### Other Laws

Privacy regulation varies by region and sector: the UK has its own version of the GDPR; California's CCPA/CPRA gives rights to residents; India's Digital Personal Data Protection Act (2023), Brazil's LGPD, and many others exist; sector laws protect health records (HIPAA in the United States), children's data (COPPA), and financial data. Penalties can be severe: the GDPR allows fines of up to 20 million euros or 4 per cent of global annual turnover, whichever is higher. Obligations include **breach notification,** to the regulator within 72 hours in many cases, and to affected people where risk is high. Engineers need to know that the rules exist and to involve legal and privacy specialists, who give legal advice; this course gives general understanding only.

## Privacy in Engineering Practice

### Design Strategies

Jaap-Henk Hoepman proposed eight strategies that translate principles into design.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minimise</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limit the amount of personal data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not ask for a phone number if email is enough</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hide</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevent exposure and linking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Encryption; separate storage of identifiers</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Process in distributed ways</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep identity data apart from behavioural data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abstract</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limit detail</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Store aggregates or approximations</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inform</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tell people what happens</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plain-language notices, just in time</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Give people choice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Settings, consent management, deletion tools</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Enforce</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make the policy binding in the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical controls matching the stated policy</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Demonstrate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prove compliance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logs, audits, documentation</td>
    </tr>
  </tbody>
</table>

### Practical Techniques

- **Data inventory and mapping:** know what personal data exists, where, why, and who has it. You cannot protect what you have not listed.
- **Data classification:** label data by sensitivity and apply matching controls.
- **Collect less:** challenge every field in a form and every analytics event.
- **Short retention:** define how long each data class is kept and automate deletion, including in backups and logs.
- **Purpose-bound access:** only roles that need the data for its purpose can reach it; log access to sensitive records.
- **Pseudonymisation and aggregation** for analytics and testing; **never use real personal data in test or development environments** unless protected as in production; use synthetic data.
- **Encryption** in transit and at rest; tokenisation of identifiers such as card numbers.
- **Privacy-enhancing technologies:** differential privacy (adding calibrated noise so that results do not reveal individuals), on-device processing, federated learning, and secure computation.
- **Consent management:** record who agreed to what and when; make withdrawal easy and effective.
- **Privacy-friendly defaults** in every setting.
- **Vendor and third-party control:** scripts, software development kits, and analytics services embedded in an application may send user data elsewhere; assess and limit them. Contracts with processors must specify protection.
- **Cross-border transfers:** moving data between jurisdictions may need legal safeguards.

### Privacy Impact Assessments

A **data protection impact assessment (DPIA)** is required under the GDPR for processing likely to cause high risk (large-scale profiling, sensitive data, systematic monitoring). It describes the processing, assesses necessity and proportionality, identifies risks to individuals, and sets measures to reduce them. Doing it at design time is far cheaper than redesigning later. The privacy equivalent of the threat model, such as LINDDUN, helps structure the analysis (previous topics).

### In Agile Teams

Add privacy criteria to user stories and to the definition of done; ask "what data does this feature need and why?" in refinement; include privacy in code review; keep an up-to-date record of data flows; assign a privacy champion; and treat privacy incidents like security incidents.

## Beyond Compliance: Respect

Legal minimums are a floor. Engineers face choices that law does not settle: whether to track users across sites, to infer sensitive traits from behaviour, to combine data sets in ways people would not expect, or to keep data "just in case". A useful test is whether a person would be **surprised** and **unhappy** to learn how their data is used. Trust, once lost, is hard to regain, and the data that is never collected can never be leaked, sold, subpoenaed, or misused.

<!--
IMAGE PROMPT  ->  generate as images/09_data_minimisation_and_user_rights.png   (16:9 explanatory diagram, place here)

Left: a form with six fields where four are crossed out in green as unnecessary, funnelling to two. Right: a data life-cycle ribbon (Collect, Use, Store, Share, Delete) with a retention clock and icons for user rights (view, correct, delete, export) attached below it.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Apply the Principles

1. A signup form asks for date of birth, home address, and phone number, though the service only needs to confirm that users are adults and send emails. Which principle is breached, and what should change?
2. A user asks to delete their account. Deleting the main database row leaves their data in analytics copies, logs and backups. What does this show?
3. Is data with names replaced by random codes, but with a table that maps codes back to names, anonymous?

For case 1, data minimisation; ask only for what is needed (for example, a confirmation of being over a minimum age and an email address). For case 2, deletion must be designed across all stores; knowing where personal data lives is a precondition. For case 3, no; it is pseudonymised and still personal data, because the mapping allows re-identification.

## Conclusion

Privacy by design is the practice of embedding the protection of personal data into the design and operation of systems from the earliest stage, by collecting only what is necessary, using it only for stated purposes, giving people transparency and control, and protecting it throughout its life. Minimising data, limiting purposes and retention, and building in the rights of individuals are engineering decisions that law now requires and users increasingly expect.

Privacy is one part of a wider question: what do engineers owe the people their work affects? The next topic introduces professional ethics.
