from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'email')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre', 'email')
