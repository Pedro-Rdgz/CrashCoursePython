# Mas de diccionarios

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")

# Recorriendo el diccionario con un ciclo for
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#  Ciclando solo las llaves (keys)
print("\nPrinting only the keys from the dictionary:")
# Imprimiendo solo las llaves con el metodo keys
# Usando for name in favorite_languages: daria el mismo resultado
# keys es el comportamiento default 
for name in favorite_languages.keys():
    print(name.title())

# Extendiendo el ejemplo
print("\n\nExtendiendo el ejemplo\n")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(f"Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")

# Revisar si un elemento esta dentro del diccionario
print("\nRevisando si existe un elemento dentro del diccionario.")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Ordenando elementos, Python versiones anteriores a la 3.6 no ordenaban elementos
# dentro de un diccionario
print("\nOrdenando elementos dentro de un diccionario.")
print("Ya no es necesario realizar esto en python 3.6 en adelante.")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Ciclando solo los valores de las llaves del diccionario
print("\nCiclando solo los valores de las llaves del diccionario.")
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Para no mostrar elementos repetidos usamos SET
print("\nMostrando la misma lista sin elementos repetidos con la ayuda de SET")
for language in set(favorite_languages.values()):
    print(language.title())

# Creando un diccionario con listas como valores
print("\n\nListas dentro del diccionario.")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
    
# Refinandolo
print("\nRefinandolo.")
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is:\n\t{languages[0].title()}")