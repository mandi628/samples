#! /usr/bin/env python

# Gradebook App

grades = {}

def add_student(name):
    name = input("What is the student's name? ")
    grades[name] = []

def add_grade(name, score):
    name = input("Which student? ")
    score = int(input("What score did they receive? "))
    grades[name].append(score)

#def final_grade():
    # Find the length of the list 'scores'
#    for grades in grades.values():
    # Return the average of the scores (sum(scores)/len(scores))
    # Print name: average

# Data needs to be saved in an external source

print("\nWelcome to your Gradebook!\n")
action = input("What would you like to do today?\n    1) Add a student\n    2) Add a grade\n    3) View final grades\n\n:: ")

#if action == "1":


#if action == "2":


#if action == "3":


# Give a save option.
# Give an exit program option.
