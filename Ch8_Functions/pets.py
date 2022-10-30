# Argumentos posicionales

# Agregaremos un argumento por defecto
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Usando keyword arguments
# Aqui no importa si los mandas en diferente orden, porque le estas indicando 
#  cual corresponde a cual.
describe_pet(pet_name='choco', animal_type='cat')


# Agregaremos un argumento por defecto
# Al agregar un argumento por defecto debemos de colocarlo al final de la funcion
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')
describe_pet('flan', 'cat')
describe_pet(pet_name='wilfred', animal_type='cat')