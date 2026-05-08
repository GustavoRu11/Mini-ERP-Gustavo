from django.contrib import admin
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'estado', 'fecha_inicio', 'fecha_fin', 'responsable']
    list_filter = ['estado']
    search_fields = ['nombre']

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'proyecto', 'asignado_a', 'fecha_limite', 'estado']
    list_filter = ['estado']
    search_fields = ['titulo']