"""
A list comprehension combines the for loop and the creation of
new elements into one line, and automatically appends each
new element.
"""

squares = [value**2 for value in range(1, 11)]
print(squares)

mas_cinco = [value + 5 for value in range(0, 11)]
print(mas_cinco)