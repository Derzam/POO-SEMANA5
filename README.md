# 🍽️ Sistema de Gestión de Restaurante — POO en Python
Nombre: Derly Alexander Zambrano Moreira

Proyecto académico desarrollado en Python aplicando **Programación Orientada a Objetos (POO)**.  
Modela un sistema básico para un restaurante con tres clases distribuidas en un proyecto modular.

---

## 📁 Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py       # Clase Producto
│   └── cliente.py        # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py    # Clase Restaurante (servicio principal)
└── main.py               # Punto de arranque del programa
```

---

## 🧩 Descripción de clases

### `Producto` — `modelos/producto.py`
Representa un plato, bebida o producto disponible en el restaurante.

| Atributo             | Tipo    | Descripción                          |
|----------------------|---------|--------------------------------------|
| `nombre`             | `str`   | Nombre del producto                  |
| `categoria`          | `str`   | Categoría (entrada, plato, bebida…)  |
| `precio`             | `float` | Precio unitario                      |
| `cantidad_disponible`| `int`   | Unidades en stock                    |
| `es_vegetariano`     | `bool`  | Indica si es apto para vegetarianos  |

**Métodos:** `actualizar_precio()`, `reducir_stock()`, `esta_disponible()`, `__str__()`

---

### `Cliente` — `modelos/cliente.py`
Representa una persona registrada en el sistema del restaurante.

| Atributo         | Tipo    | Descripción                          |
|------------------|---------|--------------------------------------|
| `nombre`         | `str`   | Nombre del cliente                   |
| `apellido`       | `str`   | Apellido del cliente                 |
| `telefono`       | `str`   | Número de contacto                   |
| `numero_mesa`    | `int`   | Mesa asignada                        |
| `tiene_reserva`  | `bool`  | Indica si tiene reserva previa       |
| `pedidos`        | `list`  | Lista de productos pedidos           |

**Métodos:** `agregar_pedido()`, `nombre_completo()`, `tiene_pedidos()`, `__str__()`

---

### `Restaurante` — `servicios/restaurante.py`
Servicio principal que administra listas de productos y clientes.

| Atributo    | Tipo   | Descripción                         |
|-------------|--------|-------------------------------------|
| `nombre`    | `str`  | Nombre del restaurante              |
| `direccion` | `str`  | Dirección física                    |
| `productos` | `list` | Lista de objetos `Producto`         |
| `clientes`  | `list` | Lista de objetos `Cliente`          |

**Métodos:** `agregar_producto()`, `mostrar_productos()`, `buscar_producto()`, `registrar_cliente()`, `mostrar_clientes()`, `__str__()`

##  Conceptos de POO Aplicados

| Concepto | Aplicación en el proyecto |
|---|---|
| **Clases y objetos** | `Producto`, `Cliente` y `Restaurante` son clases; sus instancias son los objetos del sistema |
| **Constructor `__init__()`** | Todas las clases inicializan sus atributos en el constructor |
| **Método `__str__()`** | Implementado en las 3 clases para representar objetos como texto |
| **Encapsulamiento** | Cada clase gestiona su propia información y expone métodos para operar sobre ella |
| **Composición** | `Restaurante` contiene listas de `Producto` y `Cliente`; `Cliente` contiene una lista de `Producto` |
| **Importaciones** | Los módulos se comunican mediante `from modelos.producto import Producto` |

---

## ▶️ Cómo ejecutar

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd restaurante_app

# Ejecutar el programa
python main.py
```

## 👨‍💻 Convenciones aplicadas

- **Clases:** `PascalCase` → `Producto`, `Cliente`, `Restaurante`
- **Variables, atributos y métodos:** `snake_case` → `cantidad_disponible`, `agregar_pedido`
- **Archivos y carpetas:** `snake_case` → `producto.py`, `restaurante.py`
