from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('nueva/', views.nueva_venta, name='nueva_venta'),
]