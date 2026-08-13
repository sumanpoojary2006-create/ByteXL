## Introduction

A bank commissions a model to predict which small-business loans will default. Eleven months later it is switched off, and the post-mortem is worth reading because nothing in it is about the model.

The model was accurate. It was built in five weeks by two competent people and reached a level of performance the business had agreed in advance was sufficient.

It was switched off because the loan officers never trusted a score they could not question. Because the data it was trained on came from a period when lending criteria were different, so its idea of a risky applicant was three years out of date. Because nobody had defined who was accountable for a rejected application. And because, six months in, an upstream system started recording turnover in a different unit, and no one noticed for nine weeks.

Five weeks of modelling and eleven months of everything else. That ratio is normal, and the sequence of stages a project actually passes through is the **AI development lifecycle**.

**Definition:** The `AI development lifecycle` is the sequence of stages an AI project passes through, from defining the problem and acquiring data, through building and evaluating a model, to deploying it and monitoring it in service, with each stage feeding back into the others.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_section_introduction.png)

## The Stages

Six stages, and the effort is distributed almost the inverse of how people expect.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Stage</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">The real question</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Where projects die</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Problem definition</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What decision changes, and who makes it?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Building a prediction nobody acts on</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Data collection</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does data exist, with labels, from the right period?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Labels that are expensive, biased, or leak the answer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Model development</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is the simplest thing that could work?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rarely; this stage usually goes fine</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Evaluation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is it good enough, measured how, for whom?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single number hiding uneven performance</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Deployment</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How does the prediction reach the decision?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nobody designed the workflow around it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Monitoring</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How will we know when it stops working?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Silent degradation that nobody detects</td>
    </tr>
  </tbody>
</table>

The third row is the one worth staring at. **Model development is the stage least likely to kill a project**, and it is the stage that gets almost all the attention in courses, including most of this one. The bank's failure touched every row except that one.

![Visual explanation of ai lifecycle](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_ai_lifecycle_context_v4.png)

## Problem Definition

The stage that is skipped, because it feels like talking rather than working.

Three questions have to be answered before anything is built, and a project unable to answer them should not proceed.

**What decision changes as a result?** Not what will be predicted, but what somebody will do differently. A default-risk score changes nothing unless somebody is authorised to decline, price differently, or ask for more collateral on the strength of it. A prediction that arrives after the decision is made, or that nobody may act on, is an expensive report.

**Who is accountable when it is wrong?** The bank never answered this. A loan officer who declines on the model's advice and is wrong faces consequences the model does not, which is a strong reason to ignore it. Where responsibility sits determines whether a system is used at all.

**What is the threshold for good enough?** Agreed before any results exist, because agreeing afterwards means agreeing to whatever was achieved. Stated as a measure that reflects the real costs of the two kinds of error, not as accuracy.

![Visual explanation of problem definition](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_section_problem_definition.png)

## Data

Usually the longest stage, and the one where the fatal problems are introduced quietly.

Four checks catch most of them, and all four have appeared earlier in this course in other contexts.

1. **Will each feature be available at prediction time?** The leakage question. A column filled in after the outcome makes a model that is superb in development and useless in service.
2. **Does the data come from the period the model will operate in?** The bank's data predated a change in lending criteria, so it had learned an idea of risk that no longer matched the applicants arriving.
3. **Who is represented, and who is missing?** A dataset assembled from whoever was convenient produces a model that works for whoever that was.
4. **How were the labels produced?** If past decisions were made by people, the model learns to imitate those people, including their mistakes. A model trained on which loans were approved learns the bank's past behaviour, not which loans were repaid.

The fourth is the subtlest and it has a specific trap. **You only observe outcomes for applications that were approved.** Rejected applicants have no repayment record, so the training data systematically omits the cases the model most needs to judge, and a model trained on it will be confident about a population it never saw.

![Visual explanation of data](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_section_data.png)

## Deployment Is a Workflow Problem

A model that returns a number is not a deployed system. What surrounds it decides whether it is used.

Four questions define the surroundings, and the bank got at least three wrong.

- **Where does the prediction appear?** In the officer's existing screen at the moment of decision, or in a separate report nobody opens.
- **What does it look like?** A number, a band, a recommendation with reasons, or a flag. This determines whether it can be questioned.
- **What may the person do with it?** Accept, override with a reason, or is it advisory only. Whether overrides are recorded determines whether you ever learn the model is wrong.
- **What happens when it is unavailable?** A system with no defined fallback stops the business when it fails.

Two deployment patterns are worth distinguishing, because they carry different risk.

`Shadow deployment` runs the model on live data and records its predictions without acting on them, letting the team compare against what actually happened before anything depends on it. This is the cheapest way to discover that a model excellent in testing is poor in service.

`Staged rollout` puts it in front of a small proportion of cases first, so that a problem affects a fraction rather than everyone. Both are ordinary software practice, and both are frequently skipped for AI systems on the grounds that the model was already tested, which confuses testing on historical data with testing in service.

![Visual explanation of deployment is a workflow problem](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_section_deployment_is_a_workflow_problem_simple_v2.png)

## Monitoring

The stage the bank lacked entirely, and the one that distinguishes a system from a project.

A model is not a fixed asset. Its performance decays, and the decay has three distinct causes worth telling apart.

**Data drift.** The inputs change distribution. More applications start coming from a different sector or region than the model saw.

**Concept drift.** The relationship between inputs and outcome changes. A level of turnover that indicated safety before a downturn indicates something else after it.

**Pipeline breakage.** Something upstream changes format, unit, or meaning. This is the bank's nine-week failure: turnover recorded in a different unit, the model receiving numbers a hundred times too small, and no alarm because the model still returned confident scores.

The third is the most common and the most preventable, and it produces no error message. **A model given nonsense returns confident nonsense**, which is why monitoring the inputs matters as much as monitoring the outputs.

A workable monitoring setup watches four things: the distribution of each input feature against training, the distribution of predictions, actual outcomes as they arrive, and the rate at which humans override. The last is the most informative and the most often omitted. A sudden rise in overrides means the people closest to the decisions have noticed something before any metric has.

The uncomfortable part is that ground truth arrives late. Whether a loan defaults is known in a year, so accuracy cannot be monitored in real time, and the earlier signals, drift and overrides, are what you actually have.

![Visual explanation of monitoring drift](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_monitoring_drift_context_v4.png)

## Your Turn

Write the problem definition the bank skipped, in one page.

Cover the three questions from that section: what decision changes, who is accountable when the model is wrong, and what threshold counts as good enough, expressed in a measure that reflects the different costs of declining a good applicant and approving a bad one. Then add the sentence that would have saved the project: what the loan officer is permitted to do with the score, and whether their overrides are recorded.

Then design the monitoring that would have caught the unit change in days rather than nine weeks. You cannot use loan outcomes, since those take a year. Name three things you could watch that would have shifted immediately, and for each, say what alert threshold you would set and what a false alarm would cost.

Finally, reason about the missing population. The bank has repayment records only for approved applicants. Describe how you would estimate the model's performance on applicants it would decline, given that you have no outcomes for them. There is no fully satisfying answer, and the partial ones, approving a small random sample against the model's advice, or using data from a period with looser criteria, both have costs worth naming.
