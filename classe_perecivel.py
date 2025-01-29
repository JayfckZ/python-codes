class Produto:
    def __init__(self, nome, id, validade):
        self._nome = nome
        self._id = id
        self._validade = validade

    def get_nome(self):
        return self._nome

    def get_id(self):
        return self._id

    def get_validade(self):
        return self._validade


class Produto_Perecivel(Produto):
    pass


prods = int(input("Quantos produtos você quer adicionar? - "))
produtos = []
for i in range(prods):
    prov_nome = input("Nome do produto: ")
    prov_id = "ID" + input("ID: ")
    prov_validade = input("Validade (dd/mm/aaaa): ")
    is_perecivel = input("É perecível? (s/n) ")

    if is_perecivel.lower() == "s":
        produto = Produto_Perecivel(prov_nome, prov_id, prov_validade)
    else:
        produto = Produto(prov_nome, prov_id, prov_validade)

    produtos.append(produto)

print("*" * 45)
for produto in produtos:
    if type(produto) == Produto_Perecivel:
        print(
            f"Produto perecível - Nome: {produto.get_nome()}, ID: {produto.get_id()}, Validade: {produto.get_validade()}"
        )
    else:
        print(
            f"Nome: {produto.get_nome()}, ID: {produto.get_id()}, Validade: {produto.get_validade()}"
        )
print("*" * 45)
