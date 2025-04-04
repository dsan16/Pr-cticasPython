import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

ruta = 'dia14/Empleados'
mis_fotos = []
nombres = []
lista_empleados = os.listdir(ruta)

print(f"Empleados: {lista_empleados}")

for empleado in lista_empleados:
    foto = fr.load_image_file(f"{ruta}/{empleado}")
    mis_fotos.append(foto)
    nombres.append(os.path.splitext(empleado)[0])

print(f"Nombre: {nombres}")

def codificar_fotos(fotos):
    encodings = []
    for foto in fotos:
        foto = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
        encoding = fr.face_encodings(foto)[0]
        encodings.append(encoding)
    
    return encodings

def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')

lista_empleados_codificada = codificar_fotos(mis_fotos)

captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

exito, imagen = captura.read()

if not exito:
    print("No se ha podido tomar la captura")
else:
    cara_captura = fr.face_locations(imagen)

    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de nuestros empleados")

        else:
            nombre = nombres[indice_coincidencia]

            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 2555, 255), 2)

            registrar_ingresos(nombre)

            cv2.imshow('Imagen web', imagen)

            cv2.waitKey(0)

cv2.imshow('Imagen web', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()