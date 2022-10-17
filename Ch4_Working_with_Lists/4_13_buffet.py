"""
A buffet-style restaurant offers only five basic foods. Think of
five simple foods, and store them in a tuple.
* Use a for loop to print each food the restaurant offers.
* Try to modify one of the items, and make sure that Python 
rejects the change.
* The restaurant changes its menu, replacing two of the items with
different foods. Add a block of code that rewrites the tuple, and then 
use a for loop to print each of the items on the revised menu.
"""

foods = ('arroz', 'frijoles', 'lentejas', 'sopa', 'tacos')

print("\nMenu del restaurante:")
for food in foods:
    print("\t" + food)

# Hacer un error
#foods[1] = 'tortas'

foods = ('arroz', 'frijoles', 'pizza', 'hamburguesas', 'tacos')
print("\nNuevo menu del restaurante:")
for food in foods:
    print("\t", food)