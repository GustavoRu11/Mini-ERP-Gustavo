from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = request.POST.get('first_name', '')
            user.email = request.POST.get('email', '')
            user.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.first_name or user.username}! Tu cuenta fue creada exitosamente.')
            return redirect('home')
        else:
            messages.error(request, 'Por favor corregí los errores del formulario.')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})
