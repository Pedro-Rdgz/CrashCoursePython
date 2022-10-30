"""
Write a function that accepts a list of items a person wants on
a sandwich. The function should have one parameter that collects 
as many items as the function call provides, and it should print
a summary of the sandwich that is being ordered. Call the function 
three times, using a different number of arguments each time.
"""

def sandwich(*toppings):
    print("\nYour sandwich will have the following ingredients:")
    for t in toppings:
        print("\t" + t)

sandwich('jamon', 'bolonia', 'atun', 'lechuga')
sandwich('pollo')
sandwich('lechuga', 'tomate', 'cebolla', 'queso', 'mayonesa', 'jamon', 'bolonia')