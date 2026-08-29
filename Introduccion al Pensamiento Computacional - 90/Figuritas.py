import random

intentos = [0]*10
intento = 0

while intento < len(intentos):
    album = [0]*6 # Lista de 6 ceros
    cantFiguritas = 0
    
    while sum(album) < 6:
        figurita = random.randint(0,5) # aleatorio entre 0 y 5
        album[figurita] = 1 # llenamos el espacio correspondiente a la figurta
        cantFiguritas+=1 # vamos contando la cantidad de intentos
    intentos[intento] = cantFiguritas
    intento +=1
    
print("\nEstos fueron los intentos:")
print(intentos)

promedio = sum(intentos)//len(intentos)
print("\nEl promedio de intentos es " + str(promedio))
# lista.append()
# sum(suma)
# len(largo)
# and, or, not
