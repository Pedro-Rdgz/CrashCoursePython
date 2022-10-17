# TUPLAS
# Las tuplas son como listas la unica diferencia es que no puedes 
# modificar su contenido, son inmutables.

# Definiendo una tupla, se usan parentesis () en vez de corchetes []
dimensions = (200, 50)
# Se puede acceder al elemento igual que en una lista por medio de un indice
print(dimensions[0])
print(dimensions[1])

# Tratando de modificar un elemento de la lista (error)
# dimensions[0] = 250

# Usar un ciclo for para mostrar el contenido de la tupla
print("\nUsando un ciclo for para mostrar los elementos de la tupla:")
for dimension in dimensions:
    print(dimension)

# Asignando nuevos valores a la variable que contiene la tupla
# Aqui se pierden los valores originales y se usan los nuevos 
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
    print(dimension)