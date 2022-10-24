"""
Write a program that polls users about their dream vacation.
Write a prompt similar to 'If you could visit one place in the world,
where would you go? Include a block of code that prints the result of the poll.
"""
# Diccionario vacio para guardar las respuestas 
responses = {}

# Crear bandera para terminar el ciclo
flag = True

while flag:
    name = input("\nPlease enter your name: ")
    city = input("\nIf you could visit one place in the world, where would you like to go? ")

    responses[name] = city 

    continuar = input("\nContinue with the poll? (yes/no)")
    if continuar == 'no':
        flag = False 

for k, v in responses.items():
    print(f"\n{k.title()} would like to travel to {v.title()}.")
