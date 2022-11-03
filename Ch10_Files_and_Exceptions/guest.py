def tellMeYourName():
    name = input("Name: ")
    filename = './Chapter 10/guest.txt'

    with open(filename, 'w') as file:
        file.write(name)

tellMeYourName()