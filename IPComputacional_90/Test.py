import random, numpy as np

bosque = np.array([0]*6) # Array unidimensioal de 6 espacios llenos de 0
bosque3 = np.array([[0]*10]*2) # Array bidimensional de 2 filas y 10 columnas, lleno de 0
tupla = (2, 4, 6, 8, 10) # Tupla, coleccion de valores inmutables

naturales = np.array([1, 2, 3, 4, 5,  6,  7,  8,  9,  10])
pares =     np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
conjunto = np.array([naturales, pares])

print(naturales[4:]) # Se INCLUYE el primer indice
print(pares[:9]) # Se EXCLUYE el último indice
print(conjunto[0, 4]) # Primera fila, indice valor 4
print(conjunto[:, 3:6]) # Todas las filas, desde la cuarta columna hasta la sexta