"""
Do the following to create a program tha simulates how websites ensure 
that everyone has a unique username.
* Make a list of five or more usernames called current_users.
* Make another list of five usernames called new_users. Make sure one or
  two of the new usernames are also in the current_users list.
* Loop through the new_users list to see if each new username has already
  been used. If it has, print a message that the person will need to enter a 
  new username. If a username has not been, print a message saying that the 
  username is available.
* Make sure your comparision is case insensitive. If 'John' has been used,
  'JOHN' should not be accepted.
"""
current_users = ['azcino', 'chuty', 'wos', 'bnet', 'rapder']

new_users = ['dominic', 'papo', 'vallest', 'gazir', 'WOS', 'chutY']

for n_u in new_users:
    if n_u.lower() in current_users:
        print(f"{n_u} is not available, please enter a new username.")
    else:
        print(f"{n_u} is available.")