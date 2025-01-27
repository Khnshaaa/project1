#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
#Hello! What is your name?
#KBTU

#Well, KBTU, I am thinking of a number between 1 and 20.
#Take a guess.
#12

#Your guess is too low.
#Take a guess.
#16

#Your guess is too low.
#Take a guess.
#19
#Good job, KBTU! You guessed my number in 3 guesses!

import random

def guess_the_number():
    # Generate a random number between 1 and 20
    number_to_guess = random.randint(1, 20)
    # Initialize variables for guesses
    guess_count = 0
    guessed = False
    while not guessed:
        print("Take a guess:")
        guess = int(input())
        guess_count += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            guessed = True
            print(f"Good job! You guessed the number in {guess_count} guesses.")
guess_the_number()
