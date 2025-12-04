from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('nueva/', views.nueva_venta, name='nueva_venta'),
    path('search/', views.search_products, name='search_products'),
    path('historial/', views.historial_ventas, name='historial_ventas'),
    path('<int:venta_id>/anular/', views.anular_venta, name='anular_venta'),
]