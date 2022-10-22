"""
Now that you know to loop through a dictionary, clean up the code from exercise 6-3
by replacing your series of print statements with a loop that runs throug the dictionary's
keys and values. When you're sure that your loop works, add five more Python terms
to your glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
"""

glossary = {
    'loop': "Structure that repeats a sequence of instructions until a specific condition is met."
    , 'key': "Is a unique identifier for the complete data used to retrieve it from some location in the structure."
    , 'list': "Is a tool that can be used to store multiple pieces of information at once. "
    , 'types': "An attribute of data."
    , 'dictionary': "Is a general-purpose data structure for storing a group of objects."
    , 'for': "A for loop is used for iterating over a sequence."
    , 'if': "if Statement is used for decision-making operations."
    }

for key, value in glossary.items():
    print(f"\n{key.title()}")
    print(f"\t{value.title()}")