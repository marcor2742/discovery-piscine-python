#!/usr/bin/env python3

import math

try:
	number = float(input("Give me a number: ").strip())
	print(math.ceil(number))
except:
	print("Please enter a valid number.")