#! /usr/bin/env python3

# Get Programming: Learn to Code with Python, by Ana Bell
# Lesson 13 & Lesson 18 material, combined to make a number guessing game.

from random import randrange

play = input("Do you want to play a game? ")

max_tries = 10

while play == "y" or play == "yes" or play == "Yes" or play == "YES" or play == "Y":
    secret = randrange(100)
    print("You have 10 tries to guess my number, between 1 and 100.")
    guess = int(input("Guess my number: "))
    tries = 1
    while guess != secret:
        if guess < secret:
            print(guess, "is too low!")
        elif guess > secret:
            print(guess, "is too high!")
        if tries == max_tries:
            print("You ran out of tries! My number was", secret)
            break
        guess = int(input("Guess again: "))
        tries += 1
    if tries <= max_tries and guess == secret:
        print("It took you", tries, "guesses. You got it!")
    play = input("Do you want to play again? ")
print("Thanks for playing! Have a great day!")
