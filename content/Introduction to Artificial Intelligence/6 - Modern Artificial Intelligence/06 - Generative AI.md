## Introduction

A small publishing house in Kochi asks its two-person design team to produce forty book cover concepts in a week, which is roughly four weeks of work.

They deliver in three days. Not by working faster, but by describing what they wanted to an image model, generating a few hundred variants, discarding most, and refining the survivors. The designer's job that week was not drawing. It was knowing what to ask for, recognising which outputs were nearly right, and fixing the ones that were.

That is a genuine change in what the tools do. Everything in this unit so far takes something in and produces a judgment about it: a label, a transcript, a ranking, a route. These systems produce artefacts that did not previously exist.

**Definition:** `Generative AI` refers to models that produce new content, such as text, images, audio, or code, by learning the statistical structure of a large body of examples and then sampling from it, rather than by classifying or scoring input.

![Opening scene: A small publishing house in Kochi asks its two-person design team to produce forty book cover concepts in a week, which is roughly four weeks of work.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_introduction.png)

## Recognising Against Producing

The distinction is worth stating precisely, because it changes what the model must learn.

A classifier answers a question with a small number of possible answers. Given a photograph, is this a cat or a dog? To answer, it needs only whatever distinguishes the two. Everything else about the image, the lighting, the background, the pose, can be ignored, and a good classifier learns to ignore it.

A generative model must supply all of it. Asked to produce a picture of a cat, it must decide the pose, the lighting, the background, the fur, and the shadow, none of which the request specified. **A generative model needs to have learned what a plausible whole looks like, not merely what separates one category from another.**

That is a much larger thing to learn, which is why generation lagged recognition by roughly a decade, and why generative models are so much bigger.

![Visual explanation of discriminative vs generative](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_discriminative_vs_generative_context_v4.png)

## The Common Mechanism

The four families in the table below look unrelated and share one underlying idea: learn a distribution over the training data, then sample from it.

For text, the concrete form is predicting the next token given everything before, repeated. For images, the dominant current approach is different in mechanism and identical in spirit.

`Diffusion models` learn by destruction and reversal. During training, an image is progressively corrupted with random noise across many small steps until nothing remains, and the model learns to undo one step of that corruption. To generate, the process is run backwards: begin with pure noise and repeatedly apply the learned denoising step, guided by a text description, until an image emerges. The model was never taught to draw. It was taught to remove a little noise, and drawing is what running that many times produces.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Output</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical mechanism</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Checking the result is</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Characteristic failure</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Text</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predict the next token, repeatedly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard; requires knowing the subject</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fluent statements that are false</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Images</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reverse a noising process, guided by text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy; you can look at it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anatomy, text within the image, counting</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Audio</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generate the waveform or a compressed form of it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy; you can listen</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Drifting over long durations</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Code</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predict the next token, as with text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easiest; run it and see</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plausible code calling functions that do not exist</td>
    </tr>
  </tbody>
</table>

The third column is the practical one and it is rarely discussed. **How useful a generative model is depends heavily on how cheaply you can check its output.** Code is the best case, because a test suite gives a verdict in seconds and a wrong answer is caught immediately. Images are next, because a designer can glance at a hundred and pick three. Factual text is the worst, because verifying a claim may take longer than writing it would have, and the output gives no signal about which parts need checking.

This explains an otherwise puzzling pattern in adoption. These tools took hold fastest in programming and design, not because those outputs are better, but because the cost of a bad output there is a few seconds of a person's attention.

![Visual explanation of the common mechanism](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_the_common_mechanism.png)

## Where the Publishing House Gained

The Kochi team's week is worth analysing, because the gain was not where people assume.

The model did not replace design judgment. Somebody still decided which forty concepts to pursue, what the house style was, which outputs were nearly right, and what was wrong with them. What collapsed was the cost of producing a candidate, from an hour to a few seconds.

That shifts the bottleneck. When candidates are expensive, effort goes into getting each one right first time, and you produce few. When candidates are nearly free, effort moves to specifying well and judging quickly, and you produce hundreds. **Generative tools are most valuable where the work is exploratory and a person is going to select and refine anyway**, and least valuable where the first output must be correct and nobody is positioned to check it.

Three patterns of use follow from that, and they are worth distinguishing.

- **Drafting.** The model produces a first version and a person edits. The person remains responsible and the model saves the blank page.
- **Variation.** The model produces many alternatives around a theme and a person selects. This is what the publishing house did.
- **Automation.** The output goes to a user or into a system without review. This is the pattern that requires the most care, because nothing catches a bad output.

![Visual explanation of where the publishing house gained](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_where_the_publishing_house_gained.png)

## What Goes Wrong

Four problems are structural rather than defects awaiting a fix.

**Fluency is not accuracy.** A text model is trained to produce likely continuations, and a confident false statement is a likely continuation. The output carries no signal distinguishing the parts that are reliable from the parts that are invented, which is what makes verification expensive.

**The training data was somebody's work.** These models learned from text and images made by people who were not asked and are not compensated. The legal position is unsettled and varies by jurisdiction, and treating it as settled in either direction is a mistake.

**Output can resemble training data closely.** Usually generation is genuinely novel; occasionally a model reproduces a distinctive passage or a recognisable style almost exactly, particularly for content that appeared many times in training.

**The cost of producing convincing false material collapsed.** Fabricated photographs, cloned voices, and plausible false text at volume are now cheap. This is not a misuse of a tool that also has good uses; it is the same capability seen from the other side.

To these, add one that is easy to miss. **The systems produce the average of what they were trained on**, so heavy reliance on them tends to converge on a house style nobody chose. For a publishing house whose value lies partly in looking unlike everyone else, that is a commercial risk rather than an aesthetic complaint.

![Visual explanation of generation failures](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_generation_failures_context_v4.png)

## Your Turn

Rank four tasks by how expensive it is to check the output, then decide which you would actually use a generative model for.

The tasks: writing unit tests for existing code, drafting a reply to a customer complaint, summarising a legal contract for a manager, and generating background images for a mobile game. For each, state who would check the output, how long checking takes, and what happens if a bad output gets through. Your ranking should end up close to your willingness to use the tool, and if it does not, work out why.

Then design the publishing house's process properly. They now want to use generated images on actual covers rather than as concepts. Write down three checks that must happen before an image goes to print, covering the failure modes above. At least one of your checks should address something the designer cannot determine by looking at the image.

Finally, sit with the averaging problem. Suppose every publisher in the country adopts the same tools next year. Describe what happens to the visual identity of Indian book covers over five years, and then propose how a house that wants to look distinctive should use these tools, if at all. There is a reasonable case for using them heavily and a reasonable case for avoiding them entirely, and the argument turns on what the house is selling.
