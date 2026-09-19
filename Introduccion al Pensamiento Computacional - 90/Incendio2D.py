import random
import numpy as np
from Incendio import suceso_aleatorio

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

    if c == 0: # Vecinos de fila
        v.append((f, c+1))
    elif c == columnas-1:
        v.append((f, c-1))
    else:
        v.append((f, c+1))
        v.append((f, c-1))

    if f == 0: # Vecinos de columna
        v.append((f+1, c))
    elif f == filas-1:
        v.append((f-1, c))
    else:
        v.append((f+1, c))
        v.append((f-1, c))
        
    if f == 0 and c == 0: # Vecinos diagonales(Esquinas)
        v.append((f+1, c+1))
    elif f == 0 and c == columnas-1:
        v.append((f+1, c-1))
    elif f == filas-1 and c == 0:
        v.append((f-1, c+1))
    elif f == filas-1 and c == columnas-1:
        v.append((f-1, c-1))
        
    if f == 0: # Vecinos diagonales(Bordes horizontales)
        v.append((f+1, c+1))
        v.append((f+1, c-1))
    elif f == filas-1:
        v.append((f-1, c+1))
        v.append((f-1, c-1))
        
    if c == 0: # # Vecinos diagonales(Bordes verticales)
        v.append((f+1, c+1))
        v.append((f-1, c+1))
    elif c == columnas-1:
        v.append((f+1, c-1))
        v.append((f-1, c-1))
        
    if (c != 0 and c != columnas-1) and (f != 0 and f != filas-1):
        v.append((f+1, c-1))
        v.append((f-1, c-1))
        v.append((f+1, c+1))
        v.append((f-1, c+1))
        
    return v

# --------------------------------------------------

bosque = generar_bosque(3, 5)
#brotes(bosque, 0.4)
contador = 1
for i in range(len(bosque)):
    for j in range(len(bosque[0])):
        bosque[i][j] = contador
        contador +=1
            
print(bosque)
print(vecinos(bosque, (1, 1)))