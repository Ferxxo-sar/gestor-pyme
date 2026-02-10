from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        nombre_producto = producto.nombre
        producto.delete()
        messages.success(request, f'El producto {nombre_producto} ha sido eliminado.')
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'ok', 'message': f'El producto {nombre_producto} ha sido eliminado.'})
        return redirect('productos:lista_productos')
    
    return redirect('productos:lista_productos')

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        try:
            producto.nombre = request.POST.get('nombre')
            producto.codigo = request.POST.get('codigo')
            producto.precio_venta = request.POST.get('precio')
            producto.stock = request.POST.get('stock')
            producto.save()
            
            messages.success(request, f'Producto {producto.nombre} actualizado exitosamente.')
            return redirect('productos:lista_productos')
        except Exception as e:
            messages.error(request, f'Error al actualizar el producto: {str(e)}')
            
    return render(request, 'productos/editar_producto.html', {'producto': producto})

def nuevo_producto(request):
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            codigo = request.POST.get('codigo')
            precio = request.POST.get('precio')
            stock = request.POST.get('stock')
            
            producto = Producto.objects.create(
                nombre=nombre,
                codigo=codigo,
                precio_venta=precio,
                stock=stock
            )
            messages.success(request, f'Producto {producto.nombre} creado exitosamente.')
            return redirect('productos:lista_productos')
        except Exception as e:
            messages.error(request, f'Error al crear el producto: {str(e)}')
            
    return render(request, 'productos/nuevo_producto.html')
