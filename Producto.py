class producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def convertir(self):
        return "|{}|{}|{}".format(self.codigo, self.nombre, self.precio)
