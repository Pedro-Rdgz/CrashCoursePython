from selectors import EpollSelector


def addition():
    while True:
        n1 = input('Enter first number: ')
        n2 = input('Enter second number: ')

        try:
            print(int(n1) + int(n2))
            break
        except ValueError:
            print('Please use only numbers.')


addition()