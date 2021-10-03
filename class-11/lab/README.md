# Lab: Numpy Arrays

## Overview

Today we'll be constructing chess boards like it's 1980.

No prebuilt images, just the power of arrays and pixel art.

## Feature Tasks and Requirements

Your job is to render out chess boards with red and blue queens on them.

We're keeping it really basic here so the only pieces are queens and each queen is represented by a blue or red square.

Chess board is an 8 by 8 grid of alternating black and white squares. The queens are red and blue squares.

Each board will have one red and one blue queen at different coordinates. In addition to displaying the board you'll need to identify if the queens are "under attack" based on their coordinates.

## Implementation Notes

- Define a `ChessBoard` class
  	- should contain an 8x8 grid
    	- Each cell in grid should have a color represented in RGB format.
    		- black = (0,0,0)
    		- white = (1,1,1)
    		- blue = (0,1,1)
    		- red = (1,.2,0)
  - should have `add_red` method that accepts a row and column as input which colors corresponding cell.
  - should have `add_blue` method that accepts a row and column as input which colors corresponding cell.
  - should have `render` method that displays the chess board on screen with red and blue shown in correct locations
  - should have `is_under_attack` method that return boolean if red is under attack by a blue piece horizontally, vertically or diagonally

### User Acceptance Tests

- queens on same row should be "under attack"
- queens on same column should be "under attack"
- queens on same diagonal should be "under attack"
- queens with any other coordinates should NOT be "under attack"

**NOTE:** Include `assert` statements directly in your notebook verifying the behavior above.

### Stretch Goal

- Enlarge the chessboard to allow for pixel art drawn pieces. 16x16 ought to be enough.
- Add more attacking queens.
- Add opacity to cell colors.

## Configuration

Use `poetry` to create `chess-board` project.

**NOTE:** do NOT use `poetry new` for this project. If you did use new command the easiest thing is to delete the folder and start again with instructions below.

- $ mkdir chess-board
- $ cd chess-board
- $ poetry init -n
- $ poetry add numpy matplotlib jupyterlab
- $ poetry shell
- $ touch chess_board.ipynb

> open chess-board folder in vscode

> open chess_board.ipynb and VS Code Jupyter Server should start

Use the `chess-board` folder as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
