## Introduction

The irrigation controller worked because somebody had already written the rule down in three sentences, and the weights were read off from those sentences by hand.

That is not the interesting case. The interesting case is a college's examinations office, which has records of five hundred students, how many hours a week each studied, their attendance, and whether they passed. Nobody has written a rule. There is no brief saying "pass if hours exceed six unless attendance is below fifty". If such a rule exists at all, it is buried in the records.

What is needed is a procedure that starts with no idea, looks at the examples one at a time, and adjusts its own weights whenever it gets one wrong. Run it long enough and the weights it settles on are the rule, discovered rather than supplied.

That procedure is the **perceptron**, and it was the first learning algorithm for a neuron.

**Definition:** A `perceptron` is a single artificial neuron together with a learning rule that adjusts its weights and bias in response to its own mistakes, converging on a `decision boundary` that separates two classes whenever such a straight boundary exists.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_introduction.png)

## The Learning Rule

The rule is remarkably short. For each training example: make a prediction, compare it with the correct answer, and if they differ, nudge every weight in the direction that would have helped.

Written out:

- **error = target minus prediction.** This is 0 when correct, +1 when the neuron should have fired and did not, and −1 when it fired and should not have.
- **Each weight changes by** learning rate × error × that input's value.
- **The bias changes by** learning rate × error.

Three properties of this make it work, and each is worth seeing.

**Nothing happens when the prediction is right.** The error is zero, so every update is zero. The perceptron only learns from mistakes.

**The direction is always corrective.** If the neuron failed to fire when it should have, the error is +1 and every weight on an active input goes up, making that same input more likely to trigger firing next time. If it fired wrongly, the error is −1 and those weights go down.

**Only active inputs are changed.** The update is multiplied by the input value, so an input of zero produces no change to its weight. The neuron adjusts only the connections that actually contributed to the mistake.

Reading the code below: `predict` is the neuron from the previous lesson, unchanged. Everything new is in the three lines under `if error != 0`, which are the learning rule written out literally. The outer loop counts epochs and the inner loop walks the four examples.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjnj5" 
 width="100%"
></iframe>

```
Learning the AND gate from four examples, starting from all zeros

  epoch 1: 1 mistake(s), weights [0.1, 0.1], bias 0.1
  epoch 2: 3 mistake(s), weights [0.2, 0.1], bias 0.0
  epoch 3: 3 mistake(s), weights [0.2, 0.1], bias -0.1
  epoch 4: 2 mistake(s), weights [0.2, 0.2], bias -0.1
  epoch 5: 1 mistake(s), weights [0.2, 0.1], bias -0.2
  epoch 6: 0 mistake(s), weights [0.2, 0.1], bias -0.2

Converged after 6 epochs. No example is misclassified.

Final check:
  (0, 0) -> 0 (wanted 0)
  (0, 1) -> 0 (wanted 0)
  (1, 0) -> 0 (wanted 0)
  (1, 1) -> 1 (wanted 1)
```

| In the code | What it is | Note |
| --- | --- | --- |
| `weights = [0.0, 0.0]` | The starting point | The perceptron begins knowing nothing |
| `error = target - guess` | The signal to learn from | Exactly 0, +1, or -1 |
| `if error != 0` | Learn only from mistakes | Correct predictions change nothing |
| `LEARNING_RATE * error * x[i]` | The weight update | Direction from `error`, size from the rate, gated by `x[i]` |
| `LEARNING_RATE * error` | The bias update | Same rule with the input treated as always 1 |
| `mistakes` | Errors this epoch | The number to watch; zero means done |

The AND gate whose weights were handed over in the previous lesson has now been discovered from four examples, starting from nothing.

An `epoch` is one pass through all the training examples, and the count of mistakes per epoch is the thing to watch. Notice it does not fall smoothly: 1, then 3, then 3, then 2, then 1, then 0. **Getting worse before getting better is normal**, because fixing one example can break another, and the rule has no way to see that coming.

The final weights, 0.2 and 0.1 with a bias of −0.2, are not the weights the previous lesson used. They are a different solution to the same problem, and both are correct. **There is no unique right answer**, only a set of weight combinations that separate the classes, and the perceptron stops at whichever one it stumbles into first.

![Visual explanation of perceptron learning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_perceptron_learning.png)

## The Decision Boundary

The weights define a line, and the line is what the perceptron has actually learned.

The neuron fires when w₁x₁ + w₂x₂ + b is above zero and stays quiet below. The set of points where that expression equals exactly zero is a straight line, and it divides the input space into two regions. Everything on one side gets one label, everything on the other side gets the other. This is why the perceptron is called a `linear classifier`.

Applied to the examinations office's real problem:

Reading the code below: the training loop is the same rule as above, flattened into the `for _ in range(200)` block. What is new is `scale`, and the character grid at the bottom, which is not part of the model at all. The grid asks the trained neuron for a verdict at every combination of hours and attendance, so the boundary becomes visible as the edge between the dots and the P's.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjnuz" 
 width="100%"
></iframe>

```
Learned boundary: 0.13*hours + 0.08*attendance + (-0.10) = 0   (on scaled inputs)

Predicted outcome across the whole grid, P for pass and . for fail

      hours ->
  90%  . P P P P P P P P P
  80%  . . P P P P P P P P
  70%  . . . P P P P P P P
  60%  . . . P P P P P P P
  50%  . . . . P P P P P P
  40%  . . . . . P P P P P
        1 2 3 4 5 6 7 8 910

Every training student, checked against the boundary:
  10 correct out of 10
```

| In the code | What it is | Why it is there |
| --- | --- | --- |
| `scale(hours, attendance)` | Both features onto 0 to 1 | Attendance in the 40s would otherwise dominate every sum |
| `for _ in range(200)` | The training loop | Same three-line rule, run to convergence |
| `weights[0]`, `weights[1]`, `bias` | The learned line | These three numbers are the entire model |
| The grid loop | Not part of the model | Queries the neuron everywhere so the boundary is visible |
| `" P" if ... > 0 else " ."` | One prediction per grid cell | The dividing diagonal is the decision boundary |

The boundary between the dots and the P's is a clean diagonal, which is what a straight line looks like when drawn on a character grid.

Read the diagonal as the rule the perceptron found: hours and attendance trade against each other. A student at 90 percent attendance passes from two hours of study, while one at 40 percent needs six. Nobody wrote that trade-off down, and it is now visible as the slope of the line.

Note also the scaling. Hours run 1 to 10 and attendance runs 40 to 95, so without dividing them onto a comparable range the attendance numbers would dominate every weighted sum, exactly as annual spend dominated visits in the clustering work earlier in this course. For anything that adds up weighted features, scale first.

![Visual explanation of the decision boundary](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_the_decision_boundary_simple_v2.png)

## The Limit

The perceptron comes with a genuine mathematical guarantee, and the guarantee has a condition attached that turns out to be severe.

**The perceptron convergence theorem** says that if the two classes can be separated by a straight line, the learning rule will find such a line in a finite number of steps. It does not say which one, and it does not promise the best one, but it will get there.

If no straight line separates the classes, the rule never settles.

Reading the code below: `train` is the same learning rule packaged into a function so it can be run twice on different data. The one thing to note is its return value. It returns an epoch number when it converges and `None` when it runs out of epochs, and that `None` is the whole result of the experiment. The diagram at the bottom is printed text, not computed.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjph4" 
 width="100%"
></iframe>

```
AND: converged after 6 epochs

XOR: still making mistakes after 1000 epochs
     mistakes in the last ten epochs: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
     the weights are cycling, not settling

Why XOR cannot be done with one straight line:

      x2
   1 | 1     0        the two 1s sit on opposite corners
   0 | 0     1        so does the pair of 0s
     +---------- x1
       0     1

No single straight line puts both 1s on one side and both 0s on the other.
```

| In the code | What it is | Note |
| --- | --- | --- |
| `train(data, epochs=1000)` | The same rule, twice | Only the data differs between the two runs |
| `epochs=1000` | A cap | Without it the XOR run would never end |
| `return epoch, ...` | Converged | Reached zero mistakes |
| `return None, ...` | Gave up | The result that matters here |
| `history[-10:]` | Mistakes in the last ten epochs | All fours, so it is cycling rather than crawling |

Four mistakes an epoch, forever. Not slowly improving, not stuck at one mistake: wrong about all four examples, cycling through the same weights indefinitely.

This is the exercise from the previous lesson, and now the reason is visible rather than mysterious. Plot the four points and the two that should output 1 sit on opposite corners of a square, with the two that should output 0 on the other diagonal. Any straight line you draw will always leave one of each on each side.

The failure is not about XOR being complicated. **It is about a single neuron being able to draw exactly one straight line, and some problems needing something other than a straight line.** That is a limitation of the shape of the model, and no amount of training, learning rate tuning, or data will remove it.

Historically this observation, published in 1969, contributed to a long decline in funding and interest in neural networks. The criticism was correct about single neurons and was widely read as a verdict on the whole approach, which it was not.

![Visual explanation of perceptron linear limit](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_perceptron_linear_limit.png)

## Perceptron at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it is</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>What is learned</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One weight per input, plus a bias</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>How it learns</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only from mistakes; correct predictions produce no change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>What it represents</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single straight boundary through the input space</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Guarantee</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Converges in finite steps if a separating line exists</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Failure mode</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cycles forever if no such line exists, with no signal distinguishing this from slow progress</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Practical need</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Features on comparable scales, since it sums them directly</td>
    </tr>
  </tbody>
</table>

The failure mode row is the practically dangerous one. A perceptron that has not converged looks exactly like a perceptron that needs more epochs, and on real data nobody knows in advance whether a separating line exists. The usual defence is to cap the epochs and keep the best weights seen so far.

![Visual explanation of perceptron at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_perceptron_at_a_glance.png)

## Your Turn

Change the learning rate in the AND program from 0.1 to 1.0, and then to 0.01, recording how many epochs each takes.

You will find the count changes and the final weights change with it, while the outcome does not. The learning rate controls the size of each correction: too large and the weights leap past good values before coming back, too small and it takes many more passes to travel the same distance. Neither breaks it here, because the guarantee holds for any positive rate when the data is separable.

Then break the examinations data deliberately. Add one student who studied nine hours a week with 90 percent attendance and failed anyway, perhaps through illness. Rerun the boundary program and check the count of correct classifications. A single unrepresentative example now sits inside the pass region and cannot be accommodated by any line, so the perceptron will never reach zero mistakes. Decide what you would want the program to do about that, given that in a real cohort such students always exist.

Finally, construct the argument that solves XOR before the next lesson gives it to you. You already know from the previous lesson that a single neuron can compute OR, and that a single neuron can compute NAND. Work out, using only pen and paper, what happens if you feed the outputs of those two neurons into a third neuron computing AND. Check it against all four XOR cases. If it works, you have just discovered why layers exist.
