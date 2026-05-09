from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Colaborador

def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'recursos/lista_colaboradores.html', {'colaboradores': colaboradores})

def crear_colaborador(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        puesto = request.POST.get('puesto')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        disponibilidad = request.POST.get('disponibilidad')
        Colaborador.objects.create(
            nombre=nombre,
            puesto=puesto,
            email=email,
            telefono=telefono,
            disponibilidad=disponibilidad
        )
        messages.success(request, 'Colaborador creado exitosamente.')
        return redirect('lista_colaboradores')
    return render(request, 'recursos/form_colaborador.html', {'accion': 'Crear'})

def editar_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.nombre = request.POST.get('nombre')
        colaborador.puesto = request.POST.get('puesto')
        colaborador.email = request.POST.get('email')
        colaborador.telefono = request.POST.get('telefono')
        colaborador.disponibilidad = request.POST.get('disponibilidad')
        colaborador.save()
        messages.success(request, 'Colaborador actualizado exitosamente.')
        return redirect('lista_colaboradores')
    return render(request, 'recursos/form_colaborador.html', {'accion': 'Editar', 'colaborador': colaborador})

def eliminar_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        messages.success(request, 'Colaborador eliminado exitosamente.')
        return redirect('lista_colaboradores')
    return render(request, 'recursos/confirmar_eliminar.html', {'objeto': colaborador, 'tipo': 'colaborador'})