from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_colaboradores, name='lista_colaboradores'),
    path('crear/', views.crear_colaborador, name='crear_colaborador'),
    path('editar/<int:pk>/', views.editar_colaborador, name='editar_colaborador'),
    path('eliminar/<int:pk>/', views.eliminar_colaborador, name='eliminar_colaborador'),
]