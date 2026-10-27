## Introduction

Few organisations build everything themselves. They buy software packages, subscribe to cloud services, hire contractors, and commission whole systems from outside firms. Each of these arrangements places part of the work, and part of the risk, in someone else's hands under the terms of an agreement. The form of the contract determines who bears the cost of uncertainty, how change is handled, and what happens when things go wrong. Engineers who understand these arrangements make better technical recommendations and avoid being surprised by commercial constraints.

This topic explains the reasons for outsourcing and buying, the main contract models and their trade-offs, service level agreements, selecting and managing vendors, and the risks of depending on third parties.

**Definition:** Outsourcing is the use of an external organisation to perform work or provide services that could otherwise be done in-house, and vendor management is the practice of selecting, contracting with, monitoring, and governing those external suppliers to ensure that they deliver the agreed value and that the resulting risks are controlled.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_outsourcing_contracts_and_vendor_management.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A client box on the left and a vendor box on the right connected by a document labelled Contract, with arrows labelled Requirements, Deliverables, Payment, and a gauge labelled Service Level beneath.

ON-IMAGE TEXT: show a short bold title "Outsourcing, Contracts and Vendor Management" plus only these few labels, large and legible: Client, Contract, Vendor. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Build, Buy, or Partner

Before outsourcing, an organisation chooses how to obtain a capability.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Option</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Suits</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cautions</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build in-house</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Own staff design and develop it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Core differentiating capabilities; sensitive data; long-lived products</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs skills and capacity; slower to start</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Buy off the shelf</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Purchase a ready-made product or subscribe to a service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Common needs such as payroll, email, or accounting</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fit is imperfect; customisation costly; dependence on vendor roadmap</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use open source</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adopt freely licensed components</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Common technical building blocks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs in-house skill for support; licence obligations; maintenance of dependencies</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Outsource development</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contract an external firm to build custom software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Short-term capacity; specialised skills; non-core work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Management overhead; knowledge leaves with the vendor</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contractors or staff augmentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Individuals join your team for a period</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flexible capacity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knowledge loss when they leave</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Managed services and cloud</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The vendor operates infrastructure or applications</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reducing operational burden</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost control; lock-in; shared responsibility for security</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Partnership or joint venture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared investment and risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long-term strategic aims</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Governance complexity</td>
    </tr>
  </tbody>
</table>

A guideline is to **build what differentiates the business** and **buy what is common.** The decision should consider total cost over the life of the product, not only the first price: licences, integration, customisation, training, operations, upgrades, and the cost of leaving.

## Why Organisations Outsource

- **Access to skills** not available internally.
- **Flexible capacity** for peaks of work.
- **Cost,** often through lower rates, though savings can be lost to management, rework, and communication.
- **Speed,** by starting with a ready team or product.
- **Focus,** allowing the organisation to concentrate on its core.
- **Round-the-clock work** through different time zones.

Its risks include loss of control and knowledge, quality problems, communication difficulty across distance, cultural and time-zone gaps, security and intellectual property exposure, hidden costs, and dependence on the vendor.

## Sourcing Locations

- **Onshore:** the vendor is in the same country.
- **Nearshore:** a nearby country with a similar time zone.
- **Offshore:** a distant country, often with lower cost and a large time difference.

Each brings trade-offs in cost, overlap of working hours, language, law, and data protection.

## Contract Models

The central commercial question is: **who bears the risk of the unknown?** Software work is uncertain, so the type of contract matters greatly.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Model</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How payment works</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Who bears the risk</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weaknesses</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Suits</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed price</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An agreed total for a defined scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vendor bears cost overrun; client bears the risk of wrong scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predictable budget</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs detailed up-front requirements; changes are expensive and contentious; vendors may cut quality or pad the price</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Well-understood, stable scope</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time and materials</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Payment for hours worked at agreed rates, perhaps with a cap</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client bears cost overrun</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flexible; supports changing requirements and agile work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less budget certainty; weak incentive for efficiency; needs trust and oversight</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uncertain or evolving scope</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed price per iteration or capped T&amp;M</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed budget per period with flexible scope inside it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combines predictability with flexibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs a good working relationship</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agile engagements</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dedicated team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client pays for a team for a period, which works as an extension of its own</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Client</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuity; deep knowledge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost whether or not work is busy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long-term product work</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Outcome or value based</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Payment tied to results or benefits delivered</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aligns incentives</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to measure and attribute</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mature relationships</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Subscription or licence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recurring fee for use of a product or service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vendor bears development risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predictable running costs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Price changes; lock-in</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Packaged and cloud software</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Revenue share or gain share</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vendor paid from benefits earned</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vendor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low entry cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complex to define and audit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strategic partnerships</td>
    </tr>
  </tbody>
</table>

### Fixed Price and Agile

Fixed-price contracts assume that the scope is known in advance. Agile methods assume that scope evolves. Combining them calls for care: fix the **time and budget** and let the scope vary within agreed goals; allow the client to **stop** after any iteration; use **target prices** with shared savings; or begin with a small paid **discovery phase** and then choose the contract type with better information.

## Key Contract Elements

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scope and deliverables</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is to be delivered, in what form, and what is excluded</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Acceptance criteria and process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How the client decides that work is accepted, and the time allowed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Price, payment schedule, and expenses</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When and how money is paid, tied to milestones or acceptance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How changes to scope are requested, priced, and approved</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Timeline and milestones</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dates and consequences of delay</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Roles and governance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Named contacts, meetings, escalation steps, and decision rights</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Intellectual property</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who owns the code and designs, and what rights the other party has, including pre-existing components (see Unit 14)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confidentiality and data protection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protection of secrets and personal data; where data may be stored; responsibilities under laws such as GDPR</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security obligations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Standards, audits, incident notification</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality standards and warranties</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defects to be fixed free of charge for a period</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Liability and indemnity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limits on damages; who pays if the work of the vendor infringes the rights of a third party</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Service levels and penalties or credits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measured performance and consequences</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Personnel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Key people, replacement rules, non-solicitation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Termination and exit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conditions for ending the contract; handover of code, documentation, and data; transition assistance</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Escrow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Source code deposited with a neutral party and released if the vendor fails</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dispute resolution and governing law</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How conflicts are resolved and which jurisdiction applies</td>
    </tr>
  </tbody>
</table>

Lawyers draft contracts, but engineers must supply precise technical content: acceptance criteria, performance targets, and the exit arrangements that make a contract workable in practice.

## Service Level Agreements

A **service level agreement (SLA)** is a commitment about the quality of an ongoing service, expressed in measurable terms.

- **Service level indicators (SLIs)** are the metrics: availability, response time, error rate, support response time.
- **Service level objectives (SLOs)** are the targets for them: for example, availability of at least 99.9 per cent per month.
- **The SLA** is the contract that states the targets and the **remedies** if they are missed, such as service credits.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Availability</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Allowed downtime per year (approximate)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99% ("two nines")</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">About 3.7 days</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99.9% ("three nines")</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">About 8.8 hours</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99.99% ("four nines")</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">About 53 minutes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99.999% ("five nines")</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">About 5 minutes</td>
    </tr>
  </tbody>
</table>

Good SLAs measure what users experience, define **how** and **by whom** measurement is made, exclude only **planned maintenance** that is notified in advance, and set remedies that are meaningful. A credit of a few per cent of a monthly fee rarely compensates for a serious outage. Remember too that the SLA of the vendor covers the component of the vendor; your own availability is the combination of all the services you depend on. Three services at 99.9 per cent each give about 99.7 per cent together. The reliability topics of Unit 11 explain why.

Related terms are **operational level agreements** (between internal teams), **recovery time objective (RTO)** and **recovery point objective (RPO)** for disasters, and **support tiers** that define response times by severity.

## Selecting a Vendor

1. **Define the need:** requirements, constraints, and success criteria.
2. **Issue a request for information, proposal, or quotation** (RFI, RFP, RFQ) to candidate vendors, with a clear description of needs and evaluation criteria.
3. **Evaluate against agreed criteria:** capability and experience; fit with requirements; price and total cost; technical quality; security and compliance; financial stability; references from other customers; culture and communication; support; exit terms.
4. **Test:** a demonstration, proof of concept, or small paid pilot reveals more than a presentation.
5. **Check due diligence:** security certifications, audit reports, data handling, and legal standing.
6. **Negotiate** with attention to terms beyond price.
7. **Decide and document** the reasons.

Avoid choosing solely on the lowest price: a cheap bid that omits work, or is intentionally low to win and recover through change requests, often costs more.

## Managing Vendors Day to Day

- **Treat the vendor as part of the delivery system.** Share context, goals, and priorities; partners cannot build the right thing if they only see tasks.
- **Define clear interfaces and responsibilities.** Ambiguity at the boundary is where defects and disputes occur.
- **Integrate processes:** common tools, shared boards, shared definitions of done, joint ceremonies, and access to repositories and environments.
- **Insist on frequent delivery and visibility,** with demonstrations, working builds, and metrics, rather than a single handover at the end.
- **Keep technical oversight in-house:** review the architecture, code quality, and security. Without an internal person who understands the work, the client cannot judge it.
- **Retain knowledge:** documentation, shared repositories, and involvement of internal staff to avoid dependence.
- **Review performance regularly** against SLAs and goals, and address problems early.
- **Build a relationship** with trust and fairness, since neither side benefits from an adversarial one.
- **Plan for the transition,** both at the beginning and for the end of the contract.

## Third-Party and Supply Chain Risk

Dependence on outsiders extends beyond contracted vendors to every library, framework, platform, and service in the product.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Risk</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Mitigation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vendor failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The supplier goes out of business, is acquired, or discontinues the product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Financial checks; escrow; exit plan; avoid sole dependence on small suppliers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lock-in</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Switching becomes very costly because of proprietary features or data formats</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use open standards and portable data; abstraction layers; keep exports</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Service outage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The vendor service fails</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">SLAs; redundancy; graceful degradation; fallback options</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security breach at the vendor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data or credentials exposed through the supplier</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security assessment; least privilege; encryption; incident clauses</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compliance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data stored or processed in ways that break regulations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data location and processing terms; audits</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor workmanship or hidden defects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Acceptance testing; code review; warranties</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knowledge loss</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only the vendor understands the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation; handover; shared teams</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost escalation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Price rises, usage charges, or change fees</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Price caps; monitoring of usage; alternatives</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Intellectual property disputes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unclear ownership or infringing components</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear terms; licence checks; indemnity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vulnerable dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Open-source libraries with flaws or malicious updates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inventory (software bill of materials); scanning; pinned versions; trusted sources</td>
    </tr>
  </tbody>
</table>

An **exit strategy** should exist for every important dependency: how would we leave, how long would it take, and what would it cost?

<!--
IMAGE PROMPT  ->  generate as images/09_contract_types_and_risk_sharing.png   (16:9 explanatory diagram, place here)

A horizontal spectrum from Fixed Price (risk on vendor, scope fixed) through Capped T&M to Time and Materials (risk on client, scope flexible), with a balance indicator for each. Below it, a downtime gauge with nines of availability.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose and Govern

1. A client with unclear requirements wants a fixed-price contract for a new product. What problem is likely, and what alternatives exist?
2. A service promises 99.9 per cent availability. Roughly how much downtime per year does that allow?
3. Name two actions that reduce the risk of lock-in to a vendor.

For case 1, with unclear scope a fixed price leads to disputes over every change, or low quality as the vendor cuts corners; consider time and materials with a cap, fixed price per iteration, or a paid discovery phase first. For case 2, about 8.8 hours. For case 3, use open standards and portable data formats, keep regular exports of data, and isolate the vendor behind an abstraction layer.

## Conclusion

Outsourcing is the use of an external organisation to perform work or provide services that could otherwise be done in-house, and vendor management is the practice of selecting, contracting with, monitoring, and governing those external suppliers to ensure that they deliver the agreed value and that the resulting risks are controlled. Matching the contract to the uncertainty of the work, measuring services with clear SLAs, and planning the exit from the start keep dependence on outsiders under control.

All these activities exist to deliver something worthwhile. The final topic of this unit steps back from projects to ask what value is, and how product thinking keeps teams pointed at it.
