from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('productos/', include('productos.urls')),  # Movido al principio
    path('ventas/', include('ventas.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]