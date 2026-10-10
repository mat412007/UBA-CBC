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

alf = "abcdefghijklmnñopqrstuvwxyz"
mensaje = "La conclusion: perdieron"
dicc = crear_diccionario_cesar(alf, 10)
print(codificar(mensaje, dicc))
