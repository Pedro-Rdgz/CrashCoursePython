"""
Start with the list you used in Exercise 3-1, but instead of just
printing each person's name, print a message to them. The text of 
each message should be the same, but each message should be 
personalized with the person's name.
"""
names = ['pedro', 'andrea', 'rodo', 'kike']
greeting = "Hello "
greeting2 = ", have a nice day!"
print(greeting + names[0].title() + greeting2)
print(greeting + names[1].title() + greeting2)
print(greeting + names[2].title() + greeting2)
print(greeting + names[3].title() + greeting2)