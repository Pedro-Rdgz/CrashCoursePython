# Usando un break para salir de un ciclo
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break 
    else:
        print(f"\nI'd love to go to {city.title()}!")