"""
Modify the make_shirt() function so that shirts are large by default with a message
that reads I love Python. Make a large shirt and a medium shirt with the default
message, and a shirt of any size with a different message.
"""

def make_shirt(size='L', message='I love Python'):
    print(f"The size of the t-shirt will be {size}.")
    print(f"The message on the t-shirt will be: \n\t{message}\n")

make_shirt('L', 'ola k ase')
make_shirt(size='M', message='hola mundo!!!')
make_shirt()