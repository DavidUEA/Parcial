class Libro:
    def __init__(self,isbn, titulo, autor, categoria):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.informacion = (autor,titulo)

    def __str__(self):
        return f"ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, Categoria: {self.categoria}"

class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.lista_usuarios = []


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids = set ()

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro {libro.titulo} ya existe")
        else:
            self.libros[libro.isbn] = libro
            self.ids.add(libro.isbn)
            print(f"El Libro {libro.titulo} fue agregado")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"El libro {isbn} fue eliminado ")
        else:
            print(f"El libro {isbn} No existe ")


    def agregar_usuario(self, usuario):
        if usuario.id in self.lista_usuarios:
            print(f"El usuario {usuario.id} ya existe")
        else:
            self.usuarios[usuario.id] = usuario
            self.id.add(usuario.id)
            print(f"El usuario {usuario.id} ha sido agregado")

    def dar_baja_usuario(self, id):
        if id in self.ids:
            del self.usuarios[id]
            print(f"El usuario {id} si existe")
        else:
            print(f"El usuario {id} no existe")

    def buscar_libro_nombre(self, titulo):
       if titulo in self.libros:
           return self.libros[titulo]
       else:
            return None


    def prestar_libro(self, id, isbn):
        if id not in self.usuarios:
            print(f"El {id} No existe")
        elif isbn not in self.libros:
            print(f"El libro {isbn} no existe")
        else:
            usuario = self.usuarios[id]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            print(f"Al usuario {id} fue prestado el libro {libro.titulo}")

    def listar_libros_prestados(self, id):
        if id in self.usuarios:
            usuario = self.usuarios[id]
            if usuario.libros_prestados:
                print(f"El libro fue prestado al usuario {usuario.titulo}")
                for libro in usuario.libros_prestados:
                    print(libro)
def Menu():
    mi_biblioteca = Biblioteca()
    while True:
        print("Menu")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Agregar usuario")
        print("4. Dar de baja a usuario")
        print("5. Prestar libro")
        print("6. Buscar libro")
        print ("7. Lista libros prestados")
        print("8. Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            titulo = input ("Ingrese el ISBN del libro: ")
            autor = input ("Ingrese el titulo del libro: ")
            categoria = input ("Ingresa el autor del libro: ")
            isbn = input ("Ingrese la categoria del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            mi_biblioteca.agregar_libro(libro)
            print(libro)
            print("Libro agregado")

        elif opcion == 2:
            isbn = input("Ingrese el ISBN del libro: ")
            mi_biblioteca.quitar_libro(isbn)
            print(isbn)
            print("El producto ha sido eliminado ")

        elif opcion == 3:
            id = int(input("Ingrese el id del Usuario: "))
            nombre = input("Ingrese el nombre del usuario: ")
            print(id, nombre)
            print(f"---El usuario con ID: {id} de nombres {nombre} ha sido agregado---")


        elif opcion == 4:
            id = input("Ingrese el ISBN del libro: ")
            mi_biblioteca.dar_baja_usuario(id)
            print(id)
            print("El producto ha sido eliminado ")

        elif opcion == 5:
            id = input("Ingrese el id del usuario para registrar el prestamo: ")
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            usuario = usuario(id,isbn)
            mi_biblioteca.prestar_libro(id,isbn)
            print(usuario)
            print(f"El libro {isbn} ha sido prestado a {id}")


        elif opcion == 6:
            print ("\nBuscar libro")
            nombre = input ("Ingrese el titulo del libro : ")
            nombre = mi_biblioteca.buscar_libro_nombre (nombre)
            if nombre is not None:
                print (f"ISBN: {libro.isbn}, nombre del autor: {libro.titulo} ")
            else:
                print ("nombre no encontrado")


        elif opcion == 7:
            mi_biblioteca.listar_libros_prestados("1")
            print(mi_biblioteca)


        elif opcion == 5:
            print("\nInventario")
            mi_biblioteca.mostrar_biblioteca()

        elif opcion == 8:
            break

if __name__ == "__main__":
    Menu()


