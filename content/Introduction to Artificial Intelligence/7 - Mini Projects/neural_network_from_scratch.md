## Background

Every network in Unit 5 was described as a nested list of numbers with one operation applied repeatedly. That is easy to say and easy to half-believe. The way to actually believe it is to write the whole thing yourself, in about sixty lines with no libraries, and watch it learn something a single neuron provably cannot.

XOR is the right target because it is small enough to check by hand and impossible for one neuron. When your network gets all four cases right, you will know the hidden layer did something real, because nothing else could have.

## What You Will Build

A two-input, two-hidden-unit, one-output network with backpropagation written from scratch using only the standard library, trained on XOR, plus two experiments that show why the same code sometimes succeeds and sometimes does not.

## Learning Objectives

By the end of this project, you will be able to:
- Implement forward propagation and backpropagation without a framework
- Trace each factor in a weight update back to the step of the algorithm it comes from
- Show that training success depends on where the random weights started
- Find the range of learning rates that works, from both ends
- Explain why identical initial weights would make the hidden layer useless

**Difficulty:** Advanced · **Estimated time:** 4 hours

## Tasks

### Task 1: Forward and Backward

1. Represent the network as weights and biases for a hidden layer of two units and one output unit. Initialise every one from a seeded random generator so your runs are reproducible.

2. Write `forward(x)` returning both the hidden activations and the output. You need the hidden values again on the way back, so return them rather than recomputing.

3. Implement one training step by hand. Compute the output error scaled by the output's responsiveness, pass the blame back along the output weights scaled by each hidden unit's responsiveness, then update every weight and bias.

4. Add a comment against each factor in your update naming which step of backpropagation it is. If you cannot name a factor, you have copied it rather than derived it.

### Task 2: The Starting Point Matters

1. Train the same network on XOR from at least eight different seeds, keeping everything else fixed. Report the final loss and how many of the four cases come out correct once rounded.

2. Print the count of seeds that solved it. Do not tune anything to make this number higher. The proportion is the result.

3. A seed that reaches a loss near 0.125 with three of four cases correct has not failed to finish. It has settled in a hollow it cannot climb out of, and running it longer will not help. Confirm this by increasing the epochs for one stuck seed.

### Task 3: The Learning Rate Has Two Edges

1. Choose one seed that reliably solves XOR, and sweep the learning rate across at least five values spanning three orders of magnitude, from very small to very large.

2. Report the final loss for each. You are looking for two different failures at the two ends, not one.

3. Watch for a case where the rounded answers are all correct while the loss is still high. Decide what that tells you about judging a model by its accuracy alone.

## Sample Run

```
A NEURAL NETWORK FROM SCRATCH: 2-2-1 on XOR

Does the starting point matter? Same code, same data, 8 seeds, rate 0.5

 seed   final loss  cases right  verdict
------------------------------------------------
    0      0.16695         3/4  STUCK
    1      0.00013         4/4  solved
    2      0.00017         4/4  solved
    3      0.12521         3/4  STUCK
    4      0.12522         3/4  STUCK
    5      0.00014         4/4  solved
    6      0.00014         4/4  solved
    7      0.12521         3/4  STUCK

4 of 8 seeds solved XOR. The rest reached a hollow they could not leave.

Does the learning rate matter? Seed 1 throughout, which solves at 0.5

   rate   final loss  cases right
----------------------------------
  0.001      0.24972         3/4
   0.01      0.21512         4/4
    0.1      0.00084         4/4
    0.5      0.00013         4/4
    5.0      0.00001         4/4
   50.0      0.24878         3/4
```

Four seeds out of eight is the honest answer to "does this work". Not always and not never, which is why practitioners train several times and keep the best. Notice also the rate of 0.01: all four cases round to the right side while the loss is still 0.215, so the network is correct and barely confident. Accuracy alone would have called that a success.

**Answer these questions after completing all tasks:**
- Set every weight and bias to exactly zero instead of random values. Work out on paper what the two hidden units compute on the first pass and what corrections each receives, then run it and confirm. Why is random initialisation required rather than merely conventional?
- Your rate of 0.001 and your rate of 50.0 both fail, and they fail for opposite reasons. Describe what the weights are doing in each case, in a sentence each.
- Increase the hidden layer from two units to four and rerun the seed sweep. Report the new count of seeds that solve it, and say whether extra capacity made the training more reliable or merely larger.

## Deliverables & Rubric

Submit your `.py` file, both printed tables, and your written answers.

Your project is assessed out of 10:

| Criteria | Points |
|---|---|
| Forward pass and backpropagation implemented without a framework | 3 |
| Each factor in the weight update annotated with the step it comes from | 1 |
| Seed sweep run across at least eight seeds with the proportion reported honestly | 2 |
| Learning rate sweep shows failure at both ends, not just one | 2 |
| Zero-initialisation question answered from reasoning, then confirmed by running it | 1 |
| Code readability and organisation | 1 |
| **Total** | **10** |

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/01_create_new_workspace.png)

3. Select the **Python** template, then click **Next**.

![Select the Python template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/02_select_python_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the Python workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/03_name_and_launch_workspace.png)
