## Introduction

A lab demonstrator in Warangal sets her class four points on a sheet of graph paper and asks them to draw one straight line with the two circles on one side and the two crosses on the other. She has done this every year for six years. Every year somebody spends most of the hour convinced they are nearly there.

Nobody has ever managed it, because it cannot be done. The four points are XOR, and the exercise exists so that the next thing she says lands properly: the fix is not a better line.

The way out is more modest than students expect. A single neuron can compute OR. A single neuron can compute NAND. Neither is XOR. But look at what OR and NAND say together: OR is true when at least one input is on, and NAND is true unless both are on. Both are true in exactly the cases where exactly one input is on, which is XOR.

So the answer is not a cleverer line. It is to let one neuron look at what other neurons have already worked out. The first two draw their own lines; a third asks whether both said yes.

That arrangement, neurons in layers where each layer's outputs become the next layer's inputs, is a **feedforward neural network**, and it removes the perceptron's ceiling entirely.

**Definition:** A `feedforward neural network` arranges neurons in successive `layers`, where every neuron in a layer receives the outputs of the previous layer as its inputs, and information flows in one direction from input to output with no loops.

![Warangal students try and fail to separate diagonally arranged circles and crosses with one straight line](images/04_section_introduction_v2.png)

## Solving XOR With Two Layers

The construction is exactly the one the exercise suggested.

Reading the code below: `neuron` is the same three-line function from the previous two lessons. The only new idea is in the loop, two lines long. `hidden` runs both first-layer neurons on the raw inputs, and `out` runs the third neuron on their results rather than on x1 and x2. Nothing is trained; all nine numbers were worked out by hand.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjren" 
 width="100%"
></iframe>

```
A two-layer network computing XOR

 x1  x2 |  h1 (OR)  h2 (NAND) |  output  wanted
--------------------------------------------------
  0   0 |        0          1 |       0       0
  0   1 |        1          1 |       1       1
  1   0 |        1          1 |       1       1
  1   1 |        1          0 |       0       0

4 of 4 correct. A single neuron could manage only 3.
```

| In the code | Which layer | What it does |
| --- | --- | --- |
| `HIDDEN[0]` = `([1.0, 1.0], -0.5)` | Hidden | OR, the same weights as the previous lesson |
| `HIDDEN[1]` = `([-1.0, -1.0], 1.5)` | Hidden | NAND |
| `OUTPUT` = `([1.0, 1.0], -1.5)` | Output | AND, applied to the two hidden results |
| `neuron(w, b, (x1, x2))` | Hidden | Reads the raw inputs |
| `neuron(OUTPUT[0], OUTPUT[1], hidden)` | Output | Reads `hidden`, never the raw inputs |

The two hidden columns are the interesting part, and they show what a layer is really for.

The network was never given a way to draw a curved boundary. Each of its three neurons still draws exactly one straight line, as every neuron always will. What changed is that the output neuron is not looking at x1 and x2 at all. It is looking at h1 and h2, and **in the space of h1 and h2 the problem has become linearly separable**.

Check the middle two rows against the outer two. In terms of the original inputs, the two cases wanting an output of 1 sit on opposite corners. In terms of the hidden values, both become (1, 1), while the two cases wanting 0 become (0, 1) and (1, 0). The hidden layer has moved the four points to new positions where one line suffices.

That is the whole idea of a hidden layer, and it is worth stating plainly. **A hidden layer re-describes the input in terms that make the remaining problem easier.** Later lessons will call this learning a representation, and it is the same thing seen here at the smallest possible scale.

![Visual explanation of feedforward xor](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_feedforward_xor.png)

## Anatomy of a Network

The vocabulary is straightforward once the XOR example is in hand.

- **The input layer** is the raw features. It does no computation and is often not counted as a layer at all.
- **Hidden layers** sit between input and output. They are called hidden because nothing outside the network observes their values.
- **The output layer** produces the final answer, with one neuron for a yes-or-no decision or one per class for a multi-class problem.
- **The width** of a layer is how many neurons it has; the **depth** of a network is how many layers.
- **Fully connected** means every neuron in a layer receives every output from the previous one, which is the default arrangement.

Two facts about size are worth knowing early. A network with one hidden layer, given enough neurons in it, can approximate essentially any continuous function to whatever accuracy you like. This is a genuine mathematical result and it is much less useful than it sounds, because it says nothing about how many neurons "enough" is, and nothing about whether training will ever find the right weights. In practice, several narrow layers usually work far better than one enormously wide one, and understanding why is most of what the rest of this unit is about.

![Visual explanation of anatomy of a network](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_anatomy_of_a_network.png)

## Forward Propagation

Running data through the network is called `forward propagation`, and the code makes clear how repetitive it is.

Reading the code below: `NETWORK` is a list of layers, each layer a list of `(weights, bias)` pairs, and it is pure data with no meaning attached. `forward` is six lines. The single variable `signal` carries the values from one layer to the next, and reassigning it at the end of each pass is the whole mechanism of a feedforward network.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjrtw" 
 width="100%"
></iframe>

```
Forward propagation, one layer at a time
  input    [1.0, 0.5, -1.0]
  layer 1: sums [0.35, -0.35, 1.6]
           out  [0.587, 0.413, 0.832]
  layer 2: sums [1.089]
           out  [0.748]

Network output: 0.7482

Every layer does the same thing: weighted sums, then an activation.
The only difference is that layer 2's inputs are layer 1's outputs.
```

| In the code | What it is | Note |
| --- | --- | --- |
| `NETWORK` | The whole model | A nested list of numbers, nothing more |
| `([0.8, -0.5, 0.3], 0.1)` | One neuron | Three weights because the input has three values |
| `signal = inputs` | The running values | Starts as the data, becomes each layer's output in turn |
| `totals` | The weighted sums | One per neuron in the current layer |
| `signal = [sigmoid(t) ...]` | The activation, then handover | The one line that chains layers together |
| `sigmoid(z)` | A smooth squash into 0 to 1 | Why the output is 0.748 and not a bare 1 |

Three observations about that function, because it is the core of every neural network.

**The loop body is identical for every layer.** Weighted sums, then an activation, then hand the results on. A network of two layers and a network of two hundred run the same three lines a different number of times.

**The network is data, not code.** `NETWORK` is a nested list of numbers. The `forward` function knows nothing about irrigation, students, or XOR, and would run a network for any of them unchanged. This is what makes training possible: learning means altering that nested list.

**The activation here is a smooth curve rather than a hard threshold.** `sigmoid` squashes any number into the range 0 to 1, so the output is 0.748 rather than a bare 1. That smoothness is not a stylistic choice, and the reason will decide the whole of the next two lessons.

![Visual explanation of forward propagation weights](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_forward_propagation_weights.png)

## Why an Activation Function Is Not Optional

It is natural to wonder whether the activation is needed at all. It seems to complicate a perfectly good weighted sum. Removing it answers the question decisively.

Reading the code below: this is the XOR network from the top of the lesson with exactly one change. `linear_neuron` returns the weighted sum directly instead of thresholding it. The weights, the biases, and the two-layer structure are untouched. The printed algebra at the end is text, worked out by hand, showing why the result was inevitable.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjs5p" 
 width="100%"
></iframe>

```
The same two-layer network, with the threshold removed from every neuron

 x1  x2 |      h1      h2 |   output  wanted
----------------------------------------------
  0   0 |    -0.5     1.5 |     -0.5       0
  0   1 |     0.5     0.5 |     -0.5       1
  1   0 |     0.5     0.5 |     -0.5       1
  1   1 |     1.5    -0.5 |     -0.5       0

The output is -0.5 for every single input. The network has collapsed.

Working out why, by hand:
  h1 = x1 + x2 - 0.5
  h2 = -x1 - x2 + 1.5
  out = h1 + h2 - 1.5
      = (x1 + x2 - 0.5) + (-x1 - x2 + 1.5) - 1.5
      = -0.5        <- every x1 and x2 term cancels
```

| In the code | Changed from the XOR version? | Effect |
| --- | --- | --- |
| `HIDDEN`, `OUTPUT` | Unchanged | Same nine numbers |
| Two-layer structure | Unchanged | Still hidden layer then output layer |
| `return bias + sum(...)` | Changed: no `1 if ... else 0` | The only edit in the entire program |
| The output column | Constant at -0.5 | Four different inputs, one answer |

Same weights, same structure, same two layers. Without the activation the network outputs the same number for every possible input, and the algebra at the bottom shows it was inevitable rather than unlucky.

The general result is more important than this particular cancellation. **A weighted sum of weighted sums is itself just a weighted sum.** Stack a hundred layers with no activation between them and the whole thing collapses algebraically into a single layer, capable of exactly what one neuron was capable of and no more. Every layer you added was wasted.

So the activation function is what makes depth mean anything. Without it, layers are decoration. With it, each layer can bend the space in a way the next layer can build on, which is why the XOR network worked with thresholds and failed without them.

![Visual explanation of why an activation function is not optional](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_why_an_activation_function_is_not_optional_simple_v2.png)

## Counting the Weights

The XOR network has three neurons and nine numbers in it: two weights and a bias each for the hidden pair, and two weights and a bias for the output. Small enough to write on a napkin.

That does not stay true. In a fully connected layer, every neuron receives every output from the layer before, so the weight count between two layers is the product of their widths, plus one bias per neuron.

| Network | Layer widths | Weights and biases |
| --- | --- | --- |
| The XOR network | 2, 2, 1 | 9 |
| A small tabular model | 10, 32, 16, 1 | 897 |
| A modest image classifier | 784, 128, 64, 10 | 109,386 |
| One layer of a large language model | 4096, 4096 | about 16.8 million |

The third row is worth pausing on, because it is a genuinely small network by modern standards. The input width of 784 is a 28 by 28 pixel image flattened into a list, and connecting it to a first hidden layer of 128 neurons already costs 100,352 weights before anything else exists.

Two consequences follow directly, and they shape the rest of this unit.

**Parameters demand data.** Every weight is a number to be determined from examples. A model with a hundred thousand parameters trained on a thousand images has far more freedom than the evidence can pin down, and will memorise rather than learn, which is the overfitting problem in its neural form.

**Width is expensive and depth is cheap.** Compare a network of 784, 512, 10 against one of 784, 64, 64, 64, 10. The first has roughly 407,000 parameters and the second roughly 59,000, and the deeper one is frequently the better model. This is the practical reason the field went deep rather than wide, and why the theoretical result about one wide layer being sufficient matters so little in practice.

There is also a structural point hiding in the arithmetic. The 784 by 128 connection treats every pixel as unrelated to every other, so a photograph shifted one pixel to the right presents an almost entirely different input. Nothing in a fully connected layer knows that neighbouring pixels belong together, and later architectures in this unit exist largely to fix that.

![Visual explanation of counting the weights](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_counting_the_weights_simple_v2.png)

## Feedforward Networks at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In the XOR network</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Input layer</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The raw features; computes nothing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">x1 and x2</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Hidden layer</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Re-describes the input for the next layer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two neurons computing OR and NAND</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Output layer</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Produces the answer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One neuron computing AND</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Forward propagation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Running data through, layer by layer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inputs to hidden values to output</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Activation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What stops layers collapsing into one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The threshold; removing it gave -0.5 everywhere</td>
    </tr>
  </tbody>
</table>

![Visual explanation of feedforward networks at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_feedforward_networks_at_a_glance.png)

## Your Turn

Add a third input to the XOR network so it computes whether an odd number of three inputs are on.

Start by working out the truth table for all eight combinations, then decide how many hidden neurons you need and what each should detect. This is genuinely harder than two-input XOR and the difficulty is the lesson: hand-designing weights stops being feasible almost immediately, which is precisely why the weights must be learned rather than chosen.

Then run an experiment on the general `forward` function. Add a third layer to `NETWORK` and pass an input through, checking that the code needs no modification at all. Then set every neuron's weights in the second layer to zero and see what reaches the output. A layer of zeros blocks everything downstream regardless of how good the other layers are, which is worth having seen before you meet the training problems it causes.

Finally, prove the collapse for yourself rather than accepting the demonstration. Take any two-layer network with no activation, write the output as an algebraic expression in x1 and x2, and simplify it. You will always be able to reduce it to a single weighted sum plus a constant. Then explain, in one sentence, why adding more layers cannot help.
