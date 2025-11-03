from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Proveedor, TipoProveedor


def lista_proveedores(request):
    """Muestra la lista de proveedores."""
    proveedores = Proveedor.objects.select_related('tipo').all().order_by('nombre')
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})


def crear_proveedor(request):
    """Formulario simple para crear un proveedor. Usa los campos del modelo (nombre, email, telefono)."""
    tipos = TipoProveedor.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        tipo_id = request.POST.get('tipo')

        if not nombre:
            messages.error(request, 'El nombre es obligatorio')
            return render(request, 'crear_proveedor.html', {'tipos': tipos})

        tipo = TipoProveedor.objects.filter(pk=tipo_id).first() if tipo_id else None

        Proveedor.objects.create(
            nombre=nombre,
            email=email or None,
            telefono=telefono or '',
            direccion=direccion or '',
            tipo=tipo
        )

        messages.success(request, 'Proveedor creado exitosamente')
        return redirect('proveedores:lista')

    return render(request, 'crear_proveedor.html', {'tipos': tipos})


def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)

    tipos = TipoProveedor.objects.all()

    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre') or proveedor.nombre
        proveedor.email = request.POST.get('email') or proveedor.email
        proveedor.telefono = request.POST.get('telefono') or proveedor.telefono
        proveedor.direccion = request.POST.get('direccion') or proveedor.direccion
        tipo_id = request.POST.get('tipo')
        proveedor.tipo = TipoProveedor.objects.filter(pk=tipo_id).first() if tipo_id else None
        proveedor.save()

        messages.success(request, 'Proveedor actualizado exitosamente')
        return redirect('proveedores:lista')

    return render(request, 'editar_proveedor.html', {'proveedor': proveedor, 'tipos': tipos})


def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, 'Proveedor eliminado exitosamente')
    return redirect('proveedores:lista')