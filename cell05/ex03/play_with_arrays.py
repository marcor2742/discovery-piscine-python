#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
myset = set(())

for i in array:
	if i > 5:
		myset.add(i + 2)

print(array)
print(myset)