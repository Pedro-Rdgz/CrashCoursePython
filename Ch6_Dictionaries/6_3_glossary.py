"""
A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let's call it a glossary.
* Think of five programming words, you've learned about in the previous chapters.
  Use these words as the keys in your glossary, and store their meanings as values.
* Print each word and its meaning as neatly formatted output. You might print
the word followed by a color and then its meaning, or print the word on one line
and then print its meaning indented on a second line. Use the newline character(\n)
to insert a blank line between each word-meaning pair in your output.
"""

glossary = {
    'loop': "Structure that repeats a sequence of instructions until a specific condition is met."
    , 'key': "Is a unique identifier for the complete data used to retrieve it from some location in the structure."
    , 'list': "Is a tool that can be used to store multiple pieces of information at once. "
    , 'types': "An attribute of data."
    , 'dictionary': "Is a general-purpose data structure for storing a group of objects."
    }

print("\nLoop:")
print(f"\t{glossary['loop']}")
print("\nKey:")
print(f"\t{glossary['key']}")
print("\nList:")
print(f"\t{glossary['list']}")
print("\nTypes:")
print(f"\t{glossary['types']}")
print("\nDictionary:")
print(f"\t{glossary['dictionary']}")