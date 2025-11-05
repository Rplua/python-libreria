from libreria.biblioteca.biblioteca import Biblioteca
from libreria.libro.libro import Libro
from libreria.persona.persona import Persona

# 1️⃣ Creamos algunos libros
libro1 = Libro("El Quijote", "Miguel de Cervantes")
libro2 = Libro("Harry Potter", "J.K. Rowling")
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry")

# 2️⃣ Creamos una biblioteca
biblio = Biblioteca("Biblioteca Central", "Barcelona")

# 3️⃣ Añadimos los libros a la biblioteca
biblio.addNewBook(libro1)
biblio.addNewBook(libro2)
biblio.addNewBook(libro3)

# 4️⃣ Creamos algunas personas
persona1 = Persona("Valentina", "2000-07-10")
persona2 = Persona("Randy", "1997-12-14")

# 5️⃣ Prestamos un libro
biblio.borrowBook(libro1, persona1)  # Valentina toma "El Quijote"

# 6️⃣ Comprobamos quién tiene un libro concreto
biblio.whoBorrowed(libro1)
biblio.whoBorrowed(libro2)

# 7️⃣ Listamos todos los libros con su estado
biblio.listAll()

# 8️⃣ Devolvemos un libro
biblio.returnBook(libro1)

# 9️⃣ Volvemos a listar para ver el cambio
biblio.listAll()