from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Proveedor


def lista_proveedores(request):
    """Muestra la lista de proveedores."""
    proveedores = Proveedor.objects.all().order_by('nombre')
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})


def crear_proveedor(request):
    """Formulario simple para crear un proveedor. Usa los campos del modelo (nombre, email, telefono)."""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        if not nombre:
            messages.error(request, 'El nombre es obligatorio')
            return render(request, 'crear_proveedor.html')

        Proveedor.objects.create(
            nombre=nombre,
            email=email or None,
            telefono=telefono or ''
        )

        messages.success(request, 'Proveedor creado exitosamente')
        return redirect('proveedores:lista')

    return render(request, 'crear_proveedor.html')


def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)

    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre') or proveedor.nombre
        proveedor.email = request.POST.get('email') or proveedor.email
        proveedor.telefono = request.POST.get('telefono') or proveedor.telefono
        proveedor.save()

        messages.success(request, 'Proveedor actualizado exitosamente')
        return redirect('proveedores:lista')

    return render(request, 'editar_proveedor.html', {'proveedor': proveedor})


def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        messages.success(request, 'Proveedor eliminado exitosamente')
    return redirect('proveedores:lista')