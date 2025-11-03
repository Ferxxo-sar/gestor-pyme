from django.contrib import admin
from .models import Proveedor, TipoProveedor

@admin.register(TipoProveedor)
class TipoProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'email', 'tipo')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre', 'email')
    list_filter = ('tipo',)
