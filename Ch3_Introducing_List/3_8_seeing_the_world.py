"""
Think of at least five places in the world you'd like to visit.
"""

# Store the locations in a list. Make sure the list is not in alphabetical order.
locations = ['japon', 'brasil', 'francia', 'china', 'zelanda']

# Print your list in its original order. Don't worry about printing the list 
# neatly, just print it as a raw Python list.
print("\nLista original")
print(locations)

# Use sorted() to print your list in alphabetical order without modifying
# the actual list.
print("\nUsando sorted sobre la lista: ")
print(sorted(locations))

# Show that your list is still in its original order by printing it.
print("\nLista original")
print(locations)

# Use sorted() to print your list in reverse alphabetical order without 
# changin the order of the original list.
print("\nUsando sorted con reverese=True sobre la lista: ")
print(sorted(locations, reverse=True))

# Show that your list is still in its original order by printing it again.
print("\nLista original")
print(locations)

# User reverse() to change the order of your list. Print the list to show that
# its order has changed.
print("\nUsando reverse() sobre la lista:")
locations.reverse()
print(locations)

# User reverse() to change the order of your list again. Print the list to 
# show it's back to its original order.
print("\nUsando reverse() de nuevo sobre la lista para volverla a su estado original:")
locations.reverse()
print(locations)

# Use sort() to change your list so it's stored in alphabetical order. Print
# the list to show that its order has been changed.
print("\nUsando sort() para cambiar el orden de la lista:")
locations.sort()
print(locations)

# Use sort() to change your list so it's stored in reverse alphabetical order.
# Print the list to show that its order has changed.
print("\nUsando sort() con reverse=True para cambiar el orden de la lista:")
locations.sort(reverse=True)
print(locations)