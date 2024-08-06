#!/usr/bin/env python3

try:
	i = 0
	number = int(input().strip())

	while i <= 9:
		print(i, "x", number, "=", i * number)
		i += 1
except:
	print("Please enter a valid number.")