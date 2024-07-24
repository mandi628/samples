#!/usr/bin/env python3

# Copied from Wikipedia article for Python https://en.wikipedia.org/wiki/Python_(programming_language)
n = int(input('Type a number, and its factorial will be printed: '))

if n < 0:
	raise ValueError('Your must enter a non-negative integer')

factorial = 1
for i in range(2, n + 1):
	factorial *= i

print("n! of %d is %d." % (n, factorial))

# mandi628; 2024.07.08
