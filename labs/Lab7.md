# Lab Activity #7 – Using a Graphics Module

## Goals

The goal of this lab time is to learn how to use the author's `graphics.py`
module to draw simple shapes within a graphical window.

## Instructions

In this activity, you will write a small, interactive program that allows
the user to draw a house using several simple shapes.

Create a new `Lab7` subfolder within your work repository.
Then create a new Python source file named `draw_house.py`.

Here is what your program must do:

> You are to write a program that allows the user to draw a simple house using five mouse clicks.
> The first two clicks will be the opposite corners of the rectangular frame of the house.
> The third click will indicate the _center of the top edge_ of a rectangular door.
> The door should have a total width that is `1/5` of the width of the house frame.
> The sides of the door should extend from the corners of the top down to the bottom of the frame.
> The fourth click will indicate the _center_ of a circular window.
> The window radius is half as wide as the door.
> The last click will indicate the peak of the roof.
> The edges of the roof will extend from the point at the peak to the corners of the top edge of the house frame.

__Note:__ You must also display text near the top of the window that indicates to the user what they must do at each step.
Initially, the text should read something like `Click where you want to place the bottom left corner of your house frame.`
Then, the text must change appropriately with each subsequent click.

## Completing this Lab

In order to receive full credit for this Lab activity:

1. The `Lab7` subfolder of your repository must contain at least one Python
    script named `draw_house.py` that meets the requirements above.
2. Your script must contain the name of the lab activity, the names of both members of the team, and
    the date in a comment at the top.
3. Your repository's commit history must show at least two different commits
    reflecting your changes for the two Python files.
4. All of the above must be pushed to GitHub so that I can see it.
