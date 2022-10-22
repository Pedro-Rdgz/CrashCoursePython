"""
Make several dictionaries, where the name of each dictionary is the name of the pet.
In each dictionary, include the kind of animal and the owner's name. Store these
dictionaries in a list called pets. Next, loop through your list and as you do 
print everything you know about each pet.
"""

choco = {
    'kind' : 'cat',
    'owner': 'juan',
}

wilfred = {
    'kind': 'cat',
    'owner': 'mario',
}

flan = {
    'kind': 'cat',
    'owner': 'maria'
}

blanquito = {
    'kind': 'cat',
    'owner': 'juana',
}

pets = [choco, wilfred, flan, blanquito]

for p in pets:
    print(p['kind'] + " " + p['owner'].title())
