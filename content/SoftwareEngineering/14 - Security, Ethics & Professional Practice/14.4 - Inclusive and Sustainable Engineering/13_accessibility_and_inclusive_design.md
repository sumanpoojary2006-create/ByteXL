## Introduction

People use software in very different ways. Some cannot see a screen, some cannot use a mouse, some cannot hear audio, some read slowly or with difficulty, some are using a phone in bright sunlight with one hand, and some are learning the language of the interface. Software designed only for the imagined average user excludes everyone who differs from it. Accessibility is the practice of making software usable by people with the widest possible range of abilities and circumstances, and inclusive design is the broader habit of recognising diversity from the beginning so that fewer people need special accommodation.

This topic explains who benefits from accessibility, the principles and standards that define it, the assistive technologies people use, the main design and engineering practices, how to test, and why the work is both an ethical and a legal responsibility.

**Definition:** Accessibility is the quality of software that allows people with a wide range of abilities, disabilities, and circumstances to perceive, understand, navigate, and interact with it effectively, and inclusive design is the practice of designing products by understanding and accommodating the diversity of the people who will use them.

<!--
IMAGE PROMPT  ->  generate as images/13_intro_accessibility_and_inclusive_design.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Four user silhouettes in a row, each using the same app screen in a different way: with a screen reader, with a keyboard only, with large text, and with captions; beneath them a single screen with a ring of check marks.

ON-IMAGE TEXT: show a short bold title "Accessibility and Inclusive Design" plus only these few labels, large and legible: One Product, Many Ways. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Who Benefits

The World Health Organization estimates that around 1.3 billion people, about one in six worldwide, live with a significant disability. The numbers grow with age. Disabilities are not only permanent.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Same barrier faced by</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Permanent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Blindness, deafness, limited limb mobility, cognitive disability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People with these conditions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Temporary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A broken arm, an eye infection, a concussion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anyone for a time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Situational</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Glare on a screen, a noisy room, holding a baby, a slow connection, a first language other than the interface language</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everyone, at some moment</td>
    </tr>
  </tbody>
</table>

The three rows are the central insight of inclusive design, popularised in the Microsoft Inclusive Design toolkit: **a barrier for some is an inconvenience for many.** Captions help the deaf, people in noisy stations, and those learning a language. Keyboard access helps people with motor impairments and power users. Good contrast helps people with low vision and anyone outdoors. Designs that work for people at the margins tend to work better for all (the **curb-cut effect:** ramps built for wheelchairs are used by people with prams, bicycles, and luggage).

### Categories of Need

- **Visual:** blindness, low vision, colour-vision deficiency (about 8 per cent of men have some form).
- **Auditory:** deafness and hearing loss.
- **Motor and physical:** limited dexterity, tremor, paralysis, use of one hand, inability to use a pointing device.
- **Cognitive and neurological:** dyslexia, attention difficulties, memory difficulties, autism, anxiety, learning disabilities; also fatigue and stress.
- **Speech:** difficulty speaking or being understood.
- **Seizure and vestibular sensitivity:** flashing content and motion can cause harm.
- **Age, language, and context:** older adults, children, low literacy, unfamiliar language, low bandwidth, old devices.

## Assistive Technology

People use tools that adapt the interface to their needs, and software must work with them.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technology</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Used by</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it works</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Screen readers (NVDA, JAWS, VoiceOver, TalkBack, Narrator)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Blind and low-vision users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read out the content and controls as speech or braille, relying on the structure and labels the software exposes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Screen magnifiers and zoom</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low-vision users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Enlarge the screen or the text</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Voice control and dictation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People with motor impairments, and many others</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operate controls by speaking their names</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Switch devices, eye trackers, head pointers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People with severe motor impairments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operate with very limited input, often one switch scanning through options</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keyboard-only operation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move through everything with the keyboard</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Captions and transcripts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deaf and hard-of-hearing users, and others</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provide text equivalents of speech and sound</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Braille displays</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deafblind and blind users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Raise pins to form braille from screen text</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High-contrast and reduced-motion modes, text-size settings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operating-system settings that applications should respect</td>
    </tr>
  </tbody>
</table>

The vital point for engineers is that assistive technologies rely on the **accessibility information** that applications expose: names, roles (button, link, heading), states (selected, expanded), and relationships. Where an interface is built from generic parts that carry no such information, assistive tools have nothing to work with.

## Standards: WCAG

The **Web Content Accessibility Guidelines (WCAG)** from the World Wide Web Consortium (W3C) are the international reference. Versions 2.0 (2008), 2.1 (2018), and 2.2 (2023) are cumulative. They are organised around four principles, abbreviated **POUR.**

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples of requirements</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Perceivable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Information must be presentable in ways users can perceive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text alternatives for images; captions for video; sufficient colour contrast; content that can be resized; not relying on colour alone</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interface components and navigation must be operable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything usable by keyboard; enough time; no content that flashes dangerously; clear focus; skip links; target sizes large enough to hit; alternatives to complex gestures</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understandable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Information and operation must be understandable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Readable language; predictable behaviour; clear labels and instructions; helpful error messages that suggest corrections; consistent navigation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Robust</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Content must be robust enough to be interpreted by many tools, including future ones</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Correct use of standard elements and roles, so assistive technologies can interpret the page</td>
    </tr>
  </tbody>
</table>

Each guideline has testable **success criteria** at three **levels of conformance:** A (minimum), AA (the usual target, and the level required by most laws), and AAA (highest, not always achievable for all content). A typical criterion is a minimum contrast ratio of 4.5 to 1 between normal-sized text and its background.

Mobile apps, desktop software, documents, and games have their own platform guidelines and are covered by the same principles; WCAG is applied to them by analogy, and standards such as EN 301 549 in Europe cover ICT broadly.

### Law

Accessibility is increasingly a legal requirement. Examples include the Americans with Disabilities Act and Section 508 in the United States, the Equality Act in the United Kingdom, the European Accessibility Act (applying to many products and services in the EU from 2025), and laws in Canada, Australia, India, and elsewhere. Organisations have faced lawsuits and regulatory action for inaccessible websites and apps, and public-sector procurement commonly requires conformance. The ethical codes (previous topic) also require fairness and avoiding exclusion.

## Practices for Design

- **Do not rely on colour alone.** Use text, icons, or patterns in addition (an error shown only in red is invisible to some).
- **Provide sufficient contrast** between text and background, and for interface elements.
- **Support text enlargement and flexible layouts,** so that users can scale text and zoom without losing content or function.
- **Use clear structure:** headings that form an outline, lists, consistent layout, short paragraphs, and plain language.
- **Make targets large enough** and spaced to be hit by imprecise pointing, including touch.
- **Give clear, visible focus** so keyboard users know where they are.
- **Design forms carefully:** visible labels, instructions, grouping, error messages that identify the field and say how to fix it, no time limits that cannot be extended.
- **Avoid content that flashes** more than a few times per second, and respect the reduced-motion setting.
- **Provide alternatives:** text for images and audio, captions and transcripts for video, descriptions for complex graphics.
- **Do not depend on a single sense or ability:** provide more than one way to do each task (for example, an alternative to a drag-and-drop operation).
- **Keep interaction predictable** and forgiving: confirm destructive actions, allow undo.
- **Reduce cognitive load:** one main action per screen where possible, familiar patterns, no unnecessary memory demands, avoid timeouts.
- **Consider language and culture:** support translation, right-to-left scripts, and avoid idioms and culturally specific images that mislead.
- **Consider performance and connectivity:** lightweight pages serve people on slow connections and old devices.
- **Design with people, not for them:** involve disabled users throughout the process.

## Practices for Engineering

The engineer's main task is to expose correct information to assistive technology and to make everything operable without a mouse.

- **Use the standard, native interface elements** of the platform for buttons, links, inputs, and headings. They bring correct roles, keyboard behaviour, and accessibility information for free. Building custom controls from generic parts is the leading cause of inaccessible interfaces, since every missing behaviour must then be recreated by hand.
- **Provide names and descriptions** for every control and image, in text that makes sense out of context ("Add to order", not "click here").
- **Mark up structure meaningfully:** headings in order, landmarks for main regions, lists, tables with header cells.
- **Manage focus:** keep a logical order; move focus appropriately when dialogs open and close or content changes; never trap it.
- **Announce dynamic changes** (new messages, errors, loading) to assistive technologies, using the platform's mechanisms for live updates.
- **Use the specialised accessibility attributes** (such as WAI-ARIA on the web) only when native elements cannot do the job; the first rule of ARIA is not to use it if a native element will do, and wrong use is worse than none.
- **Use the platform accessibility APIs** and guidelines on mobile (labels, traits, hints, dynamic text sizes).
- **Honour system settings:** text size, contrast, reduced motion, dark mode, captions.
- **Provide accessible media:** captions, transcripts, audio descriptions.
- **Make documents accessible:** structure, alternative text, tagged files for PDF.
- **Build components once, accessibly,** in a shared design system, so every team inherits accessibility.

## Testing for Accessibility

No single method suffices.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Method</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it finds</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limits</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automated checkers and linters</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing labels, contrast failures, invalid structure; can run in the editor and the pipeline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only a minority of issues (often estimated at around a third) can be detected automatically</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keyboard-only test</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing focus, traps, unreachable controls</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs a person</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Screen reader test</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Meaningless or missing names, wrong order, silent updates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs skill; test with more than one reader and platform</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Zoom, text size, and reflow checks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clipping and overlap</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Manual</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contrast and colour-blindness simulation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Colour dependence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simulation only approximates real experience</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expert audit against WCAG</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Systematic coverage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost; a snapshot</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing with disabled users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Real barriers and priorities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs planning and respect; the most valuable</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Content review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plain language, headings, link text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Editorial effort</td>
    </tr>
  </tbody>
</table>

Integrate accessibility into the definition of done (Unit 2), include accessibility criteria in user stories, add automated checks to continuous integration (Unit 9), and treat accessibility defects like any other defect (Unit 10). Publish an **accessibility statement** that says what is supported, known gaps, and how to give feedback, and respond to the feedback. Retrofitting accessibility is much more expensive than building it in.

## Inclusive Design Beyond Disability

Inclusion extends to age, gender, culture, language, income, and technical skill.

- **Personas and testing** should include people unlike the team.
- **Names, forms, and data fields** should not assume one cultural pattern (single family-name structures, binary gender options where not needed, a postal code format, a phone number format).
- **Imagery and language** should avoid stereotypes and exclusion; use inclusive terms in code and documentation as well (for instance "allow list" and "main branch").
- **Digital literacy and cost:** support low-end devices, limited data plans, and older software.
- **Diverse teams** see more problems; inclusion in hiring and working practices improves products.
- **Safety:** consider how design features could be used to harass or control others, and add protections.

## Business and Ethical Case

Accessibility widens the market, improves usability and search visibility, reduces legal risk, and often improves overall quality. But the first reason is simpler: excluding people from services such as banking, education, work, and public information is unfair, and engineers are the ones in a position to prevent it.

<!--
IMAGE PROMPT  ->  generate as images/13_pour_principles_and_assistive_technology.png   (16:9 explanatory diagram, place here)

Left: four tiles P, O, U, R with a one-word caption each. Right: a layered diagram: app interface at the top, an accessibility information layer (names, roles, states) in the middle, and three assistive technology icons (screen reader, switch, voice control) at the bottom connected through the layer, with a red broken link where a custom control exposes no information.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Spot the Barrier

1. An error message on a form is shown only by turning the field border red. Who is affected, and what is the fix?
2. A team builds a custom drop-down menu from generic page elements, and keyboard users cannot open it. What is the underlying lesson?
3. An automated tool reports no accessibility errors. Is the product accessible?

For case 1, people with colour-vision deficiency, screen reader users, and others; add text that states the error and identifies the field, and link it to the field. For case 2, use native elements wherever possible; when building a custom control, every behaviour and every piece of accessibility information must be supplied. For case 3, not necessarily: automated tools detect only a portion of the issues; manual keyboard and screen reader tests and testing with disabled users are needed.

## Conclusion

Accessibility is the quality of software that allows people with a wide range of abilities, disabilities, and circumstances to perceive, understand, navigate, and interact with it effectively, and inclusive design is the practice of designing products by understanding and accommodating the diversity of the people who will use them. Following WCAG, using standard elements, testing with real assistive technology, and involving disabled people make software usable by those it would otherwise exclude.

Inclusion looks at who software serves today. Sustainability looks at what it costs the planet, and the next topic covers sustainable and green software.
