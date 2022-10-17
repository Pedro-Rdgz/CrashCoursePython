# Copiar una lista
# Para copiar una lista hacemos uso de los slice pero sin 
# dar ningun indice ([:])

# Creamos una lista con elementos
my_foods = ['pizza', 'falafel', 'carrot cake']
# Creamos una lista nueva, esta sera la copia
# Para copiar la lista hacemos uso del slice vacio ([:])
friend_foods = my_foods[:]

# Agregando nuevos elementos para que se note la diferencia
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)