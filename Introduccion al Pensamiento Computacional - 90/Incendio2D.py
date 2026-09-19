import random
import numpy as np

def suceso_aleatorio(p): # Probabilidad de algo
    return random.random() <= p

# --------------------------------------------------

def encontrar_indice(lista, valor):
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            if lista[i][j] == valor:
                return (i, j)

# --------------------------------------------------

def generar_bosque(n, m):
    bosque = np.array([[0]*m]*n) # n filas y m columnas
    return bosque

# --------------------------------------------------

def brotes(bosque, p):
    for i in range(0, len(bosque)):
        for j in range(0, len(bosque[0])):
            brote = suceso_aleatorio(p) # Plantamos arboles en el bosque
            if(brote):
                bosque[i][j] = 1
            
# --------------------------------------------------

def vecinos(bosque, pos): # Bosque es un array 2D, y pos una tupla de 2 valores
    v = []
    filas, columnas = bosque.shape
    f, c = pos

    f1 = f+1
    if (f1) == filas:
        f1 = 0

    c1 = c+1
    if (c1) == columnas:
        c1 = 0

    f2 = f-1
    if (f2) < 0:
        f2 = filas-1

    c2 = c-1
    if (c2) < 0:
        c2 = columnas-1

    v.append((f, c1)) # 8 vecinos
    v.append((f, c2))
    v.append((f1, c))
    v.append((f2, c))
    v.append((f1, c1))
    v.append((f2, c2))
    v.append((f1, c2))
    v.append((f2, c1))
        
    return v

# --------------------------------------------------

bosque = generar_bosque(5, 5)
            
print(vecinos(bosque, (4, 4)))
brotes(bosque, 0.4)
print(bosque)