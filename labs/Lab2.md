# Lab Activity #2 – Numeric Types and Functions

## Goals

Practice using IDLE to create and test a simple Python program that
uses mathematical function to compute numeric solutions. Practice
basic usage of Git with GitHub Desktop. Developing your skills takes
time and practice; please practice repeatedly outside class.

## Prerequisites

This lab assumes that you have:

- A repository named `lastname-work` under our class GitHub Organization.
- Completed both Labs 0 and 1.
- Read up through Chapter 3 of our textbook.

## Skills Acquired/Reinforced Upon Completion

- Basic Git workflow (edit/stage/commit/push) using GitHub Desktop
- Writing a simple, runnable Python script
- Use of Python's `math` module and numeric data types

## Instructions

Using VSCode, write and test a Python program named `doing-math.py` that
solves the problems described in the following sections. Imagine that we
are working to build a video game of some kind.

Note: Please use _type annotation_ and choose concise, mnemonic variable names.

### Part 1 - Computing Distance

For this part, you will compute the distance between the user's position
and a random enemy.

1. Prompt the user to enter their `x` and `y` coordinates. (You'll need assignment statements and the `input`.)
2. Generate a random _x_ and _y_ coordinates for the enemy position. (You'll need the use functions from the `random` module for this.)
3. Compute the distance between the user and the enemy using the Pythagorean theorem. (You'll need the `sqrt` function from the `math` module.)
4. Report to the user how far away is the enemy. (You'll need the `print` function for this.)
5. Run and test your code.
6. When ready, use GitHub Desktop to commit and push.

## Part 2 - Computing Orientation

For this part, you will determine whether the enemy is facing the user.

1. Compute the direction from the enemy to the player. (The formula is `angle = acos( (user_x - enemy_x) / distance )`.)
2. Generate a random angle to be the enemy's orientation. (Again, use a function from the `random` module.)
3. Compute angle between the two orientations as the difference of the user and enemy angles.
4. Report to the user whether the enemy is facing toward them. (The enemy is facing the user if the difference in angles is between -180 and 180.)
5. Run and test your code.
6. When ready, use GitHub Desktop to commit and push.

## Completing this Lab

In order to receive full credit for this Lab activity:

1. The `labs/Lab2` subfolder of your repository must contain a `doing-math.py`
    script that meets the requirements above.
2. Your script must contain the name of the lab activity, your full name, and
    the date in a comment at the top.
3. Your repository's commit history must show at least two different commits
    for your `doing-math.py` file.
4. All of the above must be pushed to GitHub so that I can see it.

Congratulations! You've completed Lab #2.
