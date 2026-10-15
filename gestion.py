import json
from datetime import datetime
from cliente import Cliente
from repartidor import Repartidor
from domicilio import Domicilio

def obtener_fecha_sistema():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def generar_id(coleccion, prefijo):
    mayor = 0
    for elem in coleccion:
        codigo = elem.obtener_id()
        numero = int(codigo[1:])
        if numero > mayor:
            mayor = numero
    siguiente = mayor + 1
    if siguiente < 10:
        return prefijo + "00" + str(siguiente)
    elif siguiente < 100:
        return prefijo + "0" + str(siguiente)
    else:
        return prefijo + str(siguiente)

def repartidor_esta_disponible(repartidor, domicilios):
    for d in domicilios:
        if d.obtener_repartidor().obtener_id() == repartidor.obtener_id() and d.obtener_estado() == "ACTIVO":
            return False
    return True

def buscar_cliente_por_id(clientes, id_cli):
    for c in clientes:
        if c.obtener_id() == id_cli:
            return c
    return None

def buscar_repartidor_por_id(repartidores, id_rep):
    for r in repartidores:
        if r.obtener_id() == id_rep:
            return r
    return None

def buscar_domicilio_por_id(domicilios, id_serv):
    for d in domicilios:
        if d.obtener_id() == id_serv:
            return d

def cliente_a_diccionario(cliente):
    return {
        "id_cliente": cliente.obtener_id(),
        "documento": cliente.obtener_documento(),
        "nombre": cliente.obtener_nombre(),
        "telefono": cliente.obtener_telefono(),
        "direccion": cliente.obtener_direccion()
    }

def repartidor_a_diccionario(repartidor):
    return {
        "id_repartidor": repartidor.obtener_id(),
        "documento": repartidor.obtener_documento(),
        "nombre": repartidor.obtener_nombre(),
        "telefono": repartidor.obtener_telefono(),
        "vehiculo": repartidor.obtener_vehiculo()
    }

def domicilio_a_diccionario(domicilio):
    return {
        "id_servicio": domicilio.obtener_id(),
        "id_cliente": domicilio.obtener_cliente().obtener_id(),
        "id_repartidor": domicilio.obtener_repartidor().obtener_id(),
        "descripcion": domicilio.obtener_descripcion(),
        "dir_recogida": domicilio.obtener_dir_recogida(),
        "dir_entrega": domicilio.obtener_dir_entrega(),
        "fecha_registro": domicilio.obtener_fecha_registro(),
        "fecha_cierre": domicilio.obtener_fecha_cierre(),
        "estado": domicilio.obtener_estado()
    }

def guardar_datos_json(clientes, repartidores, domicilios):
    lista_cli = []
    for c in clientes:
        lista_cli.append(cliente_a_diccionario(c))

    lista_rep = []
    for r in repartidores:
        lista_rep.append(repartidor_a_diccionario(r))

    lista_dom = []
    for d in domicilios:
        lista_dom.append(domicilio_a_diccionario(d))

    datos = {
        "clientes": lista_cli,
        "repartidores": lista_rep,
        "domicilios": lista_dom
    }

    with open("datos_mensajeria.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos_json(clientes, repartidores, domicilios):
    try:
        with open("datos_mensajeria.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        clientes.clear()
        repartidores.clear()
        domicilios.clear()

        for c_dict in datos["clientes"]:
            nuevo_c = Cliente(
                c_dict["id_cliente"],
                c_dict["documento"],
                c_dict["nombre"],
                c_dict["telefono"],
                c_dict["direccion"]
            )
            clientes.append(nuevo_c)

        for r_dict in datos["repartidores"]:
            nuevo_r = Repartidor(
                r_dict["id_repartidor"],
                r_dict["documento"],
                r_dict["nombre"],
                r_dict["telefono"],
                r_dict["vehiculo"]
            )
            repartidores.append(nuevo_r)

        for d_dict in datos["domicilios"]:
            cli = buscar_cliente_por_id(clientes, d_dict["id_cliente"])
            rep = buscar_repartidor_por_id(repartidores, d_dict["id_repartidor"])
            if cli is not None and rep is not None:
                nuevo_d = Domicilio(
                    d_dict["id_servicio"],
                    cli,
                    rep,
                    d_dict["descripcion"],
                    d_dict["dir_recogida"],
                    d_dict["dir_entrega"],
                    d_dict["fecha_registro"]
                )
                nuevo_d.restaurar_estado_json(d_dict["estado"], d_dict["fecha_cierre"])
                domicilios.append(nuevo_d)
    except FileNotFoundError:
        pass
    except Exception:
        print("Error: No se pudo leer el archivo JSON.")

def gestionar_registro_cliente(clientes, repartidores, domicilios, documento, nombre, telefono, direccion):
    if documento == "" or nombre == "" or direccion == "":
        return False, "Error: Datos incompletos."
    if len(telefono) < 7 or len(telefono) > 10 or not telefono.isdigit():
        return False, "Error: El telefono debe tener entre 7 y 10 digitos."
    for c in clientes:
        if c.obtener_documento() == documento:
            return False, "Error: El documento ya existe."

    id_cliente = generar_id(clientes, "C")
    nuevo_cliente = Cliente(id_cliente, documento, nombre, telefono, direccion)
    clientes.append(nuevo_cliente)
    guardar_datos_json(clientes, repartidores, domicilios)
    return True, "Cliente registrado con exito: " + id_cliente

def gestionar_actualizacion_cliente(clientes, repartidores, domicilios, id_cliente, nombre, telefono, direccion):
    cliente = buscar_cliente_por_id(clientes, id_cliente)
    if cliente is None:
        return False, "Error: Cliente no encontrado."
    if cliente.actualizar_datos(nombre, telefono, direccion):
        guardar_datos_json(clientes, repartidores, domicilios)
        return True, "Cliente actualizado con exito."
    return False, "Error: Datos invalidos. Se conserva el estado anterior."

def gestionar_eliminacion_cliente(clientes, repartidores, domicilios, id_cliente):
    cliente = buscar_cliente_por_id(clientes, id_cliente)
    if cliente is None:
        return False, "Error: Cliente no encontrado."
    for d in domicilios:
        if d.obtener_cliente().obtener_id() == id_cliente:
            return False, "Error: No se puede eliminar, tiene historial de domicilios."
    clientes.remove(cliente)
    guardar_datos_json(clientes, repartidores, domicilios)
    return True, "Cliente eliminado."

def gestionar_registro_repartidor(clientes, repartidores, domicilios, documento, nombre, telefono, vehiculo):
    if documento == "" or nombre == "":
        return False, "Error: Datos incompletos."
    if len(telefono) < 7 or len(telefono) > 10 or not telefono.isdigit():
        return False, "Error: El telefono debe tener entre 7 y 10 digitos."
    if vehiculo != "Moto" and vehiculo != "Bicicleta" and vehiculo != "Carro":
        return False, "Error: Tipo de vehiculo no valido."
    for r in repartidores:
        if r.obtener_documento() == documento:
            return False, "Error: El documento ya existe."

    id_repartidor = generar_id(repartidores, "R")
    nuevo_rep = Repartidor(id_repartidor, documento, nombre, telefono, vehiculo)
    repartidores.append(nuevo_rep)
    guardar_datos_json(clientes, repartidores, domicilios)
    return True, "Repartidor registrado con exito: " + id_repartidor

def gestionar_actualizacion_repartidor(clientes, repartidores, domicilios, id_repartidor, nombre, telefono, vehiculo):
    repartidor = buscar_repartidor_por_id(repartidores, id_repartidor)
    if repartidor is None:
        return False, "Error: Repartidor no encontrado."
    if repartidor.actualizar_datos(nombre, telefono, vehiculo):
        guardar_datos_json(clientes, repartidores, domicilios)
        return True, "Repartidor actualizado con exito."
    return False, "Error: Datos o vehiculo invalidos. Se conserva el estado anterior."

def gestionar_eliminacion_repartidor(clientes, repartidores, domicilios, id_repartidor):
    repartidor = buscar_repartidor_por_id(repartidores, id_repartidor)
    if repartidor is None:
        return False, "Error: Repartidor no encontrado."
    for d in domicilios:
        if d.obtener_repartidor().obtener_id() == id_repartidor:
            return False, "Error: No se puede eliminar, tiene servicios asociados."
    repartidores.remove(repartidor)
    guardar_datos_json(clientes, repartidores, domicilios)
    return True, "Repartidor eliminado."

def gestionar_registro_domicilio(clientes, repartidores, domicilios, id_cliente, id_repartidor, descripcion, dir_recogida, dir_entrega):
    cliente = buscar_cliente_por_id(clientes, id_cliente)
    if cliente is None:
        return False, "Error: El cliente no existe."
    repartidor = buscar_repartidor_por_id(repartidores, id_repartidor)
    if repartidor is None:
        return False, "Error: El repartidor no existe."
    if repartidor_esta_disponible(repartidor, domicilios) == False:
        return False, "Error: El repartidor ya tiene un servicio activo."
    if descripcion == "" or dir_recogida == "" or dir_entrega == "":
        return False, "Error: Campos obligatorios incompletos."

    id_servicio = generar_id(domicilios, "S")
    fecha_actual = obtener_fecha_sistema()
    nuevo_domicilio = Domicilio(id_servicio, cliente, repartidor, descripcion, dir_recogida, dir_entrega, fecha_actual)
    domicilios.append(nuevo_domicilio)
    guardar_datos_json(clientes, repartidores, domicilios)
    return True, "Domicilio registrado con estado ACTIVO: " + id_servicio

def gestionar_finalizar_domicilio(clientes, repartidores, domicilios, id_servicio):
    domicilio = buscar_domicilio_por_id(domicilios, id_servicio)
    if domicilio is None:
        return False, "Error: El domicilio no existe."
    if domicilio.obtener_estado() != "ACTIVO":
        return False, "Error: El servicio ya fue finalizado o cancelado."
    domicilio.finalizar(obtener_fecha_sistema())
    guardar_datos_json(clientes, repartidores, domicilios)
    return True, "Servicio finalizado exitosamente."

def gestionar_cancelar_domicilio(clientes, repartidores, domicilios, id_servicio):
    domicilio = buscar_domicilio_por_id(domicilios, id_servicio)
    if domicilio is None:
        return False, "Error: El domicilio no existe."
    if domicilio.obtener_estado() != "ACTIVO":
        return False, "Error: El servicio ya se encuentra cerrado."
    domicilio.cancelar(obtener_fecha_sistema())
    guardar_datos_json(clientes, repartidores, domicilios)
    return True, "Servicio cancelado exitosamente."