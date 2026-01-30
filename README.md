# python-akinator
An akinator that guesses members of my CS class!

I worked on this project with my classmate, @ElijahCassidy. His repository for this project is here: https://github.com/ElijahCassidy/Akinator-Project1 

I had lots of fun making this project.

## Project Summary

The game (named Guess Who: Classroom Edition) is a text-based Python guessing game where the computer tries to guess a classmate you’re thinking of by asking a series of yes/no questions. The game includes a tutorial, input validation, and replay functionality.

## Program Overview

The program:

1. Greets the user and asks for their name and age
1. Validates user input (especially age)
1. Optionally walks the user through a tutorial
1. Asks a series of yes/no questions to guess a classmate
1. Confirms whether the guess was correct
1. Allows the user to replay the game multiple times
1. The game is designed to work for one specific classroom group.

## Key Features

- Interactive command-line gameplay

- Tutorial mode for first-time players

- Input validation for age and responses

- Confirmation function to handle correct/incorrect guesses

- Tracks how many times the user has played

- Replay option without restarting the program

## Instructions to Run
### Requirements:

- Python 3.x

- No external libraries required

### How to Run the Project

1. Make sure Python 3 is installed on your computer.

2. Save the file as something like:
```
guess_who.py

```
3. Navigate to the folder containing the file.

4. Run the program using python.

### How to Play

1. Enter your name and age when prompted.

2. Choose whether to view the tutorial.

3. Think of a classmate from the supported class group.

4. Answer questions using exactly:
  - yes
  - no
The program will try to guess the student.

5. Confirm whether the guess was correct.

6. Press ENTER to play again or S to exit.

## Example Gameplay
```
Hello there! Welcome to Guess Who: Classroom Edition!
What is your name? Alex
How old are you, Alex? 14
...
Guess Who: Classroom Edition
Write T for tutorial.
Press ENTER to play.
...
My first question: Is your student a boy? yes
Does your student’s name begin with letters A-M? yes
Does your student have glasses? no
...
I know it! Your student is Adam Reisfeld!
Right? yes
Yay, I got it!
```
## File Key
- **pythonator_logic_tree.xlsx** includes my original logic tree
- **AkinatorProject** includes the python code for the project.
