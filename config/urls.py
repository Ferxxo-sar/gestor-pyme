from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # si no es admin va a buscar al core 
    path('', include('core.urls')),
]