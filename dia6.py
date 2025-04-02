from os import system
from pathlib import Path

actual_path = Path.cwd().joinpath('Recetas')
print("Elige una receta de las siguientes:")


def mostrar_menu():
    print("1. Leer receta")
    print("2. Añadir receta")
    print("3. Añadir categoría")
    print("4. Eliminar recetas")
    print("5. Salir")
    option = int(input("¿Qué quieres hacer?\n"))

    if(option < 1 or option > 5):
        print("Opción no válida. Por favor, elige una opción entre 1 y 4.")
        return mostrar_menu()
    elif(option == 1 or option == 2 or option == 4):
        mostrar_capeta_archivo(option)
    elif(option == 3):
        crear_categoria()
    return option

def crear_categoria():
    cat = input("¿Qué categoría quieres crear?\n")
    if actual_path.joinpath(cat).exists():
        print("Categoría ya existe. Por favor, elige otra categoría.")
        return crear_categoria()
    else:
        actual_path.joinpath(cat).mkdir()
        print(f"Categoría '{cat}' creada con éxito.")
        return cat

def mostrar_capeta_archivo(option):
    print("Elige una categoría de las siguientes:")
    for file in actual_path.glob('*'):
        print(file.name)   
    cat = input("¿Qué categría quieres?\n")
    if not actual_path.joinpath(cat).exists():
        print("Categoría no válida. Por favor, elige una categoría existente.")
        return mostrar_capeta_archivo(option)
    else:
        if(option == 2):
            agregar_receta(cat)
        else:
            mostrar_eliminar_recetas(cat, option)


def agregar_receta(cat):
    new_path = actual_path.joinpath(cat)
    receta = input("¿Qué receta quieres añadir (sin sufijo txt)?\n")
    new_path = new_path / f"{receta}.txt"

    receta_content = input("¿Qué quieres añadir a la receta?\n")

    new_path.write_text(receta_content)

def mostrar_eliminar_recetas(cat, option):
    print("Elige una receta de las siguientes:")
    for file in actual_path.joinpath(cat).glob('*'):
        print(file.name)   
    receta = input("¿Qué receta quieres?\n")
    if not actual_path.joinpath(cat).joinpath(receta).exists():
        print("Receta no válida. Por favor, elige una receta existente.")
        return mostrar_eliminar_recetas(cat)
    elif option == 1:
        leer_receta(cat, receta)
    else:
        eliminar_receta(cat, receta)

def eliminar_receta(cat, receta):
    archive = actual_path.joinpath(cat).joinpath(receta)
    archive.unlink()
    print(f"Receta '{receta}' eliminada con éxito.")

def leer_receta(cat, receta):
    archive = actual_path.joinpath(cat).joinpath(receta)

    print(archive.read_text())

options_loop = 0
while options_loop != 5:
    options_loop = mostrar_menu()