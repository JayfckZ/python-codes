import numpy as np

def analise_array(array):
    """
    soma
    media
    max e min
    indice maior e menor
    soma par
    soma impar
    vetor com negativos substituidos por 0
    """

    resultado = {}

    resultado["soma"] = np.sum(array)
    resultado["media"] = np.mean(array)
    resultado["max"], resultado["i_max"] = np.max(array), np.argmax(array)
    resultado["min"], resultado["i_min"] = np.min(array), np.argmin(array)
    resultado["soma_par"] = np.sum(np.where(array % 2 == 0, array, 0))
    resultado["soma_impar"] = np.sum(np.where(array % 2 != 0, array, 0))
    resultado["array_positivo"] = np.where(array < 0, 0, array)

    return resultado



array = np.array([-3, 7, -9, 2, 0, 10, -5, 6, -1, 8])

resultado = analise_array(array)

print(f"Soma: {resultado['soma']}")
print(f"Media: {resultado['media']}")
print(f"Maior número: {resultado['max']}")
print(f"Índice do maior Número: {resultado['i_max']}")
print(f"Menor número: {resultado['min']}")
print(f"Índice do menor número: {resultado['i_min']}")
print(f"Soma dos valores pares: {resultado['soma_par']}")
print(f"Soma dos valores ímpares: {resultado['soma_impar']}")
print(f"Array substituído: {resultado['array_positivo']}")