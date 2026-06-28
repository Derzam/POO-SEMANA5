# Módulo de servicio principal: gestiona productos y clientes del restaurante

# Importaciones de los modelos definidos en la carpeta modelos
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Administra las listas de productos y clientes registrados en el sistema."""

    def __init__(self, nombre: str, direccion: str) -> None:
        self.nombre: str = nombre
        self.direccion: str = direccion
        # Listas como tipo de dato compuesto para almacenar múltiples objetos
        self.productos: list = []
        self.clientes: list = []

    # ------------------------------------------------------------------ #
    # Métodos para gestionar productos                                     #
    # ------------------------------------------------------------------ #

    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un producto a la lista del restaurante."""
        self.productos.append(producto)

    def mostrar_productos(self) -> None:
        """Muestra todos los productos registrados en consola."""
        print(f"\n{'='*60}")
        print(f"  MENÚ DE PRODUCTOS — {self.nombre}")
        print(f"{'='*60}")
        if not self.productos:
            print("  No hay productos registrados.")
        for producto in self.productos:
            print(f"  • {producto}")
        print(f"{'='*60}")

    def buscar_producto(self, nombre: str) -> Producto | None:
        """Busca un producto por nombre y lo retorna si existe."""
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    # ------------------------------------------------------------------ #
    # Métodos para gestionar clientes                                      #
    # ------------------------------------------------------------------ #

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente en el sistema del restaurante."""
        self.clientes.append(cliente)

    def mostrar_clientes(self) -> None:
        """Muestra todos los clientes registrados en consola."""
        print(f"\n{'='*60}")
        print(f"  CLIENTES REGISTRADOS — {self.nombre}")
        print(f"{'='*60}")
        if not self.clientes:
            print("  No hay clientes registrados.")
        for cliente in self.clientes:
            print(f"  • {cliente}")
        print(f"{'='*60}")

    def __str__(self) -> str:
        return (
            f"Restaurante: {self.nombre} | Dirección: {self.direccion} | "
            f"Productos: {len(self.productos)} | Clientes: {len(self.clientes)}"
        )
