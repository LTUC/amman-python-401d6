# Lab: Class 1 - Intro to Python

## Overview

Today you'll begin working on a command line utility which will mimic the functionality of a point of sale restaurant system using your basic Python tools and understanding of the basics of the language.

## Feature Tasks and Requirements

- When run, the program should print an intro message and the menu for the restaurant
- The restaurant's menu should include appetizers, entrees, desserts, and beverages.
- The program should prompt the user for an order
- When a user enters an item, the program should print an acknowledgment of their input
- The program should tell the user how to exit
- The program's content should match included sample exactly
  - Actually, there's one tiny spot that should be different - see if you can spot it.
  - The `>` character represents user input line and should be printed out with a trailing space.

```console
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
>
```

### Entering an order

```console
***********************************
** What would you like to order? **
***********************************
> Wings

** 1 order of Wings have been added to your meal **

> Wings

** 2 orders of Wings have been added to your meal **
```

### Exiting

```console
> quit
```

### Stretch Goals

- Print out a summary of complete order.
- Only allow ordering items on the menu.
- Allow ordering items not on menu but give custom reply.

## Configuration

Use `poetry` to create `snakes-cafe` project

```console
$ poetry new snakes-cafe
...
```

See the **Creating Project with Poetry** section of [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for additional details

Create a `snakes_cafe.py` file inside the `snakes_cafe` folder. Note the hyphen vs. underscore

```console
snakes-cafe/
├── README.md
├── poetry.lock
├── pyproject.toml
├── snakes_cafe
│   ├── __init__.py
│   └── snakes_cafe.py
└── tests
    ├── __init__.py
    └── test_snakes_cafe.py
```

## Repository set-up

- Create a repository on Github with the exact name of `snakes-cafe`.
- See the **Github** section of [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for additional details


## Submission Instructions

- Refer to the the [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for the complete lab submission process and expectations
- You may have noticed many references to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"}
  - That's on purpose. Getting the steps exactly right is crucial. So make sure you follow them closely.
