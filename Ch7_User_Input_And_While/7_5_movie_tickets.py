"""
A movie theater charges different ticket prices depending on a person's age.
If a person is under the age of 3, the ticket is free; if they are between 
3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15.
Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

flag = True
while flag:
    age = int(input("Please enter your age (0 to exit) "))
    if age == 0:
        flag = False
    else:0
        if age < 3:
            price = "free"
        elif age >= 3 and age <= 12:
            price = 10
        elif age > 12:
            price = 15 
        
        if price == "free":
            print("\nYour ticket is free.")
        else:
            print(f"\nThe cost of your ticket is ${price}.")