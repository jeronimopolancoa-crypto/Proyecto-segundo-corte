import tkinter as tk
from gestion import (
    repartidor_esta_disponible,
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

clientes = []
repartidores = []
domicilios = []

cargar_datos_json(clientes, repartidores, domicilios)

ventana = tk.Tk()
ventana.title("QuickDrop Logistics - Sistema de Gestión")
ventana.geometry("940x620")

frame_principal = tk.Frame(ventana, padx=15, pady=10)
frame_principal.pack(fill=tk.BOTH, expand=True)
frame_izq = tk.Frame(frame_principal)
frame_izq.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))

tk.Label(frame_izq, text="Panel de entrada", font=("Arial", 11, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 6))

tk.Label(frame_izq, text="ID (para actualizar/eliminar):").grid(row=1, column=0, sticky="w", pady=2)
entry_id_persona = tk.Entry(frame_izq, width=15)
entry_id_persona.grid(row=1, column=1, pady=2, sticky="w")

tk.Label(frame_izq, text="documento:").grid(row=2, column=0, sticky="w", pady=2)
entry_doc = tk.Entry(frame_izq, width=28)
entry_doc.grid(row=2, column=1, pady=2, sticky="w")

tk.Label(frame_izq, text="nombre:").grid(row=3, column=0, sticky="w", pady=2)
entry_nom = tk.Entry(frame_izq, width=28)
entry_nom.grid(row=3, column=1, pady=2, sticky="w")

tk.Label(frame_izq, text="teléfono:").grid(row=4, column=0, sticky="w", pady=2)
entry_tel = tk.Entry(frame_izq, width=28)
entry_tel.grid(row=4, column=1, pady=2, sticky="w")

tk.Label(frame_izq, text="dirección / vehículo:").grid(row=5, column=0, sticky="w", pady=2)
entry_dir_veh = tk.Entry(frame_izq, width=28)
entry_dir_veh.grid(row=5, column=1, pady=2, sticky="w")

frame_btns_personas = tk.Frame(frame_izq)
frame_btns_personas.grid(row=6, column=0, columnspan=2, pady=4, sticky="w")

frame_btns_crud = tk.Frame(frame_izq)
frame_btns_crud.grid(row=7, column=0, columnspan=2, pady=2, sticky="w")

frame_ids = tk.Frame(frame_izq)
frame_ids.grid(row=8, column=0, columnspan=2, sticky="w", pady=(8, 2))
tk.Label(frame_ids, text="Id cliente:").pack(side=tk.LEFT)
entry_id_cliente = tk.Entry(frame_ids, width=8)
entry_id_cliente.pack(side=tk.LEFT, padx=(5, 15))
tk.Label(frame_ids, text="Id repartidor:").pack(side=tk.LEFT)
entry_id_repartidor = tk.Entry(frame_ids, width=8)
entry_id_repartidor.pack(side=tk.LEFT, padx=5)

tk.Label(frame_izq, text="Descripción:").grid(row=9, column=0, sticky="w", pady=2)
entry_descripcion = tk.Entry(frame_izq, width=28)
entry_descripcion.grid(row=9, column=1, pady=2, sticky="w")

tk.Label(frame_izq, text="Dir. recogida:").grid(row=10, column=0, sticky="w", pady=2)
entry_recogida = tk.Entry(frame_izq, width=28)
entry_recogida.grid(row=10, column=1, pady=2, sticky="w")

tk.Label(frame_izq, text="Dir. entrega:").grid(row=11, column=0, sticky="w", pady=2)
entry_entrega = tk.Entry(frame_izq, width=28)
entry_entrega.grid(row=11, column=1, pady=2, sticky="w")

frame_cierre = tk.Frame(frame_izq)
frame_cierre.grid(row=13, column=0, columnspan=2, sticky="w", pady=(8, 2))
tk.Label(frame_cierre, text="ID servicio:").pack(side=tk.LEFT)
entry_id_servicio = tk.Entry(frame_cierre, width=12)
entry_id_servicio.pack(side=tk.LEFT, padx=10)

frame_btns_cierre = tk.Frame(frame_izq)
frame_btns_cierre.grid(row=14, column=0, columnspan=2, sticky="w", pady=6)
frame_der = tk.Frame(frame_principal)
frame_der.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(frame_der, text="LISTA DE RESULTADOS", font=("Arial", 11, "bold")).pack(anchor="w", pady=(0, 10))

listbox_resultados = tk.Listbox(frame_der, width=54, height=16)
listbox_resultados.pack(fill=tk.BOTH, expand=True)

frame_consultas_1 = tk.Frame(frame_der)
frame_consultas_1.pack(fill=tk.X, pady=(10, 4))

frame_consultas_2 = tk.Frame(frame_der)
frame_consultas_2.pack(fill=tk.X, pady=4)
lbl_estado = tk.Label(
    ventana,
    text="Sistema iniciado",
    bd=1,
    relief=tk.SUNKEN,
    anchor="w",
    padx=10,
    pady=6
)
lbl_estado.pack(side=tk.BOTTOM, fill=tk.X)
def mostrar_mensaje(texto, es_error=False):
    color = "red" if es_error else "green"
    lbl_estado.config(text=texto, fg=color)

def mostrar_clientes_gui():
    listbox_resultados.delete(0, tk.END)
    if len(clientes) == 0:
        listbox_resultados.insert(tk.END, "No hay elementos registrados.")
    for c in clientes:
        listbox_resultados.insert(tk.END, c.obtener_informacion())

def mostrar_repartidores_gui():
    listbox_resultados.delete(0, tk.END)
    if len(repartidores) == 0:
        listbox_resultados.insert(tk.END, "No hay elementos registrados.")
    for r in repartidores:
        if repartidor_esta_disponible(r, domicilios):
            disp = "[Disponible]"
        else:
            disp = "[Ocupado]"
        listbox_resultados.insert(tk.END, r.obtener_informacion() + " " + disp)

def mostrar_domicilios_gui():
    listbox_resultados.delete(0, tk.END)
    if len(domicilios) == 0:
        listbox_resultados.insert(tk.END, "No hay elementos registrados.")
    for d in domicilios:
        listbox_resultados.insert(tk.END, d.obtener_informacion())

def registrar_cliente_gui():
    ok, msg = gestionar_registro_cliente(
        clientes, repartidores, domicilios,
        entry_doc.get().strip(), entry_nom.get().strip(),
        entry_tel.get().strip(), entry_dir_veh.get().strip()
    )
    mostrar_mensaje(msg, es_error=not ok)
    if ok:
        mostrar_clientes_gui()

def registrar_repartidor_gui():
    ok, msg = gestionar_registro_repartidor(
        clientes, repartidores, domicilios,
        entry_doc.get().strip(), entry_nom.get().strip(),
        entry_tel.get().strip(), entry_dir_veh.get().strip()
    )
    mostrar_mensaje(msg, es_error=not ok)
    if ok:
        mostrar_repartidores_gui()

def actualizar_cliente_gui():
    ok, msg = gestionar_actualizacion_cliente(
        clientes, repartidores, domicilios,
        entry_id_persona.get().strip(), entry_nom.get().strip(),
        entry_tel.get().strip(), entry_dir_veh.get().strip()
    )
    mostrar_mensaje(msg, es_error=not ok)
    if ok:
        mostrar_clientes_gui()

def actualizar_repartidor_gui():
    ok, msg = gestionar_actualizacion_repartidor(
        clientes, repartidores, domicilios,
        entry_id_persona.get().strip(), entry_nom.get().strip(),
        entry_tel.get().strip(), entry_dir_veh.get().strip()
    )
    mostrar_mensaje(msg, es_error=not ok)
    if ok:
        mostrar_repartidores_gui()

def eliminar_cliente_gui():
    ok, msg = gestionar_eliminacion_cliente(
        clientes, repartidores, domicilios, entry_id_persona.get().strip()
    )
    mostrar_mensaje(msg, es_error=not ok)
    if ok:
        mostrar_clientes_gui()

def eliminar_repartidor_gui():
    ok, msg = gestionar_eliminacion_repartidor(
        clientes, repartidores, domicilios, entry_id_persona.get().strip()
    )
    mostrar_mensaje(msg, es_error=not ok)
    if ok:
        mostrar_repartidores_gui()

def despachar_domicilio_gui():
    ok, msg = gestionar_registro_domicilio(
        clientes, repartidores, domicilios,
        entry_id_cliente.get().strip(), entry_id_repartidor.get().strip(),
        entry_descripcion.get().strip(), entry_recogida.get().strip(), entry_entrega.get().strip()
    )
    mostrar_mensaje(msg, es_error=not ok)
    if ok:
        mostrar_domicilios_gui()

def finalizar_servicio_gui():
    ok, msg = gestionar_finalizar_domicilio(
        clientes, repartidores, domicilios, entry_id_servicio.get().strip()
    )
    mostrar_mensaje(msg, es_error=not ok)
    if ok:
        mostrar_domicilios_gui()

def cancelar_servicio_gui():
    ok, msg = gestionar_cancelar_domicilio(
        clientes, repartidores, domicilios, entry_id_servicio.get().strip()
    )
    mostrar_mensaje(msg, es_error=not ok)
    if ok:
        mostrar_domicilios_gui()

def guardar_gui():
    guardar_datos_json(clientes, repartidores, domicilios)
    mostrar_mensaje("Datos guardados en datos_mensajeria.json")


tk.Button(frame_btns_personas, text="registrar cliente", command=registrar_cliente_gui).pack(side=tk.LEFT, padx=(0, 8))
tk.Button(frame_btns_personas, text="registrar repartidor", command=registrar_repartidor_gui).pack(side=tk.LEFT)

tk.Button(frame_btns_crud, text="actualizar cli", command=actualizar_cliente_gui).pack(side=tk.LEFT, padx=(0, 4))
tk.Button(frame_btns_crud, text="actualizar rep", command=actualizar_repartidor_gui).pack(side=tk.LEFT, padx=(0, 4))
tk.Button(frame_btns_crud, text="eliminar cli", command=eliminar_cliente_gui).pack(side=tk.LEFT, padx=(0, 4))
tk.Button(frame_btns_crud, text="eliminar rep", command=eliminar_repartidor_gui).pack(side=tk.LEFT)

tk.Button(frame_izq, text="Despachar domicilio (ACTIVO)", bg="#e1e1e1", command=despachar_domicilio_gui).grid(row=12, column=0, columnspan=2, pady=6, sticky="w")

tk.Button(frame_btns_cierre, text="finalizar servicio", command=finalizar_servicio_gui).pack(side=tk.LEFT, padx=(0, 10))
tk.Button(frame_btns_cierre, text="cancelar servicio", command=cancelar_servicio_gui).pack(side=tk.LEFT)

tk.Button(frame_consultas_1, text="Mostrar clientes", width=18, command=mostrar_clientes_gui).pack(side=tk.LEFT, padx=(0, 10))
tk.Button(frame_consultas_1, text="Mostrar repart", width=18, command=mostrar_repartidores_gui).pack(side=tk.LEFT)

tk.Button(frame_consultas_2, text="Ver historial de domicilios", width=22, command=mostrar_domicilios_gui).pack(side=tk.LEFT, padx=(0, 10))
tk.Button(frame_consultas_2, text="guardar", width=12, command=guardar_gui).pack(side=tk.LEFT)

mostrar_clientes_gui()

ventana.mainloop()
