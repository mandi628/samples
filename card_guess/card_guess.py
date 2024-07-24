#!/usr/bin/env python

# Get Programming: Learn to Code with Python, by Ana Bell

# Unit 5: Organizing Your Code Into Reuseable Blocks
# Lesson 21: Achieveing modularity and abstraction with fuctions

# mandi628.codes@gmail.com; github.com/mandi628

# Upgrade notes:
#    -- randomize card selection (currently, the 8 hearts is set)
#    -- remember cards chosen and don't allow for reselection

print("Let's Play Guess My Card!")

def guessed_card(number, suit, bet):
    money_won = 0
    guessed = False
    if number == "8" and suit == "hearts":
        money_won = 10 * bet
        guessed = True
    else:
        money_won = bet / 10
    return(money_won, guessed)

#print(guessed_card(8, "hearts", 10)) # result is (100, True)
#print(guessed_card("8", "hearts", 10)) # result is (10.0, False)
#guessed_card(10, "spades", 5) # no print


#print(did_win) # False
#print(amount) # 8.0

print("\n~~~~~~~~\n")

bank = 100.00

print("Your starting bank is $", bank)
play = input("Are you ready to play? (y/n): ")

while play == "y":
    number = input("Enter a card number (A-10, J, Q, K): ")
    suit = input("Enter a suit (hearts, spades, clubs, diamonds: ")
    bet = int(input("How much do you want to bet? $ "))
    
    (amount, did_win) = guessed_card(number, suit, bet)
    bank = bank - bet + amount
    
    if did_win == True:
        print("Great guess! You won $", amount)
        print("Your new bank is $", bank)
        play = input("\nDo you want to play again? (y/n) ")
    else:
        print("Sorry - better luck next time. You lost $", (bet - amount))
        print("Your new bank is $", bank)
        play = input("\nDo you want to play again? (y/n) ")

print("\nThanks for playing! Have a great day!")
