from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required

from .models import Producto, Categoria, Proveedor
from .forms import ProductoForm, CategoriaForm, ProveedorForm


# CRUD DE PRODUCTOS

#LISTAR PRODUCTOS (Catálogo general con funciones de Admin)
def home(request):
    # Si el usuario es administrador o dueño, ve absolutamente todo
    if request.user.is_authenticated and (request.user.is_superuser or request.user.has_perm('tienda.delete_producto')):
        productos = Producto.objects.all()
    else:
        # Si es un cliente común, solo ve los productos activos
        productos = Producto.objects.filter(activo=True)
        
    return render(request, "tienda/index.html", {"productos": productos})


#reactivar el producto desde la web
@login_required
@permission_required('tienda.delete_producto')
def reactivar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.activo = True # Volvemos a activar el producto
    producto.save()
    return redirect("home")

@login_required
@permission_required('tienda.add_producto')
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductoForm()
    return render(request, "tienda/crear_producto.html", {"form": form})

@login_required
@permission_required('tienda.change_producto')
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductoForm(instance=producto)
    return render(request, "tienda/editar_producto.html", {"form": form, "producto": producto})

@login_required
@permission_required('tienda.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.activo = False
        producto.save()
        return redirect("home")
    return render(request, "tienda/borrar_producto.html", {"producto": producto})

# CRUD Y VISTAS DE CATEGORÍAS 

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "tienda/listar_categorias.html", {"categorias": categorias})

#ver los productos de una categoría específica
def ver_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    productos = Producto.objects.filter(categoria=categoria, activo=True)
    return render(request, "tienda/ver_categoria.html", {"categoria": categoria, "productos": productos})

@login_required
@permission_required('tienda.add_categoria')
def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias') 
    else:
        form = CategoriaForm()
    return render(request, "tienda/crear_categoria.html", {"form": form})


# CRUD DE PROVEEDORES


@login_required
@permission_required('tienda.view_proveedor')
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "tienda/listar_proveedores.html", {"proveedores": proveedores})

@login_required
@permission_required('tienda.add_proveedor')
def crear_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, "tienda/crear_proveedor.html", {"form": form})