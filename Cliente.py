class cliente:
    def __init__(self, dni, nombres, apellidos, direccion, telefono):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono

    def convertir(self):
        return "|{}|{}|{}|{}|{}".format(self.dni, self.nombres, self.apellidos, self.direccion, self.telefono)

