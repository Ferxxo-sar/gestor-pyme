# 📥 Guía de Instalación - Gestor PyME

Esta guía te ayudará a instalar y configurar el sistema Gestor PyME en tu computadora desde GitHub.

---

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

### ✅ Software Necesario

1. **Python 3.9 o superior**
   - Descarga desde: https://www.python.org/downloads/
   - Durante la instalación, marca la opción "Add Python to PATH"
   - Verifica la instalación:
     ```bash
     python --version
     ```

2. **Git** (para clonar el repositorio)
   - Descarga desde: https://git-scm.com/downloads
   - Verifica la instalación:
     ```bash
     git --version
     ```

3. **Navegador Web Moderno**
   - Chrome, Firefox, Edge o Safari actualizado
   - Necesario para el escáner de códigos QR

---

## 🚀 Instalación Paso a Paso

### Paso 1: Clonar el Repositorio

Abre tu terminal (CMD, PowerShell o Terminal) y ejecuta:

```bash
# Opción 1: Clonar con HTTPS
git clone https://github.com/Ferxxo-sar/gestor-pyme.git

# Opción 2: Clonar con SSH (si tienes configurada una clave SSH)
git clone git@github.com:Ferxxo-sar/gestor-pyme.git
```

Navega al directorio del proyecto:

```bash
cd gestor-pyme
```

---

### Paso 2: Crear Entorno Virtual

El entorno virtual aísla las dependencias del proyecto.

#### En Windows:

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
.venv\Scripts\activate
```

#### En macOS/Linux:

```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate
```

Cuando el entorno esté activo, verás `(.venv)` al inicio de tu línea de comando.

---

### Paso 3: Instalar Dependencias

Con el entorno virtual activado:

```bash
# Instalar Django
pip install django

# Si hay un archivo requirements.txt
pip install -r requirements.txt
```

---

### Paso 4: Configurar Variables de Entorno

El sistema usa variables de entorno para configuración sensible (SECRET_KEY, DEBUG, etc.).

#### 4.1. Crear archivo .env

Copia el archivo de ejemplo:

**Windows:**
```bash
copy .env.example .env
```

**macOS/Linux:**
```bash
cp .env.example .env
```

#### 4.2. Generar SECRET_KEY

Genera una nueva clave secreta para tu instalación:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### 4.3. Editar el archivo .env

Abre el archivo `.env` con tu editor de texto favorito y configura:

```env
# SEGURIDAD: Django Secret Key
SECRET_KEY=tu-clave-secreta-generada-aqui

# MODO DEBUG (True para desarrollo, False para producción)
DEBUG=True

# HOSTS PERMITIDOS
ALLOWED_HOSTS=localhost,127.0.0.1
```

**⚠️ IMPORTANTE:** 
- Nunca compartas tu archivo `.env` ni lo subas a Git
- Cambia `DEBUG=False` en producción
- Configura `ALLOWED_HOSTS` con tu dominio en producción

---

### Paso 5: Configurar la Base de Datos

Aplica las migraciones para crear la base de datos:

```bash
python manage.py migrate
```

Esto creará un archivo `db.sqlite3` con todas las tablas necesarias.

---

### Paso 6: Crear Superusuario (Administrador)

#### Opción 1: Automática (Recomendada)

El proyecto incluye un comando personalizado que crea automáticamente un superusuario:

```bash
python manage.py crear_superusuario
```

Credenciales por defecto:
- **Usuario:** `admin`
- **Contraseña:** `admin`
- **Email:** `admin@admin.com`

#### Opción 2: Manual

Crea tu propio superusuario:

```bash
python manage.py createsuperuser
```

Se te pedirá:
- Nombre de usuario
- Email (opcional)
- Contraseña (escríbela dos veces)

---

### Paso 7: Iniciar el Servidor

#### Opción 1: Usando Scripts de Inicio

**Windows (CMD):**
```bash
iniciar_servidor.bat
```

**Windows (PowerShell):**
```bash
.\iniciar_servidor.ps1
```

Estos scripts automáticamente:
1. Crean el superusuario si no existe
2. Inician el servidor en http://127.0.0.1:8000/

#### Opción 2: Manual

```bash
python manage.py runserver
```

---

### Paso 7: Acceder al Sistema

Una vez iniciado el servidor, abre tu navegador y dirígete a:

- **Aplicación principal:** http://127.0.0.1:8000/
- **Panel de administración:** http://127.0.0.1:8000/admin/

Inicia sesión con las credenciales del superusuario.

---

## 🎨 Configuración Post-Instalación

### 1. Crear Categorías de Productos

1. Ve a **Productos** → botón **Agregar Producto**
2. Haz clic en el ícono **+** junto a "Categoría"
3. Crea categorías como:
   - Alimentos
   - Bebidas
   - Limpieza
   - Electrónica
   - Etc.

### 2. Agregar Proveedores

1. Ve a **Proveedores** → **Agregar Proveedor**
2. Completa la información básica:
   - Nombre del proveedor
   - Teléfono
   - Email

### 3. Agregar Productos

1. Ve a **Productos** → **Agregar Producto**
2. Llena el formulario:
   - Nombre del producto
   - Descripción
   - Precio de venta
   - Stock inicial
   - Stock mínimo (para alertas)
   - Categoría
   - Proveedor (opcional)

### 4. Configurar el Escáner (Opcional)

Para usar el escáner de códigos:

1. Accede desde una red local (http://127.0.0.1:8000/)
2. Permite el acceso a la cámara cuando el navegador lo solicite
3. Asegúrate de que tus productos tengan códigos de barras o códigos QR generados

---

## 🔧 Comandos Útiles

### Gestión de la Base de Datos

```bash
# Crear migraciones después de cambios en modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear un respaldo de la base de datos (copiar db.sqlite3)
copy db.sqlite3 db.backup.sqlite3
```

### Gestión del Servidor

```bash
# Iniciar servidor en puerto diferente
python manage.py runserver 8080

# Hacer el servidor accesible en la red local
python manage.py runserver 0.0.0.0:8000
```

### Gestión de Usuarios

```bash
# Crear superusuario automáticamente
python manage.py crear_superusuario

# Crear superusuario manualmente
python manage.py createsuperuser

# Cambiar contraseña de usuario
python manage.py changepassword admin
```

### Otros Comandos

```bash
# Abrir shell de Django
python manage.py shell

# Recopilar archivos estáticos
python manage.py collectstatic

# Ver todas las URLs del proyecto
python manage.py show_urls
```

---

## 🐛 Solución de Problemas Comunes

### Error: "python no se reconoce como comando"

**Solución:** Agrega Python al PATH del sistema.

1. Busca "Variables de entorno" en Windows
2. Edita la variable PATH
3. Agrega la ruta de instalación de Python (ej: `C:\Python39\`)
4. Reinicia la terminal

### Error: "No module named 'django'"

**Solución:** Asegúrate de tener el entorno virtual activado e instala Django:

```bash
# Activar entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Instalar Django
pip install django
```

### Error: "port 8000 already in use"

**Solución:** El puerto está ocupado. Usa otro puerto:

```bash
python manage.py runserver 8080
```

O detén el proceso que está usando el puerto 8000.

### Error: "OperationalError: no such table"

**Solución:** Aplica las migraciones:

```bash
python manage.py migrate
```

### El escáner de códigos no funciona

**Posibles soluciones:**

1. Permite el acceso a la cámara en el navegador
2. Usa HTTPS o localhost (http://127.0.0.1:8000/)
3. Verifica que tu navegador soporte getUserMedia API
4. Prueba con otro navegador (Chrome recomendado)

### Error al crear superusuario automático

**Solución:** Créalo manualmente:

```bash
python manage.py createsuperuser
```

---

## 🔄 Actualizar el Sistema

Para obtener las últimas actualizaciones del repositorio:

```bash
# Guardar cambios locales (si los hay)
git stash

# Obtener últimos cambios
git pull origin main

# Aplicar nuevas migraciones
python manage.py migrate

# Restaurar cambios locales
git stash pop
```

---

## 📦 Despliegue en Producción

Para desplegar en un servidor de producción:

1. **Cambia la configuración en `config/settings.py`:**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['tudominio.com', 'www.tudominio.com']
   ```

2. **Configura una base de datos más robusta** (PostgreSQL, MySQL)

3. **Usa un servidor WSGI** como Gunicorn o uWSGI

4. **Configura un servidor web** (Nginx, Apache)

5. **Configura HTTPS** con Let's Encrypt

6. **Recopila archivos estáticos:**
   ```bash
   python manage.py collectstatic
   ```

---

## 📞 ¿Necesitas Ayuda?

Si tienes problemas durante la instalación:

1. **Revisa esta guía nuevamente** para asegurarte de seguir todos los pasos
2. **Consulta el README.md** para información adicional
3. **Abre un Issue** en GitHub: https://github.com/Ferxxo-sar/gestor-pyme/issues
4. **Incluye en tu consulta:**
   - Sistema operativo
   - Versión de Python
   - Mensaje de error completo
   - Capturas de pantalla si es posible

---

## ✅ Checklist de Instalación

Marca cada paso a medida que lo completes:

- [ ] Python 3.9+ instalado
- [ ] Git instalado
- [ ] Repositorio clonado
- [ ] Entorno virtual creado
- [ ] Entorno virtual activado
- [ ] Django instalado
- [ ] Migraciones aplicadas
- [ ] Superusuario creado
- [ ] Servidor iniciado exitosamente
- [ ] Acceso a http://127.0.0.1:8000/ funcionando
- [ ] Login en panel de admin exitoso
- [ ] Categorías creadas
- [ ] Al menos un proveedor agregado
- [ ] Al menos un producto agregado
- [ ] Primera venta de prueba realizada

¡Felicidades! Si completaste todos los pasos, el sistema está listo para usar. 🎉

---

## 📚 Próximos Pasos

Después de la instalación:

1. **Lee el README.md completo** para entender todas las funcionalidades
2. **Explora el panel de administración** en http://127.0.0.1:8000/admin/
3. **Carga datos iniciales** (categorías, proveedores, productos)
4. **Realiza ventas de prueba** para familiarizarte con el sistema
5. **Personaliza el sistema** según las necesidades de tu negocio

---

⭐ **¡Gracias por usar Gestor PyME!** ⭐
