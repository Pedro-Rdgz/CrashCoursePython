"""
Make a class called User. Create two attributes called first_name and 
last_name, and then create several other attributes that are typically
stored in a user profile. Make a method called describe_user() that prints
a summary of the user's information. Make another method called greet_user()
that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""
# Creando la clase
class User():
    """Clase simple para informacion basica de un usuario."""

    def __init__(self, first_name, last_name, nickname, email):
        """ Inicializar atributos first and last name."""
        self.first_name = first_name
        self.last_name = last_name 
        self.nickname = nickname
        self.email = email 

    def describe_user(self):
        """Mostrar informacion basica de un usuario."""
        print("\n****** INFORMATION *******")
        print(f"Username: {self.nickname}")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Email: {self.email}\n")

    def greet_user(self):
        print(f"Hello there {self.nickname}, hope you're doing great!\n")


# Creando instancias
usuario1 = User('juan', 'perez', 'pepito', 'juanp@gmail.com')
usuario1.describe_user()
usuario1.greet_user()
