import random

def cantidad_para_llenar(tam):
    album = [0]*tam
    cant_figus = 0
    while sum(album)<len(album):
        figu = random.randint(0,tam-1)
        album[figu] = 1
        cant_figus = cant_figus + 1
    return cant_figus # Cantidad de figuritas que compramos para llenar un album

# --------------------------------------------------

def cuantas_figus_multiple(figus_total, n_albumes):
    albumes = [0]*n_albumes
    contador = 0
    
    while contador < n_albumes:
        
        albumes[contador] = cantidad_para_llenar(figus_total)
        contador += 1
        
    return albumes # Lista de cantidades de figuritas que compramos para llenar el mismo album

# --------------------------------------------------

def promedio_figus(figus_total, n_albumes):
    cantidades = cuantas_figus_multiple(figus_total, n_albumes)
    
    return sum(cantidades) / n_albumes # Promedio de cuantas figurtas nos toma llenar un album, usando una lista de intentos

# --------------------------------------------------

def probar_todos_tams(figus_min, figus_max, repeticiones):
    listaPromedios = [0]*(figus_max-figus_min)
    tam_album = figus_min
    
    while tam_album < figus_max:
        listaPromedios[tam_album-figus_min] = promedio_figus(tam_album, repeticiones)
        tam_album += 1
    
    return listaPromedios # Lista de promedios de albumes de diferentes tamaños, sin contar el ultimo

# --------------------------------------------------


lista = probar_todos_tams(4, 7, 100)
print(lista)

