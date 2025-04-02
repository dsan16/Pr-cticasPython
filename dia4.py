from random import randint

nombre = input("¿Cuál es tu nombre?\n")
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número.")

numero = randint(1, 100)
aciertos = 0

for i in range(8):
    intento = int(input("Pon un número:\n"))
    if intento < 1 or intento > 100:
        print("Número fuera de rango")
    elif intento == numero:
        print(f"¡Correcto! El número era {numero}")
        print("Ahora intentaremos con otro número")
        numero = randint(1, 100)
        aciertos += 1
    elif intento < numero:
        print("El número es mayor")
    elif intento > numero:
        print("El número es menor")
    else:
        print("Número incorrecto")

print(f"Has acertado {aciertos} veces")