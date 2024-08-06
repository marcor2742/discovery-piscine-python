#!/usr/bin/env python3

try:
	number = float(input().strip())
	if number < 0:
		print("This number is negative.")
	elif number == 0:
		print("This number is both positive and negative.")
	else:
		print("This number is positive.")
except:
	print("Please enter a valid number.")