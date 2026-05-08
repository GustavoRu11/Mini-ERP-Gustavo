from django.contrib import admin
from .models import Colaborador

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'puesto', 'disponibilidad', 'email']
    list_filter = ['disponibilidad']
    search_fields = ['nombre', 'puesto']