"""
Add an attribute called login_attempts to your User class from exercise 9-3.
Write a method increment_login_attempts() that increments the value of 
login_attempts by 1. Write another method called reset_login_attempts() 
that resets the value of login_attempts to 0.
"""
class User():
    """Clase simple para informacion basica de un usuario."""

    def __init__(self, first_name, last_name, nickname, email):
        """ Inicializar atributos first and last name."""
        self.first_name = first_name
        self.last_name = last_name 
        self.nickname = nickname
        self.email = email 
        self.login_attempts = 0

    def describe_user(self):
        """Mostrar informacion basica de un usuario."""
        print("\n****** INFORMATION *******")
        print(f"Username: {self.nickname}")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Email: {self.email}\n")

    def greet_user(self):
        print(f"Hello there {self.nickname}, hope you're doing great!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1 

    def reset_login_attempts(self):
        self.login_attempts = 0 


# Creando instancias
usuario1 = User('juan', 'perez', 'pepito', 'juanp@gmail.com')
usuario1.describe_user()
usuario1.greet_user()

for n in range(5):
    usuario1.increment_login_attempts()

print(f"Login attempts: {usuario1.login_attempts}")

usuario1.reset_login_attempts()
print(f"Login attempts: {usuario1.login_attempts}")
