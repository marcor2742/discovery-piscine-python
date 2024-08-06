#!/usr/bin/env python3

def add_one(n):
	n += 1

if __name__ == "__main__":
	try:
		x = 1
		print(x)
		add_one(x)
		print(x)
	except:
		print("none")