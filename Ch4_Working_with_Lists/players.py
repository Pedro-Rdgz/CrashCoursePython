# Trabajando con partes (slice) de una lista
# Para hacer un slice, se da el primer y el ultimo indice
# de los elementos con los cuales se quiere trabajar.
# El ultimo elemento siempre es N - 1 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Mostrando lista completa:")
print(players)
# Mostrando solo una parte de la lista
print("\nMostrando solo los elementos 0,1,2")
print(players[0:3])
print("\nMostrando solo los elementos 1, 2, 3")
print(players[1:4])

# Si omites el primer indice, automaticamente se inicia desde el primero
print("\nOmitiendo primer indice [:4]:")
print(players[:4])

# Si omites el segundo, automaticamente termina hasta el final de la lista
print("\nOmitiendo el segundo indice [2:]:")
print(players[2:])

# Mostrando los ultimos tres elementos de la lista
print("\nMostrando los ultimo tres elementos de la lista con [-3:]")
print(players[-3:])

# Ciclando sobre un slice
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())