#!/usr/bin/env python3

import sys

def downcase_it(s: str) -> str:
	return	s.lower()

if __name__ == "__main__":
	try:
		if len(sys.argv) == 1:
			raise ValueError 
		for i in sys.argv[1:]:
			print(downcase_it(i))
	except:
		print("none")