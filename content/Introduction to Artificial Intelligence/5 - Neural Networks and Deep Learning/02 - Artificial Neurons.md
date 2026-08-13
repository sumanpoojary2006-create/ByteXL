## Introduction

A horticulture department wants an automatic irrigation controller for its polyhouse, and the brief given to the electronics student building it is three sentences long.

Run the pump when the soil is dry. Do not run it if rain is forecast, because the beds flood. Never run it when the tank is empty, because the pump burns out.

Three sensors, each reporting yes or no, and one decision. The student's first instinct is a chain of if-statements, and that would work. Instead her supervisor asks her to build it a different way: as a single unit that adds up its three inputs, each multiplied by a number saying how much that input counts, and switches the pump on if the total clears a threshold.

It sounds like a needlessly indirect way to write three conditions, and for this problem it is. The reason to learn it is that the same unit, with different numbers, decides something else entirely, and nothing about the unit has to be rewritten to make that happen. That unit is the **artificial neuron**.

**Definition:** An `artificial neuron` computes a weighted sum of its inputs, adds a `bias`, and passes the result through an `activation function` to produce an output, so that its entire behaviour is determined by the numbers on its connections rather than by its structure.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_introduction.png)

## The Four Parts

Everything in the rest of this unit is built from a component with exactly four pieces.

1. **Inputs.** The numbers coming in. For the controller these are three sensor readings, each 0 or 1.
2. **Weights.** One number per input, saying how strongly that input counts and in which direction. A positive weight pushes towards firing, a negative weight pushes against it.
3. **Bias.** A single number added to the total regardless of the inputs. It sets how much evidence the neuron demands before it fires.
4. **Activation function.** The rule turning the total into an output. Here it is a threshold: fire if the total is above zero.

Written as a formula, with inputs x and weights w:

**output = activation( w₁x₁ + w₂x₂ + w₃x₃ + bias )**

The weights carry the direction of each influence, matching the excitatory and inhibitory connections from biology. Soil being dry should encourage watering, so its weight is positive. Rain being forecast should discourage it, so its weight is negative.

![Visual explanation of artificial neuron parts](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_artificial_neuron_parts.png)

## The Controller as One Neuron

The three-sentence brief becomes three weights and a bias.

Reading the code below: `neuron` is five lines and contains the entire idea. Everything else is a loop over the eight possible sensor combinations, printing a truth table. `product([0, 1], repeat=3)` is just a compact way to generate 000, 001, 010 and so on.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjpxw" 
 width="100%"
></iframe>

```
 soil_dry  rain  tank  weighted sum   pump
--------------------------------------------
        0     0     0          -1.5    off
        0     0     1          -0.5    off
        0     1     0          -2.5    off
        0     1     1          -1.5    off
        1     0     0          -0.5    off
        1     0     1           0.5     ON
        1     1     0          -1.5    off
        1     1     1          -0.5    off

The pump runs in exactly one of the eight situations:
  soil dry, no rain expected, water in the tank
```

| In the code | Which of the four parts | In the brief |
| --- | --- | --- |
| `inputs` | The inputs | The three sensor readings |
| `"soil_dry": 1.0` | A positive weight | "Run the pump when the soil is dry" |
| `"rain_forecast": -1.0` | A negative weight | "Do not run it if rain is forecast" |
| `BIAS = -1.5` | The bias | How much evidence is demanded before firing |
| `1 if total > 0 else 0` | The activation function | The pump is on or off, nothing in between |

Eight possible situations, and the neuron gets all eight right. The supervisor's three sentences are now three numbers and a threshold.

The weighted sum column is where the behaviour is visible. Watch the two rows that differ only in the rain sensor. With soil dry and water in the tank and no rain, the total is 0.5 and the pump runs. Switch the rain forecast on and its weight of minus one drags the total to minus 0.5, and the pump stops. **The negative weight is doing the work of the word "unless" in the brief.**

Notice too how close the decisions are. The winning case clears the threshold by 0.5, and three separate losing cases fall short by exactly 0.5. The neuron is not confidently right; it is barely right, and that margin will matter when the numbers stop being chosen by hand.

![Visual explanation of the controller as one neuron](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_the_controller_as_one_neuron_simple_v2.png)

## The Same Neuron, Different Behaviour

The claim worth testing is that this unit is general. Keep the structure identical, change only the numbers, and see what else it can do.

Reading the code below: `neuron` is now three lines and takes its weights and bias as arguments rather than reading them from globals. That single change is what lets the `gates` dictionary hold four completely different behaviours while calling the same function.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjq96" 
 width="100%"
></iframe>

```
The same neuron, four different pairs of weights

 x1  x2                   AND                    OR                  NAND   NOT x1 (ignores x2)
-----------------------------------------------------------------------------------------------
  0   0                     0                     0                     1                     1
  0   1                     0                     1                     1                     1
  1   0                     0                     1                     1                     0
  1   1                     1                     1                     0                     0

Nothing about the neuron changed. Only the weights and the bias did.
```

| In the code | What changed | What it produces |
| --- | --- | --- |
| `([1.0, 1.0], -1.5)` | Nothing but the numbers | AND |
| `([1.0, 1.0], -0.5)` | Only the bias, versus AND | OR |
| `([-1.0, -1.0], 1.5)` | Both signs flipped | NAND |
| `([-1.0, 0.0], 0.5)` | One weight set to zero | An input ignored entirely |
| `def neuron(weights, bias, inputs)` | Weights passed in, not fixed | One function serving all four |

Four different logical functions from one six-line function. The `neuron` definition never changed; only what was passed to it.

This is the property the whole field rests on, and it is worth stating carefully. **The neuron's structure is fixed and its behaviour is entirely in its numbers.** That is what makes learning possible: if behaviour lived in the structure, a system could only change what it does by rewriting itself, whereas numbers can be adjusted a little at a time in response to being wrong.

The fourth column is a small point with a consequence. Its weight on x2 is zero, so x2 is ignored completely. A weight of zero is how a neuron says a particular input is irrelevant, and a network that sets many weights near zero during training is telling you which of your features did not matter.

![Visual explanation of the same neuron, different behaviour](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_the_same_neuron_different_behaviour_simple_v2.png)

## When the Inputs Are Not Just 0 and 1

Every input so far has been a sensor answering yes or no, which kept the arithmetic easy to follow and is not the normal case. Inputs are usually measurements: a soil moisture reading of 23 percent, a temperature of 31 degrees, a tank level of 140 litres.

Nothing in the neuron changes. The weighted sum works the same way on 23 as on 1. What changes is the meaning of a weight, and it becomes considerably more slippery.

With binary inputs, a weight of 1.0 meant "this counts for one point when present". With a moisture reading, a weight of 1.0 means "each percentage point of moisture adds one to the total", which is an entirely different kind of statement. A weight is now **the amount the total changes per unit of that input**, and the size of a unit is whatever the measuring instrument happened to use.

That has a consequence that catches people out repeatedly. Suppose the controller takes soil moisture as a percentage from 0 to 100, and tank level in litres from 0 to 500. Give both a weight of 1.0 and the tank level dominates every decision, not because it matters more but because it is measured in larger numbers. Switch the tank to cubic metres and the same neuron behaves completely differently, having been given identical information.

The repair is the one that appeared in the clustering and nearest-neighbour work earlier in this course: **rescale the inputs to comparable ranges before they reach the neuron**. Divide the moisture by 100 and the tank by 500 and both arrive between 0 and 1, at which point the weights can be compared with each other and mean something.

There is a second consequence worth noticing. With binary inputs, the weighted sum takes only a handful of possible values, which is why the eight-row table above could be written out completely. With continuous inputs it takes any value at all, so the neuron's behaviour can no longer be tabulated and has to be reasoned about geometrically instead, as a boundary somewhere in the space of possible readings.

![Visual explanation of when the inputs are not just 0 and 1](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_when_the_inputs_are_not_just_0_and_1_simple_v2.png)

## What the Bias Really Does

The bias is the piece students most often treat as a technicality. It is not; it is the neuron's threshold, and moving it alone changes what the unit computes.

Reading the code below: the weights are frozen at `[1.0, 1.0]` and never touched. The loop tries four biases, and the `if` chain in the middle simply looks at the four outputs and names the familiar gate they match. No learning, no arithmetic beyond the neuron itself.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjqn8" 
 width="100%"
></iframe>

```
Same weights [1.0, 1.0]. Only the bias moves.

  bias  (0,0)  (0,1)  (1,0)  (1,1)   behaves as
----------------------------------------------------
   0.5     1    1    1    1     always on
  -0.5     0    1    1    1     OR
  -1.5     0    0    0    1     AND
  -2.5     0    0    0    0     always off

The bias sets how much evidence the neuron demands before it fires.
```

| In the code | Bias | Evidence demanded |
| --- | --- | --- |
| `0.5` | Positive | None; the neuron fires with no inputs at all |
| `-0.5` | Small demand | Any one input is enough, which is OR |
| `-1.5` | Larger demand | Both inputs needed, which is AND |
| `-2.5` | Beyond reach | No combination can supply it, so it never fires |

Identical weights throughout. The bias alone takes the neuron from firing always, through OR, through AND, to never firing.

Read it as a demand for evidence. At minus 0.5 the neuron needs one input active. At minus 1.5 it needs two. Push the demand beyond what any input combination can supply and it never fires; remove the demand entirely and it always does.

This is why a neuron without a bias is crippled. With no bias the total is zero whenever every input is zero, so the neuron is forced to output the same thing for the all-zero input no matter what its weights are. The bias is what lets the boundary sit somewhere other than through the origin, and every practical neuron has one.

![Visual explanation of weights bias behavior](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_weights_bias_behavior.png)

## Artificial Neuron at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Part</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it is</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In the controller</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Set by</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Input</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A number arriving from data or another neuron</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Three sensor readings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Weight</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How much an input counts, and in which direction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">+1 for dry soil, -1 for rain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learning, in every later lesson</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Bias</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How much total evidence is demanded</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">-1.5, so two positives are needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learning, alongside the weights</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Activation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The rule turning the total into an output</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fire if the total exceeds zero</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The designer, from a small menu</td>
    </tr>
  </tbody>
</table>

The right-hand column is the part to carry forward. Two of the four are learned from data, and that is the entire subject of the next several lessons.

![Visual explanation of artificial neuron at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_artificial_neuron_at_a_glance.png)

## Your Turn

The polyhouse adds a fourth sensor reporting whether it is currently daytime, because watering in full sun wastes water to evaporation.

Extend the controller so the pump runs only when the soil is dry, no rain is forecast, the tank has water, and it is not the middle of the day. Choose the fourth weight and adjust the bias, then print all sixteen combinations and check every one. Getting the bias right is the fiddly part, and doing it by hand once is exactly the point, because it shows you what the training procedure will later be doing for you.

Then try to build something the neuron cannot do. Set yourself the target of firing when exactly one of two inputs is active, and not when both are and not when neither is. Try several weight and bias combinations and record what happens. You will not succeed, and the reason is not a lack of cleverness on your part. Write down what pattern you notice about which cases you can and cannot separate.

Finally, take the weighted sum seriously as a sentence. Write the controller's rule out in words as "fire when one point for dry soil, minus one point for rain, plus one point for water, totals more than one and a half points". Then explain what changing the rain weight from minus one to minus three would mean in that sentence, and confirm your explanation by running it. Being able to move between the numbers and their meaning is what makes weights readable, and it is a skill that stops working in large networks, which is worth knowing in advance.
