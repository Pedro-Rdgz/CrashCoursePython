"""
Turn your if-else chain from exercise 5-4 into an if-elif-else chain.
* If the alien is green, print a message that the player earned 5 points.
* If the alien is yellow, print a message that the player earned 10 points.
* If the alien is red, print a message that the player earned 15 points.
* Write three versions of this program, making sure each message is
  printed for the appropiate color alien.
"""

#alien_color = 'green'
#alien_color = 'yellow'
alien_color = 'red'

if alien_color == 'green':
    print("\nYou got 5 points.\n")
elif alien_color == 'yellow':
    print("\nYou got 10 points.\n")
else:
    print("\nYou got 15 points.\n")