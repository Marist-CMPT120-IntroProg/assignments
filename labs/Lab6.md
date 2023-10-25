# Lab Activity #6 – Top-Down Design

## Goals

The goal of this lab time is to build a framework for an interactive Tic-Ta-Toe
game in Python by implementing a top-downdesign for the program. You will work
in pairs to brainstorm and implement as much of the design as you can.

## Instructions

1. Study very carefully the design given below.
2. Implement each function fromthe top-down. For example, try to write `check_gameover` before you write `check_row`, `check_col`, or `check_diag`.
3. Use placeholders for the bodies of all unimplemented functions.
    - If a function does not need to return a value, the placeholder statement is `pass`.
    - If the function will eventually return a useful value, the placeholder statement is `return None`.
4. After each new function you implement, try to ensure that your code runs without syntax errors or crashing before moving on to the next function.
5. Take turns with your partner at the keyboard, one person coding while the other asks questions, looks for problems and makes suggestions.
6. At the end, be sure that both of you have all the code that you wrote together so you can commit it to your own repository. Use [codeshare.io](http://codeshare.io) to transfer the code to one another.

## The Design

### Top-Down Functional Components

What are the fundamentals tasks involved in the Tic Tac Toe game?

```
                                         [ main ]
    ________________________________________|_______________________________________________
   /                                     /                                  \               \
[setup_board]                         [play]                            [show_intro]   [show_outro]
                       _________________|_______________________
                      /             /           \               \
                [show_board]   [get_move]   [make_move]   [check_game_over]
                     |             |                 __________|_______________________
                     |             |                /          |           \           \
                [show_row]    [check_move]    [check_row] [check_col] [check_diag] [check_tie]
                     |
                     |
                [show_cell]
```

### Data Representation

What information is relevant to the game of Tic Tac Toe?

**Explicit:**
  * Players - Whose turn is it? Who, if anyone, has marked a given cell?
  * Board - a 3x3 grid of cells
  * Cells - may contain a mark made by a player
  * Mark - identifies which player owns a cell, what does a mark look like?

**Implicit:**
  * Rows/Columns/Diagonals - a collection of 3 consecutive/adjacent cells
  * Boundaries/Borders - surrounds the board and separates rows and columns

### Process / Control Flow

What are the steps, in order, needed to implemnent the Tic Tac Toe game? Here
is the high-level outline... Your task is to implement that mid- to low-level
parts of this process, basically anything that's not implemented below.

```
def main():
  show_intro()
  board = setup_board()
  result = play(board)
  show_outro(result)

def play(board):
  player = "x"
  row, col = 0, 0
  while moves_remain(board):
    show_board(board)
    row, col = get_move()
    make_move(board, row, col)
    is_gameover = check_gameover(board, row, col)
    if is_gameover:
      return is_gameover
    player = "o" if player == "x" else "x"
  return "No moves remain... It's a tie!"
```

## Completing this Lab

In order to receive full credit for this Lab activity:

1. The `Lab6` subfolder of your repository must contain at least one Python
    script named `tictactoe.py` that meets the requirements above.
2. Your script must contain the name of the lab activity, the names of both members of the team, and
    the date in a comment at the top.
3. Your repository's commit history must show at least two different commits
    reflecting your changes for the two Python files.
4. All of the above must be pushed to GitHub so that I can see it.
