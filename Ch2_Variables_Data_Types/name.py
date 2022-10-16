# Declarando y asignando un valor a una variable
name = "ada lovelace"

# Convierte en mayuscula la primera letra de cada palabra
print(name.title())

# Convierte a mayuscula toda la cadena
print(name.upper())

# Convierte a minuscula toda la cadena
print(name.lower())

# Concatenacion de cadenas
first_name = "pedro"
last_name = "rodriguez"
# Concatenando los valores de las variables
# usando el simbolo (+)
full_name = first_name + " " + last_name

print(full_name)
print("Hello, " + full_name.title() + "!")
# Concatenando datos dentro de una variable
message = "Hello, " + full_name.title() + "!"
print(message)

# Cortando espacios en blanco
favorite_language = 'python ' # Agregando un espacio al final
print(favorite_language)
print(favorite_language.rstrip()) # Remueve un espacio en el lado derecho
print(favorite_language)

print(favorite_language.lstrip()) # Remueve un espacio en el lado izquierdo