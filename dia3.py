text = input("¿Inserta un texto entero?\n").upper()

chars = input("Inserta 3 letras separadas por comas sin espacios:\n").upper()

chars = chars.split(",")

print(chars)
print(text)

print(f" 1.- {chars[0]}: {text.count(chars[0])} {chars[1]}:{text.count(chars[1])} {chars[2]}:{text.count(chars[2])}")

palabras = text.split(" ")
print(palabras)
print(f"2.- El texto tiene {len(palabras)} palabras")

print(f"3.- Primera letra: {text[0]}\nUltima letra: {text[-1]}")

palabras.reverse()
print(f"4.- {' '.join(palabras)}")

print(f"5.- ¿Está la palabra Python en el texto? {'Python'.upper() in text}")