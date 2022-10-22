"""
Start with the program you wrote for exercise 6-1.
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As
you loop through the list, print everything you know about each person.
"""
person_A = {
    'first_name': 'john',
    'last_name': 'cena',
    'age': 40,
    'city': 'thuganomics',
}

person_B = {
    'first_name': 'stone',
    'last_name': 'cold',
    'age': 45,
    'city': 'texas',
}

person_C = {
    'first_name': 'hulk',
    'last_name': 'hogan',
    'age': 60,
    'city': 'hollywood',
}

people = [person_A, person_B, person_C]

for p in people:
    print(f"\nName: {p['first_name'].title()} {p['last_name'].title()}")
    print(f"Age: {p['age']}")
    print(f"Location: {p['city'].title()}")
 
