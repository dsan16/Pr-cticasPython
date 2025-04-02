def decorador_turno(func):
    def turnos():
        print("Gracias por utilizar el sistema de turnos.")
        resultado = func()
        print("Por favor, aguarde y será atendido.\n")
        return resultado
    return turnos

def generador_turnos(prefijo):
    numero = 1
    while True:
        yield f"{prefijo}-{numero}"
        numero += 1

turnos_perfumeria = generador_turnos("P")
turnos_farmacia = generador_turnos("F")
turnos_cosmetica = generador_turnos("C")

@decorador_turno
def siguiente_turno_perfumeria():
    print(f"Su turno es: {next(turnos_perfumeria)}")

@decorador_turno
def siguiente_turno_farmacia():
    print(f"Su turno es: {next(turnos_farmacia)}")

@decorador_turno
def siguiente_turno_cosmetica():
    print(f"Su turno es: {next(turnos_cosmetica)}")