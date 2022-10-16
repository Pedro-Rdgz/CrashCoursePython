"""
You just foud out that your new dinner table won't arrive in time for the 
dinner, and you have space for only two guests.
* Start with your program from exercise 3-6. Add a new line that prints
a message saying that you can invite only two people for dinner.
* Use pop() to remove guest from your list one at at time until only
two names remain in your list. Each time you pop a name from your list,
print a message to that person letting them know you're sorry you can't 
invite them to dinner.
* Print a message to each of the two people still on your list, letting 
them know they're still invited.
* Use del to remove the last two names from your list, so you have an
empty list. Print your list to make sure you actually have an empty list
at the end of your program.
"""
guest_list = ['batman', 'joker', 'harambe', 'harley']

print(guest_list[1] + "could not make it to the dinner.\n\n")
guest_list[1] = 'superman'


print("\nHello, I have just found a bigger table so more people are joining!")
print(guest_list)
guest_list.insert(0, 'flash')
print(guest_list)
guest_list.insert(2, 'green lanter')
print(guest_list)
guest_list.append('wonder woman')
print(guest_list)
print("Hello " + guest_list[0] + " you are invited to a dinner.")
print("Hello " + guest_list[1] + " you are invited to a dinner.")
print("Hello " + guest_list[2] + " you are invited to a dinner.")
print("Hello " + guest_list[3] + " you are invited to a dinner.")
print("Hello " + guest_list[4] + " you are invited to a dinner.")
print("Hello " + guest_list[5] + " you are invited to a dinner.")
print("Hello " + guest_list[6] + " you are invited to a dinner.")

print("\nSorry to inform you that I can only invite two people to dinner.")
popped_guest = guest_list.pop()
print("I'm sorry " + popped_guest + " that I can't invite you to dinner.")
popped_guest = guest_list.pop()
print("I'm sorry " + popped_guest + " that I can't invite you to dinner.")
popped_guest = guest_list.pop()
print("I'm sorry " + popped_guest + " that I can't invite you to dinner.")
popped_guest = guest_list.pop()
print("I'm sorry " + popped_guest + " that I can't invite you to dinner.")
popped_guest = guest_list.pop()
print("I'm sorry " + popped_guest + " that I can't invite you to dinner.")
print("\n")
print("Hello " + guest_list[0] + " you are still invited to the dinner.")
print("Hello " + guest_list[1] + " you are still invited to the dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)