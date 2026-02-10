from django.contrib import admin
from .models import Proveedor, TipoProveedor, Direccion

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'calle', 'ciudad', 'estado', 'codigo_postal', 'pais')
    search_fields = ('calle', 'ciudad', 'estado', 'pais')

@admin.register(TipoProveedor)
class TipoProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'email', 'get_direccion', 'tipo')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre', 'email', 'direccion__calle', 'direccion__ciudad')
    list_filter = ('tipo',)
    
    def get_direccion(self, obj):
        if obj.direccion:
            return str(obj.direccion)
        return '-'
    get_direccion.short_description = 'Dirección'
