# Ordenando una lista con el metodo sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']

# Usando el metodo sort()
# Este metodo cambia el orden de la lista de manera permanente
print("\nOrdenando en orden alfabetico")
cars.sort()
print(cars)

# Ordenando de manera inversa
print("Ordenando de manera inversa")
cars.sort(reverse=True)
print(cars)

# Ordenando una lista de manera temporal
# Para esto usamos la funcion sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the sorted list in reverse order: ")
print(sorted(cars, reverse=True))

print("\nHere is the original list again: ")
print(cars)

# Mostrando una lista en orden inverso
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nMostrando la lista en orden normal")
print(cars)

# Orden inverso sin ordenar de la lista
cars.reverse()
print("\nOrden inverso sin ordenar la lista")
print(cars)

# El metodo reverse cambia el orden de la lista de manera permanente
# Puedes regresar al orden inicial volviendo a usar reverse() por segunda vez en la lista
cars.reverse()
print("\nRegresando la lista a su estado original")
print(cars)

# Longitud de una lista
cars = ['bmw', 'audi', 'toyota', 'subaru']
# Para mostrar la longitud de una lista usamos la funcion len()
print("\nLongitud de la lista: ")
print(len(cars))
