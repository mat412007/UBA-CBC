import random

def tirar_cubilete(): # Funcion de tirar los dados
    dados = [0]*5 # Hay cinco dados
    contador = 0
    while contador < 5:
        dado = random.randint(1, 6)
        dados[contador] = dado
        contador += 1

    return dados 

# -------------------------------------------------

def contar_elemento(lista, elemento): # Correcta
    cantidad = 0
    i = 0
    while i < len(lista):
        if(lista[i] == elemento):
            cantidad += 1
        i += 1
    return cantidad

# -------------------------------------------------

def puntos_por_unos(lista_dados): # Correcta
    puntaje = 0
    unos = contar_elemento(lista_dados, 1)

    puntaje += unos*100

    if(unos == 5): # Combos de 1
        puntaje += 10000
    elif(unos >= 3):
        puntaje += 1000  

    return puntaje

# -------------------------------------------------

def puntos_por_cincos(lista_dados): # Correcta
    puntaje = 0
    cincos = contar_elemento(lista_dados, 5)
    
    puntaje += cincos*50

    if(cincos == 5): # Combos de 5
        puntaje += 5000
    elif(cincos >= 3):
        puntaje += 500  

    return puntaje

# -------------------------------------------------

def total_puntos(lista_dados): # Calculamos el puntaje de los dados que tiramos

    puntaje = puntos_por_unos(lista_dados) + puntos_por_cincos(lista_dados)

    return puntaje

# -------------------------------------------------

def jugar_ronda(puntajes):
    idJugador = 0
    while idJugador < len(puntajes):
        puntajes[idJugador] += total_puntos(tirar_cubilete()) 
        idJugador += 1

    return puntajes

# -------------------------------------------------

def hay_10mil(puntajes): # Verificamos si alguien ha ganado
    i = 0
    ganador = False
    while i < len(puntajes):
        if(puntajes[i] >= 10000):
            ganador = True
        i += 1
    return ganador

# -------------------------------------------------

def partida_completa(cant_jugadores):
    rondas = 0
    puntajes = [0]*cant_jugadores
    ganador = False

    while ganador == False:
        puntajes = jugar_ronda(puntajes) # Jugamos la ronda
        rondas += 1
        ganador = hay_10mil(puntajes) # Verificamos si hay un ganador
        
    print(puntajes)
    return rondas

# -------------------------------------------------

rondas = partida_completa(3) # Jugamos con 3 jugadores
print(rondas)