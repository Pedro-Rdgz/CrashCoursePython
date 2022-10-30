"""
Write a function called favorite_book() that accepts one parameter, title.
The function  should print a message, such as One of my favorite books is 
Alice in Wonderland!. Call the function, making sure to include a book title
as an argument in the function call.
"""

def favorite_book(title):
    """Displays a message showing the favorite book of the user."""
    print(f"\nOne of my favorite books is {title.title()}\n")

favorite_book('1Q84')
favorite_book('the magicians')
