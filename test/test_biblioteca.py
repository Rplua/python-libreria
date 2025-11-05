import unittest

from libreria.biblioteca.biblioteca import Biblioteca
from libreria.libro.libro import Libro
from libreria.persona.persona import Persona


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada test: crea datos frescos."""
        self.biblio = Biblioteca("Biblioteca Central", "Barcelona")
        self.libro1 = Libro("El Quijote", "Miguel de Cervantes")
        self.libro2 = Libro("Harry Potter", "J.K. Rowling")
        self.persona = Persona("Valentina", "2000-07-10")

        # Añadimos libros al inventario
        self.biblio.addNewBook(self.libro1)
        self.biblio.addNewBook(self.libro2)

    def test_add_new_book(self):
        """Añadir libro debe incrementar el inventario y mantener la referencia exacta."""
        libro3 = Libro("El Principito", "Antoine de Saint-Exupéry")
        self.biblio.addNewBook(libro3)
        self.assertIn(libro3, self.biblio.libros)
        self.assertEqual(len(self.biblio.libros), 3)

    def test_borrow_book_ok(self):
        """Prestar un libro disponible debe marcarlo prestado y guardar quién lo tiene."""
        self.biblio.borrowBook(self.libro1, self.persona)
        self.assertTrue(self.libro1.isBorrowed)
        self.assertIs(self.libro1.borrowed_by, self.persona)

    def test_borrow_book_not_in_library(self):
        """Prestar un libro que no pertenece a la biblioteca debe fallar."""
        libro_ajeno = Libro("Clean Code", "Robert C. Martin")
        with self.assertRaises(ValueError):
            self.biblio.borrowBook(libro_ajeno, self.persona)

    def test_borrow_book_already_borrowed(self):
        """Prestar un libro ya prestado debe fallar."""
        self.biblio.borrowBook(self.libro1, self.persona)
        with self.assertRaises(ValueError):
            self.biblio.borrowBook(self.libro1, self.persona)

    def test_return_book_ok(self):
        """Devolver un libro de la biblioteca debe marcarlo disponible y limpiar borrowed_by."""
        self.biblio.borrowBook(self.libro2, self.persona)
        self.biblio.returnBook(self.libro2)
        self.assertFalse(self.libro2.isBorrowed)
        self.assertIsNone(self.libro2.borrowed_by)

    def test_return_book_not_in_library(self):
        """Devolver un libro que no es de la biblioteca debe fallar."""
        libro_ajeno = Libro("Refactoring", "Martin Fowler")
        with self.assertRaises(ValueError):
            self.biblio.returnBook(libro_ajeno)

    def test_who_borrowed(self):
        """whoBorrowed debe devolver la persona correcta o None si disponible."""
        self.assertIsNone(self.biblio.whoBorrowed(self.libro1))
        self.biblio.borrowBook(self.libro1, self.persona)
        self.assertIs(self.biblio.whoBorrowed(self.libro1), self.persona)

    def test_list_available_and_borrowed(self):
        """Las listas de disponibles/prestados deben reflejar el estado real."""
        disponibles = self.biblio.listAvailable()
        prestados = self.biblio.listBorrowed()
        self.assertIn(self.libro1, disponibles)
        self.assertIn(self.libro2, disponibles)
        self.assertEqual(len(prestados), 0)

        # Prestamos uno y comprobamos de nuevo
        self.biblio.borrowBook(self.libro2, self.persona)
        disponibles = self.biblio.listAvailable()
        prestados = self.biblio.listBorrowed()
        self.assertIn(self.libro1, disponibles)
        self.assertNotIn(self.libro2, disponibles)
        self.assertIn(self.libro2, prestados)

    def test_list_borrowed_by_person(self):
        """Listar libros prestados a una persona debe devolver solo los suyos."""
        otra_persona = Persona("Randy", "1997-12-14")
        self.biblio.borrowBook(self.libro1, self.persona)
        self.biblio.borrowBook(self.libro2, otra_persona)

        de_valentina = self.biblio.listBorrowedBy(self.persona)
        de_randy = self.biblio.listBorrowedBy(otra_persona)

        self.assertListEqual(de_valentina, [self.libro1])
        self.assertListEqual(de_randy, [self.libro2])


if __name__ == "__main__":
    unittest.main()