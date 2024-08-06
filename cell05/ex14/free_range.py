#!/usr/bin/env python3

import sys

try:
	array = []

	if len(sys.argv) != 3:
		print("none")
	else:
		for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
			array.append(i)
		print(array)
except:
	print("none")
