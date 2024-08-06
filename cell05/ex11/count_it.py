#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
	print("none")
else:
	print("parameters:", len(sys.argv) - 1)
	i = 1
	for i in range(1, len(sys.argv)):
		print(sys.argv[i], ": ", len(sys.argv[i]), sep="")