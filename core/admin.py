from django.contrib import admin

# importo todos los modelos
from .models import Categoria, Proveedor, Producto, Venta, DetalleVenta

# otorgo permisos de administrador
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(DetalleVenta)