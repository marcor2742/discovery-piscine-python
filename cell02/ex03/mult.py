#!/usr/bin/env python3

try:
	first = float(input("Enter the first number:\n").strip())
	second = float(input("Enter the second number:\n").strip())
	result = first * second
	print(first, "*", second, "=", result)

	if result < 0:
		print("This result is negative.")
	elif result == 0:
		print("This result is positive and negative.")
	else:
		print("This result is positive.")
except:
	print("Please enter a valid number.")
