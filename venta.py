class Venta:
    def __init__(self):
        self.numero_boleta = ""
        self.fecha = ""
        self.total = 0.0
        self.cliente = ""
        self.detalles = []

    def convertir(self):
        return "|{}|{}|{}".format(self.fecha, self.total, self.cliente)

