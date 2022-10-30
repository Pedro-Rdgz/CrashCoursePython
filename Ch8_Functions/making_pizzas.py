
# Si usamos import para importar todo un modulo, cada funcion sera
# invocada de la siguiente manera
# module_name.function_name()

import pizza_module

pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Para importar una funcion en especifico de un modulo 
# from module_name impor function_name 
# De esta manera no es necesario usar la notacion de punto y solo
# se usa el nombre de la funcion 
# Para llamar mas funciones solo se usa una coma
# from module_name impor function_0, function_1, function_2

from pizza_module import make_pizza

make_pizza(18, 'pepperoni')
make_pizza(14, 'mushrooms', 'green peppers', 'extra cheese')

# Podemos usar un alias para cambiar el nombre de la funcion a importar
# usando la keyword as seguido del alias
# from module_name import function_name as fn 
from pizza import make_pizza as mp
mp(20, 'pepperoni')
mp(16, 'mushrooms', 'green peppers', 'extra cheese')

# Tambien podemos darle un alias al modulo completo
# import module_name as mn 
import pizza_module as p
p.make_pizza(22, 'pepperoni')
p.make_pizza(18, 'mushrooms', 'green peppers', 'extra cheese')

# Podemos importar todas las funciones dentro de un modulo de la siguiente manera
# from module_name import *
from pizza_module import *

make_pizza(24, 'pepperoni')
make_pizza(20, 'mushrooms', 'green peppers', 'extra cheese')