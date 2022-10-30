"""
Put the functions for the example print_models.py in a separate file called
printing_functions.py. Write an import statement at the top of 
print_models.py, and modify the file to use the imported functions.
"""

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
###################### import module_name ######################
import printing_functions
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)


unprinted_designs = ['xiaomi case', 'robot pendant', 'dodecahedron']
completed_models = []
################ from module_name import function_name #################
from printing_functions import print_models, show_completed_models
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


unprinted_designs = ['razer case', 'robot pendant', 'dodecahedron']
completed_models = []
############ from module_name import function_name as fn ##############
from printing_functions import print_models as pm, show_completed_models as scm 
pm(unprinted_designs, completed_models)
scm(completed_models)


unprinted_designs = ['samsung case', 'robot pendant', 'dodecahedron']
completed_models = []
###################### import module_name as mn ######################
import printing_functions as pf 
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)


unprinted_designs = ['one plus case', 'robot pendant', 'dodecahedron']
completed_models = []
################ from module_name import * ##################
from printing_functions import * 
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)