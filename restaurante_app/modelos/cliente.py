# Módulo que define la clase Cliente para el sistema de restaurante


class Cliente:
    """Representa una persona registrada en el sistema del restaurante."""

    def __init__(self, nombre: str, apellido: str, telefono: str, numero_mesa: int, tiene_reserva: bool) -> None:
        # Atributos con tipos de datos básicos: str, int, bool
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.numero_mesa = numero_mesa
        self.tiene_reserva = tiene_reserva
        # Lista como tipo de dato compuesto: historial de pedidos del cliente
        self.pedidos: list = []

    def agregar_pedido(self, nombre_producto: str) -> None:
        """Agrega un producto al historial de pedidos del cliente."""
        self.pedidos.append(nombre_producto)

    def nombre_completo(self) -> str:
        """Retorna el nombre completo del cliente."""
        return f"{self.nombre} {self.apellido}"

    def tiene_pedidos(self) -> bool:
        """Retorna True si el cliente tiene al menos un pedido registrado."""
        return len(self.pedidos) > 0

    def __str__(self) -> str:
        reserva = "Sí" if self.tiene_reserva else "No"
        pedidos_str = ", ".join(self.pedidos) if self.pedidos else "Ninguno"
        return (
            f"Cliente: {self.nombre_completo()} | Tel: {self.telefono} | "
            f"Mesa: {self.numero_mesa} | Reserva: {reserva} | "
            f"Pedidos: {pedidos_str}"
        )
