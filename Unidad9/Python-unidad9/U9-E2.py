from functools import reduce


def sacarImpares(listaColocada):
    numerosImpar = list(filter(lambda x: x % 2 != 0, listaColocada))
    sumaNumeros = reduce((lambda a, b: a + b), numerosImpar)
    return f'la lista de numeros impares fue: {numerosImpar} y su suma da {sumaNumeros}'


print(sacarImpares([1, 2, 3, 4, 5, 6, 7, 13]))
