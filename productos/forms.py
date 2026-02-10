from django import forms
from .models import Producto, Categoria
from proveedores.models import Proveedor


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio_venta', 'stock', 'stock_minimo', 'categoria', 'proveedor']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción del producto (opcional)'
            }),
            'precio_venta': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0'
            }),
            'stock_minimo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '5',
                'min': '0'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
            'proveedor': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio_venta': 'Precio de Venta',
            'stock': 'Stock Actual',
            'stock_minimo': 'Stock Mínimo',
            'categoria': 'Categoría',
            'proveedor': 'Proveedor',
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la categoría'
            }),
        }
        labels = {
            'nombre': 'Nombre de la Categoría',
        }
