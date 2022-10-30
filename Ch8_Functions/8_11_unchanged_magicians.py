"""
Start with your work from exercise 8-10. Call the function make_great()
with a copy of the list of magician's names. Because the original list will be 
unchanged, return the new list and store it in a separete list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the great added to each magician's name.
"""
def make_great(magicians):
    """Ading 'the great' to each magician."""
    great_magician = []

    while magicians:
        current_magician = magicians.pop()
        current_magician += " the Great"
        great_magician.append(current_magician)

    return great_magician
    
        
def show_magicians(magicians):
    """Print a list of magicians."""
    for magician in magicians:
        print(magician.title())


magicians = ['quentin', 'alice', 'penny', 'janet', 'john']

great_magician = make_great(magicians[:])
print("\nWithout the great.")
show_magicians(magicians)
print("\nWith the great")
show_magicians(great_magician)