#! /usr/bin/env python3
# Get Programming: Learn to Code in Python, by Ana Bell
# Borrowed from library 2024.07.05

# Unit 3: Making Decisions in Your Programs
# Lesson 13: Introducing Decisions in Programs


print("Welcome to Chocolate Bar Decider!")

hungry = input("Are you hungry? (yes or no) ")

if hungry == "yes":
    price = float(input("How much does a chocolate bar cost? "))
    if price < 1:
        print("Buy every chocolate bar.")
        bars = 100
    if 1 <= price <= 5:
        print("Buy 10 chocolate bars.")
        bars = 10
    if price > 5:
        print("Buy one chocolate bar.")
        bars = 1
    if bars > 10:
        print("Cashier says: someone's hungry!")

if hungry == "no":
    print("Stick to the list!")

