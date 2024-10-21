import random
import string


def gerador(maiusculas, minusculas, especiais, numeros, tamanho):
    caracteres = ""

    if maiusculas:
        caracteres += string.ascii_uppercase

    if minusculas:
        caracteres += string.ascii_lowercase

    if especiais:
        caracteres += "@#$"

    if numeros:
        caracteres += string.digits

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


print("=" * 45)
print(f"{'GERADOR DE SENHA':^45}")
print("=" * 45)
add_maiuscula = input("Adicionar letras maiúsculas? (s/n) ").lower() == "s"
add_minusculas = input("Adicionar minúsculas? (s/n) ").lower() == "s"
add_especiais = input("Adicionar caracteres especiais? (s/n) ").lower() == "s"
if not add_maiuscula and not add_minusculas and not add_especiais:
    print("Apenas números serão gerados.")
    add_numeros = True
else:
    add_numeros = input("Adicionar números? (s/n) ").lower() == "s"
tamanho = int(input("Tamanho da senha: (min 8 / max 32) "))
if tamanho < 8:
    print("Tamanho mínimo de 8 caracteres.")
    tamanho = 8
elif tamanho > 32:
    print("Tamanho máximo de 32 caracteres.")
    tamanho = 32

print(
    f"\nSenha gerada: {gerador(add_maiuscula, add_minusculas, add_especiais, add_numeros, tamanho)}"
)
print("=" * 45)
