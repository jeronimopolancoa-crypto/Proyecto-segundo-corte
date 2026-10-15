from gestion import (
    repartidor_esta_disponible,
    buscar_cliente_por_id,
    buscar_repartidor_por_id,
    buscar_domicilio_por_id,
    guardar_datos_json,
    cargar_datos_json,
    gestionar_registro_cliente,
    gestionar_actualizacion_cliente,
    gestionar_eliminacion_cliente,
    gestionar_registro_repartidor,
    gestionar_actualizacion_repartidor,
    gestionar_eliminacion_repartidor,
    gestionar_registro_domicilio,
    gestionar_finalizar_domicilio,
    gestionar_cancelar_domicilio
)

def consultar_clientes(clientes):
    if len(clientes) == 0:
        print("No hay elementos registrados.")
        return
    for c in clientes:
        print(c.obtener_informacion())

def consultar_repartidores(repartidores, domicilios):
    if len(repartidores) == 0:
        print("No hay elementos registrados.")
        return
    for r in repartidores:
        if repartidor_esta_disponible(r, domicilios):
            estado = "[Disponible]"
        else:
            estado = "[Ocupado]"
        print(r.obtener_informacion() + " " + estado)

def consultar_domicilio(domicilios):
    if len(domicilios) == 0:
        print("No hay elementos registrados.")
        return
    id_serv = input("Ingrese el codigo del domicilio (o Enter para mostrar todos): ").strip()
    if id_serv == "":
        for d in domicilios:
            print(d.obtener_informacion())
    else:
        domicilio = buscar_domicilio_por_id(domicilios, id_serv)
        if domicilio is None:
            print("Error: El domicilio no existe.")
        else:
            print(domicilio.obtener_informacion())

def registrar_cliente(clientes, repartidores, domicilios):
    doc = input("Documento: ").strip()
    nom = input("Nombre: ").strip()
    tel = input("Telefono: ").strip()
    dir_c = input("Direccion: ").strip()
    _, msg = gestionar_registro_cliente(clientes, repartidores, domicilios, doc, nom, tel, dir_c)
    print(msg)

def registrar_repartidor(repartidores, clientes, domicilios):
    doc = input("Documento: ").strip()
    nom = input("Nombre: ").strip()
    tel = input("Telefono: ").strip()
    veh = input("Vehiculo (Moto, Bicicleta, Carro): ").strip()
    _, msg = gestionar_registro_repartidor(clientes, repartidores, domicilios, doc, nom, tel, veh)
    print(msg)

def registrar_domicilio(clientes, repartidores, domicilios):
    id_c = input("ID del cliente: ").strip()
    id_r = input("ID del repartidor: ").strip()
    desc = input("Descripcion del paquete: ").strip()
    rec = input("Direccion de recogida: ").strip()
    ent = input("Direccion de entrega: ").strip()
    _, msg = gestionar_registro_domicilio(clientes, repartidores, domicilios, id_c, id_r, desc, rec, ent)
    print(msg)

def finalizar_domicilio(domicilios, clientes, repartidores):
    id_s = input("ID del servicio: ").strip()
    _, msg = gestionar_finalizar_domicilio(clientes, repartidores, domicilios, id_s)
    print(msg)

def cancelar_domicilio(domicilios, clientes, repartidores):
    id_s = input("ID del servicio: ").strip()
    _, msg = gestionar_cancelar_domicilio(clientes, repartidores, domicilios, id_s)
    print(msg)

def eliminar_cliente(clientes, domicilios, repartidores):
    id_c = input("ID del cliente: ").strip()
    if buscar_cliente_por_id(clientes, id_c) is None:
        print("Error: Cliente no encontrado.")
        return
    conf = input("Confirma eliminacion (s/n): ").strip().lower()
    if conf == "s":
        _, msg = gestionar_eliminacion_cliente(clientes, repartidores, domicilios, id_c)
        print(msg)
    else:
        print("Operacion cancelada.")

def eliminar_repartidor(repartidores, domicilios, clientes):
    id_r = input("ID del repartidor: ").strip()
    if buscar_repartidor_por_id(repartidores, id_r) is None:
        print("Error: Repartidor no encontrado.")
        return
    conf = input("Confirma eliminacion (s/n): ").strip().lower()
    if conf == "s":
        _, msg = gestionar_eliminacion_repartidor(clientes, repartidores, domicilios, id_r)
        print(msg)
    else:
        print("Operacion cancelada.")

def actualizar_cliente(clientes, repartidores, domicilios):
    id_c = input("ID del cliente a actualizar: ").strip()
    nom = input("Nuevo nombre: ").strip()
    tel = input("Nuevo telefono: ").strip()
    dir_c = input("Nueva direccion: ").strip()
    _, msg = gestionar_actualizacion_cliente(clientes, repartidores, domicilios, id_c, nom, tel, dir_c)
    print(msg)

def actualizar_repartidor(clientes, repartidores, domicilios):
    id_r = input("ID del repartidor a actualizar: ").strip()
    nom = input("Nuevo nombre: ").strip()
    tel = input("Nuevo telefono: ").strip()
    veh = input("Nuevo vehiculo (Moto, Bicicleta, Carro): ").strip()
    _, msg = gestionar_actualizacion_repartidor(clientes, repartidores, domicilios, id_r, nom, tel, veh)
    print(msg)

def main():
    clientes = []
    repartidores = []
    domicilios = []
    cargar_datos_json(clientes, repartidores, domicilios)

    opcion = ""
    while opcion != "0":
        print("\nQuickDrop Logistics")
        print("1. Mostrar clientes")
        print("2. Mostrar repartidores")
        print("3. Registrar cliente")
        print("4. Registrar repartidor")
        print("5. Registrar domicilio")
        print("6. Consultar domicilio")
        print("7. Finalizar domicilio")
        print("8. Cancelar domicilio")
        print("9. Eliminar cliente")
        print("10. Eliminar repartidor")
        print("11. Actualizar cliente")
        print("12. Actualizar repartidor")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            consultar_clientes(clientes)
        elif opcion == "2":
            consultar_repartidores(repartidores, domicilios)
        elif opcion == "3":
            registrar_cliente(clientes, repartidores, domicilios)
        elif opcion == "4":
            registrar_repartidor(repartidores, clientes, domicilios)
        elif opcion == "5":
            registrar_domicilio(clientes, repartidores, domicilios)
        elif opcion == "6":
            consultar_domicilio(domicilios)
        elif opcion == "7":
            finalizar_domicilio(domicilios, clientes, repartidores)
        elif opcion == "8":
            cancelar_domicilio(domicilios, clientes, repartidores)
        elif opcion == "9":
            eliminar_cliente(clientes, domicilios, repartidores)
        elif opcion == "10":
            eliminar_repartidor(repartidores, domicilios, clientes)
        elif opcion == "11":
            actualizar_cliente(clientes, repartidores, domicilios)
        elif opcion == "12":
            actualizar_repartidor(clientes, repartidores, domicilios)
        elif opcion == "0":
            guardar_datos_json(clientes, repartidores, domicilios)
            print("Programa finalizado.")
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()