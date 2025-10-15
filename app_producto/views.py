from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

# Listar todos los productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

# Agregar producto
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria = request.POST['categoria']
        precio = request.POST['precio']
        stock = request.POST['stock']
        descripcion = request.POST['descripcion']
        
        Producto.objects.create(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            stock=stock,
            descripcion=descripcion
        )
        return redirect('listar_productos')
    
    return render(request, 'agregar_producto.html')

# Editar producto existente
def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.categoria = request.POST['categoria']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.descripcion = request.POST['descripcion']
        producto.save()
        return redirect('listar_productos')
    
    return render(request, 'editar_producto.html', {'producto': producto})

# Borrar producto
def borrar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    
    return render(request, 'borrar_producto.html', {'producto': producto})
