

class Biblioteca:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.libros = []  # la biblioteca "tiene" libros (has-a)

    # Inventario
    def addNewBook(self, libro):
        self.libros.append(libro)

    # Reglas de préstamo
    def borrowBook(self, libro, persona):
        if libro not in self.libros:
            raise ValueError("El libro no pertenece a esta biblioteca.")
        if libro.isBorrowed:
            raise ValueError("El libro ya está prestado.")
        libro.isBorrowed = True
        libro.borrowed_by = persona

    def returnBook(self, libro):
        if libro not in self.libros:
            raise ValueError("El libro no pertenece a esta biblioteca.")
        libro.isBorrowed = False
        libro.borrowed_by = None

    # Consultas útiles
    def whoBorrowed(self, libro):
        return libro.borrowed_by  # Persona o None

    def listAll(self):
        return list(self.libros)  # todos los libros

    def listBorrowed(self):
        return [l for l in self.libros if l.isBorrowed]

    def listAvailable(self):
        return [l for l in self.libros if not l.isBorrowed]

    def listBorrowedBy(self, persona):
        return [l for l in self.libros if l.borrowed_by == persona]