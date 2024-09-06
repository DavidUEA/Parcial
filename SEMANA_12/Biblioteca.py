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

    def quitar_libro(self, libro):
        if libro.isbn in self.libros:
            del self.libros[libro.isbn]
            print(f"El libro {libro.titulo} fue eliminado")
        else:
            print(f"El libro {libro.titulo} No existe")


    def agregar_usuario(self, usuario):
        if usuario.isbn in self.usuarios:
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
        print("1. agregar_libro")
        print("2. quitar_libro")
        print("3. agregar_usuario")
        print("4. dar_baja_usuario")
        print("5. prestar_libro")
        print("6. Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            titulo = input("Ingrese el Titulo del libro: ")
            autor = input("Ingrese el nombre del autor: ")
            categoria = input("Ingresa la categoria del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            mi_biblioteca.agregar_libro(libro)
            print(libro)
            print("Libro agregado")

        elif opcion == 2:
            isbn = input("Ingrese el ISBN del libro")
            mi_biblioteca.quitar_libro(isbn)
            print(isbn)
            print("El producto ha sido eliminado")

        elif opcion == 3:
            print("\nActualizar ")
            id = int(input("Ingrese el ID del producto a actualizar: "))
            precio = float(input("Ingrese precio del producto: "))
            mi_inventario.actualizar_precio(id, precio)
            print("Precio actualizado")

        elif opcion == 4:
            print("\nBuscar Nombre")
            nombre = input("Ingrese el nombre del producto: ")
            producto = mi_inventario.buscar_producto_nombre(nombre)
            if producto is not None:
                print(f"ID: {producto.id}, nombre: {producto.nombre}")
            else:
                print("nombre no encontrado")


        elif opcion == 5:
            print("\nInventario")
            mi_biblioteca.mostrar_biblioteca()

        elif opcion == 6:
            break

if __name__ == "__main__":
    Menu()


