file_path = './Chapter 10/learningPython.txt'
# Print the contents by reading the entire file
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)
# Loop over the object fle    
with open(file_path) as file_object:
    for line in file_object.readlines():
        print(line.strip())
# Store the lines on a file in a list the print outside of with
with open(file_path) as file_object:
    content = file_object.readlines()

for line in content:
    print(line.strip())

# Replace the word Python with C
for line in content:
    print(line.replace('Python', 'C').strip())

