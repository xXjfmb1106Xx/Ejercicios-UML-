# ============================
# Clase PRODUCTOS
# ============================
class Producto:
    def _init_(self, id_producto, nombre_producto, precio, contenido):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.contenido = contenido

    # Método polimórfico
    def info(self):
        return f"[PRODUCTO] ID: {self.id_producto}, Nombre: {self.nombre_producto}, Precio: ${self.precio}"


# ============================
# PROBANDO EL POLIMORFISMO
# ============================

if _name_ == "_main_":
    # Crear objetos
    trabajador1 = Trabajador(1, "Ana Gómez", "Vendedora", "1990-05-14")
    cliente1 = Cliente(101, "Carlos López", "M", "1995-07-21")
    servicio1 = Servicio(201, "Reparación técnica", trabajador1)
    producto1 = Producto(301, "Laptop", 2500.0, "16GB RAM, 512GB SSD")

    # Lista polimórfica
    objetos = [trabajador1, cliente1, servicio1, producto1]

    print("=== DEMOSTRACIÓN DE POLIMORFISMO ===")
    for obj in objetos:
        print(obj.info())  # Llama al método info() de cada clase según corresponda