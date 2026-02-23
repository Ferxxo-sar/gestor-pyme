# Gestor PyME 🏪

Sistema de gestión integral para pequeñas y medianas empresas (PyMEs) desarrollado con Django. Incluye módulos de punto de venta, inventario, gestión de proveedores y análisis de ventas en tiempo real.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/Django-6.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Tabla de Contenidos

- [Características Principales](#-características-principales)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Instalación Rápida](#-instalación-rápida)
- [Uso del Sistema](#-uso-del-sistema)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

---

## ✨ Características Principales

### 🛒 **Punto de Venta (POS)**
- Interfaz intuitiva para procesar ventas rápidamente
- Escáner de códigos QR y códigos de barras integrado
- Búsqueda dinámica de productos en tiempo real
- Carrito de compras interactivo con cálculo automático de totales e IVA
- Gestión de descuentos y promociones
- Impresión de tickets de venta
- Feedback audiovisual en cada operación

### 📦 **Gestión de Inventario**
- Control completo de productos y categorías
- Alertas automáticas de stock bajo
- Registro de entrada y salida de productos
- Códigos de barras únicos para cada producto
- Visualización de stock en tiempo real
- Historial de movimientos de inventario
- Formularios intuitivos para agregar/editar productos

### 🤝 **Gestión de Proveedores**
- Base de datos completa de proveedores
- Información de contacto detallada (teléfono, email, dirección)
- Clasificación por tipo de proveedor
- Sistema de ubicación con ciudad, estado y país
- Panel de visualización tipo tarjetas
- Formularios intuitivos para agregar/editar proveedores

### 📊 **Dashboard y Análisis**
- Dashboard en tiempo real con métricas clave:
  - Total de ventas del día
  - Cantidad de productos en inventario
  - Productos con stock bajo
  - Total de proveedores registrados
- Gráficos y visualización de datos
- Historial completo de ventas
- Cancelación de ventas con devolución automática de stock

### 🔐 **Panel de Administración**
- Sistema de autenticación seguro
- Gestión de usuarios y permisos
- Panel de administración de Django integrado
- Creación automática de superusuario

### 🛡️ **Seguridad (FASE 1 - Implementada)**
- **Autenticación obligatoria** - Todas las vistas protegidas con `@login_required`
- **Variables de entorno** - SECRET_KEY y configuración sensible separada del código
- **Validaciones de datos** - Códigos de producto únicos, validaciones de precios y stock
- **Transacciones atómicas** - Operaciones críticas protegidas contra inconsistencias
- **Configuración segura** - DEBUG y ALLOWED_HOSTS configurables por entorno

> 📋 Ver [SECURITY_CHANGELOG.md](SECURITY_CHANGELOG.md) para detalles completos de seguridad

---

## 🔧 Tecnologías Utilizadas

### Backend
- **Django 6.0.2** - Framework web de Python
- **SQLite3** - Base de datos ligera (incluida con Python)
- **Python 3.13+** - Lenguaje de programación

### Frontend
- **HTML5** - Estructura de páginas
- **CSS3** - Estilos y diseño responsive
- **Bootstrap 5** - Framework CSS para diseño moderno
- **Bootstrap Icons** - Iconografía
- **JavaScript ES6+** - Interactividad del cliente
- **html5-qrcode** - Escáner de códigos QR/barras

### Herramientas de Desarrollo
- **Git** - Control de versiones
- **VS Code** - Editor de código recomendado
- **Virtual Environment** - Aislamiento de dependencias

---

## 🚀 Instalación Rápida

> **📖 Para instrucciones detalladas, consulta [INSTALL.md](INSTALL.md)**

### Inicio Rápido

```bash
# 1. Clonar el repositorio
git clone https://github.com/Ferxxo-sar/gestor-pyme.git
cd gestor-pyme

# 2. Crear y activar entorno virtual
python -m venv .venv
.venv\Scripts\activate  # En Windows
# source .venv/bin/activate  # En macOS/Linux

# 3. Instalar Django
pip install django

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario (automático)
python manage.py crear_superusuario

# 6. Iniciar servidor
python manage.py runserver
```

**Accede a:** http://127.0.0.1:8000/

**Credenciales por defecto:**
- Usuario: `admin`
- Contraseña: `admin`

---

## 📖 Uso del Sistema

### 1. **Inicio de Sesión**
- **Panel admin:** http://127.0.0.1:8000/admin/
- Usuario: `admin` / Contraseña: `admin`

### 2. **Configuración Inicial**

#### Agregar Categorías
1. Ve a **Productos** → **Agregar Producto**
2. Haz clic en el botón **+** junto a "Categoría"
3. Ingresa el nombre (ej: "Alimentos", "Bebidas", "Limpieza")

#### Agregar Proveedores
1. Ve a **Proveedores** → **Agregar Proveedor**
2. Completa:
   - Nombre del proveedor
   - Teléfono (opcional)
   - Email (opcional)

#### Agregar Productos
1. Ve a **Productos** → **Agregar Producto**
2. Completa:
   - Nombre del producto
   - Descripción (opcional)
   - Precio de venta
   - Stock inicial
   - Stock mínimo (para alertas)
   - Categoría
   - Proveedor (opcional)

### 3. **Realizar Ventas**

#### Usando el Escáner de Códigos
1. Ve a **Nueva Venta**
2. Haz clic en **Escanear Código**
3. Permite el acceso a la cámara
4. Escanea el código QR o código de barras
5. El producto se agregará automáticamente

#### Búsqueda Manual
1. Ve a **Nueva Venta**
2. Escribe el nombre o código en el buscador
3. Selecciona el producto
4. Se agregará al carrito

#### Completar la Venta
1. Revisa los productos en el carrito
2. Ajusta cantidades si es necesario
3. Verifica el total y el IVA
4. Haz clic en **Procesar Venta**
5. El stock se actualiza automáticamente

### 4. **Consultar Información**

#### Ver Stock de Productos
- Ve a **Productos** para ver todos
- Productos con stock bajo se resaltan en amarillo/rojo

#### Dashboard de Métricas
La página principal muestra:
- Ventas del día
- Total de productos
- Productos con stock bajo
- Total de proveedores

---

## 📁 Estructura del Proyecto

```
gestor-pyme/
├── config/                 # Configuración de Django
│   ├── settings.py        # Configuración principal
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # Configuración WSGI
│
├── core/                   # App principal
│   ├── management/        # Comandos personalizados
│   │   └── commands/
│   │       └── crear_superusuario.py
│   ├── templates/         # Templates del core
│   │   └── core/
│   │       └── index.html # Dashboard principal
│   └── views.py           # Vistas del core
│
├── productos/             # App de productos
│   ├── forms.py           # Formularios de productos
│   ├── models.py          # Modelos (Producto, Categoria)
│   ├── templates/         # Templates de productos
│   ├── urls.py            # URLs de productos
│   └── views.py           # Vistas de productos
│
├── proveedores/           # App de proveedores
│   ├── forms.py           # Formularios de proveedores
│   ├── models.py          # Modelos (Proveedor, Direccion)
│   ├── templates/         # Templates de proveedores
│   ├── urls.py            # URLs de proveedores
│   └── views.py           # Vistas de proveedores
│
├── ventas/                # App de ventas
│   ├── models.py          # Modelos (Venta, DetalleVenta)
│   ├── templates/         # Templates de ventas
│   ├── urls.py            # URLs de ventas
│   └── views.py           # Vistas de ventas (POS)
│
├── templates/             # Templates globales
│   └── base/
│       └── base.html      # Template base
│
├── static/                # Archivos estáticos
│
├── manage.py              # Script de gestión de Django
├── iniciar_servidor.bat   # Script de inicio (Windows)
├── iniciar_servidor.ps1   # Script de inicio (PowerShell)
├── README.md              # Este archivo
└── INSTALL.md             # Guía de instalación detallada
```

---

## 🎯 Casos de Uso

### Para Tiendas de Abarrotes
- Control de inventario de productos variados
- Punto de venta rápido con escáner
- Gestión de múltiples proveedores
- Alertas de productos por agotarse

### Para Farmacias
- Búsqueda rápida de medicamentos
- Control de stock con alertas
- Registro de proveedores farmacéuticos
- Historial de ventas detallado

### Para Librerías
- Escaneo de códigos ISBN
- Categorización por tipo de libro
- Gestión de editoriales como proveedores
- Control de existencias

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto:

1. Haz un Fork del repositorio
2. Crea una rama para tu función (`git checkout -b feature/NuevaFuncion`)
3. Realiza tus cambios y haz commit (`git commit -m 'Agregar nueva función'`)
4. Sube tus cambios (`git push origin feature/NuevaFuncion`)
5. Abre un Pull Request

### Áreas de Mejora
- [ ] Sistema de reportes avanzados con gráficos
- [ ] Exportación a PDF/Excel
- [ ] Múltiples puntos de venta
- [ ] Sistema de facturación electrónica
- [ ] API RESTful para integraciones
- [ ] App móvil nativa
- [ ] Sistema de clientes y fidelización
- [ ] Integración con plataformas de pago

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 👨‍💻 Autor

**Fernando SAR**
- GitHub: [@Ferxxo-sar](https://github.com/Ferxxo-sar)

---

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:

1. Abre un [Issue](https://github.com/Ferxxo-sar/gestor-pyme/issues) en GitHub
2. Describe el problema con el mayor detalle posible
3. Incluye capturas de pantalla si es necesario

---

## 🙏 Agradecimientos

- Django Software Foundation por el excelente framework
- Bootstrap por el framework CSS
- Comunidad de código abierto por las librerías utilizadas

---

⭐ **Si este proyecto te fue útil, no olvides dejar una estrella en GitHub!** ⭐
