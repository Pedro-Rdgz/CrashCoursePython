from fileinput import filename
import json 

# username = input("What is your name? ")

# filename = 'username.json'

# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print(f"We'll remember you when you come back, {username}!")

# Full version

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None 
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        answer = input(f"Is {username} the correct username?(yes/no): ")
        if answer == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
greet_user()