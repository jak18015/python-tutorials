#dependencies
import json
from difflib import get_close_matches

#data
data = json.load(open("data.json"))

#function for finding the definition in the dictionary
def translate(w):
    w = w.lower()

    if w in data:
        return data[w]
    
    elif w.title() in data:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % w.title())
        yn = yn.lower()
        if yn == "y":
            return data[w.title()]
        elif yn == "n":
            return "I don't know what you mean"
        else:
            return "We didn't understand your entry."
        
    elif w.upper() in data:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % w.upper())
        yn = yn.lower()
        if yn == "y":
            return data[w.upper()]
        elif yn == "n":
            return "I don't know what you mean"
        else:
            return "We didn't understand your entry."
        
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
        
    else:
        return "The word doesn't exist. Please double check it."

#input
word = input("Enter word: ")

#function output
output = translate(word)

#print output formatting based on type
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
