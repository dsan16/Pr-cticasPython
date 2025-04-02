from random import choice

palabras = ["coche", "marron", "mesa", "silla", "raton", "ordenador", "monitor", "teclado", "pantalla", "telefono"]
palabra = choice(palabras)
vidas = 6
letras_acertadas = []
letras_elegidas = []
letra = ""

def mostrar_guiones(palabra, letras_acertadas):
    guiones = ""
    for letra in palabra:
        if letra in letras_acertadas:
            guiones += letra
        else:
            guiones += "_"
    return guiones

def acertar_letra(letra, palabra, letras_acertadas, letras_elegidas):
    if letra in palabra:
        letras_acertadas.append(letra)
        print(f"La letra '{letra}' está en la palabra")
    else:
        letras_elegidas.append(letra)
        print(f"La letra '{letra}' no está en la palabra. Te quedan {vidas - len(letras_elegidas)} vidas.")

def pedir_letra(letras_elegidas, letras_acertadas):

    while True:
        letra = input("Introduce una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha() or letra in letras_elegidas or letra in letras_acertadas:
            print("Entrada inválida. Introduce una sola letra que no hayas adivinado.")
        else:
            return letra
def mostrar_resultado(vidas, letras_elegidas):
    if vidas > len(letras_elegidas):
        print("Has ganado")
    else:
        print("Has perdido")
    
    print(f"La palabra era: {palabra}")

def jugar(palabra, letras_elegidas, letras_acertadas, vidas):
    while "_" in mostrar_guiones(palabra, letras_acertadas) and len(letras_elegidas) < vidas:       
        print(mostrar_guiones(palabra, letras_acertadas))
        print(letras_elegidas + letras_acertadas)
        letra = pedir_letra(letras_elegidas, letras_acertadas)
        acertar_letra(letra, palabra, letras_acertadas, letras_elegidas)

jugar(palabra, letras_elegidas, letras_acertadas, vidas)
mostrar_resultado(vidas, letras_elegidas)