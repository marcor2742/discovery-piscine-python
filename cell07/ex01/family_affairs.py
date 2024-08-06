#!/usr/bin/env python3

def find_the_redheads(dict):
	myfilter = filter(lambda key: dict[key] == "red", dict)
	return list(myfilter)

if __name__ == "__main__":
	try:
		dupont_family = {
			"florian": "red",
			"marie": "blond",
			"virginie": "brunette",
			"david": "red",
			"franck": "red"
		}
		print(find_the_redheads(dupont_family))
	except:
		print("exception encountered")