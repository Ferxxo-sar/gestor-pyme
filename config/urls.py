from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('productos/', include('productos.urls')),  # Movido al principio
    path('ventas/', include('ventas.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('admin/', admin.site.urls),
    # si no es admin va a buscar al core 
    path('', include('core.urls')),
]