from functools import reduce


modelos = [
    {"nome": "João", "notas": [9.0, 7.0, 10.0]},
    {"nome": "Maria", "notas": [5.0, 7.0, 3.0]},
    {"nome": "John", "notas": [9.0, 8.0, 6.0]},
]


# função principal pra calcular as notas
def calc_notas(alunos: list) -> list:
    resultados = []

    # iterando sobre cada item da lista fornecida
    for aluno in alunos:
        # usando reduce para somar as notas e len para o total e calculando a média
        media = reduce(lambda x, y: x + y, aluno["notas"]) / len(aluno["notas"])

        # se a media for maior que 7 adiciona ao resusultados e pula pro próximo aluno caso houver
        if media >= 7:
            resultados.append({"nome": aluno["nome"], "aprovado": True})
            continue

        resultados.append({"nome": aluno["nome"], "aprovado": False})

    return resultados


for resultado in calc_notas(modelos):
    print(f"Nome: {resultado['nome']}\n" + f"Aprovado: {resultado['aprovado']}\n")
