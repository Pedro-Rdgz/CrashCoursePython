file_path = '/home/pedro/Coding/Python_Programming/Chapter 10/pi_digits.txt'

# Reading all contents of the file
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents)

# Reading line by line the contents of the file
# with open(file_path) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# Making a list of lines from a file
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
