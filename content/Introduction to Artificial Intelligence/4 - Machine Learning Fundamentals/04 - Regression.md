## Introduction

Harsh's property portal wants a number on every listing page: an estimated fair price, shown before the seller enters their asking price, so that buyers have something to compare against.

The number has to be a rupee amount. Not a band, not a category like "affordable" or "premium", but a figure such as 74 lakh, produced for a flat the system has never seen. A seller lists 1,100 square feet in a locality where the portal has records of flats at 1,050 and 1,150 square feet, and the estimator must produce something sensible in between.

This is a different shape of problem from anything in the previous unit. There is no rule to apply and no category to select. There is a continuous quantity to be produced, and the only guidance available is a table of flats whose prices are already known.

Finding a relationship between the features and a continuous label, so that the label can be estimated for new examples, is **regression**.

**Definition:** `Regression` is supervised learning where the label is a continuous quantity, and the model learns a function from the features to that quantity by adjusting its parameters to minimise the difference between its predictions and the known values.

![Opening scene: Harsh's property portal wants a number on every listing page: an estimated fair price, shown before the seller enters their asking price, so that buyers have something to compare against.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_introduction.png)

## Fitting a Line

The simplest useful regression assumes the label is a straight-line function of one feature.

**price = slope × area + intercept**

Two numbers, `slope` and `intercept`, are the entire model. Learning means choosing them. The slope says how much the price rises per extra square foot, and the intercept is where the line crosses zero area, which is not a meaningful flat but is a necessary part of positioning the line.

The question is which pair of numbers is best, and answering it requires deciding what "best" means. The standard answer is `least squares`: choose the line that makes the sum of the squared vertical distances between the points and the line as small as possible.

Squaring rather than taking absolute values does two things. It prevents a large positive error cancelling a large negative one, and it penalises big misses disproportionately, so a single wildly wrong prediction hurts more than several slightly wrong ones. For a straight line, the values minimising that quantity can be computed directly with no searching at all.

Forty lines follow, and six of them are the lesson. `FLATS` is the data and `train_test_split` is the function from the previous lesson; `fit_line` is least squares, and it is the only part worth reading closely.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk3q8" 
 width="100%"
></iframe>

```
Learned model:  price = 0.0761 * area + (-9.62)
Read as: every extra square foot adds 7.61 lakh per 100 sqft

  area   actual  predicted    error
------------------------------------
   700       41       43.6      2.6
   780       55       49.7     -5.3
   850       52       55.0      3.0
   900       63       58.8     -4.2
   980       60       64.9      4.9
  1050       71       70.3     -0.7
  1150       82       77.9     -4.1
  1250       80       85.5      5.5
  1550      110      108.3     -1.7

An unseen flat of 1100 sqft is estimated at 74.1 lakh
```

Nine lines of arithmetic and the portal has its estimator. The 1,100 square foot flat gets 74.1 lakh, sitting sensibly between the 1,050 flat at 71 and the 1,150 flat at 82.

| In the code | What it is | Why it is there |
| --- | --- | --- |
| `mean_x`, `mean_y` | The centre of the data | Every least-squares line passes through it |
| `top` | How area and price move together | Positive when bigger flats cost more |
| `bottom` | How much area varies on its own | Puts `top` onto a per-square-foot scale |
| `slope = top / bottom` | Lakh per square foot | The number the model learned |
| `intercept = mean_y - slope * mean_x` | Where the line crosses zero | Whatever makes the line hit the centre |

Note that there is no loop, no search, and no repeated guessing anywhere in `fit_line`. For a straight line the best answer has a formula, so it is computed once. Almost nothing else in this course has that luxury.

Three things in that output are worth reading properly.

**The slope is interpretable.** 0.0761 lakh per square foot means roughly 7.6 lakh per hundred square feet, and a domain expert can immediately say whether that is plausible for Pune. This interpretability is a genuine advantage of linear models and a reason they survive despite being simple.

**The intercept is not.** Minus 9.62 lakh is what the model says a flat of zero area costs, which is meaningless. The intercept exists to position the line, not to describe reality, and reading meaning into it is a common error.

**The errors have both signs and do not vanish.** The model is wrong by up to 5.5 lakh on flats it trained on. That is not a failure. A straight line through twelve points cannot pass through all of them, and a model that did would be suspicious rather than impressive.

![Visual explanation of regression line](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_regression_line.png)

## Measuring the Error

"Wrong by up to 5.5 lakh" is not a usable summary. Two standard measures reduce all the errors to one number, and they answer slightly different questions.

- **Mean absolute error**, MAE, is the average size of the error ignoring sign. It is in the same units as the label, so an MAE of 3.57 means the typical estimate is off by about 3.57 lakh, which is a sentence anyone can understand.
- **Root mean squared error**, RMSE, squares the errors before averaging and then takes the square root. Also in the label's units, but it punishes large errors more heavily, so RMSE exceeds MAE whenever some errors are much bigger than others.

Both need something to be compared against, and this is the step beginners skip.

Reading the code below: `mae` and `rmse` are one line each. The part worth attention is inside `report`, where a second set of predictions is built that ignores every feature. That is the baseline, and it is the reason the numbers mean anything.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk44z" 
 width="100%"
></iframe>

```
On the training set:
   model    MAE  3.57  RMSE  3.89
   baseline MAE 15.58  RMSE 19.31   (always guess the training mean, 68.2)

On the held-out test set:
   model    MAE  0.52  RMSE  0.58
   baseline MAE 31.41  RMSE 31.61   (always guess the training mean, 68.2)
```

| In the code | What it computes | Reading it |
| --- | --- | --- |
| `abs(a-p)` summed | Mean absolute error | The typical miss, in lakh |
| `(a-p)**2` summed, then square root | Root mean squared error | Same units, large misses weighted harder |
| `[mean_price] * len(rows)` | **The baseline** | One prediction, repeated: ignore all features |

The third row is the important addition. It is the dumbest possible model, and any real model must beat it. Reporting an MAE without a baseline tells the reader nothing, because they have no idea whether 3.57 lakh is impressive or embarrassing. Here it is clearly impressive, since guessing the mean is off by 15.58.

Now look at the number that should bother you. **The test MAE of 0.52 is far lower than the training MAE of 3.57**, and a model performing better on unseen data than on data it trained on is not a triumph. It is a warning that the measurement is unreliable.

The cause is visible in the previous lesson's output: the test set is three flats, at 550, 620, and 1,400 square feet, and those three happen to lie almost exactly on the fitted line. With three examples, one lucky draw dominates everything. The honest conclusion is not that this model achieves 0.52 lakh accuracy; it is that a three-row test set cannot measure accuracy at all.

![Visual explanation of measuring the error](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_measuring_the_error.png)

## Beyond a Single Feature

The model above uses area and throws away three columns that obviously matter. Real regression uses all of them:

**price = w₁ × area + w₂ × bedrooms + w₃ × age + w₄ × distance + b**

The idea is unchanged, with one weight per feature instead of a single slope, and least squares still defines the best set. What changes is the arithmetic: solving for several weights at once requires linear algebra rather than the two-line formula above, which is one reason libraries exist.

Two cautions carry over from single-feature regression and get worse with more.

**Correlated features make weights uninterpretable.** In this dataset, larger flats also tend to have more bedrooms and be closer to the centre. When features move together, the fitting procedure can distribute credit among them almost arbitrarily, so a weight becoming negative does not necessarily mean that feature reduces price.

**Straight lines are an assumption, not a fact.** Price may rise steeply with area up to a point and then flatten. A linear model cannot represent that and will split the difference, being wrong at both ends. Checking whether the assumption holds is part of the job, and the usual way is to look at whether the errors show a pattern rather than scattering randomly.

![Visual explanation of multivariable regression](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_multivariable_regression.png)

## Your Turn

The lesson used area because it seemed obviously the most important feature. Test that assumption instead of accepting it.

Reading the code below: `fit_line` and `mae` are unchanged. The only new thing is the final loop, which fits a separate one-feature model for each of the four columns by passing `r[i]` instead of `r[0]`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzk4es" 
 width="100%"
></iframe>

```
       feature      slope  train MAE  test MAE
----------------------------------------------
          area      0.076       3.57      0.52
      bedrooms     25.917       7.26      8.91
           age     -3.157      11.49     24.51
  km_to_centre     -7.684       8.15     13.19
```

Area does win, and the other three rows repay careful reading. The slopes for `age` and `km_to_centre` are negative, which is exactly right: older flats and flats further from the centre are cheaper. Bedrooms alone gives roughly 26 lakh per bedroom, which sounds plausible until you notice it is really measuring size in disguise, since bedrooms and area move together.

Now do three things with this code.

Change the seed from 42 to 7, then to 100, and record how much the test MAE for area moves. If it swings substantially, you have demonstrated for yourself that a three-row test set measures luck rather than accuracy, which is the honest reading of the 0.52 above.

Then add a fifth column to each row, a `price_per_sqft` computed as price divided by area, and fit a line from it to price. The test error will be excellent and the model will be useless, because price per square foot cannot be known before the price is. Naming which leakage category from the previous lesson this falls into is the point of the exercise.

Finally, predict the price of a 3,000 square foot flat with the area model. The dataset's largest flat is 1,550 square feet, so the model is being asked about a world it has never seen, and the number it returns will be confident and unsupported. Deciding what a production system should do in that situation is a real design question with no automatic answer.
