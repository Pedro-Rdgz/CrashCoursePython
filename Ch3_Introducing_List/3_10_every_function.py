"""
Think of something you could store in a list. For example, you could make 
a list of mountains, rivers, countries, cities, languages, or anything
else you'd like. Write a program that creates a list  containing these items
and the uses each function introduced in this chapter at least once.
"""

juegos = ['megaman', 'cuphead', 'hades', 'braid', 'punch out']

# Mostrar un juego de la lista
print("\nUno de los mejores juegos de accion-aventura es " + juegos[0].title())

juego_removido = 'braid'

print("\nUn juego se tiene que eliminar de la lista:")
juegos.remove(juego_removido)
print("Este fue el juego que se elimino: " + juego_removido)

print("\nSe agregara un nuevo juego al final de la lista:")
juegos.append('super mario world')
print(juegos)

print("\nSe eliminara el juego con el indice numero 1")
del juegos[1]
print(juegos)

print("\nSe insertara un juego en medio de la lista")
juegos.insert(2, 'zelda')
print(juegos)

print("\nAhora se ordenara la lista de juegos de manera alfabetica")
juegos.sort()
print(juegos)

print("\nAhora se ordenara de manera inversa")
juegos.sort(reverse=True)
print(juegos)

popped_game = juegos.pop()
print("\nEl ultimo juego removido de la lista es " + popped_game)
print(juegos)

print("\nNumero total de juegos en la lista " + str(len(juegos)))