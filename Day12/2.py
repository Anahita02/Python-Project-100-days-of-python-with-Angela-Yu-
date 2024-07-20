#Final Project
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURN = 5

def check_ans(guess, num, turn):
    """checks answer against guess. Returns the number of turns remaning."""
    if guess > num:
        print("Too high")
        return turn - 1
    elif guess < num :
        print("Too low")
        return turn - 1
    else:
        print("You got it! The number was {num}.") 

def set_dificulty():
    ans = input(f"Choose a dificulty. Type 'easy' or 'hard': ")
    if ans == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURN

def game():
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    num = random.randint(1,100)

    turn = set_dificulty()

    guess = 0

    while guess != num:

        print(f"You have {turn} attempts ramaning to guess the number.")
        guess = int(input(f"Make a guess: "))

        turn = check_ans(guess, num, turn)
        if turn == 0 :
            print("You've run out of guesses, you lose.")
            return
        elif guess != num:
            print("Guess again.")
game()