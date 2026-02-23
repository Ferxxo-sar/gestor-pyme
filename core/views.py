from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from productos.models import Producto
from proveedores.models import Proveedor
from ventas.models import Venta
from datetime import date

@login_required
def index(request):
    # Ventas del día
    ventas_hoy = Venta.objects.filter(fecha__date=date.today()).aggregate(
        total=Sum('total')
    )['total'] or 0
    
    # Total de productos
    total_productos = Producto.objects.count()
    
    # Productos con stock bajo (menor o igual al stock mínimo)
    stock_bajo = Producto.objects.filter(stock__lte=F('stock_minimo')).count()
    
    # Total de proveedores
    total_proveedores = Proveedor.objects.count()
    
    context = {
        'ventas_hoy': ventas_hoy,
        'total_productos': total_productos,
        'stock_bajo': stock_bajo,
        'total_proveedores': total_proveedores,
    }
    
    return render(request, 'core/index.html', context)
