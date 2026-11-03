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

def dinamica(f, a, n, p):
    bosque = generar_bosque(n) # Generamos el bosque
    arboles = [0]*a

    for i in range(a): 
        brotes(bosque, p) # Brote con probabilidad p

        rayos(bosque, f) # Rayo con probabilidad f

        propagar(bosque) # Propagacion del fuego

        limpieza(bosque) # Limpieza de arboles quemados

        for a in range(len(bosque)):
            if(bosque[a] == 1):
                arboles[i] += 1

    return round((sum(arboles)/a), 2) # Redondeamos el promedio de arboles sobrevivientes

# ---------------------------------

def arboles_sobrevivientes(f, a, n):
    sobrevivientes = []
    for p in np.arange(0, 1.01, 0.01):
        sobrevivientes.append(dinamica(f, a, n, p))

    return sobrevivientes

# ---------------------------------

def p_optimo(f, a, n):
    sobrevivientes = arboles_sobrevivientes(f, a, n)
    i_optimo = 0
    maximo = 0
    for i in range(len(sobrevivientes)):
        if(sobrevivientes[i] > maximo):
            maximo = sobrevivientes[i]
            i_optimo = i

    return (0.01*i_optimo) 

# ---------------------------------

print(p_optimo(0.3, 5, 10))