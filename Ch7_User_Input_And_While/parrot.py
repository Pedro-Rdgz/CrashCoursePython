# Uso de la funcion input() para recibir informacion
#message = input("\nTell me something, and I will repeat it back to you: ")
#print(message)

# Usando un ciclo while 
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n"


"""
message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
"""

# Usando una bandera (flag)
# Declarando la bandera con el valor booleano True
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False 
    else:
        print(message)