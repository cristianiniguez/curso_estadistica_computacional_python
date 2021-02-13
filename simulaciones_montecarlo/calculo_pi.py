import random
import math


def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)


def desviacion_estandar(X):
    return math.sqrt(varianza(X))


def lanzar_agujas(numero_agujas):
    adentro_del_circulo = 0

    for _ in range(numero_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])

        distancia_desde_centro = math.sqrt(x**2 + y**2)
        if distancia_desde_centro <= 1:
            adentro_del_circulo += 1

    return (4 * adentro_del_circulo) / numero_agujas


def estimacion(numero_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = lanzar_agujas(numero_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma_estimados = desviacion_estandar(estimados)

    print(
        f'Estimado={round(media_estimados, 5)}, sigma={round(sigma_estimados, 5)}, agujas={numero_agujas}'
    )
    return (media_estimados, sigma_estimados)


def estimar_pi(precision, numero_intentos):
    numero_agujas = 1000
    sigma_pi = precision

    while sigma_pi >= precision / 1.96:
        media_pi, sigma_pi = estimacion(numero_agujas, numero_intentos)
        numero_agujas *= 2

    return media_pi


if __name__ == '__main__':
    print(estimar_pi(0.01, 100))
