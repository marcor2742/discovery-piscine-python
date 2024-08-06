#!/usr/bin/env python3

import sys

def shrink(s: str) -> str:
	return s[:8]

def enlarge(s: str) -> str:
	return s + (8 - len(s)) * 'Z'

if __name__ == "__main__":
	try:
		if len(sys.argv) == 1:
			raise ValueError 
		for i in sys.argv[1:]:
			if len(i) == 8:
				print(i)
			elif len(i) > 8:
				print(shrink(i))
			else: 
				print(enlarge(i))
	except:
		print("none")