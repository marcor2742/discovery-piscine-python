#!/usr/bin/env python3

try:
	number = int(input().strip())

	while number <= 25:
		print("Inside the loop, my variable is", number)
		number += 1
except:
	print("Please enter a valid number.")