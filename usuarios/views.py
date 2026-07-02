from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioPersonalizadoForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioPersonalizadoForm(request.POST, request.FILES) # FILES por si suben foto de perfil
        if form.is_valid():
            form.save()
            messages.success(request, "¡Cuenta creada con éxito! Ya podés iniciar sesión.")
            return redirect('login')
    else:
        form = UsuarioPersonalizadoForm()
    return render(request, 'registration/registrar.html', {'form': form})