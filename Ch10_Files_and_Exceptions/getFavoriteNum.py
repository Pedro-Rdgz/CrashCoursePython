import json 

filename = 'favoriteNumber.json'

with open(filename) as file:
    favNum = json.load(file)
    print(f"I know your favorite number! It's {favNum}!")