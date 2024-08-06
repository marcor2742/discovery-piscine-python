#!/usr/bin/env python3

def array_of_names(dict):
	array_of_names = []
	for key in dict:
		array_of_names.append(key.capitalize() + " " + dict[key].capitalize())
	return array_of_names

if __name__ == "__main__":
	try:
		persons = {
			"jean": "valjean",
			"grace": "hopper",
			"xavier": "niel",
			"fifi": "brindacier"
		}
		print(array_of_names(persons))
	except:
		print("exception encountered")