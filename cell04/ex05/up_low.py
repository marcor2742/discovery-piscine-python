#!/usr/bin/env python3

str = input().strip()
i = 0
while i < len(str):
	if str[i].isupper():
		print(str[i].lower(), end="")
	else:
		print(str[i].upper(), end="")
	i += 1
print()