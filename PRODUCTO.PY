class Producto:
    def __init__(self, nombre, descripcion, precio, stock, categoria=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            raise ValueError("Cantidad a retirar excede el stock disponible")

    def calcular_valor_total(self):
        return self.precio * self.stock
