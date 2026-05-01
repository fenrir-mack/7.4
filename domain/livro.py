class Livro:
    def __init__(self, titulo, autor, editora, categoria):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.categoria = categoria

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "editora": self.editora,
            "categoria": self.categoria
        }
