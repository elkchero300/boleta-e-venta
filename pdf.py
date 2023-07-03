from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf(datos_venta):
    # Crea un nuevo archivo PDF
    c = canvas.Canvas("venta.pdf", pagesize=letter)

    # Define el contenido del PDF
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "Datos de Venta:")

    # Imprime los datos de venta
    y = 700
    for key, value in datos_venta.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 20

    # Guarda y cierra el archivo PDF
    c.save()
    print("Archivo PDF generado correctamente.")

def lista_ventas():
    if len(ventas) == 0:
        print("No se han registrado ventas.")
    else:
        print("Listado de ventas:")
        for venta in ventas:
            print("----------------------------------")
            print("Número de boleta:", venta.numero_boleta)
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

            # Generar PDF de la venta
            datos_venta = {
                "Número de boleta": venta.numero_boleta,
                "Fecha": venta.fecha,
                "Cliente": venta.cliente.nombres + " " + venta.cliente.apellidos,
                "DNI": venta.cliente.dni,
                "Total": venta.total,
                "IGV": round(igv, 2),
                "Total (con IGV)": round(total_con_igv, 2)
            }
            generar_pdf(datos_venta)

            print("----------------------------------")

