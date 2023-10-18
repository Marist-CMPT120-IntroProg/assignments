# Lab Activity #5 – Two-Dimensional Lists

## Goals

Gain familiarity with creating and using a 2D list, or matrix.

### Prerequisites

This lab assumes that you have:

- read up to and including Chapter 8 of our textbook;
- basic experience with Python/IDLE and Git;

### Skills Acquired/Reinforced Upon Completion

- Create functions that perform arithmetic computations.
- Create functions that operate on lists.
- Create functions that test the results of your other functions.

## Instructions

We will begin writing some code that could be used to build a Tic-Tac-Toe
game. We are not writing a complete game today, just using the idea of a
Tic-Tac-Toe game as context for working with 2D lists.

For this activity, you should create a new Python script named `board.py`
in a new `Lab5` subfolder.

## Design Choices

Before coding a solution to a problem, there are several important things we
must decide. Here are some things we'll need in a Tic-Tac-Toe game:

- What data do we need to store and manipulate?
    - the Tic-Tac-Toe board
    - the marks in the cells of the board
- How will we represent that data in our program?
    - strings to represent the marks ("x", "o", and " " for blank cells)
    - a list-of-lists (2D list) to store the marks as a 3x3 grid
- What operations must we perform to manipulate the data?
    - we must be able to display the board on the screen
    - we must be able to change the marks on the board

### Building an Empty Board

We start by creating an empty board.

1. Define a new function named `createBoard`.
    - this function has no parameters
    - start out with a `return None` statement as the function body
2. Your function must return a 2D list of _blank_ cells.
    - make a variable named `cells` that holds an empty list
    - append three new lists to your `cells` lists
    - these three lists should each contain three blank strings `" "`
    - change the return statement to return the `cells` instead of `None`
3. Write a `main` function that calls your `createBoard` function.
    - make a local variable named `board` in the main function to hold the return value
    - call your `main` function at the end of your script
4. Test your program by copying and pasting your code into PythonTutor.com.
    - step through to see the memory diagram and verify that your 3x3 board seems correct
5. Commit your changes so far with GitHub Desktop.

### Displaying the Board

Next, we print the board to the console.

1. Define a new function named `displayBoard`.
     - this function has one parameter, a `board`
     - start out with a `pass` statement as the function body
2. Print top and bottom borders for the board.
     - decide how wide the borders must be an print that many `-` characters
3. Use a loop to print the board one row at a time.
     - use `"|".join(board[i])` to print a row with `|` characters separating the cells
     - you might need to print an extra `|` at the start and end to make the edges of the board
4. Display the board.
     - add a statement to your `main` function to print your empty board
5. Test your program in VSCode and also in PythonTutor.com.
6. Commit your changes so far with GitHub Desktop.

### Marking the Board (if time permits)

Finally, we add the ability to change the board by placing new marks.

1. Define a new function named `placeMark`.
     - this function has four parameters - a `board`, a `mark` string, and two integer indexes identifying the cell
     - start out with a `pass` statement as the function body
2. Change the desired cell so it contains the desired mark.
     - use doble subscript `[i][j]` to get/set the desired cell
2. Now, check the desired cell position and make sure it's blank before marking it.
     - use an `if` statement to compare the cell contents to `" "`
     - if it's not blank, don't change it
4. Place a few marks
     - add four statements to your `main` function that place new marks
     - be sure to try placing a mark in an already marked cell
5. Test your program in VSCode and also in PythonTutor.com.
6. Commit your changes so far with GitHub Desktop.

## Completing this Lab

In order to receive full credit for this Lab activity:

1. The `Lab5` subfolder of your repository must contain one Python
    script `board.py` that meets the requirements above.
2. Your script must contain the name of the lab activity, your full name, and
    the date in a comment at the top.
3. Your repository's commit history must show at least two different commits
    reflecting your changes for the two Python files.
4. All of the above must be pushed to GitHub so that I can see it.

Congratulations! You've completed Lab #5.
