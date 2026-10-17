import Cripto as c1

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

alf = "abcdefghijklmnñopqrstuvwxyz"
dicc = {'a':'1','b':'9','c':'2','d':'-'} 
codificar_archivo_con_dicc("original.txt", dicc)

alf = leer_archivo("alfabeto.txt") 
dicc = c1.crear_diccionario_cesar(alf,4)
decodificar_archivo_con_dicc("mensaje misterioso.enc",dicc) 

cant = contar_coincidencias(['hola','soy','una','lista'], ['hola','soy','lista','jeje'])

palabras_comunes = leer_archivo('palabras')
palabras_comunes = c1.normalizar(palabras_comunes)
print(coincidencias_por_k("Mica y Claudia toman mate", palabras_comunes, alf))