import random
import numpy as np

def obtener_indice(caracter, cadena):
    if caracter in cadena:
        for i in range(len(cadena)):
            if(caracter == cadena[i]):
                return i

# --------------------------------------------

def codificar_caracter(letra, alfabeto, k):
    index = obtener_indice(letra, alfabeto)
    return alfabeto[(index + k) % 27]

# --------------------------------------------

def normalizar(mensaje):
    mensaje = mensaje.lower()
    mensaje2 = ""
    for c in mensaje:
        if(c == "á"): mensaje2 += "a"
        elif(c == "é"): mensaje2 += "e"
        elif(c == "í"): mensaje2 += "i"
        elif(c == "ó"): mensaje2 += "o"
        elif(c == "ú" or c == "ü"): mensaje2 += "u"
        else: mensaje2 += c

    return mensaje2
        
# --------------------------------------------

def crear_diccionario_cesar(alfabeto, k):
    desplazamiento = [0]*len(alfabeto)
    for i in range(len(alfabeto)):
        desplazamiento[i] = codificar_caracter(alfabeto[i], alfabeto, k)

    return dict(zip(alfabeto, desplazamiento))

# --------------------------------------------

def codificar(mensaje, diccionario):
    mensaje = normalizar(mensaje)
    codigo = ""
    for c in mensaje:  
        if(c in diccionario.keys()):
            codigo += diccionario[c]
        else:
            codigo += c

    return codigo
        
# --------------------------------------------

def crear_diccionario_invertido(diccionario):
    llaves = diccionario.keys()
    valores = diccionario.values()
    return dict(zip(valores, llaves))

# --------------------------------------------

def decodificar(mensaje, diccionario):
    mensaje = normalizar(mensaje)
    dicc_inv = crear_diccionario_invertido(diccionario)
    codigo = ""
    for c in mensaje:  
        if(c in dicc_inv.keys()):
            codigo += dicc_inv[c]
        else:
            codigo += c

    return codigo

# --------------------------------------------

def quitar(caracteres, cadena):
    cadena2 = ""
    for i in cadena:
        if i not in caracteres:
            cadena2 += i

    return cadena2

# --------------------------------------------

def sin_repetidos(cadena):
    cadena2 = ""
    repetidos = []
    for i in cadena:
        if i not in repetidos:
            repetidos.append(i)
            cadena2 += i

    return cadena2

# --------------------------------------------

def crear_codificacion(palabra, alfabeto):
    palabra2 = sin_repetidos(palabra) 
    alf2 = quitar(palabra2, alfabeto) 
    val = palabra2 + alf2
    valores = list(val)

    return dict(zip(alfabeto, valores))


# --------------------------------------------

alf = "abcdefghijklmnñopqrstuvwxyz"
mensaje = "La conclusion: perdieron"
dicc = crear_diccionario_cesar(alf, 3)

print(crear_codificacion("catapulta", alf))