# Lab Activity #8 – Getting Started with OOP

## Goals

The goal of this lab time is to practice object-oriented programming by writing and using simple classes.

## Instructions

Create a new `Lab8` subfolder within your work repository. Then create a new Python source file in this folder and name it `shapes.py`.

### Part I - Circles

Define a class that represents a `Circle`.

1. Write a constructor/initializer. Circles have a `radius`.
2. Write an _observer_ (i.e., "getter") method for this field.
3. Write a _mutator_ (i.e., "setter") method for this field.
4. Write additional observers that compute the `perimeter` and `area` of the shape.
5. Write a `main` function that instantiates your `Circle` class and tests its methods.
    - Be sure to create two instances to demonstrate the that methods produce different results for each instance.
6. Commit and push your work before continuing.

### Part II - Rectangles

Define a class that represents a `Rectangle`.

1. Write a constructor/initializer. Rectangles must have a `width` and `height`.
2. Write _observer_ (i.e., "getter") methods for these two fields.
3. Write _mutator_ (i.e., "setter") methods for these two fields.
4. Write additional observers that compute the `perimeter` and `area` of the shape.
5. Add to your `main` function so that you instantiate and test the methods of your `Rectangle` class.
    - Be sure to create two instances to demonstrate the that methods produce different results for each instance.
6. Commit and push your work before continuing.

### Part III - 3D Boxes

Define a class that represents a `Box`.

1. Write a constructor/initializer. Boxes must have a `depth` and a `Rectangle` (which itself has width and height).
2. Write _observer_ (i.e., "getter") methods for width, height, and depth. (For width and height, you should get the width/height of the contained Rectangle.)
3. Write _mutator_ (i.e., "setter") methods for these fields. (Again, for width and height, you should set the width/height of the contained Rectangle.)
4. Write an observers that computes the `volume`of the Box.
    - The volume of a Box is just the product of its width, height and depth.
5. Add to your `main` function so that you instantiate and test the methods of your `Box` class.
    - Be sure to create two instances to demonstrate the that methods produce different results for each instance.
6. Commit and push your work before continuing.

## Completing this Lab

In order to receive full credit for this Lab activity:

1. The `Lab8` subfolder of your repository must contain at least one Python script named `shapes.py` that meets the requirements above.
2. Your script must contain the name of the lab activity, the names of both members of the team, and the date in a comment at the top.
3. Your repository's commit history must show at least three different commits reflecting your changes for this Python file.
4. All of the above must be pushed to GitHub so that I can see it.
