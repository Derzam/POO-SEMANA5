# Módulo que define la clase Producto para el sistema de restaurante


class Producto:
    """Representa un plato, bebida o producto disponible en el restaurante."""

    def __init__(self, nombre: str, categoria: str, precio: float, cantidad_disponible: int, es_vegetariano: bool):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.es_vegetariano = es_vegetariano

    def actualizar_precio(self, nuevo_precio: float):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio

    def reducir_stock(self, cantidad: int):
        """Reduce la cantidad disponible al realizarse un pedido."""
        if cantidad <= self.cantidad_disponible:
            self.cantidad_disponible -= cantidad
        else:
            print(f"  Stock insuficiente para '{self.nombre}'.")

    def esta_disponible(self) -> bool:
        """Retorna True si el producto tiene stock mayor a cero."""
        return self.cantidad_disponible > 0

    def __str__(self) -> str:
        vegetariano = "Sí" if self.es_vegetariano else "No"
        return (
            f"Producto: {self.nombre} | Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | Stock: {self.cantidad_disponible} | "
            f"Vegetariano: {vegetariano}"
        )
