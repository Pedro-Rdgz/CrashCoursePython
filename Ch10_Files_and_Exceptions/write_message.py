filename = './Chapter 10/programming.txt'


#with open(filename, 'w') as file_object:   # Write to a new file, each time it runs it will delete the previous version of the file.
with open(filename, 'a') as file_object:    # Append information at the end of the file. Will not delete the file.
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
