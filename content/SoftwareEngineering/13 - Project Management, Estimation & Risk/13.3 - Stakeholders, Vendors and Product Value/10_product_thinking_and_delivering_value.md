## Introduction

A project can be completed on time, within budget, and to specification, and still deliver nothing of value if the thing built does not solve a real problem for real people. The planning, estimation, and tracking of earlier topics make a team efficient at building; product thinking makes the team effective at building the right thing. It shifts attention from outputs, the features shipped, to outcomes, the changes in the lives of users and the results for the organisation.

This topic distinguishes products from projects, explains product discovery, minimum viable products, outcome-oriented goals and metrics, and ways of prioritising, and closes the unit by showing how product thinking completes project management.

**Definition:** Product thinking is the practice of organising software work around the continuing creation of value for users and for the organisation, by understanding problems, testing assumptions, and measuring the outcomes of what is delivered, rather than treating a fixed list of features as the goal.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_product_thinking_and_delivering_value.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A loop of four stages (Discover, Build, Measure, Learn) around a central product, an arrow leaving the loop labelled Outcomes, and beside it two stacked boxes labelled Output (features shipped) and Outcome (behaviour changed).

ON-IMAGE TEXT: show a short bold title "Product Thinking and Delivering Value" plus only these few labels, large and legible: Outputs vs Outcomes. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Project Thinking and Product Thinking

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Project thinking</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Product thinking</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unit of work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A project with a start and end</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A product that continues and evolves</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Goal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deliver an agreed scope on time and budget</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Create and sustain value for users and the business</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Success measured by</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plan adherence: on time, on budget, in scope</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Outcomes: adoption, satisfaction, results</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assembled for the project and disbanded after</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stable team that owns the product over time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specified in advance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discovered and refined through learning</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Funding</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Per project</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Per product or team, with continuing investment</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">After release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handover to maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continued improvement and learning</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivering late or over budget</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Building something nobody needs</td>
    </tr>
  </tbody>
</table>

Both views are needed. Product thinking decides **what** is worth doing; project management techniques help to deliver it predictably. Where there is a fixed deadline or contract, project discipline wraps around product learning.

## Output, Outcome, and Impact

- **Output:** what the team produces: features, releases, documents.
- **Outcome:** the change in the behaviour of users or in results that follows: more customers complete an order, fewer calls to support.
- **Impact:** the lasting benefit to the organisation or society: revenue, retention, reduced cost, improved health.

The "feature factory" is a team that measures itself by outputs and ships steadily without knowing whether anything improved. A successful team agrees on the **outcome** it seeks and treats features as hypotheses about how to achieve it.

## The Product Manager and the Product Team

The product manager (or product owner in Scrum) is accountable for the **value** of the product. Marty Cagan, a writer on product management, describes the need to address four risks before and during building.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Risk</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Who mainly addresses it</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Will customers choose to use or buy it?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product manager with design</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can users work out how to use it?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Designer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feasibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can we build it with the time, skill, and technology we have?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Engineers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Viability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it work for the business: legal, financial, ethical, strategic?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product manager with stakeholders</td>
    </tr>
  </tbody>
</table>

Engineers are part of the product team and should take an interest in value, not only in delivery. Many of the best product ideas come from engineers who understand what is technically possible.

## Product Discovery

**Discovery** is the work of deciding what to build, as distinct from **delivery,** the work of building it. It reduces the risk of building the wrong thing before substantial effort has been spent.

### Activities

- **Understand users:** interviews, observation of real work, surveys, support tickets, usage data. The aim is to understand the **problem,** the **jobs** people are trying to accomplish, and the obstacles, not to collect feature requests. Users are expert in their problems and not always in solutions.
- **Define the problem clearly:** who has it, how often, how painful, and how it is solved today.
- **Generate options** and ideas with the whole team.
- **Test assumptions** cheaply. Every idea rests on assumptions about desirability, usability, feasibility, and viability; the riskiest are tested first.
- **Prototype:** sketches, clickable mock-ups, and simple working versions put something in front of users before development begins.
- **Experiment:** concierge tests (delivering the service manually), "Wizard of Oz" tests (a human behind a seemingly automated interface), landing pages to gauge interest, and A/B tests.

### Frameworks

- **Design thinking:** empathise, define, ideate, prototype, test.
- **Lean Startup** (Eric Ries): build, measure, learn, with the aim of minimising the time to learn.
- **Jobs to be Done:** frame needs as the progress a person seeks in a situation.
- **Opportunity solution trees** (Teresa Torres): connect a desired outcome to opportunities (user needs) and to candidate solutions and experiments.
- **Dual-track agile:** discovery and delivery proceed in parallel, with discovery ahead of the delivery backlog.

## The Minimum Viable Product

A **minimum viable product (MVP)** is the smallest version of a product that lets a team collect the maximum validated learning about customers with the least effort. The term was popularised by Eric Ries and Frank Robinson.

Common misunderstandings:

- An MVP is **not** a poor-quality or half-built product, and not the first release of a large specification. It must be viable: it must deliver real value for a particular group, even if narrow.
- It is **not a one-off.** It begins a series of learning cycles.
- It is **a means of testing a hypothesis,** such as "small restaurants will pay for online ordering that takes no commission." The MVP is whatever tests this fastest.

### Slicing Value

Rather than building layers (all of the database, then all of the logic, then all of the screens), a team builds **thin vertical slices** that cut through every layer and give a usable result, however small. A diagram widely used to explain this shows a skateboard, a scooter, a bicycle, a motorcycle, and then a car as successive useful vehicles, in contrast with delivering a wheel, an axle, and a chassis that is of no use to anyone until the car is complete.

### Related Practices

- **Release early to a small group** (pilot, beta, or gradual rollout) and learn before wider release.
- **Feature flags** let a feature be turned on for some users only and withdrawn easily.
- **Throw-away prototypes** answer questions, then are discarded rather than hardened into production.

## Goals and Metrics for Outcomes

### Objectives and Key Results

OKRs state an **objective,** an inspiring qualitative goal, and a few **key results,** measurable indicators of progress toward it, focusing on outcomes. For example, the objective "Make ordering effortless" might have key results such as raising the share of visitors who complete an order, and cutting the time taken to place one.

### Product Metrics

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Acquisition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New sign-ups, installs, conversion from visit to account</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is the product attracting people?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Activation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users who complete a first valuable action</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do they reach the first moment of value?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Engagement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Daily or monthly active users, sessions, depth of use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is it used regularly?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retention</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Share of users who return after a week, a month</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it keep delivering value? Often the most important measure</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Satisfaction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Net promoter score, customer satisfaction, ratings, support volume</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How do users feel?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Task success</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Completion rate, time on task, error rate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is it usable?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Revenue</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conversion to paid, average revenue per user, lifetime value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is it viable?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost to acquire or serve a customer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is it sustainable?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical health</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance, availability, defects (Units 10 and 11)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is it reliable enough to deliver value?</td>
    </tr>
  </tbody>
</table>

A widely used view is the **"North Star" metric,** a single measure that best captures the value delivered to customers, supported by input metrics that teams can influence directly.

### Using Evidence Well

- **Define success before building,** so results cannot be reinterpreted afterwards.
- **Use experiments** (A/B tests) to separate real effects from coincidence, with sufficient sample size and time.
- **Combine quantitative data** (what happens) with **qualitative research** (why it happens).
- **Beware of vanity metrics** and of optimising a number at the expense of users. Ethical product practice avoids manipulative design, covered in Unit 14.
- **Respect privacy** in collecting data.
- **Be willing to stop.** Evidence that a feature is not working is a reason to remove it, which also lowers maintenance cost.

## Prioritising

Resources are limited, so choices must be made on a basis other than who shouts loudest.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Value versus effort</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plot items by estimated value and effort; start with high value and low effort</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MoSCoW</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Classify as must have, should have, could have, and will not have this time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">RICE</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Score items by reach, impact, confidence, and effort: reach times impact times confidence, divided by effort</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weighted scoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Score against agreed criteria, each with a weight</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Kano model</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separate basic needs (expected), performance needs (more is better), and delighters (unexpected pleasure)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost of delay</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Estimate the loss incurred for each period an item is not delivered; combined with duration, as in weighted shortest job first</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Story mapping</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Arrange stories along the user journey to see the end-to-end flow and slice releases</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Opportunity scoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compare importance of a need with satisfaction with current solutions</td>
    </tr>
  </tbody>
</table>

Prioritising is also a matter of saying no (topic 8). A short list of things done well beats a long list done thinly. Include **technical work** (reducing debt, improving reliability and security) in the same prioritisation, with its benefits explained in terms of value and risk, not as a special category that is always deferred.

## Delivering Value Continuously

Value arrives only when software is **in use.** Delivery practices from earlier units serve product thinking.

- **Small batches, frequent releases,** from Unit 9, shorten the time to learn.
- **Quality** from Units 10 and 11 keeps users' trust; a feature with defects delivers negative value.
- **Operability:** monitoring and support tell the team what really happens in production.
- **Feedback loops:** analytics, support requests, reviews, and direct conversations with users feed back into discovery.
- **Sustainable pace and healthy code** allow the team to keep delivering for years.

## Common Failures

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Failure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build trap</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measuring success by features shipped, regardless of results</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Set and review outcome goals</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Solution first</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Starting from a favourite technology or a customer request without understanding the problem</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ask why; study the underlying need</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Big-bang launch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Months of building with no feedback, then disappointment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MVPs, pilots, and incremental release</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ignoring users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decisions based on opinion of the loudest internal voice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regular contact with real users</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feature accumulation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Never removing anything; the product becomes complex and costly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retire features with low value</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Metrics theatre</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Collecting data nobody uses to decide</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tie measures to decisions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treating the date as the goal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shipping on time something that does not work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Define success in outcomes, not only dates</td>
    </tr>
  </tbody>
</table>

## Bringing the Unit Together

Project management gives the team the means to **plan** (breakdown and scheduling), **predict** (estimation and cost models), **prepare** (risk management), **organise** (teams), **observe** (tracking), **align** (stakeholders), and **collaborate with others** (vendors). Product thinking asks the question that frames all of these: **is this the right thing to build, and how will we know that it has helped?** A well-managed project that serves no need has failed; a valuable product that is chaotically managed will struggle to reach its users. Good engineers learn both disciplines.

<!--
IMAGE PROMPT  ->  generate as images/10_output_vs_outcome_and_mvp_slicing.png   (16:9 explanatory diagram, place here)

Left: two rows contrasting a wheel then an axle then a chassis then a car (grey, useless until the end) with skateboard then scooter then bicycle then motorcycle then car (green, each usable). Right: a build-measure-learn loop with a metrics panel showing retention rising.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Think Like a Product Team

1. A team ships every feature requested and still sees falling usage. Which trap are they in, and what should they change?
2. Describe an MVP for testing whether independent cafes would use an online ordering tool.
3. Why might an MVP be thought of as a series rather than a single release?

For case 1, the build trap or feature factory; define the desired outcome, measure it, and treat features as hypotheses. For case 2, a simple ordering page and manual handling of orders for a few cafes, to see whether they use it and what they value, before building automation. For case 3, each version tests a hypothesis, and the learning decides what to build or change next.

## Conclusion

Product thinking is the practice of organising software work around the continuing creation of value for users and for the organisation, by understanding problems, testing assumptions, and measuring the outcomes of what is delivered, rather than treating a fixed list of features as the goal. Together with the planning, estimation, risk, team, and stakeholder skills of this unit, it makes it possible not only to deliver software predictably but to deliver software worth having.

This completes the unit on project management, estimation, and risk. The final unit of the course addresses the responsibilities that surround all software work: security, ethics, and professional practice.
