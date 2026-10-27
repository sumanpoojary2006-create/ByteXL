## Introduction

In conventional software, engineers write the rules and the program applies them. In machine learning (ML), engineers supply data and an algorithm, and the system derives the rules itself, in the form of a model. This changes what can go wrong and how teams must work. The behaviour of the system depends on the data as much as on the code; tests cannot give exact expected outputs for every input; performance can quietly decline as the world changes; and the model is only a small part of a larger system. Practices from the earlier units still apply, but they need adapting. Many ML projects fail not because the model is poor but because the surrounding engineering is missing.

This topic describes how ML systems differ from conventional software, the life cycle and data pipelines, how to test and deploy models, how technical debt arises in ML, monitoring and drift, and the responsible-engineering concerns specific to ML.

**Definition:** Software engineering for machine-learning systems is the application of engineering practices to the development, deployment, and operation of systems whose behaviour is learned from data, covering data management, model development, testing, deployment, monitoring, and maintenance, so that such systems are reliable, reproducible, and accountable.

<!--
IMAGE PROMPT  ->  generate as images/16_intro_software_engineering_for_machine_learning_systems.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A small box labelled Model sitting in the middle of a much larger set of surrounding boxes: Data collection, Data verification, Feature extraction, Serving, Monitoring, Configuration, Infrastructure.

ON-IMAGE TEXT: show a short bold title "Software Engineering for Machine Learning Systems" plus only these few labels, large and legible: The Model Is a Small Part. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## How ML Systems Differ

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Conventional software</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Machine-learning system</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Source of behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules written by programmers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patterns learned from data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Main artefacts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code, data, model, and configuration, all of which change behaviour</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Correctness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defined by a specification; outputs can be exactly predicted</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Statistical: accuracy is measured on average; some errors are expected</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specific inputs with known expected outputs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evaluation against held-out data, metrics, and behavioural checks</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usually visible: crashes, errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Often silent: wrong or biased predictions without any error message</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change over time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behaviour changes only when code changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behaviour can degrade as the real world drifts away from the training data</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explainability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The logic can be read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Often opaque</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Development process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mostly deterministic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Experimental and iterative; many trials with uncertain results</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Roles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers, testers, operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plus data scientists, data engineers, ML engineers, domain experts</td>
    </tr>
  </tbody>
</table>

A well-known paper by D. Sculley and colleagues at Google (2015) observed that in a real ML system the learning code is a tiny fraction of the whole; the larger parts are data collection and verification, configuration, feature extraction, serving infrastructure, resource management, and monitoring. Successful ML is therefore mostly engineering.

## The Machine-Learning Life Cycle

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Stage</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Activities</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Engineering concerns</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1. Problem framing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decide what to predict or decide, and whether ML is appropriate; define success metrics linked to business value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is ML needed, or would rules suffice? What are the costs of wrong answers? Ethical and legal constraints</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2. Data collection and understanding</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gather, explore, and document data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quality, representativeness, consent and privacy, provenance, licensing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3. Data preparation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clean, label, transform, and split data; build features</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reproducible pipelines; label quality; avoiding leakage of information from the test data into training</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4. Model development</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose algorithms, train, tune, and compare experiments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Experiment tracking; reproducibility; avoiding over-fitting; simple baselines first</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5. Evaluation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measure performance on unseen data; check subgroups, robustness, fairness, and failure cases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Metrics aligned with real goals; slices of data; comparison with the existing process</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6. Deployment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Package the model and serve it as a service, batch job, or embedded component</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Versioning; latency; scaling; rollout strategy; integration with the application</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">7. Monitoring and maintenance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Watch data, predictions, and outcomes; retrain and update</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Drift detection; alerting; feedback collection; model retirement</td>
    </tr>
  </tbody>
</table>

The cycle is iterative: monitoring reveals problems that send the team back to data and modelling. This resembles the iterative processes of Unit 2 and the feedback loops of product thinking in Unit 13.

## Data Is a First-Class Artefact

- **Data pipelines** move raw data through ingestion, validation, cleaning, transformation, and storage to produce training sets and features. They are software and need version control, review, testing, and monitoring (Units 9 to 11).
- **Data quality** limits model quality. Typical problems: missing values, duplicates, errors, shifts in definitions, biased sampling, and mislabelled examples. Validate data automatically against expectations (schemas, ranges, distributions) and stop pipelines when checks fail (Unit 12 on schemas).
- **Labelling** often relies on people; define guidelines, measure agreement between labellers, and treat labellers fairly.
- **Data versioning and lineage:** record which data produced which model, so results can be reproduced and audited.
- **Feature stores** provide consistent features for training and for serving.
- **Training-serving skew:** the features computed at prediction time differ subtly from those in training, causing unexplained failures. Use the same code and definitions in both.
- **Data leakage:** accidentally using information in training that would not be available at prediction time, which gives deceptively good results that vanish in production.
- **Privacy and governance** apply fully: minimise personal data, control access, and respect consent and purpose limits (previous topics).

## Testing Machine-Learning Systems

Exact expected outputs are not available, but testing remains essential. Layers of testing include:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verify input data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Schema and range checks; distribution comparison against training data; detection of missing or duplicated records</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pipeline and code tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verify the conventional software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unit tests of feature calculations; integration tests of the pipeline end to end (Unit 10)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Model evaluation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measure predictive quality on held-out data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accuracy, precision and recall, error rates, calibration; compare to a simple baseline and the current system</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slice-based evaluation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find groups on which the model performs poorly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance by region, language, device, demographic group</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behavioural tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check expected properties</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invariance tests (changing irrelevant details should not change the output), directional tests (raising a relevant input should move the output in the expected direction), minimum functionality tests on simple cases</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Robustness and adversarial tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check behaviour under noise and attack</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small input perturbations; deliberately crafted inputs; out-of-range data</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fairness and bias tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detect disparate impact (Unit 14 case studies)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compare error rates and outcomes across groups</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regression tests for models</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make sure new versions are not worse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A fixed suite of important cases and metrics for every candidate</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integration and performance tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check the model within the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Latency, throughput, memory, failure handling when the model is unavailable</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Online experiments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measure real-world impact</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A/B tests; shadow deployment, where the new model runs on live traffic without affecting users; gradual rollout (Unit 9)</td>
    </tr>
  </tbody>
</table>

Choosing **metrics** needs care: overall accuracy can mislead when classes are imbalanced (a fraud model that always predicts "no fraud" is highly accurate and useless). Link metrics to business and harm costs, and set thresholds explicitly.

## Deployment and MLOps

**MLOps** applies DevOps (Unit 9) to ML: automation, versioning, monitoring, and collaboration across the life cycle.

- **Version everything:** code, data, features, model, configuration, and environment; keep a **model registry** with metadata, evaluation results, and approvals.
- **Reproducible training:** fixed environments (containers), recorded random seeds and parameters, tracked experiments.
- **Continuous integration and delivery for ML:** automated pipelines that test data and code, train, evaluate against the current model, and promote only models that pass; sometimes called continuous training.
- **Serving patterns:** online services behind an interface, batch scoring on a schedule, streaming, or embedded on-device models.
- **Release strategies:** shadow, canary, and A/B releases with the ability to roll back quickly to the previous model.
- **Fallbacks:** if the model fails or is unsure, use a simple rule, a human, or a safe default.
- **Resource management:** training and serving can be costly in compute and energy (previous topics).

## Monitoring and Drift

A deployed model begins to age immediately, because the world changes.

- **Data drift:** the distribution of inputs changes (new customer groups, a changed sensor, a new product range).
- **Concept drift:** the relationship between inputs and the correct answer changes (customer behaviour shifts after an economic change; fraudsters adapt).
- **Upstream changes:** another team alters a field's meaning or format, silently breaking features.
- **Feedback loops:** the model's decisions influence future data (recommendations shape what people click, then the model learns from the clicks).

Monitor: input data statistics; prediction distributions; operational health (latency, errors); and, when labels eventually arrive, actual performance. Alert when thresholds are crossed and define retraining triggers and review procedures. A model whose outcome feedback is slow or absent needs proxies and periodic audits.

## Technical Debt in Machine-Learning Systems

Sculley and colleagues argued that ML systems carry all the maintenance problems of ordinary code, plus a set of ML-specific forms of technical debt (Unit 8).

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Form of debt</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Entanglement (CACE: changing anything changes everything)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inputs are not independent; changing one feature, hyper-parameter, or the data distribution alters the behaviour of the whole model, making isolated improvements impossible</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden feedback loops</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Models influence their own future training data in ways that are hard to see</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Undeclared consumers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Other systems use the outputs of the model without the team knowing, so any change may break them</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unstable or under-used data inputs; dependencies on data sources that change without notice, harder to analyse than code dependencies</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large numbers of settings, poorly tested and documented</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pipeline jungles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accumulated glue code and ad hoc scripts for preparing data</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dead experimental code paths</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Leftover branches from experiments that increase complexity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abstraction debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lack of agreed abstractions for ML components</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Glue code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large amounts of code written to fit a general-purpose library into a system</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reproducibility debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Results that cannot be re-created because data, code, or environment were not recorded</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monitoring debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Insufficient detection of silent failure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes in the external world</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependence on conditions that no longer hold</td>
    </tr>
  </tbody>
</table>

Remedies are those of Unit 8 applied with discipline: clean interfaces and documented dependencies, tests, monitoring, regular refactoring of pipelines, removal of unused features and experiments, registries, and clear ownership.

## Responsible and Trustworthy ML

ML decisions affect people, and the issues of the ethics topics apply with particular force.

- **Fairness and bias:** check data and outcomes across groups; document limitations (see the case studies).
- **Transparency and explainability:** use interpretable models where the stakes are high; use explanation techniques for complex ones, understanding their limits; inform affected people.
- **Documentation:** **datasheets for datasets** and **model cards** record purpose, data, performance, limits, and appropriate uses.
- **Privacy:** models can memorise and leak training data; apply minimisation, access controls, and privacy-preserving techniques (previous topic).
- **Security:** models can be attacked by poisoned training data, adversarial inputs, model theft, and extraction of private data.
- **Human oversight:** keep a person in control of consequential decisions, with real authority and information, and beware of automation bias.
- **Accountability and governance:** assign owners, impact assessments, and approval gates; laws such as the EU AI Act (adopted 2024) impose requirements by risk level, and data-protection law gives rights regarding automated decisions.
- **Environmental cost:** account for energy use of training and serving (previous topic).
- **Knowing when not to use ML:** if a simple rule works, or errors would be intolerable, or data is inadequate, choose a simpler solution.

## Working in ML Teams

- **Start simple:** a rule-based or statistical baseline often delivers most of the value and sets a benchmark.
- **Engineer the whole system first:** a basic end-to-end pipeline with monitoring before refining the model.
- **Collaborate across roles:** data scientists, engineers, domain experts, and product managers share goals and vocabulary.
- **Apply software discipline to notebooks:** exploratory notebooks are fine for exploring, but production code should be moved into tested, reviewed modules.
- **Plan for maintenance:** models need owners, retraining budgets, and retirement plans.

<!--
IMAGE PROMPT  ->  generate as images/16_ml_lifecycle_and_drift.png   (16:9 explanatory diagram, place here)

Left: a circular life cycle with seven stages from Frame to Monitor, with a return arrow from Monitor to Data. Right: a line graph of model accuracy over time falling after a vertical dashed line labelled World changes, with a green retraining step lifting it again.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Reason About ML Systems

1. A model scored 98 per cent in development but performs poorly in production because a feature is calculated differently in the serving system. What is this problem called?
2. Six months after release, a model's accuracy has fallen although no code changed. What is the likely cause, and how would you detect it?
3. Why can overall accuracy be a misleading metric?

For case 1, training-serving skew; use the same feature code and definitions in both. For case 2, drift in the data or in the underlying relationship; detect it by monitoring input distributions and prediction quality and by comparing against recent labelled data. For case 3, with imbalanced classes a model can achieve high accuracy by always predicting the common class while failing at the rare but important cases; use metrics such as precision and recall, and slice analysis.

## Conclusion

Software engineering for machine-learning systems is the application of engineering practices to the development, deployment, and operation of systems whose behaviour is learned from data, covering data management, model development, testing, deployment, monitoring, and maintenance, so that such systems are reliable, reproducible, and accountable. Because data shapes behaviour and the world keeps changing, versioning, data and model testing, monitoring, and responsible practice are as important as the model itself.

A newer development affects how almost all software is written: AI tools that generate code. The next topic covers AI-assisted software development.
