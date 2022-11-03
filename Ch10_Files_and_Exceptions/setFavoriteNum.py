import json 

filename = 'favoriteNumber.json'

try:
    with open(filename) as file:
        favNum = json.load(file)
except FileNotFoundError:
    favNum = input("Please enter your favorite number: ")
    with open(filename, 'w') as file:
        json.dump(favNum, file)
else:
    print(f"I know your favorite number! It's {favNum}!")

