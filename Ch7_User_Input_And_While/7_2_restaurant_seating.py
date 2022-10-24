"""
Write a program that asks the user how many people are in their dinner group.
If the answer is more than eight, print a message saying they'll have to wait 
for a table. Otherwise, report that their table is ready.
"""

clients = int(input("\nHow many people are in your group? "))

if clients > 8:
    print("\nYou'll have to wait for a table.")
else:
    print("\nYour table is ready.")