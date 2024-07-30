#! /usr/bin/env python

print("Welcome to the Shopping Helper!")

go = input("Would you like to manage your list? (y/n) ")

shop = []

while go == "y":
    print("\nHere are your options:\n     1) View my list (v)\n     2) Add to my list (a)\n     3) Remove from my list (r)")
    action = input("\nWhat would you like to do? (v/a/r) ")
    if action == "v":
        print(shop)
    elif action == "a":
        shop.append(input("What would you like to add? "))
        print(shop)
    elif action == "r":
        rmv = shop.index(input("What would you like to remove? "))
        shop.pop(rmv)
        print(shop)
    go = input("\nWould you like to do anything else? (y/n) ")
print("Thank you for using the Shopping Helper!")
