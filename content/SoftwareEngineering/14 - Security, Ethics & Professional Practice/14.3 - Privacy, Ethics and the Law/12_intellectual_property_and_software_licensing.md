## Introduction

Software is created by people and organisations who invest time and money in it, and it is used, copied, modified, and combined at almost no cost. The law of intellectual property decides who owns what, what others may do with it, and under what conditions. Engineers meet these rules every day without noticing: every library added to a project comes with a licence, every employment contract says something about who owns the code written, and every contribution to an open-source project is made under terms. Ignoring them can lead to legal disputes, forced removal of products, or the loss of the right to sell what has been built.

This topic explains the main forms of intellectual property, how copyright applies to software, the landscape of open-source and proprietary licences, the difference between permissive and copyleft licences, patents and other rights, and the practice of licence compliance. It gives general understanding, not legal advice; real decisions should involve qualified lawyers.

**Definition:** Intellectual property is the body of legal rights over creations of the mind, including software, which allow owners to control copying and use; a software licence is the permission, with conditions, by which an owner allows others to use, modify, or distribute a work.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_intellectual_property_and_software_licensing.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a document-shaped licence card with a small set of tick and condition icons. Centre: a spectrum bar from Proprietary through Permissive to Copyleft. Right: package boxes combined into a product box with a licence checklist.

ON-IMAGE TEXT: show a short bold title "Intellectual Property and Software Licensing" plus only these few labels, large and legible: Own, License, Comply. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Forms of Intellectual Property

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Right</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Protects</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How obtained</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Duration (typical)</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Relevance to software</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copyright</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Original expression fixed in a tangible form: source code, object code, documentation, designs, images</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automatic on creation in most countries under international agreements such as the Berne Convention; no registration needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many decades, often the life of the author plus seventy years, or ninety-five years from publication for company works</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Primary protection for code. Protects the expression, not the underlying idea</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inventions that are new, non-obvious, and useful: processes, machines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Application, examination, and grant by a patent office</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">About 20 years</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software patents are allowed in some countries (with limits) and restricted in others; can cover algorithms and methods, and may block use even of independently written code</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trade secret</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confidential information that gives a business advantage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Kept secret by reasonable measures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">As long as secrecy is kept</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Source code, algorithms, data sets, and designs kept confidential</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trademark</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Names, logos, and signs that identify the source of goods or services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use and often registration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Renewable indefinitely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product names and logos, even of open-source projects; licence may not grant trademark rights</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design rights</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Appearance of products and interfaces</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Registration or creation, depending on country</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Years to decades</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Some interface designs</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Database rights</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Substantial investment in a database (in the EU)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automatic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">15 years renewable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Collections of data</td>
    </tr>
  </tbody>
</table>

### Copyright in Software

- **Automatic and default restrictive.** Code that is published without a licence is not free to use: the default is "all rights reserved", so others may not copy, modify, or distribute it. Posting code on a public site is not the same as licensing it.
- **Rights of the owner** include copying, adapting, distributing, and making available to the public. A licence grants some of them.
- **Idea versus expression.** Copyright does not protect ideas, methods of operation, or the functionality, only the specific code and text. Different code that does the same thing is allowed, but copying the code is not. Courts have considered how far interfaces (APIs) are protected; in a long dispute about the Java interfaces used in Android, a US Supreme Court ruling in 2021 found the copying to be fair use on the facts, without settling broader questions.
- **Derivative works.** Modified or combined versions are derivative works, which require permission from the owner of the original.
- **Fair use / fair dealing** exceptions exist in some countries for limited purposes such as criticism, research, and teaching, and are narrow and fact-dependent.
- **Moral rights** (attribution) apply in many jurisdictions.

### Who Owns the Code?

- **Employees:** in most countries, work created by an employee in the course of employment belongs to the employer, often by law and by the employment contract. Contracts may also claim work done outside hours if related to the business. Read what you sign.
- **Contractors and freelancers:** by default they often own what they create unless the contract assigns it to the client in writing. Clients should obtain an **assignment** or a clear licence.
- **Students and universities:** policies vary; check them.
- **Joint authorship:** several authors share ownership, which complicates later licensing.
- **Open-source contributions:** contributors keep their copyright unless they sign it over, and agree to the project's terms through a **contributor licence agreement (CLA)** or a lighter **developer certificate of origin (DCO)** sign-off.
- **Generated code:** the position on ownership and on the licence status of output from AI code assistants and on the code used to train them is unsettled and varies by jurisdiction (see the topic on AI-assisted development).

## Software Licences

A licence is a legal document that states what recipients may do and what they must do. Software falls broadly into the following groups.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Proprietary (closed source)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The owner keeps the source private and permits use only on specified terms, usually for a fee, with limits on copying, reverse engineering, and redistribution (End-User Licence Agreement)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commercial applications, many operating systems</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Freeware and shareware</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Free of charge, or free to try, but still proprietary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Free utilities with restrictions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Open source</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The source is available and the licence allows anyone to use, study, modify, and share it, according to the Open Source Definition of the Open Source Initiative</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Linux, Python, many libraries</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Free software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The movement led by Richard Stallman and the Free Software Foundation, stressing four freedoms: to run, study and change, redistribute, and distribute changed versions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">GNU tools</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Source-available</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The source can be read but the licence limits use, for instance forbidding competing commercial services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Several newer licences used by companies</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Public domain / dedication</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The author gives up rights as far as the law allows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dedications such as CC0</td>
    </tr>
  </tbody>
</table>

### Permissive and Copyleft Open-Source Licences

The most important division among open-source licences is whether they require derivative works to remain open.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Family</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Obligations on recipients</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Effect on products</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Permissive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do almost anything, including using it in closed products</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the copyright notice and licence text; some require a notice of changes and, in some, an explicit patent grant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MIT, BSD (2-clause, 3-clause), Apache 2.0, ISC</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy to combine with proprietary software; widely used by companies</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak copyleft</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes to the licensed files must be shared under the same licence, but larger works that merely use or link to them may stay under other terms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Share modifications to the covered files or library</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mozilla Public License 2.0 (file level), GNU LGPL (library level), Eclipse Public License</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be used in proprietary products with care about how they are combined and modified</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong copyleft</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Derivative works that are distributed must be licensed under the same terms, with source made available</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provide source of the combined work to recipients, under the same licence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">GNU General Public License (GPL v2, 1991; v3, 2007)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A proprietary product that incorporates and distributes GPL code generally must be released under the GPL too</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Network copyleft</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extends the requirement to software offered over a network, since users do not receive a copy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provide source to users of the network service</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">GNU Affero GPL (AGPL)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Companies running modified versions as online services must publish their changes; many avoid it</td>
    </tr>
  </tbody>
</table>

### MIT, Apache 2.0, and GPL Compared

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">MIT</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Apache 2.0</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">GPL v3</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Length and complexity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very short</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Longer, more precise</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commercial use and closed-source products</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allowed, but distributed derivative works must also be GPL</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modification and distribution</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allowed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allowed, with notice of changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allowed, under the same licence</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patent grant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not explicit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explicit grant from contributors, with termination if the user sues over patents</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explicit grant and protections</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Notice of copyright required</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, plus licence copy and notices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Share source of changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, when distributing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trademark</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not granted</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explicitly not granted</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not granted</td>
    </tr>
  </tbody>
</table>

Other points: GPL v2 and v3 are not fully compatible with each other, and some licences cannot be combined in a single product because their conditions conflict (**licence compatibility**). The Linux kernel uses GPL v2. Documentation, images, and data are often under **Creative Commons** licences (such as CC BY, which requires attribution, and CC BY-SA, which adds share-alike), which are designed for creative works and not recommended for software code.

### What "Linking" and "Distribution" Mean

Copyleft conditions typically apply when software is **distributed** (given to others), not merely used internally. Whether combining a GPL library with another program creates a single derivative work depends on how they are combined (statically or dynamically linked, in one process or separate programs communicating through standard interfaces) and on legal interpretation, which differs and is contested. Software-as-a-service blurs the distribution boundary, which is why network copyleft licences exist. These are matters for legal advice.

## Patents and Software

A patent gives the holder the right to stop others from making or using the invention, even if they developed it independently. In software, patents on algorithms and business methods are controversial: supporters argue they reward innovation; critics point to vague claims, patent trolls (companies that exist to assert patents), and costly litigation that slows small developers. Practices include:

- awareness of patents in your field and in the licences you accept (the patent grant in Apache 2.0 is a reason for its popularity);
- defensive patent pools and pledges;
- keeping records of prior work;
- consulting specialists before shipping something novel in a crowded field.

## Practical Licence Compliance

### For Teams Using Open-Source Components

1. **Track every component** and its licence, direct and transitive, in the software bill of materials (topic 7). Use SPDX identifiers (standard short names such as MIT or Apache-2.0) to describe them consistently.
2. **Set a policy** on which licences are allowed freely, which need review, and which are prohibited for the kind of product you build.
3. **Check before you add:** a new dependency is a legal decision as well as a technical one.
4. **Automate scanning** of dependencies and containers for licences in the pipeline; review the findings.
5. **Meet the obligations:** include required notices and licence texts, usually in a documentation or acknowledgements file; make source available when required; keep changes to copyleft components properly published.
6. **Do not copy code from the web, forums, or other projects** without checking its licence. Code snippets on question-and-answer sites usually carry their own terms.
7. **Keep records** of decisions, to answer customers' due-diligence questions and to prepare for company acquisitions, where licence audits are standard.
8. **Respond quickly** to non-compliance: remove the component, replace it, comply, or obtain a commercial licence. Many projects offer **dual licensing:** a free licence (often copyleft) and a paid commercial one.

### For Publishing Your Own Work

- **Choose a licence deliberately and include it** (a LICENSE file at the top of the project); no licence means no permission.
- Consider your goals: wide adoption suggests permissive; keeping improvements open suggests copyleft; protecting against cloud providers might suggest network copyleft or source-available terms.
- Ensure you hold the right to license it (your employer may own it).
- State how to contribute and what terms apply to contributions.
- Respect trademarks: forks cannot use the original name without permission.

### In Employment and Contracts

- Understand **assignment clauses**, **non-compete** and **confidentiality** agreements.
- Do not bring a former employer's code or trade secrets to a new job.
- Seek approval before contributing to open source on company time or using company resources.
- Keep personal projects clearly separate where contracts require it.

### Also Remember

- **Third-party content** in products: fonts, images, icons, music, and data sets have licences too.
- **Export controls** restrict some encryption software and technology across borders.
- **Terms of service** of APIs and data sources limit permitted use, such as storing, redistributing, or training models on the data.
- **Attribution and honesty** are ethical requirements, not only legal ones (previous topic).

<!--
IMAGE PROMPT  ->  generate as images/12_licence_spectrum_and_compliance.png   (16:9 explanatory diagram, place here)

A horizontal spectrum with five markers: Proprietary, Source-available, Permissive (MIT, Apache), Weak copyleft (LGPL, MPL), Strong copyleft (GPL, AGPL), with a bar underneath showing "freedom to close your own product" decreasing and "obligation to share" increasing. Below, a four-step compliance cycle: Inventory, Check policy, Meet obligations, Record.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Mind the Terms

1. A developer finds a useful code library on a public site with no licence file and copies it into a commercial product. Why is this a problem?
2. A company wants to build a closed-source product and is considering two libraries, one under MIT and one under GPL. What should it consider?
3. Who normally owns software written by an employee as part of their job?

For case 1, with no licence, the default is that all rights are reserved, so there is no permission to copy or use it; ask the author for a licence or choose another library. For case 2, MIT places only light conditions (keep the notice), whereas distributing a product that incorporates GPL code generally requires releasing the combined work under the GPL; obtain legal advice before using the GPL library. For case 3, normally the employer, under law and the contract, but this depends on jurisdiction and the contract terms.

## Conclusion

Intellectual property is the body of legal rights over creations of the mind, including software, which allow owners to control copying and use; a software licence is the permission, with conditions, by which an owner allows others to use, modify, or distribute a work. Knowing who owns what, reading the licences of what you use, and recording your obligations protect both your employer and the community on whose work most software rests.

Rights and obligations concern not only owners but also the people who use software. The next chapter considers designing for everyone, beginning with accessibility and inclusive design.
