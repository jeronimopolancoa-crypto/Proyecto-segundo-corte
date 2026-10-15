class Domicilio:
    def __init__(self, id_servicio, cliente, repartidor, descripcion, dir_recogida, dir_entrega, fecha_registro):
        self.__id_servicio = id_servicio
        self.__cliente = cliente
        self.__repartidor = repartidor
        self.__descripcion = descripcion
        self.__dir_recogida = dir_recogida
        self.__dir_entrega = dir_entrega
        self.__fecha_registro = fecha_registro
        self.__fecha_cierre = None
        self.__estado = "ACTIVO"

    def obtener_id(self):
        return self.__id_servicio

    def obtener_cliente(self):
        return self.__cliente

    def obtener_repartidor(self):
        return self.__repartidor

    def obtener_descripcion(self):
        return self.__descripcion

    def obtener_dir_recogida(self):
        return self.__dir_recogida

    def obtener_dir_entrega(self):
        return self.__dir_entrega

    def obtener_fecha_registro(self):
        return self.__fecha_registro

    def obtener_fecha_cierre(self):
        return self.__fecha_cierre

    def obtener_estado(self):
        return self.__estado

    def finalizar(self, fecha_cierre):
        if self.__estado == "ACTIVO":
            self.__estado = "FINALIZADO"
            self.__fecha_cierre = fecha_cierre
            return True
        return False

    def cancelar(self, fecha_cierre):
        if self.__estado == "ACTIVO":
            self.__estado = "CANCELADO"
            self.__fecha_cierre = fecha_cierre
            return True
        return False

    def restaurar_estado_json(self, estado, fecha_cierre):
        self.__estado = estado
        self.__fecha_cierre = fecha_cierre

    def obtener_informacion(self):
        info = self.__id_servicio + " - " + self.__cliente.obtener_nombre() + " -> " + self.__repartidor.obtener_nombre() + " [" + self.__estado + "]"
        info = info + " | Paquete: " + self.__descripcion + " | Recogida: " + self.__dir_recogida + " | Entrega: " + self.__dir_entrega
        info = info + " | Registro: " + self.__fecha_registro
        if self.__fecha_cierre is not None:
            info = info + " | Cierre: " + str(self.__fecha_cierre)
        return info