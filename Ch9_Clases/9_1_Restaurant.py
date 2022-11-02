"""
Make a class called Restaurant. The __init__ method for Restaurant 
should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces
of information, and a method called open_restaurant() that prints a 
message indicating that the restaurant is open.
"""

class Restaurant():
    """A simple restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 

    def describe_restaurant(self):
        """ Gives information about the restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name.title()}")
        print(f"The type of cuisine they serve is {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Tells the user that the restaurant is open."""
        print("The restaurant is open. Please come visit us.")

# Creando una instancia del restaurante
my_restaurant = Restaurant('flamingos', 'tacos')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()