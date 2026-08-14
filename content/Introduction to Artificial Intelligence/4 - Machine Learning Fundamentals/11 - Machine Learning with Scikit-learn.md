## Introduction

Harsh has until Friday to tell the property portal which model to ship, and he has four candidates: the straight line from earlier, a nearest-neighbour version, a decision tree, and one more his manager read about on a flight.

Comparing them honestly means the same work four times over. Four fitting procedures, four ways of holding out a test set, four scoring conventions to reconcile before the numbers can even be put side by side. He did this properly once and it cost him a day. So on Thursday evening he does what most people do: fits each model once, on one split, and reports whichever number came out highest.

Notice what he dropped, and why. Cross-validation, a baseline to beat, choosing the threshold on validation data rather than test data. He knows all three matter. Each one costs effort per model, and a four-way comparison multiplies effort per model by four. The discipline was abandoned not through ignorance but because knowing better had become expensive.

That is the problem **scikit-learn** solves, and it is not typing. When every model is driven by the same two methods, comparing four of them is a loop rather than four projects, and the careful workflow stops being the expensive option.

**Definition:** `scikit-learn` is a Python library providing a uniform interface to machine learning models, in which every estimator offers `fit` to learn from data and `predict` to apply what was learned, together with tools for splitting data, tuning settings, and measuring results.

![Harsh compares four property-price models while a Friday deadline approaches](images/11_section_introduction_v2.png)

## The Interface Is the Idea

Three methods carry almost everything.

- **`fit(X, y)`** learns from features `X` and labels `y`. This is training.
- **`predict(X)`** applies the trained model to new features. This is inference.
- **`fit_transform(X)`** is the equivalent for preparation steps such as scaling, which learn something from the data and then apply it.

Because every model implements the same methods, code written for one works for another unchanged. That uniformity is worth more than any individual algorithm in the library.

Two conventions go with it. Features are held in `X`, a list of rows where each row is one example, and labels in `y`, one entry per row. Any setting you choose yourself is passed to the constructor, and anything learned from data is stored on the fitted object with a trailing underscore, as in `coef_` or `feature_importances_`.

![Visual explanation of sklearn workflow](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_sklearn_workflow.png)

## The Complete Workflow, Sixteen Lines

Here is the loan problem from earlier in this unit, done the library way.

Reading the code below: the tree from lesson 06, roughly sixty hand-written lines, is now four. `train_test_split` does the shuffling and cutting, `DecisionTreeClassifier(...)` chooses the settings, `.fit` learns, and `.predict` applies. Everything after that is printing.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk955" 
 width="100%"
></iframe>

```
Trained on 12 applications, tested on 4
Test accuracy: 0.75

The tree it learned:
|--- income_k <= 31.50
|   |--- years_employed <= 4.50
|   |   |--- class: 0
|   |--- years_employed >  4.50
|   |   |--- class: 1
|--- income_k >  31.50
|   |--- class: 1

How much each feature was used:
          income_k 0.70
    years_employed 0.30
      credit_score 0.00
```

| In the code | What it replaces | Note |
| --- | --- | --- |
| `train_test_split(...)` | The hand-written shuffle and slice | `stratify=y` is the part the hand-written version lacked |
| `DecisionTreeClassifier(max_depth=2)` | Your `build` function and its depth limit | Settings you choose go in the constructor |
| `model.fit(X_train, y_train)` | The whole splitting and recursion | Learning is one call, on training data only |
| `model.predict(X_test)` | Your `predict` walk down the tree | Same idea, works identically for every model |
| `model.feature_importances_` | Nothing you wrote | The trailing underscore means it was learned |

Everything the hand-written tree did, and several things it did not, in a fraction of the code.

Three details repay attention.

**`stratify=y` does the fair splitting.** It keeps the same proportion of approved and rejected applications in both halves, which on a 16-row set with 11 approvals matters a great deal and which the hand-written split did not do.

**`random_state=0` makes it reproducible.** Every function in the library that involves randomness takes this argument, and omitting it means your colleague cannot reproduce your numbers.

**`feature_importances_` is free information.** Credit score scores 0.00, meaning this tree never split on it. The hand-written tree on the full sixteen rows split on credit score first; this one, trained on a stratified twelve, found income more useful. That is not a contradiction, it is the instability of trees from earlier in this unit, appearing again on a smaller training set.

![Visual explanation of the complete workflow, sixteen lines](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_the_complete_workflow_sixteen_lines_simple_v2.png)

## Comparing Models Honestly

The real gain arrives when several models must be compared. Because they share an interface, they can be put in a list and evaluated in a loop.

Reading the code below: the long import block is four different model families, and the point is that the loop at the bottom does not care which is which. Every one of them accepts the same `cross_val_score(model, X, y, cv=4)` call, which is the entire argument of this lesson in one line.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk9em" 
 width="100%"
></iframe>

```
4-fold cross-validation on 16 applications

                   model    mean   spread  fold scores
------------------------------------------------------------
  always predict approve    0.69     0.11  0.50 0.75 0.75 0.75
   decision tree depth 2    0.81     0.11  1.00 0.75 0.75 0.75
    3 nearest neighbours    0.75     0.18  0.75 0.75 1.00 0.50
     logistic regression    0.88     0.12  1.00 0.75 1.00 0.75
```

| In the code | What it is | Why it is there |
| --- | --- | --- |
| `DummyClassifier(strategy="most_frequent")` | The do-nothing model | The bar every real model must clear |
| `make_pipeline(StandardScaler(), ...)` | Scaler glued to model | Refits the scaler inside each fold, so nothing leaks |
| `cross_val_score(model, X, y, cv=4)` | The whole of lesson 08 | Identical call regardless of the model |
| `scores.mean()` and `spread` | The two-number report | The spread is what stops you overreading the mean |

Four models, cross-validated, in one loop. Three things in this block are the whole argument for the library.

**`DummyClassifier` is the baseline, provided as a first-class model.** It always predicts the most common class and scores 0.69. Any model not clearly beating that has earned nothing, and nearest neighbours at 0.75 with a spread of 0.18 has not clearly beaten it.

**`make_pipeline` binds scaling to the model.** This is not a convenience. Scaling learned from the whole dataset and then cross-validated would leak information from each held-out fold into the scaler, quietly inflating every score. A pipeline refits the scaler inside each fold using only that fold's training portion, which is the correct procedure and is easy to get wrong by hand.

**`cross_val_score` replaces the whole hand-written cross-validation.** One call, and the fold scores come back so the spread can be reported alongside the mean.

Read the spread column before the mean column. Logistic regression leads at 0.88, and with four folds on sixteen rows and a spread of 0.12, the honest statement is that it looks best on very little evidence.

![Visual explanation of honest model comparison](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_honest_model_comparison.png)

## Tuning Without Cheating

The last piece of the workflow is choosing a hyperparameter without contaminating the test set, which the library packages as a single object.

Reading the code below: two models are fitted to the flats data. The first, `LinearRegression`, needs no tuning and is three lines. The second is the interesting one. `GridSearchCV` wraps a pipeline and a dictionary of values to try, and its `.fit` runs a full cross-validated search over all five values of k inside the training data before refitting the winner. The test set is touched exactly once, in the final `mean_absolute_error` call.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk9sk" 
 width="100%"
></iframe>

```
Linear regression on all four features
   test MAE 1.15 lakh
            area weight    0.055
        bedrooms weight    5.107
             age weight   -1.563
    km_to_centre weight    0.923

Nearest-neighbour regression, k chosen by cross-validation
   best k = 3
   cross-validated MAE 10.26 lakh
   test MAE 9.67 lakh
```

| In the code | What it is | Note |
| --- | --- | --- |
| `line.coef_` | The learned weight per feature | One per column, and one of them is nonsense |
| `{"kneighborsregressor__n_neighbors": [...]}` | The values to try | Double underscore addresses a step inside the pipeline |
| `scoring="neg_mean_absolute_error"` | The thing being optimised | Negated because the library maximises its score |
| `search.fit(X_train, y_train)` | 15 fits behind one call | Every one of them inside the training data |
| `search.best_score_` | Cross-validated MAE of the winner | The honest estimate, before test is opened |
| `search.predict(X_test)` | The refitted best model | The single permitted look at the test set |

`GridSearchCV` cross-validates every candidate value inside the training data, keeps the best, and refits on all of it. The test set is opened once at the end. The three-way discipline from the training lesson, in one object.

Two results here are worth more than the convenience.

**Using all four features beats using one.** Test MAE of 1.15 lakh against roughly 3.4 for the hand-written single-feature line. The extra columns were carrying real information that the earlier model discarded.

**One weight is nonsense, and you should notice.** `km_to_centre` has a weight of positive 0.923, which says flats further from the city centre cost more. That is not true in Pune or anywhere else. It is the correlated-features warning made concrete: distance moves with area and bedrooms in this small sample, and least squares distributed the credit among them in a way that happens to fit twelve rows and does not describe reality. **A model can predict well and still contain coefficients that are worthless as explanations**, and reading weights as causes is one of the commonest mistakes made with linear models.

Note also that nearest neighbours does badly here, at 9.67 lakh. With nine training flats, the three nearest are often not very near, and the library made it effortless to discover that rather than assuming it.

![Visual explanation of tuning without cheating](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_tuning_without_cheating.png)

## What the Library Does Not Do

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">It handles</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">You still decide</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fitting, predicting, splitting, cross-validating, scoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether the problem needs learning at all</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scaling, encoding, and binding them into a pipeline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which features to collect, and whether any of them leak the answer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Searching hyperparameters without touching the test set</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which metric matters, and where the threshold goes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Computing accuracy, precision, recall, and the rest</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether a coefficient of positive 0.923 makes any sense</td>
    </tr>
  </tbody>
</table>

Everything in the right-hand column is judgment, and none of it is a call anyone can import. The library removes the implementation, not the thinking, and a practitioner who only ever learned the left-hand column will produce a leaking model with an excellent score and no idea anything is wrong.

![Visual explanation of what the library does not do](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_section_what_the_library_does_not_do.png)

## Your Turn

Take the model comparison and make it answer a question the loan committee would actually ask.

Replace `cross_val_score`'s default scoring with `scoring="recall"` and rerun, then with `scoring="precision"`. The ranking will change, and the always-approve baseline will score a perfect 1.00 on recall while being worthless. Explain why, and you will have connected the library's scoring options to the evaluation lesson properly.

Then extend the grid search. Add `max_depth` of 1, 2, 3, and None as a second hyperparameter for a decision tree, and search over both it and the criterion, `gini` against `entropy`. Report which combination wins and by how much over the dummy baseline. Note how little code the second hyperparameter cost you, and note also that the honest conclusion on sixteen rows may well be that the differences are smaller than the fold-to-fold spread.

Finally, do the exercise that matters most. Take the hand-written least-squares function from earlier in this unit and check it against `LinearRegression` on the same single feature. They should agree to several decimal places. Confirming that the library is doing the thing you already understand, rather than something mysterious, is the point of having written it yourself first.
