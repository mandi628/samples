#! /usr/bin/env python3

# Get Programming: Learn to Code with Python, by Ana Bell
# Borrowed from library 2024.07.05

# Unit 3: Making Decisions in Your Programs
# Lesson 15: Capstone Project: Choose Your Own Adventure
# mandi628.codes@gmail.com

# You'll use conditionals and branching to create a story. At each scene,
# the user will enter a word. The word will tell the program which path
# to continue following. Your program should handle all possible paths
# that the user might choose, but doesn't need to handle any unexpected
# input from the user.

# Setting up the rules
print("Welcome to the Adventure!")
print("You are on a deserted island in a 2D world.")
print("Try to survive until rescue arrives!")
print("Available commands are in CAPITAL letters.") #How to play
print("Any other command exits the game.") #Unexpected behavior
print("First LOOK around...")

do = input(":: ")
if do == "LOOK":
    print("You are stuck in a sand ditch.")
    print("Crawl out LEFT or RIGHT?")

    do = input(":: ")
    if do == "LEFT":
        print("You see a STARFISH and a CRAB on the sand.")
        print("And you're hungry! Which do you eat?")

        do = input(":: ")
        if do == "STARFISH":
            print("Oh no! You immediately don't feel well.")
            print("You do not survive :(")

        elif do == "CRAB":
            print("Raw crab should be fine, right? YES or NO?")

            do = input(":: ")
            if do == "YES":
                print("Ok, you eat it raw. Fingers crossed.")
                print("Food in your belly helps you see a TREE.")

                do = input(":: ")
                if do == "TREE":
                    print("It's a coconut tree! And you're thirsty!")
                    print("Do you drink the coconut water? YES or NO")

                    do = input(":: ")
                    if do == "YES":
                        print("Oh boy. Coconut water and raw crab don't mix.")
                        print("You do not survive!")

                    elif do == "NO":
                        print("Good choice.")
                        print("The sun is setting and you see two caves.")
                        print("Do you choose the cave on the LEFT or the RIGHT?")

                        do = input(":: ")
                        if do == "RIGHT":
                            print("This cave is roomy and dry.")
                            print("You will SLEEP well tonight.")

                            do = input(":: ")
                            if do == "SLEEP":
                                print("It is now morning and you are rested, but hungry again.")
                                print("Do you get your COCONUT or HUNT for something else?")

                                do = input(":: ")
                                if do == "COCONUT":
                                    print("That coconut was rotten and made you sick.")
                                    print("You do not survive.")

                                elif do == "HUNT":
                                    print("Great job! You found food!")
                                    print("And just in time, a rescue ship arrives!")

                        elif do == "LEFT":
                            print("Oh no! A bear has already chosen this cave!")
                            print("You do not survive.")

            elif do == "NO":
                print("Well, there's nothing else left to eat.")
                print("You do not survive :(")

    elif do == "RIGHT":
        print("No can do. That side is very slippery.")
        print("You fall very far into some weird cavern.")
        print("You do not survive.")

else:
    print("You can only do actions shown in capital letters.")
    print("Try again!")
