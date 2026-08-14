## Introduction

A logistics firm in Surat asks Devika to write a program that flags suspicious invoices before they are paid, and she starts the way any competent programmer would. She sits with the accounts team and writes down their rules.

Flag anything above two lakh rupees. Flag anything from a vendor registered in the last thirty days. Flag anything where the invoice number is out of sequence.

Within a month the accounts team is exhausted. The rules flag four hundred invoices a week, almost all of them legitimate, because most large invoices are perfectly ordinary. Meanwhile a genuine fraud passes through untouched: three invoices of ninety thousand each, from a vendor of two years' standing, in perfect sequence. The senior accountant who eventually spots it cannot explain how. She says the amounts looked wrong for that vendor's usual pattern.

Devika asks her to write that down as a rule and gets the same answer Ramesh gave about generators and Iqbal gave about scooters: it depends. There is no threshold. There is a sense, built from eleven years of invoices, of what that vendor's invoices normally look like.

Devika cannot write that rule because nobody can. But she has something the accountant does not: four years of invoices in a database, each one now known to have been fine or fraudulent. What if the program could work out the rule from those, rather than being told it? That inversion is **machine learning**.

**Definition:** `Machine learning` is the field concerned with systems that improve at a task by processing data rather than by being explicitly programmed, deriving the rule from examples instead of receiving it from a person.

![Opening scene: A logistics firm in Surat asks Devika to write a program that flags suspicious invoices before they are paid, and she starts the way any competent programmer would.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_introduction_simple_v2.png)

## The Inversion

The relationship between rules, data, and answers is the clearest way to see what has changed.

In ordinary programming you supply the rules and the data, and the computer produces the answers. Devika writes "flag if amount is over two lakh", feeds in the invoices, and gets a list of flagged ones.

In machine learning you supply the data and the answers, and the computer produces the rules. Devika feeds in four years of invoices together with which ones turned out to be fraudulent, and the system derives whatever pattern separates them.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Approach</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">You provide</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Machine produces</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Fails when</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Rule-based programming</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules and data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Answers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nobody can state the rule</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Machine learning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data and answers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules, in the form of a model</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">There are too few examples, or the answers are wrong</td>
    </tr>
  </tbody>
</table>

Note carefully what this does *not* mean. Machine learning is not better than rules. It is the appropriate tool for a specific situation: **when the pattern is real but nobody can articulate it, and examples of it are available in quantity.** Devika's rule about invoices above two lakh needed no learning at all, and encoding it as a learned model would have been absurd. Income tax slabs, eligibility criteria, and safety interlocks should all remain rules.

![Visual explanation of ml inversion](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_ml_inversion.png)

## What "Learning" Means Here

The word is borrowed and slightly misleading, so it is worth pinning down.

A system has learned when its performance on a task improves as it processes more data, without anyone modifying its instructions. Three things must be present for that sentence to mean anything.

1. **A task.** Something specific the system does. Classify this invoice. Predict this price. Group these customers.
2. **A performance measure.** A number saying how well the task is being done. The proportion of frauds caught, say, or the average error in rupees.
3. **Experience.** Data the system processes, from which the improvement comes.

Say all three aloud for Devika's problem and the vagueness disappears: the task is labelling an invoice fraudulent or not, the measure is how many frauds are caught against how many legitimate invoices are wrongly flagged, and the experience is four years of settled invoices.

If you cannot name all three, you do not yet have a machine learning problem. This is the single most useful check to apply to any proposal, and a surprising number of them fail it, usually on the second item.

![Visual explanation of what "learning" means here](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_what_learning_means_here.png)

## The Model

The thing the learning produces is called a `model`, and beginners often expect something more mysterious than it is.

A model is a function with adjustable numbers inside it. Learning means searching for values of those numbers that make the function agree with the examples. Once the numbers are fixed, the model is just a function: give it an invoice, it returns a judgment.

Three words describe the stages, and keeping them distinct prevents a lot of confusion later.

- **Training** is the process of adjusting the numbers using examples whose answers are known.
- **The trained model** is the result: the function with its numbers now fixed.
- **Inference**, sometimes called prediction, is using that fixed function on new data.

Training is expensive and happens occasionally. Inference is cheap and happens constantly. A fraud model might train overnight once a week and then judge fifty thousand invoices a day, which is why the two are usually separate systems in practice.

![Visual explanation of the model](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_the_model.png)

## AI, Machine Learning, and Deep Learning

These three words are used interchangeably in ordinary conversation and mean different things, so it is worth fixing the relationship now.

They are **nested, not parallel**. Artificial intelligence is the broad field of building systems that perform tasks requiring intelligence. Machine learning is the part of AI where the system derives its behaviour from data. Deep learning is the part of machine learning that uses neural networks with many layers and learns its own features from raw input.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Scope</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example that belongs here and not lower</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Artificial intelligence</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any system performing tasks that would require intelligence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A route planner searching a road network; a rule-based diagnostic system</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Machine learning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Systems that derive behaviour from data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A decision tree scoring loan applications; Devika's fraud model</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Deep learning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Multi-layer neural networks that learn their own features</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recognising a face in a photograph from raw pixels</td>
    </tr>
  </tbody>
</table>

Two corrections follow, and both are worth making explicitly because they are so commonly got wrong.

**Not all AI is machine learning.** A route planner is unambiguously AI and learns nothing. Neither does a rule-based diagnostic system, nor a chess engine searching a game tree.

**Not all machine learning is deep learning.** A decision tree is machine learning and contains no neural network whatsoever. On the tabular data most organisations actually hold, simpler models frequently beat neural networks while training in seconds and remaining explainable, which matters when a rejected applicant asks why.

![Visual explanation of ai ml dl relationship](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_ai_ml_dl_relationship_context_v4.png)

## What Machine Learning Costs

Devika's inversion is not free, and a lesson that presents only the upside produces engineers who reach for a model when a rule would do. Four costs are real.

1. **It needs data, in quantity and with answers attached.** Devika is fortunate: four years of invoices with known outcomes. A firm launching a new product line has nothing to learn from.

2. **It inherits whatever is in the data.** If past investigators only ever scrutinised small vendors, the data records frauds among small vendors, and the model will learn to watch small vendors rather than to detect fraud.

3. **It gives no guarantees.** A rule that flags invoices above two lakh is provably correct about what it does. A learned model is accurate to some percentage on data resembling its training set, and the interesting cases are usually the ones that do not resemble it.

4. **It can be hard to explain.** Devika's accounts team will ask why a particular invoice was flagged, and depending on the model chosen, the honest answer may be difficult to give in a form anyone can act on.

The fourth cost is the reason model choice is a real decision rather than a matter of picking the most accurate option, and it returns repeatedly through this unit.

![Visual explanation of what machine learning costs](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_what_machine_learning_costs.png)

## Your Turn

Take three problems from your own experience and decide, for each, whether it needs rules or learning.

Suggested candidates: deciding whether a student has enough attendance to sit an examination, deciding which film a person will enjoy next, and deciding whether a photograph contains a cat. For each one, try to state the rule explicitly. Where you can state it, you have a rules problem and machine learning would be the wrong tool.

Then, for whichever of the three genuinely needs learning, write down the three requirements from earlier: the task in one sentence, the performance measure as a number somebody could actually compute, and where the experience would come from. The second is where most people stall, so push until you have a formula rather than a phrase. "Recommends good films" is not a measure. "The proportion of recommended films the user watches beyond ten minutes" is.

Finally, do the uncomfortable part. For your learning problem, write down one way the available data could be systematically biased by how it was collected, in the manner of Devika's investigators only ever examining small vendors. If you cannot find one, ask who generated the data and why, and try again.
