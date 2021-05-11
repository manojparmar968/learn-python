"""
Write a Python program that simulates the "Rock, Paper, Scissors" game.

The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").

The player should play against the computer, which will select a random option.

The computer's selection will be compared against the player's selection to determine who wins.

A descriptive message should be displayed indicating if the player won, lost, or if the game ended in a tie.

Basic Game Rules:

    Paper beats Rock

    Rock beats Scissors

    Scissors beat Paper.

Hints:
You will need to use nested conditionals (conditionals within conditionals) to implement this game.

To generate a random choice for the computer player, you may use the random module and the randint function.
"""

import random

options = ("rock","paper","scissors")
computer = options[random.randint(0,2)]

print("==== Welcome to the game ====")
player = input("Please enter Rock, Paper, or Scissor below: \n")

if player.lower() == computer:
    print("Its a tie! Try again.")
elif player.lower() == "rock":
    if computer == "paper":
        print("You lose! your apponent chose 'Paper'")
    else:
        print("YOu win! Your apponent chose 'Scissors'")
elif player.lower() == "paper":
    if computer == "scissors":
        print("You lose! your apponent chose 'Scissors'")
    else:
        print("YOu win! Your apponent chose 'Rock'")
elif player.lower() == "scissors":
    if computer == "rock":
        print("You lose! your apponent chose 'Rock'")
    else:
        print("YOu win! Your apponent chose 'Paper'")
else:
    print("Please enter a valid option.")