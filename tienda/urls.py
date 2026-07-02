from django.urls import path
from . import views

urlpatterns = [
    # URLs Principales del Catálogo
    path('', views.home, name='home'),
    
    # CRUD de Productos
    path('producto/nuevo/', views.crear_producto, name='crear_producto'),
    path('producto/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('producto/reactivar/<int:id>/', views.reactivar_producto, name='reactivar_producto'),
    
    # CRUD y Vistas de Categorías
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categoria/<int:id>/', views.ver_categoria, name='ver_categoria'), 
    
    # CRUD de Proveedores
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/nuevo/', views.crear_proveedor, name='crear_proveedor'),
]