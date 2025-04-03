import shutil
import os
from pathlib import Path
import re
import datetime
import time

path = Path.cwd().joinpath('ProyectoDia9')

regex = r"N[a-zA-Z]{3}-\d{5}"

encontrados = 0

print(f"Fecha actual: {datetime.datetime.now().strftime('%d-%m-%Y')}")

print("ARCHIVOS\t\tNRO. SERIE\n------------------------------------------")
inicio = time.time()

for carpeta, subcarpetas, archivos in os.walk(path):
    for archivo in archivos:
        if archivo == "Instrucciones.txt":
            continue
        imprimir = ""
        try:
            imprimir = imprimir + archivo + "\t\t"
            ruta_actual = os.path.join(carpeta, archivo)
            read = open(ruta_actual, "r")
            contenido = read.read()

            hallazgos = re.findall(regex, contenido)
            if hallazgos:
                for hallazgo in hallazgos:
                    imprimir = imprimir + hallazgo
                    encontrados += 1
            else:
                imprimir = imprimir + "None"
        except Exception as e:
            print(f"Error al procesar el archivo {archivo}: {e}")
        print(imprimir)
        read.close()

final = time.time()

print(f"Encontrados: {encontrados}")
print(f"Tiempo total: {final - inicio} segundos")