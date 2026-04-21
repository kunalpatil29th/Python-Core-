# number_gussing .py
# number_guessing.py

"""
Project: Number Guessing Game
The computer picks a random number, and the user tries to guess it with hints.
"""

import random

def start_game():
    secret_number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10.")
    
    # Simulated guess
    guess = 5
    print(f"User guesses: {guess}")
    
    if guess == secret_number:
        print("Correct!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

start_game()
