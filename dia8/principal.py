from numeros import siguiente_turno_perfumeria, siguiente_turno_farmacia, siguiente_turno_cosmetica

def mostrar_menu():
    print("Seleccione la sección deseada:")
    print("1 - Perfumería")
    print("2 - Farmacia")
    print("3 - Cosmética")

def ejecutar_turnero():
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Introduce el número de la sección: ")

        if opcion == "1":
            siguiente_turno_perfumeria()
        elif opcion == "2":
            siguiente_turno_farmacia()
        elif opcion == "3":
            siguiente_turno_cosmetica()
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.\n")

        respuesta = input("¿Deseas sacar otro turno? (s/n): ").lower()
        if respuesta != "s":
            continuar = False

ejecutar_turnero()