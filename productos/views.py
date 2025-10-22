from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Producto
from .forms import ProductoForm

#Vista para listar productos
def lista_productos(request):
    productos_list = Producto.objects.all().order_by('-fecha_ultima_modificacion')
    paginator = Paginator(productos_list, 10)
    page = request.GET.get('page', 1)
    try:
        productos = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        productos = paginator.page(1)
    return render(request, 'productos/product_list.html', {'productos': productos})

#Vista para crear un nuevo producto
def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos:lista')
    else:
        form = ProductoForm()
    return render(request, 'productos/product_form.html', {'form': form})

#Vista para editar un producto existente
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos:lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/product_form.html', {'form': form, 'accion': 'Editar'})

#Vista para eliminar un producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos:lista')
    return render(request, 'productos/product_confirm_delete.html', {'producto': producto})



