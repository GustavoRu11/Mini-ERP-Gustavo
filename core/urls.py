from django.contrib import admin
from django.urls import path, include
from proyectos import views as proyectos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyectos/', include('proyectos.urls')),
    path('colaboradores/', include('recursos.urls')),
    path('tareas/', proyectos_views.lista_tareas, name='lista_tareas'),
    path('tareas/crear/', proyectos_views.crear_tarea, name='crear_tarea'),
    path('', proyectos_views.lista_proyectos, name='home'),
]