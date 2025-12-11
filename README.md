# Gestor PyME 🏪

Un sistema de gestión integral diseñado para pequeñas y medianas empresas (PyMEs). Incluye módulos de punto de venta, inventario, gestión de proveedores y análisis de ventas.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [API Endpoints](#api-endpoints)
- [Tecnologías](#tecnologías)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## ✨ Características

### 🛒 Punto de Venta (POS)
- **Escáner de Códigos QR/Códigos de Barras**: Integración con tecnología de escaneo web usando html5-qrcode
- **Búsqueda Dinámica**: Búsqueda en tiempo real de productos por nombre o código
- **Carrito de Compras**: Gestión interactiva del carrito con cálculo automático de totales
- **Feedback Audiovisual**: Sonido de confirmación en escaneos exitosos

### 📊 Gestión de Inventario
- **Control de Productos**: Crear, editar y eliminar productos
- **Categorización**: Organizar productos por categorías
- **Alertas de Stock**: Notificaciones automáticas de productos con stock bajo
- **Códigos de Producto**: Identificación única con códigos de barras

### 🤝 Gestión de Proveedores
- **Base de Datos de Proveedores**: Registro completo de proveedores
- **Información de Contacto**: Teléfono, email y dirección
- **Categorías de Proveedores**: Clasificación por tipo de suministro
- **Historial de Transacciones**: Registro de compras y transacciones

### 📈 Análisis y Reportes
- **Dashboard en Tiempo Real**: Visualización de métricas principales
  - Total de ventas del día
  - Cantidad de productos en inventario
  - Productos con stock bajo
  - Total de proveedores registrados
- **Historial de Ventas**: Registro completo de todas las transacciones
- **Cancelación de Ventas**: Anulación de ventas con devolución automática de stock

## 🔧 Requisitos Previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- SQLite3 (incluido en Python)
- Navegador moderno con soporte para:
  - ES6 JavaScript
  - Web Audio API
  - Geolocalización (para acceso a cámara)

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Ferxxo-sar/gestor-pyme.git
cd gestor-pyme
```

### 2. Crear y activar entorno virtual

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si no existe `requirements.txt`, instala manualmente:
```bash
pip install django==5.2.7
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (administrador)

```bash
python manage.py createsuperuser
```

Sigue las indicaciones para crear tu cuenta de administrador.

### 6. Recolectar archivos estáticos

```bash
python manage.py collectstatic --noinput
```

## ⚙️ Configuración

### Variables de Entorno (Producción)

Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,tudominio.com
DATABASE_URL=sqlite:///db.sqlite3
```

### Archivo settings.py

Para desarrollo, el archivo `config/settings.py` ya está configurado. Para producción, actualiza:

```python
DEBUG = False
ALLOWED_HOSTS = ['tudominio.com', 'www.tudominio.com']
SECRET_KEY = 'usa-una-clave-segura-aleatorias'
```

## 🚀 Uso

### Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

El sitio estará disponible en `http://127.0.0.1:8000/`

### Acceder al Panel de Administración

1. Navega a `http://127.0.0.1:8000/admin/`
2. Inicia sesión con las credenciales de superusuario
3. Gestiona productos, proveedores y visualiza datos

### Usar el Punto de Venta

1. Desde la página principal, ve a "Nueva Venta"
2. **Opción 1 - Escanear Código**: Haz clic en "Escanear Código" y apunta tu cámara al código QR/barras
3. **Opción 2 - Búsqueda Manual**: Usa la barra de búsqueda para encontrar productos por nombre o código
4. Ajusta cantidades en el carrito
5. Confirma la venta
6. Visualiza el historial en "Historial de Ventas"

### Gestionar Productos

1. Ve a "Productos"
2. Haz clic en "Nuevo Producto"
3. Completa los datos (nombre, código, precio, stock, categoría)
4. Guarda los cambios

### Gestionar Proveedores

1. Ve a "Proveedores"
2. Crea nuevos proveedores con información de contacto
3. Asigna categorías de proveedor
4. Visualiza el listado completo

## 📁 Estructura del Proyecto

```
gestor_pyme/
├── config/                 # Configuración principal de Django
│   ├── settings.py        # Configuración del proyecto
│   ├── urls.py            # Rutas principales
│   ├── asgi.py            # Configuración ASGI
│   └── wsgi.py            # Configuración WSGI
├── core/                   # Aplicación principal (Dashboard)
│   ├── models.py
│   ├── views.py           # Vista del dashboard
│   ├── urls.py
│   └── templates/
│       └── core/
│           └── index.html # Página principal con métricas
├── ventas/                 # Módulo de ventas y POS
│   ├── models.py          # Modelos Venta, DetalleVenta
│   ├── views.py           # Vistas de POS, búsqueda, historial
│   ├── urls.py            # Rutas de ventas
│   └── templates/ventas/
│       ├── nueva_venta.html      # Interfaz POS con escaneo
│       └── historial_ventas.html # Historial y anulación
├── productos/             # Módulo de inventario
│   ├── models.py          # Modelo Producto, Categoría
│   ├── views.py
│   ├── urls.py
│   └── templates/productos/
│       ├── lista_productos.html
│       ├── nuevo_producto.html
│       └── editar_producto.html
├── proveedores/           # Módulo de proveedores
│   ├── models.py          # Modelo Proveedor, TipoProveedor
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── lista_proveedores.html
│       ├── nuevo_proveedor.html
│       └── editar_proveedor.html
├── templates/             # Plantillas base
│   └── base/
│       └── base.html      # Plantilla madre con navbar
├── static/                # Archivos estáticos
│   └── vendor/
│       └── html5-qrcode.min.js  # Librería de escaneo
├── db.sqlite3             # Base de datos SQLite
├── manage.py              # Utilidad de línea de comandos de Django
└── README.md              # Este archivo
```

## 🔌 API Endpoints

### Búsqueda de Productos (AJAX)
```
GET /ventas/search/?q=nombre_o_codigo
```

**Respuesta:**
```json
[
  {
    "id": 1,
    "nombre": "Producto A",
    "codigo": "12345",
    "precio": "99.99",
    "stock": 50,
    "categoria": "Electrónica"
  }
]
```

### Crear Venta
```
POST /ventas/nueva-venta/
```

**Body:**
```json
{
  "productos": [
    {"id": 1, "cantidad": 2},
    {"id": 2, "cantidad": 1}
  ]
}
```

### Obtener Historial de Ventas
```
GET /ventas/historial/
```

### Anular Venta
```
POST /ventas/anular/<venta_id>/
```

## 💻 Tecnologías

### Backend
- **Django 5.2.7**: Framework web Python de alto nivel
- **Python 3.9+**: Lenguaje de programación
- **SQLite**: Base de datos (desarrollo)

### Frontend
- **HTML5**: Estructura
- **Bootstrap 5.3.3**: Framework CSS responsivo
- **Bootstrap Icons 1.11.3**: Iconografía
- **JavaScript ES6**: Lógica del cliente
- **html5-qrcode**: Librería de escaneo de códigos QR/barras

### Librerías JavaScript Adicionales
- **SweetAlert2**: Alertas personalizadas
- **DataTables**: Tablas con funcionalidades avanzadas
- **Web Audio API**: Sonidos de confirmación

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Roadmap

### Próximas Características
- [ ] Autenticación de usuarios con roles (Admin, Vendedor, Gerente)
- [ ] Suite de reportes y análisis avanzados
- [ ] Generación de facturas/recibos en PDF
- [ ] Historial de inventario y auditoría
- [ ] Descuentos y promociones
- [ ] Gestión de clientes
- [ ] Integración con pasarelas de pago
- [ ] API REST para aplicaciones móviles
- [ ] Sincronización en la nube

## ⚠️ Notas Importantes

### Desarrollo
- El proyecto está configurado en modo `DEBUG = True` para desarrollo
- Usa SQLite para desarrollo; considera PostgreSQL para producción
- El `SECRET_KEY` en `settings.py` es inseguro para producción

### Producción
- Cambia `DEBUG = False`
- Usa una `SECRET_KEY` segura y aleatoria
- Configura `ALLOWED_HOSTS` apropiadamente
- Usa una base de datos robusta (PostgreSQL recomendado)
- Implementa HTTPS
- Usa un servidor WSGI de producción (Gunicorn, uWSGI)

## 📧 Contacto y Soporte

Para reportar bugs o sugerir mejoras, abre un issue en el repositorio de GitHub.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**Última actualización:** Diciembre 2025

Hecho con ❤️ para PyMEs
