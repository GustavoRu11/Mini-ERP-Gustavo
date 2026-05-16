from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from proyectos import views as proyectos_views
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyectos/', include('proyectos.urls')),
    path('colaboradores/', include('recursos.urls')),
    path('tareas/', proyectos_views.lista_tareas, name='lista_tareas'),
    path('tareas/crear/', proyectos_views.crear_tarea, name='crear_tarea'),
    path('dashboard/', proyectos_views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', core_views.registro, name='registro'),
    path('', proyectos_views.dashboard, name='home'),
]