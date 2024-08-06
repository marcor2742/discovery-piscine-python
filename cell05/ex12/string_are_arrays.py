#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("none")
else:
	found = False
	for i in sys.argv[1]:
		if i == "z":
			print(i, end="")
			found = True
	if not found:
		print("none")