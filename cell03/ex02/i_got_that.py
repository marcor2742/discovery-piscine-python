#!/usr/bin/env python3

try:
	str = input("What you gotta say? : ").strip()
	while str != "STOP":
		str = input("I got that! Anything else? : ").strip()
	#while True:
	#	str = input("I got that! Anything else? : ").strip()
	#	if str == "STOP":
	#		break
except:
	print("Please enter a valid number.")