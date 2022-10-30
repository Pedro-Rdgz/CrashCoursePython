"""
Write a function called make_shirt() that accepts a size and the text 
of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments.
"""

def make_shirt(size, message):
    print(f"The size of the t-shirt will be {size}.")
    print(f"The message on the t-shirt will be: \n\t{message}\n")

make_shirt('L', 'ola k ase')
make_shirt(size='M', message='hola mundo!!!')