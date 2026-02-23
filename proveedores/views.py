from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import (
    Proveedor, TipoProveedor, Direccion,
    Ciudad, Estado, Pais, CodigoPostal
)
from django.http import JsonResponse


@login_required
def estados_por_pais(request, pais_id):
    """Devuelve JSON con los estados pertenecientes a un país."""
    estados = list(Estado.objects.filter(pais_id=pais_id).values('id', 'nombre'))
    return JsonResponse({'estados': estados})


@login_required
def ciudades_por_estado(request, estado_id):
    """Devuelve JSON con las ciudades pertenecientes a un estado."""
    ciudades = list(Ciudad.objects.filter(estado_id=estado_id).values('id', 'nombre'))
    return JsonResponse({'ciudades': ciudades})


@login_required
def lista_proveedores(request):
    """Muestra la lista de proveedores."""
    proveedores = Proveedor.objects.select_related('tipo', 'direccion').all().order_by('nombre')
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})


@login_required
def crear_proveedor(request):
    """Formulario para crear un proveedor con su dirección."""
    tipos = TipoProveedor.objects.all()
    context = {
        'tipos': tipos,
        'ciudades': Ciudad.objects.all(),
        'estados': Estado.objects.all(),
        'paises': Pais.objects.all(),
        'codigos_postales': CodigoPostal.objects.all(),
    }

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        tipo_id = request.POST.get('tipo')

        # Datos de dirección
        calle = request.POST.get('calle')
        numero = request.POST.get('numero')
        ciudad_id = request.POST.get('ciudad')
        estado_id = request.POST.get('estado')
        codigo_postal_id = request.POST.get('codigo_postal')
        pais_id = request.POST.get('pais')

        if not nombre:
            messages.error(request, 'El nombre es obligatorio')
            return render(request, 'crear_proveedor.html', context)

        # Crear dirección si se proporcionaron datos
        direccion = None
        if calle and numero and ciudad_id:
            try:
                direccion = Direccion.objects.create(
                    calle=calle,
                    numero=numero,
                    ciudad=Ciudad.objects.get(pk=ciudad_id),
                    estado=Estado.objects.get(pk=estado_id) if estado_id else None,
                    codigo_postal=CodigoPostal.objects.get(pk=codigo_postal_id) if codigo_postal_id else None,
                    pais=Pais.objects.get(pk=pais_id) if pais_id else None
                )
            except (Ciudad.DoesNotExist, Estado.DoesNotExist, Pais.DoesNotExist, CodigoPostal.DoesNotExist):
                messages.error(request, 'Error al procesar los datos de la dirección')
                return render(request, 'crear_proveedor.html', context)

        tipo = TipoProveedor.objects.filter(pk=tipo_id).first() if tipo_id else None

        Proveedor.objects.create(
            nombre=nombre,
            email=email or None,
            telefono=telefono or '',
            direccion=direccion,
            tipo=tipo
        )

        messages.success(request, 'Proveedor creado exitosamente')
        return redirect('proveedores:lista')

    return render(request, 'crear_proveedor.html', context)


@login_required
def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    tipos = TipoProveedor.objects.all()
    context = {
        'proveedor': proveedor,
        'tipos': tipos,
        'ciudades': Ciudad.objects.all(),
        'estados': Estado.objects.all(),
        'paises': Pais.objects.all(),
        'codigos_postales': CodigoPostal.objects.all(),
    }

    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre') or proveedor.nombre
        proveedor.email = request.POST.get('email') or proveedor.email
        proveedor.telefono = request.POST.get('telefono') or proveedor.telefono
        
        # Actualizar o crear dirección
        calle = request.POST.get('calle')
        numero = request.POST.get('numero')
        ciudad_id = request.POST.get('ciudad')
        estado_id = request.POST.get('estado')
        codigo_postal_id = request.POST.get('codigo_postal')
        pais_id = request.POST.get('pais')

        try:
            if calle and numero and ciudad_id:
                if proveedor.direccion:
                    # Actualizar dirección existente
                    proveedor.direccion.calle = calle
                    proveedor.direccion.numero = numero
                    proveedor.direccion.ciudad = Ciudad.objects.get(pk=ciudad_id)
                    if estado_id:
                        proveedor.direccion.estado = Estado.objects.get(pk=estado_id)
                    if codigo_postal_id:
                        proveedor.direccion.codigo_postal = CodigoPostal.objects.get(pk=codigo_postal_id)
                    if pais_id:
                        proveedor.direccion.pais = Pais.objects.get(pk=pais_id)
                    proveedor.direccion.save()
                else:
                    # Crear nueva dirección
                    direccion = Direccion.objects.create(
                        calle=calle,
                        numero=numero,
                        ciudad=Ciudad.objects.get(pk=ciudad_id),
                        estado=Estado.objects.get(pk=estado_id) if estado_id else None,
                        codigo_postal=CodigoPostal.objects.get(pk=codigo_postal_id) if codigo_postal_id else None,
                        pais=Pais.objects.get(pk=pais_id) if pais_id else None
                    )
                    proveedor.direccion = direccion
        except (Ciudad.DoesNotExist, Estado.DoesNotExist, Pais.DoesNotExist, CodigoPostal.DoesNotExist):
            messages.error(request, 'Error al procesar los datos de la dirección')
            return render(request, 'editar_proveedor.html', context)

        tipo_id = request.POST.get('tipo')
        proveedor.tipo = TipoProveedor.objects.filter(pk=tipo_id).first() if tipo_id else None
        proveedor.save()

        messages.success(request, 'Proveedor actualizado exitosamente')
        return redirect('proveedores:lista')

    return render(request, 'editar_proveedor.html', context)


@login_required
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        # Guardar la dirección para eliminarla después si existe
        direccion = proveedor.direccion
        proveedor.delete()
        if direccion:
            direccion.delete()
        messages.success(request, 'Proveedor eliminado exitosamente')
    return redirect('proveedores:lista')