"""
Modify your program from exercise 6-2 so each person can have more than one favorite
number. Then print each person's name along with their favorite numbers.
"""

favorite_numbers = {
    'person_A': [1, 2, 3],
    'person_B': [4, 5, 6],
    'person_C': [7, 8, 9],
    'person_D': [10, 11, 12],
}

for k,v in favorite_numbers.items():
    print(f"\n{k.title()}'s favorite numbers are:")
    for n in v:
        print(f"\t{n}")