class Cliente:
    def __init__(self, id_cliente, documento, nombre, telefono, direccion):
        self.__id_cliente = id_cliente
        self.__documento = documento
        self.__nombre = nombre
        self.__telefono = telefono
        self.__direccion = direccion

    def obtener_id(self):
        return self.__id_cliente

    def obtener_documento(self):
        return self.__documento

    def obtener_nombre(self):
        return self.__nombre

    def obtener_telefono(self):
        return self.__telefono

    def obtener_direccion(self):
        return self.__direccion

    def actualizar_datos(self, nom, tel, dir):
        if nom == "" or dir == "":
            return False
        if len(tel) < 7 or len(tel) > 10 or not tel.isdigit():
            return False
        self.__nombre = nom
        self.__telefono = tel
        self.__direccion = dir
        return True

    def obtener_informacion(self):
        return self.__id_cliente + " - " + self.__documento + " - " + self.__nombre + " - Tel: " + self.__telefono + " - Dir: " + self.__direccion