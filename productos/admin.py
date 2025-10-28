from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio_venta', 'stock', 'categoria', 'proveedor')
    list_display_links = ('id', 'nombre')
    list_filter = ('categoria', 'proveedor')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('precio_venta', 'stock')
