nombre = input("¿Cuál es tu nombre? ")
ingresos = input("¿Cuánto dinero has ganado este mes? ")

comision = round(float(ingresos) * 13 / 100, 2)

print(f"Hola {nombre}, tu comisión es de {comision} euros.")