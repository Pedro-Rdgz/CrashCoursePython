"""
All versions of foods.py in this section have avoided using for loops
when printing to save space. Choose a version of foods.py, and write
two for loops to print each list of foods.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']

# Creamos una lista nueva, esta sera la copia
# Para copiar la lista hacemos uso del slice vacio ([:])
friend_foods = my_foods[:]

# Agregando nuevos elementos para que se note la diferencia
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)