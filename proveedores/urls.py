from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('', views.lista_proveedores, name='lista'),
    path('crear/', views.crear_proveedor, name='crear'),
    path('editar/<int:pk>/', views.editar_proveedor, name='editar'),
    # AJAX endpoints for cascading selects
    path('ajax/estados/<int:pais_id>/', views.estados_por_pais, name='ajax_estados_por_pais'),
    path('ajax/ciudades/<int:estado_id>/', views.ciudades_por_estado, name='ajax_ciudades_por_estado'),
    path('eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar'),
]