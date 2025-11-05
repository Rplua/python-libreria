

# 👇 Clase que representa la biblioteca
class Biblioteca:
    def __init__(self, name, city):
        # Nombre y ciudad de la biblioteca
        self.name = name
        self.city = city

        # Lista vacía de libros que posee la biblioteca
        # Aquí guardaremos objetos de tipo Libro
        self.libros = []

    # 🟩 Método para añadir un nuevo libro a la biblioteca
    def addNewBook(self, libro):
        # "libro" es un objeto de tipo Libro
        self.libros.append(libro)
        print(f"📚 Se añadió el libro '{libro.titulo}' a la biblioteca '{self.name}'.")

    # 🟨 Método para prestar un libro a una persona
    def borrowBook(self, libro, persona):
        # Comprobamos que el libro pertenece a la biblioteca
        if libro not in self.libros:
            raise ValueError("❌ El libro no pertenece a esta biblioteca.")

        # Si ya está prestado, no se puede volver a prestar
        if libro.isBorrowed:
            raise ValueError("❌ El libro ya está prestado.")

        # Marcamos el libro como prestado
        libro.isBorrowed = True
        libro.borrowed_by = persona
        print(f"🤝 '{libro.titulo}' ha sido prestado a {persona.name}.")

    # 🟦 Método para devolver un libro
    def returnBook(self, libro):
        # Comprobamos que el libro pertenece a la biblioteca
        if libro not in self.libros:
            raise ValueError("❌ El libro no pertenece a esta biblioteca.")

        # Marcamos el libro como disponible otra vez
        libro.isBorrowed = False
        print(f"🔁 '{libro.titulo}' ha sido devuelto.")
        libro.borrowed_by = None

    # 🔍 Saber quién tiene prestado un libro concreto
    def whoBorrowed(self, libro):
        if libro.borrowed_by:
            print(f"👤 El libro '{libro.titulo}' lo tiene {libro.borrowed_by.name}.")
        else:
            print(f"📗 El libro '{libro.titulo}' está disponible.")
        return libro.borrowed_by

    # 📚 Listar todos los libros
    def listAll(self):
        print(f"🏛️ Libros en '{self.name}':")
        for libro in self.libros:
            estado = "Prestado" if libro.isBorrowed else "Disponible"
            print(f" - {libro.titulo} ({estado})")

    # 📕 Listar solo los libros prestados
    def listBorrowed(self):
        return [l for l in self.libros if l.isBorrowed]

    # 📗 Listar solo los libros disponibles
    def listAvailable(self):
        return [l for l in self.libros if not l.isBorrowed]

    # 👤 Listar los libros prestados a una persona concreta
    def listBorrowedBy(self, persona):
        return [l for l in self.libros if l.borrowed_by == persona]