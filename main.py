import art
import random

def game_difficulty(difficulty):
    """Determines the number of attempts based on the difficulty level.
    
    Args:
        difficulty (str): The difficulty level ('easy' or 'hard').
    
    Returns:
        int: Number of attempts (10 for 'easy', 5 for 'hard').
    """
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    return attempts 

def user_guess_check():
    """Gets and validates the user's guess.
    
    Returns:
        int: A number between 1 and 100 entered by the user.
    """
    while True:
        try:
            user_guess = int(input("Make a guess: "))
            if 1 <= user_guess <= 100:
                return user_guess
            print("The number should be between 1 and 100!")
        except ValueError:
            print("The answer should be a number!")
            continue
    
def main_game_action():
    """Runs the main logic of the number guessing game.
    
    The game picks a random number between 1 and 100, lets the user choose a difficulty
    level, and allows guessing until attempts run out or the number is guessed.
    """
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I`m thinking about a number between 1 and 100")
    computer_number = random.randint(1, 100)
    user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    while user_difficulty not in ['easy', 'hard']:
        print("You should write 'easy' or 'hard'")
        user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = game_difficulty(difficulty=user_difficulty)
    print(f"You have {attempts} remaining to guess the number")
    while attempts > 0:
        user_guess = user_guess_check()
        if user_guess < computer_number:
            print("Too low")
            print("Guess again")
        elif user_guess > computer_number:
            print("Too high")
            print("Guess again")
        elif user_guess == computer_number:
            print(f"You got it! The answer was {computer_number}")
            return
        attempts -= 1
        print(f"You have {attempts} remaining to guess the number")
    print(f"You've run out of guesses. The answer was {computer_number}")

main_game_action()
