from django.db import models

class CodigoPostal(models.Model):
    codigo = models.CharField(max_length=10, unique=False)
    
    def __str__(self):
        return self.codigo
class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, unique=False)
    # Link ciudad to un Estado (provincia) to allow cascading selects
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Estado(models.Model):
    nombre = models.CharField(max_length=100, unique=False)
    # Link estado to a Pais to allow country -> state cascading
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
class Direccion(models.Model):
    calle = models.CharField(max_length=200, blank=False)
    numero = models.CharField(max_length=20, blank=False)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, blank=False)
    codigo_postal = models.ForeignKey(CodigoPostal, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=False)
    
    def __str__(self):
        return f"{self.calle}, {self.ciudad}, {self.pais}"
class TipoProveedor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre
class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tipo = models.ForeignKey(TipoProveedor, on_delete=models.SET_NULL, null=True, blank=True)
    
    
    def __str__(self):
        return self.nombre
