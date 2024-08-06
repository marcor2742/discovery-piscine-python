#!/usr/bin/env python3

import sys

try:
	if len(sys.argv) != 1:
		print("none")
	else:
		number = 0
		while number <= 10:
			print("Table de", number, ":", end="")
			i = 0
			while i <= 10:
				print("", i * number, end="")
				i += 1
			print()
			number += 1
except:
	print("Please enter a valid number.")