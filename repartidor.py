class Repartidor:
    def __init__(self, id_repartidor, documento, nombre, telefono, vehiculo):
        self.__id_repartidor = id_repartidor
        self.__documento = documento
        self.__nombre = nombre
        self.__telefono = telefono
        self.__vehiculo = vehiculo

    def obtener_id(self):
        return self.__id_repartidor

    def obtener_documento(self):
        return self.__documento

    def obtener_nombre(self):
        return self.__nombre

    def obtener_telefono(self):
        return self.__telefono

    def obtener_vehiculo(self):
        return self.__vehiculo

    def actualizar_datos(self, nom, tel, veh):
        if nom == "":
            return False
        if len(tel) < 7 or len(tel) > 10 or not tel.isdigit():
            return False
        if veh != "Moto" and veh != "Bicicleta" and veh != "Carro":
            return False
        self.__nombre = nom
        self.__telefono = tel
        self.__vehiculo = veh
        return True

    def obtener_informacion(self):
        return self.__id_repartidor + " - " + self.__documento + " - " + self.__nombre + " - Tel: " + self.__telefono + " - Vehiculo: " + self.__vehiculo