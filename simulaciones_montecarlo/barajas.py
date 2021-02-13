import random
import collections

PALOS = ['espada', 'corazon', 'diamante', 'trebol']
VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def crear_baraja():
    baraja = []
    for palo in PALOS:
        for valor in VALORES:
            baraja.append((palo, valor))
    return baraja


def obtener_mano(baraja, tamanho_mano):
    mano = random.sample(baraja, tamanho_mano)
    return mano


def obtener_conteo_valores(mano):
    valores = []
    for carta in mano:
        valores.append(carta[1])
    counter = dict(collections.Counter(valores))
    return counter


def contar_pares(manos):
    pares = 0
    for mano in manos:
        conteo_valores = obtener_conteo_valores(mano)
        for val in conteo_valores.values():
            if val == 2:
                pares += 1
                break
    return pares


def contar_tercias(manos):
    tercias = 0
    for mano in manos:
        conteo_valores = obtener_conteo_valores(mano)
        for val in conteo_valores.values():
            if val == 3:
                tercias += 1
                break
    return tercias


def contar_poquers(manos):
    poquers = 0
    for mano in manos:
        conteo_valores = obtener_conteo_valores(mano)
        for val in conteo_valores.values():
            if val == 4:
                poquers += 1
                break
    return poquers


def main(tamanho_mano, intentos):
    baraja = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(baraja, tamanho_mano)
        manos.append(mano)

    pares = contar_pares(manos)
    tercias = contar_tercias(manos)
    poquers = contar_poquers(manos)

    probabilidad_par = pares / intentos
    probabilidad_tercia = tercias / intentos
    probabilidad_poquer = poquers / intentos

    print(f"""
Probabilidad de obtener un par en una mano de {tamanho_mano} carta(s) = {probabilidad_par}
Probabilidad de obtener una tercia en una mano de {tamanho_mano} carta(s) = {probabilidad_tercia}
Probabilidad de obtener una poquer en una mano de {tamanho_mano} carta(s) = {probabilidad_poquer}
    """)


if __name__ == '__main__':
    tamanho_mano = int(input('¿De cuantas cartas sera la mano?: '))
    intentos = int(input('¿Cuantos intentos para calcular la probabilidad?: '))
    main(tamanho_mano, intentos)
