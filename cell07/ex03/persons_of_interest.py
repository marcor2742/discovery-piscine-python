#!/usr/bin/env python3

def famous_births(dict):
	ordered_dict = sorted(dict.items(), key = lambda x: x[1]['date_of_birth'])
	
	for item in ordered_dict:
		x = item[0]
		print(f"{dict[x]['name']} is a great scientist born in {dict[x]['date_of_birth']}")

if __name__ == "__main__":
	try:
		women_scientists = {
			"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
			"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
			"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
			"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
		}

		famous_births(women_scientists)
	except:
		print("exception encountered")