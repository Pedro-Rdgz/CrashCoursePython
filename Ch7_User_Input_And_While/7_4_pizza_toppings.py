"""
Write a loop that prompts the user to enter a series of pizza toppings until they
enter a 'quit' value. As they enter each topping, print a message saying you'll
add that topping to their pizza.
"""

prompt = "\nPlease enter the ingredient that you want in your pizza: "
prompt += "\n(Enter 'quit' to exit) "

flag = True

while flag:
    topping = input(prompt)

    if topping == 'quit':
        flag = False 
    else:
        print(f"\n{topping.title()} will be added to your pizza.")