import time

start = time.time()

#Funcion para conseguir todas las rutas posibles
def permutaciones(ciudades):
    n = len(ciudades)
    indices = list(range(n))
    
    while True:
        yield [ciudades[i] for i in indices]

        # Encuentra el índice j más grande para el que indices[j] < indices[j+1]
        j = n - 2 #Comienza en 6 para este caso
        while j >= 0 and indices[j] > indices[j + 1]:
            j -= 1

        if j == -1:
            break  # Todas las permutaciones se han generado

        # Encuentra el índice más pequeño k tal que indices[k] > indices[j]
        k = n - 1 #Comienza en 7 para este caso
        while indices[k] < indices[j]:
            k -= 1

        # Intercambia los valores en indices[j] y indices[k]
        indices[j], indices[k] = indices[k], indices[j]

        # Invierte los valores en indices[j+1:]
        indices[j + 1:] = reversed(indices[j + 1:])


def Sumar_distancias(ruta):
    #Suma de todas las distancias en el recorrido
    distancia = 0
    
    #Almacena la posicion de la ciudad destino
    destino = ciudades.index(ruta[0])
    #Suma la distancia desde mi posicion hasta el destino
    distancia += distancias["Bogota"][destino]
    
    for i in range(len(ruta)):
        #Calcula la distancia desde la ultima ciudad hasta bogota
        if i == (len(ruta)-1):
            distancia += distancias[ruta[i]][0]
        #Suma las distancias de una ciudad a otra
        else:                                          
            destino = ciudades.index(ruta[i+1])         
            distancia += distancias[ruta[i]][destino]
            
    return distancia

#Toma como entrada una ruta y las va separando en varias rutas
#segun se supere la capacidad maxima de los camiones
def separar_rutas(ruta,capacidad):
    sub_ruta = []
    total_rutas = []
    Dtotal = 0
    
    for i in range(len(ruta)):
        Dtotal += demandas[ruta[i]]
        sub_ruta.append(ruta[i])
        #Guarda una ruta una vez se
        if (i == (len(ruta)-1) ):
            total_rutas.append(sub_ruta)
            return total_rutas
        elif (Dtotal + demandas[ruta[i+1]]) > (capacidad):
            total_rutas.append(sub_ruta)
            sub_ruta = []
            Dtotal = 0
            
    return total_rutas

#Diccionario con distancias entre ciudades
distancias = {
    "Bogota": (0, 129, 192, 265, 90, 426, 95, 292, 249, 216, 303, 343, 309, 13, 22, 23),
    "Tunja": (129, 0, 63, 174, 104, 370, 112, 176, 224, 87, 174, 274, 295, 143, 115, 114),
    "Sogamoso": (192, 63, 0, 111, 161, 369, 168, 171, 250, 149, 190, 267, 276, 206, 169, 157),
    "Yopal": (265, 174, 111, 0, 250, 472, 251, 332, 411, 261, 316, 337, 381, 256, 259, 255),
    "Villavicencio": (90, 104, 161, 250, 0, 537, 110, 372, 269, 90, 233, 117, 446, 205, 63, 97),
    "Medellin": (426, 370, 369, 472, 537, 0, 429, 193, 317, 438, 536, 420, 140, 422, 442, 415),
    "Villeta": (95, 112, 168, 251, 110, 429, 0, 261, 164, 118, 213, 70, 353, 139, 73, 28),
    "Manizales": (292, 176, 171, 332, 372, 193, 261, 0, 126, 295, 368, 215, 256, 276, 326, 299),
    "Pereira": (249, 224, 250, 411, 269, 317, 164, 126, 0, 188, 281, 157, 392, 216, 92, 98),
    "Ibague": (216, 87, 149, 261, 90, 438, 118, 295, 188, 0, 116, 262, 330, 159, 127, 117),
    "Neiva": (303, 174, 190, 316, 233, 536, 213, 368, 281, 116, 0, 383, 396, 248, 216, 232),
    "Cali": (343, 274, 267, 337, 117, 420, 70, 215, 157, 262, 383, 0, 477, 144, 127, 88),
    "Bucaramanga": (309, 295, 276, 381, 446, 140, 353, 256, 392, 330, 396, 477, 0, 359, 442, 413),
    "Villanueva": (13, 143, 206, 256, 205, 422, 139, 276, 216, 159, 248, 144, 359, 0, 134, 126),
    "Soacha": (22, 115, 169, 259, 63, 442, 73, 326, 92, 127, 216, 127, 442, 134, 0, 42),
    "Ituango": (23, 114, 157, 255, 97, 415, 28, 299, 98, 117, 232, 88, 413, 126, 42, 0)
}

#Diccionario con demandas de cada ciudad
demandas = {
    "Tunja": 4,
    "Sogamoso": 2,
    "Yopal": 5,
    "Villavicencio": 3,
    "Medellin": 1,
    "Villeta": 4,
    "Manizales": 3,
    "Pereira": 5,
    "Ibague": 2,
    "Neiva": 4
}

#Tupla con configuracion de ciudades inicial
ciudades = (
    "Tunja", "Sogamoso", "Yopal", "Villavicencio",
    "Medellin", "Villeta", "Manizales", "Pereira", "Ibague",
    "Neiva"
)

#Capacidad de los camiones
capacidad = 12


cam = separar_rutas(ciudades, capacidad) #Guarda la primera solucion 
minDist = 0
for i in range(len(cam)):
    minDist = minDist + Sumar_distancias(cam[i]) #Guarda la distancia de la primera solucion
    
total_rutas = []

dist = 0

# Imprime todas las permutaciones
for ruta in permutaciones(ciudades):
    dist = 0
    
    total_rutas = separar_rutas(ruta, capacidad)

    for i in range(len(total_rutas)):
        dist = dist + Sumar_distancias(total_rutas[i])
    
    #Si la distancia total recorrida en la ruta es menor a la de
    #la mejor solucion hasta el momento, la reemplaza y guarda las rutas       
    if dist <= minDist:
        minDist = dist
        cam = total_rutas      
        
end = time.time()

print(cam)
print("Con una distancia recorrida de: ", minDist)
print("Solucion encontrada en: ", end - start, " segundos")


        
