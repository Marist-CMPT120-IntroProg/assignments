# Lab Activity #4 – Errors and Exceptions

## Goals

Gain familiarity with Boolean expressions and except handling.

### Prerequisites

This lab assumes that you have:

- read up to and including Chapter 7 of our textbook;
- basic experience with Python/IDLE and Git;

### Skills Acquired/Reinforced Upon Completion

- Refactor functions to reduce code duplication.
- Use logical operators to make more complex test expressions.
- Modify a function to handle exceptions that might be raised.

## Instructions

### Preliminaries

1. Create a new `Lab4` subfolder in your local `lastname-work` folder.
2. Download the `average.py` script from this repository and place it in your new `Lab4` subfolder.
3. Open the `average.py` script in VSCode.
4. Run the script and test it out to make sure you know what it does and how it works.

### Part 1 - Refactoring

Refactoring means reorganizing the design and structure of a program in some way.

The simplest refactorings are things like renaming a variable or function. More complex refactoring can completely change that way a program looks and runs.

For this Lab, we will reduce some code duplication (places where our program repeats itself) and thus make the code simpler and less error prone.

1. Carefully examine the `read_numbers` and `read_numbers_into` functions. Notice that the two functions are nearly identical.
    - They differ only by one line - `read_numbers` has one extra line at the beginning to create an empty list in which to place the numbers.
3. Delete all bu the first line (`xs = []`) of the `read_numbers` function.
4. Add a new second line in the body of `read_numbers` that calls the other function, `read_numbers_into`, and passes the empty `xs` list as an argument.
    - The idea here is to _delegate_ to the second function so we don't have to repeat all the some lines of code in two places.
    - Now, if we fix or change something in the `read_numbers_into` function, then the `read_numbers` function automatically benefits from those changes, and we don't have to make those changes in two places.
5. Run the script to test that the program still works correctly.
6. Finally, commit these changes.

### Part 2 - Logical Connectives

Next, we will make use of a logical operator to handle a wider variety of situations in our program. Recall that the logical operators are `and`, `or`, `not`.

1. First, modify the `if`-statement in the `read_numbers_into` function so that it handles either uppercase "Q" or lowercase "q" as commands to quit the program.
    - To do this, choose the logical operator that is appropriate for the situation.
    - Do __not__ use the `.lower()` or `.upper()` functions!
2. Run the script to test that the program now handles both upper and lower case quit commands.
3. Finally, commit these changes.

### Part 3 - Exception Handling

The last change we will make is to introduce exception handling to deal with non-numeric user input.

1. Modify the `read_numbers_into` function by adding the `try`-`except` statements that we studied in class.
2. In the case of non-numeric input, the program should print a message to the user indicating the problem, and then simply continue with the loop.
3. Run the script to test that the program now handles non-numeric input without crashing.
4. Finally, commit these changes.

## Completing this Lab

Submit your work for the lab activity by _pushing_ your commits to GitHub (i.e., `origin`).

In order to receive full credit for this Lab activity:

1. The `Lab4` subfolder of your repository must contain one Python
    scripts - `average.py` - that reflects the required changes described above.
2. Your script must contain the name of the lab activity, your full name, and
    the date in a comment at the top.
3. Your repository's commit history must show at least three different commits
    reflecting your changes for the two Python files.
4. All of the above must be pushed to GitHub so that I can see it.

Congratulations! You've completed Lab #4.
