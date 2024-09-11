from functools import reduce

vendas = {
    "Carlos": [900, 750, 100, 500],
    "José": [1200, 800, 1500, 1000],
    "Maria": [800, 600, 750, 900],
    "João": [1000, 1500, 1200, 700],
    "Pedro": [700, 900, 800, 600],
    "Ana": [600, 800, 700, 1000],
    "Lucas": [1300, 1100, 1400, 900],
    "Jorge": [1500, 1200, 1000, 800],
    "Marcos": [1100, 1400, 1300, 900],
}


# Função para calcular a quantidade de vendas
def total_vendas(vendedores: dict) -> dict:
    return {
        vendedor: reduce(lambda x, y: x + y, valores)
        for vendedor, valores in vendedores.items()
    }


# Função para gerar o ranking baseado no valor vendido
def gera_ranking(total_vendas: dict) -> list:
    total_vendas = sorted(total_vendas, key=total_vendas.get, reverse=True)
    return total_vendas


# Calculando o total de vendas por vendedor
ranking = gera_ranking(total_vendas(vendas))
print(ranking)
