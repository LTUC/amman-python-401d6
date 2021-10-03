# Lab: Game of Greed 4

## Overview

Today you'll continue work on command line version of the dice game `greed` by adding an AI bot to play the game.

## Feature Tasks and Requirements

- Create an AI Bot to play Game of Greed
  - The only method available for use from Game class is `play`.
  - All static methods of `GameLogic` class are available.
  - All other interactions with game can take place **ONLY** via the I/O features of the game.
    - In other words, via injectable `print` and `input` functionality.
    - It is FORBIDDEN to inject a custom `roller` function into Game class.
- Copy [bots.py](./bots.py){:target="_blank"} to your project.
  - Place it at root of project, at same level as `pyproject.toml`
- Your Bot class should be added to `bots.py` file with name of your choosing replacing `YourBot`.
  - **NOTE** the code for `BaseBot` class is supplied for reference, but your custom code will be in the overridden `_roll_bank_or_quit` and `_enter_dice` methods.
- User should be able to see your bot play by executing `bots.py` from terminal.
- Application should implement features from previous classes

The goal is to beat **Nervous Nellie** - A reference bot that banks on the first roll every time.

## Implementation Notes

- Review [rules of game](https://en.wikipedia.org/wiki/Dice_10000){:target="_blank"}
- Play game [online](http://www.playonlinedicegames.com/farkle){:target="_blank"}

## Configuration

Continue working with team in `game-of-greed` repository

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
