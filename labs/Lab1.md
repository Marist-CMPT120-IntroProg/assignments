# Lab Activity #1 – Getting Started with Git and Python

## Goals

Practice basic usage of Git with GitHub Desktop. Practice using IDLE to create
and test a simple Python program. Using these tools effectively takes time and
practice; please practice repeatedly outside class.

## Prerequisites

This lab assumes that you have:

- Signed up on GitHub and joined the GitHub Organization for the class;
- Created your own `lastname-work` repository to your own account;
- Completed Lab 0 during the first week of class;
- Read Chapters 1 and 2 of our textbook.

## Skills Acquired/Reinforced Upon Completion

- Basic Git workflow (edit/stage/commit/push) using GitHub Desktop
- Writing a simple, runnable Python script
- Git commands
    - `git config` – set your name and email address
    - `git clone` – copy remote repository to your local machine
    - `git push` and `git pull` – upload/download changes to remote repository
    - `git add` – stage changes to a file
    - `git commit` – record a new version of your code

## The Tools

- **Integrated Development Environment (IDE)** - We will being with VSCode, a
ligthweight and modern application for editing and running source code, including
Python code. An IDE brings several tools together in one application: the Python
interpreter and compiler; an editor with syntax highlighting and other features;
and additional tools such as and integrated debugger, etc. (Later on we will
explore a more sophisticated and powerful IDE.)
- **Version control system** - We will use Git through the graphical GitHub
Desktop application, which runs on both Windows and Mac. Git is one of the most
popular version control systems. As usual, there are a variety of other choices
for interacting with Git, but we'll start with this simple tool that is integrated
with the GitHub website.

## Coding in Python – Variables & Strings

Using VSCode, write and test a [Mad Libs™](https://www.madlibs.com/) program
named `madlib.py` that prompts the user to enter a series of words (ideally,
of differing parts of speech) and then uses those input words to construct an
amusing story. Your story should include at least four sentences in two
paragraphs, and you should prompt the user for at least eight (8) different
words. Consider the following sample output (along with hypothetical user
input) from a partial solution:

```
    Enter a noun: pillow
    Enter a verb: whirl
    Enter an adjective: fancy
    Enter a place: stadium

    George bought a fancy pillow. He planned to whirl it at the stadium!
```

Here's how you can get started:

1. **Open your local repo in VSCode.** Launch VSCode and then select "Open Folder" from the File menu. Browse and select your local `lastname-work` repository folder to open it in the IDE.
2. **Start a new Python script.** From the Explorer tool, click the "New Folder..." icon to create a new folder named `Lab1`. Then, with the new `Lab1` folder selected, click the "New File..." icon to create a new script named `madlibs.py`.
3. Here is a short program to serve as a starting point. Type the following code into your new `madlibs.py` file.
    ```python
    # Introduction to Programming
    # Author: [your name here]
    # Date: [today's date here]
    def main():
        print("Welcome to my MadLibs(R) program!")
        print()
        print("Please enter the following words: ")
        noun1 = input("A noun: ")
        verb1 = input("A verb: ")

        print("YOUR STORY:")
        print("Once upon a time, a " + noun1 + " wanted to " + verb1 + " among the stars.")
    main()
    ```
4. **Test your program.** From the “Run” menu, select “Run Module” to execute your Python script. You should see a new REPL window appear and the “Hello, instructor!” message will be displayed. If you encounter an error, then try to figure out what went wrong and fix it. Move on when you Hello program is working correctly.

## Tracking Your Work with Git

Next, you will tell Git to track your new file by staging and commiting your changes.

1. Launch GitHub Desktop if it is not already open, and make sure that your `lastname-work` repository is selected.
2. GitHub Desktop automatically stages your changes, so you need only commit them. Type a short, descriptive message in the Summary box (the Description is optional) and then click the blue "Commit" button.
3. Once the commit is finished, you should see an option in the window to "Push origin". Click this button to upload your changes to the GitHub cloud.
4. Refresh your repository's GitHub page in a Web browser to see that your changes are now present in the cloud.

## Fleshing Out Your Story

Continue in the same manner to expand your program and make a longer story with at least two paragraphs.
The user should have to enter at least ten (10) different words of various kinds - nouns, verbs, adjectives, colors, etc.
Try to use between 1 and 3 words in each sentence of your story.

Stage, commit, and push your work to GitHub using GitHub Desktop.

## Completing this Lab

In order to receive full credit for this Lab activity:

1. The `labs/Lab1` subfolder of your repository must contain a `madlibs.py`
    script that meets the requirements above.
2. Your script must contain the name of the lab activity, your full name, and
    the date in a comment at the top.
3. Your repository's commit history must show at least two different commits
    for your `madlibs.py` file.
4. All of the above must be pushed to GitHub so that I can see it.

Congratulations! You've completed Lab #1.
