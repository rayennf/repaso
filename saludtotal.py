consultas = [
    {"id_consulta": 1, "fecha": "05/07/2025", "paciente": "Juan Pérez", "total": 0},
    {"id_consulta": 2, "fecha": "12/07/2025", "paciente": "Ana Torres", "total": 0},
    {"id_consulta": 3, "fecha": "01/08/2025", "paciente": "Carlos Soto", "total": 0},
]

detalle_consultas = [
    {"id_consulta": 1, "producto": "Radiografía", "cantidad": 1, "precio_unitario": 15000},
    {"id_consulta": 1, "producto": "Consulta general", "cantidad": 1, "precio_unitario": 10000},
    {"id_consulta": 2, "producto": "Examen de sangre", "cantidad": 1, "precio_unitario": 8000},
]

servicios_validos = [
    "Radiografía", "Consulta general", "Examen de sangre", 
    "Vacuna", "Ecografia", "Consulta psicológica"
]

def info_consulta(id_consulta):
    for cons in consultas:
        if cons["id_consulta"] == id_consulta:
            return cons
    return None

def muestrar_consulta(cons):
    if cons is None:
        print("La consulta no existe")
        return
    print("DATOS DE LA CONSULTA")
    print("==========================================================")
    print("ID       : ", cons["id_consulta"])
    print("Fecha    : ", cons["fecha"])
    print("Paciente : ", cons["paciente"])
    print("Total    : ", cons["total"])
    print("==========================================================")
    print("Servicio\tCantidad\tPrecio Unitario\tSubtotal")

    for det in detalle_consultas:
        if det["id_consulta"] == cons["id_consulta"]:
            subtotal = det["cantidad"] * det["precio_unitario"]
            print(f"{det['producto']}\t\t{det['cantidad']}\t\t{det['precio_unitario']}\t\t{subtotal}")

def actualiza_totales():
    for cons in consultas:
        total = 0
        for det in detalle_consultas:
            if det["id_consulta"] == cons["id_consulta"]:
                total += det["cantidad"] * det["precio_unitario"]
        cons["total"] = total
    print("Totales actualizados correctamente.")

def totales(mes, año):
    total = 0
    for cons in consultas:
        fecha = cons["fecha"].split("/")  # formato dd/mm/yyyy
        if int(fecha[1]) == mes and int(fecha[2]) == año:
            for det in detalle_consultas:
                if det["id_consulta"] == cons["id_consulta"]:
                    total += det["cantidad"] * det["precio_unitario"]
    print(f"\nEl total recaudado en el mes {mes:02}/{año} es: ${total}\n")

def agrega_servicio(id_consulta):
    cons = info_consulta(id_consulta)
    if cons is None:
        print("La consulta no existe")
        return

    while True:
        nom = input("Ingrese nombre del servicio que desea: ").capitalize()
        if nom in servicios_validos:
            break
        else:
            print("El servicio no es válido")

    while True:
        try:
            cant = int(input("Ingrese cantidad del servicio: "))
            break
        except:
            print("La cantidad debe ser un número entero.")

    while True:
        try:
            precio = int(input("Ingrese el precio unitario: "))
            break
        except:
            print("El precio debe ser un número entero.")

    detalle_consultas.append({
        "id_consulta": id_consulta,
        "producto": nom,
        "cantidad": cant,
        "precio_unitario": precio
    })

    print("Servicio agregado correctamente.\n")


# ========================
# Menú Principal
# ========================

while True:
    print("\nMENU PRINCIPAL - CLÍNICA SALUD TOTAL")
    print("==============================================")
    print("1.- Ver total recaudado en un mes y año")
    print("2.- Mostrar información completa de una consulta")
    print("3.- Agregar servicio a una consulta existente")
    print("4.- Actualizar los totales de todas las consultas")
    print("5.- Salir del sistema")
    
    opc = input("Ingrese la opción que desee: ")

    if opc == "1":
        mes = int(input("Ingrese el mes (número): "))
        año = int(input("Ingrese el año: "))
        totales(mes, año)

    elif opc == "2":
        id_consulta = int(input("Ingrese el ID de la consulta: "))
        c = info_consulta(id_consulta)
        muestrar_consulta(c)

    elif opc == "3":
        id_consulta = int(input("Ingrese el ID de la consulta a modificar: "))
        agrega_servicio(id_consulta)

    elif opc == "4":
        actualiza_totales()

    elif opc == "5":
        print("Gracias por atenderte con nosotros. Hasta pronto.")
        break

    else:
        print("Opción incorrecta. Intente de nuevo.")