# Lab: Data Visualization

## Overview

Today you'll be telling a story visually. Choose 2 datasets from Kaggle (or built in to Seaborn) and visualize it as effectively as you can.

## Feature Tasks and Requirements

- Select 2 [Kaggle data sets](https://www.kaggle.com/datasets){:target="_blank"} that are suitable for the story you want to tell.
  - **Note** make sure the data set has csv file/s to download.
- Optionally use dataset built into Seaborn
- Load the data you receive into a Pandas `DataFrame`
- Analyze dataset
- Verbalize your insights in notebook in Markdown cells
- Summarize your insights at bottom of notebook
- Notebook should have professional polish
  - In other words, imagine you are presenting it on the job. 

## Implementation Notes

### User Acceptance Tests

- No automated tests

## Setup

- Use either JupyterLab or VS Code to author your notebooks.

## Configuration

Use `poetry` to create `data-visualization` project.

```console
> $ mkdir data-visulization
> $ cd data-visualization
> $ poetry init -n
> touch viz-a.ipynb
> touch viz-b.ipynb
```

Use the `data-visualization` folder as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.

## Stretch Goals

- Use a different visualization library
- Stream data from url instead of loading local file
- Join a Kaggle competition
