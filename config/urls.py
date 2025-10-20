# config/urls.py
from django.contrib import admin
# Es fundamental importar la función 'include'
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea delega cualquier URL que no sea '/admin/'
    # al archivo urls.py de la aplicación 'core'.
    path('', include('core.urls')),
]