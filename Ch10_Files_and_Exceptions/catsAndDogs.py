filenames = ['cats.txt', 'dog.txt']

def readFile(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        pass
    

for filename in filenames:
    readFile(filename)