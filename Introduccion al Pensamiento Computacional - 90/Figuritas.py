import random

def cantidad_para_llenar(tam):
    album = [0]*tam
    cant_figus = 0
    while sum(album)<len(album):
        figu = random.randint(0,tam-1)
        album[figu] = 1
        cant_figus = cant_figus + 1
    return cant_figus

# --------------------------------------------------

def cuantas_figus_multiple(figus_total, n_albumes):
    repeticiones = [0]*n_albumes
    contador = 0
    
    while contador < n_albumes:
        
        repeticiones[contador] = cantidad_para_llenar(figus_total)
        contador += 1
        
    return repeticiones

# --------------------------------------------------

def promedio_figus(figus_total, n_albumes):
    cantidades = cuantas_figus_multiple(figus_total, n_albumes)
    print(cantidades)
    
    return sum(cantidades) // n_albumes

# --------------------------------------------------

repeticiones = 5
tam_album = 6

promedio = promedio_figus(tam_album, repeticiones)
print(promedio)

