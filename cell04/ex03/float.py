#!/usr/bin/env python3

try:
	number = float(input("Give me a number: ").strip())
	int_num = int(number)

	if number == int_num:
		print("This number is an integer.")
	else:
		print("This number is a decimal.")

except:
	print("Please enter a valid number.")