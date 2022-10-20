"""
You don't have to limit the number of test you create to 10.
If you want to try more comparisons, write more tests and add
them the conditional_tests.py. Have at least one True and one False
result of the following:
* Tests for equality and inequality with strings.
* Tests using the lower() function.
* Numerical tests involving equality and inequality, greater
  than and less than, greater than or equal to, and less
  than or equal to.
* Test using the and keyword and the or keyword.
* Test whether an item is in a list.
* Test whether an item is not in a list.
"""

mensaje = "hola mundo"

print("\nEs mensaje == Game over? Resultado = False")
print(mensaje == 'Game over')

print("\nEs mensaje != Game over? Resultado = True")
print(mensaje != 'Game over')

palabra = 'PLAYER'
print("\nEs palabra == player? Resultado = False")
print(palabra == 'player')
print("\nEs palabra == player? Resultado = True")
print(palabra.lower() == 'player')

num = 10
print("\nEs num >= 5 y num < 100? Resultado = True")
print(num >= 5 and num < 100)
print("\nEs num == 5 o num != 7? Resultado = True")
print(num == 5 or num != 7)

lista = ['megaman', 'mario world', 'metroid', 'minecraft']
game = 'cuphead'

print("\nEsta game dentro de la lista? Resultado = False")
print(game in lista)

print("\ngame no esta en la lista? Resultado = True")
print(game not in lista)