"""
Make a dictionary called cities. Use the names of three cities as keys in your
dictionary. Create a dictionary of information about each city and include the 
country that the city is in, approximate population, and one fact about that city.
The keys for each city's dictionary should be something like country, population,
and a fact. Print the name of each city and all of the information you have
stored about it.
"""

cities = {
    'tijuana': {
        'country': 'mexico',
        'population': '12345',
        'fact': 'los mejores tacos',
    },
    'barcelona': {
        'country': 'españa',
        'population': '123456',
        'fact': 'algunos no hablan español'
    }
}

for keys, values in cities.items():
    print(f"\nCity of {keys.title()}:")
    for k,v in values.items():
        print(f"\t{k.title()}: {v.title()}")
