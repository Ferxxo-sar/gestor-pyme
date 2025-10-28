from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Venta, DetalleVenta
from productos.models import Producto

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
