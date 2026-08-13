## Introduction

An insurance company handles motor claims, and the process has always had two halves that never met.

A claim arrives as a written description and a set of photographs. An assessor reads the description, looks at the photographs, and forms one judgment from both. A dented bumper photographed alone might be a minor claim or the visible corner of a serious one; the description resolves it. A description saying "significant front-end damage" might be accurate or optimistic; the photographs resolve that.

Their first automated system had a text model reading descriptions and a vision model examining photographs, and it worked poorly, because the two never spoke. The text model could not see that the photographs showed something milder than described. The vision model could not know the claimant had mentioned a prior repair.

What the assessor does, and what the two models could not, is reason across both at once. Systems that can are **multimodal**.

**Definition:** `Multimodal AI` refers to systems that accept or produce more than one kind of input, such as text, images, audio, and video, by representing each in a shared space so that information from different sources can be combined within a single model.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_introduction.png)

## The Central Problem

Bringing two modalities together requires solving something specific: a sentence and a photograph have nothing in common as data.

A sentence is a short sequence of tokens from a vocabulary of perhaps fifty thousand. A photograph is a grid of two million brightness values. They differ in size, in structure, in what adjacency means, and in every other respect. There is no direct way to compare them.

The solution is the one that has appeared repeatedly in this course: **map both into vectors in the same space, and arrange the training so that related things land near each other.** An encoder converts an image into a vector, another converts text into a vector, and the two are trained together so that a photograph of a dented bumper and the phrase "dented bumper" end up close.

Once that holds, everything else follows. Comparison becomes distance. Search across modalities becomes a nearest-neighbour lookup. And a language model can accept image vectors alongside token vectors, because by then they are the same kind of object.

![Visual explanation of multimodal alignment](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_multimodal_alignment_context_v4.png)

## How the Alignment Is Learned

The training trick is elegant and requires no manual labelling.

The internet contains an enormous quantity of images accompanied by text: captions, alt text, surrounding article copy. Each such pair is a weak statement that this picture and this text go together.

A model is then trained on a very simple objective: given a batch of image and text pairs, make each image's vector close to its own text's vector and far from all the others in the batch. Nobody labelled anything; the pairing was already present in the data, which is the self-supervised approach appearing again in a new setting.

What emerges is a shared space with a useful property. Because the model has seen millions of captioned images, it can score how well any image matches any description, including descriptions of categories it was never explicitly trained to recognise. Asked whether a photograph is better described as "a dented bumper" or "a cracked windscreen", it can answer, without either having been a class in a training set.

That capability, classifying against categories supplied at the time of asking rather than fixed during training, is called `zero-shot` classification, and it is the main practical reason these models matter. The insurance company can add a new damage category by writing a phrase, not by collecting and labelling examples.

![Visual explanation of how the alignment is learned](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_how_the_alignment_is_learned.png)

## Four Things Multimodal Systems Do

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Capability</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In goes</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Out comes</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">For the insurer</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Cross-modal search</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Matching images</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Find past claims resembling this one</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Captioning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An image</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A description</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Summarise what each photograph shows</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Visual question answering</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An image and a question</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An answer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Is the airbag deployed in this photograph?"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Joint reasoning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text and images together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A judgment using both</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does the damage shown match the description given?</td>
    </tr>
  </tbody>
</table>

The last row is what the assessor was doing and what the two separate models could not. It is also the row that changes the work rather than merely speeding it up: checking a description against evidence is a different task from either reading or looking, and it was not previously automatable at all.

Note what this enables that neither model could manage alone. A claim describing severe damage with photographs showing a scratch is now detectable as an inconsistency, which is a fraud signal. Neither model would have flagged it, because each saw only half.

![Visual explanation of multimodal capabilities](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_multimodal_capabilities_context_v4.png)

## What Grounding Does and Does Not Fix

A common claim is that adding vision fixes the reliability problems of text-only models, on the reasoning that a model which can see is anchored to reality. The claim is partly right and worth being careful about.

**What genuinely improves.** A model asked about a specific document, chart, or photograph in front of it is far less likely to invent, because the answer is present in the input rather than recalled. This is the same benefit retrieval provides for text, and it is real.

**What does not.** The model can still misread the image and then describe its misreading fluently. Multimodal systems are notably weak at counting objects, at reading text within images accurately, at spatial relationships, and at fine detail. A confident wrong answer about a photograph is exactly as confident as a right one.

**What gets worse.** There are now two ways to be wrong and they interact. A model may correctly read a chart and draw a false conclusion from it, or misread it and reason impeccably from the misreading, and the output looks the same in both cases. Diagnosing which happened requires checking the intermediate perception, which the output does not expose.

The honest position is that grounding narrows the gap between fluency and accuracy without closing it, and that a system permitted to act on what it thinks it saw needs the same verification as one acting on what it thinks it knows.

![Visual explanation of what grounding does and does not fix](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_what_grounding_does_and_does_not_fix_simple_v2.png)

## Why This Is Where the Field Is Going

Three reasons, and only the first is about capability.

**The world is not text.** Most tasks people want automated involve looking at something: a form, a scan, a shelf, a screen. A system confined to text can only act on what somebody has already transcribed.

**Modalities reinforce each other.** Training on images and text together produces better representations of both than training on either alone, because the caption tells the vision encoder what matters in the picture and the picture disambiguates the caption.

**Text data is finite.** The quantity of high-quality text is large and not unlimited, and much of it has been used. Images, video, and audio represent an enormous additional supply of training signal, and self-supervised objectives can exploit it without labelling.

The last point is a resource argument rather than an intellectual one, and it is doing a great deal of the work in current research direction.

![Visual explanation of why this is where the field is going](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_why_this_is_where_the_field_is_going.png)

## Your Turn

Design the insurer's inconsistency check.

The system must flag claims where the written description and the photographs disagree. Write down the steps it would take, using the four capabilities in the table. Then decide what threshold of disagreement should trigger a human review, and state the two kinds of error that threshold trades against, in the language of the evaluation lesson from earlier in this unit.

Then think carefully about who is harmed by a mistake. A claimant whose honest claim is flagged as inconsistent faces delay and suspicion. Describe two ways the system could produce that outcome unfairly: one involving the photographs, one involving the description. If your answers involve poor lighting in a claimant's photographs or a description written in a second language, you have identified failure modes that fall unevenly across claimants.

Finally, test the grounding claim. Suppose the model reads a photograph of a damaged wheel and reports "alloy wheel, cracked, requires replacement". List three distinct ways that sentence could be wrong, and for each, say whether the error is in perception or in reasoning, and how you would tell from the output alone. You will find that in at least one case you cannot tell, which is the practical limit of these systems and the reason a human remains in the loop for consequential decisions.
