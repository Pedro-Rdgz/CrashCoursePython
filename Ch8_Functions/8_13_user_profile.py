"""
Start with a copy of user_profile from page 153. Build a profile
of yourself by calling build_profile(), using your first and last 
names and three other key-value pairs that describe you.
"""
# El doble ** indica crear un diccionario vacio llamado, en este caso, user_info
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first 
    profile['last_name'] = last 
    for key, value in user_info.items():
        profile[key] = value 
    return profile 

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

mi_perfil = build_profile('juan', 'perez', edad=20, ciudad='cdmx', musica='rock')
print(user_profile)
print(mi_perfil)
