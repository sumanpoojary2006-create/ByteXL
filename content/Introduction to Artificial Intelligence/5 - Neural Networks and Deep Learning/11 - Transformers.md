## Introduction

A machine translation team meets on a Monday morning in June 2017 to discuss a paper somebody circulated over the weekend. The meeting is unusually short, because half the room has read no further than the title and does not take it seriously: attention is all you need.

It reads as a design decision rather than a discovery, and that is more or less what it was. The claim was that the recurrent machinery everyone had been building translation systems around, the carefully engineered gated cells, the sequential processing, all of it, could be removed. Not improved. Removed, and replaced with stacked attention layers and very little else.

This was not an obvious proposal. Recurrence had been the natural way to handle sequences for thirty years, on the reasonable grounds that language arrives in order and a model should process it in order. Discarding that meant discarding the only thing giving the model any notion of sequence.

It worked, and the resulting architecture now underlies essentially every large language model, most modern translation, a great deal of speech processing, and increasingly image and video systems as well.

**Definition:** A `transformer` is a neural architecture built from stacked layers of self-attention and position-wise feedforward networks, with positional encoding supplying order and residual connections and normalisation making depth trainable, processing all positions of a sequence in parallel.

![A machine-translation team splits between skepticism and curiosity over Attention Is All You Need on a Monday in June 2017](images/11_section_introduction_v2.png)

## What a Transformer Block Contains

The architecture is repetitive, which is much of its appeal. One block is defined, and then stacked.

A block has four components in a fixed arrangement.

1. **Multi-head self-attention.** Each position gathers information from all positions, several times over in parallel.
2. **A residual connection and normalisation.** The block's input is added back to its output, and the result is rescaled.
3. **A position-wise feedforward network.** A small two-layer network applied to each position separately and identically.
4. **Another residual connection and normalisation.**

Stack twelve of these and you have a small transformer; stack ninety-six and you have a large one. Nothing changes between blocks except the learned weights.

Two of these components deserve explanation, because they are what turns a mechanism into a trainable architecture.

![Visual explanation of transformer block](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_transformer_block.png)

## Multi-Head Attention

A single attention calculation produces one set of weights per position, which forces one notion of relevance. But a word relates to its neighbours in several different ways at once. In "the cat that the dog chased drank the milk", the word "drank" needs to find its subject, which is "cat", and separately its object, which is "milk", and these are different questions with different answers.

`Multi-head attention` runs several attention calculations in parallel, each with its own learned query, key, and value projections, and concatenates the results. Each `head` is free to specialise.

When researchers examined trained models, heads were found that track broadly interpretable relationships: one attending from a verb to its subject, another from a pronoun to its likely referent, another simply to the previous word. **Nobody assigned those roles.** Each head learned a different notion of relevance because nothing constrained them to agree.

The practical arrangement matters for cost. With twelve heads, each head works in a twelfth of the dimensions rather than the full space, so twelve heads cost roughly what one full-width head would. Multi-head attention buys variety, not extra computation.

![Visual explanation of multi-head attention](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_multi_head_attention_simple_v2.png)

## Residual Connections and Normalisation

A transformer is deep, and depth caused the vanishing gradient problem examined earlier in this unit. Two components address it, and without them the architecture would not train.

A `residual connection` adds a layer's input to its output, so the layer computes a change to its input rather than a replacement for it. The consequence for training is direct: the correction travelling backwards has a path that skips the layer entirely, so it arrives at earlier layers undiminished no matter how many blocks sit in between. This is what makes ninety-six layers possible.

There is a second benefit worth noting. If a layer has nothing useful to contribute, it can output near-zero and the residual passes the input through unchanged, so adding layers cannot easily make things worse.

`Layer normalisation` rescales the values flowing between components so their spread stays consistent. Without it, the numbers drift larger or smaller as they pass through many layers, and training becomes unstable. It is unglamorous and it is the difference between a network that trains and one that produces meaningless numbers after twenty blocks.

![Visual explanation of residual connections and normalisation](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_residual_connections_and_normalisation.png)

## Encoder and Decoder

The original design had two stacks, and the distinction still matters because the three families of modern model correspond to which parts they kept.

The **encoder** reads the input. Every position attends to every other position, both earlier and later, because when reading a sentence the whole thing is available at once and a word's meaning may depend on what follows it.

The **decoder** produces the output, one token at a time. It has two attention layers per block rather than one: a self-attention over what it has generated so far, and a `cross-attention` that looks back into the encoder's output. Cross-attention is the mechanism doing the translator's job from the previous lesson, looking back at the relevant part of the source while producing each word.

The decoder's self-attention has one crucial restriction called `masking`: a position may attend only to positions before it, never after. This is not a technicality. During training the model sees the whole target sentence at once for speed, and without masking it could simply look at the next word it is being asked to predict, learning nothing. Masking forces it to predict from the left context alone, which is the same situation it will face when generating.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Family</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Which stacks</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Sees</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Suited to</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Encoder only</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Encoder</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The whole input, both directions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Classification, search, understanding a fixed text</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Decoder only</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decoder</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only what precedes each position</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generating text; the shape of most large language models</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Encoder-decoder</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Both</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whole input, plus generated output so far</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Translation and summarising, where input and output differ in form</td>
    </tr>
  </tbody>
</table>

The middle row is the one that surprised people. The original architecture was built for translation and used both stacks, and it turned out that the decoder alone, trained on enough text simply to predict the next token, produces a system that can also translate, summarise, answer questions, and write code without being separately built for any of them.

![Visual explanation of encoder decoder parallel](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_encoder_decoder_parallel.png)

## Why It Displaced Recurrence

Three advantages, and it is worth being clear that only the first is about quality.

**Training parallelises completely.** Every position in a sequence is processed simultaneously, so the graphics hardware that had been sitting idle during recurrent training is fully occupied. This is the decisive advantage: a transformer can be trained on far more text in the same wall-clock time, and more text turned out to matter enormously.

**Distance costs nothing.** Position 1 reaches position 1,000 in one attention step, with no decay. The long-range dependency problem, unsolved for decades, dissolves.

**It scales predictably.** Making the model bigger and training it on more data improves it in a way regular enough to be described by fitted curves, which is why organisations were willing to commit very large budgets: the return was forecastable rather than speculative.

The cost is the quadratic one from the previous lesson. Every position attends to every other, so doubling the sequence length quadruples the attention computation, which is why context length is a headline specification and why a great deal of research goes into reducing it.

![Visual explanation of why it displaced recurrence](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_why_it_displaced_recurrence.png)

## What a Transformer Does Not Do

Three clarifications, because the architecture's success invites overstatement.

**It has no memory between calls.** A transformer processes whatever is in its context window. It does not retain anything from a previous conversation unless that text is placed in the context again.

**It has no notion of truth.** The training objective is to predict the next token accurately. Nothing in the architecture distinguishes a true continuation from a plausible one, which is the structural origin of confident falsehoods rather than a bug to be patched.

**It is not doing what a brain does.** Attention is a weighted average computed from dot products. That it produces something resembling contextual understanding is a genuine and surprising result about scale, and it is not evidence of a mechanism shared with human cognition.

![Visual explanation of what a transformer does not do](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_what_a_transformer_does_not_do.png)

## Your Turn

Reason about masking without any code, because getting it right is a good test of whether the decoder makes sense to you.

A decoder is trained on the sentence "the cat drank the milk". Write out which positions position 4, the word "the", is permitted to attend to, and which it is forbidden from attending to. Then explain what would go wrong during training if the mask were removed, and specifically what the model would learn to do instead of predicting.

Then work out the parameter arithmetic for a block. Take a model width of 512. A single attention head needs three projections, for query, key, and value, each 512 by 512, plus an output projection of the same size. The feedforward network expands to 2,048 and back. Count the weights in one block, then multiply by 12 blocks. Compare your total with the fully connected image network from earlier in this unit, and you will see why these models are described in billions of parameters.

Finally, take a position on the design. The original paper removed recurrence entirely, and the previous lesson showed that attention alone is blind to order and needs positional encoding bolted on. Argue that this was the right trade, then argue it was not, using the parallelism and quadratic-cost facts on each side. There is a defensible case both ways, and articulating it is more useful than accepting that the winning design was obviously correct.
