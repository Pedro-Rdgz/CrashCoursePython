"""
Add an if to hello_admin.py to make sure the list of users is not empty.
* If the list is empty, print the message We need to find some users!
* Remove all of the usernames from your list, and make sure the correct
  message is printed.
"""

users = []

if users:
    for user in users:
        if user == 'admin':
            print("\nHello admin, would you like to see a status report?\n")
        else:
            print(f"\nHello {user.title()}, thank you for logging in again.")
else:
    print("\nWE NEED TO FIND SOME USERS!!!\n")