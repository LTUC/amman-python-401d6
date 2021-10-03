# Lab: File IO and Exceptions

## Overview

In this lab assignment you will be creating a command line application which takes advantage of Python's built in capabilities for reading and writing files.

## Resources

- [starter test script](./starter_tests/test_madlib.py){:target="_blank"} is supplied and should be moved to your application's `tests` folder.
  - **NOTE:** All included tests must pass as written.
  - though you can add more tests if you like.
- [Python String format() Method](https://www.w3schools.com/python/ref_string_format.asp)
- [Unpacking Arrays](https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators)

## Configuration

Use `Poetry` to create project named `madlib-cli`.

## Repository set-up

Create repository on Github with name `madlib-cli`

## Feature Tasks and Requirements

- Create a file called `madlib.py` at root of `madlib_cli` folder, which will contain all of the Python code that you will write relating to your Madlib game.
- Keeping in mind the concept of [Single Responsibility Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle){:target="_blank"}, build a command line tool which will perform the following:
  - Print a welcome message to the user, explaining the Madlib process and command line interactions
  - Read a template Madlib file ([Example](./assets/make_me_a_video_game_template.txt){:target="_blank"}), and parse that file into usable parts.
  - Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
  - With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
  - After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
  - Write the completed text ([Example](./assets/make_me_a_video_game_output.txt){:target="_blank"})to a new file on your file system (in the repo).
  - **Note:** A [smaller example file](./assets/dark_and_stormy_night_template.txt){:target="_blank"} is included as well which can be handy when developing/testing.

## Testing Details

You are NOT required to test terminal input/output, AKA print and input functions.

However you ARE expected to have meaningful tests for your application.

So how can we skip testing print and output functionality while still proceeding with confidence?

The resolution to that dilemma is to break down your code so that it is more easily testable.

- Create and test a **read_template** function that takes in a path to text file and returns a stripped string of the file's contents.
- **read_template** should raise a FileNotFoundError if path is invalid.
- Create and test a **parse_template** function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
- Create and test a **merge** function that takes in a "bare" template and a list of user entered language parts, and returns a string with the language parts inserted into the template.

## Stretch Goals

- Figure out / research a way to verify terminal input/output.
- Test that completed madlib is properly written to disk with correct content.

## Submission Instructions

Refer to the the [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for the complete lab submission process and expectations
