import random
import time

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


def select_random_number():
    number = random.randint(1, 100)
    return number


def user_choose_difficulty_level():
    modes = {
        '1': ('Easy', EASY_CHANCES),
        '2': ('Medium', MEDIUM_CHANCES),
        '3': ('Hard', HARD_CHANCES)}
    try:
        while True:
            choice = input('Enter your choice: ')
            if choice in modes:
                name, chances = modes[choice]
                print(f"\nGreat! You have selected the {name} difficulty level.\nLet's start the game!")
                return chances
            else:
                print('Please enter 1, 2 or 3')
    except KeyboardInterrupt:
        print('\nExit...')


def user_guess_try(number, chances):
    start = time.perf_counter()
    attempts = 0
    try:
        while True:
            user_guess = int(input('\nEnter your guess number: '))
            if user_guess != number:
                chances -= 1
                attempts += 1
                direction = 'greater' if number > user_guess else 'less'
                print(f'Incorrect! The number is {direction} than {user_guess}. You have {chances} attempts.')
                if chances == 0:
                    print(f"You lose :( The number was {number}")
                    break
            else:
                attempts += 1
                end = time.perf_counter()
                print(f'Congratulations! You guessed the correct number {number} in {attempts} attempts in {end - start:.1f} sec.')
                break
            
    except KeyboardInterrupt:
        print('\nExit...')
    except ValueError:
        print('\nIt should be a number!')


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
    chances = user_choose_difficulty_level()
    number = select_random_number()
    user_guess_try(number, chances)
    try:
        play_again = input('\nWould you like to play again? Yes/No: ')
        if play_again.lower() != 'yes' and play_again.lower() != 'y':
            print('\nExit...')
            break
    except KeyboardInterrupt:
        print('\nExit...')
        break