# Python Small Projects

A collection of small Python projects, built for practice while learning the language.

## Projects

###  [guess_game.py](./guess_game.py)
A number guessing game. The computer picks a random number between 1 and 100, and the player has to guess it within a limited number of attempts.

- Choose a difficulty level (Easy / Medium / Hard) — each with a different number of chances
- Get feedback after each guess (too high / too low, chances remaining)
- Tracks number of attempts and time taken to win
- Option to play again after each round
- Handles invalid input (non-numbers) and manual exit (Ctrl+C) gracefully

**Run it:**
```bash
python guess_game.py
```

###  [rpg_character.py](./rpg_character.py)
An RPG-style character creator. Validates a character's name and stats, then displays the stats as a visual bar (●○) for Strength, Intelligence, and Charisma.

- Validates the character name (type, length, no spaces, not empty)
- Validates stats (must be integers between 1 and 4, summing to exactly 7)
- Renders each stat as a 10-point dot meter

**Run it:**
```bash
python rpg_character.py
```

## About

These are learning projects — each one was built step by step while getting comfortable with Python fundamentals: functions, loops, conditionals, string formatting, and basic error handling.
