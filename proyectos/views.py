from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Proyecto, Tarea
from recursos.models import Colaborador

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})

def crear_proyecto(request):
    colaboradores = Colaborador.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        estado = request.POST.get('estado')
        responsable_id = request.POST.get('responsable')
        colaboradores_ids = request.POST.getlist('colaboradores')
        responsable = Colaborador.objects.get(pk=responsable_id) if responsable_id else None
        proyecto = Proyecto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            estado=estado,
            responsable=responsable
        )
        proyecto.colaboradores.set(colaboradores_ids)
        messages.success(request, 'Proyecto creado exitosamente.')
        return redirect('lista_proyectos')
    return render(request, 'proyectos/form_proyecto.html', {'accion': 'Crear', 'colaboradores': colaboradores})

def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    tareas = proyecto.tareas.all()
    return render(request, 'proyectos/detalle_proyecto.html', {'proyecto': proyecto, 'tareas': tareas})

def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    colaboradores = Colaborador.objects.all()
    if request.method == 'POST':
        proyecto.nombre = request.POST.get('nombre')
        proyecto.descripcion = request.POST.get('descripcion')
        proyecto.fecha_inicio = request.POST.get('fecha_inicio')
        proyecto.fecha_fin = request.POST.get('fecha_fin')
        proyecto.estado = request.POST.get('estado')
        responsable_id = request.POST.get('responsable')
        proyecto.responsable = Colaborador.objects.get(pk=responsable_id) if responsable_id else None
        proyecto.colaboradores.set(request.POST.getlist('colaboradores'))
        proyecto.save()
        messages.success(request, 'Proyecto actualizado exitosamente.')
        return redirect('lista_proyectos')
    return render(request, 'proyectos/form_proyecto.html', {'accion': 'Editar', 'proyecto': proyecto, 'colaboradores': colaboradores})

def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, 'Proyecto eliminado exitosamente.')
        return redirect('lista_proyectos')
    return render(request, 'proyectos/confirmar_eliminar.html', {'objeto': proyecto, 'tipo': 'proyecto'})

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'proyectos/lista_tareas.html', {'tareas': tareas})

def crear_tarea(request):
    proyectos = Proyecto.objects.all()
    colaboradores = Colaborador.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        proyecto_id = request.POST.get('proyecto')
        asignado_id = request.POST.get('asignado_a')
        fecha_limite = request.POST.get('fecha_limite')
        estado = request.POST.get('estado')
        Tarea.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            proyecto_id=proyecto_id,
            asignado_a_id=asignado_id if asignado_id else None,
            fecha_limite=fecha_limite,
            estado=estado
        )
        messages.success(request, 'Tarea creada exitosamente.')
        return redirect('lista_tareas')
    return render(request, 'proyectos/form_tarea.html', {'accion': 'Crear', 'proyectos': proyectos, 'colaboradores': colaboradores})