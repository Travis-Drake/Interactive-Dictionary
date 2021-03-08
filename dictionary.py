import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))
loop = True

def translate(w):
	if w in data:
		return data[w]
	else:
		match = get_close_matches(word, data.keys())
		if len(match)>0:
			return (f"The word doesn't exist. Did you mean to type any of these?: {match} ")
		else:
			return "The word doesn't exist. Please check your spelling."

while loop:
	word = input("Type your word (enter q to quit): ")
	word = word.lower()
	if word == "q":
		loop = False
	else:
		print(translate(word))