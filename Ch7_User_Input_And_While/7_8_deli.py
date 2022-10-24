"""
Make a list called sandwich_orders and fill it with the names of varios sandwiches.
Then make an empty list called finished_sandwiches. Loop through the list of
sandwich orders and print a message for each order, such as I maed your tuna sandwich.
As each sandwich is made, move it to the list of finished sandwiches. After all the
sandwiches have been made, print a message listing each sandwich that was made.
"""
sandwich_orders = ['jamon', 'atun', 'pollo', 'vegano']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThis were the sandwich that were made: ")
for sandwich in finished_sandwiches:
    print("\t" + sandwich)