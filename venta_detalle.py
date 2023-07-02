class VentaDetalle:
    def __init__(self, venta, producto, precio, cantidad):
        self.venta = venta
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad

    def convertir(self):
        return "|{}|{}|{}| x {}".format(self.venta, self.producto, self.precio, self.cantidad)
