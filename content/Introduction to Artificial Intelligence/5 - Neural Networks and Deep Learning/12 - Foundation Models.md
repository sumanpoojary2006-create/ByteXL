## Introduction

A hospital group wants a system that reads discharge summaries and flags the ones needing follow-up. They have four thousand summaries, labelled by a consultant over several months.

Four thousand examples is nowhere near enough to train a language model from scratch. A model built on that data alone would have to learn what words are, how sentences work, and what a discharge summary is, all before getting to the actual question, and it would learn none of it properly.

Ten years ago that would have ended the project. Today the team downloads a model somebody else trained on an enormous quantity of general text, at a cost they could never have met, and adapts it to their four thousand examples in an afternoon. It works.

Nothing in the architecture changed. What changed is where the knowledge comes from: the expensive general learning happens once, centrally, and everybody else starts from it.

**Definition:** A `foundation model` is a large model trained once on a broad quantity of unlabelled data, producing general-purpose capabilities that can then be adapted cheaply to many specific tasks through `fine-tuning` or prompting, rather than each task requiring a model trained from scratch.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_section_introduction.png)

## The Labelling Problem, Solved Sideways

Supervised learning needs labelled examples, and labels are expensive because a person has to produce each one. That is the binding constraint on almost every practical project.

Foundation models get around it with a trick worth understanding properly. Take a sentence, hide part of it, and ask the model to predict what was hidden. The correct answer is the part that was hidden, so **the label was already in the data**. No human wrote it.

This is called `self-supervised learning`, and its consequence is that the supply of training data becomes effectively unlimited. Every sentence ever written is a training example for predicting the next word. There is no annotation budget, no team of labellers, and no ceiling except how much text exists.

The task sounds trivial and is not. To predict the next word well across billions of varied sentences, a model has to represent grammar, factual associations, the structure of arguments, the conventions of different kinds of document, and a great deal about how the world tends to work. **Capability arrives as a by-product of a simple objective pursued at enormous scale.**

![Visual explanation of the labelling problem, solved sideways](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_section_the_labelling_problem_solved_sideways.png)

## Pre-Training and Adaptation

The two-stage arrangement is the whole idea.

`Pre-training` is the expensive stage. One model, an enormous corpus, and a self-supervised objective, run for weeks or months on large hardware at a cost that only a handful of organisations can meet. The result is a model with broad capability and no particular specialisation.

Adaptation is the cheap stage, and there are several ways to do it.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Method</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Data needed</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cost</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Full fine-tuning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continue training every weight on your data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Thousands of examples</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hours to days</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Partial fine-tuning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Freeze most weights, train a small added set</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hundreds to thousands</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Minutes to hours</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Few-shot prompting</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Put a few worked examples in the input</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A handful</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">None; no weights change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Zero-shot prompting</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simply describe the task</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">None</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">None</td>
    </tr>
  </tbody>
</table>

The bottom two rows are the genuinely new thing. In the older way of working, changing what a model does meant retraining it. With a sufficiently capable pre-trained model, some tasks can be specified in the input itself, and the model performs them without a single weight being altered. That is a different relationship between a model and a task than anything earlier in this unit.

The hospital would use the second row. Four thousand summaries is too few to train anything from scratch and ample for adapting a model that already understands English.

![Visual explanation of pretrain adapt](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_pretrain_adapt.png)

## Why Transfer Works

The underlying reason is the layered representation described earlier in this unit.

A model trained on general text learns, in its earlier layers, things that are useful for almost any language task: how words relate, how clauses combine, how negation works. Only the last part of the network is specific to predicting the next word in general prose. Replace or adjust that part and the general machinery below is still exactly what a discharge-summary classifier needs.

This is the same phenomenon that lets an image network trained on photographs of animals be reused for medical scans. Edges and textures are edges and textures.

Two practical consequences follow, and they explain how organisations without vast resources use deep learning at all.

- **You need far less data.** The model is not learning language from your four thousand examples; it is learning your particular task, which is a much smaller thing to learn.
- **You need far less compute.** Pre-training is measured in months and millions; adaptation is measured in hours.

`Transfer learning` is the general name for reusing a model trained on one task as the starting point for another, and foundation models are that idea taken to its limit: pre-train once on everything, transfer to anything.

![Visual explanation of transfer limits](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_transfer_limits.png)

## What This Changed Beyond the Technology

The shift has consequences that are not technical, and they belong in an honest account.

**Capability concentrated.** Pre-training a large model requires resources available to a small number of organisations, so the models everyone builds on are made by very few actors. The choices they make about training data, filtering, and behaviour propagate to every downstream system.

**Inherited flaws propagate too.** A bias in a foundation model appears in every application built on it. Previously a flawed model harmed one project; now it can appear in thousands, and the organisations deploying it often cannot inspect the training data.

**Evaluation became harder.** A model built for one task is tested on that task. A model that does thousands of tasks, including ones nobody anticipated, cannot be exhaustively evaluated, so its failure modes are found in deployment.

**The economics inverted.** The expensive part is no longer building your model; it is the pre-training you did not do. Most organisations are now consumers of capability rather than producers of it, and that is a genuine change in who controls what.

![Visual explanation of what this changed beyond the technology](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_section_what_this_changed_beyond_the_technology.png)

## The Honest Limits

Foundation models are described in language that outruns them, so three limits are worth stating plainly.

**Fluency is not accuracy.** The training objective rewards plausible continuations, and a confident false statement is a plausible continuation. This is structural, not a defect awaiting a patch.

**The knowledge has a cut-off and no source.** What the model absorbed during pre-training is fixed at that moment and cannot be traced to any particular document, which makes both updating and verification hard.

**Adaptation does not add knowledge reliably.** Fine-tuning on four thousand discharge summaries teaches the model your task and your conventions. It does not reliably install new facts, and expecting it to is one of the more common disappointments in practice.

![Visual explanation of the honest limits](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_section_the_honest_limits.png)

## Your Turn

Decide, for three situations, which row of the adaptation table you would use and why.

First, classifying customer complaints into eight categories, with 200 labelled examples. Second, the same task with 50,000 labelled examples. Third, drafting replies in your organisation's particular tone, with no labelled data but twenty good examples written by your best agent. Justify each by the amount of data rather than by which method sounds most sophisticated, and notice that more data does not always mean the heavier method is better.

Then think through the propagation problem concretely. Suppose the foundation model your hospital adapted was pre-trained on text in which a particular condition is discussed mostly in the context of one demographic group. Describe how that could surface in the follow-up flagging system, and what you would test to find out whether it has. Note that you cannot inspect the pre-training data, so your test has to work from the outside.

Finally, take a position on concentration. Argue that a handful of organisations pre-training the models everyone uses is efficient and sensible, since duplicating that cost would be wasteful. Then argue it is a serious problem. Both cases are strong, and the ability to hold them at once is closer to how people who work on this actually think than picking a side.
