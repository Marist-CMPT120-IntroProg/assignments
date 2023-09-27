# Lab Activity #3 – Writing Simple Functions

## Goals

Gain familiarity with creating and calling functions of one or more arguments.
You will also practice writing simple test cases to validate your computations.

### Prerequisites

This lab assumes that you have:

- read up to and including Chapter 6 of our textbook;
- basic experience with Python/IDLE and Git;

### Skills Acquired/Reinforced Upon Completion

- Create functions that perform arithmetic computations.
- Create functions that operate on lists.
- Create functions that test the results of your other functions.

## Example - Pythagorean Theorem

Consider the following example.

First, we write a function to compute the Pythagorean theorem. That is,
the function takes the lengths of two sides of a triangle, adjacent to its
right angle, and then computes the length of the hypoteneuse (the side
opposite the right angle).

```python
def pythagorean(a, b):
    sumOfSquares = a**2 + b**2
    hypoteneuse = math.sqrt(sumOfSquares)
    return hypoteneuse
```

Next, we write a function that will test the first function. This test
function must call the other function multiple times with different
arguments in order to ensure that the first function works correctly.
It is up to the test writer to think of _test cases_ which exercise
as many scenarios as possible, especially _edge cases_.

```python
def testPythagorean():
    # Case 1
    answer = 5
    result = pythagorean(3, 4)
    print("Case 1 correct?", result == answer)

    # Case 2
    answer = 10
    result = pythagorean(8, 6)
    print("Case 2 correct?", result == answer)

    # Case 3 - degenerate triangle
    answer = 17
    result = pythagorean(0, 17)
    print("Case 3 correct?", result == answer)

```

It is important to try to test enough cases to be confident that the
original function is correct. Think about what the "edge cases" might
be. For the Pythagoream Theorem, one "edge case" might be for a so-called
degenerate triangle, when the length of one side is 0. Then, we would
expect the hypoteneuse to be the same length as the remaining side.

You can test in the IDLE Shell by calling the test function.

```
>>> testPythagorean()
Case #1 correct? True
Case #2 correct? True
Case #3 correct? True
```

## Instructions - Area of a Rectangle

For this exercise, you should create a new Python script named `area.py`
in a `Lab3` subfolder.

Write a function that takes two numbers - representing the width and height
of a rectangle, respectively - and uses those two numbers to compute the area
of the corresponding rectangle.

Write a function that will call the first function with specific values
for the widths and heights of some rectangles, and then check the results
against known answers, printing the results of each comparison.

Finally, write a main function that calls the test function, and be sure to
call the main function at the end of your script.

### Commit your changes

Before continuing to the next exercise, use GitHub Desktop to commit your
changes for the `area.py` file with a meaningful summary message.

## Instructions - Sum of Squares

For this exercise, you should create a new Python script named `sumsquares.py`
also in the `Lab3` subfolder.

Write a function that takes a list of numbers and returns the sum of the
squares of each number in the list. Again, you do not need to write a main
function.

Write a function that will call the first function with specific lists
of numbers and check the results against known answers, printing the results
of each comparison.

Finally, write a main function that calls the test function, and be sure to
call the main function at the end of your script.

### Commit your changes

To submit your work for the lab activity, use GitHub Desktop to commit your
changes for the `sumsquares.py` file with a meaningful summary message and
then push all your new commits to GitHub (i.e., `origin`).

## Completing this Lab

In order to receive full credit for this Lab activity:

1. The `Lab03` subfolder of your repository must contain two Python
    scripts - `area.py` and `sumsquares.py` - that meet the requirements above.
2. Your scripts must contain the name of the lab activity, your full name, and
    the date in a comment at the top.
3. Your repository's commit history must show at least two different commits
    reflecting your changes for the two Python files.
4. All of the above must be pushed to GitHub so that I can see it.

Congratulations! You've completed Lab #3.
