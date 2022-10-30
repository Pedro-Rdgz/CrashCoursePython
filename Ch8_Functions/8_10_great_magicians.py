"""
Start with a copy of your program from exercise 8-9.
Write a function called make_great() that modifies the list of magicians
by adding the phrase 'the Great' to each magician's name. Call show_magicians()
to see that the list has actually been modified.
"""

def make_great(magicians):
    """Ading 'the great' to each magician."""
    great_magician = []

    while magicians:
        current_magician = magicians.pop()
        current_magician += " the Great"
        great_magician.append(current_magician)

    while great_magician:
        current_magician = great_magician.pop()
        magicians.append(current_magician)
    
        
def show_magicians(magicians):
    """Print a list of magicians."""
    for magician in magicians:
        print(magician.title())

magicians = ['quentin', 'alice', 'penny', 'janet', 'john']

make_great(magicians)
show_magicians(magicians)