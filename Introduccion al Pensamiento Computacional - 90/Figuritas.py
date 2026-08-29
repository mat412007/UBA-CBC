import random

def llenarAlbum(nFiguritas):
    album = [0]*nFiguritas # Lista de n ceros
    cantFiguritas = 0 # Cantidad de figuritas compradas para llenar el album
        
    while sum(album) < nFiguritas:
        figurita = random.randint(0,nFiguritas-1) # aleatorio entre 0 y size-1
        album[figurita] = 1 # llenamos el espacio correspondiente a la figurta
        cantFiguritas+=1 # vamos contando la cantidad de intentos

    return cantFiguritas


nFiguritas = int(input("\nCual es el tamaño del album? : "))
albumes = int(input("Cuantos albumes deseas llenar? : "))

intentos = [0]*albumes
intento = 0

while intento < albumes:
    
    intentos[intento] = llenarAlbum(nFiguritas)
    intento +=1
    
print("\nEstos fueron los intentos:")
print(intentos) # Cantidades de figuritas compradas para llenar los albumes

promedio = sum(intentos)//len(intentos)
print("\nEl promedio de intentos es " + str(promedio))


# lista.append()
# sum(suma)
# len(largo)
# and, or, not
