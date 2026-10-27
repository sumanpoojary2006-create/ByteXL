## Introduction

If effort depends on the size of the software and on the conditions under which it is built, then it should be possible to express that dependence as an equation, calibrated from the experience of many past projects. Algorithmic, or parametric, cost models do exactly this: they take a size measure and a set of adjusting factors as input and produce estimates of effort and duration. They add repeatability and a structured way to think about the drivers of cost. They also have significant limits, and they are only as good as the data and judgement behind their inputs.

This topic explains how parametric models work, introduces COCOMO as the best-known example, describes calibration, and discusses where such models help and where they mislead.

**Definition:** An algorithmic cost model is a mathematical formula, derived from analysis of historical project data, that estimates software development effort and duration from a measure of software size and a set of factors describing the product, the platform, the people, and the project.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_algorithmic_cost_models.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A function-machine drawing: inputs Size and a column of adjustment dials (Product, People, Platform, Project) flow into a central box labelled Model, which outputs Effort and Duration; a loop labelled Calibration returns from past project data to the box.

ON-IMAGE TEXT: show a short bold title "Algorithmic Cost Models" plus only these few labels, large and legible: Inputs, Model, Outputs. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Form of Parametric Models

Most models share a common shape.

1. **Effort grows with size,** but not in a straight line. Doubling the size more than doubles the effort, because larger systems require more communication, integration, and management. The relationship is expressed with an exponent greater than one applied to size.
2. **Effort is scaled by a set of factors** (**cost drivers**) that raise or lower it: the capability of the team, the complexity of the product, the required reliability, constraints on time and storage, the tools used, and so on.
3. **Duration** is derived from effort, again through a power relationship with a smaller exponent, reflecting that adding people shortens the schedule only to a limited extent.
4. **Constants** are fixed by calibrating the model against data.

This structure represents the idea of **diseconomies of scale** in software: bigger projects are proportionally less productive.

## COCOMO

The **Constructive Cost Model (COCOMO)** was published by Barry Boehm in 1981 in his book on software engineering economics, based on data from 63 projects. It is the most widely known parametric model and a good vehicle for understanding the family.

### Basic COCOMO (1981)

Basic COCOMO estimates effort from size in thousands of delivered lines of code only, with different constants for three project classes.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Class</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Organic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small teams, familiar problem, flexible requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relaxed constraints</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Semi-detached</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Medium teams, mixed experience, some rigid requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Intermediate</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Embedded</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operating within tight hardware, software, and operational constraints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Highly constrained</td>
    </tr>
  </tbody>
</table>

The more constrained the class, the greater the effort for the same size.

### Intermediate COCOMO

Intermediate COCOMO multiplies the basic result by fifteen **effort multipliers** in four groups.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Group</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples of drivers</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product attributes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Required reliability, size of the database, complexity of the product</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Computer (platform) attributes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Execution time constraints, storage constraints, volatility of the platform, turnaround time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Personnel attributes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analyst capability, programmer capability, applications experience, platform experience, language experience</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Project attributes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use of modern practices, use of software tools, required development schedule</td>
    </tr>
  </tbody>
</table>

Each driver is rated on a scale (very low to extra high), and each rating maps to a multiplier. Personnel factors have among the largest effects, which agrees with common experience that people matter more than tools.

### COCOMO II (2000)

COCOMO II updated the model for modern development, with three sub-models suited to different stages.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Sub-model</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Used when</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Size input</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Application composition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early prototyping with fast tools and reusable components</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Object points or application points</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements are known but architecture is not settled</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Function points converted to size</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Post-architecture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">After the architecture is defined, for detailed estimates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Source lines or function points</td>
    </tr>
  </tbody>
</table>

COCOMO II replaced the three project classes with **five scale factors** that determine the exponent: precedentedness (how familiar the work is), development flexibility, architecture and risk resolution, team cohesion, and process maturity. It uses seventeen cost drivers, and accounts for reuse of existing code and for the effort of modifying it. It also allows for the uncertainty that rises at the early stages.

### Other Models

- **SLIM** (Lawrence Putnam), based on a curve of staffing over time and on the idea that compressing the schedule below a point raises effort steeply.
- **SEER-SEM** and **PRICE-S** are commercial models.
- **Use-case-based and function-point-based models,** where effort is derived from points using productivity rates.
- **Machine-learning models,** which learn patterns from data sets of past projects; they inherit the weaknesses of their data.

## Calibration

A model's constants reflect the organisations and years in which its data were collected. Using them unchanged for a very different organisation produces large errors. **Calibration** adjusts the model with local data.

1. Collect **size, effort, duration, and driver ratings** for completed projects in your own organisation.
2. **Fit** the constants so that the model reproduces your history.
3. **Check** the fit on projects not used for fitting.
4. **Recalibrate** regularly as technology and practices change.

An organisation that does not record actual size and effort cannot calibrate, and its use of a parametric model is little more than guesswork with an authoritative look.

## Worked Idea

Suppose an intermediate-class project is sized at 30 thousand lines of code. The model yields a nominal effort, perhaps around a hundred person-months, which is then multiplied by the product of the cost drivers. A strong, experienced team with good tools might bring the multiplier below one; a weak team with demanding reliability requirements might push it above one and double the effort. The duration comes out as some months, and the average team size follows by dividing effort by duration. The values themselves depend on the version and the calibration; the key insight is the **structure:** a size term raised to a power, adjusted by multipliers.

## Strengths

- **Repeatable and transparent:** the same inputs give the same output, and assumptions are explicit.
- **Encourages thinking about cost drivers:** teams ask whether reliability, team experience, and schedule pressure are properly considered.
- **Supports what-if analysis:** how does the estimate change if experience is lower, or the schedule compressed?
- **Gives a second opinion** to compare with expert or bottom-up estimates.
- **Highlights schedule compression:** compressing time below the model's nominal schedule raises effort steeply.

## Limits and Dangers

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limit</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The size input is itself an estimate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Errors in size flow straight into effort, and size is hardest to know early, when estimates are most wanted</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Calibration dependence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Models fit on data from other environments can be badly wrong for yours</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">False precision</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A result like 412.7 person-months looks exact but may be wrong by a large factor</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Subjective driver ratings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rating team capability or complexity involves judgement; people can tune ratings to reach a desired answer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Out of date</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Practices such as agile methods, cloud services, frameworks, and open-source reuse change productivity in ways old data do not reflect</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor fit for some work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintenance, research, data and machine learning work, and highly innovative products are less predictable</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treats effort as a product of size</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ignores how work is organised, decisions made, or requirements change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Misuse as target</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A model result used as a commitment hides the uncertainty</td>
    </tr>
  </tbody>
</table>

## Using Models Wisely

- Treat the output as **one input to a range,** along with other methods.
- **Calibrate** on local history before trusting results.
- **Record the inputs and assumptions** with every use.
- **Run sensitivity analysis:** vary the uncertain inputs to see which matter most.
- **Do not use models to resist change** or to justify a fixed commitment.
- **Update the estimate** as size and drivers become better known.
- In agile settings, prefer **empirical forecasting from velocity or throughput,** and use parametric models, if at all, for early budgeting and for comparing options.

<!--
IMAGE PROMPT  ->  generate as images/04_effort_vs_size_and_cost_drivers.png   (16:9 explanatory diagram, place here)

Left: a chart of effort against size with two curves: a straight dashed line labelled Linear (wrong) and a rising curve labelled Diseconomy of scale (model). Right: a row of sliders for cost drivers (team capability, reliability, schedule pressure) each moving a multiplier bar up or down.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Read the Model

1. Why does doubling the size of a project more than double the effort in COCOMO?
2. A model calibrated on aerospace projects is used unchanged by a small web start-up. What risk arises?
3. Name two reasons a model's output should be presented as a range.

For case 1, the exponent on size is greater than one, representing coordination and integration costs that grow with scale. For case 2, a large error, since the productivity and practices differ; calibrate with local data. For case 3, the size input is uncertain, and the driver ratings are subjective; also the data may be out of date.

## Conclusion

An algorithmic cost model is a mathematical formula, derived from analysis of historical project data, that estimates software development effort and duration from a measure of software size and a set of factors describing the product, the platform, the people, and the project. Calibrated with local data and used alongside other methods, such models structure the thinking about cost.

Estimates describe what is expected; the next topic addresses what might go wrong. It introduces risk management.
