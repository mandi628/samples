#!/usr/bin/env python3
# A script to convert distance from miles to kilometers, and vice versa

scale = input("Are you converting 'distance' or 'weight': ")
scale_str = str(scale)

if scale_str == "distance":
    measure = input("Please enter 'miles' or 'kilometers': ")
    measure_str = str(measure)
    if measure_str == "miles":
        distance_m = float(input("Enter distance in miles: "))
        conv_km = round(distance_m / 0.62137, 2)
        print("Your new distance is %s kilometers." % conv_km)
    elif measure_str == "kilometers":
        distance_k = float(input("Enter distance in kilometers: "))
        conv_mi = round(distance_k * 0.62137, 2)
        print("Your new distance is %s miles." % conv_mi)
elif scale_str == "weight":
    weight = input("Please enter 'pounds' or 'kilograms': ")
    weight_str = str(weight)
    if weight_str == "kilograms":
        weight_k = float(input("Enter the weight in kilograms: "))
        conv_lb = round(weight_k * 2.204, 2)
        print("Your new weight is %s pounds." % conv_lb)
    elif weight_str == "pounds":
        weight_p = float(input("Enter the weight in pounds: "))
        conv_kg = round(weight_p / 2.204, 2)
        print("Your new weight is %s kilograms." % conv_kg)
else:
	print("Sorry, I can't do that right now.")

# mandi628; 2024.07.17; added weight conversion to original distance conversion
