# ============================
# Clase TRABAJADORES
# ============================
class Trabajador:
    def _init_(self, id_trabajador, nombre, cargo, fecha_nacimiento):
        self.id_trabajador = id_trabajador
        self.nombre = nombre
        self.cargo = cargo
        self.fecha_nacimiento = fecha_nacimiento

    def info_trabajador(self):
        return f"ID: {self.id_trabajador}, Nombre: {self.nombre}, Cargo: {self.cargo}, Fecha Nac: {self.fecha_nacimiento}"


# ============================
# Clase CLIENTES
# ============================
class Cliente:
    def _init_(self, id_cliente, nombre, genero, fecha_nacimiento):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento

    def info_cliente(self):
        return f"ID: {self.id_cliente}, Nombre: {self.nombre}, Género: {self.genero}, Fecha Nac: {self.fecha_nacimiento}"


# ============================
# Clase SERVICIOS
# ============================
class Servicio:
    def _init_(self, id_servicio, nombre_servicio, trabajador: Trabajador):
        self.id_servicio = id_servicio
        self.nombre_servicio = nombre_servicio
        self.trabajador = trabajador  # relación con Trabajador

    def info_servicio(self):
        return f"ID Servicio: {self.id_servicio}, Nombre: {self.nombre_servicio}, Atendido por: {self.trabajador.nombre}"


# ============================
# Clase PRODUCTOS
# ============================
class Producto:
    def _init_(self, id_producto, nombre_producto, precio, contenido):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.contenido = contenido

    def info_producto(self):
        return f"ID Producto: {self.id_producto}, Nombre: {self.nombre_producto}, Precio: ${self.precio}, Contenido: {self.contenido}"
    