import random
import numpy as np
import matplotlib.pyplot as plt

def suceso_aleatorio(p): # Probabilidad de algo
    return random.random() <= p

# --------------------------------------------------

def visualizar_bosque(bosque):
    cmap = plt.cm.colors.ListedColormap(["red", "white", "green"])
    cmap.set_under("black")
    plt.imshow(bosque, cmap=cmap, vmin=-1.5, vmax=1.5)
    plt.show()

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

def rayos(bosque, f):
    filas, columnas = bosque.shape
    for i in range(filas):
        for j in range(columnas):
            if suceso_aleatorio(f) and bosque[i][j]:
                bosque[i][j] = -1
                
# --------------------------------------------------

def vecinos(bosque, pos): # Bosque es un array 2D, y pos una tupla de 2 valores
    v = []
    filas, columnas = bosque.shape
    f, c = pos

    f1 = (f+1) % len(bosque)

    c1 = (c+1) % len(bosque[0])

    f2 = (f-1) % len(bosque)

    c2 = (c-1) % len(bosque[0])

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

def propagar_vecinos(bosque):
    propagado = False
    filas, columnas = bosque.shape
    for i in range(filas):
        for j in range(columnas):
            if bosque[i][j] == -1:
                vec = vecinos(bosque, (i, j))
                for x in range(8): # 8 vecinos
                    if (bosque[vec[x][0]][vec[x][1]] == 1):
                        propagado = True
                        bosque[vec[x][0]][vec[x][1]] = -1
    return propagado

# --------------------------------------------------

def propagar(bosque):
    propagando = propagar_vecinos(bosque)
    while(propagando):
        propagando = propagar_vecinos(bosque)

# --------------------------------------------------

def limpieza(bosque):
    for i in range(len(bosque)):
        for j in range(len(bosque[0])):
            if(bosque[i][j] == -1):
                bosque[i][j] = 0
    
# --------------------------------------------------

def dinamica(n, m, p, f, a):
    sobrevivientes = [0]*a
    for x in range(a):
        arboles = 0
        bosque = generar_bosque(n, m)
        brotes(bosque, p)
        rayos(bosque, f)
        propagar(bosque)
        limpieza(bosque)
        for i in range(len(bosque)):
            for j in range(len(bosque[0])):
                if bosque[i][j] == 1:
                    arboles += 1
        sobrevivientes[x] = arboles

    return sum(sobrevivientes) / len(sobrevivientes) # Promedio de sobrevivientes

# --------------------------------------------------

def arboles_sobrevivientes(n, m, f, a):
    sobrevivientes = [0]*101 # 0 hasta 1
    i = 0
    for p in np.arange(0, 1.01, 0.01):
        sobrevivientes[i] = dinamica(n, m, p, f, a)
        i += 1
    return sobrevivientes

# --------------------------------------------------

def p_optimo(n, m, f, a):
    sobrevivientes = arboles_sobrevivientes(n, m, f, a) 
    maximo = 0
    indice = 0
    for i in range(101):
        if(sobrevivientes[i] > maximo):
            indice = i
    return  0 + (0.01*indice)

# --------------------------------------------------

print(p_optimo(10, 10, 0.2, 5)) # 5 años

#visualizar_bosque(bosque)
            