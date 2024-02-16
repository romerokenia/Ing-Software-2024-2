#Romero Estrada Kenia Surisadahi
def partido_tenis():
    jugador1 = input("Ingrese el nombre del Jugador 1: ")
    jugador2 = input("Ingrese el nombre del Jugador 2: ")

    puntos_jugador1 = 0
    puntos_jugador2 = 0

    while not juego_terminado(puntos_jugador1, puntos_jugador2):
        punto_ganado = input(f"¿Quien gano el punto? ¿{jugador1} o {jugador2}? ")

        if punto_ganado == jugador1:
            puntos_jugador1 += 1
        elif punto_ganado == jugador2:
            puntos_jugador2 += 1
        else:
            print("Entrada no válida. Ingresa 1 o 2.")

        puntuacion_jugador1 = calcular_puntuacion(puntos_jugador1)
        puntuacion_jugador2 = calcular_puntuacion(puntos_jugador2)

        print(f"Puntuación: {jugador1} ({puntuacion_jugador1}) - {jugador2} ({puntuacion_jugador2})")

    imprimir_resultado_final(jugador1, jugador2, puntos_jugador1, puntos_jugador2)


def juego_terminado(puntos_jugador1, puntos_jugador2):
    return max(puntos_jugador1, puntos_jugador2) >= 4 and abs(puntos_jugador1 - puntos_jugador2) >= 2


def calcular_puntuacion(puntos):
    if puntos == 0:
        return 0
    elif puntos == 1:
        return 15
    elif puntos == 2:
        return 30
    elif puntos == 3:
        return 40
    else:
        return 0  # Puedes ajustar esta lógica si es necesario para partidas más largas

def imprimir_resultado_final(jugador1, jugador2, puntos_jugador1, puntos_jugador2):
    if puntos_jugador1 > puntos_jugador2:
        print(f"¡{jugador1} gana con una puntuación de {calcular_puntuacion(puntos_jugador1)}!")
    else:
        print(f"¡{jugador2} gana con una puntuación de {calcular_puntuacion(puntos_jugador2)}!")


if __name__ == "__main__":
    partido_tenis()
