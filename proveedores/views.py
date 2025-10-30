from django.shortcuts import render

# Create your views here.
def nuevo_proveedor(request):

    return render(request, 'nuevo_proveedor.html')