# core/urls.py
from django.urls import path
from . import views # Importa el archivo views.py de esta misma app

# Django busca esta lista específica para las URLs de la app.
urlpatterns = [
    # Define que la ruta raíz ('') será manejada por la vista 'nueva_venta'.
    path('', views.nueva_venta, name='nueva_venta'),
]