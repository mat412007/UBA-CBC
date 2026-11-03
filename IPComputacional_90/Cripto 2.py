import Cripto as c1
import matplotlib.pyplot as plt

def leer_archivo(nombre):
    archivo = open(nombre, encoding = "utf-8")
    texto = archivo.read()
    archivo.close()
    return texto
        
# ------------------------------------------

def codificar_archivo_con_dicc(nombre, diccionario):
    texto = leer_archivo(nombre)
    codigo = c1.codificar(texto, diccionario)
    
    nombre2 = nombre.replace(".txt", ".enc")
    archivo = open(nombre2, "w")
    archivo.write(codigo)
    archivo.close()

# ------------------------------------------

def decodificar_archivo_con_dicc(nombre, diccionario):
    texto = leer_archivo(nombre)
    codigo = c1.decodificar(texto, diccionario)
    
    nombre2 = nombre.replace(".enc", ".dec")
    archivo = open(nombre2, "w")
    archivo.write(codigo)
    archivo.close()

# ------------------------------------------

def pertence(elemento, lista):
    if(elemento in lista):
        return True
    return False

# ------------------------------------------

def contar_coincidencias(palabras_mensaje, palabras_comunes):
    cantidad = 0
    for palabra in palabras_mensaje:
        if pertence(palabra, palabras_comunes):
            cantidad += 1
    return cantidad
        
# ------------------------------------------

def coincidencias_por_k(mensaje_codificado, palabras_comunes, alfabeto):
    coincidencias = [0]*len(alfabeto)
    for k in range(len(alfabeto)):
        dicc = c1.crear_diccionario_cesar(alfabeto, k)
        mensaje2 = c1.decodificar(mensaje_codificado, dicc)
        palabras_mensaje2 = mensaje2.split(' ')
        palabras_comunes2 = palabras_comunes.split(' ')
        coincidencias[k] = contar_coincidencias(palabras_mensaje2, palabras_comunes2)
    return coincidencias

# ------------------------------------------

def k_optimo(mensaje_codificado, palabras_comunes, alfabeto):
    maximo = 0
    indice = 0
    coincidencias = coincidencias_por_k(mensaje_codificado, palabras_comunes, alfabeto)
    for c in range(len(coincidencias)):
        if coincidencias[c] > maximo:
            maximo = coincidencias[c]
            indice = c
            
    return indice
    
# ------------------------------------------

def decodificar_mensaje(archivo_codificado, archivo_palabras, alfabeto):
    archivo = open(archivo_codificado, encoding = "utf-8")
    mensaje_codificado = archivo.read()
    archivo = open(archivo_palabras, encoding = "utf-8")
    palabras_comunes = archivo.read()
    archivo.close()
    
    mejor_k = k_optimo(mensaje_codificado, palabras_comunes, alfabeto)
    dicc = c1.crear_diccionario_cesar(alfabeto, mejor_k)
    mensaje_decodificado = c1.decodificar(mensaje_codificado, dicc)
    archivo = open("Decodificacion.dec", "w")
    archivo.write(mensaje_decodificado)
    archivo.close()
    
# ------------------------------------------

def graficar_k(lista_coincidencias):
    Ks = [0]*27
    for i in range(len(Ks)):
        Ks[i] = i
    
    plt.bar(Ks, height=lista_coincidencias)
    plt.show()

# ------------------------------------------

alf = "abcdefghijklmnñopqrstuvwxyz"
dicc = {'a':'1','b':'9','c':'2','d':'-'} 
codificar_archivo_con_dicc("original.txt", dicc)

alf = leer_archivo("alfabeto.txt") 
dicc = c1.crear_diccionario_cesar(alf,4)
decodificar_archivo_con_dicc("mensaje misterioso.enc",dicc) 

cant = contar_coincidencias(['hola','soy','una','lista'], ['hola','soy','lista','jeje'])

palabras_comunes = leer_archivo('palabras')
palabras_comunes = c1.normalizar(palabras_comunes)
dic10 = c1.crear_diccionario_cesar(alf,10)
#print(k_optimo(c1.codificar("el arte de programar!",dic10), palabras_comunes , alf))

decodificar_mensaje("decodificame.enc", "palabras", alf)


graficar_k(coincidencias_por_k(leer_archivo("decodificame.enc"), palabras_comunes, alf))