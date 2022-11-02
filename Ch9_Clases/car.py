# Trabajando con clases e instancias

class Car():
    """ A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributers to describe a car."""
        self.make = make 
        self.model = model 
        self.year = year 
        # Agregando un valor default para un atributo (no se necesita mandar como atributo en este caso)
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    # Modificando el valor de un atributo a travez de un metodo
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else:
            print("You can't roll back an odometer!")

    # Incrementando el valor de un atributo a traves de un metodo
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles 

# Creando instancias de la clase Car 

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modificando el valor de un atributo de manera directa
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modificando el valor de un atributo a travez de un metodo
my_new_car.update_odometer(24)
my_new_car.read_odometer()

# Incrementando el valor de un atributo a traves de un metodo
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()