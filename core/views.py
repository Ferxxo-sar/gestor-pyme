from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto, Venta, DetalleVenta
from django.contrib.auth.models import User

def nueva_venta(request):
    termino_busqueda = request.GET.get('busqueda', '')

    if termino_busqueda:
        productos = Producto.objects.filter(nombre__icontains=termino_busqueda)
    else:
        productos = Producto.objects.all()

    if request.method == 'POST':
        # por ahora lo dejo con el superuser, despues podria ser cualquier user!
        vendedor = User.objects.filter(is_superuser=True).first()

        # inicio el objeto venta en 0
        venta = Venta.objects.create(vendedor=vendedor, total=0)
        
        total_venta = 0
        productos_vendidos = 0

        # recorro el queryset(IMPORTANTE-> Lazy Evaluation) instanciado en el get anterior
        # el queryset no instancia la lista, simplemente guarda la consulta y no la realiza hasta necesitarla
        for producto in productos:
            cantidad_str = request.POST.get(f'cantidad_{producto.id}')
            # si no esta vacia castea la cantidad a int
            if cantidad_str and int(cantidad_str) > 0:
                cantidad = int(cantidad_str)

                # manejo de falta de stock
                if cantidad > producto.stock:
                    messages.error(request, f"No hay stock suficiente para '{producto.nombre}'. Disponible: {producto.stock}")
                    continue # <- salta a la siguiente iteracion

                # creo el detalle
                DetalleVenta.objects.create(
                    venta=venta,
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=producto.precio_venta
                )

                # descuento los vendidos del stock
                producto.stock -= cantidad
                producto.save() # impacto en la base de datos

                total_venta += cantidad * producto.precio_venta
                productos_vendidos += 1
        
        if productos_vendidos > 0:
            # si hubo venta se guarda
            venta.total = total_venta
            venta.save()
            messages.success(request, f"Venta #{venta.id} registrada")
        else:
            # sino se borra
            venta.delete()
            messages.warning(request, "venta #{venta.id} cancelada")

        # IMPORTANTE!!! Actualiza la pagina con el formulario limpio para comenzar otra venta
        return redirect('nueva_venta')
    # ESTO ES PARA PODER PROBAR EL PROGRAMA POR AHORA DESPUES ES ELIMINACION O MUERTE
    vendedor_por_defecto = User.objects.filter(is_superuser=True).first()
    
    # el context el comunicador con el HTML
    context = {
        'productos': productos,
        'vendedor': vendedor_por_defecto,
    }
    return render(request, 'core/nueva_venta.html', context)