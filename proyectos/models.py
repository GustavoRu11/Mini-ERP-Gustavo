from django.db import models
from recursos.models import Colaborador

class Proyecto(models.Model):
    ESTADO_CHOICES = [
        ('planificacion', 'En Planificación'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado'),
        ('en_riesgo', 'En Riesgo'),
        ('cancelado', 'Cancelado'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='planificacion'
    )
    responsable = models.ForeignKey(
        Colaborador,
        on_delete=models.SET_NULL,
        null=True,
        related_name='proyectos_responsable'
    )
    colaboradores = models.ManyToManyField(
        Colaborador,
        blank=True,
        related_name='proyectos_asignados'
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'


class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('vencida', 'Vencida'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name='tareas'
    )
    asignado_a = models.ForeignKey(
        Colaborador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    fecha_limite = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pendiente'
    )

    def __str__(self):
        return f"{self.titulo} - {self.proyecto.nombre}"

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'