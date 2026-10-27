## Introduction

Although every system is different, the weaknesses that attackers exploit are surprisingly repetitive. The same few categories of mistake account for a large share of real breaches, year after year, across languages and industries. The Open Worldwide Application Security Project (OWASP), a non-profit community founded in 2001, publishes a ranked list of the ten most critical categories of web application risk, based on data from many organisations and on surveys of practitioners. The OWASP Top 10 is the most widely used starting point for teaching and checking secure development, and a list of the mistakes most worth avoiding.

This topic explains each category of the 2021 edition in concept, its typical causes, and the general defences, without technical exploit detail. Later topics treat the most important defences in depth.

**Definition:** The OWASP Top 10 is a regularly updated awareness document that ranks the ten most critical categories of security risk to web applications, each category grouping related weaknesses by cause and consequence, to guide developers and organisations toward the most valuable defences.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_common_vulnerabilities_the_owasp_top_10.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A ranked list of ten horizontal bars of decreasing length, each with a small padlock-and-crack icon, the top three highlighted in red.

ON-IMAGE TEXT: show a short bold title "Common Vulnerabilities: The OWASP Top 10" plus only these few labels, large and legible: Ten Recurring Mistakes. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The 2021 List

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rank</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Category</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In one sentence</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Broken access control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users can act outside their intended permissions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A02</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cryptographic failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sensitive data is not protected properly in transit or at rest</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A03</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Injection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Untrusted data is interpreted as part of a command or query</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A04</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Insecure design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The design lacks the controls the threats require</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A05</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security misconfiguration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Systems are set up insecurely, or left with defaults</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A06</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vulnerable and outdated components</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Known flaws in libraries and platforms are left unpatched</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A07</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Identification and authentication failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak proof of who a user is</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A08</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software and data integrity failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code, updates, and data are trusted without verification</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A09</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security logging and monitoring failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attacks go unnoticed because events are not recorded or watched</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A10</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Server-side request forgery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The server can be tricked into making requests on behalf of an attacker</td>
    </tr>
  </tbody>
</table>

The list is revised every few years; categories change in rank and scope as practice and attacks evolve. The ideas matter more than the numbers.

## A01 Broken Access Control

Access control enforces the policy of who may do what. It is broken when the system fails to check permission at the moment of use. Typical forms:

- Viewing or changing another user's records by altering an identifier in a request (an **insecure direct object reference**).
- Reaching administrative functions by guessing their address, because only the menu hides them.
- Acting in a role that was never granted, such as a normal user changing their own privilege level.
- Relying on checks performed only in the client, such as the browser or mobile app, which an attacker controls.
- Missing checks for particular actions (for example, viewing is protected but deleting is not).

**Defences:** deny by default; perform every check on the server for every request; check ownership of each object, not just login status; use central, reusable authorisation logic; log failures; test with different roles. This has been the most commonly found category in recent analyses.

## A02 Cryptographic Failures

Sensitive data, such as passwords, personal details, and payment information, must be protected in transit and at rest. Failures include sending data without encryption, using outdated or weak algorithms, poor key management, storing passwords without proper protection, and collecting more sensitive data than necessary.

**Defences:** classify data; do not store what you do not need; encrypt in transit with current transport security; encrypt sensitive data at rest; store passwords with dedicated slow hashing designed for the purpose; use well-tested libraries, never invented algorithms; manage keys carefully (see topic 7).

## A03 Injection

Injection occurs when data supplied by a user, or by any outside source, is mixed into a command or query in a way that lets the data be understood as instructions. The interpreter, such as a database engine, an operating system shell, a directory service, or a template engine, cannot tell where the programmer's intent ends and the attacker's input begins. The consequences range from reading all data to taking over the server. Cross-site scripting, in which attacker-supplied content runs in another user's browser, is a form of injection into web pages and was folded into this category in 2021.

**Defences:** keep data and instructions separate by using interfaces that pass data as parameters; validate input on the server; encode output for the context in which it is shown; apply least privilege to the accounts that interpreters use; use safe frameworks. Topic 5 treats these in depth.

## A04 Insecure Design

Some failures cannot be repaired by better coding because the design itself omits needed protection: a password-reset flow that reveals whether an account exists, a booking system that allows one buyer to reserve all tickets, a workflow with no limit on how often a costly action may be triggered. This category was introduced to promote design-stage practices.

**Defences:** threat modelling; abuse cases; secure design patterns; reference architectures; limits on resource use and on business-logic abuse; security requirements; unit and integration tests of the misuse cases.

## A05 Security Misconfiguration

Secure software can be undone by how it is deployed: default accounts and passwords, unnecessary features enabled, open cloud storage, overly detailed error messages, missing security headers, unpatched servers, permissive permissions, and differences between environments.

**Defences:** a repeatable hardening process; minimal installations; infrastructure as code with review (Unit 9); automated configuration scanning; separate and secure environments; regular review of cloud permissions.

## A06 Vulnerable and Outdated Components

Modern applications consist mostly of third-party libraries, frameworks, and platforms. When a flaw is published in one of them, attackers scan the internet for systems that have not updated. The 2017 breach of a major credit reporting agency, which exposed personal data of roughly 147 million people, was attributed to a known flaw in a web framework for which a fix was available. The late 2021 flaw in a widely used logging library affected countless applications within days.

**Defences:** keep an inventory of components (a **software bill of materials**); scan dependencies continuously; update promptly; remove unused components; choose well-maintained projects; monitor advisories. Topic 7 returns to this.

## A07 Identification and Authentication Failures

Weak authentication allows impersonation: permitting weak or common passwords, no protection against repeated guessing, exposed session identifiers, session that never expire, poor recovery processes, and no second factor for important accounts.

**Defences:** multi-factor authentication; limits on attempts; screening passwords against lists of known breached ones; secure session management; careful recovery flows; using established identity services (topic 6).

## A08 Software and Data Integrity Failures

Systems fail when they accept code or data from sources they cannot verify: auto-updates without signature checks, build pipelines that can be modified by outsiders, libraries pulled from unverified repositories, and data that is deserialised without checks so that crafted content alters behaviour. The compromise of a network-management vendor's build process in 2020 delivered malicious updates to thousands of customers.

**Defences:** digitally signed code and updates; verified sources; protected build and deployment pipelines; reviewed changes; safe handling of serialised data (Unit 12).

## A09 Security Logging and Monitoring Failures

Without good logs and alerts, attacks go unnoticed for months. Typical problems are failures to record sign-in attempts, access denials and high-value actions; logs without enough context; logs stored where attackers can alter them; no alerting; and, conversely, logging sensitive data.

**Defences:** record security-relevant events with time, identity, and outcome; protect and centralise logs; set alerts for suspicious patterns; rehearse incident response (Unit 9). Do not log secrets or personal data unnecessarily.

## A10 Server-Side Request Forgery

When an application fetches a resource whose address is supplied by a user, an attacker may direct the server to reach internal systems that the attacker cannot reach directly, including cloud management services. 

**Defences:** validate and restrict destinations with allow-lists; block access to internal address ranges; do not return raw responses to users; segment the network.

## Patterns Behind the List

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Underlying cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Categories it touches</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trusting input or other parties</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Injection, access control, integrity failures, request forgery</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing or misplaced checks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Broken access control, authentication failures</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor handling of secrets and data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cryptographic failures, logging failures</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Neglected maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vulnerable components, misconfiguration</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design without threat thinking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Insecure design</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lack of visibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logging and monitoring failures</td>
    </tr>
  </tbody>
</table>

Beyond the web, similar lists exist for APIs, mobile applications, and for large language model applications. Other catalogues are **CWE** (Common Weakness Enumeration), a detailed taxonomy of software weaknesses, and the **CWE Top 25** most dangerous weaknesses published annually.

## Using the List Well

- Treat it as a **minimum awareness baseline,** not a complete checklist; it says nothing, for example, of your specific business logic.
- **Map defences to each category** in architecture and code review checklists.
- **Train developers** with examples relevant to your stack.
- **Test for these categories** with automated and manual methods (topic 8).
- **Review the list when it is updated.**

<!--
IMAGE PROMPT  ->  generate as images/04_owasp_top_10_overview.png   (16:9 explanatory diagram, place here)

A grid of ten tiles labelled A01 to A10 with short names and a simple icon each (key, lock, syringe-style injection arrow, blueprint, gear, puzzle piece, user badge, chain link, notebook, arrow looping outward). Colour intensity indicates rank.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Name the Weakness

1. A customer changes the number at the end of an order's web address and sees someone else's order. Which category?
2. A site still runs a framework with a known, fixed flaw published months earlier. Which category?
3. An attack is carried out over weeks without anyone noticing. Which category contributed?

Case 1 is broken access control (an insecure direct object reference); the server must check that the order belongs to the requester. Case 2 is vulnerable and outdated components. Case 3 is security logging and monitoring failures.

## Conclusion

The OWASP Top 10 is a regularly updated awareness document that ranks the ten most critical categories of security risk to web applications, each category grouping related weaknesses by cause and consequence, to guide developers and organisations toward the most valuable defences. A small set of recurring mistakes accounts for most breaches, and learning to recognise them is the quickest route to safer software.

The defence against the most notorious category, injection, rests on one principle: never trust input. The next topic explains input validation and the safe handling of data.
