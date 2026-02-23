from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from productos.models import Producto

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(0, message="El total no puede ser negativo")]
    )
    vendedor = models.ForeignKey(User, on_delete=models.PROTECT)

    def clean(self):
        """Validaciones personalizadas."""
        super().clean()
        
        # Validar que el vendedor esté activo
        if self.vendedor and not self.vendedor.is_active:
            raise ValidationError({'vendedor': 'El vendedor no está activo.'})
    
    def __str__(self):
        return f"Venta #{self.id} por {self.vendedor.username} - {self.fecha.strftime('%Y-%m-%d')}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(
        validators=[MinValueValidator(1, message="La cantidad debe ser al menos 1")]
    )
    precio_unitario = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(0.01, message="El precio unitario debe ser mayor a 0")]
    )
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def clean(self):
        """Validaciones personalizadas."""
        super().clean()
        
        # Validar que hay suficiente stock
        if self.producto and self.cantidad:
            if self.cantidad > self.producto.stock:
                raise ValidationError({
                    'cantidad': f'Stock insuficiente. Disponible: {self.producto.stock}, solicitado: {self.cantidad}'
                })
    
    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
