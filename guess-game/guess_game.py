import random
import time
import json


EASY_CHANCES = 10
MEDIUM_CHANCES = 5
HARD_CHANCES = 3
EXIT_MESSAGE = "\nExit..."


class GuessingGame:
    def __init__(self) -> None:
        self.difficulty: str | None = None
        self.chances: int | None = None
        self.number: int | None = None
        self.attempts: int = 0

    # Computer selects a random number between 1 and 100.
    def select_random_number(self) -> None:
        self.number = random.randint(1, 100)

    # User chooses a difficulty level and receives attempts.
    def user_choose_difficulty_level(self) -> bool:
        modes: dict[str, tuple[str, int]] = {
            "1": ("Easy", EASY_CHANCES),
            "2": ("Medium", MEDIUM_CHANCES),
            "3": ("Hard", HARD_CHANCES),
        }
        try:
            while True:
                choice = input("Enter your choice: ")
                if choice in modes:
                    self.difficulty, self.chances = modes[choice]
                    print(f"\nGreat! You have selected the {self.difficulty} difficulty level.\nLet's start the game!")
                    return True
                else:
                    print("Please enter 1, 2 or 3")
        except KeyboardInterrupt:
            print(EXIT_MESSAGE)
            return False


    # User tries to guess the number.
    def user_guess_try(self) -> None | bool:
        assert self.number is not None
        assert self.chances is not None
        start: float = time.perf_counter()
        while True:
            try:
                user_guess = int(input("\nEnter your guess number: "))
                if user_guess != self.number:
                    self.chances -= 1
                    self.attempts += 1
                    direction:str = "greater" if self.number > user_guess else "less"
                    print(f"Incorrect! The number is {direction} than {user_guess}. You have {self.chances} attempts.")
                    if self.chances == 0:
                        print(f"You lose :( The number was {self.number}")
                        return False
                else:
                    self.attempts += 1
                    end: float = time.perf_counter()
                    print(
                        f"Congratulations! You guessed the correct number {self.number} in {self.attempts} attempts in {end - start:.1f} sec."
                    )
                    return True
            except KeyboardInterrupt:
                print(EXIT_MESSAGE)
                return None
            except ValueError:
                print("\nIt should be a number!")
                continue

    # Shows the user's score for this round.
    def user_score(self) -> None:
        print(f"Difficulty: {self.difficulty}, Attempts: {self.attempts}")
        data = self.check_file()
        
        data.append({
            "difficulty:" : self.difficulty,
            "attempts" : self.attempts
        })
        self.write_file(data)
        
    def check_file(self):
        try:
            with open('data.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            return []
        
    def write_file(self, data):
        with open("data.json", "w") as f:
            json.dump(data, f, indent=2)
        
    # TODO: user_hints() — planned for giving hints to the user  
    def user_hints(self) -> None:
        pass


welcome_input_message = """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have few chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n"""


# Start the game.
while True:
    print(welcome_input_message)
    game = GuessingGame()
    if not game.user_choose_difficulty_level():
        break
    game.select_random_number()
    won = game.user_guess_try()
    if won is None:
        break
    game.user_score()

    try:
        play_again = input("\nWould you like to play again? Yes/No: ")
        if play_again.lower() not in ("yes", "y"):
            print(EXIT_MESSAGE)
            break
    except KeyboardInterrupt:
        print(EXIT_MESSAGE)
        break
