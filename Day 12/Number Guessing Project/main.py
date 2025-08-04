from mimetypes import guess_all_extensions

import art
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty_level = input("Choose difficulty. Type 'easy' or 'hard': ")

    if difficulty_level.lower() == "easy":
        num_turns = EASY_LEVEL_TURNS
    elif difficulty_level.lower() == "hard":
        num_turns = HARD_LEVEL_TURNS
    else:
        print("That is not a valid choice. Game over.")
        return

    answer = random.randint(1,100)

    while num_turns > 0:
        print(f"You have {num_turns} attempts remaining to guess the number")

        guess = int(input("Make a guess: "))
        num_turns -= 1

        if answer > guess:
            print("Too low.")
        elif answer < guess:
            print("Too high.")
        else:
            print(f"You got it! The answer is {answer}")
            return

    print("You've run out of guesses. Refresh the page to run again.")
    return

game()
