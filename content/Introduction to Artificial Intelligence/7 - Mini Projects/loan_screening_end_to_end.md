## Background

A cooperative bank asks for a model that predicts which loan applications will be repaid. The team builds one, reports 90 percent accuracy, and the manager is delighted. Six weeks after launch the model is performing at chance, and nobody can say what changed.

Nothing changed. One of the columns in the training data was written by a loan officer after the decision had already been taken, so the model spent its training learning to read the answer rather than predict it. In deployment that column is blank, and what remains is a model that never learned anything.

This project walks the whole pipeline with that trap deliberately planted, so you find it yourself rather than being warned about it.

## What You Will Build

An end-to-end loan screening pipeline: generate the dataset, detect and remove a leaked feature, establish a baseline, choose a hyperparameter without touching the test set, and report the result as a confusion matrix rather than a single number.

## Learning Objectives

By the end of this project, you will be able to:
- Recognise leakage from the pattern it leaves in feature importance
- Establish a baseline before believing any model result
- Choose a hyperparameter by cross-validation inside the training data
- Open a test set exactly once, at the end
- Report performance in counts the person making the decision can act on

**Difficulty:** Intermediate · **Estimated time:** 3 hours

## Tasks

### Task 1: Build the Dataset, Including the Trap

1. Generate at least 400 applications with a fixed random seed, each having income, years employed, and credit score. Derive the repayment outcome from those three features with some randomness, so the relationship is real but imperfect.

2. Add a fourth column called `officer_note` which agrees with the outcome about 95 percent of the time. This column represents something recorded after the decision was taken.

3. Print how many applications you generated and what fraction were approved. If your approval rate is close to 0 or 1, adjust the generation until both classes are reasonably represented.

### Task 2: Find the Leak

1. Train a decision tree with a fixed depth on all four features, using a stratified split, and report test accuracy together with the feature importances.

2. Train the same model on only the first three features and report the same figures.

3. Print the difference in accuracy and state plainly which number was real.

4. The importance vector is the evidence. A single feature carrying almost all the importance while the features you know to be causal carry almost none is the signature to learn.

### Task 3: The Honest Pipeline

1. Establish a baseline that always predicts the majority class, scored by cross-validation on the training portion. Any model that fails to beat this has earned nothing.

2. Use a grid search with cross-validation over at least five values of the tree's maximum depth. All of this happens inside the training data.

3. Open the test set once, at the very end, and report a confusion matrix in four labelled counts, plus accuracy, precision and recall.

4. Label the four cells in the bank's language, not in abstract terms: approved and repaid, approved and defaulted, rejected who would have repaid, rejected correctly.

## Sample Run

```
400 applications, 201 approved (50 percent)

WITH officer_note (recorded after the decision)
   test accuracy       0.900
   feature importance  {'income_k': 0.0, 'years_employed': 0.0, 'credit_score': 0.03, 'officer_note': 0.97}

WITHOUT officer_note
   test accuracy       0.680
   feature importance  {'income_k': 0.17, 'years_employed': 0.25, 'credit_score': 0.58}

Dropping the leaked column costs 0.220 accuracy.
The higher number was never real; it was the answer copied into a column.

Baseline (always predict the majority)  0.497
Best max_depth by cross-validation      2
Cross-validated accuracy                0.633

TEST SET, opened once
   approved and repaid (tp)    40      approved, defaulted (fp)  22
   rejected, would repay (fn)  10      rejected correctly  (tn)  28
   accuracy 0.680   precision 0.645   recall 0.800
```

The importance row is the tell. With the leaked column present, income and years employed carry importance of exactly zero, which should be alarming rather than reassuring: the model has stopped using the features that actually cause repayment because one column tells it the answer outright.

**Answer these questions after completing all tasks:**
- Your honest model scores 0.680 against a baseline of about 0.497. Is that worth deploying? Answer in terms of what the bank gains per hundred applications rather than in terms of the accuracy figure.
- Look at your two error cells. One is money lost, the other is a customer turned away who would have repaid. Which would your bank rather have, and how would you move the model's threshold to get more of it?
- You dropped `officer_note` because you knew how it was generated. In a real dataset nobody tells you. Write the one question you would ask about every column before training, and explain why asking it is cheaper than discovering the answer after launch.

## Deliverables & Rubric

Submit your `.py` file, the full printed output, and your written answers.

Your project is assessed out of 10:

| Criteria | Points |
|---|---|
| Dataset generated with a fixed seed, both classes represented, trap included | 2 |
| Leak demonstrated through both accuracy and feature importance | 2 |
| Baseline established and beaten, with the comparison reported | 2 |
| Hyperparameter chosen by cross-validation, test set opened only once | 2 |
| Confusion matrix reported in the bank's language, not abstract labels | 1 |
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

This project needs scikit-learn, the library introduced in Unit 4. If the workspace does not already have it, install it once with `pip install scikit-learn` before running your script.
