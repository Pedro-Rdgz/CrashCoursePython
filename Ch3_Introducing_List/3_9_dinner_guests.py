"""
Working with one of the program from exercise 3-4, use len() to print 
a message indicating the number of people you are inviting to dinner.
"""

guest_list = ['batman', 'joker', 'harambe', 'harley']

print("Hello " + guest_list[0] + " you are invited to a dinner.")
print("Hello " + guest_list[1] + " you are invited to a dinner.")
print("Hello " + guest_list[2] + " you are invited to a dinner.")
print("Hello " + guest_list[3] + " you are invited to a dinner.")

print("\nNumber of people invited to dinner: ")
print(len(guest_list))