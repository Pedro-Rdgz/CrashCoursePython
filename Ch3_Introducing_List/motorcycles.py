motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Cambiando el valor del primer elemento de la lista
#motorcycles[0] = 'ducati'
#print(motorcycles)

# Agregando un nuevo elemento a la lista
# Usando append(), el nuevo elemento se agrega al final de la lista 
motorcycles.append('ducati')
print(motorcycles)

# Creando una lista vacia para agregarle valores despues
motorcycles = [] # Lista vacia

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Se puede insertar un nuevo elemento usando insert()
# Con insert podemos indicar en que posicion queremos el nuevo elemento
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removiendo un elemento usando del
# Se usa del si se sabe la posicion del elemento que queremos remover
del motorcycles[0]
print(motorcycles)

# Usando pop() para remover el ultimo elemento de la lista (tambien se puede indicar la posicion)
# Este elemento se guarda en una variable para poder hacer uso de él
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)

# Otro ejemplo usando pop()
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Otro ejemplo usando pop() e indicando una posicion
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# Removiendo un elemento por su valor
print("\nUsando remove()")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# Usando remove() e indicandole el valor del elemento a remover
#motorcycles.remove('ducati')
#print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() +  " is too expensive for me.")