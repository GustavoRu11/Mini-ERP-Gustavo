from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count
from .models import Proyecto, Tarea
from recursos.models import Colaborador

def es_admin(user):
    try:
        return user.perfil.rol == 'admin'
    except:
        return False

def es_gerente_o_admin(user):
    try:
        return user.perfil.rol in ['admin', 'gerente']
    except:
        return False

@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})

@user_passes_test(es_gerente_o_admin, login_url='/login/')
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

@login_required
def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    tareas = proyecto.tareas.all()
    return render(request, 'proyectos/detalle_proyecto.html', {'proyecto': proyecto, 'tareas': tareas})

@user_passes_test(es_gerente_o_admin, login_url='/login/')
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

@user_passes_test(es_admin, login_url='/login/')
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, 'Proyecto eliminado exitosamente.')
        return redirect('lista_proyectos')
    return render(request, 'proyectos/confirmar_eliminar.html', {'objeto': proyecto, 'tipo': 'proyecto'})

@login_required
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'proyectos/lista_tareas.html', {'tareas': tareas})

@user_passes_test(es_gerente_o_admin, login_url='/login/')
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

@login_required
def dashboard(request):
    total_proyectos = Proyecto.objects.count()
    proyectos_en_progreso = Proyecto.objects.filter(estado='en_progreso').count()
    proyectos_completados = Proyecto.objects.filter(estado='completado').count()
    proyectos_en_riesgo = Proyecto.objects.filter(estado='en_riesgo').count()
    proyectos_planificacion = Proyecto.objects.filter(estado='planificacion').count()
    total_colaboradores = Colaborador.objects.count()
    colaboradores_disponibles = Colaborador.objects.filter(disponibilidad='disponible').count()
    colaboradores_ocupados = Colaborador.objects.filter(disponibilidad='ocupado').count()
    colaboradores_vacaciones = Colaborador.objects.filter(disponibilidad='vacaciones').count()
    total_tareas = Tarea.objects.count()
    tareas_completadas = Tarea.objects.filter(estado='completada').count()
    tareas_pendientes = Tarea.objects.filter(estado='pendiente').count()
    tareas_en_progreso = Tarea.objects.filter(estado='en_progreso').count()
    tareas_vencidas = Tarea.objects.filter(estado='vencida').count()
    proyectos_recientes = Proyecto.objects.order_by('-id')[:5]
    tareas_recientes = Tarea.objects.order_by('-id')[:5]
    context = {
        'total_proyectos': total_proyectos,
        'proyectos_en_progreso': proyectos_en_progreso,
        'proyectos_completados': proyectos_completados,
        'proyectos_en_riesgo': proyectos_en_riesgo,
        'proyectos_planificacion': proyectos_planificacion,
        'total_colaboradores': total_colaboradores,
        'colaboradores_disponibles': colaboradores_disponibles,
        'colaboradores_ocupados': colaboradores_ocupados,
        'colaboradores_vacaciones': colaboradores_vacaciones,
        'total_tareas': total_tareas,
        'tareas_completadas': tareas_completadas,
        'tareas_pendientes': tareas_pendientes,
        'tareas_en_progreso': tareas_en_progreso,
        'tareas_vencidas': tareas_vencidas,
        'proyectos_recientes': proyectos_recientes,
        'tareas_recientes': tareas_recientes,
    }
    return render(request, 'dashboard.html', context)