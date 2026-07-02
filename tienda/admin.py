from django.contrib import admin
from .models import Categoria, Producto, Proveedor, Pedido, DetallePedido

# Registro simple para Categoría
admin.site.register(Categoria)

# Registro avanzado para Producto (Filtros, búsquedas y ordenamiento)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "categoria", "precio", "stock", "activo")
    list_filter = ("categoria", "activo") # Filtros en el lateral derecho
    search_fields = ("nombre", "descripcion") # Barra de búsqueda superior
    ordering = ("nombre",) # Ordenamiento alfabético por nombre

# Registro avanzado para Proveedor
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_empresa", "contacto", "email", "telefono")
    search_fields = ("nombre_empresa", "contacto")

# Registro avanzado para Pedido (Filtros por estado y fecha)
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "fecha", "estado", "total")
    list_filter = ("estado", "fecha")
    search_fields = ("usuario__username", "id") # Busca por el nombre del usuario o el número de pedido
    ordering = ("-fecha",) # Los pedidos más nuevos primero

# Registro avanzado para los Detalles de los Pedidos
@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "pedido", "producto", "cantidad", "precio_unitario")
    search_fields = ("producto__nombre", "pedido__id")