# Punto de arranque del programa — sistema de gestión de restaurante (POO)
# Importaciones desde los módulos del proyecto
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main() -> None:
    """Función principal: crea objetos, los agrega al servicio y muestra la información."""

    # ------------------------------------------------------------------ #
    # Crear el restaurante (servicio principal)                           #
    # ------------------------------------------------------------------ #
    restaurante = Restaurante(
        nombre="Manaba Grill",
        direccion="Locoa, Latacunga"
    )

    # ------------------------------------------------------------------ #
    # Crear al menos dos objetos de la clase Producto                     #
    # ------------------------------------------------------------------ #
    producto_1 = Producto(
        nombre="Sopa de Res",
        categoria="Entrada",
        precio=3.50,
        cantidad_disponible=20,
        es_vegetariano=False,
    )

    producto_2 = Producto(
        nombre="Llapingachos",
        categoria="Plato Fuerte",
        precio=5.00,
        cantidad_disponible=15,
        es_vegetariano=True,
    )

    producto_3 = Producto(
        nombre="Jugo de Naranja",
        categoria="Bebida",
        precio=1.50,
        cantidad_disponible=30,
        es_vegetariano=True,
    )

    # Agregar productos al servicio principal (lista de productos)
    restaurante.agregar_producto(producto_1)
    restaurante.agregar_producto(producto_2)
    restaurante.agregar_producto(producto_3)

    # ------------------------------------------------------------------ #
    # Crear al menos dos objetos de la clase Cliente                      #
    # ------------------------------------------------------------------ #
    cliente_1 = Cliente(
        nombre="María",
        apellido="González",
        telefono="0991234567",
        numero_mesa=3,
        tiene_reserva=True,
    )

    cliente_2 = Cliente(
        nombre="Carlos",
        apellido="Pereira",
        telefono="0987654321",
        numero_mesa=7,
        tiene_reserva=False,
    )

    # Registrar pedidos en los clientes y reducir stock
    cliente_1.agregar_pedido("Sopa de Res")
    cliente_1.agregar_pedido("Jugo de Naranja")
    producto_1.reducir_stock(1)
    producto_3.reducir_stock(1)

    cliente_2.agregar_pedido("Llapingachos")
    cliente_2.agregar_pedido("Jugo de Naranja")
    producto_2.reducir_stock(1)
    producto_3.reducir_stock(1)

    # Agregar clientes al servicio principal (lista de clientes)
    restaurante.registrar_cliente(cliente_1)
    restaurante.registrar_cliente(cliente_2)

    # ------------------------------------------------------------------ #
    # Mostrar información registrada de forma organizada en consola       #
    # ------------------------------------------------------------------ #
    print("\n" + "="*60)
    print(f"  SISTEMA DE GESTIÓN — {restaurante.nombre.upper()}")
    print("="*60)
    print(f"  {restaurante}")

    # Mostrar productos del menú
    restaurante.mostrar_productos()

    # Mostrar clientes registrados
    restaurante.mostrar_clientes()

    # Demostración de métodos adicionales
    print("\n--- Verificaciones adicionales ---")
    print(f"  ¿'Sopa de Res' disponible? {producto_1.esta_disponible()}")
    print(f"  ¿'{cliente_1.nombre_completo()}' tiene pedidos? {cliente_1.tiene_pedidos()}")

    producto_buscado = restaurante.buscar_producto("Llapingachos")
    if producto_buscado:
        print(f"  Producto encontrado → {producto_buscado}")


# Punto de entrada estándar de Python
if __name__ == "__main__":
    main()
