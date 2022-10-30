"""
Write a function called city_country() that takes in th ename of a city 
and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with a least three city-country pairs, and print the 
value that's returned.
"""

def city_country(city, country):
    """Function that returns a string with a city and its country."""
    city_country = city + ', ' + country
    return city_country.title()

print(city_country('santiago','chile'))
print(city_country('paris', 'francia'))
print(city_country('tokio', 'japon'))