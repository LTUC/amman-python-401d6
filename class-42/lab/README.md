# Lab: Pythonisms

## Overview

Python has many elegant features that can show the difference between a "programmer who uses Python" and a true "Pythonista"

Pythonista may be a silly word but it's a real thing. A true pythonista is able to leverage the particular features of Python to accomplish a task in a simpler and more easy to reason about way.

## Feature Tasks and Requirements

- Create examples demonstrating `pythonic` language features. For example...
  - Use iterators/generators on a custom collection to...
    - add ability to be used in a `for in` loop
    - add ability to be used in a list comprehension
    - add ability to convert to a list or other collection type
  - Create a decorator that adds behavior to a given function. For example...
    - Calculate the time spent in the function
    - Log relevant info for debugging purposes
    - Slow down the function
    - Convert the return value in some way
    - Validate some condition on the way in
  - Use dunder methods make your code more readable and elegant. For example...
    - add ability for two custom data structure to be considered equal
    - add ability for custom data structure to be considered truthy/falsy
  - Anything else that catches your interest

## Implementation Notes

- Describe your findings in README
- Optionally create your project as a Jupyter Notebook if you prefer
  - In that case add tests as asserts within Notebook

### User Acceptance Tests

- Create unit tests to demonstrate the features you select.

## Configuration

- create a `pythonisms` repository on GitHub.
- Use `poetry` to initialize project.
  - > $ poetry init -n


Use the folder created by Poetry as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
