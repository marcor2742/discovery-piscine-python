#!/usr/bin/env python3

try:
	age = int(input("Please tell me your age: ").strip())
	print("You are currently", age, "years old.")
	i = 10
	while i <= 30:
		print("In", i, "years, you'll be", age + i, "years old.")
		i += 10
except:
	print("Please enter a valid number.")