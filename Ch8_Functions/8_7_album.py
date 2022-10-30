"""
Write a function called make_album() that builds a dictionary describing a 
music album. The function should take in an artist name and a album title,
and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums.
Print each return value to show that the dictionaries are storing the album
information correctly.
"""

def make_album(artist_name, album_title):
    """Function to build a dictionary with an artist information."""
    information = {'artist': artist_name, 'album': album_title}
    return information

print(make_album('foster the people', 'torches'))
print(make_album('blink 182', 'enema of the state'))
print(make_album('cafe tacuba', 're'))