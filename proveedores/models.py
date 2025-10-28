from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre
