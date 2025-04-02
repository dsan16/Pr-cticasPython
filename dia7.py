class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, saldo):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad}. Nuevo saldo: {self.saldo} euros.")

    def retirar(self, cantidad):
        if(cantidad > self.saldo):
            print("No hay suficiente saldo para retirar esa cantidad.")
            return
        self.saldo -= cantidad
        print(f"Se han retirado {cantidad}. Nuevo saldo: {self.saldo} euros.")

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Número de cuenta: {self.numero_cuenta}, Saldo: {self.saldo}"
    
cliente = Cliente("Juan", "Pérez", "123456789", 1000)

while True:
    print("1. Depositar")
    print("2. Retirar")
    print("3. Mostrar saldo")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        cantidad = float(input("¿Cuánto quieres depositar? "))
        cliente.depositar(cantidad)
    elif opcion == "2":
        cantidad = float(input("¿Cuánto quieres retirar? "))
        cliente.retirar(cantidad)
    elif opcion == "3":
        print(cliente)
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")