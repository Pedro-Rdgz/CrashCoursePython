"""
Using one of the programs you wrote in this chapte, add several lines
to the end of the program that do the following:
* Print the message, 'The first three items in the list are:'. Then
use a slice to print the first three items from that program's list.
* Print the message, 'Three items from the middle of the list are:'.
Use a lisce to print three items from the middle of the list.
* Print the message, 'The last three items in the list are:'. Use a
slice to print the last three items in the list.
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'nadal', 'marquez']
print("Mostrando lista completa:")
print(players)

print("\nLos primeros tres elementos de la lista son:")
print(players[:3])

print("\nLos tres elementos de en medio de la lista son:")
print(players[2:5])

print("\nLos tres ultimos elementos de la lista son: ")
print(players[-3:])