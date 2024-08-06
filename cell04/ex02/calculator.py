#!/usr/bin/env python3

try:
	num1 = int(input("Give me the first number: ").strip())
	num2 = int(input("Give me the second number: ").strip())
	print("Thank you!")

	print(num1, "+", num2, "=", num1 + num2)
	print(num1, "-", num2, "=", num1 - num2)
	if (num2 == 0):
		print("Division by zero is not possible.")
	else:
		print(num1, "/", num2, "=", num1 / num2)
	print(num1, "*", num2, "=", num1 * num2)
except:
	print("Please enter a valid number.")