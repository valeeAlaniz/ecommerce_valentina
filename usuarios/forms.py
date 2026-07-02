from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado

class UsuarioPersonalizadoForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta(UserCreationForm.Meta):
        model = UsuarioPersonalizado
        fields = UserCreationForm.Meta.fields + ('email', 'dni', 'telefono', 'foto_perfil')