from functools import reduce

def transformador(lista: list, funcoes: list) -> list:
    return reduce(funcoes[2], filter(funcoes[1], map(funcoes[0], lista)))

funcoes = [
    lambda x: x ** 2,
    lambda x: x > 2,
    lambda a, b: a + b
]
print(transformador([1, 2, 3, 4], funcoes))