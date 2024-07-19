import csv
import matplotlib.pyplot as plt

# Mostrar el título del programa al inicio
def mostrar_titulo():
    print("=================================================")
    print("          Analizador de Calidad del Aire         ")
    print("=================================================")
    print()

# Llamar a la función para mostrar el título
mostrar_titulo()

def recuperar_rangos(nombre_archivo):
    try:
        rangos = []
        with open(nombre_archivo, "r") as archivocsv:
            lector_csv = csv.reader(archivocsv)
            for calidad, so2min, so2max, pm10min, pm10max, p25min, p25max in lector_csv:
                rangos.append((calidad, int(so2min), int(so2max), 
                               int(pm10min), int(pm10max), int(p25min), int(p25max)))
        return rangos
    except FileNotFoundError:
        print("Error. No se pudo abrir el archivo: " + nombre_archivo)
        return None

def imprime(rango):
    cad = "{0:<10} | {1:4d} | {2:4d} | {3:4d} | {4:4d} | {5:4d} | {6:4d}"
    print(cad.format(rango[0], rango[1], rango[2], rango[3], rango[4], rango[5], rango[6]))

def imprimir_rangos(rangos):
    cabecera = "Calidad    | som  | soM  | pm10m| pm10M| pm25m| pm25M"
    print(cabecera)
    cabecera = "-----------------------------------------------------"
    print(cabecera)
    for rango in rangos:
        imprime(rango)
    print(cabecera)

def imprime_medida(medida):
    cad = "{0:<10} | {1:4d} | {2:4d} | {3:4d}"
    print(cad.format(medida[0], medida[1], medida[2], medida[3]))

def imprimir_medidas(medidas):
    cabecera = "Fecha      | SO   | pm10 | pm25m"
    print(cabecera)
    cabecera = "--------------------------------"
    print(cabecera)
    for medida in medidas:
        imprime_medida(medida)
    print(cabecera)

def recuperar_medidas(nombre_archivo):
    try:
        medidas = []
        with open(nombre_archivo, "r") as archivocsv:
            lector_csv = csv.reader(archivocsv)
            for fecha, so, pm10, pm25 in lector_csv:
                medidas.append((fecha, int(so), int(pm10), int(pm25)))
        return medidas
    except FileNotFoundError:
        print("Error. No se pudo abrir el archivo: " + nombre_archivo)
        return None

def getRangoSO(so, rangos):
    for rango in rangos:
        if so >= rango[1] and so <= rango[2]:
            calidad = rango[0]
            break
    return calidad

def getRangoPM10(pm10, rango):
    for rango in rangos:
        if pm10 >= rango[3] and pm10 <= rango[4]:
            calidad = rango[0]
            break
    return calidad

def getRangoPM25(pm25, rango):
    for rango in rangos:
        if pm25 >= rango[5] and pm25 <= rango[6]:
            calidad = rango[0]
            break
    return calidad

def testear_calidad(medidas, rangos):
    print("calidad    |  SO        |  PM 10     |   PM25     ")
    print("--------------------------------------------------")
    cad = "{0:<10} | {1:<10} | {2:<10} | {3:<10}"
    for medida in medidas:
        calidadSO = getRangoSO(medida[1], rangos)
        calidadPM10 = getRangoPM10(medida[2], rangos)
        calidadPM25 = getRangoPM25(medida[3], rangos)
        print(cad.format(medida[0], calidadSO, calidadPM10, calidadPM25))
    print("--------------------------------------------------")

def pedir_ficheros():
    fichero_medidas = "medidas.txt"
    fichero_rangos = "rangos.txt"
    usuario_medidas = input("Nombre fichero de medidas (intro por defecto): ")
    if usuario_medidas != "":
        fichero_medidas = usuario_medidas
    print("Cargando fichero medidas: ", fichero_medidas)
    usuario_rangos = input("Nombre fichero de rangos (intro por defecto): ")
    if usuario_rangos != "":
        fichero_rangos = usuario_rangos
    print("Cargando fichero medidas: ", fichero_rangos)
    return fichero_medidas, fichero_rangos


def menuPrincipal():
    opciones = ["medidas", "rangos", "calidad", "grafica", "salir"]
    while True:
        opcion = input("medidas, rangos, calidad, grafica, salir: ")
        if opcion not in opciones:
            print("Error en opcion.")
        else:
            break
    return opcion

def graficas(medidas, rangos):
    medidasSO = []
    medidasPM10 = []
    medidasPM25 = []
    for medida in medidas:
        medidasSO.append(medida[1])
        medidasPM10.append(medida[2])
        medidasPM25.append(medida[3])
    
    plt.xlabel("num. medida")
    plt.ylabel("valores")
    plt.plot(medidasSO, label = "SO")
    plt.plot(medidasPM10, label = "PM10")
    plt.plot(medidasPM25, label = "PM25")
    plt.legend()
    plt.show()

def ejecutar_opcion(medidas, rangos, opcion):
    if opcion == "medidas":
        imprimir_medidas(medidas)
    elif opcion == "rangos":
        imprimir_rangos(rangos)
    elif opcion == "calidad":
        testear_calidad(medidas, rangos)
    elif opcion == "grafica":
        graficas(medidas, rangos)
    else:
        print("Adios...")
#
# principal
#
fichero_medidas, fichero_rangos = pedir_ficheros()
medidas = recuperar_medidas(fichero_medidas)
rangos = recuperar_rangos(fichero_rangos)
if medidas == None:
    print("No se pudieron cargar medidas de", fichero_medidas)
elif rangos == None:
    print("No se pudieron cargar rangos de", fichero_rangos)
else:
    while True:
        opcion = menuPrincipal()
        ejecutar_opcion(medidas, rangos, opcion)
        if opcion == "salir":
            break
    
    



