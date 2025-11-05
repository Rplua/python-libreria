
class Libro():
    def __init__(self, titulo, autor) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isBorrowed = False
        self.borrowed_by = None

