# Guía de Contribución 🤝

¡Gracias por tu interés en contribuir a Gestor PyME! Esta guía te ayudará a empezar.

## 📋 Código de Conducta

Este proyecto y todos los participantes están regidos por nuestro Código de Conducta. Al participar, se espera que respetes este código.

### Se espera que:
- Seas respetuoso y considerado con otros
- Aceptes críticas constructivas
- Te enfoques en lo que es mejor para la comunidad
- Muestres empatía hacia otros miembros

## 🚀 Cómo Contribuir

### Reportar Bugs

Si encuentras un bug, abre un [Issue](https://github.com/Ferxxo-sar/gestor-pyme/issues) con:

1. **Título descriptivo**: Resume el problema en una línea
2. **Descripción detallada**: Explica el bug
3. **Pasos para reproducir**:
   ```
   1. Ve a '...'
   2. Haz clic en '....'
   3. Observa el error
   ```
4. **Comportamiento esperado**: Qué debería suceder
5. **Comportamiento actual**: Qué está sucediendo
6. **Capturas de pantalla**: Si es posible
7. **Entorno**:
   - SO: [ej. Windows 10]
   - Python: [ej. 3.9.0]
   - Django: [ej. 6.0.2]
   - Navegador: [ej. Chrome 120]

### Sugerir Mejoras

Para sugerir nuevas funcionalidades:

1. Revisa si ya existe un Issue similar
2. Abre un nuevo Issue con la etiqueta "enhancement"
3. Describe claramente la funcionalidad
4. Explica por qué sería útil
5. Proporciona ejemplos de uso si es posible

## 💻 Proceso de Desarrollo

### 1. Fork y Clone

```bash
# Fork el repositorio en GitHub
# Luego clona tu fork
git clone https://github.com/TU-USUARIO/gestor-pyme.git
cd gestor-pyme

# Agrega el repositorio original como remote
git remote add upstream https://github.com/Ferxxo-sar/gestor-pyme.git
```

### 2. Crear una Rama

```bash
# Actualiza tu main
git checkout main
git pull upstream main

# Crea una nueva rama
git checkout -b feature/nombre-descriptivo
# o
git checkout -b bugfix/descripcion-del-bug
```

**Convención de nombres de ramas:**
- `feature/` - Para nuevas funcionalidades
- `bugfix/` - Para corrección de bugs
- `hotfix/` - Para correcciones urgentes
- `docs/` - Para documentación
- `refactor/` - Para refactorización de código

### 3. Configurar el Entorno

```bash
# Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Instalar dependencias
pip install django

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py crear_superusuario
```

### 4. Hacer tus Cambios

#### Estilo de Código

- Sigue [PEP 8](https://pep8.org/) para Python
- Usa nombres descriptivos para variables y funciones
- Comenta código complejo
- Mantén líneas de menos de 100 caracteres

#### Ejemplo de código limpio:

```python
# ✅ BIEN
def calcular_total_venta(productos, aplicar_iva=True):
    """
    Calcula el total de una venta incluyendo IVA.
    
    Args:
        productos (list): Lista de productos con precio y cantidad
        aplicar_iva (bool): Si se debe aplicar IVA (default: True)
    
    Returns:
        Decimal: Total de la venta
    """
    subtotal = sum(p.precio * p.cantidad for p in productos)
    if aplicar_iva:
        return subtotal * Decimal('1.16')
    return subtotal

# ❌ MAL
def calc(p,i=True):
    t=0
    for x in p:
        t+=x.precio*x.cantidad
    if i:
        return t*1.16
    return t
```

#### Estructura de Commits

Usa mensajes de commit descriptivos:

```bash
# Formato recomendado
tipo(scope): descripción corta

Descripción más detallada si es necesario.
Explica QUÉ cambió y POR QUÉ, no cómo.
```

**Tipos:**
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Cambios en documentación
- `style`: Formato, sin cambios de código
- `refactor`: Refactorización
- `test`: Agregar o modificar tests
- `chore`: Mantenimiento

**Ejemplos:**
```bash
git commit -m "feat(ventas): agregar descuentos por cantidad"
git commit -m "fix(productos): corregir cálculo de stock"
git commit -m "docs(readme): actualizar guía de instalación"
```

### 5. Tests

Antes de enviar tu Pull Request:

```bash
# Ejecutar tests (si existen)
python manage.py test

# Verificar que el servidor inicia sin errores
python manage.py runserver

# Probar manualmente las funcionalidades modificadas
```

### 6. Push y Pull Request

```bash
# Asegúrate de que tu rama está actualizada
git fetch upstream
git rebase upstream/main

# Push a tu fork
git push origin feature/nombre-descriptivo
```

Luego en GitHub:
1. Ve a tu fork
2. Haz clic en "Compare & pull request"
3. Completa el template de PR
4. Espera la revisión

#### Template de Pull Request

```markdown
## Descripción
Breve descripción de los cambios

## Tipo de cambio
- [ ] Bug fix (cambio que corrige un issue)
- [ ] Nueva funcionalidad (cambio que agrega funcionalidad)
- [ ] Breaking change (cambio que puede romper funcionalidad existente)
- [ ] Documentación

## ¿Cómo se ha probado?
Describe las pruebas realizadas

## Checklist
- [ ] Mi código sigue el estilo del proyecto
- [ ] He realizado una auto-revisión
- [ ] He comentado código complejo
- [ ] He actualizado la documentación
- [ ] Mis cambios no generan nuevas warnings
- [ ] He probado que funciona localmente
```

## 📚 Áreas de Contribución

### Funcionalidades Pendientes
- [ ] Sistema de reportes con gráficos
- [ ] Exportación a PDF/Excel
- [ ] Sistema de clientes
- [ ] Facturación electrónica
- [ ] API RESTful
- [ ] App móvil
- [ ] Sistema de notificaciones
- [ ] Múltiples sucursales

### Mejoras de Código
- [ ] Agregar tests unitarios
- [ ] Mejorar validación de formularios
- [ ] Optimizar queries de base de datos
- [ ] Agregar decoradores de permisos
- [ ] Implementar caché

### Documentación
- [ ] Mejorar comentarios en código
- [ ] Crear tutoriales en video
- [ ] Traducir documentación
- [ ] Agregar ejemplos de uso

## 🔍 Proceso de Revisión

Cuando abres un PR:

1. **Revisión automática**: Se ejecutan checks automáticos
2. **Revisión de código**: Un maintainer revisa tu código
3. **Feedback**: Puede haber comentarios o solicitud de cambios
4. **Aprobación**: Una vez aprobado, se hace merge

### Tiempo de respuesta esperado
- Issues: 2-3 días
- PRs: 3-5 días

## 💡 Consejos

### Para Principiantes
- Empieza con issues etiquetados como "good first issue"
- Lee el código existente para entender el estilo
- No temas hacer preguntas
- Empieza con cambios pequeños

### Para Contribuidores Experimentados
- Ayuda a revisar PRs de otros
- Propón mejoras de arquitectura
- Mantén comunicación en Issues antes de cambios grandes
- Ayuda a mentorear nuevos contribuidores

## 📮 Contacto

¿Preguntas sobre contribución?
- Abre un Issue con la etiqueta "question"
- Menciona a @Ferxxo-sar en tu Issue o PR

## 🎉 Reconocimientos

Todos los contribuidores serán listados en el README.

---

¡Gracias por contribuir a Gestor PyME! 🚀
