# ----------- CLASSES ----------- #


class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, is_disponivel: bool = True):
        self.titulo: str = titulo
        self.autor: str = autor
        self.ano: int = ano
        self.is_disponivel: bool = is_disponivel

    def get_titulo(self) -> str:
        return self.titulo

    def set_titulo(self, titulo: str) -> None:
        self.titulo = titulo

    def get_autor(self) -> str:
        return self.autor

    def set_autor(self, autor: str) -> None:
        self.autor = autor

    def get_ano(self) -> int:
        return self.ano

    def set_ano(self, ano: int) -> None:
        self.ano = ano

    def get_disponibilidade(self) -> bool:
        return self.is_disponivel

    def emprestar(self) -> None:
        self.is_disponivel = False

    def devolver(self) -> None:
        self.is_disponivel = True

    def __str__(self) -> str:
        return self.titulo


class Usuario:
    def __init__(self, nome: str, livros_emprestados: list[Livro]=None):
        self.nome: str = nome
        self.livros_emprestados: list[Livro] = (
            livros_emprestados if livros_emprestados else []
        )

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome) -> None:
        self.nome = nome

    def get_livros_emprestados(self) -> list[Livro]:
        return [livro.get_titulo() for livro in self.livros_emprestados]

    def emprestar_livro(self, livro: Livro) -> None:
        if livro.get_disponibilidade():
            self.livros_emprestados.append(livro)
            livro.emprestar()
            return

        print("Livro não disponível para ser emprestado.")
        return

    def devolver_livro(self, livro: Livro) -> None:
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.devolver()
            return

        print("Livro não foi emprestado.")
        return


class Biblioteca:
    def __init__(self, livros: list[Livro], usuarios: list[Usuario]):
        self.livros: list[Livro] = livros
        self.usuarios: list[Usuario] = usuarios

    def get_livros(self) -> list[Livro]:
        return self.livros

    def adicionar_livro(self, livro: Livro) -> None:
        self.livros.append(livro)

    def get_usuarios(self) -> list[Usuario]:
        return self.usuarios

    def adicionar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)

    def get_livros_disponiveis(self) -> list[Livro]:
        return [livro.get_titulo() for livro in self.livros if livro.get_disponibilidade()] 


# ----------- MAIN ----------- #

# Criando alguns livros
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

# Criando um usuário
usuario1 = Usuario("Maria")

# Criando uma biblioteca e adicionando livros e usuários
biblioteca = Biblioteca([livro1, livro2], [usuario1])

# Exibindo livros disponíveis
print("Livros disponíveis:", biblioteca.get_livros_disponiveis())

# Usuário empresta um livro
usuario1.emprestar_livro(livro1)
print("Livros emprestados por Maria:", usuario1.get_livros_emprestados())

# Exibindo livros disponíveis novamente
print("Livros disponíveis:", biblioteca.get_livros_disponiveis())

# Usuário devolve o livro
usuario1.devolver_livro(livro1)
print("Livros disponíveis após devolução:", biblioteca.get_livros_disponiveis())
