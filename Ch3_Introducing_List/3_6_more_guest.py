"""
You just found a bigger dinner table, so now more space is 
available. Think of three more guest to invite to dinner.
* Start with your program from exercise 3-4 or exercise 3-5.
Add a print statement to the end of your program informing that you
found a bigger dinner table.
* Use insert() to add one new guest to the beginning of your list.
* User insert() to add one new guest to the middle of your list.
* User append() to add one new guest to the end of your list.
* Print a new set of invitation messages, one for each person in your list.
"""
guest_list = ['batman', 'joker', 'harambe', 'harley']

print("Hello " + guest_list[0] + " you are invited to a dinner.")
print("Hello " + guest_list[1] + " you are invited to a dinner.")
print("Hello " + guest_list[2] + " you are invited to a dinner.")
print("Hello " + guest_list[3] + " you are invited to a dinner.")

print(guest_list[1] + "could not make it to the dinner.\n\n")
guest_list[1] = 'superman'
print("Hello " + guest_list[0] + " you are invited to a dinner.")
print("Hello " + guest_list[1] + " you are invited to a dinner.")
print("Hello " + guest_list[2] + " you are invited to a dinner.")
print("Hello " + guest_list[3] + " you are invited to a dinner.")

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