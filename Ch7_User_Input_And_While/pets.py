# Removiendo todas las instacias de un valor de una lista

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# Usamos remove dentro de un ciclo para remover todas las instancias del valor
while 'cat' in pets:
    pets.remove('cat')

print(pets)