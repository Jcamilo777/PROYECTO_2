# Sistema de Gestión de Inventario

Este proyecto implementa un sistema de gestión de inventario en Python, permitiendo la creación y gestión de productos, categorías, proveedores y bodegas. El sistema incluye un menú interactivo para realizar diversas operaciones de inventario.

# Descripción
El sistema permite realizar las siguientes operaciones:

Agregar Producto: Crea un nuevo producto y lo asocia con una categoría.
Agregar Categoría: Crea una nueva categoría para agrupar productos.
Agregar Proveedor: Crea un nuevo proveedor de productos.
Agregar Bodega: Crea una nueva bodega para almacenar productos.
Agregar Stock a Producto: Aumenta la cantidad de stock de un producto existente.
Retirar Stock de Producto: Disminuye la cantidad de stock de un producto existente.
Consultar Disponibilidad de Producto en Bodega: Muestra la cantidad disponible de un producto en una bodega específica.

# Estructura de Clases
Producto
Clase que representa un producto en el inventario.

Atributos:

nombre: Nombre del producto.
descripcion: Descripción del producto.
precio: Precio del producto.
stock: Cantidad en inventario del producto.
categoria: Categoría a la que pertenece el producto (opcional).
Métodos:

agregar_stock(cantidad): Agrega una cantidad al stock del producto.
retirar_stock(cantidad): Retira una cantidad del stock del producto.
calcular_valor_total(): Calcula el valor total del stock del producto en base al precio.

# Categoria
Clase que representa una categoría de productos.

Atributos:

nombre: Nombre de la categoría.
descripcion: Descripción de la categoría.
productos: Lista de productos asociados a la categoría.
Métodos:

agregar_producto(producto): Agrega un producto a la categoría.
eliminar_producto(producto): Elimina un producto de la categoría.
listar_productos(): Retorna la lista de productos en la categoría.

# Proveedor
Clase que representa un proveedor de productos.

Atributos:

nombre: Nombre del proveedor.
direccion: Dirección del proveedor.
telefono: Teléfono del proveedor.
productos: Lista de productos ofrecidos por el proveedor.
Métodos:

agregar_producto(producto): Agrega un producto al proveedor.
eliminar_producto(producto): Elimina un producto del proveedor.
listar_productos(): Retorna la lista de productos ofrecidos por el proveedor.

# Bodega
Clase que representa una bodega donde se almacenan productos.

Atributos:

nombre: Nombre de la bodega.
ubicacion: Ubicación de la bodega.
capacidad_maxima: Capacidad máxima de productos en la bodega.
productos: Lista de productos almacenados en la bodega.
Métodos:

agregar_producto(producto, cantidad): Agrega una cantidad específica de un producto a la bodega.
retirar_producto(producto, cantidad): Retira una cantidad específica de un producto de la bodega.
consultar_disponibilidad(producto): Consulta la disponibilidad de un producto en la bodega.
Ejecución
Para ejecutar el sistema de gestión de inventario, ejecuta el script principal:

```bash
python main.py
```
Un menú interactivo te guiará a través de las opciones disponibles.

# Requisitos
Python 3.x
# Autor
Jcamilo777

