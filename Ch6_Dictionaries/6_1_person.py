"""
Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live.
You should have keys such as first_name, last_name, age, and city. 
Print each piece of information stored in your dictionary.
"""

person = {
    'first_name': 'john',
    'last_name': 'cena',
    'age': 40,
    'city': 'Thuganomics',
}

print(f"\nName: {person['first_name'].title()} {person['last_name'].title()}")
print(f"Age: {person['age']}")
print(f"City: {person['city'].title()}")
