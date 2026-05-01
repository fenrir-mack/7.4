from abc import ABC, abstractmethod
from typing import List
from domain.livro import Livro

class ILivroRepository(ABC):
    @abstractmethod
    def obter_todos(self) -> List[Livro]:
        pass

    @abstractmethod
    def adicionar(self, livro: Livro) -> None:
        pass
