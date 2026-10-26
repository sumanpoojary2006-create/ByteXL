## Introduction

Agile teams still need to know what to build. Instead of a long specification written at the start, they keep a living, ordered list of needs, the product backlog, and describe each need briefly as a user story. The detail is worked out through conversation when the work is about to start, close to the time it is needed and when the most is known.

**Definition:** A user story is a short description of a need from the point of view of the person who wants it, written with acceptance criteria, and the product backlog is the single, ordered list of such items that the team works from and that is continually refined as understanding grows.

<!--
IMAGE PROMPT  ->  generate as images/17_intro_user_stories_and_the_product_backlog.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A vertical ordered list of cards, the top ones detailed and small, the lower ones large and vague, with a Product Owner figure reordering them and an arrow pointing to the top labelled Next sprint.

ON-IMAGE TEXT: show a short bold title "User Stories and the Product Backlog" plus only these few labels, large and legible: Story, Priority, Refine. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Anatomy of a User Story

A common template is:

**As a** (type of user), **I want** (some capability), **so that** (benefit).

The "so that" is important: it records the reason, which lets the team find a better solution if the obvious one is costly. A story is deliberately incomplete. It is a promise of a conversation, not a specification. A well-known description, attributed to Ron Jeffries, calls it three Cs:

- **Card:** the short written statement
- **Conversation:** discussion between team and customer to explore details
- **Confirmation:** the acceptance criteria that confirm the story is done

## Acceptance Criteria

Acceptance criteria state, in concrete terms, how anyone will know that a story is complete. A frequent format is **Given, When, Then**: given some starting situation, when an action occurs, then a specific result is expected. For a story about rating a meal, a criterion might say: given that a user has already rated a meal, when they try to rate it again, then the system refuses and explains why. Good criteria are specific, testable, and agreed before work begins.

## What Makes a Good Story: INVEST

Bill Wake proposed a checklist for judging stories.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Letter</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quality</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">I</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Independent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be built and delivered without depending on a specific other story</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">N</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Negotiable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The details can be discussed; it is not a contract</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">V</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Valuable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivers something that matters to a user or the business</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">E</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understood well enough to estimate</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">S</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fits comfortably in one sprint</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">T</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">There is a clear way to tell if it is done</td>
    </tr>
  </tbody>
</table>

## Splitting Large Stories

Large stories, often called **epics**, are too big to deliver in one iteration and must be split. The split should preserve user value: slice vertically so each part delivers something usable end to end, instead of slicing by technical layer, which delivers nothing until all layers exist. Useful ways to split include by workflow step, by user type, by simple case before complex cases, by data variation, and by quality level, delivering a basic version first and improving it later.

## The Product Backlog

The product backlog is a single, ordered list of everything that might be needed in the product. It contains stories, defects, technical work, and research. It has important characteristics.

- **Ordered**, not just listed: the most valuable and urgent items are at the top.
- **Emergent**: it is never finished and changes as the product and market change.
- **Detailed appropriately**: items near the top are small and clear, items far down can be large and vague (sometimes described as a pile that is detailed only as it nears the top).
- **Owned** by the Product Owner, though many people contribute.

## Backlog Refinement

**Refinement** is the ongoing activity of keeping the backlog healthy: adding detail, splitting large items, estimating, removing items that are no longer relevant, and reordering as priorities shift. It prevents sprint planning from being a surprise discovery of what the work actually is.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Value versus effort ordering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Favour high-value, low-effort items</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MoSCoW (Must, Should, Could, Will not)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Classify items by necessity for a given release</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Story mapping</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Arrange stories along the user journey to see the whole product and plan thin slices</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost of delay</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order by what waiting costs, not just by value</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_backlog_funnel.png   (16:9 explanatory diagram, place here)

A funnel-shaped backlog: at the top, large vague epics; in the middle, medium stories being split; at the bottom, small well-defined stories ready for the sprint, each with acceptance criteria tick marks. A refinement arrow loops between layers.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Improve the Story

1. "The system shall use a relational database." Is this a good user story? Why?
2. Rewrite this as a user story: "Add a search feature."
3. A story reads "Build the whole checkout." What is wrong with it?

Item 1 is a technical statement, not a user story: it names no user and no benefit, and it prescribes a solution. Item 2 could become: "As a student, I want to search the menu by dish name, so that I can quickly find what I like," with criteria such as results showing partial matches. Item 3 is too large to be small or estimable; it should be split into slices such as paying by one method first, then adding others, then handling failed payments.

## Conclusion

A user story is a short description of a need from the point of view of the person who wants it, written with acceptance criteria, and the product backlog is the single, ordered list of such items that the team works from and that is continually refined as understanding grows. Stories invite conversation instead of replacing it.

Once stories exist, teams need to judge how big they are. The next topic explains how agile teams estimate.
