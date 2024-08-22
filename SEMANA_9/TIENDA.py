#Creamos clases que vamos  utilizar con cada uno de sus atributos
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id= id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
#creamos la clases  para llamar a cada una de los atributos
    def __str__(self):
        return f" {self.id} {self.nombre} {self.cantidad} {self.precio}"

#creamos una lista
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto Agregado correctamente")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Error: Producto no encontrado.")

    def actualizar_precio(self, id, precio):
        for producto in self.productos:
            if producto.id == id:
                producto.precio = precio
                print(f"Producto actualizado exitosamente")

    def buscar_producto_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto)

mi_inventario = Inventario()

def Menu():
    while True:
        print("Menu")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))

            mi_inventario.agregar_producto(Producto(id, nombre, precio, id))

        elif opcion == 2:
            id = int(input("Ingrese el ID del producto a eliminar: "))
            mi_inventario.eliminar_producto(id)
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
            print("nombre buscado")
            print(producto.id, producto.nombre, producto.precio)

        elif opcion == 5:
            print("\nInventario")
            mi_inventario.mostrar_inventario()

        elif opcion == 6:
            break

if __name__ == "__main__":
    Menu()

