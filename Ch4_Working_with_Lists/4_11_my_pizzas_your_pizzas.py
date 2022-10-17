"""
Start with your program from exercise 4-1. Make a copy of the list of 
pizzas, and call it friend_pizzas. Then, do the following:
* Add a new pizza to the original list.
* Add a different pizza to the list friend_pizzas.
* Prove that you have two separate lists. Print the message, 'My favorite
pizzas are:', and then use a for loop to print the first list. Print the 
message, 'My friend's favorite pizzas are:', and then use a for loop to 
print the second list. Make sure each new pizza is stored in the
appropiate list.
"""

pizzas = ['mexicana', 'peperoni', 'hawaiana', 'carnes', 'pollo']

# Creando la copia de la lista
friend_pizzas = pizzas[:]

# Agregando una nueva pizza a la lista original
pizzas.append('italiana')

# Agregando una nueva pizza a la copia
friend_pizzas.append('atun')

# Mostrando que las listas son diferentes
print("\nMis pizzas favoritas son:")
for pizza in pizzas:
    print(pizza)

print("\nLas pizzas favoritas de mi amigo son:")
for pizza in friend_pizzas:
    print(pizza)