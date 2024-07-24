#!/usr/bin/env python3
# A script to convert distance from miles to kilometers, and vice versa

measure = input("Please enter 'miles' or 'kilometers': ")
measure_str = str(measure)

if measure_str == "miles":
	distance_m = input("Enter distance in miles: ")
	dist_m_int = float(distance_m)
	conv_km = round(dist_m_int / 0.62137, 2)
	print("Your new distance is %s kilometers." % conv_km)
elif measure_str == "kilometers":
	distance_k = input("Enter distance in kilometers: ")
	dist_k_int = float(distance_k)
	conv_mi = round(dist_k_int * 0.62137, 2)
	print("Your new distance is %s miles." % conv_mi)
else:
	print("Sorry, I can't do that right now.")

# mandi628; 2024.07.08
