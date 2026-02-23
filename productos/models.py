from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from proveedores.models import Proveedor

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.IntegerField(unique=True)
    descripcion = models.TextField(blank=True)
    precio_venta = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0.01, message="El precio debe ser mayor a 0")]
    )
    stock = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0, message="El stock no puede ser negativo")]
    )
    stock_minimo = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(0, message="El stock mínimo no puede ser negativo")]
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    
    def clean(self):
        """Validaciones personalizadas."""
        super().clean()
        
        # Validar que el código sea positivo
        if self.codigo and self.codigo <= 0:
            raise ValidationError({'codigo': 'El código debe ser un número positivo.'})
        
        # Validar que el stock mínimo no sea mayor al stock actual
        if self.stock_minimo > self.stock:
            raise ValidationError({
                'stock_minimo': f'El stock mínimo ({self.stock_minimo}) no puede ser mayor al stock actual ({self.stock}).'
            })
    
    def save(self, *args, **kwargs):
        """Override save para ejecutar validaciones."""
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre
