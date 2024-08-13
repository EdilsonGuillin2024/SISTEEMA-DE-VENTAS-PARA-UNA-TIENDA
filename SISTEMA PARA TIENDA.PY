# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}.")
        else:
            self.productos.append(producto)
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id):
        producto = self.buscar_producto_por_id(id)
        if producto:
            self.productos.remove(producto)
            print(f"Producto con ID {id} eliminado.")
        else:
            print(f"Error: No se encontró un producto con el ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = self.buscar_producto_por_id(id)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {id} actualizado.")
        else:
            print(f"Error: No se encontró un producto con el ID {id}.")

    def buscar_producto_por_id(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def buscar_productos_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)

# Funciones para mostrar el logo y la información
def mostrar_logo_uea():
    # Simulación de un logo usando caracteres ASCII
    print("""
**************************************************
*                                                *
*                  UEA                           *

*INGENIERIA EN TECNOLOGIAS D E LA INFORMACION    *
*                                                *
**************************************************
    """)

def mostrar_informacion():
    print("Ingeniería en Tecnologías de la Información\n")

# Función para mostrar el menú
def mostrar_menu():
    mostrar_logo_uea()
    mostrar_informacion()
    print("Gestión de Inventario")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

# Función principal
def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_productos_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            print("Saliendo del sistema de gestión de inventarios.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
