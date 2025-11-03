from django.db import models

class TipoProveedor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tipo = models.ForeignKey(TipoProveedor, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self):
        return self.nombre
