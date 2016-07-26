# have the computer think of an integer between 1 and 100
# have a human guess the number responding "higher" or "lower" for incorrect guesses
# bonus points: keep a high-score table with names that persists between runs

import random

MIN_NUM = 1
MAX_NUM = 100

def guessing_game():
    number = random.randint(MIN_NUM, MAX_NUM)
    num_guesses = 0
    guessed = False
    while not guessed:
        guess = int(input("Guess a number between {} and {}: ".format(MIN_NUM, MAX_NUM)))
        num_guesses += 1
        if number == guess:
            guessed = True
            print("Yay! You got it in {} tries!!".format(num_guesses))
        elif guess < number:
            print("Higher...")
        else:
            print("Lower...")


guessing_game()