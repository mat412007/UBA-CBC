import random

album = [0]*6 # Lista de 6 ceros
intentos = 0

while sum(album) < 6:
    figurita = random.randint(0,5) # aleatorio entre 0 y 5
    album[figurita] = 1 # llenamos el espacio correspondiente a la figurta
    intentos+=1 # vamos contando la cantidad de intentos
    
print(album)
print("Cantidad de intentos: " + str(intentos))

# lista.append()
# sum(suma)
# len(largo)
# and, or, not
