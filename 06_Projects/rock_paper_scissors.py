# rock_paper_scissors.py

"""
Project: Rock, Paper, Scissors
A classic game played against the computer.
"""

import random

def play():
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    user = "rock" # Simulated input
    
    print(f"User: {user} | Computer: {computer}")
    
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("User wins!")
    else:
        print("Computer wins!")

play()
