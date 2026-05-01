from typing import List, Tuple
from domain.livro import Livro
from domain.repository import ILivroRepository

class LivroUseCase:
    def __init__(self, repository: ILivroRepository):
        self.repository = repository

    def obter_todos_livros(self) -> List[Livro]:
        return self.repository.obter_todos()

    def filtrar_livros(self, chave: str, valor: str) -> List[Livro]:
        todos_os_livros = self.repository.obter_todos()
        
        resultado = []
        for livro in todos_os_livros:
            valor_livro = getattr(livro, chave, "")
            if str(valor_livro).lower() == str(valor).lower():
                resultado.append(livro)

        return resultado

    def adicionar_livro(self, titulo: str, autor: str, editora: str, categoria: str) -> Tuple[bool, str]:
        if not titulo or not autor:
            return False, "Título e Autor são obrigatórios."
        
        novo_livro = Livro(titulo, autor, editora, categoria)
        self.repository.adicionar(novo_livro)
        return True, "Livro adicionado com sucesso."
