from os import system
from pathlib import Path

actual_path = Path.cwd().joinpath('Recetas')
print("Elige una receta de las siguientes:")


def mostrar_menu():
    print("1. Leer receta")
    print("2. Añadir receta")
    print("3. Eliminar receta")
    print("4. Salir")
    option = int(input("¿Qué quieres hacer?\n"))

    if(option < 1 or option > 4):
        print("Opción no válida. Por favor, elige una opción entre 1 y 4.")
        return mostrar_menu()
    elif(option == 1 or option == 2):
        mostrar_capeta_archivo(option)
    elif(option == 3):
        mostrar_menu()
    return option

def mostrar_capeta_archivo(option):
    print("Elige una categoría de las siguientes:")
    for file in actual_path.glob('*'):
        print(file.name)   
    cat = input("¿Qué categría quieres?\n")
    if not actual_path.joinpath(cat).exists():
        print("Categoría no válida. Por favor, elige una categoría existente.")
        return mostrar_capeta_archivo(option)
    else:
        if(option == 1):
            mostrar_recetas(cat)
        elif(option == 2):
            agregar_receta(cat)

def agregar_receta(cat):
    new_path = actual_path.joinpath(cat)
    receta = input("¿Qué receta quieres añadir (sin sufijo txt)?\n")
    new_path = new_path / f"{receta}.txt"

    receta_content = input("¿Qué quieres añadir a la receta?\n")

    new_path.write_text(receta_content)

def mostrar_recetas(cat):
    print("Elige una receta de las siguientes:")
    for file in actual_path.joinpath(cat).glob('*'):
        print(file.name)   
    receta = input("¿Qué receta quieres?\n")
    if not actual_path.joinpath(cat).joinpath(receta).exists():
        print("Receta no válida. Por favor, elige una receta existente.")
        return mostrar_recetas(cat)
    else:
        leer_receta(cat, receta)

def leer_receta(cat, receta):
    archive = actual_path.joinpath(cat).joinpath(receta)

    print(archive.read_text())

mostrar_menu()