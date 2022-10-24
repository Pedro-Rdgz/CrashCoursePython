"""
Using the list sandwich_orders from exercise 7-8, make sure that sandwich 
'pastrani' appears in the list at least three times. Add code near the beginning
of your program to print a message saying the deli has run out of pastrani, 
and then use a while loop to remove all occurrences of 'pastrani' from sandwich_orders.
Make sure no pastrami sandwiches end up in finished_sandiwches.
"""
sandwich_orders = ['jamon', 'pastrani', 'atun', 'pastrani', 'pollo', 'pastrani', 'vegano']
finished_sandwiches = []

print("\nThe deli has run out of pastrami.\n")
while 'pastrani' in sandwich_orders:
    sandwich_orders.remove('pastrani')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThis were the sandwich that were made: ")
for sandwich in finished_sandwiches:
    print("\t" + sandwich)