"""
Make a list of magician's names. Pass the list to a function 
called show_magicians(), which prints the name of each magician in the list.
"""

magicians = ['quentin', 'alice', 'penny', 'janet', 'john']

def show_magicians(magicians):
    """Print a list of magicians."""
    for magician in magicians:
        print(magician)

show_magicians(magicians)