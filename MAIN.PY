from PRODUCTO import Producto
from CATEGORIA import Categoria
from PROVEEDOR import Proveedor
from BODEGA import Bodega

def main():
    # Crear algunas categorías
    categorias = {}
    categorias["Alimentos"] = Categoria("Alimentos", "Productos comestibles")
    categorias["Bebidas"] = Categoria("Bebidas", "Líquidos para consumo")

    # Crear algunos proveedores
    proveedores = {}
    proveedores["Proveedor Alimentos"] = Proveedor("Proveedor Alimentos", "Calle 123", "555-1234")

    # Crear algunas bodegas
    bodegas = {}
    bodegas["Bodega Principal"] = Bodega("Bodega Principal", "Ubicación 1", 200)

    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Agregar Producto")
        print("2. Agregar Categoría")
        print("3. Agregar Proveedor")
        print("4. Agregar Bodega")
        print("5. Agregar Stock a Producto")
        print("6. Retirar Stock de Producto")
        print("7. Consultar Disponibilidad de Producto en Bodega")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción del producto: ")
            precio = float(input("Precio del producto: "))
            stock = int(input("Stock inicial del producto: "))
            categoria_nombre = input("Nombre de la categoría: ")
            categoria = categorias.get(categoria_nombre)

            producto = Producto(nombre, descripcion, precio, stock, categoria)
            print(f"Producto {nombre} creado con éxito.")

        elif opcion == '2':
            nombre = input("Nombre de la categoría: ")
            descripcion = input("Descripción de la categoría: ")
            categoria = Categoria(nombre, descripcion)
            categorias[nombre] = categoria
            print(f"Categoría {nombre} creada con éxito.")

        elif opcion == '3':
            nombre = input("Nombre del proveedor: ")
            direccion = input("Dirección del proveedor: ")
            telefono = input("Teléfono del proveedor: ")
            proveedor = Proveedor(nombre, direccion, telefono)
            proveedores[nombre] = proveedor
            print(f"Proveedor {nombre} creado con éxito.")

        elif opcion == '4':
            nombre = input("Nombre de la bodega: ")
            ubicacion = input("Ubicación de la bodega: ")
            capacidad_maxima = int(input("Capacidad máxima de la bodega: "))
            bodega = Bodega(nombre, ubicacion, capacidad_maxima)
            bodegas[nombre] = bodega
            print(f"Bodega {nombre} creada con éxito.")

        elif opcion == '5':
            nombre_producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a agregar: "))
            producto = None  # Buscar el producto en alguna estructura de datos
            for categoria in categorias.values():
                for prod in categoria.listar_productos():
                    if prod.nombre == nombre_producto:
                        producto = prod
                        break

            if producto:
                producto.agregar_stock(cantidad)
                print(f"Se agregaron {cantidad} unidades al producto {nombre_producto}.")
            else:
                print("Producto no encontrado.")

        elif opcion == '6':
            nombre_producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad a retirar: "))
            producto = None  # Buscar el producto en alguna estructura de datos
            for categoria in categorias.values():
                for prod in categoria.listar_productos():
                    if prod.nombre == nombre_producto:
                        producto = prod
                        break

            if producto:
                try:
                    producto.retirar_stock(cantidad)
                    print(f"Se retiraron {cantidad} unidades del producto {nombre_producto}.")
                except ValueError as e:
                    print(e)
            else:
                print("Producto no encontrado.")

        elif opcion == '7':
            nombre_producto = input("Nombre del producto: ")
            nombre_bodega = input("Nombre de la bodega: ")
            bodega = bodegas.get(nombre_bodega)
            producto = None  # Buscar el producto en alguna estructura de datos
            for categoria in categorias.values():
                for prod in categoria.listar_productos():
                    if prod.nombre == nombre_producto:
                        producto = prod
                        break

            if producto and bodega:
                disponibilidad = bodega.consultar_disponibilidad(producto)
                print(f"Disponibilidad de {nombre_producto} en {nombre_bodega}: {disponibilidad} unidades")
            else:
                print("Producto o bodega no encontrados.")

        elif opcion == '8':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
