import random
import numpy as np

def generar_bosque(n): # Genera un bosque de n tamaño
    return np.array([0]*n)

# ---------------------------------

def suceso_aleatorio(p): # Probabilidad de algo
    return random.random() <= p

# ---------------------------------

def brotes(bosque, p):
    for i in range(0, len(bosque)):
        brote = suceso_aleatorio(p) # Plantamos arboles en el bosque
        if(brote):
            bosque[i] = 1

# ---------------------------------

def rayos(bosque, f):
    for i in range(0, len(bosque)):
            rayo = suceso_aleatorio(f) # Revisamos si le cayo un rayo a un arbol
            if(rayo and bosque[i] == 1):
                bosque[i] = -1

# ---------------------------------

def vecinos(bosque, pos):
     if(pos == 0): # Si es el primer elemento, devolvemos el segundo
          return [1]
     elif(pos == len(bosque)-1): # Si es el ultimo elemento, devolvemos el anteultimo
        return [len(bosque)-2]
     else:
         return [pos-1, pos+1] # Devolvemos los elementos de izquierda y derecha

# ---------------------------------

def propagar_vecinos(bosque):
    propague = False
    for i in range(len(bosque)):
        if(bosque[i] == -1):
            for v in vecinos(bosque, i):
                if(bosque[v] == 1):
                    bosque[v] = -1
                    propague = True
    return propague

# ---------------------------------

def propagar(bosque):
    seguir = propagar_vecinos(bosque)
    while(seguir):
        seguir = propagar_vecinos(bosque)

# ---------------------------------

def limpieza(bosque):
    for i in range(len(bosque)):
        if(bosque[i] == -1):
            bosque[i] = 0

# ---------------------------------



# ---------------------------------

bosque = generar_bosque(10)

brotes(bosque, 0.4) 

rayos(bosque, 0.2)

propagar(bosque)

limpieza(bosque)