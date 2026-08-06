import random
import time

# import json


""" 
A simple number guessing game where 
the computer randomly selects a number and the user has to guess it. 
The user will be given a limited number of chances to guess the number. 
If the user guesses the number correctly, the game will end, and the user will win. 
Otherwise, the game will continue until the user runs out of chances.
"""
EASY_CHANCES = 10
MEDIUM_CHANCES = 5
HARD_CHANCES = 3
EXIT_MESSAGE = "\nExit..."


def select_random_number():
    number = random.randint(1, 100)
    return number


def user_choose_difficulty_level():
    modes = {
        "1": ("Easy", EASY_CHANCES),
        "2": ("Medium", MEDIUM_CHANCES),
        "3": ("Hard", HARD_CHANCES),
    }
    try:
        while True:
            choice = input("Enter your choice: ")
            if choice in modes:
                difficulty, chances = modes[choice]
                print(
                    f"\nGreat! You have selected the {difficulty} difficulty level.\nLet's start the game!"
                )
                return difficulty, chances
            else:
                print("Please enter 1, 2 or 3")
    except KeyboardInterrupt:
        print(EXIT_MESSAGE)
        return None, None


def user_guess_try(number, chances):
    start = time.perf_counter()
    attempts = 0
    while True:
        try:
            user_guess = int(input("\nEnter your guess number: "))
            if user_guess != number:
                chances -= 1
                attempts += 1
                direction = "greater" if number > user_guess else "less"
                print(
                    f"Incorrect! The number is {direction} than {user_guess}. You have {chances} attempts."
                )
                if chances == 0:
                    print(f"You lose :( The number was {number}")
                    return attempts, False

            else:
                attempts += 1
                end = time.perf_counter()
                print(
                    f"Congratulations! You guessed the correct number {number} in {attempts} attempts in {end - start:.1f} sec."
                )
                return attempts, True

        except KeyboardInterrupt:
            print(EXIT_MESSAGE)
            return attempts, None
        except ValueError:
            print("\nIt should be a number!")
            continue


def user_score(difficulty, attempts):
    score = {"Difficulty": difficulty, "Attempts": attempts}
    print(f"Difficulty: {score['Difficulty']}, Attempts: {score['Attempts']}")
    return score


welcome_input_message = """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have few chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n"""


while True:
    print(welcome_input_message)
    difficulty, chances = user_choose_difficulty_level()
    if difficulty is None:
        break
    number = select_random_number()

    attempts, won = user_guess_try(number, chances)
    if won is None:
        break
    score = user_score(difficulty, attempts)

    try:
        play_again = input("\nWould you like to play again? Yes/No: ")
        if play_again.lower() != "yes" and play_again.lower() != "y":
            print(EXIT_MESSAGE)
            break
    except KeyboardInterrupt:
        print(EXIT_MESSAGE)
        break
