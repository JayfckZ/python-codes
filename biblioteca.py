# ----------- CLASSES ----------- #


class Livro:
    def __init__(self, titulo, autor, ano, is_disponivel):
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
        return self.nome


class Usuario:
    def __init__(self, nome, livros_empretados):
        self.nome: str = nome
        self.livros_emprestados: list[Livro] = livros_empretados

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome) -> None:
        self.nome = nome

    def get_livros_emprestados(self) -> list[Livro]:
        return self.livros_emprestados

    def emprestar_livro(self, livro: Livro) -> None | str:
        if livro.get_disponibilidade:
            self.livros_emprestados.append(livro)
            livro.emprestar()
            return

        return "Livro não disponível para ser emprestado."
    

    def devolver_livro(self, livro: Livro) -> None | str:
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.devolver()
            return
        
        return "Livro não foi emprestado."
    

class Biblioteca:
    def __init__(self, livros, usuarios):
        self.livros: list[Livro] = livros
        self.usuarios: list[Usuario] = usuarios

    
    def get_livros(self) -> list[Livro]:
        return self.livros

    
    def set_livro(self, livro: Livro) -> None:
        self.livros.append(livro)

    
    def get_usuarios(self) -> list[Usuario]:
        return self.usuarios

    
    def set_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)


    def get_livros_disponiveis(self) -> str | list[Livro]:
        livros_disponiveis = []

        for livro in self.livros:
            if livro.get_disponibilidade():
                livros_disponiveis.append(livro)
        
        return livros_disponiveis if livros_disponiveis else "Nenhum livro disponível."

# ----------- MAIN ----------- #
