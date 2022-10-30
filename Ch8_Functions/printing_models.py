# Modificando una lista dentro de una funcion

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#  Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design.
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

###########################################################################
# El mismo codigo pero con funciones
print("\n\nEl mismo codigo pero usando funciones.\n\n")
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Usando las funciones
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Para mandar una copia de una lista en vez de la original se hace lo siguiente
#  function_name(list_name[:])
# Ejemplo:
#  print_models(unprinted_designs[:], completed_models)
# Nota: consume mas memoria y tiempo realizar esto
