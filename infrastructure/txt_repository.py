import json
import os
from typing import List
from domain.livro import Livro
from domain.repository import ILivroRepository

class TxtLivroRepository(ILivroRepository):
    def __init__(self, filepath: str = "banco.txt"):
        self.filepath = filepath
        # Ensure the file and directory exist
        os.makedirs(os.path.dirname(os.path.abspath(self.filepath)), exist_ok=True)
        if not os.path.exists(self.filepath):
            open(self.filepath, 'w', encoding='utf-8').close()

    def obter_todos(self) -> List[Livro]:
        livros = []
        with open(self.filepath, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    dados = json.loads(linha)
                    livros.append(Livro(**dados))
        return livros

    def adicionar(self, livro: Livro) -> None:
        with open(self.filepath, 'a', encoding='utf-8') as f:
            f.write(json.dumps(livro.to_dict()) + '\n')
