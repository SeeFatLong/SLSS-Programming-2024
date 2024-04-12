# Unit 2 activity
# Author: Bryant Chan
# Date: 8 April 2024

import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to Guess the Number!")
    print("I've picked a secret number between 1 and 100. Can you guess what it is?")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            break

guess_the_number()