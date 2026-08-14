## Introduction

A postgraduate student in Coimbatore is asked to build a system that reads handwritten pin codes off envelopes, and she starts the way she was taught: work out what each connection should weigh, then write the numbers in.

She gets as far as the second layer before stopping. The network she has sketched has a hundred and twelve thousand weights. At the irrigation controller's three, or the XOR network's nine, a person can reason each number out from what the system is supposed to do. At a hundred thousand there is nothing to reason from, and no amount of care makes the twelfth weight in the fourth layer a thing anyone can argue about.

So the weights have to be found rather than chosen, and the network has to find them itself, from examples, starting from nothing but random values. That process has three parts: a way of measuring how wrong the network currently is, a way of working out which direction each weight should move, and a way of pushing the blame for a mistake back through every layer that contributed to it.

**Definition:** `Training` a neural network means repeatedly measuring its error with a `loss function`, computing how each weight affects that error, and adjusting every weight a little in the direction that reduces it, using `gradient descent` driven by `backpropagation` to distribute the error across all layers.

![A postgraduate student confronts the impossibility of setting 112,000 neural-network weights by hand](images/06_section_introduction_v2.png)

## The Loss Function

Before anything can improve, being wrong has to become a number.

A `loss function` takes the network's predictions and the correct answers and returns a single value, low when the network is doing well and high when it is not. For predicting a quantity, the usual choice is the mean of the squared differences, which punishes large misses disproportionately and is never negative.

The useful way to picture it is as a landscape. Every possible setting of the weights is a location, and the loss at that location is the height. Training means walking downhill.

With a single weight the landscape is a curve, and it can be printed.

Reading the code below: there is no network and no training. `loss` is the only function, and it answers one question: if the model were "minutes equals weight times kilometres", how badly would this particular weight fit the four deliveries. The rest of the program calls it at thirteen different weights and draws a bar chart.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjwqt" 
 width="100%"
></iframe>

```
Loss for different values of the single weight

  weight       loss
--------------------
     0.0     485.03
     0.5     337.33
     1.0     216.38
     1.5     122.19
     2.0      54.73
     2.5      14.03
     3.0       0.09
     3.5      12.89
     4.0      52.44
     4.5     118.74
     5.0     211.79
     5.5     331.59
     6.0     478.14

The same numbers, drawn (each row is one weight, bar length is loss)

  0.0 |##################################################
  0.5 |##################################
  1.0 |######################
  1.5 |############
  2.0 |#####
  2.5 |#
  3.0 |
  3.5 |#
  4.0 |#####
  4.5 |############
  5.0 |#####################
  5.5 |##################################
  6.0 |#################################################

Lowest loss is at weight 3.01, where the loss is 0.079
The curve is a valley, and training means walking down it.
```

| In the code | What it is | Note |
| --- | --- | --- |
| `weight * km` | The entire model | One weight, no bias, no activation |
| `(... - mins) ** 2` | Squared error on one delivery | Direction of the miss stops mattering |
| `/ len(DATA)` | The mean | Makes the number independent of dataset size |
| `loss(w)` across a range | The landscape | Position is the weight, height is the loss |
| `min(..., key=loss)` | Brute-force search | Works here only because there is one weight |

A clean valley with its floor near 3, which makes sense because the deliveries take roughly three minutes per kilometre.

Two features of that shape are what make training possible at all.

**It slopes.** At any weight other than the best one, the loss is higher on one side and lower on the other, so there is always a direction to move.

**The slope points at the answer.** Far from the bottom, at a weight of 0, the curve is steep. Near the bottom it is nearly flat. The steepness itself says both which way to go and how far.

Note also that the loss never reaches zero, bottoming at 0.079. The four deliveries do not lie exactly on a straight line, so no single weight fits them perfectly, and that residual is the data's noise rather than the model's failure.

![Visual explanation of loss gradient descent](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_loss_gradient_descent.png)

## Gradient Descent

The procedure follows directly. Measure the slope at the current weight, take a step downhill proportional to it, and repeat.

The size of the step is the slope multiplied by the `learning rate`, a small number set by you.

Reading the code below: `loss` is unchanged from the previous block and is only printed, never used to decide anything. The whole of gradient descent is the two lines at the end of the loop: compute `g`, then `weight -= rate * g`. `slope` is the derivative of `loss`, and you can take it as given.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjx2z" 
 width="100%"
></iframe>

```
Gradient descent from a weight of 0.0

 step   weight       loss      slope     move
----------------------------------------------
    0    0.000    485.035   -322.150    1.611
    1    1.611    104.938   -149.800    0.749
    2    2.360     22.752    -69.657    0.348
    3    2.708      4.981    -32.390    0.162
    4    2.870      1.139    -15.062    0.075
    5    2.945      0.308     -7.004    0.035
    6    2.980      0.128     -3.257    0.016
    7    2.997      0.090     -1.514    0.008
    8    3.004      0.081     -0.704    0.004
    9    3.008      0.079     -0.327    0.002
   10    3.009      0.079     -0.152    0.001
   11    3.010      0.079     -0.071    0.000
   12    3.010      0.079     -0.033    0.000

Settled at weight 3.011, loss 0.0788

The slope tells the weight which way to move and how urgently.
As the valley floor approaches, the slope shrinks and so do the steps.
```

| In the code | What it is | Note |
| --- | --- | --- |
| `slope(weight)` | The gradient | Positive means uphill to the right |
| `rate = 0.005` | The learning rate | The only setting, and the only way to break this |
| `weight -= rate * g` | The whole of gradient descent | Minus, because the goal is downhill |
| The `move` column | `-rate * g` | Shrinks on its own as the slope flattens |
| `loss(weight)` | Printed, never used | Descent needs only the slope, not the loss itself |

Thirteen steps from knowing nothing to the right answer.

Read the two right-hand columns together. The slope starts at −322 and the first move is a leap of 1.611. By step 8 the slope is −0.70 and the move is 0.004. **The procedure slows down automatically as it approaches the bottom**, because the same formula that says "go this way" also says "and there is not much further to go". Nobody schedules that.

The learning rate is the one setting, and both directions of getting it wrong are instructive. Too small and the steps are tiny, so the same journey takes thousands of iterations. Too large and a step can overshoot the valley floor and land higher up the far side, after which the next step overshoots back, and the loss oscillates or grows without limit.

One honest qualification. This valley has a single lowest point, so descending always arrives there. A real network's loss landscape has thousands of dimensions and many separate hollows, and gradient descent finds whichever one it happens to fall into. That it usually finds a good enough hollow is an empirical fact rather than a guarantee.

![Visual explanation of gradient descent](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_gradient_descent_simple_v2.png)

## Backpropagation

For one weight, the slope was a formula. For a network, there is a difficulty: the weights in the first layer affect the loss only indirectly, through everything the later layers do afterwards. Working out how much a first-layer weight is to blame for an error at the output requires tracing responsibility backwards through the whole network.

`Backpropagation` is the procedure that does this efficiently, and the idea behind it is simpler than its reputation.

1. **Run the input forward** and record what every neuron produced along the way.
2. **Compute the error at the output**, which is straightforward because the correct answer is known there.
3. **Pass the blame back one layer.** A hidden neuron's share of the error is the error of the neuron it fed, multiplied by the weight connecting them, since a strong connection means more responsibility.
4. **Scale by responsiveness.** Multiply by how steep that neuron's activation currently is, because a saturated neuron could not have helped.
5. **Repeat backwards** through every layer, then adjust every weight by its own share.

That is the whole thing. It is bookkeeping, applied consistently, and the reason it is efficient is that each layer's blame is computed once and reused for every weight in it, rather than recalculating from scratch.

Putting all three pieces together trains the XOR network that had to be hand-designed two lessons ago.

Reading the code below: `forward` is the two-layer network from lesson 04, with sigmoid activations. The nine weights start random. Inside the training loop, the five lines from `d_out` to `b_hidden[j] -= ...` are backpropagation, and each factor in those products corresponds to one numbered step in the list above. Everything else is printing progress.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjxcw" 
 width="100%"
></iframe>

```
Training a 2-2-1 network on XOR, starting from random weights

  epoch      loss   predictions for (0,0) (0,1) (1,0) (1,1)
------------------------------------------------------------------
      0   0.25895   0.404  0.400  0.410  0.405
   2500   0.00155   0.044  0.963  0.962  0.039
   5000   0.00063   0.028  0.976  0.976  0.025
   7500   0.00039   0.022  0.981  0.981  0.019
  10000   0.00028   0.018  0.984  0.984  0.017
  12500   0.00022   0.016  0.986  0.986  0.015
  15000   0.00018   0.015  0.987  0.987  0.013
  17500   0.00015   0.014  0.988  0.988  0.012
  20000   0.00013   0.013  0.989  0.989  0.011

Rounded to a decision:
  (0, 0) -> 0  (wanted 0)
  (0, 1) -> 1  (wanted 1)
  (1, 0) -> 1  (wanted 1)
  (1, 1) -> 0  (wanted 0)

Nobody chose these weights. The network found them from four examples.
```

| In the code | Which factor | What it means |
| --- | --- | --- |
| `(output - target)` | The error | How wrong this prediction was, and in which direction |
| `output * (1 - output)` | Responsiveness | The slope of sigmoid; near zero if saturated |
| `* w_out[j]` | The connection | A strong connection carries more of the blame |
| `* hidden[j] * (1 - hidden[j])` | The hidden neuron's slope | A saturated hidden neuron could not have helped |
| `-= RATE * d_out * hidden[j]` | The weight update | Gradient descent, one weight at a time |
| `rng.uniform(-1, 1)` | Random start | Identical weights would learn identically forever |

This is the payoff for the whole unit so far, and the first row is worth dwelling on.

At epoch 0 the network outputs roughly 0.4 for all four inputs. It is not wrong in an interesting way; it is producing nearly the same answer regardless of input, which is what random weights give you. By epoch 2500 the pattern is essentially learned, and the remaining epochs are polishing.

Nothing in that code knows what XOR is. It knows four examples and a rule for reducing error, and the nine numbers it ends with are a solution to the problem that stopped the perceptron dead.

The five lines doing the real work are the two starting `d_out` and `d_hidden`. Compare them against the backpropagation steps listed above: `(output - target)` is the error, `* output * (1 - output)` is the responsiveness of a sigmoid, `* w_out[j]` passes the blame along the connection, and `* hidden[j] * (1 - hidden[j])` scales it by the hidden neuron's own responsiveness. Every step of the procedure is one factor in a product.

![Visual explanation of backpropagation](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_backpropagation.png)

## Training at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Piece</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Goes wrong when</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Loss function</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Turns being wrong into one number to minimise</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It measures something other than what you care about</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Gradient</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Says which way each weight should move and how urgently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Activations saturate, so it vanishes before reaching early layers</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Learning rate</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scales every step</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too small crawls; too large overshoots and diverges</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Backpropagation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Distributes blame back through every layer efficiently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nothing, in itself; it is exact bookkeeping</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Random start</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Breaks symmetry so neurons learn different things</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An unlucky start lands in a poor hollow</td>
    </tr>
  </tbody>
</table>

The last row is not hypothetical, as the exercise below demonstrates.

![Visual explanation of training at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_section_training_at_a_glance.png)

## Your Turn

Change the seed in the XOR program from 1 to 4 and run it again.

The loss will fall to about 0.125 and stop, and one of the four cases will come out wrong. Nothing about the code changed, only where the random weights started. The network has descended into a hollow that is lower than everywhere nearby and is not the bottom of the landscape, and gradient descent has no way to climb out. Record what the four predictions look like when this happens, because recognising a stalled training run by the shape of its output is a genuinely useful skill.

Then find out how common it is. Wrap the training in a loop over seeds 0 to 19, and count how many converge to a loss below 0.01. You will get a proportion rather than always or never, and that proportion is the honest answer to "does this work". It is also why practitioners train several times and keep the best result.

Then break it the other way. Set `RATE` to 5.0 and watch the loss. Then set it to 0.01 and see how far 20,000 epochs gets you. Neither the learning rate nor the seed is a detail.

Finally, reason about a case with no code. Initialise every weight and bias to exactly zero instead of random values, and work out on paper what the two hidden neurons will compute on the first forward pass, and what corrections each will receive. If you conclude that they will always be identical to each other forever, you have found the reason random initialisation is required rather than merely conventional.
