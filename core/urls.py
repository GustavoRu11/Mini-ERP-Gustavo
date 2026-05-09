from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyectos/', include('proyectos.urls')),
    path('colaboradores/', include('recursos.urls')),
    path('tareas/', include('proyectos.urls')),
    path('', include('proyectos.urls')),
]