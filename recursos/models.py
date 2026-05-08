from django.db import models

class Colaborador(models.Model):
    DISPONIBILIDAD_CHOICES = [
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado'),
        ('vacaciones', 'En Vacaciones'),
    ]

    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    disponibilidad = models.CharField(
        max_length=20,
        choices=DISPONIBILIDAD_CHOICES,
        default='disponible'
    )
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.puesto}"

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'