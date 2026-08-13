## Introduction

A retail chain in Jaipur gives its new data team three requests in the same week, and the team's first mistake is assuming they are three versions of one job.

The first request comes from the credit desk: here are forty thousand past loan applications and whether each one was repaid, so predict repayment for new applicants. The second comes from marketing: here are two lakh customers and everything they have ever bought, so tell us what kinds of customer we have. The third comes from operations: here is a warehouse robot, make it find the quickest route through the aisles, and no, we have no record of good routes because nobody has ever measured one.

The team builds the first successfully and then stalls on the other two, because they keep trying to make them look like the first. Marketing has no answers to learn from, since nobody has ever labelled a customer as belonging to a type. Operations has no data at all until the robot starts moving.

These are not one problem with three datasets. They are three fundamentally different learning situations, distinguished by what feedback the system receives, and each has its own methods. They are the **learning paradigms**.

**Definition:** The `learning paradigms` classify machine learning problems by the kind of feedback available: `supervised learning` when every example carries a correct answer, `unsupervised learning` when the data has no answers at all, and `reinforcement learning` when feedback arrives as rewards following actions rather than as answers.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_introduction.png)

## Supervised Learning

`Supervised learning` is learning from examples where the correct answer is attached to each one. The credit desk's request is the pure case: forty thousand applications, each with a known repayment outcome.

The vocabulary is worth fixing precisely, because it is used constantly.

- A **feature** is an input the model gets to see. Income, age, loan amount, existing debt.
- A **label** is the correct answer for that example. Repaid or defaulted.
- A **labelled dataset** is a collection of examples that each carry both.

The word "supervised" refers to the label acting as a supervisor: for every example, something external tells the system what the right answer was, so the system can measure how wrong it currently is and adjust.

Supervised problems split into two kinds according to what the label is.

- **Classification** predicts a category from a fixed set. Repaid or defaulted. Spam or not spam. Which of five product categories this is.
- **Regression** predicts a continuous quantity. The price of a flat in rupees. Tomorrow's demand in units. Days until a machine fails.

The distinction matters because it changes both the methods available and how error is measured. Being wrong about a category is a different kind of wrong from being off by three thousand rupees, and the two cannot share a scoring function.

The binding constraint on supervised learning is labels. Not data, labels. Most organisations have plenty of the first and very little of the second, because labelling usually requires a human to examine each example and record the answer. This is why so much practical effort in industry goes into acquiring labels cheaply, and why a problem where labels arrive for free, as they do when a loan eventually repays or defaults on its own, is a fortunate one.

![Visual explanation of three learning paradigms](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_three_learning_paradigms.png)

## Unsupervised Learning

`Unsupervised learning` finds structure in data that has no labels at all. Marketing's request is this: two lakh customers, complete purchase histories, and nothing saying what type any customer is.

Notice that the request is not badly specified. Nobody is withholding the labels. **The labels do not exist**, because "type of customer" is not a fact about the world that somebody forgot to record. It is a structure the data may or may not contain, and finding it is the task.

Three families of unsupervised problem cover most of what is done.

1. **Clustering** groups examples that resemble one another, which is exactly what marketing wants: discover that the customer base contains, say, four recognisable buying patterns.
2. **Dimensionality reduction** compresses many features into a few that retain most of the information, which makes data visualisable and models faster.
3. **Anomaly detection** identifies examples unlike anything else, which is a common approach to fraud precisely when labelled fraud examples are scarce.

The genuine difficulty of unsupervised learning is that **there is no answer key, so there is no unambiguous way to say whether the result is right.** If the algorithm reports four customer groups and a colleague's algorithm reports six, no measurement settles which is correct. What can be assessed is whether the groups are internally similar, whether they are stable when the data changes, and above all whether they are useful to the person who asked. Marketing's four groups are good if marketing can act differently towards each and see a result.

This is a real epistemological difference from supervised learning, not a temporary shortcoming, and it should make you appropriately cautious about confident claims made from unsupervised results.

![Visual explanation of unsupervised learning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_unsupervised_learning.png)

## Reinforcement Learning

`Reinforcement learning` learns from the consequences of actions. There is no dataset of correct answers, and often no dataset at all at the start. An agent acts, the environment responds with a reward or a penalty, and the agent adjusts to earn more reward over time.

Operations' warehouse robot is this case. Nobody knows the quickest route, so nobody can label one. What can be measured is how long a completed trip took, and that number, fed back after the fact, is enough to learn from.

Four terms define the setting.

- **The agent** is the learner, here the robot.
- **The environment** is what it acts in, here the warehouse.
- **An action** is a choice it makes, such as which aisle to enter.
- **A reward** is the numerical feedback that follows, here negative for time spent and positive for an order completed.

Two features make this paradigm genuinely harder than the other two.

**Feedback is delayed.** The robot learns the trip took nine minutes only when the trip ends, and by then it has taken forty decisions. Working out which of those decisions deserves the blame is called the credit assignment problem, and it is the central difficulty of the field.

**The agent generates its own data.** In supervised learning the dataset sits there, fixed. Here, what the robot experiences depends on what it chooses to do, so a robot that always takes the route it currently believes is best will never discover a better one. It must sometimes act suboptimally on purpose in order to learn, which is the tension between exploration and exploitation.

![Visual explanation of reinforcement learning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_reinforcement_learning.png)

## Choosing the Paradigm

The choice is not a matter of taste. It follows directly from what feedback is available, and the question to ask is simply: **for a given example, does something tell me the right answer?**

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Paradigm</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Feedback</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Goal</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Jaipur example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Hardest part</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Supervised</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A correct answer for every example</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predict the label for new examples</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predict loan repayment from 40,000 settled applications</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Getting enough labels</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Unsupervised</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">None</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find structure in the data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discover what kinds of customer exist among 2 lakh</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No answer key, so no clean way to be right</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Reinforcement</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rewards following actions, often delayed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learn a policy that earns the most reward</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Robot learns quick aisle routes with no recorded good routes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delayed credit assignment, and generating its own data</td>
    </tr>
  </tbody>
</table>

Two boundary cases deserve mention, because real problems land on them regularly.

**Semi-supervised learning** applies when a few examples are labelled and a great many are not, which is the usual situation in practice. A hospital may have a thousand scans read by a radiologist and two lakh unread, and methods exist that use the unlabelled majority to improve on what the labelled minority alone would give.

**Self-supervised learning** manufactures labels from the structure of the data itself. Hide a word in a sentence and ask the model to predict it, and you have a supervised problem with labels nobody had to write, generated from ordinary text in unlimited quantity. This trick is what made modern language models possible, and it is best understood as a clever way of converting an unlabelled pile into a supervised problem rather than as a fourth paradigm.

![Visual explanation of choose learning paradigm](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_choose_learning_paradigm.png)

## Your Turn

Classify five systems you use by paradigm, and justify each by naming the feedback rather than the application area.

Try these: a spam filter, the shuffle feature that learns which songs you skip, a keyboard that suggests the next word, a shop's "customers who bought this also bought" panel, and a thermostat that learns your schedule. For each, answer one question: for a single example, what tells the system whether it was right, and when does that information arrive?

The keyboard is the interesting one. It looks unsupervised, since nobody labels text, and it is in fact supervised on labels the data generates for itself, because the next word in every sentence ever written is a free label for predicting the next word. Work out why that makes it self-supervised, and why that distinction matters for how much training data is available.

Then take one of your own realistic problems and try to move it between paradigms. Suppose you want to detect faulty items on a production line and have no labelled faults. Describe the unsupervised approach, then describe what would have to be collected to make it supervised, then estimate what that collection would cost in human hours. Most machine learning projects are decided by exactly this calculation, and doing it once yourself is worth more than memorising the three definitions.
