#! /usr/bin/env python3
# Get Programming: Learn to Code with Python, by Ana Bell
# Borrowed from library on 2024.07.05

# Unit 2: Strings, Tuples, and Integrating With the User
# Lesson 12: Capstone Project
# mandi628.codes@gmail.com, 2024.07.10

# GENERAL PROBLEM STATEMENT:
# You want to write a program that automatically combines two names given
# by the user.

# 1. Tell the user to give you two neames in the format FIRST LAST.
# 2. Show the user two possible new names in the format FIRST LAST.
# 3. The new first name is a combination of the two first names given
#   by the user, and the new last name is a combination of the last names
#   given by the user. For example, if the user gives you "Alice Cat" and
#   "Bob Dog", a possible mashup is "Bolice Dot".

# Pseudocode (blocks of code):
# 1. Get user input and store it in variables.
# 2. Split up the full names into first and last names and store them in
#   variables.
# 3. Split up the names with halfway points and store each half in variables
# 4. Combine the first half of one name with the second half of the other
#   name. Repeat for the second set of names.
# 5. Display the results for the user.

print("Welcome to the Mashup Game!")

name1 = input("Enter one full name (FIRST LAST): ")
name2 = input("Enter another full name (FIRST LAST): ")

space = name1.find(" ")
first1 = name1[0:space]
last1 = name1[space+1:]
space = name2.find(" ")
first2 = name2[:space]
last2 = name2[space+1:]

len_first1 = len(first1)
len_last1 = len(last1)
index_first1 = int(len(first1) / 2)
index_last1 = int(len(last1) / 2)

left_first1 = first1[:index_first1]
right_first1 = first1[index_first1:]
left_last1 = last1[:index_last1]
right_last1 = last1[index_last1:]

len_first2 = len(first2)
len_last2 = len(last2)
index_first2 = int(len(first2) / 2)
index_last2 = int(len(last2) / 2)

left_first2 = first2[:index_first2]
right_first2 = first2[index_first2:]
left_last2 = last2[:index_last2]
right_last2 = last2[index_last2:]

new_first1 = left_first1 + right_first2
new_last1 = left_last1 + right_last2
new_first2 = left_first2 + right_first1
new_last2 = left_last2 + right_last1

new_name1 = new_first1 + " " + new_last1
new_name2 = new_first2 + " " + new_last2

print("Your new names are:\n" + new_name1 + "\n" + new_name2)
