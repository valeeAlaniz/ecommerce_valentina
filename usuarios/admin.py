from django.contrib import admin
from .models import UsuarioPersonalizado

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "dni", "telefono", "is_staff")
    search_fields = ("username", "dni", "email")