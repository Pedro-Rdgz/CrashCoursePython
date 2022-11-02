"""
Start with your class from exercise 9-1. Create three different instances
from the class, and call describe_restaurant() for each instance.
"""

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 

    def describe_restaurant(self):
        """ Gives information about the restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name.title()}")
        print(f"The type of cuisine they serve is {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Tells the user that the restaurant is open."""
        print("The restaurant is open. Please come visit us.")

restaurante1 = Restaurant('hoya', 'mexicana')
restaurante2 = Restaurant('pizzarelli', 'italiana')
restaurante3 = Restaurant('gojita', 'japonesa')

restaurante1.describe_restaurant()
restaurante2.describe_restaurant()
restaurante3.describe_restaurant()