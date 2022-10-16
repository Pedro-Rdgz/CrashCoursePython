"""
You just heard that one of your guests can't make the dinner, so you need to send
out a new set of invitations. You'll have to think of someone else to invite.
* Start with your program from exercise 3-4. Add a print statement at the end
of your program stating the name of th eguest who can't make it.
* Modify your list, replacing the name of the guest who can't make it
with the name of the new person you are inviting.
* Print a second set of invitation messages,, one for each person who is
still in your list.
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
