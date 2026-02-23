from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import transaction
from .models import Venta, DetalleVenta
from productos.models import Producto

@login_required
def historial_ventas(request):
    """Vista para mostrar el historial de ventas."""
    ventas = Venta.objects.all().select_related('vendedor').prefetch_related('detalleventa_set__producto').order_by('-fecha')
    
    context = {
        'ventas': ventas,
    }
    return render(request, 'ventas/historial_ventas.html', context)


@login_required
@transaction.atomic
def anular_venta(request, venta_id):
    """Vista para anular una venta y devolver el stock."""
    if request.method == 'POST':
        try:
            venta = Venta.objects.get(id=venta_id)
            
            # Devolver el stock de cada producto
            for detalle in venta.detalleventa_set.all():
                producto = detalle.producto
                producto.stock += detalle.cantidad
                producto.save()
            
            # Eliminar la venta
            venta.delete()
            messages.success(request, f'Venta #{venta_id} anulada exitosamente. Stock devuelto.')
            
        except Venta.DoesNotExist:
            messages.error(request, 'La venta no existe.')
        except Exception as e:
            messages.error(request, f'Error al anular la venta: {str(e)}')
    
    return redirect('ventas:historial_ventas')

@login_required
@transaction.atomic
def nueva_venta(request):
    termino_busqueda = request.GET.get('busqueda', '')

    if termino_busqueda:
        productos = Producto.objects.filter(nombre__icontains=termino_busqueda)
    else:
        productos = Producto.objects.all()

    if request.method == 'POST':
        vendedor = User.objects.filter(is_superuser=True).first()
        venta = Venta.objects.create(vendedor=vendedor, total=0)
        total_venta = 0
        productos_vendidos = 0

        for producto in productos:
            cantidad_str = request.POST.get(f'cantidad_{producto.id}')
            if cantidad_str and int(cantidad_str) > 0:
                cantidad = int(cantidad_str)

                if cantidad > producto.stock:
                    messages.error(request, f"No hay stock suficiente para '{producto.nombre}'. Disponible: {producto.stock}")
                    continue

                DetalleVenta.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio_venta
                )

                producto.stock -= cantidad
                producto.save()

                total_venta += cantidad * producto.precio_venta
                productos_vendidos += 1
        
        if productos_vendidos > 0:
            venta.total = total_venta
            venta.save()
            messages.success(request, f"Venta #{venta.id} registrada")
        else:
            venta.delete()
            messages.warning(request, "venta #{venta.id} cancelada")

        return redirect('ventas:nueva_venta')

    vendedor_por_defecto = User.objects.filter(is_superuser=True).first()
    
    context = {
        'productos': productos,
        'vendedor': vendedor_por_defecto,
    }
    return render(request, 'ventas/nueva_venta.html', context)


@login_required
def search_products(request):
    """AJAX endpoint: return products matching q as JSON."""
    from django.db.models import Q
    
    q = request.GET.get('q', '').strip()
    if not q:
        return JsonResponse({'results': []})

    # Buscar por nombre (parcial) o por código (parcial)
    query = Q(nombre__icontains=q)
    
    # Si el término contiene solo dígitos, también buscar por código
    if q.isdigit():
        query |= Q(codigo__icontains=q)
    
    productos_qs = Producto.objects.filter(query)[:60]
    
    results = []
    for p in productos_qs:
        try:
            categoria_nombre = str(p.categoria) if hasattr(p, 'categoria') and p.categoria else None
        except:
            categoria_nombre = None
            
        results.append({
            'id': p.id,
            'nombre': p.nombre,
            'precio_venta': float(p.precio_venta),
            'stock': p.stock,
            'categoria': categoria_nombre,
            'stock_minimo': getattr(p, 'stock_minimo', 0),
        })

    return JsonResponse({'results': results})
