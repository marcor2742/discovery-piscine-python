#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("none")
else:
	if sys.argv[1] == input("What was the parameter? "):
		print("Good job!")
	else:
		print("Nope, sorry...")