# Lab: Exploratory Analysis with Linear Regressions

## Overview

Today you'll perform exploratory analysis by using Linear Regressions on the Kaggle data set of your choice.

## Feature Tasks and Requirements

- Select a [Kaggle data set](https://www.kaggle.com/datasets?search=linear+regression){:target="_blank"} that is suitable for Linear Regression.
  - **Note** make sure the data set has csv file/s to download.
  - Data set must be **continous** values appropriate for a **Linear** Regression. If you're not sure then ask Instructor or TA.
- Load the data you receive into a Pandas `DataFrame`.
- Show the first five rows of the data set.
- Show the `description` and the `info` of the data set.
- Ensure that any `date` columns have been cast into a `datetime` object in your DataFrame.
- Using a regression model, split your data into train and test data.
- Fit your training split to the regression model.
- Show your regression model's score.
- Draw at least three conclusions from your regression model.
- Your notebook should be clutter free and polished.

## Implementation Notes

### User Acceptance Tests

No acceptance tests today.

## Configuration

Use `poetry` to create `linear-regression` project.

```console
> $ mkdir linear-regression
> $ cd linear-regression
> $ poetry init -n
> $ poetry add [required libraries, see demo]
> $ touch regression.ipynb
```

Use the `linear-regression` folder as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
