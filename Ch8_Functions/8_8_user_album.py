"""
Start with your program from exercise 8-7. Write a while loop that allows
users to enter an album's artist and title. Once you have that information,
call make_album() with the user's input and print the dictionary that's created.
Be sure to include a quit value in the while loop.
"""

def make_album(artist_name, album_title):
    """Function to build a dictionary with an artist information."""
    information = {'artist': artist_name, 'album': album_title}
    return information

while True:
    print("\nPlease enter artist information (input 'q' to exit):")
  
    artist = input("Enter artist name: ")
    if artist == 'q':
        break
    
    album = input("Enter album title: ")
    if album == 'q':
        break 

    print(make_album(artist, album))



