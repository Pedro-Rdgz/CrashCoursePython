"""
Start with your program from exercise 9-1. Add an attribute called 
number_served with a default value of 0. Create an instance called 
restaurant called from this calss. Print the number of customers the 
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of 
customers that have been served. Call this method with anew number and
print the value again.
Add a method called increment_number_served() that lets you increment the 
number of customers who've been served. Call this method with any number
you like that could represent how many customers were served in, say, a 
day of business.
"""

class Restaurant():
    """A simple restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 
        self.number_served = 0

    def describe_restaurant(self):
        """ Gives information about the restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name.title()}")
        print(f"The type of cuisine they serve is {self.cuisine_type.title()}")

    def open_restaurant(self):
        """Tells the user that the restaurant is open."""
        print("The restaurant is open. Please come visit us.")

    def customers_served(self):
        print(f"Numbers of costumers served {self.number_served}")

    def set_number_served(self, number):
        self.number_served = number 

    def increment_number_served(self):
        self.number_served += 1 


# Creando una instancia del restaurante
restaurant = Restaurant('flamingos', 'tacos')
restaurant.number_served = 3
restaurant.customers_served()

restaurant.set_number_served(45)
restaurant.customers_served()

restaurant.increment_number_served()
restaurant.customers_served()
