def guest_book():
    name = ''
    filename = './Chapter 10/guest_book.txt'
    while name != 'none':
        name = input("What's your name? (Enter none to quit): ")

        if name != 'none':
            with open(filename, 'a') as file:
                file.write(name + '\n')

guest_book()