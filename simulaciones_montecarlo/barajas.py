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


def main(tamanho_mano, intentos):
    baraja = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(baraja, tamanho_mano)
        manos.append(mano)

    pares = 0
    tricas = 0
    for mano in manos:
        # obteniendo los valores de la mano
        valores = []
        for carta in mano:
            valores.append(carta[1])

        # contando cuantas veces salio cada valor
        counter = dict(collections.Counter(valores))

        # contando las manos que son par
        for val in counter.values():
            if val == 2:
                pares += 1
                break

        # contando las manos que son trica
        for val in counter.values():
            if val == 3:
                tricas += 1
                break

    probabilidad_par = pares / intentos
    probabilidad_trica = tricas / intentos

    print(f"""
Probabilidad de obtener un par en una mano de {tamanho_mano} carta(s) = {probabilidad_par}
Probabilidad de obtener una trica en una mano de {tamanho_mano} carta(s) = {probabilidad_trica}
    """)


if __name__ == '__main__':
    tamanho_mano = int(input('¿De cuantas cartas sera la mano?: '))
    intentos = int(input('¿Cuantos intentos para calcular la probabilidad?: '))
    main(tamanho_mano, intentos)
