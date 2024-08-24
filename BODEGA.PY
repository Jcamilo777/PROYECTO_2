class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        if self.capacidad_maxima >= len(self.productos) + cantidad:
            self.productos.append((producto, cantidad))
        else:
            raise ValueError("Capacidad de la bodega excedida")

    def retirar_producto(self, producto, cantidad):
        for i, (prod, cant) in enumerate(self.productos):
            if prod == producto:
                if cant >= cantidad:
                    self.productos[i] = (prod, cant - cantidad)
                else:
                    raise ValueError("Cantidad a retirar excede el stock en la bodega")
                break

    def consultar_disponibilidad(self, producto):
        for prod, cant in self.productos:
            if prod == producto:
                return cant
        return 0
