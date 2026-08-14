## Introduction

A food delivery company wants to score restaurant reviews automatically, and the first attempt is the obvious one: give every word a sentiment score and add them up.

It works reasonably until somebody checks the failures, and the failures share a shape. "The food was not good" scores positive, because "good" contributes and "not" contributes nothing. "Good luck getting a refund" scores positive. "I wanted to like it" scores positive.

Adding scores throws away order, and in language order is not decoration. The same words in a different arrangement mean something else, sometimes the opposite.

Convolution will not help here either. A filter slides across a fixed grid where neighbours are related by adjacency, and a sentence is not a grid: it has no fixed length, and the word that changes the meaning of the last word may be nineteen positions back.

What is needed is a network that reads one item at a time and carries something forward, so that what it has already seen shapes how it interprets what comes next. That is a **recurrent neural network**.

**Definition:** A `recurrent neural network` processes a sequence one element at a time, maintaining a `hidden state` that is updated at each step from the current input and the previous state, so that the state acts as a memory of everything seen so far.

![Opening scene: A food delivery company wants to score restaurant reviews automatically, and the first attempt is the obvious one: give every word a sentiment score and add them up.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_introduction.png)

## The Loop

An ordinary network maps input to output in one pass. A recurrent network has one extra connection: its own output from the previous step feeds back in.

At each step the cell computes:

**new state = activation( W_input × current input + W_hidden × previous state + bias )**

The first term is the new information. The second is the memory. Notice that the same weights are used at every step, exactly as a convolutional filter uses the same weights at every position, which is why a recurrent network can handle a sentence of any length with a fixed number of parameters.

Reading the code below: `step` is one line and is the recurrent cell in full. Everything else is a loop calling it once per word and printing a trace. The variable `hidden` is the only memory in the program; it is a single float, overwritten at every word.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjxx6" 
 width="100%"
></iframe>

```
Reading a review one word at a time

     word   score   carried in   new state
-------------------------------------------
      the     0.0        0.000       0.000
     food     0.0        0.000       0.000
      was     0.0        0.000       0.000
     good     1.2        0.000       0.834
  service     0.0        0.667       0.583
      was     0.0        0.466       0.435
     slow    -0.8        0.348      -0.423

Final state: -0.423

Nothing stores the words. The state is the only thing carried forward,
and every word that came before has left a trace in it.
```

| In the code | Which term | What it represents |
| --- | --- | --- |
| `W_INPUT * SCORES[word]` | New information | What this word contributes on its own |
| `W_HIDDEN * hidden` | The memory | Everything seen so far, discounted by 0.8 |
| `math.tanh(...)` | The activation | Keeps the state inside -1 to +1 so it cannot run away |
| `hidden = step(hidden, word)` | The loop | Output becomes input for the next word |
| `hidden` after the loop | The verdict | One number summarising the whole review |

Follow the "carried in" column, because that single number is the entire memory.

After "good" the state is 0.834, distinctly positive. The next two words carry no sentiment of their own, and the state decays to 0.583 and then 0.435 without going away. When "slow" arrives with a score of −0.8, it is added to a carried-in value of 0.348, and the result is −0.423.

The final verdict is mildly negative, and that is a genuine judgment about the whole review rather than about any single word. **Nothing in the network stores the sentence.** There is one number being repeatedly overwritten, and the influence of every earlier word survives only in how it shaped that number.

![Visual explanation of rnn loop](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_rnn_loop.png)

## Order Changes the Answer

The point of all this is to distinguish sentences that a bag of words cannot.

Reading the code below: two scoring functions are put side by side on the same sentences. `bag_of_words` is one line, a plain sum, and `recurrent` is the same cell as above with the trace removed. Each pair in `pairs` contains identical words in a different order, which is what makes the comparison fair.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjyg6" 
 width="100%"
></iframe>

```
              sentence  bag of words   recurrent
-------------------------------------------------
           it was good          1.20       0.834
           good it was          1.20       0.435

          good was bad          0.00      -0.625
          bad was good          0.00       0.625

         very good bad          0.00      -0.488
         very bad good          0.00       0.488

Every pair contains exactly the same words.
The bag of words cannot tell them apart. The recurrent state can,
because the state at each step depends on what came before it.
```

| In the code | What it does with order | Result on a reordered pair |
| --- | --- | --- |
| `sum(SCORES[w] for w in sentence)` | Ignores it entirely | Identical score both ways |
| `hidden = math.tanh(... + w_hidden * hidden)` | Depends on it at every step | Different score each way |
| `w_hidden=0.8` | Discounts older words | Later words weigh more, which is why the last word dominates |
| Word lists in `pairs` | Same words, shuffled | Isolates order as the only variable |

Three pairs, three times the bag of words gives identical answers and three times the recurrent state does not.

The middle pair is the clearest. "Good was bad" and "bad was good" contain exactly the same three words, sum to exactly zero, and the recurrent readings are −0.625 and +0.625. The last word dominates, because it arrives when the earlier contributions have already been discounted by the carrying weight.

That is a real property of language and the network captured it without being told: **later words tend to matter more, and the words before them set the context they land in.**

Do not overclaim from this. A hand-set weight of 0.8 is not a theory of English, and the network here has one number of memory. What the example establishes is the mechanism, which is that a state carried forward makes order matter at all.

![Visual explanation of order changes the answer](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_order_changes_the_answer_simple_v2.png)

## The Memory Fades

Now the limitation, which is severe and shaped everything that followed.

At each step the carried-over state is multiplied by the recurrent weight. Over many steps, that multiplication compounds.

Reading the code below: there is no network at all, only `w ** steps`. That single expression is what "multiplied by the recurrent weight once per word" comes to after N words, and it is the same arithmetic as the vanishing-gradient table in lesson 05, with time steps in place of layers.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjysw" 
 width="100%"
></iframe>

```
Influence of the first word on the state, after N more words

 steps later      w=0.5      w=0.8     w=0.95       w=1.05
----------------------------------------------------------
           1   5.00e-01   8.00e-01   9.50e-01     1.05e+00
           2   2.50e-01   6.40e-01   9.02e-01     1.10e+00
           5   3.12e-02   3.28e-01   7.74e-01     1.28e+00
          10   9.77e-04   1.07e-01   5.99e-01     1.63e+00
          20   9.54e-07   1.15e-02   3.58e-01     2.65e+00
          50   8.88e-16   1.43e-05   7.69e-02     1.15e+01

With w below 1 the trace of early words fades away exponentially.
At w=0.8, a word twenty positions back contributes about 1 percent.
At w=1.05, the opposite happens and the state grows without limit.

A review: 'The service, despite the long wait and the confusion over
our booking which took twenty minutes to sort out, was excellent.'

The word 'service' is 19 positions before 'excellent'. A plain
recurrent state has almost forgotten it by the time the verdict arrives.
```

| In the code | The weight | What happens over 50 words |
| --- | --- | --- |
| `0.5 ** steps` | Forgets fast | 8.9e-16, effectively nothing survives |
| `0.8 ** steps` | The value used above | 1.4e-05, the first word is gone |
| `0.95 ** steps` | Remembers longest of the stable options | 0.077, still fading |
| `1.05 ** steps` | Above 1 | 11.5 and climbing, the state explodes |
| `w ** steps` | The whole program | Same arithmetic as lesson 05, time steps for layers |

This is the vanishing gradient problem again, in a new costume. Where a deep network multiplies by small slopes across layers, a recurrent network multiplies by the recurrent weight across time steps, and a sequence of fifty words is effectively a fifty-layer network.

The columns show the bind precisely. **Below 1, early information disappears. Above 1, the state explodes.** There is no setting that both remembers a long way back and stays stable, which is why long-range dependencies were the central unsolved problem of sequence modelling for years.

The standard repair was the `LSTM`, a more elaborate cell with explicit gates deciding what to keep, what to discard, and what to expose at each step. Rather than a single multiplier applied to everything, an LSTM maintains a separate channel that information can travel along largely undisturbed, and learns when to write to it and when to read from it. It works, and it made machine translation and speech recognition practical for the first time.

![Visual explanation of rnn memory limits](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_rnn_memory_limits.png)

## Four Shapes of Sequence Problem

The examples above all read a sequence and produce one number at the end. That is one arrangement of four, and knowing the others makes it clear how flexible the loop is.

1. **Many to one.** A sequence goes in, a single answer comes out. Sentiment from a review, or a spoken command classified into an intent. Only the final state is used.

2. **One to many.** A single input produces a sequence. A caption generated from an image, where the state is initialised from the picture and then unrolled one word at a time, each output fed back in as the next input.

3. **Many to many, aligned.** One output per input, at every step. Tagging each word with its part of speech, or labelling each frame of a video. The state at step t produces the output for step t.

4. **Many to many, unaligned.** A sequence in and a sequence out, of different lengths and not in step with each other. Translation is the case that matters, since a seven-word English sentence may become a nine-word Hindi one, and the words do not line up.

The fourth shape is where the difficulty concentrated, and the standard solution was the `encoder-decoder` arrangement: one recurrent network reads the whole input and compresses it into a final state, and a second one generates the output from that state.

Notice what that design demands. **The entire meaning of the source sentence has to pass through one fixed-size vector.** A four-word sentence and a forty-word paragraph get the same number of values, and the longer the input, the more is lost in the squeeze. Translation quality was observed to fall off sharply as sentences grew, and the bottleneck was the reason.

That specific failure is what attention was originally invented to fix, before it was ever proposed as a replacement for recurrence itself.

![Visual explanation of four shapes of sequence problem](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_four_shapes_of_sequence_problem.png)

## The Other Problem: Recurrence Cannot Be Parallelised

There is a second limitation, and it has nothing to do with memory.

The state at step 20 depends on the state at step 19, which depends on step 18, and so on back to the beginning. **The steps must be computed in order.** No amount of hardware changes that, because step 20 cannot start until step 19 has finished.

This matters enormously in practice. Training a convolutional network on a batch of images computes every position simultaneously, which is exactly what graphics processors are built for. Training a recurrent network on a thousand-word document requires a thousand sequential steps, and the expensive parallel hardware sits mostly idle.

So recurrent networks carried two burdens: they struggled to remember far back, and they were slow to train in a way that better hardware could not fix.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;"></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Convolutional network</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Recurrent network</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Input shape</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed-size grid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sequence of any length</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is shared</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same filter at every position</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same weights at every time step</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sense of order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spatial adjacency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sequential, through the carried state</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long-range links</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reached by stacking layers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fade exponentially with distance</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be parallelised</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, every position at once</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No, steps must run in order</td>
    </tr>
  </tbody>
</table>

![Visual explanation of the other problem: recurrence cannot be parallelised](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_the_other_problem_recurrence_cannot_be_parallelised.png)

## Your Turn

Change `W_HIDDEN` in the first program from 0.8 to 0.3 and rerun the review.

The final reading will change, and more interestingly the "carried in" column will collapse much faster. With a low carrying weight the network becomes nearly a bag of words, since almost nothing survives from one step to the next. Then set it to 0.99 and watch the opposite: early words dominate and later ones barely register. Neither extreme is a memory; both are failures in different directions.

Then test the ordering claim properly. Construct a pair of sentences from the second program's vocabulary where you believe the recurrent reading is *wrong*, that is, where the ordering it prefers does not match how a person would read it. This is not hard to do, and finding one yourself is the fastest way to see that a single carried number is a crude model of context.

Finally, work out the sequential-computation cost. A document of 2,000 words must be processed in 2,000 dependent steps. Suppose each step takes 1 millisecond on your hardware, and you have 100,000 documents to train on for 10 passes. Compute the total time. Then work out what it would be if all 2,000 words in a document could be processed simultaneously. The gap is the second reason recurrence was abandoned, and it is larger than most people expect before doing the arithmetic.
