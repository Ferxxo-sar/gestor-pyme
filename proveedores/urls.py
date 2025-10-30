from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('proveedores/', views.nuevo_proveedor, name='proveedor'),
]