#!/usr/bin/env python3
# Copyright 2024 mandi628
# E-mail: mandi627.codes@gmail.com
# License

# Title
# https://mandi628.github.io/____

import math

def area(shape, n):
    return shape(n)

def perimeter(shape, n):
    return shape(n)

def volume(shape, n):
    return shape(n)

def sq_area(length):
    return length*length

def sq_perimeter(length):
    return length*4

def sq_volume(length):
    return (length*length)*length

def rec_area(length, width):
    return length*width

def rec_perimeter(length, width):
    return (length*2) + (width*2)

def rec_volume(length, width, height):
    return (length*width)*height

def circ_area(radius):
    return round((radius*math.pi)**2, 2)

def circ_perimeter(radius):
    return round(2*math.pi*radius, 2)

def circ_volume(radius, height):
    return round(((math.pi*radius)**2)*height, 2)

def tri_perimeter(side1, side2, side3):
    return side1 + side2 + side3

def tri_area(base, height):
    return round((base*height)/2, 2)

def tri_volume(base_l, base_w, height):
    return round((base_l*base_w*height)/3, 2)

print("What would you like to calculate:\n    1) Perimeter\n    2) Area\n    3) Volume\n")
calc = input("Enter 1, 2, or 3: ")

if calc == "1":
    print("\nPlease choose your shape:\n    A) Square\n    B) Rectangle\n    C) Circle\n    D) Triangle\n")
    shape = input("Enter A, B, C, or D: ")
    if shape == "A":
        length = int(input("\nEnter the length of the side: "))
        print("\nThe perimeter of a square with side", length, "is", sq_perimeter(length))
    elif shape == "B":
        length = int(input("\nEnter the length of the shape: "))
        width = int(input("Enter the width of the shape: "))
        print("\nThe perimeter of a rectangle with length", length, "and width", width, "is", rec_perimeter(length, width))
    elif shape == "C":
        radius = int(input("\nEnter the radius of the circle: "))
        print("\nThe circumference of a circle with the radius", radius, "is", circ_perimeter(radius))
    elif shape == "D":
        side1 = int(input("\nEnter the length of side no. 1: "))
        side2 = int(input("Enter the length of side no. 2: "))
        side3 = int(input("Enter the length of side no. 3: "))
        print("\nThe perimeter of a triangle with sides", side1, ", ", side2, ", and", side3, "is", tri_perimeter(side1, side2, side3))
    else:
        print("\nOperator error. Please try again.")
elif calc == "2":
    print("\nPlease choose your shape:\n    A) Square\n    B) Rectangle\n    C) Circle\n    D) Triangle\n")
    shape = input("Enter A, B, C, or D: ")
    if shape == "A":
        length = int(input("\nEnter the length of the side: "))
        print("\nThe area of a square with side", length, "is", sq_area(length))
    elif shape == "B":
        length = int(input("\nEnter the length of the shape: "))
        width = int(input("Enter the width of the shape: "))
        print("\nThe area of a rectangle with length", length, "and width", width, "is", rec_area(length, width))
    elif shape == "C":
        radius = int(input("\nEnter the radius of the circle: "))
        print("\nThe area of a circle with the radius", radius, "is", circ_area(radius))
    elif shape == "D":
        base = int(input("\nEnter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        print("\nThe area of a triangle with base", base, "and height", height, "is", tri_area(base, height))
    else:
        print("\nOperator error. Please try again.")
elif calc == "3":
    print("\nPlease choose your shape:\n    A) Cube\n    B) Rectangle Cube\n    C) Cylinder\n    D) Pyramid\n")
    shape = input("Enter A, B, C, or D: ")
    if shape == "A":
        length = int(input("\nEnter the length of the side: "))
        print("\nThe volume of a square cube with sides", length, "is", sq_volume(length))
    elif shape == "B":
        length = int(input("\nEnter the length of the shape: "))
        width = int(input("Enter the width of the shape: "))
        height = int(input("Enter the height of the shape: "))
        print("\nThe volume of a rectangle cube with length", length, ", width", width, "and height", height,  "is", rec_volume(length, width, height))
    elif shape == "C":
        radius = int(input("\nEnter the radius of the cylinder: "))
        height = int(input("Enter the height of the cylinder: "))
        print("\nThe volume of a cylinder with the radius", radius, "and height", height, "is", circ_volume(radius, height))
    elif shape == "D":
        base_l = int(input("\nEnter the base length: "))
        base_w = int(input("Enter the base width: "))
        height = int(input("Enter the height of the pyramid: "))
        print("\nThe volume of a pyramid with base length", base_l, ", base width", base_w, "and height", height, "is", tri_volume(base_l, base_w, height))
    else:
        print("\nOperator error. Please try again.")
else:
    print("I'm sorry. That is not an option today. Please try again later.")
