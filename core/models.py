from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    ROL_CHOICES = [
        ('admin', 'Administrador'),
        ('gerente', 'Gerente'),
        ('colaborador', 'Colaborador'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='colaborador')

    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'