"""
Make a list of your favorite fruits, and then write a series of 
independent if statements that check for certain fruits in your list.
* Make a list of you three favorite fruits and call it favorite_fruits.
* Write five if statements. Each should check whether a certain kind of
  fruit is in your list. If the fruit is in your list, the if block
  should print a statement, such as You really like bananas!
  """

favorite_fruits = ['fresas', 'platano', 'mango', 'uva']

if 'pera' not in favorite_fruits:
    print("\nNo hay peras en tu lista")
if 'platano' in favorite_fruits:
    print("\nDeberias de preparar un licuado de platano.")
if 'pepino' not in favorite_fruits:
    print("\nEl pepino no es una fruta")
if 'mango' in favorite_fruits:
    print("\nEl mango es una fruta exotica.")
if 'brocoli' in favorite_fruits:
    print("\nEste if es false y no saldra en pantalla.")
if 'fresas' in favorite_fruits:
    print("\nHay que preparar fresas con crema.")