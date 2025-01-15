import random

#lista de caracteres
symbols =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#distancia
lenght = int(input('numero de caracteres en tu contraseñas:'))
#variable de la contraseña
password = ''

for i in range(lenght): 
    password += random.choice(symbols)
print(password)
