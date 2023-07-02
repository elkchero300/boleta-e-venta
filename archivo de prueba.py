from Cliente import cliente
from Producto import producto
from venta_detalle import VentaDetalle
from venta import Venta

ventas = []

contador = 0

datos_cliente = [
    {"dni": "47259697", "nombres": "Noe Wilber", "apellidos": "Tipo Mamani", "direccion": "jr tupac yupanqui 590 juliaca", "telefono": "997124032"},
    {"dni": "71849102", "nombres": "grober", "apellidos": "Huisa Apaza", "direccion": "salida cusco", "telefono": "99999999"},
    {"dni": "74059496", "nombres": "Rosa Maria de los angeles", "apellidos": "Torres Apaza", "direccion": "Jr. Jose Galvez", "telefono": "9888888"},
    {"dni": "75902902", "nombres": "Yohan", "apellidos": "Escarcena", "direccion": "Salida Puno", "telefono": "20022145"},
    {"dni": "76606525", "nombres": "jhosue", "apellidos": "pastor", "direccion": "san miguel ", "telefono": "944501816"}
]

datos_producto = [
    {"codigo": "001", "nombre": "Sujetador de encaje", "precio": 25.99},
    {"codigo": "002", "nombre": "Panties de algodón", "precio": 9.99},
    {"codigo": "003", "nombre": "Camisón sedoso", "precio": 39.99},
    {"codigo": "004", "nombre": "Tanga de encaje", "precio": 12.99},
    {"codigo": "005", "nombre": "Braguitas de satén", "precio": 14.99},
    {"codigo": "006", "nombre": "Babydoll transparente", "precio": 29.99},
    {"codigo": "007", "nombre": "Bustier de encaje", "precio": 34.99},
    {"codigo": "008", "nombre": "Pijama de seda", "precio": 49.99},
    {"codigo": "009", "nombre": "Medias de malla", "precio": 8.99},
    {"codigo": "010", "nombre": "Corsé de cuero", "precio": 59.99},
]

clientes = []

def insertar_cliente():
    dni = input("Ingrese DNI del cliente: ") 
    nombre = input("Ingrese nombre del cliente: ")
    apellido = input("Ingrese apellido del cliente: ")
    direccion = input("Ingrese dirección del cliente: ")
    telefono = input("Ingrese teléfono del cliente: ")
    clientes.append(cliente(dni, nombre, apellido, direccion, telefono))
    return clientes

def lista_clientes():
    for cliente in clientes:
        print(cliente.convertir())
    for cliente in datos_cliente:
        print("|{}|{}|{}|{}|{}|".format(cliente["dni"], cliente["nombres"], cliente["apellidos"], cliente["direccion"], cliente["telefono"]))

def buscar_cliente():
    dni = input("Ingrese el DNI del cliente: ")
    encontrado = False
    for cliente in clientes:
        if cliente.dni == dni:
            print(cliente.convertir())
            encontrado = True
            break
    for cliente in datos_cliente:
        if cliente["dni"] == dni:
            print("|{}|{}|{}|{}|{}|".format(cliente["dni"], cliente["nombres"], cliente["apellidos"], cliente["direccion"], cliente["telefono"]))
            encontrado = True
            break
    if not encontrado:
        print("Cliente no encontrado.")

def editar_datos_cliente():
    dni = input("Ingrese el DNI de la Persona: ")
    encontrado = False
    for cliente in clientes:
        if cliente.dni == dni:
            print(cliente.convertir())
            cliente.nombres = input("Ingrese nombres de la Persona: ")
            cliente.apellidos = input("Ingrese apellidos de la Persona: ")
            cliente.direccion = input("Ingrese dirección de la Persona: ")
            cliente.telefono = input("Ingrese telefono de la Persona: ")
            encontrado = True
            break
    if not encontrado:
        print("Cliente no encontrado.")

def eliminar_cliente():
    dni = input("Ingrese el DNI del cliente a eliminar: ")
    encontrado = False
    for cliente in clientes:
        if cliente.dni == dni:
            clientes.remove(cliente)
            encontrado = True
            break
    if not encontrado:
        print("Cliente no encontrado.")

def insertar_producto():
    codigo = input("Ingrese código del producto: ")
    nombre = input("Ingrese nombre del producto: ")
    precio = float(input("Ingrese precio del producto: "))
    producto_nuevo = producto(codigo, nombre, precio)
    datos_producto.append({"codigo": codigo, "nombre": nombre, "precio": precio})
    return producto_nuevo

def lista_productos():
    for producto in datos_producto:
        print("|{}|{}|{}|".format(producto["codigo"], producto["nombre"], producto["precio"]))

def buscar_producto():
    codigo = input("Ingrese el código del producto: ")
    encontrado = False
    for producto in datos_producto:
        if producto["codigo"] == codigo:
            print("|{}|{}|{}|".format(producto["codigo"], producto["nombre"], producto["precio"]))
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")


def editar_datos_producto():
    codigo:str = input("Ingrese el codigo del producto: ")
    for producto in datos_producto:
        if producto.codigo == codigo:
            print(producto.convertir())
            producto.nombre_producto = input("Ingrese nombre del producto: ")
            producto.precio = input("Ingrese el precio del producto: ")
    for producto in datos_producto:
        if producto["codigo"] == codigo:
            print("|{}|{}|{}|".format(producto["codigo"], producto["nombre"], producto["precio"]))
            producto["nombre"] = input("Ingrese el nombre del producto: ")
            producto["precio"] = float(input("Ingrese el precio del producto: "))

def eliminar_producto():
    codigo = input("Ingrese el código del producto: ")
    encontrado = False
    for indice, producto in enumerate(producto):
        if producto.codigo == codigo:
            print(producto.convertir())
            producto.pop(indice)
            encontrado = True
            break
    for indice, producto in enumerate(datos_producto):
        if producto["codigo"] == codigo:
            print("|{}|{}|{}|".format(producto["codigo"], producto["nombre"], producto["precio"]))
            datos_producto.pop(indice)
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

#============================================================


def registrar_venta():
    global contador 

    venta = Venta()
    venta.fecha = input("Ingrese la fecha de la venta: ")
    venta.numero_boleta = contador + 1
    print("La fecha de la venta es:", venta.fecha)
    dni_cliente = input("Ingrese el DNI del cliente: ")

    encontrado = False
    for cliente_obj in clientes:
        if cliente_obj.dni == dni_cliente:
            print("El cliente es:", cliente_obj.nombres , cliente_obj.apellidos , "dni: ", cliente_obj.dni)
            venta.cliente = cliente_obj
            encontrado = True
            break

    if not encontrado:
        for cliente_dict in datos_cliente:
            if cliente_dict["dni"] == dni_cliente:
                print("El cliente es:", cliente_dict["nombres"] , cliente_dict["apellidos"], "dni: ",cliente_dict["dni"])
                venta.cliente = cliente(dni_cliente, cliente_dict["nombres"], cliente_dict["apellidos"], cliente_dict["direccion"], cliente_dict["telefono"])
                encontrado = True
                break

    if not encontrado:
        print("Cliente no encontrado.")
        return

    venta.total = 0.0
    opcion = "s"
    while opcion.lower() == "s":
        print("Lista de productos:")
        for producto in datos_producto:
            print("| {} | {} | {} |".format(producto["codigo"], producto["nombre"], producto["precio"]))

        codigo = input("Ingrese el código del producto: ")
        encontrado = False
        for producto in datos_producto:
            if producto["codigo"] == codigo:
                cantidad = int(input("Ingrese la cantidad de unidades: "))
                detalle = VentaDetalle(producto["codigo"], producto["nombre"], producto["precio"], cantidad)
                venta.detalles.append(detalle)
                venta.total += producto["precio"] * cantidad
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
        
        opcion = input("¿Desea agregar otro producto? (s/n): ")
        if opcion.lower() == "n":
            break


    ventas.append(venta)
    contador += 1
    print("Venta registrada con éxito.")

def lista_ventas():
    if len(ventas) == 0:
        print("No se han registrado ventas.")
    else:
        print("Listado de ventas:")
        for venta in ventas:
            print("----------------------------------")
            print("Número de boleta:", venta.numero_boleta)  
            print("Empresa: Fantasías Prohibidas")
            print("Dirección: uliaca -Puno")
            print("Fecha:", venta.fecha)
            if isinstance(venta.cliente, dict):
                print("Cliente:", venta.cliente["nombres"], venta.cliente["apellidos"])
                print("DNI:", venta.cliente["dni"])
            else:
                print("Cliente:", venta.cliente.nombres, venta.cliente.apellidos)
                print("DNI:", venta.cliente.dni)
            print("===================================")
            print("Detalles:")
            for detalle in venta.detalles:
                print(detalle.convertir(), "Cantidad:", detalle.cantidad)
                print("Precio unitario:", detalle.precio)
                print("Precio total:", detalle.precio * detalle.cantidad)
            igv = venta.total * 0.18
            total_con_igv = venta.total + igv
            print("===================================")
            print("Total:", venta.total)
            print("IGV:", round(igv, 2))
            print("Total (con IGV):", round(total_con_igv, 2))
            print("----------------------------------")

def menu_text():
    print("============================================")
    print("====BIENVENIDO A NUESTRA TIENDA VIRTUAL=====")
    print("============================================")
    print("          FANTASIAS PROHIBIDAS.Sac\n            ")
    print("== \fAqui cumpliras todas tus fantasias\f == ")
    print("--------------------------------------------\n")
    print(" Seleccione alguna opcion segun su preferencia\n ")

    print("****\2 Menu para cliente \2****\n")
    print("1) para insertar datos de cliente: ")
    print("2) para lista de clientes: ")
    print("3) para buscar cliente: ")
    print("4) para editar datos de cliente: ")
    print("5) para eliminar datos de cliente:\n ")
    print("=======\3 Menu para producto \3======\n")
    print("6) para insertar producto: ")
    print("7) para la lista de clientes: ")
    print("8) para buscar producto: ")
    print("9) para editar los datos del producto: ")
    print("10) para eliminar producto:\n ")
    print("\3\3\3 \4 Menu boletas \4 \3\3\3\n")
    print("11) para realizar una venta: ")
    print("12) lista de boletas: ")
    
def menu():
    continuar:bool=True
    while continuar:
        opcion:str = input("seleccione la opcion: ")
        menu_text()
        match opcion:
            case "1":
                insertar_cliente()
            case "2":
                lista_clientes()
            case "3":
                buscar_cliente()
            case "4":
                editar_datos_cliente()
            case "5": 
                eliminar_cliente()
            case "6":
                insertar_producto()
            case "7":
                lista_productos()
            case "8":
                buscar_producto()
            case "9":
                editar_datos_producto()
            case "10":
                eliminar_producto()
            case "11":
                registrar_venta()
            case "12":
                lista_ventas()
            case "13":
                continuar=False
                print("el programa finalizo")

def main():
    print("Inicia el programa")
    print(" ¡ANTES QUE NADA INTRODUCE TU NOMBRE!\n ")
    nombre= input(" Introduce tu nombre: ")
    print("\n\v\v BIENVENIDO ", nombre, " Estamos muy felizes de su visita \v\v\n ")
    menu()
    return True

if __name__ == "__main__":
    main()