from django.contrib import admin
from .models import Venta, DetalleVenta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'vendedor', 'total')
    list_display_links = ('id',)
    list_filter = ('fecha', 'vendedor')
    search_fields = ('id', 'vendedor__username')
    date_hierarchy = 'fecha'

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'venta', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
    list_display_links = ('id',)
    list_filter = ('venta__fecha',)
    search_fields = ('venta__id', 'producto__nombre')
