# Uso de las sentencias if-elif-else

age = 64

if age < 4:
    #print("Your admission cost is $0.")
    price = 0
elif age < 18:
    #print("Your admission cost is $5.")
    price = 5
elif age < 65:
    price = 10
elif age >= 65: # A veces no es necesario usar else:
    #print("Your admission cost is $10.")
    price = 5

print("Your admission cost is $" + str(price) + ".")